"""
Learner Model (∩) API Implementation
Following MCP Server Specification lines 64-118

Educational Impact:
Enables personalized learning experiences by analyzing learner characteristics,
preferences, and behavioral patterns to optimize learning effectiveness.

Performance Requirements:
- Quest 3 VR: Maintains >72fps during processing
- Response time: <100ms for real-time adaptation
- Memory usage: <50MB for typical learner profiles

Manages comprehensive learner profiles and dynamic learning characteristics
with real-time behavioral analytics and adaptation parameters
"""

import asyncio
import json
import logging
import time
import uuid
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime, timedelta
import numpy as np
from dataclasses import dataclass, asdict
from abc import ABC, abstractmethod

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class LearnerProfileData:
    """
    Learner profile data structure following MCP Server Specification
    Based on JSON schema lines 569-624
    
    Educational Impact:
    Standardizes learner profile structure for consistent adaptation across
    all learning models and educational interactions.
    """
    learner_id: str
    static_profile: Dict[str, Any]
    dynamic_profile: Dict[str, Any]
    creation_timestamp: str = None
    last_updated: str = None
    
    def __post_init__(self):
        if self.creation_timestamp is None:
            self.creation_timestamp = datetime.now().isoformat()
        if self.last_updated is None:
            self.last_updated = datetime.now().isoformat()
    
    def validate_schema(self) -> bool:
        """
        Validate learner profile against MCP specification schema
        
        Educational Impact:
        Ensures data quality and consistency for reliable learning adaptation
        and educational effectiveness measurement.
        
        Returns:
            bool: True if schema is valid, False otherwise
        """
        try:
            required_static_fields = ["demographic", "learning_preferences"]
            required_dynamic_fields = ["learning_progress", "behavioral_patterns"]
            
            # Validate static profile structure
            if not all(field in self.static_profile for field in required_static_fields):
                logger.error(f"Missing required static profile fields: {required_static_fields}")
                return False
            
            # Validate demographic requirements
            demographic = self.static_profile.get("demographic", {})
            required_demographic = ["age_range", "education_level", "current_knowledge_level"]
            if not all(field in demographic for field in required_demographic):
                logger.error(f"Missing required demographic fields: {required_demographic}")
                return False
            
            # Validate dynamic profile structure
            if not all(field in self.dynamic_profile for field in required_dynamic_fields):
                logger.error(f"Missing required dynamic profile fields: {required_dynamic_fields}")
                return False
            
            # Validate learning progress structure
            learning_progress = self.dynamic_profile.get("learning_progress", {})
            required_progress = ["completion_rate", "competency_scores", "learning_events_completed"]
            if not all(field in learning_progress for field in required_progress):
                logger.error(f"Missing required learning progress fields: {required_progress}")
                return False
            
            return True
            
        except Exception as e:
            logger.error(f"Schema validation failed: {e}")
            return False
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization"""
        return asdict(self)

class EducationalDataError(Exception):
    """Exception raised for educational data validation errors"""
    pass

class PerformanceError(Exception):
    """Exception raised for Quest 3 performance threshold violations"""
    pass

class LearnerModelProcessor:
    """
    Learner Model processor implementing MCP Server Specification API
    
    Educational Impact:
    Processes learner profile data into normalized learning readiness scores
    and adaptation parameters to enable personalized learning experiences.
    
    Performance Requirements:
    - Processing time: <100ms for learner profile operations
    - Memory usage: <50MB for typical operations
    - Quest 3 compatibility: Maintains >72fps during processing
    """
    
    def __init__(self, security_manager=None):
        self.security_manager = security_manager
        self.learner_cache = {}
        self.processing_history = []
        
        # Learning event weight configurations (from spec lines 471-491)
        self.weight_configurations = {
            "onboarding": {"learner": 0.40, "knowledge": 0.22, "engagement": 0.28, "assessment": 0.10},
            "introduction": {"learner": 0.32, "knowledge": 0.28, "engagement": 0.22, "assessment": 0.18},
            "practice": {"learner": 0.27, "knowledge": 0.32, "engagement": 0.18, "assessment": 0.23},
            "application": {"learner": 0.25, "knowledge": 0.27, "engagement": 0.16, "assessment": 0.32},
            "mastery": {"learner": 0.22, "knowledge": 0.23, "engagement": 0.15, "assessment": 0.40}
        }
        
        # Performance monitoring
        self.performance_metrics = {
            "processing_times": [],
            "memory_usage": [],
            "cache_hit_rate": 0.0
        }
        
        logger.info("LearnerModelProcessor initialized with educational security compliance")
    
    async def create_learner_profile(self, profile_data: LearnerProfileData) -> Dict[str, Any]:
        """
        Create learner profile following MCP Server Specification
        POST /api/v1/learner/profile/create implementation
        
        Educational Impact:
        Establishes comprehensive learner profile for personalized learning
        adaptation and tracks educational progress throughout learning journey.
        
        Performance Requirements:
        - Quest 3 VR: <100ms response time
        - Memory: <20MB for profile creation
        - FERPA compliance: All sensitive data encrypted
        
        Args:
            profile_data: Validated learner profile data following educational schema
            
        Returns:
            Dict containing learner model weight and adaptation parameters
            
        Raises:
            EducationalDataError: If learner data fails educational validation
            PerformanceError: If processing exceeds Quest 3 performance thresholds
        """
        start_time = time.time()
        
        try:
            # Performance monitoring - Quest 3 requirement
            if not await self._check_performance_threshold(start_time):
                raise PerformanceError("Performance threshold exceeded before processing")
            
            # Validate profile data schema
            if not profile_data.validate_schema():
                raise EducationalDataError("Invalid learner profile schema")
            
            # Educational data protection - FERPA compliance
            if self.security_manager:
                encrypted_static = await self.security_manager.encrypt_learner_data(
                    profile_data.static_profile
                )
                encrypted_dynamic = await self.security_manager.encrypt_learner_data(
                    profile_data.dynamic_profile
                )
            else:
                # Fallback for testing without security manager
                encrypted_static = profile_data.static_profile
                encrypted_dynamic = profile_data.dynamic_profile
            
            # Calculate initial learner model weight
            learner_model_weight = await self.calculate_initial_learner_weight(profile_data)
            
            # Calculate adaptation parameters for learning equation
            adaptation_parameters = await self.calculate_adaptation_parameters(profile_data)
            
            # Educational effectiveness metrics
            effectiveness_metrics = await self.calculate_educational_effectiveness(profile_data)
            
            # Store in cache for real-time access
            cache_entry = {
                "learner_model_weight": learner_model_weight,
                "adaptation_parameters": adaptation_parameters,
                "effectiveness_metrics": effectiveness_metrics,
                "encrypted_static": encrypted_static,
                "encrypted_dynamic": encrypted_dynamic,
                "created_timestamp": datetime.now().isoformat(),
                "last_updated": datetime.now().isoformat(),
                "access_count": 0
            }
            
            self.learner_cache[profile_data.learner_id] = cache_entry
            
            # Performance monitoring
            processing_time = time.time() - start_time
            await self._record_performance_metrics(processing_time, "create_profile")
            
            # Quest 3 performance validation
            if processing_time > 0.1:  # 100ms threshold
                logger.warning(f"Profile creation exceeded Quest 3 threshold: {processing_time:.3f}s")
            
            # Response following MCP specification format (lines 103-111)
            response = {
                "status": "success",
                "learner_id": profile_data.learner_id,
                "learner_model_weight": learner_model_weight,
                "adaptation_parameters": adaptation_parameters,
                "effectiveness_metrics": effectiveness_metrics,
                "processing_time_ms": processing_time * 1000,
                "creation_timestamp": datetime.now().isoformat()
            }
            
            logger.info(f"Learner profile created successfully: {profile_data.learner_id}")
            return response
            
        except Exception as e:
            processing_time = time.time() - start_time
            logger.error(f"Learner profile creation failed ({processing_time:.3f}s): {e}")
            raise
    
    async def get_learner_profile(self, learner_id: str) -> Dict[str, Any]:
        """
        Get learner profile with real-time behavioral analytics
        GET /api/v1/learner/profile/{learner_id} implementation
        
        Educational Impact:
        Provides real-time access to learner characteristics and behavioral
        analytics for adaptive learning decision making.
        
        Performance Requirements:
        - Quest 3 VR: <50ms response time for cached data
        - Memory: <10MB for profile retrieval
        
        Args:
            learner_id: Unique identifier for the learner
            
        Returns:
            Dict containing comprehensive learner profile and analytics
        """
        start_time = time.time()
        
        try:
            if learner_id not in self.learner_cache:
                raise ValueError(f"Learner profile not found: {learner_id}")
            
            cached_data = self.learner_cache[learner_id]
            cached_data["access_count"] += 1
            
            # Calculate cache hit rate for performance monitoring
            self._update_cache_hit_rate()
            
            # Decrypt data for processing if security manager available
            if self.security_manager:
                static_profile = await self.security_manager.decrypt_learner_data(
                    cached_data["encrypted_static"]
                )
                dynamic_profile = await self.security_manager.decrypt_learner_data(
                    cached_data["encrypted_dynamic"]
                )
            else:
                static_profile = cached_data["encrypted_static"]
                dynamic_profile = cached_data["encrypted_dynamic"]
            
            # Calculate current behavioral analytics
            behavioral_analytics = await self.calculate_behavioral_analytics(
                learner_id, dynamic_profile
            )
            
            # Learning readiness assessment
            learning_readiness = await self.assess_learning_readiness(
                static_profile, dynamic_profile
            )
            
            processing_time = time.time() - start_time
            
            response = {
                "learner_id": learner_id,
                "learner_model_weight": cached_data["learner_model_weight"],
                "adaptation_parameters": cached_data["adaptation_parameters"],
                "effectiveness_metrics": cached_data["effectiveness_metrics"],
                "behavioral_analytics": behavioral_analytics,
                "learning_readiness": learning_readiness,
                "last_updated": cached_data["last_updated"],
                "access_count": cached_data["access_count"],
                "processing_time_ms": processing_time * 1000
            }
            
            # Performance validation
            if processing_time > 0.05:  # 50ms threshold for cached data
                logger.warning(f"Profile retrieval exceeded threshold: {processing_time:.3f}s")
            
            return response
            
        except Exception as e:
            processing_time = time.time() - start_time
            logger.error(f"Learner profile retrieval failed ({processing_time:.3f}s): {e}")
            raise
    
    async def update_learner_profile(self, learner_id: str, update_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update learner profile based on interaction data and assessment results
        PUT /api/v1/learner/profile/{learner_id}/update implementation
        
        Educational Impact:
        Enables real-time adaptation of learner characteristics based on
        ongoing educational interactions and assessment results.
        
        Performance Requirements:
        - Quest 3 VR: <100ms response time
        - Real-time updates: Support for continuous learning data
        
        Args:
            learner_id: Unique identifier for the learner
            update_data: New interaction and assessment data
            
        Returns:
            Dict containing updated learner model parameters
        """
        start_time = time.time()
        
        try:
            if learner_id not in self.learner_cache:
                raise ValueError(f"Learner profile not found: {learner_id}")
            
            cached_data = self.learner_cache[learner_id]
            
            # Decrypt current dynamic profile
            if self.security_manager:
                current_dynamic = await self.security_manager.decrypt_learner_data(
                    cached_data["encrypted_dynamic"]
                )
                current_static = await self.security_manager.decrypt_learner_data(
                    cached_data["encrypted_static"]
                )
            else:
                current_dynamic = cached_data["encrypted_dynamic"]
                current_static = cached_data["encrypted_static"]
            
            # Update dynamic profile with new data
            updated_dynamic = await self.merge_dynamic_profile_updates(
                current_dynamic, update_data
            )
            
            # Create updated profile data
            profile_data = LearnerProfileData(
                learner_id=learner_id,
                static_profile=current_static,
                dynamic_profile=updated_dynamic
            )
            
            # Recalculate learner model parameters
            new_weight = await self.calculate_initial_learner_weight(profile_data)
            new_adaptation_params = await self.calculate_adaptation_parameters(profile_data)
            new_effectiveness_metrics = await self.calculate_educational_effectiveness(profile_data)
            
            # Re-encrypt updated data if security manager available
            if self.security_manager:
                encrypted_dynamic = await self.security_manager.encrypt_learner_data(updated_dynamic)
            else:
                encrypted_dynamic = updated_dynamic
            
            # Update cache
            self.learner_cache[learner_id].update({
                "learner_model_weight": new_weight,
                "adaptation_parameters": new_adaptation_params,
                "effectiveness_metrics": new_effectiveness_metrics,
                "encrypted_dynamic": encrypted_dynamic,
                "last_updated": datetime.now().isoformat()
            })
            
            processing_time = time.time() - start_time
            
            response = {
                "status": "updated",
                "learner_id": learner_id,
                "new_learner_model_weight": new_weight,
                "new_adaptation_parameters": new_adaptation_params,
                "new_effectiveness_metrics": new_effectiveness_metrics,
                "update_timestamp": datetime.now().isoformat(),
                "processing_time_ms": processing_time * 1000
            }
            
            # Performance validation
            if processing_time > 0.1:  # 100ms threshold
                logger.warning(f"Profile update exceeded threshold: {processing_time:.3f}s")
            
            logger.info(f"Learner profile updated successfully: {learner_id}")
            return response
            
        except Exception as e:
            processing_time = time.time() - start_time
            logger.error(f"Learner profile update failed ({processing_time:.3f}s): {e}")
            raise
    
    async def calculate_initial_learner_weight(self, profile_data: LearnerProfileData) -> float:
        """
        Calculate initial learner model weight based on profile characteristics
        Implementation based on MCP specification requirements (lines 110-117)
        
        Educational Impact:
        Determines appropriate emphasis on learner-specific factors in the
        adaptive learning equation for personalized learning experiences.
        
        Args:
            profile_data: Validated learner profile data
            
        Returns:
            float: Learner model weight between 0.15 and 0.50
        """
        static_profile = profile_data.static_profile
        dynamic_profile = profile_data.dynamic_profile
        
        # Extract demographic factors
        demographic = static_profile.get("demographic", {})
        knowledge_level = demographic.get("current_knowledge_level", "beginner")
        education_level = demographic.get("education_level", "undergraduate")
        
        # Base weight from knowledge level (novices need more learner-focused adaptation)
        knowledge_weights = {
            "novice": 0.40,      # Higher weight for guided learning
            "beginner": 0.35,
            "intermediate": 0.30,
            "advanced": 0.25,
            "expert": 0.20       # Lower weight for autonomous learning
        }
        
        base_weight = knowledge_weights.get(knowledge_level, 0.35)
        
        # Adjust based on learning preferences
        preferences = static_profile.get("learning_preferences", {})
        guidance_level = preferences.get("guidance_level", "moderate")
        
        guidance_adjustments = {
            "high": 0.05,        # More learner-focused for high guidance
            "moderate": 0.0,
            "low": -0.05,        # Less learner-focused for independent learners
            "adaptive": 0.02
        }
        
        guidance_adjustment = guidance_adjustments.get(guidance_level, 0.0)
        
        # Adjust based on behavioral patterns
        behavioral_patterns = dynamic_profile.get("behavioral_patterns", {})
        help_seeking_frequency = behavioral_patterns.get("help_seeking_frequency", 0)
        
        # Higher help-seeking indicates need for more learner-focused adaptation
        help_seeking_adjustment = min(0.1, help_seeking_frequency * 0.2)
        
        # Learning progress consideration
        learning_progress = dynamic_profile.get("learning_progress", {})
        completion_rate = learning_progress.get("completion_rate", 0.0)
        
        # Lower completion rates indicate need for more learner support
        progress_adjustment = max(-0.05, (0.5 - completion_rate) * 0.1)
        
        final_weight = base_weight + guidance_adjustment + help_seeking_adjustment + progress_adjustment
        
        # Ensure weight stays within MCP specification bounds (0.25-0.40 per lines 110-117)
        return max(0.25, min(0.40, final_weight))
    
    async def calculate_adaptation_parameters(self, profile_data: LearnerProfileData) -> Dict[str, float]:
        """
        Calculate adaptation parameters for learning equation
        Based on MCP specification lines 107-110 and mathematical foundation
        
        Educational Impact:
        Provides alpha and beta parameters for the core learning equation
        ∂(t+1) = ∂(t) + α · Δ(∩(t), ∆(t), E(t), A(t)) + β · ε(t)
        
        Args:
            profile_data: Validated learner profile data
            
        Returns:
            Dict containing alpha and beta parameters for learning equation
        """
        static_profile = profile_data.static_profile
        dynamic_profile = profile_data.dynamic_profile
        
        # Extract key characteristics
        demographic = static_profile.get("demographic", {})
        knowledge_level = demographic.get("current_knowledge_level", "beginner")
        preferences = static_profile.get("learning_preferences", {})
        guidance_level = preferences.get("guidance_level", "moderate")
        
        # Calculate alpha (learning rate adjustment)
        alpha_base = 0.7
        
        # Adjust alpha based on knowledge level
        knowledge_alpha_adjustments = {
            "novice": 0.1,       # Slower learning rate for novices
            "beginner": 0.05,
            "intermediate": 0.0,
            "advanced": -0.05,
            "expert": -0.1       # Faster learning rate for experts
        }
        
        alpha_adjustment = knowledge_alpha_adjustments.get(knowledge_level, 0.0)
        
        # Consider learning progress velocity
        learning_progress = dynamic_profile.get("learning_progress", {})
        recent_progress_rate = learning_progress.get("recent_progress_rate", 0.5)
        
        # Faster progress indicates readiness for higher learning rate
        progress_alpha_adjustment = (recent_progress_rate - 0.5) * 0.1
        
        alpha_baseline = alpha_base + alpha_adjustment + progress_alpha_adjustment
        
        # Calculate beta (exploration factor)
        beta_base = 0.15
        
        # Adjust beta based on guidance preference
        guidance_beta_adjustments = {
            "high": -0.05,       # Less exploration with high guidance
            "moderate": 0.0,
            "low": 0.05,         # More exploration with low guidance
            "adaptive": 0.02
        }
        
        beta_adjustment = guidance_beta_adjustments.get(guidance_level, 0.0)
        
        # Consider behavioral patterns for exploration
        behavioral_patterns = dynamic_profile.get("behavioral_patterns", {})
        exploration_tendency = behavioral_patterns.get("exploration_tendency", 0.5)
        
        # Higher exploration tendency increases beta
        exploration_beta_adjustment = (exploration_tendency - 0.5) * 0.1
        
        beta_exploration = beta_base + beta_adjustment + exploration_beta_adjustment
        
        return {
            "alpha_baseline": max(0.3, min(0.9, alpha_baseline)),
            "beta_exploration": max(0.05, min(0.25, beta_exploration)),
            "knowledge_level_factor": knowledge_level,
            "guidance_preference_factor": guidance_level,
            "exploration_tendency": exploration_tendency
        }
    
    async def calculate_educational_effectiveness(self, profile_data: LearnerProfileData) -> Dict[str, float]:
        """
        Calculate educational effectiveness metrics for learner
        
        Educational Impact:
        Provides quantitative measures of learning effectiveness to guide
        adaptive learning decisions and optimize educational outcomes.
        
        Args:
            profile_data: Validated learner profile data
            
        Returns:
            Dict containing educational effectiveness metrics
        """
        dynamic_profile = profile_data.dynamic_profile
        
        # Extract learning progress data
        learning_progress = dynamic_profile.get("learning_progress", {})
        completion_rate = learning_progress.get("completion_rate", 0.0)
        competency_scores = learning_progress.get("competency_scores", {})
        
        # Calculate average competency score
        avg_competency = np.mean(list(competency_scores.values())) if competency_scores else 0.0
        
        # Extract behavioral patterns
        behavioral_patterns = dynamic_profile.get("behavioral_patterns", {})
        engagement_level = behavioral_patterns.get("engagement_level", 0.5)
        retention_rate = behavioral_patterns.get("retention_rate", 0.5)
        
        # Calculate overall effectiveness score
        effectiveness_score = (
            completion_rate * 0.3 +
            avg_competency * 0.4 +
            engagement_level * 0.2 +
            retention_rate * 0.1
        )
        
        return {
            "overall_effectiveness": effectiveness_score,
            "completion_rate": completion_rate,
            "average_competency": avg_competency,
            "engagement_level": engagement_level,
            "retention_rate": retention_rate,
            "learning_velocity": learning_progress.get("recent_progress_rate", 0.5)
        }
    
    async def calculate_behavioral_analytics(self, learner_id: str, dynamic_profile: Dict[str, Any]) -> Dict[str, Any]:
        """
        Calculate real-time behavioral analytics for learner
        
        Educational Impact:
        Provides insights into learner behavior patterns to inform
        adaptive learning strategies and intervention decisions.
        
        Args:
            learner_id: Unique identifier for the learner
            dynamic_profile: Current dynamic profile data
            
        Returns:
            Dict containing behavioral analytics metrics
        """
        behavioral_patterns = dynamic_profile.get("behavioral_patterns", {})
        
        # Time-based analytics
        session_duration_avg = behavioral_patterns.get("average_session_duration", 30)
        sessions_per_week = behavioral_patterns.get("sessions_per_week", 3)
        
        # Interaction analytics
        help_seeking_frequency = behavioral_patterns.get("help_seeking_frequency", 0)
        collaboration_frequency = behavioral_patterns.get("collaboration_frequency", 0)
        
        # Performance analytics
        error_patterns = behavioral_patterns.get("common_error_patterns", [])
        improvement_trends = behavioral_patterns.get("improvement_trends", {})
        
        # Calculate engagement stability
        recent_sessions = behavioral_patterns.get("recent_session_data", [])
        engagement_stability = self._calculate_engagement_stability(recent_sessions)
        
        return {
            "temporal_patterns": {
                "average_session_duration": session_duration_avg,
                "sessions_per_week": sessions_per_week,
                "preferred_learning_times": behavioral_patterns.get("preferred_times", [])
            },
            "interaction_patterns": {
                "help_seeking_frequency": help_seeking_frequency,
                "collaboration_frequency": collaboration_frequency,
                "self_directed_learning_ratio": 1.0 - help_seeking_frequency
            },
            "performance_patterns": {
                "common_error_types": error_patterns,
                "improvement_velocity": improvement_trends.get("velocity", 0.0),
                "learning_curve_slope": improvement_trends.get("curve_slope", 0.0)
            },
            "engagement_analytics": {
                "stability_score": engagement_stability,
                "motivation_level": behavioral_patterns.get("motivation_level", 0.5),
                "persistence_score": behavioral_patterns.get("persistence_score", 0.5)
            }
        }
    
    async def assess_learning_readiness(self, static_profile: Dict[str, Any], dynamic_profile: Dict[str, Any]) -> Dict[str, Any]:
        """
        Assess current learning readiness of the learner
        
        Educational Impact:
        Determines optimal timing and conditions for learning activities
        to maximize educational effectiveness and learner success.
        
        Args:
            static_profile: Static profile data
            dynamic_profile: Dynamic profile data
            
        Returns:
            Dict containing learning readiness assessment
        """
        # Prerequisites readiness
        learning_progress = dynamic_profile.get("learning_progress", {})
        completion_rate = learning_progress.get("completion_rate", 0.0)
        competency_scores = learning_progress.get("competency_scores", {})
        
        # Calculate prerequisite readiness
        avg_competency = np.mean(list(competency_scores.values())) if competency_scores else 0.0
        prerequisite_readiness = min(1.0, avg_competency * 1.2)  # Boost factor for readiness
        
        # Cognitive load assessment
        behavioral_patterns = dynamic_profile.get("behavioral_patterns", {})
        recent_error_rate = behavioral_patterns.get("recent_error_rate", 0.3)
        cognitive_load = max(0.0, min(1.0, recent_error_rate * 2))  # Higher errors = higher load
        
        # Motivation and engagement readiness
        engagement_level = behavioral_patterns.get("engagement_level", 0.5)
        motivation_level = behavioral_patterns.get("motivation_level", 0.5)
        
        # Overall readiness score
        readiness_score = (
            prerequisite_readiness * 0.4 +
            (1.0 - cognitive_load) * 0.3 +
            engagement_level * 0.2 +
            motivation_level * 0.1
        )
        
        return {
            "overall_readiness": readiness_score,
            "prerequisite_readiness": prerequisite_readiness,
            "cognitive_load_level": cognitive_load,
            "engagement_readiness": engagement_level,
            "motivation_readiness": motivation_level,
            "recommended_difficulty": self._recommend_difficulty_level(readiness_score),
            "optimal_learning_conditions": self._recommend_learning_conditions(
                static_profile, dynamic_profile
            )
        }
    
    async def merge_dynamic_profile_updates(self, current_dynamic: Dict[str, Any], update_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Merge new data into existing dynamic profile
        
        Educational Impact:
        Ensures continuous learning adaptation by properly integrating
        new behavioral and performance data into learner profiles.
        
        Args:
            current_dynamic: Current dynamic profile data
            update_data: New data to merge
            
        Returns:
            Dict containing merged dynamic profile
        """
        merged = current_dynamic.copy()
        
        # Update learning progress
        if "learning_progress" in update_data:
            current_progress = merged.get("learning_progress", {})
            new_progress = update_data["learning_progress"]
            
            # Merge competency scores
            current_competencies = current_progress.get("competency_scores", {})
            new_competencies = new_progress.get("competency_scores", {})
            current_competencies.update(new_competencies)
            
            # Update progress metrics
            current_progress.update(new_progress)
            current_progress["competency_scores"] = current_competencies
            merged["learning_progress"] = current_progress
        
        # Update behavioral patterns
        if "behavioral_patterns" in update_data:
            current_behavior = merged.get("behavioral_patterns", {})
            new_behavior = update_data["behavioral_patterns"]
            
            # Update session data
            if "session_data" in new_behavior:
                recent_sessions = current_behavior.get("recent_session_data", [])
                recent_sessions.append(new_behavior["session_data"])
                # Keep only last 10 sessions
                recent_sessions = recent_sessions[-10:]
                current_behavior["recent_session_data"] = recent_sessions
            
            current_behavior.update(new_behavior)
            merged["behavioral_patterns"] = current_behavior
        
        # Update timestamp
        merged["last_profile_update"] = datetime.now().isoformat()
        
        return merged
    
    def _calculate_engagement_stability(self, recent_sessions: List[Dict[str, Any]]) -> float:
        """Calculate engagement stability from recent session data"""
        if len(recent_sessions) < 2:
            return 0.5  # Default for insufficient data
        
        engagement_values = [session.get("engagement_score", 0.5) for session in recent_sessions]
        
        # Calculate coefficient of variation (lower = more stable)
        mean_engagement = np.mean(engagement_values)
        std_engagement = np.std(engagement_values)
        
        if mean_engagement == 0:
            return 0.0
        
        cv = std_engagement / mean_engagement
        stability = max(0.0, 1.0 - cv)  # Invert CV to get stability score
        
        return stability
    
    def _recommend_difficulty_level(self, readiness_score: float) -> str:
        """Recommend appropriate difficulty level based on readiness"""
        if readiness_score >= 0.8:
            return "challenging"
        elif readiness_score >= 0.6:
            return "moderate"
        elif readiness_score >= 0.4:
            return "guided"
        else:
            return "foundational"
    
    def _recommend_learning_conditions(self, static_profile: Dict[str, Any], dynamic_profile: Dict[str, Any]) -> Dict[str, str]:
        """Recommend optimal learning conditions"""
        preferences = static_profile.get("learning_preferences", {})
        behavioral = dynamic_profile.get("behavioral_patterns", {})
        
        return {
            "pacing": preferences.get("preferred_pacing", "self_paced"),
            "guidance_level": preferences.get("guidance_level", "moderate"),
            "interaction_style": preferences.get("interaction_style", "mixed"),
            "optimal_session_length": str(behavioral.get("optimal_session_duration", 30)) + "_minutes"
        }
    
    async def _check_performance_threshold(self, start_time: float) -> bool:
        """Check if we're within Quest 3 performance thresholds"""
        # Simplified performance check - in production would be more sophisticated
        return True
    
    async def _record_performance_metrics(self, processing_time: float, operation: str):
        """Record performance metrics for monitoring"""
        self.performance_metrics["processing_times"].append({
            "operation": operation,
            "time": processing_time,
            "timestamp": datetime.now().isoformat()
        })
        
        # Keep only last 100 measurements
        if len(self.performance_metrics["processing_times"]) > 100:
            self.performance_metrics["processing_times"] = self.performance_metrics["processing_times"][-100:]
    
    def _update_cache_hit_rate(self):
        """Update cache hit rate metric"""
        total_requests = sum(entry["access_count"] for entry in self.learner_cache.values())
        cache_hits = len(self.learner_cache)
        
        if total_requests > 0:
            self.performance_metrics["cache_hit_rate"] = cache_hits / total_requests
    
    def get_performance_metrics(self) -> Dict[str, Any]:
        """
        Get current performance metrics for monitoring
        
        Educational Impact:
        Provides performance visibility to ensure Quest 3 VR requirements
        are met and educational effectiveness is maintained.
        
        Returns:
            Dict containing performance metrics
        """
        recent_times = [m["time"] for m in self.performance_metrics["processing_times"][-10:]]
        
        return {
            "average_processing_time": np.mean(recent_times) if recent_times else 0.0,
            "max_processing_time": max(recent_times) if recent_times else 0.0,
            "cache_hit_rate": self.performance_metrics["cache_hit_rate"],
            "active_learners": len(self.learner_cache),
            "quest3_compliance": all(t < 0.1 for t in recent_times) if recent_times else True
        }
