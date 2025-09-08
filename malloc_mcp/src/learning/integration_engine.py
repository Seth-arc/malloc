"""
Learning Integration Engine Implementation
Following MCP Server Specification lines 400-492

Real-time implementation of the learning adaptation equation:
∂(t+1) = ∂(t) + α · Δ(∩(t), ∆(t), E(t), A(t)) + β · ε(t)

Educational Impact:
This engine enables real-time adaptive learning by mathematically combining
learner profile, knowledge state, engagement level, and assessment results
to make optimal learning progression decisions.

Performance Requirements:
- Quest 3 VR: Computation time <10ms
- Response time: <100ms total processing
- Memory usage: <50MB for integration operations
"""

import asyncio
import logging
import json
import random
import numpy as np
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime, timedelta
from dataclasses import dataclass, field
import math
from enum import Enum

# Import learning models
from .learner_model import LearnerModelManager
from .knowledge_model import KnowledgeModelManager
from .engagement_model import EngagementModelManager
from .assessment_model import AssessmentModelManager
from .transition_model import TransitionModelManager

@dataclass
class LearningModelInputs:
    """
    Structure for learning model inputs to integration equation
    
    Educational Impact:
    Standardizes data flow between all learning models for consistent
    mathematical computation and educational decision-making.
    """
    learner_model_data: Dict[str, Any]      # ∩(t) - Learner profile data
    knowledge_model_data: Dict[str, Any]    # ∆(t) - Knowledge state data
    engagement_model_data: Dict[str, Any]   # E(t) - Engagement tracking data
    assessment_model_data: Dict[str, Any]   # A(t) - Assessment results data
    learning_event: str = "practice"        # Current learning event type
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    
    def __post_init__(self):
        """Validate and normalize input data"""
        if not self.learner_model_data:
            self.learner_model_data = {}
        if not self.knowledge_model_data:
            self.knowledge_model_data = {}
        if not self.engagement_model_data:
            self.engagement_model_data = {}
        if not self.assessment_model_data:
            self.assessment_model_data = {}

class LearningEventType(Enum):
    """
    Learning event types with associated weight configurations
    Following MCP specification lines 471-491
    """
    ONBOARDING = "onboarding"
    INTRODUCTION = "introduction"
    PRACTICE = "practice"
    APPLICATION = "application"
    MASTERY = "mastery"

@dataclass
class IntegrationResult:
    """
    Result structure for learning integration computation
    
    Educational Impact:
    Provides comprehensive feedback for learning progression decisions
    and educational analytics.
    """
    learner_id: str
    transition_state: float
    transition_decision: Dict[str, Any]
    integration_result: float
    stochastic_element: float
    computation_time_ms: float
    learning_event: str
    model_weights: Dict[str, float]
    equation_parameters: Dict[str, float]
    timestamp: str
    confidence_score: float
    recommended_action: str
    reasoning: str

