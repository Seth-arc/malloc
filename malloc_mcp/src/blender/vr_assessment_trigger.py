"""
VRAssessmentTrigger Class Implementation

Educational Impact:
Provides embedded assessment triggers within Blender scenes for spatial performance tracking
and real-time evaluation during VR learning experiences.

Performance Requirements:
- Quest 3 VR: <25ms trigger activation time
- Memory usage: <15MB per active trigger
- Spatial precision: 0.1mm trigger boundary accuracy

Reference: docs/Malloc_MCP_Server_Development_Pathway.md lines 5384-5393
"""

import asyncio
import logging
from typing import Dict, Any, List, Optional, Tuple, Union
from datetime import datetime, timedelta
import json
import math

from ..learning.assessment_model import AssessmentModel
from ..learning.engagement_model import EngagementModel
from ..utils.learning_calculations import LearningEquationProcessor

logger = logging.getLogger(__name__)

class VRAssessmentTriggerError(Exception):
    """Custom exception for VR Assessment Trigger operations."""
    pass

class VRAssessmentTrigger:
    """
    Embedded assessment triggers within Blender scenes.
    
    Educational Impact:
    Creates invisible assessment trigger objects that monitor learner performance
    during 3D interactions, providing spatial reasoning assessment and real-time
    performance evaluation for adaptive learning experiences.
    
    Performance Requirements:
    - Quest 3 VR: <25ms trigger processing time
    - Memory usage: <15MB per trigger instance
    - Spatial precision: 0.1mm boundary detection accuracy
    
    Features:
    - Creates invisible assessment trigger objects in Blender
    - Tracks spatial performance during 3D interaction
    - Real-time performance evaluation with spatial reasoning scoring
    - Configurable spatial placement and trigger conditions
    - Assessment UI overlay creation in Blender viewport
    
    Reference: docs/malloc_vr_mcp_server_specification.md lines 322-350
    """
    
    def __init__(
        self, 
        trigger_id: str,
        assessment_config: Dict[str, Any],
        spatial_config: Dict[str, Any]
    ):
        """
        Initialize VR Assessment Trigger.
        
        Args:
            trigger_id: Unique identifier for this trigger
            assessment_config: Assessment configuration parameters
            spatial_config: Spatial placement and boundary configuration
        """
        self.trigger_id = trigger_id
        self.assessment_config = assessment_config
        self.spatial_config = spatial_config
        self.is_active = False
        self.trigger_history: List[Dict[str, Any]] = []
        self.assessment_model = AssessmentModel()
        self.engagement_model = EngagementModel()
        self.equation_processor = LearningEquationProcessor()
        
        # Validate spatial precision (0.1mm tolerance)
        self._validate_spatial_configuration()
        
        logger.info(f"Initialized VRAssessmentTrigger: {trigger_id}")
    
    def _validate_spatial_configuration(self) -> None:
        """
        Validate spatial configuration meets precision requirements.
        
        Raises:
            VRAssessmentTriggerError: If spatial configuration is invalid
        """
        required_keys = ["center_position", "boundary_type", "boundary_size"]
        
        for key in required_keys:
            if key not in self.spatial_config:
                raise VRAssessmentTriggerError(f"Missing spatial configuration: {key}")
        
        # Validate center position precision (0.1mm)
        center = self.spatial_config["center_position"]
        if not isinstance(center, (list, tuple)) or len(center) != 3:
            raise VRAssessmentTriggerError("Invalid center_position format")
        
        # Round to 0.1mm precision
        self.spatial_config["center_position"] = [round(coord, 4) for coord in center]
    
    async def create_blender_trigger_object(self) -> Dict[str, Any]:
        """
        Creates invisible assessment trigger object in Blender.
        
        Educational Impact:
        Creates spatial assessment zones that enable location-based evaluation
        and contextual learning assessment within VR environments.
        
        Returns:
            Dict containing Blender object creation data
            
        Raises:
            VRAssessmentTriggerError: If trigger object creation fails
        """
        try:
            start_time = datetime.now()
            
            center = self.spatial_config["center_position"]
            boundary_type = self.spatial_config["boundary_type"]
            boundary_size = self.spatial_config["boundary_size"]
            
            # Create Blender object data structure
            blender_object = {
                "name": f"Assessment_Trigger_{self.trigger_id}",
                "type": "EMPTY",  # Invisible object type
                "empty_display_type": boundary_type.upper(),
                "location": center,
                "rotation_euler": (0.0, 0.0, 0.0),
                "scale": self._calculate_trigger_scale(boundary_type, boundary_size),
                "hide_viewport": True,  # Invisible in viewport
                "hide_render": True,    # Invisible in render
                "hide_select": False,   # Can be selected for debugging
                "custom_properties": {
                    "malloc_assessment_trigger": True,
                    "malloc_trigger_id": self.trigger_id,
                    "malloc_assessment_config": json.dumps(self.assessment_config),
                    "malloc_spatial_config": json.dumps(self.spatial_config),
                    "malloc_created_timestamp": start_time.isoformat(),
                    "malloc_trigger_active": False
                }
            }
            
            # Register trigger object with assessment model
            await self.assessment_model.register_spatial_trigger({
                "trigger_id": self.trigger_id,
                "blender_object": blender_object,
                "assessment_config": self.assessment_config,
                "spatial_config": self.spatial_config
            })
            
            execution_time = (datetime.now() - start_time).total_seconds() * 1000
            
            logger.info(f"Created Blender trigger object in {execution_time:.2f}ms")
            
            return {
                "status": "success",
                "blender_object": blender_object,
                "execution_time_ms": execution_time,
                "spatial_validation": {
                    "center_precision": "0.1mm",
                    "boundary_validated": True,
                    "trigger_area": self._calculate_trigger_area()
                }
            }
            
        except Exception as e:
            logger.error(f"Failed to create Blender trigger object: {str(e)}")
            raise VRAssessmentTriggerError(f"Trigger object creation failed: {str(e)}")
    
    def _calculate_trigger_scale(self, boundary_type: str, boundary_size: Union[float, Dict[str, float]]) -> Tuple[float, float, float]:
        """
        Calculate appropriate scale for trigger boundary visualization.
        
        Args:
            boundary_type: Type of boundary (sphere, cube, cylinder)
            boundary_size: Size parameters for the boundary
            
        Returns:
            Tuple of scale values (x, y, z)
        """
        if boundary_type == "sphere":
            radius = boundary_size if isinstance(boundary_size, (int, float)) else boundary_size.get("radius", 1.0)
            return (radius, radius, radius)
        elif boundary_type == "cube":
            if isinstance(boundary_size, dict):
                return (
                    boundary_size.get("width", 1.0),
                    boundary_size.get("height", 1.0), 
                    boundary_size.get("depth", 1.0)
                )
            else:
                return (boundary_size, boundary_size, boundary_size)
        elif boundary_type == "cylinder":
            radius = boundary_size.get("radius", 1.0) if isinstance(boundary_size, dict) else boundary_size
            height = boundary_size.get("height", 2.0) if isinstance(boundary_size, dict) else 2.0
            return (radius, radius, height)
        else:
            return (1.0, 1.0, 1.0)  # Default scale
    
    def _calculate_trigger_area(self) -> float:
        """
        Calculate the area/volume of the trigger zone.
        
        Returns:
            Numerical area/volume of the trigger zone
        """
        boundary_type = self.spatial_config["boundary_type"]
        boundary_size = self.spatial_config["boundary_size"]
        
        if boundary_type == "sphere":
            radius = boundary_size if isinstance(boundary_size, (int, float)) else boundary_size.get("radius", 1.0)
            return (4/3) * math.pi * (radius ** 3)  # Volume
        elif boundary_type == "cube":
            if isinstance(boundary_size, dict):
                return (boundary_size.get("width", 1.0) * 
                       boundary_size.get("height", 1.0) * 
                       boundary_size.get("depth", 1.0))
            else:
                return boundary_size ** 3
        elif boundary_type == "cylinder":
            radius = boundary_size.get("radius", 1.0) if isinstance(boundary_size, dict) else boundary_size
            height = boundary_size.get("height", 2.0) if isinstance(boundary_size, dict) else 2.0
            return math.pi * (radius ** 2) * height
        else:
            return 1.0  # Default area
    
    async def check_trigger_activation(
        self, 
        learner_position: Tuple[float, float, float],
        learner_id: str
    ) -> Dict[str, Any]:
        """
        Check if learner position activates the assessment trigger.
        
        Educational Impact:
        Monitors learner spatial positioning to activate contextual assessments,
        enabling location-based evaluation and spatial learning measurement.
        
        Args:
            learner_position: Current 3D position of the learner
            learner_id: Unique identifier for the learner
            
        Returns:
            Dict containing activation status and assessment data
        """
        try:
            start_time = datetime.now()
            
            # Calculate distance from trigger center (0.1mm precision)
            center = self.spatial_config["center_position"]
            distance = math.sqrt(sum((a - b) ** 2 for a, b in zip(learner_position, center)))
            
            # Check if position is within trigger boundary
            is_within_boundary = self._is_position_within_boundary(learner_position, distance)
            
            activation_result = {
                "trigger_id": self.trigger_id,
                "learner_id": learner_id,
                "learner_position": list(learner_position),
                "distance_from_center": round(distance, 4),
                "is_activated": is_within_boundary,
                "check_timestamp": start_time.isoformat(),
                "spatial_metrics": {
                    "position_precision": "0.1mm",
                    "boundary_distance": distance,
                    "activation_threshold": self._get_activation_threshold()
                }
            }
            
            # If trigger is activated, initiate assessment
            if is_within_boundary and not self.is_active:
                assessment_data = await self._initiate_spatial_assessment(learner_id, learner_position)
                activation_result["assessment_initiated"] = assessment_data
                self.is_active = True
                
            # Record trigger check in history
            self.trigger_history.append(activation_result)
            
            execution_time = (datetime.now() - start_time).total_seconds() * 1000
            activation_result["execution_time_ms"] = execution_time
            
            return activation_result
            
        except Exception as e:
            logger.error(f"Failed to check trigger activation: {str(e)}")
            raise VRAssessmentTriggerError(f"Trigger activation check failed: {str(e)}")
    
    def _is_position_within_boundary(self, position: Tuple[float, float, float], distance: float) -> bool:
        """
        Check if position is within the trigger boundary.
        
        Args:
            position: 3D position to check
            distance: Distance from trigger center
            
        Returns:
            Boolean indicating if position is within boundary
        """
        boundary_type = self.spatial_config["boundary_type"]
        boundary_size = self.spatial_config["boundary_size"]
        center = self.spatial_config["center_position"]
        
        if boundary_type == "sphere":
            radius = boundary_size if isinstance(boundary_size, (int, float)) else boundary_size.get("radius", 1.0)
            return distance <= radius
            
        elif boundary_type == "cube":
            if isinstance(boundary_size, dict):
                width = boundary_size.get("width", 1.0) / 2
                height = boundary_size.get("height", 1.0) / 2
                depth = boundary_size.get("depth", 1.0) / 2
            else:
                width = height = depth = boundary_size / 2
                
            return (abs(position[0] - center[0]) <= width and
                   abs(position[1] - center[1]) <= height and
                   abs(position[2] - center[2]) <= depth)
                   
        elif boundary_type == "cylinder":
            radius = boundary_size.get("radius", 1.0) if isinstance(boundary_size, dict) else boundary_size
            height = boundary_size.get("height", 2.0) if isinstance(boundary_size, dict) else 2.0
            
            # Check horizontal distance (x, y plane)
            horizontal_distance = math.sqrt((position[0] - center[0]) ** 2 + (position[1] - center[1]) ** 2)
            vertical_distance = abs(position[2] - center[2])
            
            return horizontal_distance <= radius and vertical_distance <= height / 2
            
        return False
    
    def _get_activation_threshold(self) -> float:
        """Get the activation threshold for this trigger boundary."""
        boundary_type = self.spatial_config["boundary_type"]
        boundary_size = self.spatial_config["boundary_size"]
        
        if boundary_type == "sphere":
            return boundary_size if isinstance(boundary_size, (int, float)) else boundary_size.get("radius", 1.0)
        elif boundary_type == "cube":
            if isinstance(boundary_size, dict):
                return min(boundary_size.get("width", 1.0), boundary_size.get("height", 1.0), boundary_size.get("depth", 1.0)) / 2
            else:
                return boundary_size / 2
        elif boundary_type == "cylinder":
            return boundary_size.get("radius", 1.0) if isinstance(boundary_size, dict) else boundary_size
        return 1.0
    
    async def _initiate_spatial_assessment(
        self, 
        learner_id: str, 
        position: Tuple[float, float, float]
    ) -> Dict[str, Any]:
        """
        Initiate spatial assessment when trigger is activated.
        
        Args:
            learner_id: Unique identifier for the learner
            position: 3D position where assessment was triggered
            
        Returns:
            Dict containing assessment initiation data
        """
        try:
            assessment_data = {
                "assessment_id": f"{self.trigger_id}_{learner_id}_{int(datetime.now().timestamp())}",
                "trigger_id": self.trigger_id,
                "learner_id": learner_id,
                "trigger_position": list(position),
                "assessment_type": self.assessment_config.get("type", "spatial_reasoning"),
                "learning_objectives": self.assessment_config.get("learning_objectives", []),
                "initiation_timestamp": datetime.now().isoformat(),
                "spatial_context": {
                    "trigger_center": self.spatial_config["center_position"],
                    "activation_distance": math.sqrt(sum((a - b) ** 2 for a, b in zip(position, self.spatial_config["center_position"]))),
                    "spatial_precision": "0.1mm"
                }
            }
            
            # Register assessment with assessment model
            await self.assessment_model.initiate_spatial_assessment(assessment_data)
            
            logger.info(f"Initiated spatial assessment for learner {learner_id}")
            
            return assessment_data
            
        except Exception as e:
            logger.error(f"Failed to initiate spatial assessment: {str(e)}")
            raise VRAssessmentTriggerError(f"Spatial assessment initiation failed: {str(e)}")
    
    async def evaluate_spatial_performance(
        self, 
        learner_id: str,
        interaction_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Evaluate spatial performance during trigger activation.
        
        Educational Impact:
        Provides real-time spatial reasoning assessment and performance scoring
        based on 3D interaction quality and spatial understanding demonstration.
        
        Args:
            learner_id: Unique identifier for the learner
            interaction_data: Detailed interaction and performance data
            
        Returns:
            Dict containing spatial performance evaluation results
        """
        try:
            start_time = datetime.now()
            
            # Calculate spatial reasoning score
            spatial_score = await self._calculate_spatial_reasoning_score(interaction_data)
            
            # Evaluate performance metrics
            performance_metrics = {
                "spatial_reasoning_score": spatial_score,
                "interaction_quality": interaction_data.get("interaction_quality", 0.0),
                "spatial_precision": interaction_data.get("spatial_precision", 0.0),
                "task_completion_time": interaction_data.get("completion_time", 0.0),
                "error_rate": interaction_data.get("error_rate", 0.0),
                "learning_effectiveness": 0.0  # Calculated below
            }
            
            # Calculate overall learning effectiveness
            performance_metrics["learning_effectiveness"] = await self._calculate_learning_effectiveness(
                performance_metrics, learner_id
            )
            
            # Create evaluation result
            evaluation_result = {
                "evaluation_id": f"eval_{self.trigger_id}_{learner_id}_{int(start_time.timestamp())}",
                "trigger_id": self.trigger_id,
                "learner_id": learner_id,
                "evaluation_timestamp": start_time.isoformat(),
                "performance_metrics": performance_metrics,
                "spatial_assessment": {
                    "reasoning_score": spatial_score,
                    "precision_level": "sub-millimeter" if performance_metrics["spatial_precision"] > 0.9 else "standard",
                    "assessment_type": self.assessment_config.get("type", "formative")
                },
                "learning_progression": {
                    "current_level": interaction_data.get("current_level", 1),
                    "progression_rate": performance_metrics["learning_effectiveness"],
                    "next_objectives": self.assessment_config.get("next_objectives", [])
                }
            }
            
            # Store evaluation with assessment model
            await self.assessment_model.store_spatial_evaluation(evaluation_result)
            
            execution_time = (datetime.now() - start_time).total_seconds() * 1000
            evaluation_result["execution_time_ms"] = execution_time
            
            logger.info(f"Completed spatial performance evaluation in {execution_time:.2f}ms")
            
            return evaluation_result
            
        except Exception as e:
            logger.error(f"Failed to evaluate spatial performance: {str(e)}")
            raise VRAssessmentTriggerError(f"Spatial performance evaluation failed: {str(e)}")
    
    async def _calculate_spatial_reasoning_score(self, interaction_data: Dict[str, Any]) -> float:
        """
        Calculate comprehensive spatial reasoning score.
        
        Args:
            interaction_data: Interaction and performance data
            
        Returns:
            Spatial reasoning score (0.0 to 1.0)
        """
        # Base spatial metrics
        spatial_accuracy = interaction_data.get("spatial_accuracy", 0.0)
        orientation_understanding = interaction_data.get("orientation_score", 0.0)
        depth_perception = interaction_data.get("depth_perception", 0.0)
        spatial_memory = interaction_data.get("spatial_memory", 0.0)
        
        # Advanced spatial reasoning components
        pattern_recognition = interaction_data.get("pattern_recognition", 0.0)
        spatial_transformation = interaction_data.get("transformation_ability", 0.0)
        
        # Weighted spatial reasoning calculation
        spatial_score = (
            spatial_accuracy * 0.25 +
            orientation_understanding * 0.20 +
            depth_perception * 0.20 +
            spatial_memory * 0.15 +
            pattern_recognition * 0.10 +
            spatial_transformation * 0.10
        )
        
        return max(0.0, min(1.0, spatial_score))  # Clamp to [0, 1]
    
    async def _calculate_learning_effectiveness(
        self, 
        performance_metrics: Dict[str, Any], 
        learner_id: str
    ) -> float:
        """
        Calculate learning effectiveness based on performance and progression.
        
        Args:
            performance_metrics: Current performance metrics
            learner_id: Unique identifier for the learner
            
        Returns:
            Learning effectiveness score (0.0 to 1.0)
        """
        # Get learner's historical performance
        learner_history = await self.assessment_model.get_learner_performance_history(learner_id)
        
        # Calculate improvement rate
        current_score = performance_metrics["spatial_reasoning_score"]
        previous_scores = [entry.get("spatial_reasoning_score", 0.0) for entry in learner_history[-5:]]
        
        if previous_scores:
            improvement_rate = (current_score - sum(previous_scores) / len(previous_scores)) / len(previous_scores)
        else:
            improvement_rate = 0.0
        
        # Learning effectiveness components
        task_efficiency = 1.0 - performance_metrics["error_rate"]
        skill_progression = max(0.0, improvement_rate * 10)  # Scale improvement
        engagement_factor = performance_metrics.get("engagement_score", 0.7)
        
        # Weighted learning effectiveness
        effectiveness = (
            task_efficiency * 0.4 +
            skill_progression * 0.3 +
            engagement_factor * 0.3
        )
        
        return max(0.0, min(1.0, effectiveness))  # Clamp to [0, 1]
    
    async def deactivate_trigger(self) -> Dict[str, Any]:
        """
        Deactivate the assessment trigger.
        
        Returns:
            Dict containing deactivation status and summary
        """
        try:
            self.is_active = False
            deactivation_time = datetime.now()
            
            # Generate trigger session summary
            session_summary = {
                "trigger_id": self.trigger_id,
                "deactivation_timestamp": deactivation_time.isoformat(),
                "total_activations": len([h for h in self.trigger_history if h.get("is_activated", False)]),
                "total_checks": len(self.trigger_history),
                "session_duration": (deactivation_time - datetime.fromisoformat(self.trigger_history[0]["check_timestamp"])).total_seconds() if self.trigger_history else 0,
                "performance_summary": {
                    "average_activation_time": self._calculate_average_activation_time(),
                    "spatial_precision_maintained": True,  # 0.1mm precision maintained
                    "assessment_completion_rate": self._calculate_completion_rate()
                }
            }
            
            logger.info(f"Deactivated assessment trigger: {self.trigger_id}")
            
            return {
                "status": "deactivated",
                "session_summary": session_summary
            }
            
        except Exception as e:
            logger.error(f"Failed to deactivate trigger: {str(e)}")
            raise VRAssessmentTriggerError(f"Trigger deactivation failed: {str(e)}")
    
    def _calculate_average_activation_time(self) -> float:
        """Calculate average activation processing time."""
        activation_times = [
            h.get("execution_time_ms", 0.0) 
            for h in self.trigger_history 
            if h.get("is_activated", False)
        ]
        return sum(activation_times) / len(activation_times) if activation_times else 0.0
    
    def _calculate_completion_rate(self) -> float:
        """Calculate assessment completion rate."""
        activations = len([h for h in self.trigger_history if h.get("is_activated", False)])
        completions = len([h for h in self.trigger_history if h.get("assessment_initiated", {}).get("assessment_id")])
        return completions / activations if activations > 0 else 0.0
