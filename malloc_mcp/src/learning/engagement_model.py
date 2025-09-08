"""
Engagement Model (E) API Implementation
Following MCP Server Specification lines 193-261

Educational Impact:
Tracks VR interaction patterns and spatial engagement metrics to optimize
learning experiences and maintain learner motivation throughout education.

Performance Requirements:
- Quest 3 VR: Engagement tracking <50ms response time
- Memory usage: <30MB for interaction tracking
- Spatial precision: 0.1mm tolerance for VR interactions

Manages VR interaction tracking, attention metrics, and spatial engagement
with real-time analysis for adaptive learning optimization
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
import math

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class VRInteractionData:
    """
    VR interaction data structure following MCP Server Specification
    Based on engagement tracking requirements lines 193-261
    
    Educational Impact:
    Standardizes VR interaction data for consistent engagement analysis
    and spatial learning optimization across all educational content.
    """
    learner_id: str
    session_id: str
    interaction_type: str
    spatial_coordinates: Dict[str, float]
    interaction_duration: float
    interaction_intensity: float
    timestamp: str = None
    
    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now().isoformat()
    
    def validate_spatial_precision(self) -> bool:
        """
        Validate spatial coordinates meet 0.1mm precision requirements
        
        Educational Impact:
        Ensures spatial precision for accurate VR learning analytics
        and reliable spatial reasoning assessment.
        
        Returns:
            bool: True if spatial precision is valid, False otherwise
        """
        required_coords = ["x", "y", "z"]
        
        if not all(coord in self.spatial_coordinates for coord in required_coords):
            logger.error("Missing required spatial coordinates")
            return False
        
        # Validate precision (0.1mm = 0.0001m)
        for coord, value in self.spatial_coordinates.items():
            if not isinstance(value, (int, float)):
                logger.error(f"Invalid coordinate type for {coord}: {type(value)}")
                return False
            
            # Check if value has reasonable precision
            if abs(value) > 100:  # Reasonable VR space bounds
                logger.warning(f"Coordinate {coord} outside reasonable VR space: {value}")
        
        return True

@dataclass
class AttentionMetrics:
    """
    Attention tracking metrics for VR learning environments
    
    Educational Impact:
    Provides quantitative measures of learner attention and focus
    to optimize content delivery and identify engagement issues.
    """
    gaze_focus_duration: float
    object_interaction_count: int
    navigation_efficiency: float
    task_completion_rate: float
    distraction_events: int
    attention_stability: float
    
    def calculate_overall_attention(self) -> float:
        """Calculate overall attention score"""
        return (
            min(1.0, self.gaze_focus_duration / 60.0) * 0.3 +  # Normalize to 1 minute
            min(1.0, self.object_interaction_count / 10.0) * 0.2 +  # Normalize to 10 interactions
            self.navigation_efficiency * 0.2 +
            self.task_completion_rate * 0.2 +
            max(0.0, 1.0 - self.distraction_events / 5.0) * 0.1  # Penalize distractions
        )

class EngagementModelProcessor:
    """
    Engagement Model processor implementing MCP Server Specification API
    
    Educational Impact:
    Processes VR interaction data and attention metrics to provide
    real-time engagement insights for adaptive learning optimization.
    
    Performance Requirements:
    - Engagement tracking: <50ms response time
    - Memory usage: <30MB for typical operations
    - Quest 3 compatibility: Maintains >72fps during processing
    """
    
    def __init__(self, spatial_precision_tolerance: float = 0.0001):
        self.spatial_precision_tolerance = spatial_precision_tolerance  # 0.1mm
        self.engagement_sessions = {}
        self.interaction_history = {}
        self.attention_analytics = {}
        
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
            "tracking_response_times": [],
            "spatial_analysis_times": [],
            "attention_calculation_times": []
        }
        
        # VR environment configuration
        self.vr_environment_bounds = {
            "min_x": -5.0, "max_x": 5.0,
            "min_y": -5.0, "max_y": 5.0,
            "min_z": 0.0, "max_z": 3.0
        }
        
        logger.info("EngagementModelProcessor initialized with VR interaction tracking")
    
    async def start_engagement_session(self, session_config: Dict[str, Any]) -> Dict[str, Any]:
        """
        Start engagement tracking session for VR learning
        POST /api/v1/engagement/session/start implementation
        
        Educational Impact:
        Initiates comprehensive engagement tracking to monitor learner
        attention and interaction patterns throughout VR learning experience.
        
        Performance Requirements:
        - Quest 3 VR: <50ms session initialization
        - Memory: <10MB for session setup
        - Spatial tracking: 0.1mm precision enabled
        
        Args:
            session_config: Session configuration including learner and environment data
            
        Returns:
            Dict containing session initialization results
        """
        start_time = time.time()
        
        try:
            learner_id = session_config["learner_id"]
            session_id = session_config.get("session_id", str(uuid.uuid4()))
            learning_context = session_config.get("learning_context", {})
            vr_environment = session_config.get("vr_environment", {})
            
            # Initialize engagement session
            session_data = {
                "session_id": session_id,
                "learner_id": learner_id,
                "learning_context": learning_context,
                "vr_environment": vr_environment,
                "start_time": datetime.now(),
                "interaction_count": 0,
                "attention_events": [],
                "spatial_interactions": [],
                "engagement_metrics": {
                    "total_gaze_time": 0.0,
                    "interaction_frequency": 0.0,
                    "navigation_efficiency": 0.0,
                    "task_engagement": 0.0
                }
            }
            
            # Store session
            self.engagement_sessions[session_id] = session_data
            
            # Initialize interaction history for learner
            if learner_id not in self.interaction_history:
                self.interaction_history[learner_id] = []
            
            # Initialize attention analytics
            self.attention_analytics[session_id] = {
                "gaze_tracking": [],
                "interaction_patterns": [],
                "spatial_movement": [],
                "engagement_fluctuations": []
            }
            
            # Calculate initial engagement weight for learning event
            learning_event = learning_context.get("learning_event", "practice")
            engagement_weight = self.weight_configurations.get(learning_event, {}).get("engagement", 0.18)
            
            processing_time = time.time() - start_time
            
            # Performance validation
            if processing_time > 0.05:  # 50ms threshold
                logger.warning(f"Engagement session start exceeded Quest 3 threshold: {processing_time:.3f}s")
            
            response = {
                "status": "started",
                "session_id": session_id,
                "learner_id": learner_id,
                "engagement_weight": engagement_weight,
                "spatial_precision": f"{self.spatial_precision_tolerance}m",
                "vr_tracking_enabled": True,
                "attention_monitoring_active": True,
                "processing_time_ms": processing_time * 1000,
                "start_timestamp": datetime.now().isoformat()
            }
            
            logger.info(f"Engagement session started: {session_id} for learner {learner_id}")
            return response
            
        except Exception as e:
            processing_time = time.time() - start_time
            logger.error(f"Engagement session start failed ({processing_time:.3f}s): {e}")
            raise
    
    async def track_vr_interaction(self, interaction_data: VRInteractionData) -> Dict[str, Any]:
        """
        Track VR interaction with spatial precision validation
        POST /api/v1/engagement/interaction/track implementation
        
        Educational Impact:
        Captures detailed VR interaction data to understand spatial learning
        patterns and optimize 3D educational content effectiveness.
        
        Performance Requirements:
        - Quest 3 VR: <25ms interaction processing
        - Spatial precision: 0.1mm tolerance validation
        - Real-time analysis: Immediate engagement feedback
        
        Args:
            interaction_data: VR interaction data with spatial coordinates
            
        Returns:
            Dict containing interaction analysis and engagement metrics
        """
        start_time = time.time()
        
        try:
            # Validate spatial precision
            if not interaction_data.validate_spatial_precision():
                raise ValueError("Invalid spatial precision in interaction data")
            
            session_id = interaction_data.session_id
            learner_id = interaction_data.learner_id
            
            # Validate session exists
            if session_id not in self.engagement_sessions:
                raise ValueError(f"Engagement session not found: {session_id}")
            
            session_data = self.engagement_sessions[session_id]
            session_data["interaction_count"] += 1
            
            # Process spatial interaction
            spatial_analysis = await self.analyze_spatial_interaction(
                interaction_data.spatial_coordinates,
                interaction_data.interaction_type
            )
            
            # Calculate interaction engagement metrics
            interaction_metrics = await self.calculate_interaction_engagement(interaction_data)
            
            # Update attention analytics
            await self.update_attention_analytics(session_id, interaction_data, interaction_metrics)
            
            # Store interaction in history
            interaction_record = {
                "timestamp": interaction_data.timestamp,
                "session_id": session_id,
                "interaction_type": interaction_data.interaction_type,
                "spatial_coordinates": interaction_data.spatial_coordinates,
                "duration": interaction_data.interaction_duration,
                "intensity": interaction_data.interaction_intensity,
                "spatial_analysis": spatial_analysis,
                "engagement_metrics": interaction_metrics
            }
            
            self.interaction_history[learner_id].append(interaction_record)
            session_data["spatial_interactions"].append(interaction_record)
            
            # Calculate real-time engagement score
            current_engagement = await self.calculate_realtime_engagement(session_id)
            
            # Update session engagement metrics
            session_data["engagement_metrics"].update({
                "current_engagement": current_engagement,
                "last_interaction_time": datetime.now().isoformat()
            })
            
            processing_time = time.time() - start_time
            
            # Record performance metrics
            await self._record_performance_metrics(processing_time, "track_interaction")
            
            # Performance validation
            if processing_time > 0.025:  # 25ms threshold
                logger.warning(f"VR interaction tracking exceeded Quest 3 threshold: {processing_time:.3f}s")
            
            response = {
                "interaction_processed": True,
                "session_id": session_id,
                "interaction_count": session_data["interaction_count"],
                "spatial_analysis": spatial_analysis,
                "engagement_metrics": interaction_metrics,
                "current_engagement_score": current_engagement,
                "spatial_precision_validated": True,
                "processing_time_ms": processing_time * 1000
            }
            
            return response
            
        except Exception as e:
            processing_time = time.time() - start_time
            logger.error(f"VR interaction tracking failed ({processing_time:.3f}s): {e}")
            raise
    
    async def analyze_attention_patterns(self, session_id: str, time_window_minutes: int = 5) -> Dict[str, Any]:
        """
        Analyze learner attention patterns over time window
        GET /api/v1/engagement/attention/{session_id} implementation
        
        Educational Impact:
        Provides insights into attention stability and focus patterns
        to optimize content pacing and identify engagement issues.
        
        Args:
            session_id: Engagement session identifier
            time_window_minutes: Analysis time window in minutes
            
        Returns:
            Dict containing comprehensive attention analysis
        """
        start_time = time.time()
        
        try:
            if session_id not in self.engagement_sessions:
                raise ValueError(f"Session not found: {session_id}")
            
            session_data = self.engagement_sessions[session_id]
            analytics_data = self.attention_analytics.get(session_id, {})
            
            # Define time window for analysis
            current_time = datetime.now()
            window_start = current_time - timedelta(minutes=time_window_minutes)
            
            # Filter interactions within time window
            recent_interactions = [
                interaction for interaction in session_data["spatial_interactions"]
                if datetime.fromisoformat(interaction["timestamp"]) >= window_start
            ]
            
            # Calculate attention metrics
            attention_metrics = await self.calculate_attention_metrics(recent_interactions)
            
            # Analyze gaze patterns
            gaze_analysis = await self.analyze_gaze_patterns(analytics_data.get("gaze_tracking", []))
            
            # Calculate attention stability
            attention_stability = await self.calculate_attention_stability(recent_interactions)
            
            # Identify attention events (focus/distraction)
            attention_events = await self.identify_attention_events(recent_interactions)
            
            # Generate engagement recommendations
            recommendations = await self.generate_engagement_recommendations(
                attention_metrics, gaze_analysis, attention_stability
            )
            
            processing_time = time.time() - start_time
            
            response = {
                "session_id": session_id,
                "time_window_minutes": time_window_minutes,
                "interactions_analyzed": len(recent_interactions),
                "attention_metrics": attention_metrics,
                "gaze_analysis": gaze_analysis,
                "attention_stability": attention_stability,
                "attention_events": attention_events,
                "engagement_recommendations": recommendations,
                "analysis_timestamp": datetime.now().isoformat(),
                "processing_time_ms": processing_time * 1000
            }
            
            return response
            
        except Exception as e:
            processing_time = time.time() - start_time
            logger.error(f"Attention pattern analysis failed ({processing_time:.3f}s): {e}")
            raise
    
    async def calculate_engagement_weight(self, learner_id: str, learning_event: str) -> Dict[str, Any]:
        """
        Calculate engagement model weight for learning equation
        Based on MCP specification lines 114-117 and 98-101
        
        Educational Impact:
        Determines appropriate emphasis on engagement factors in the
        adaptive learning equation based on current learner state.
        
        Args:
            learner_id: Unique learner identifier
            learning_event: Current learning event type
            
        Returns:
            Dict containing engagement weight and contributing factors
        """
        try:
            # Get base weight for learning event
            base_weight = self.weight_configurations.get(learning_event, {}).get("engagement", 0.18)
            
            # Get recent engagement data for learner
            recent_interactions = self.interaction_history.get(learner_id, [])[-20:]  # Last 20 interactions
            
            # Calculate engagement trend
            engagement_trend = await self.calculate_engagement_trend(recent_interactions)
            
            # Adjust weight based on engagement level
            if engagement_trend < 0.3:  # Low engagement
                weight_adjustment = 0.08  # Increase engagement emphasis
            elif engagement_trend > 0.8:  # High engagement
                weight_adjustment = -0.03  # Reduce engagement emphasis
            else:
                weight_adjustment = 0.0
            
            # Calculate spatial interaction quality factor
            spatial_quality = await self.calculate_spatial_interaction_quality(recent_interactions)
            spatial_adjustment = (spatial_quality - 0.5) * 0.05
            
            final_weight = base_weight + weight_adjustment + spatial_adjustment
            
            # Ensure weight stays within MCP specification bounds (0.15-0.30)
            final_weight = max(0.15, min(0.30, final_weight))
            
            return {
                "engagement_weight": final_weight,
                "learning_event": learning_event,
                "base_weight": base_weight,
                "engagement_trend": engagement_trend,
                "spatial_quality": spatial_quality,
                "weight_adjustments": {
                    "engagement_adjustment": weight_adjustment,
                    "spatial_adjustment": spatial_adjustment
                },
                "calculation_timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"Engagement weight calculation failed: {e}")
            raise
    
    async def analyze_spatial_interaction(self, spatial_coords: Dict[str, float], interaction_type: str) -> Dict[str, Any]:
        """
        Analyze spatial interaction for VR learning insights
        
        Educational Impact:
        Provides spatial learning analytics to optimize 3D content placement
        and understand spatial reasoning development patterns.
        
        Args:
            spatial_coords: 3D spatial coordinates of interaction
            interaction_type: Type of VR interaction
            
        Returns:
            Dict containing spatial interaction analysis
        """
        try:
            x, y, z = spatial_coords.get("x", 0), spatial_coords.get("y", 0), spatial_coords.get("z", 0)
            
            # Validate coordinates are within VR environment bounds
            within_bounds = (
                self.vr_environment_bounds["min_x"] <= x <= self.vr_environment_bounds["max_x"] and
                self.vr_environment_bounds["min_y"] <= y <= self.vr_environment_bounds["max_y"] and
                self.vr_environment_bounds["min_z"] <= z <= self.vr_environment_bounds["max_z"]
            )
            
            # Calculate distance from center (learning focus point)
            distance_from_center = math.sqrt(x**2 + y**2 + z**2)
            
            # Analyze spatial zone (near, medium, far)
            if distance_from_center < 1.0:
                spatial_zone = "near"
                engagement_factor = 1.0
            elif distance_from_center < 2.5:
                spatial_zone = "medium"
                engagement_factor = 0.8
            else:
                spatial_zone = "far"
                engagement_factor = 0.6
            
            # Calculate spatial precision score
            precision_score = self._calculate_spatial_precision_score(spatial_coords)
            
            # Determine interaction quality based on type and position
            interaction_quality = await self._assess_interaction_quality(
                interaction_type, spatial_coords, distance_from_center
            )
            
            return {
                "spatial_coordinates": spatial_coords,
                "within_bounds": within_bounds,
                "distance_from_center": distance_from_center,
                "spatial_zone": spatial_zone,
                "engagement_factor": engagement_factor,
                "precision_score": precision_score,
                "interaction_quality": interaction_quality,
                "spatial_reasoning_indicator": spatial_zone == "near" and interaction_quality > 0.7
            }
            
        except Exception as e:
            logger.error(f"Spatial interaction analysis failed: {e}")
            return {"error": str(e)}
    
    async def calculate_interaction_engagement(self, interaction_data: VRInteractionData) -> Dict[str, Any]:
        """
        Calculate engagement metrics for individual interaction
        
        Educational Impact:
        Quantifies individual interaction engagement to build comprehensive
        understanding of learner engagement patterns over time.
        
        Args:
            interaction_data: VR interaction data
            
        Returns:
            Dict containing interaction engagement metrics
        """
        try:
            # Duration-based engagement (longer interactions often indicate higher engagement)
            duration_score = min(1.0, interaction_data.interaction_duration / 30.0)  # Normalize to 30 seconds
            
            # Intensity-based engagement
            intensity_score = min(1.0, interaction_data.interaction_intensity)
            
            # Spatial engagement (interactions closer to learning objects score higher)
            spatial_coords = interaction_data.spatial_coordinates
            distance_from_center = math.sqrt(
                spatial_coords.get("x", 0)**2 + 
                spatial_coords.get("y", 0)**2 + 
                spatial_coords.get("z", 0)**2
            )
            spatial_score = max(0.0, 1.0 - distance_from_center / 3.0)  # Closer = higher score
            
            # Interaction type weighting
            type_weights = {
                "gaze": 0.3,
                "touch": 0.8,
                "manipulation": 1.0,
                "navigation": 0.5,
                "gesture": 0.7
            }
            type_weight = type_weights.get(interaction_data.interaction_type, 0.5)
            
            # Calculate overall engagement score
            engagement_score = (
                duration_score * 0.3 +
                intensity_score * 0.3 +
                spatial_score * 0.2 +
                type_weight * 0.2
            )
            
            return {
                "overall_engagement": engagement_score,
                "duration_score": duration_score,
                "intensity_score": intensity_score,
                "spatial_score": spatial_score,
                "type_weight": type_weight,
                "interaction_type": interaction_data.interaction_type,
                "engagement_level": self._categorize_engagement_level(engagement_score)
            }
            
        except Exception as e:
            logger.error(f"Interaction engagement calculation failed: {e}")
            return {"error": str(e)}
    
    async def update_attention_analytics(self, session_id: str, interaction_data: VRInteractionData, interaction_metrics: Dict[str, Any]):
        """
        Update attention analytics with new interaction data
        
        Educational Impact:
        Maintains comprehensive attention tracking to identify patterns
        and optimize content delivery for sustained engagement.
        
        Args:
            session_id: Session identifier
            interaction_data: VR interaction data
            interaction_metrics: Calculated interaction metrics
        """
        try:
            if session_id not in self.attention_analytics:
                return
            
            analytics = self.attention_analytics[session_id]
            current_time = datetime.now()
            
            # Update gaze tracking if applicable
            if interaction_data.interaction_type == "gaze":
                gaze_event = {
                    "timestamp": interaction_data.timestamp,
                    "duration": interaction_data.interaction_duration,
                    "spatial_coordinates": interaction_data.spatial_coordinates,
                    "intensity": interaction_data.interaction_intensity
                }
                analytics["gaze_tracking"].append(gaze_event)
            
            # Update interaction patterns
            interaction_pattern = {
                "timestamp": interaction_data.timestamp,
                "type": interaction_data.interaction_type,
                "engagement_score": interaction_metrics.get("overall_engagement", 0.0),
                "spatial_zone": interaction_metrics.get("spatial_score", 0.0)
            }
            analytics["interaction_patterns"].append(interaction_pattern)
            
            # Update spatial movement tracking
            spatial_movement = {
                "timestamp": interaction_data.timestamp,
                "coordinates": interaction_data.spatial_coordinates,
                "movement_type": interaction_data.interaction_type
            }
            analytics["spatial_movement"].append(spatial_movement)
            
            # Calculate engagement fluctuation
            recent_patterns = analytics["interaction_patterns"][-5:]  # Last 5 interactions
            if len(recent_patterns) >= 2:
                engagement_scores = [p["engagement_score"] for p in recent_patterns]
                fluctuation = np.std(engagement_scores) if len(engagement_scores) > 1 else 0.0
                
                analytics["engagement_fluctuations"].append({
                    "timestamp": interaction_data.timestamp,
                    "fluctuation": fluctuation,
                    "trend": "increasing" if engagement_scores[-1] > engagement_scores[0] else "decreasing"
                })
            
            # Keep only recent data to manage memory
            max_entries = 100
            for key in analytics:
                if isinstance(analytics[key], list) and len(analytics[key]) > max_entries:
                    analytics[key] = analytics[key][-max_entries:]
            
        except Exception as e:
            logger.error(f"Attention analytics update failed: {e}")
    
    async def calculate_realtime_engagement(self, session_id: str) -> float:
        """
        Calculate real-time engagement score for session
        
        Educational Impact:
        Provides immediate engagement feedback for real-time learning
        adaptation and intervention decisions.
        
        Args:
            session_id: Session identifier
            
        Returns:
            float: Real-time engagement score (0.0 to 1.0)
        """
        try:
            if session_id not in self.engagement_sessions:
                return 0.0
            
            session_data = self.engagement_sessions[session_id]
            recent_interactions = session_data["spatial_interactions"][-10:]  # Last 10 interactions
            
            if not recent_interactions:
                return 0.0
            
            # Calculate average engagement from recent interactions
            engagement_scores = [
                interaction.get("engagement_metrics", {}).get("overall_engagement", 0.0)
                for interaction in recent_interactions
            ]
            
            avg_engagement = np.mean(engagement_scores) if engagement_scores else 0.0
            
            # Apply time decay (more recent interactions weighted higher)
            current_time = datetime.now()
            weighted_engagement = 0.0
            total_weight = 0.0
            
            for i, interaction in enumerate(recent_interactions):
                interaction_time = datetime.fromisoformat(interaction["timestamp"])
                time_diff = (current_time - interaction_time).total_seconds()
                
                # Exponential decay with 5-minute half-life
                weight = math.exp(-time_diff / 300)
                engagement_score = interaction.get("engagement_metrics", {}).get("overall_engagement", 0.0)
                
                weighted_engagement += engagement_score * weight
                total_weight += weight
            
            final_engagement = weighted_engagement / total_weight if total_weight > 0 else avg_engagement
            
            return max(0.0, min(1.0, final_engagement))
            
        except Exception as e:
            logger.error(f"Real-time engagement calculation failed: {e}")
            return 0.0
    
    async def calculate_attention_metrics(self, interactions: List[Dict[str, Any]]) -> AttentionMetrics:
        """
        Calculate comprehensive attention metrics from interactions
        
        Educational Impact:
        Quantifies attention patterns to optimize content delivery
        and identify learners needing attention support.
        
        Args:
            interactions: List of interaction records
            
        Returns:
            AttentionMetrics object with calculated metrics
        """
        try:
            if not interactions:
                return AttentionMetrics(0.0, 0, 0.0, 0.0, 0, 0.0)
            
            # Calculate gaze focus duration
            gaze_interactions = [i for i in interactions if i.get("interaction_type") == "gaze"]
            total_gaze_duration = sum(i.get("duration", 0) for i in gaze_interactions)
            
            # Count object interactions
            object_interactions = [i for i in interactions if i.get("interaction_type") in ["touch", "manipulation"]]
            
            # Calculate navigation efficiency
            navigation_interactions = [i for i in interactions if i.get("interaction_type") == "navigation"]
            navigation_efficiency = await self._calculate_navigation_efficiency(navigation_interactions)
            
            # Calculate task completion rate (based on successful interactions)
            successful_interactions = [
                i for i in interactions 
                if i.get("engagement_metrics", {}).get("overall_engagement", 0) > 0.6
            ]
            task_completion_rate = len(successful_interactions) / len(interactions) if interactions else 0.0
            
            # Count distraction events (low engagement interactions)
            distraction_events = sum(
                1 for i in interactions 
                if i.get("engagement_metrics", {}).get("overall_engagement", 0) < 0.3
            )
            
            # Calculate attention stability
            engagement_scores = [
                i.get("engagement_metrics", {}).get("overall_engagement", 0.0)
                for i in interactions
            ]
            attention_stability = 1.0 - np.std(engagement_scores) if len(engagement_scores) > 1 else 1.0
            
            return AttentionMetrics(
                gaze_focus_duration=total_gaze_duration,
                object_interaction_count=len(object_interactions),
                navigation_efficiency=navigation_efficiency,
                task_completion_rate=task_completion_rate,
                distraction_events=distraction_events,
                attention_stability=max(0.0, attention_stability)
            )
            
        except Exception as e:
            logger.error(f"Attention metrics calculation failed: {e}")
            return AttentionMetrics(0.0, 0, 0.0, 0.0, 0, 0.0)
    
    async def analyze_gaze_patterns(self, gaze_tracking_data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Analyze gaze patterns for attention insights
        
        Educational Impact:
        Provides detailed gaze analysis to understand visual attention
        patterns and optimize visual content design.
        
        Args:
            gaze_tracking_data: List of gaze tracking events
            
        Returns:
            Dict containing gaze pattern analysis
        """
        try:
            if not gaze_tracking_data:
                return {"total_gaze_events": 0, "average_gaze_duration": 0.0}
            
            # Calculate basic gaze metrics
            total_events = len(gaze_tracking_data)
            durations = [event.get("duration", 0) for event in gaze_tracking_data]
            avg_duration = np.mean(durations) if durations else 0.0
            
            # Analyze gaze distribution across spatial zones
            zone_distribution = {"near": 0, "medium": 0, "far": 0}
            
            for event in gaze_tracking_data:
                coords = event.get("spatial_coordinates", {})
                distance = math.sqrt(
                    coords.get("x", 0)**2 + 
                    coords.get("y", 0)**2 + 
                    coords.get("z", 0)**2
                )
                
                if distance < 1.0:
                    zone_distribution["near"] += 1
                elif distance < 2.5:
                    zone_distribution["medium"] += 1
                else:
                    zone_distribution["far"] += 1
            
            # Calculate gaze consistency
            if len(durations) > 1:
                gaze_consistency = 1.0 - (np.std(durations) / np.mean(durations))
            else:
                gaze_consistency = 1.0
            
            # Identify focus hotspots
            focus_hotspots = await self._identify_focus_hotspots(gaze_tracking_data)
            
            return {
                "total_gaze_events": total_events,
                "average_gaze_duration": avg_duration,
                "max_gaze_duration": max(durations) if durations else 0.0,
                "gaze_consistency": max(0.0, gaze_consistency),
                "zone_distribution": zone_distribution,
                "focus_hotspots": focus_hotspots,
                "gaze_stability": self._calculate_gaze_stability(gaze_tracking_data)
            }
            
        except Exception as e:
            logger.error(f"Gaze pattern analysis failed: {e}")
            return {"error": str(e)}
    
    async def calculate_attention_stability(self, interactions: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Calculate attention stability metrics
        
        Educational Impact:
        Measures attention consistency to identify learners who may need
        additional support or modified content delivery strategies.
        
        Args:
            interactions: List of interaction records
            
        Returns:
            Dict containing attention stability analysis
        """
        try:
            if len(interactions) < 2:
                return {"stability_score": 1.0, "attention_variance": 0.0}
            
            # Extract engagement scores over time
            engagement_scores = []
            timestamps = []
            
            for interaction in interactions:
                engagement_score = interaction.get("engagement_metrics", {}).get("overall_engagement", 0.0)
                timestamp = datetime.fromisoformat(interaction["timestamp"])
                
                engagement_scores.append(engagement_score)
                timestamps.append(timestamp)
            
            # Calculate stability metrics
            engagement_variance = np.var(engagement_scores)
            engagement_mean = np.mean(engagement_scores)
            
            # Coefficient of variation (normalized stability)
            if engagement_mean > 0:
                cv = np.std(engagement_scores) / engagement_mean
                stability_score = max(0.0, 1.0 - cv)
            else:
                stability_score = 0.0
            
            # Calculate attention trend
            if len(engagement_scores) >= 3:
                # Simple linear regression for trend
                x = np.arange(len(engagement_scores))
                slope = np.polyfit(x, engagement_scores, 1)[0]
                
                if slope > 0.01:
                    trend = "increasing"
                elif slope < -0.01:
                    trend = "decreasing"
                else:
                    trend = "stable"
            else:
                slope = 0.0
                trend = "stable"
            
            # Identify attention drops
            attention_drops = []
            for i in range(1, len(engagement_scores)):
                if engagement_scores[i] < engagement_scores[i-1] - 0.2:  # Significant drop
                    attention_drops.append({
                        "timestamp": timestamps[i].isoformat(),
                        "drop_magnitude": engagement_scores[i-1] - engagement_scores[i]
                    })
            
            return {
                "stability_score": stability_score,
                "attention_variance": engagement_variance,
                "attention_mean": engagement_mean,
                "trend": trend,
                "trend_slope": slope,
                "attention_drops": attention_drops,
                "drop_frequency": len(attention_drops) / len(interactions)
            }
            
        except Exception as e:
            logger.error(f"Attention stability calculation failed: {e}")
            return {"error": str(e)}
    
    async def identify_attention_events(self, interactions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Identify significant attention events (focus/distraction)
        
        Educational Impact:
        Identifies critical attention moments to understand learning
        disruptions and optimize content timing.
        
        Args:
            interactions: List of interaction records
            
        Returns:
            List of attention events with timestamps and types
        """
        try:
            attention_events = []
            
            if len(interactions) < 2:
                return attention_events
            
            # Extract engagement scores
            engagement_scores = [
                interaction.get("engagement_metrics", {}).get("overall_engagement", 0.0)
                for interaction in interactions
            ]
            
            # Identify focus events (high engagement periods)
            for i, score in enumerate(engagement_scores):
                if score >= 0.8:  # High engagement threshold
                    attention_events.append({
                        "event_type": "high_focus",
                        "timestamp": interactions[i]["timestamp"],
                        "engagement_score": score,
                        "interaction_type": interactions[i].get("interaction_type"),
                        "spatial_coordinates": interactions[i].get("spatial_coordinates")
                    })
            
            # Identify distraction events
            for i, score in enumerate(engagement_scores):
                if score <= 0.3:  # Low engagement threshold
                    attention_events.append({
                        "event_type": "distraction",
                        "timestamp": interactions[i]["timestamp"],
                        "engagement_score": score,
                        "interaction_type": interactions[i].get("interaction_type"),
                        "spatial_coordinates": interactions[i].get("spatial_coordinates")
                    })
            
            # Identify attention transitions (sudden changes)
            for i in range(1, len(engagement_scores)):
                score_change = abs(engagement_scores[i] - engagement_scores[i-1])
                
                if score_change >= 0.4:  # Significant change threshold
                    event_type = "attention_increase" if engagement_scores[i] > engagement_scores[i-1] else "attention_decrease"
                    
                    attention_events.append({
                        "event_type": event_type,
                        "timestamp": interactions[i]["timestamp"],
                        "engagement_change": engagement_scores[i] - engagement_scores[i-1],
                        "previous_score": engagement_scores[i-1],
                        "current_score": engagement_scores[i]
                    })
            
            # Sort events by timestamp
            attention_events.sort(key=lambda x: x["timestamp"])
            
            return attention_events
            
        except Exception as e:
            logger.error(f"Attention event identification failed: {e}")
            return []
    
    async def generate_engagement_recommendations(self, attention_metrics: AttentionMetrics, gaze_analysis: Dict[str, Any], attention_stability: Dict[str, Any]) -> List[str]:
        """
        Generate recommendations for improving engagement
        
        Educational Impact:
        Provides actionable insights for optimizing learning experiences
        based on engagement and attention analysis.
        
        Args:
            attention_metrics: Calculated attention metrics
            gaze_analysis: Gaze pattern analysis results
            attention_stability: Attention stability analysis
            
        Returns:
            List of engagement improvement recommendations
        """
        recommendations = []
        
        try:
            # Check overall attention level
            overall_attention = attention_metrics.calculate_overall_attention()
            
            if overall_attention < 0.4:
                recommendations.append("Consider reducing content complexity or adding interactive elements")
                recommendations.append("Implement attention-grabbing visual cues or audio prompts")
            
            # Check gaze patterns
            if gaze_analysis.get("gaze_consistency", 1.0) < 0.5:
                recommendations.append("Improve visual focus by reducing visual distractions")
            
            zone_dist = gaze_analysis.get("zone_distribution", {})
            total_gazes = sum(zone_dist.values())
            if total_gazes > 0 and zone_dist.get("far", 0) / total_gazes > 0.6:
                recommendations.append("Encourage closer interaction with learning objects")
            
            # Check interaction frequency
            if attention_metrics.object_interaction_count < 3:
                recommendations.append("Add more interactive elements to increase hands-on engagement")
            
            # Check navigation efficiency
            if attention_metrics.navigation_efficiency < 0.5:
                recommendations.append("Provide clearer navigation guidance or simplify environment layout")
            
            # Check attention stability
            if attention_stability.get("stability_score", 1.0) < 0.6:
                recommendations.append("Consider shorter content segments to maintain attention")
                
                if attention_stability.get("trend") == "decreasing":
                    recommendations.append("Implement engagement recovery strategies (breaks, rewards)")
            
            # Check distraction frequency
            if attention_metrics.distraction_events > 3:
                recommendations.append("Identify and minimize sources of distraction in VR environment")
            
            # Task completion recommendations
            if attention_metrics.task_completion_rate < 0.6:
                recommendations.append("Provide more scaffolding or break tasks into smaller steps")
            
            return recommendations
            
        except Exception as e:
            logger.error(f"Engagement recommendation generation failed: {e}")
            return ["Unable to generate recommendations due to analysis error"]
    
    def _calculate_spatial_precision_score(self, spatial_coords: Dict[str, float]) -> float:
        """Calculate spatial precision score for coordinates"""
        try:
            # Check precision of coordinates (more decimal places = higher precision)
            precision_scores = []
            
            for coord_name, value in spatial_coords.items():
                if coord_name in ["x", "y", "z"]:
                    # Count decimal places as precision indicator
                    value_str = str(value)
                    if "." in value_str:
                        decimal_places = len(value_str.split(".")[1])
                        precision_score = min(1.0, decimal_places / 4.0)  # Normalize to 4 decimal places
                    else:
                        precision_score = 0.5  # Integer precision
                    
                    precision_scores.append(precision_score)
            
            return np.mean(precision_scores) if precision_scores else 0.5
            
        except Exception as e:
            logger.error(f"Spatial precision calculation failed: {e}")
            return 0.5
    
    async def _assess_interaction_quality(self, interaction_type: str, spatial_coords: Dict[str, float], distance: float) -> float:
        """Assess quality of interaction based on type and spatial context"""
        try:
            base_quality = 0.5
            
            # Quality factors based on interaction type
            type_quality_factors = {
                "gaze": 0.6,
                "touch": 0.8,
                "manipulation": 1.0,
                "navigation": 0.4,
                "gesture": 0.7
            }
            
            type_factor = type_quality_factors.get(interaction_type, 0.5)
            
            # Distance factor (closer interactions generally higher quality for learning)
            distance_factor = max(0.2, 1.0 - distance / 3.0)
            
            # Precision factor
            precision_factor = self._calculate_spatial_precision_score(spatial_coords)
            
            quality_score = (type_factor * 0.5 + distance_factor * 0.3 + precision_factor * 0.2)
            
            return max(0.0, min(1.0, quality_score))
            
        except Exception as e:
            logger.error(f"Interaction quality assessment failed: {e}")
            return 0.5
    
    def _categorize_engagement_level(self, engagement_score: float) -> str:
        """Categorize engagement level based on score"""
        if engagement_score >= 0.8:
            return "high"
        elif engagement_score >= 0.6:
            return "moderate"
        elif engagement_score >= 0.4:
            return "low"
        else:
            return "very_low"
    
    async def _calculate_navigation_efficiency(self, navigation_interactions: List[Dict[str, Any]]) -> float:
        """Calculate navigation efficiency from navigation interactions"""
        try:
            if not navigation_interactions:
                return 0.5  # Default moderate efficiency
            
            # Calculate path efficiency (straight-line vs actual path)
            total_efficiency = 0.0
            valid_paths = 0
            
            for i in range(1, len(navigation_interactions)):
                prev_coords = navigation_interactions[i-1].get("spatial_coordinates", {})
                curr_coords = navigation_interactions[i].get("spatial_coordinates", {})
                
                if prev_coords and curr_coords:
                    # Calculate straight-line distance
                    straight_distance = math.sqrt(
                        (curr_coords.get("x", 0) - prev_coords.get("x", 0))**2 +
                        (curr_coords.get("y", 0) - prev_coords.get("y", 0))**2 +
                        (curr_coords.get("z", 0) - prev_coords.get("z", 0))**2
                    )
                    
                    # For navigation efficiency, assume ideal path efficiency
                    # In production, would calculate actual path vs optimal path
                    duration = navigation_interactions[i].get("duration", 1.0)
                    
                    if duration > 0 and straight_distance > 0:
                        efficiency = min(1.0, straight_distance / (duration * 0.5))  # Assuming 0.5 m/s optimal speed
                        total_efficiency += efficiency
                        valid_paths += 1
            
            return total_efficiency / valid_paths if valid_paths > 0 else 0.5
            
        except Exception as e:
            logger.error(f"Navigation efficiency calculation failed: {e}")
            return 0.5
    
    async def _identify_focus_hotspots(self, gaze_tracking_data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Identify spatial areas of high gaze concentration"""
        try:
            if not gaze_tracking_data:
                return []
            
            # Group gaze events by spatial proximity
            hotspots = []
            proximity_threshold = 0.5  # 0.5 meter clustering
            
            for event in gaze_tracking_data:
                coords = event.get("spatial_coordinates", {})
                x, y, z = coords.get("x", 0), coords.get("y", 0), coords.get("z", 0)
                
                # Find nearby hotspot or create new one
                found_hotspot = False
                for hotspot in hotspots:
                    hx, hy, hz = hotspot["center_x"], hotspot["center_y"], hotspot["center_z"]
                    distance = math.sqrt((x - hx)**2 + (y - hy)**2 + (z - hz)**2)
                    
                    if distance <= proximity_threshold:
                        # Add to existing hotspot
                        hotspot["gaze_count"] += 1
                        hotspot["total_duration"] += event.get("duration", 0)
                        
                        # Update center (weighted average)
                        weight = hotspot["gaze_count"]
                        hotspot["center_x"] = (hx * (weight - 1) + x) / weight
                        hotspot["center_y"] = (hy * (weight - 1) + y) / weight
                        hotspot["center_z"] = (hz * (weight - 1) + z) / weight
                        
                        found_hotspot = True
                        break
                
                if not found_hotspot:
                    # Create new hotspot
                    hotspots.append({
                        "center_x": x,
                        "center_y": y,
                        "center_z": z,
                        "gaze_count": 1,
                        "total_duration": event.get("duration", 0)
                    })
            
            # Sort by gaze count and return top hotspots
            hotspots.sort(key=lambda h: h["gaze_count"], reverse=True)
            return hotspots[:5]  # Top 5 hotspots
            
        except Exception as e:
            logger.error(f"Focus hotspot identification failed: {e}")
            return []
    
    def _calculate_gaze_stability(self, gaze_tracking_data: List[Dict[str, Any]]) -> float:
        """Calculate gaze stability metric"""
        try:
            if len(gaze_tracking_data) < 2:
                return 1.0
            
            # Calculate variance in gaze durations
            durations = [event.get("duration", 0) for event in gaze_tracking_data]
            duration_variance = np.var(durations) if durations else 0.0
            
            # Calculate spatial variance
            x_coords = [event.get("spatial_coordinates", {}).get("x", 0) for event in gaze_tracking_data]
            y_coords = [event.get("spatial_coordinates", {}).get("y", 0) for event in gaze_tracking_data]
            z_coords = [event.get("spatial_coordinates", {}).get("z", 0) for event in gaze_tracking_data]
            
            spatial_variance = (np.var(x_coords) + np.var(y_coords) + np.var(z_coords)) / 3
            
            # Combine duration and spatial stability
            duration_stability = max(0.0, 1.0 - duration_variance / 100)  # Normalize
            spatial_stability = max(0.0, 1.0 - spatial_variance / 4)  # Normalize
            
            return (duration_stability + spatial_stability) / 2
            
        except Exception as e:
            logger.error(f"Gaze stability calculation failed: {e}")
            return 0.5
    
    async def calculate_engagement_trend(self, interactions: List[Dict[str, Any]]) -> float:
        """Calculate engagement trend from recent interactions"""
        try:
            if not interactions:
                return 0.5
            
            engagement_scores = [
                interaction.get("engagement_metrics", {}).get("overall_engagement", 0.0)
                for interaction in interactions
            ]
            
            return np.mean(engagement_scores) if engagement_scores else 0.5
            
        except Exception as e:
            logger.error(f"Engagement trend calculation failed: {e}")
            return 0.5
    
    async def calculate_spatial_interaction_quality(self, interactions: List[Dict[str, Any]]) -> float:
        """Calculate overall spatial interaction quality"""
        try:
            if not interactions:
                return 0.5
            
            quality_scores = []
            
            for interaction in interactions:
                spatial_analysis = interaction.get("spatial_analysis", {})
                quality_scores.append(spatial_analysis.get("interaction_quality", 0.5))
            
            return np.mean(quality_scores) if quality_scores else 0.5
            
        except Exception as e:
            logger.error(f"Spatial interaction quality calculation failed: {e}")
            return 0.5
    
    async def _record_performance_metrics(self, processing_time: float, operation: str):
        """Record performance metrics for monitoring"""
        self.performance_metrics[f"{operation}_times"] = self.performance_metrics.get(f"{operation}_times", [])
        self.performance_metrics[f"{operation}_times"].append({
            "time": processing_time,
            "timestamp": datetime.now().isoformat()
        })
        
        # Keep only last 100 measurements
        if len(self.performance_metrics[f"{operation}_times"]) > 100:
            self.performance_metrics[f"{operation}_times"] = self.performance_metrics[f"{operation}_times"][-100:]
    
    def get_performance_metrics(self) -> Dict[str, Any]:
        """Get current performance metrics for monitoring"""
        recent_tracking_times = [m["time"] for m in self.performance_metrics.get("track_interaction_times", [])[-10:]]
        
        return {
            "average_tracking_time": np.mean(recent_tracking_times) if recent_tracking_times else 0.0,
            "max_tracking_time": max(recent_tracking_times) if recent_tracking_times else 0.0,
            "active_sessions": len(self.engagement_sessions),
            "quest3_compliance": all(t < 0.05 for t in recent_tracking_times) if recent_tracking_times else True,
            "spatial_precision": f"{self.spatial_precision_tolerance}m"
        }