class LearningIntegrationEngine:
    """
    Real-time implementation of the learning adaptation equation
    Following MCP Server Specification lines 407-442
    
    Educational Impact:
    Enables personalized learning experiences through mathematical modeling
    of learner progress, knowledge mastery, engagement patterns, and 
    assessment performance.
    
    Performance Requirements:
    - Quest 3 VR: Maintain >72fps during operations
    - Integration computation: <10ms as per spec line 678
    - Memory usage: <50MB for integration engine operations
    - Response latency: <100ms for learning model updates
    """
    
    def __init__(self):
        """Initialize the Learning Integration Engine"""
        
        # Store current transition states for each learner
        self.current_states: Dict[str, Dict[str, Any]] = {}
        
        # Model weights - dynamically adjusted based on learning event
        # From MCP specification lines 471-491
        self.weight_configurations = {
            LearningEventType.ONBOARDING.value: {
                "learner": 0.40, "knowledge": 0.22, "engagement": 0.28, "assessment": 0.10
            },
            LearningEventType.INTRODUCTION.value: {
                "learner": 0.32, "knowledge": 0.28, "engagement": 0.22, "assessment": 0.18
            },
            LearningEventType.PRACTICE.value: {
                "learner": 0.27, "knowledge": 0.32, "engagement": 0.18, "assessment": 0.23
            },
            LearningEventType.APPLICATION.value: {
                "learner": 0.25, "knowledge": 0.27, "engagement": 0.16, "assessment": 0.32
            },
            LearningEventType.MASTERY.value: {
                "learner": 0.22, "knowledge": 0.23, "engagement": 0.15, "assessment": 0.40
            }
        }
        
        # Current active model weights (default to practice)
        self.current_model_weights = self.weight_configurations[LearningEventType.PRACTICE.value]
        
        # Learning equation parameters
        # α: Adaptive learning rate (0.0-1.0)
        # β: Exploration factor (0.0-0.3)
        self.alpha = 0.7   # Adaptive learning rate
        self.beta = 0.15   # Exploration factor
        
        # Processing history for analysis and optimization
        self.computation_history: List[Dict[str, Any]] = []
        
        # Performance monitoring
        self.computation_times: List[float] = []
        self.memory_usage_history: List[float] = []
        
        # Initialize learning model managers
        self.learner_manager = LearnerModelManager()
        self.knowledge_manager = KnowledgeModelManager()
        self.engagement_manager = EngagementModelManager()
        self.assessment_manager = AssessmentModelManager()
        self.transition_manager = TransitionModelManager()
        
        # Performance thresholds
        self.MAX_COMPUTATION_TIME_MS = 10.0  # Quest 3 VR requirement
        self.MAX_MEMORY_USAGE_MB = 50.0      # Memory constraint
        
        # Set up logging
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
    
    async def compute_transition_state(
        self, 
        learner_id: str, 
        model_inputs: LearningModelInputs,
        learning_event: str = "practice"
    ) -> IntegrationResult:
        """
        Implements: ∂(t+1) = ∂(t) + α · Δ(∩(t), ∆(t), E(t), A(t)) + β · ε(t)
        Following MCP Server Specification lines 422-442
        
        Educational Impact:
        Computes optimal learning progression based on comprehensive learner analysis,
        enabling personalized learning paths and adaptive educational experiences.
        
        Performance Requirements:
        - Computation time: <10ms for Quest 3 VR compliance
        - Memory efficiency: Minimal allocation during computation
        - Real-time processing: Supports continuous adaptation
        
        Args:
            learner_id: Unique identifier for the learner
            model_inputs: Structured input data from all learning models
            learning_event: Current learning event (onboarding, practice, etc.)
            
        Returns:
            IntegrationResult with transition state and educational decisions
            
        Raises:
            Exception: If computation fails or exceeds performance thresholds
        """
        computation_start_time = datetime.now()
        
        try:
            # Validate input parameters
            if not learner_id:
                raise ValueError("learner_id is required for transition computation")
            
            # Adjust weights for current learning event
            await self._adjust_weights_for_learning_event(learning_event)
            
            # Get current transition state ∂(t)
            current_transition = await self._get_current_transition_state(learner_id)
            
            # Compute integration function Δ(∩(t), ∆(t), E(t), A(t))
            integration_result = await self._compute_integration_function(model_inputs)
            
            # Generate stochastic element ε(t)
            stochastic_element = await self._generate_stochastic_element()
            
            # Compute next state: ∂(t+1) = ∂(t) + α · Δ + β · ε
            next_transition = (
                current_transition + 
                self.alpha * integration_result + 
                self.beta * stochastic_element
            )
            
            # Normalize to valid range [0, 1]
            next_transition = max(0.0, min(1.0, next_transition))
            
            # Update current state
            self.current_states[learner_id] = {
                "transition_state": next_transition,
                "last_updated": datetime.now().isoformat(),
                "learning_event": learning_event,
                "integration_result": integration_result,
                "stochastic_element": stochastic_element
            }
            
            # Interpret transition decision
            transition_decision = await self._interpret_transition_decision(
                learner_id, next_transition, model_inputs
            )
            
            # Calculate computation time
            computation_time = (datetime.now() - computation_start_time).total_seconds() * 1000
            self.computation_times.append(computation_time)
            
            # Store computation history
            await self._store_computation_history(
                learner_id, model_inputs, integration_result, 
                stochastic_element, next_transition, computation_time
            )
            
            # Validate performance requirement (<10ms from spec line 678)
            if computation_time > self.MAX_COMPUTATION_TIME_MS:
                self.logger.warning(
                    f"Integration computation exceeded {self.MAX_COMPUTATION_TIME_MS}ms limit: "
                    f"{computation_time:.2f}ms for learner {learner_id}"
                )
            
            # Create comprehensive result
            result = IntegrationResult(
                learner_id=learner_id,
                transition_state=next_transition,
                transition_decision=transition_decision,
                integration_result=integration_result,
                stochastic_element=stochastic_element,
                computation_time_ms=computation_time,
                learning_event=learning_event,
                model_weights=self.current_model_weights.copy(),
                equation_parameters={
                    "alpha": self.alpha,
                    "beta": self.beta
                },
                timestamp=datetime.now().isoformat(),
                confidence_score=transition_decision.get("confidence_score", 0.5),
                recommended_action=transition_decision.get("recommended_action", "continue_current_event"),
                reasoning=transition_decision.get("reasoning", "Standard progression")
            )
            
            self.logger.info(
                f"Computed transition state for learner {learner_id}: "
                f"{next_transition:.3f} in {computation_time:.2f}ms"
            )
            
            return result
            
        except Exception as e:
            computation_time = (datetime.now() - computation_start_time).total_seconds() * 1000
            self.logger.error(f"Integration computation failed for learner {learner_id}: {e}")
            
            # Return error state with safe defaults
            return IntegrationResult(
                learner_id=learner_id,
                transition_state=0.5,  # Neutral state
                transition_decision={
                    "recommended_action": "maintain_current_state",
                    "confidence_score": 0.0,
                    "reasoning": f"Computation error: {str(e)}",
                    "next_learning_event": learning_event
                },
                integration_result=0.0,
                stochastic_element=0.0,
                computation_time_ms=computation_time,
                learning_event=learning_event,
                model_weights=self.current_model_weights.copy(),
                equation_parameters={"alpha": self.alpha, "beta": self.beta},
                timestamp=datetime.now().isoformat(),
                confidence_score=0.0,
                recommended_action="maintain_current_state",
                reasoning=f"Computation error: {str(e)}"
            )
    
    async def _compute_integration_function(self, model_inputs: LearningModelInputs) -> float:
        """
        Weighted sum of all model inputs with dynamic weighting
        Following MCP Server Specification lines 444-461
        
        Educational Impact:
        Combines learner profile, knowledge state, engagement, and assessment
        data into single numeric value representing learning readiness.
        
        Args:
            model_inputs: Structured data from all learning models
            
        Returns:
            Weighted integration result (0.0-1.0)
            
        Raises:
            Exception: If normalization or computation fails
        """
        try:
            # Normalize model data to 0-1 scale
            normalized_learner = await self._normalize_learner_data(
                model_inputs.learner_model_data
            )
            normalized_knowledge = await self._normalize_knowledge_data(
                model_inputs.knowledge_model_data
            )
            normalized_engagement = await self._normalize_engagement_data(
                model_inputs.engagement_model_data
            )
            normalized_assessment = await self._normalize_assessment_data(
                model_inputs.assessment_model_data
            )
            
            # Apply dynamic weighting based on current learning event
            weighted_sum = (
                self.current_model_weights["learner"] * normalized_learner +
                self.current_model_weights["knowledge"] * normalized_knowledge +
                self.current_model_weights["engagement"] * normalized_engagement +
                self.current_model_weights["assessment"] * normalized_assessment
            )
            
            # Ensure result is in valid range
            weighted_sum = max(0.0, min(1.0, weighted_sum))
            
            self.logger.debug(
                f"Integration function computed: {weighted_sum:.3f} "
                f"(L:{normalized_learner:.2f}, K:{normalized_knowledge:.2f}, "
                f"E:{normalized_engagement:.2f}, A:{normalized_assessment:.2f})"
            )
            
            return weighted_sum
            
        except Exception as e:
            self.logger.error(f"Integration function computation failed: {e}")
            return 0.5  # Return neutral value on error
    
    async def _generate_stochastic_element(self) -> float:
        """
        Generate controlled randomness for exploration and serendipitous learning
        Following MCP Server Specification lines 463-468
        
        Educational Impact:
        Introduces controlled variability to prevent learning stagnation and
        encourage exploration of new learning pathways.
        
        Returns:
            Gaussian-distributed random value centered at 0
        """
        try:
            # Gaussian distribution centered at 0 with small variance
            # This provides controlled exploration while maintaining stability
            stochastic_value = random.gauss(0, 0.1)
            
            # Clamp to reasonable bounds to prevent extreme values
            stochastic_value = max(-0.3, min(0.3, stochastic_value))
            
            return stochastic_value
            
        except Exception as e:
            self.logger.error(f"Stochastic element generation failed: {e}")
            return 0.0  # Return neutral value on error
    
    async def _adjust_weights_for_learning_event(self, learning_event: str):
        """
        Dynamic weight adjustment based on learning progression phase
        Following MCP Server Specification lines 470-491
        
        Educational Impact:
        Optimizes learning model importance based on educational context,
        emphasizing learner readiness during onboarding and assessment
        during mastery phases.
        
        Args:
            learning_event: Current learning event type
        """
        try:
            if learning_event in self.weight_configurations:
                old_weights = self.current_model_weights.copy()
                self.current_model_weights = self.weight_configurations[learning_event]
                
                self.logger.debug(
                    f"Adjusted weights for {learning_event}: {self.current_model_weights}"
                )
                
                # Log weight changes for analysis
                if old_weights != self.current_model_weights:
                    weight_changes = {
                        key: self.current_model_weights[key] - old_weights.get(key, 0)
                        for key in self.current_model_weights.keys()
                    }
                    self.logger.info(f"Weight changes for {learning_event}: {weight_changes}")
                    
            else:
                self.logger.warning(
                    f"Unknown learning event: {learning_event}, using default weights"
                )
                
        except Exception as e:
            self.logger.error(f"Weight adjustment failed: {e}")
    
    async def _normalize_learner_data(self, learner_data: Dict[str, Any]) -> float:
        """
        Normalize learner model data to 0-1 scale
        
        Educational Impact:
        Converts learner profile metrics into normalized score representing
        learner readiness and engagement capacity.
        
        Args:
            learner_data: Raw learner model data
            
        Returns:
            Normalized learner readiness score (0.0-1.0)
        """
        try:
            # Extract key learner metrics
            learner_weight = learner_data.get("learner_model_weight", 0.35)
            adaptation_params = learner_data.get("adaptation_parameters", {})
            alpha_baseline = adaptation_params.get("alpha_baseline", 0.7)
            
            # Get behavioral analytics if available
            behavioral_data = learner_data.get("behavioral_analytics", {})
            engagement_pattern = behavioral_data.get("engagement_pattern_score", 0.5)
            learning_velocity = behavioral_data.get("learning_velocity", 0.5)
            
            # Combine metrics into normalized score
            # Higher learner weight and alpha indicate higher learner readiness
            base_score = (learner_weight + (alpha_baseline * 0.5)) / 1.5
            behavioral_score = (engagement_pattern + learning_velocity) / 2
            
            # Weighted combination
            normalized_score = (base_score * 0.7) + (behavioral_score * 0.3)
            
            # Ensure valid range
            normalized_score = max(0.0, min(1.0, normalized_score))
            
            return normalized_score
            
        except Exception as e:
            self.logger.error(f"Learner data normalization failed: {e}")
            return 0.5  # Default neutral value
    
    async def _normalize_knowledge_data(self, knowledge_data: Dict[str, Any]) -> float:
        """
        Normalize knowledge model data to 0-1 scale
        
        Educational Impact:
        Evaluates knowledge readiness based on prerequisite satisfaction
        and curriculum progress.
        
        Args:
            knowledge_data: Raw knowledge model data
            
        Returns:
            Normalized knowledge readiness score (0.0-1.0)
        """
        try:
            # Extract knowledge readiness indicators
            units_completed = knowledge_data.get("units_completed", 0)
            total_units = knowledge_data.get("total_units", 1)
            prerequisite_satisfaction = knowledge_data.get("prerequisite_satisfaction", 0.5)
            
            # Get curriculum analytics if available
            curriculum_data = knowledge_data.get("curriculum_analytics", {})
            mastery_level = curriculum_data.get("overall_mastery_level", 0.5)
            progression_rate = curriculum_data.get("progression_rate", 0.5)
            
            # Calculate knowledge readiness score
            completion_ratio = units_completed / max(total_units, 1)
            knowledge_foundation = (completion_ratio + prerequisite_satisfaction) / 2
            knowledge_progression = (mastery_level + progression_rate) / 2
            
            # Weighted combination
            knowledge_score = (knowledge_foundation * 0.6) + (knowledge_progression * 0.4)
            
            # Ensure valid range
            knowledge_score = max(0.0, min(1.0, knowledge_score))
            
            return knowledge_score
            
        except Exception as e:
            self.logger.error(f"Knowledge data normalization failed: {e}")
            return 0.5
    
    async def _normalize_engagement_data(self, engagement_data: Dict[str, Any]) -> float:
        """
        Normalize engagement model data to 0-1 scale
        
        Educational Impact:
        Measures current engagement level and interaction quality to
        determine optimal learning intensity and content difficulty.
        
        Args:
            engagement_data: Raw engagement model data
            
        Returns:
            Normalized engagement score (0.0-1.0)
        """
        try:
            # Extract engagement metrics
            attention_level = engagement_data.get("attention_level", 0.5)
            interaction_quality = engagement_data.get("interaction_quality", 0.5)
            flow_state = engagement_data.get("flow_state_indicators", 0.5)
            
            # Get VR-specific engagement data
            vr_metrics = engagement_data.get("vr_interaction_metrics", {})
            spatial_engagement = vr_metrics.get("spatial_engagement_score", 0.5)
            gesture_engagement = vr_metrics.get("gesture_engagement_score", 0.5)
            
            # Calculate overall engagement score
            core_engagement = (attention_level + interaction_quality + flow_state) / 3
            vr_engagement = (spatial_engagement + gesture_engagement) / 2
            
            # Weighted combination (VR metrics important for Quest 3)
            engagement_score = (core_engagement * 0.7) + (vr_engagement * 0.3)
            
            # Ensure valid range
            engagement_score = max(0.0, min(1.0, engagement_score))
            
            return engagement_score
            
        except Exception as e:
            self.logger.error(f"Engagement data normalization failed: {e}")
            return 0.5
    
    async def _normalize_assessment_data(self, assessment_data: Dict[str, Any]) -> float:
        """
        Normalize assessment model data to 0-1 scale
        
        Educational Impact:
        Evaluates demonstrated competency and learning evidence to determine
        readiness for progression to more advanced content.
        
        Args:
            assessment_data: Raw assessment model data
            
        Returns:
            Normalized assessment performance score (0.0-1.0)
        """
        try:
            # Extract assessment metrics
            competency_score = assessment_data.get("competency_score", 0.5)
            skill_demonstration = assessment_data.get("skill_demonstration", 0.5)
            learning_evidence = assessment_data.get("learning_evidence_strength", 0.5)
            
            # Get detailed assessment results
            assessment_results = assessment_data.get("assessment_results", {})
            overall_score = assessment_results.get("overall_score", 0.5)
            confidence_level = assessment_results.get("confidence_level", 0.5)
            
            # Calculate overall assessment score
            performance_score = (competency_score + skill_demonstration + learning_evidence) / 3
            assessment_quality = (overall_score + confidence_level) / 2
            
            # Weighted combination
            assessment_score = (performance_score * 0.8) + (assessment_quality * 0.2)
            
            # Ensure valid range
            assessment_score = max(0.0, min(1.0, assessment_score))
            
            return assessment_score
            
        except Exception as e:
            self.logger.error(f"Assessment data normalization failed: {e}")
            return 0.5
    
    async def _get_current_transition_state(self, learner_id: str) -> float:
        """
        Get current transition state ∂(t) for learner
        
        Educational Impact:
        Maintains learning progression continuity by tracking individual
        learner states across learning sessions.
        
        Args:
            learner_id: Unique learner identifier
            
        Returns:
            Current transition state value (0.0-1.0)
        """
        try:
            if learner_id in self.current_states:
                return self.current_states[learner_id]["transition_state"]
            else:
                # Initialize new learner with neutral state
                initial_state = {
                    "transition_state": 0.5,
                    "last_updated": datetime.now().isoformat(),
                    "learning_event": "introduction",
                    "session_count": 0
                }
                self.current_states[learner_id] = initial_state
                
                self.logger.info(f"Initialized new learner state for {learner_id}")
                return 0.5
                
        except Exception as e:
            self.logger.error(f"Failed to get transition state for {learner_id}: {e}")
            return 0.5
    
    async def _interpret_transition_decision(
        self, 
        learner_id: str, 
        transition_state: float, 
        model_inputs: LearningModelInputs
    ) -> Dict[str, Any]:
        """
        Interpret transition state into actionable learning decisions
        Following MCP Server Specification transition decision format (lines 376-395)
        
        Educational Impact:
        Converts mathematical transition state into concrete educational
        recommendations and learning path adjustments.
        
        Args:
            learner_id: Unique learner identifier
            transition_state: Computed transition state value
            model_inputs: Original model input data
            
        Returns:
            Dictionary containing educational decision recommendations
        """
        try:
            # Determine recommended action based on transition state
            if transition_state >= 0.8:
                recommended_action = "advance_to_next_event"
                confidence_score = 0.9
                reasoning = "High transition state indicates strong learning progress and readiness for advancement"
            elif transition_state >= 0.6:
                recommended_action = "continue_current_event"
                confidence_score = 0.7
                reasoning = "Moderate progress, continue with current learning activities for consolidation"
            elif transition_state >= 0.4:
                recommended_action = "provide_additional_support"
                confidence_score = 0.6
                reasoning = "Learning progress below optimal, additional support and scaffolding recommended"
            else:
                recommended_action = "remediate_prerequisites"
                confidence_score = 0.8
                reasoning = "Low transition state indicates need for prerequisite knowledge remediation"
            
            # Determine next learning event
            current_event = self.current_states[learner_id].get("learning_event", "practice")
            next_learning_event = await self._determine_next_learning_event(
                current_event, recommended_action
            )
            
            # Calculate adaptive parameters
            adaptive_parameters = await self._calculate_adaptive_parameters(
                transition_state, model_inputs
            )
            
            # Generate educational recommendations
            educational_recommendations = await self._generate_educational_recommendations(
                learner_id, transition_state, model_inputs
            )
            
            return {
                "recommended_action": recommended_action,
                "confidence_score": confidence_score,
                "reasoning": reasoning,
                "next_learning_event": next_learning_event,
                "adaptive_parameters": adaptive_parameters,
                "educational_recommendations": educational_recommendations,
                "transition_state_analysis": {
                    "current_state": transition_state,
                    "state_category": self._categorize_transition_state(transition_state),
                    "improvement_potential": max(0, 1.0 - transition_state),
                    "stability_indicator": self._calculate_state_stability(learner_id)
                }
            }
            
        except Exception as e:
            self.logger.error(f"Transition decision interpretation failed: {e}")
            return {
                "recommended_action": "continue_current_event",
                "confidence_score": 0.5,
                "reasoning": f"Error in decision interpretation: {str(e)}",
                "next_learning_event": "practice",
                "adaptive_parameters": {
                    "difficulty_adjustment": 1.0,
                    "support_level": "moderate",
                    "pacing_adjustment": "normal"
                },
                "educational_recommendations": ["Review current learning objectives"],
                "transition_state_analysis": {
                    "current_state": 0.5,
                    "state_category": "neutral",
                    "improvement_potential": 0.5,
                    "stability_indicator": "unknown"
                }
            }
    
    async def _determine_next_learning_event(
        self, 
        current_event: str, 
        recommended_action: str
    ) -> str:
        """
        Determine next learning event based on current state and recommendation
        
        Educational Impact:
        Ensures appropriate learning progression following educational
        design principles and learner readiness.
        
        Args:
            current_event: Current learning event
            recommended_action: Recommended action from transition analysis
            
        Returns:
            Next appropriate learning event
        """
        try:
            # Define learning event progression
            event_progression = {
                "onboarding": "introduction",
                "introduction": "practice", 
                "practice": "application",
                "application": "mastery",
                "mastery": "mastery"  # Stay at mastery
            }
            
            if recommended_action == "advance_to_next_event":
                return event_progression.get(current_event, current_event)
            elif recommended_action == "remediate_prerequisites":
                # Move back one level if possible
                reverse_progression = {
                    "mastery": "application",
                    "application": "practice",
                    "practice": "introduction", 
                    "introduction": "onboarding",
                    "onboarding": "onboarding"
                }
                return reverse_progression.get(current_event, current_event)
            else:
                # Continue with current event
                return current_event
                
        except Exception as e:
            self.logger.error(f"Next learning event determination failed: {e}")
            return "practice"  # Safe default
    
    async def _calculate_adaptive_parameters(
        self, 
        transition_state: float, 
        model_inputs: LearningModelInputs
    ) -> Dict[str, Any]:
        """
        Calculate adaptive parameters for learning optimization
        
        Educational Impact:
        Provides specific guidance for content difficulty, support level,
        and pacing adjustments based on learner performance.
        
        Args:
            transition_state: Current transition state
            model_inputs: Learning model input data
            
        Returns:
            Dictionary of adaptive learning parameters
        """
        try:
            # Calculate difficulty adjustment
            if transition_state >= 0.8:
                difficulty_adjustment = 1.2  # Increase difficulty
                support_level = "minimal"
                pacing_adjustment = "accelerated"
            elif transition_state >= 0.6:
                difficulty_adjustment = 1.0  # Maintain difficulty
                support_level = "moderate"
                pacing_adjustment = "normal"
            elif transition_state >= 0.4:
                difficulty_adjustment = 0.8  # Reduce difficulty
                support_level = "enhanced"
                pacing_adjustment = "slower"
            else:
                difficulty_adjustment = 0.6  # Significantly reduce difficulty
                support_level = "intensive"
                pacing_adjustment = "much_slower"
            
            # Extract engagement data for additional parameters
            engagement_data = model_inputs.engagement_model_data
            attention_level = engagement_data.get("attention_level", 0.5)
            
            # Adjust for attention level
            if attention_level < 0.4:
                pacing_adjustment = "slower"
                support_level = "enhanced"
            
            return {
                "difficulty_adjustment": difficulty_adjustment,
                "support_level": support_level,
                "pacing_adjustment": pacing_adjustment,
                "attention_optimization": {
                    "current_attention": attention_level,
                    "recommended_session_length": "short" if attention_level < 0.5 else "normal",
                    "break_frequency": "frequent" if attention_level < 0.4 else "normal"
                },
                "content_recommendations": {
                    "interactivity_level": "high" if transition_state < 0.6 else "moderate",
                    "multimedia_usage": "enhanced" if transition_state < 0.5 else "standard",
                    "practice_repetition": "increased" if transition_state < 0.7 else "standard"
                }
            }
            
        except Exception as e:
            self.logger.error(f"Adaptive parameter calculation failed: {e}")
            return {
                "difficulty_adjustment": 1.0,
                "support_level": "moderate",
                "pacing_adjustment": "normal"
            }
    
    async def _generate_educational_recommendations(
        self,
        learner_id: str,
        transition_state: float,
        model_inputs: LearningModelInputs
    ) -> List[str]:
        """
        Generate specific educational recommendations based on analysis
        
        Educational Impact:
        Provides actionable guidance for educators and learners to optimize
        learning outcomes and address identified challenges.
        
        Args:
            learner_id: Unique learner identifier
            transition_state: Current transition state
            model_inputs: Learning model input data
            
        Returns:
            List of educational recommendations
        """
        try:
            recommendations = []
            
            # Analyze transition state
            if transition_state >= 0.8:
                recommendations.extend([
                    "Learner shows excellent progress - consider advanced challenges",
                    "Introduce peer teaching opportunities",
                    "Prepare for next learning event advancement"
                ])
            elif transition_state >= 0.6:
                recommendations.extend([
                    "Maintain current learning activities with minor enhancements",
                    "Provide additional practice exercises for consolidation",
                    "Monitor progress for advancement readiness"
                ])
            elif transition_state >= 0.4:
                recommendations.extend([
                    "Increase learning support and scaffolding",
                    "Provide additional examples and guided practice",
                    "Consider peer collaboration opportunities"
                ])
            else:
                recommendations.extend([
                    "Review prerequisite knowledge gaps",
                    "Provide intensive remediation support",
                    "Consider individual tutoring or mentoring"
                ])
            
            # Analyze engagement patterns
            engagement_data = model_inputs.engagement_model_data
            attention_level = engagement_data.get("attention_level", 0.5)
            
            if attention_level < 0.4:
                recommendations.extend([
                    "Implement attention-grabbing activities",
                    "Reduce session length and increase breaks",
                    "Use multimedia and interactive content"
                ])
            
            # Analyze assessment results
            assessment_data = model_inputs.assessment_model_data
            competency_score = assessment_data.get("competency_score", 0.5)
            
            if competency_score < 0.5:
                recommendations.extend([
                    "Focus on competency skill development",
                    "Provide targeted skill practice activities",
                    "Use formative assessment for progress monitoring"
                ])
            
            return recommendations
            
        except Exception as e:
            self.logger.error(f"Educational recommendation generation failed: {e}")
            return ["Continue current learning activities", "Monitor learner progress"]
    
    def _categorize_transition_state(self, transition_state: float) -> str:
        """Categorize transition state into descriptive category"""
        if transition_state >= 0.8:
            return "excellent"
        elif transition_state >= 0.6:
            return "good"
        elif transition_state >= 0.4:
            return "developing"
        else:
            return "needs_support"
    
    def _calculate_state_stability(self, learner_id: str) -> str:
        """Calculate stability indicator for learner's transition state"""
        try:
            if learner_id not in self.current_states:
                return "new_learner"
            
            # This would typically analyze historical transition states
            # For now, return based on current state characteristics
            return "stable"
            
        except Exception:
            return "unknown"
    
    async def _store_computation_history(
        self,
        learner_id: str,
        model_inputs: LearningModelInputs,
        integration_result: float,
        stochastic_element: float,
        transition_state: float,
        computation_time: float
    ):
        """
        Store computation history for analysis and optimization
        
        Educational Impact:
        Enables learning analytics and system optimization through
        historical data analysis and pattern recognition.
        
        Args:
            learner_id: Unique learner identifier
            model_inputs: Original input data
            integration_result: Computed integration value
            stochastic_element: Generated stochastic value
            transition_state: Final transition state
            computation_time: Processing time in milliseconds
        """
        try:
            history_entry = {
                "learner_id": learner_id,
                "timestamp": datetime.now().isoformat(),
                "learning_event": model_inputs.learning_event,
                "integration_result": integration_result,
                "stochastic_element": stochastic_element,
                "transition_state": transition_state,
                "computation_time_ms": computation_time,
                "model_weights": self.current_model_weights.copy(),
                "equation_parameters": {
                    "alpha": self.alpha,
                    "beta": self.beta
                }
            }
            
            self.computation_history.append(history_entry)
            
            # Limit history size to prevent memory issues
            max_history_size = 1000
            if len(self.computation_history) > max_history_size:
                self.computation_history = self.computation_history[-max_history_size:]
            
            self.logger.debug(f"Stored computation history for learner {learner_id}")
            
        except Exception as e:
            self.logger.error(f"Failed to store computation history: {e}")
    
    async def get_performance_metrics(self) -> Dict[str, Any]:
        """
        Get current performance metrics for monitoring
        
        Educational Impact:
        Enables system monitoring and optimization to ensure Quest 3 VR
        performance requirements are maintained.
        
        Returns:
            Dictionary containing performance metrics
        """
        try:
            if not self.computation_times:
                return {
                    "status": "no_data",
                    "message": "No computation history available"
                }
            
            # Calculate performance statistics
            avg_computation_time = sum(self.computation_times) / len(self.computation_times)
            max_computation_time = max(self.computation_times)
            min_computation_time = min(self.computation_times)
            
            # Performance threshold compliance
            threshold_compliance = sum(
                1 for time in self.computation_times 
                if time <= self.MAX_COMPUTATION_TIME_MS
            ) / len(self.computation_times) * 100
            
            return {
                "computation_performance": {
                    "average_time_ms": round(avg_computation_time, 2),
                    "max_time_ms": round(max_computation_time, 2),
                    "min_time_ms": round(min_computation_time, 2),
                    "threshold_compliance_percent": round(threshold_compliance, 1),
                    "total_computations": len(self.computation_times)
                },
                "memory_usage": {
                    "current_states_count": len(self.current_states),
                    "history_entries": len(self.computation_history)
                },
                "quest3_compliance": {
                    "performance_target": f"<{self.MAX_COMPUTATION_TIME_MS}ms",
                    "compliance_rate": f"{threshold_compliance:.1f}%",
                    "status": "compliant" if threshold_compliance >= 95 else "needs_optimization"
                },
                "learning_events_processed": self._get_learning_event_statistics()
            }
            
        except Exception as e:
            self.logger.error(f"Performance metrics calculation failed: {e}")
            return {
                "status": "error",
                "message": f"Failed to calculate metrics: {str(e)}"
            }
    
    def _get_learning_event_statistics(self) -> Dict[str, int]:
        """Get statistics on processed learning events"""
        try:
            event_counts = {}
            for entry in self.computation_history:
                event = entry.get("learning_event", "unknown")
                event_counts[event] = event_counts.get(event, 0) + 1
            return event_counts
        except Exception:
            return {}
    
    async def reset_learner_state(self, learner_id: str):
        """
        Reset learner state (for testing or new learning sessions)
        
        Educational Impact:
        Allows fresh start for learners or testing scenarios while
        maintaining system integrity.
        
        Args:
            learner_id: Unique learner identifier
        """
        try:
            if learner_id in self.current_states:
                del self.current_states[learner_id]
                self.logger.info(f"Reset state for learner {learner_id}")
            else:
                self.logger.warning(f"No state found for learner {learner_id}")
                
        except Exception as e:
            self.logger.error(f"Failed to reset learner state: {e}")
    
    async def update_equation_parameters(self, alpha: Optional[float] = None, beta: Optional[float] = None):
        """
        Update learning equation parameters for system tuning
        
        Educational Impact:
        Allows fine-tuning of learning adaptation strength and exploration
        factor based on educational effectiveness analysis.
        
        Args:
            alpha: New adaptive learning rate (0.0-1.0)
            beta: New exploration factor (0.0-0.3)
        """
        try:
            if alpha is not None:
                if 0.0 <= alpha <= 1.0:
                    old_alpha = self.alpha
                    self.alpha = alpha
                    self.logger.info(f"Updated alpha from {old_alpha} to {alpha}")
                else:
                    raise ValueError("Alpha must be between 0.0 and 1.0")
            
            if beta is not None:
                if 0.0 <= beta <= 0.3:
                    old_beta = self.beta
                    self.beta = beta
                    self.logger.info(f"Updated beta from {old_beta} to {beta}")
                else:
                    raise ValueError("Beta must be between 0.0 and 0.3")
                    
        except Exception as e:
            self.logger.error(f"Failed to update equation parameters: {e}")
            raise
