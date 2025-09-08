"""
Educational Metadata Integration System

Educational Impact:
Provides comprehensive educational metadata integration with scene properties and real-time updates,
enabling persistent learning data storage and adaptive content delivery in Blender-based VR learning.

Performance Requirements:
- Quest 3 VR: <50ms metadata operations
- Memory usage: <20MB per metadata system
- Update frequency: Real-time updates every 5 seconds

Reference: docs/Malloc_MCP_Server_Development_Pathway.md lines 5418-5423
"""

import asyncio
import logging
from typing import Dict, Any, List, Optional, Tuple, Union
from datetime import datetime, timedelta
import json
import uuid
import hashlib

from ..learning.knowledge_model import KnowledgeModel
from ..learning.learner_model import LearnerModel
from ..learning.assessment_model import AssessmentModel
from ..utils.learning_calculations import LearningEquationProcessor

logger = logging.getLogger(__name__)

class EducationalMetadataError(Exception):
    """Custom exception for Educational Metadata operations."""
    pass

class EducationalMetadataManager:
    """
    Educational metadata integration system for Blender scenes.
    
    Educational Impact:
    Manages embedded learning metadata in Blender scenes, providing persistent educational
    data storage, real-time learning progress tracking, and adaptive content delivery
    based on learner performance and progress.
    
    Performance Requirements:
    - Quest 3 VR: <50ms for metadata operations
    - Memory usage: <20MB per active metadata system
    - Real-time updates: Every 5 seconds maximum
    - Spatial precision: 0.1mm accuracy for educational object placement
    
    Features:
    - Scene Property Embedding: Learning unit IDs, objectives, prerequisites, duration
    - Assessment Configuration: Trigger conditions, spatial placement, learning objectives
    - Real-time Updates: Dynamic metadata modification based on learning progress
    - Educational Object Detection: Automatic identification and tracking of learning content
    
    Reference: docs/Malloc_MCP_Server_Development_Pathway.md lines 5418-5423
    """
    
    def __init__(self, scene_name: str, metadata_config: Dict[str, Any]):
        """
        Initialize Educational Metadata Manager.
        
        Args:
            scene_name: Name of the Blender scene to manage metadata for
            metadata_config: Configuration parameters for metadata management
        """
        self.scene_name = scene_name
        self.metadata_config = metadata_config
        self.manager_id = str(uuid.uuid4())
        self.scene_metadata: Dict[str, Any] = {}
        self.educational_objects: Dict[str, Dict[str, Any]] = {}
        self.assessment_configurations: Dict[str, Dict[str, Any]] = {}
        self.real_time_updates_active = False
        
        # Initialize learning models
        self.knowledge_model = KnowledgeModel()
        self.learner_model = LearnerModel()
        self.assessment_model = AssessmentModel()
        self.equation_processor = LearningEquationProcessor()
        
        # Initialize metadata structure
        self._initialize_metadata_structure()
        
        logger.info(f"Initialized EducationalMetadataManager for scene: {scene_name}")
    
    def _initialize_metadata_structure(self) -> None:
        """Initialize the base metadata structure for the scene."""
        self.scene_metadata = {
            "manager_id": self.manager_id,
            "scene_name": self.scene_name,
            "created_timestamp": datetime.now().isoformat(),
            "metadata_version": "1.0",
            "educational_context": {
                "learning_domain": self.metadata_config.get("learning_domain", "general"),
                "target_audience": self.metadata_config.get("target_audience", "students"),
                "difficulty_level": self.metadata_config.get("difficulty_level", "intermediate"),
                "estimated_duration_minutes": self.metadata_config.get("duration", 30)
            },
            "scene_properties": {
                "malloc_scene_type": "educational_vr",
                "malloc_metadata_manager": self.manager_id,
                "malloc_learning_enabled": True,
                "malloc_created": datetime.now().isoformat()
            },
            "learning_units": {},
            "assessment_triggers": {},
            "adaptive_parameters": {
                "personalization_level": "medium",
                "difficulty_adaptation": True,
                "content_sequencing": "adaptive",
                "feedback_frequency": "real_time"
            },
            "tracking_data": {
                "learner_interactions": {},
                "learning_progress": {},
                "engagement_metrics": {},
                "assessment_results": {}
            }
        }
    
    async def embed_learning_unit_metadata(
        self,
        unit_id: str,
        unit_data: Dict[str, Any],
        spatial_placement: Optional[Tuple[float, float, float]] = None
    ) -> Dict[str, Any]:
        """
        Embed learning unit metadata in scene properties.
        
        Educational Impact:
        Creates persistent educational data storage within Blender scenes,
        enabling context-aware learning experiences and progress tracking.
        
        Args:
            unit_id: Unique identifier for the learning unit
            unit_data: Complete learning unit data and metadata
            spatial_placement: Optional 3D position for spatial learning context
            
        Returns:
            Dict containing embedding results and metadata references
            
        Raises:
            EducationalMetadataError: If metadata embedding fails
        """
        try:
            start_time = datetime.now()
            
            # Validate required unit data
            required_fields = ["title", "objectives", "prerequisites", "content_type"]
            for field in required_fields:
                if field not in unit_data:
                    raise EducationalMetadataError(f"Missing required unit field: {field}")
            
            # Create comprehensive learning unit metadata
            unit_metadata = {
                "unit_id": unit_id,
                "title": unit_data["title"],
                "description": unit_data.get("description", ""),
                "objectives": unit_data["objectives"],
                "prerequisites": unit_data["prerequisites"],
                "content_type": unit_data["content_type"],
                "difficulty_level": unit_data.get("difficulty_level", "intermediate"),
                "estimated_duration": unit_data.get("duration_minutes", 15),
                "spatial_placement": {
                    "x": round(spatial_placement[0], 4) if spatial_placement else 0.0,
                    "y": round(spatial_placement[1], 4) if spatial_placement else 0.0,
                    "z": round(spatial_placement[2], 4) if spatial_placement else 0.0
                } if spatial_placement else None,
                "learning_metadata": {
                    "competency_mapping": unit_data.get("competencies", []),
                    "assessment_criteria": unit_data.get("assessment_criteria", []),
                    "learning_activities": unit_data.get("activities", []),
                    "multimedia_resources": unit_data.get("resources", [])
                },
                "adaptive_properties": {
                    "difficulty_adaptable": unit_data.get("adaptive_difficulty", True),
                    "content_variants": unit_data.get("content_variants", []),
                    "personalization_options": unit_data.get("personalization", {}),
                    "prerequisite_flexibility": unit_data.get("flexible_prerequisites", False)
                },
                "embedding_metadata": {
                    "embedded_timestamp": start_time.isoformat(),
                    "metadata_hash": self._calculate_metadata_hash(unit_data),
                    "version": "1.0",
                    "manager_id": self.manager_id
                }
            }
            
            # Store unit metadata
            self.scene_metadata["learning_units"][unit_id] = unit_metadata
            
            # Create Blender scene properties for this unit
            scene_properties = {
                f"malloc_unit_{unit_id}_title": unit_data["title"],
                f"malloc_unit_{unit_id}_objectives": json.dumps(unit_data["objectives"]),
                f"malloc_unit_{unit_id}_prerequisites": json.dumps(unit_data["prerequisites"]),
                f"malloc_unit_{unit_id}_duration": str(unit_data.get("duration_minutes", 15)),
                f"malloc_unit_{unit_id}_difficulty": unit_data.get("difficulty_level", "intermediate"),
                f"malloc_unit_{unit_id}_metadata": json.dumps(unit_metadata["learning_metadata"]),
                f"malloc_unit_{unit_id}_spatial": json.dumps(unit_metadata["spatial_placement"]) if spatial_placement else "null"
            }
            
            # Update scene properties
            self.scene_metadata["scene_properties"].update(scene_properties)
            
            # Register with knowledge model
            await self.knowledge_model.register_learning_unit_metadata(unit_metadata)
            
            execution_time = (datetime.now() - start_time).total_seconds() * 1000
            
            logger.info(f"Embedded learning unit metadata for '{unit_id}' in {execution_time:.2f}ms")
            
            return {
                "status": "success",
                "unit_id": unit_id,
                "metadata_embedded": unit_metadata,
                "scene_properties_added": len(scene_properties),
                "spatial_placement": spatial_placement,
                "execution_time_ms": execution_time,
                "educational_context": {
                    "objectives_count": len(unit_data["objectives"]),
                    "prerequisites_count": len(unit_data["prerequisites"]),
                    "competencies_mapped": len(unit_data.get("competencies", [])),
                    "adaptive_enabled": unit_metadata["adaptive_properties"]["difficulty_adaptable"]
                }
            }
            
        except Exception as e:
            logger.error(f"Failed to embed learning unit metadata: {str(e)}")
            raise EducationalMetadataError(f"Metadata embedding failed: {str(e)}")
    
    def _calculate_metadata_hash(self, data: Dict[str, Any]) -> str:
        """Calculate hash for metadata integrity verification."""
        data_string = json.dumps(data, sort_keys=True)
        return hashlib.sha256(data_string.encode()).hexdigest()[:16]
    
    async def configure_assessment_metadata(
        self,
        assessment_id: str,
        assessment_config: Dict[str, Any],
        trigger_conditions: Dict[str, Any],
        spatial_placement: Tuple[float, float, float]
    ) -> Dict[str, Any]:
        """
        Configure assessment metadata with trigger conditions and spatial placement.
        
        Educational Impact:
        Enables spatial assessment configuration with precise trigger conditions,
        supporting contextual evaluation and location-based learning assessment.
        
        Args:
            assessment_id: Unique identifier for the assessment
            assessment_config: Assessment configuration and criteria
            trigger_conditions: Conditions that activate the assessment
            spatial_placement: 3D position for assessment trigger placement
            
        Returns:
            Dict containing assessment configuration results
        """
        try:
            start_time = datetime.now()
            
            # Validate spatial placement precision (0.1mm)
            validated_placement = tuple(round(coord, 4) for coord in spatial_placement)
            
            # Create comprehensive assessment metadata
            assessment_metadata = {
                "assessment_id": assessment_id,
                "assessment_type": assessment_config.get("type", "formative"),
                "learning_objectives": assessment_config.get("objectives", []),
                "assessment_criteria": assessment_config.get("criteria", []),
                "scoring_method": assessment_config.get("scoring", "rubric_based"),
                "time_limit_minutes": assessment_config.get("time_limit", 10),
                "attempts_allowed": assessment_config.get("attempts", 3),
                "feedback_type": assessment_config.get("feedback", "immediate"),
                "spatial_configuration": {
                    "trigger_position": {
                        "x": validated_placement[0],
                        "y": validated_placement[1],
                        "z": validated_placement[2]
                    },
                    "activation_radius": trigger_conditions.get("radius", 1.0),
                    "trigger_shape": trigger_conditions.get("shape", "sphere"),
                    "visibility": trigger_conditions.get("visibility", "invisible"),
                    "interaction_required": trigger_conditions.get("interaction_required", True)
                },
                "trigger_conditions": {
                    "proximity_activation": trigger_conditions.get("proximity", True),
                    "gaze_activation": trigger_conditions.get("gaze", False),
                    "gesture_activation": trigger_conditions.get("gesture", False),
                    "time_based": trigger_conditions.get("time_based", False),
                    "prerequisite_completion": trigger_conditions.get("prerequisites", []),
                    "learner_readiness": trigger_conditions.get("readiness_check", True)
                },
                "adaptive_assessment": {
                    "difficulty_adaptation": assessment_config.get("adaptive_difficulty", True),
                    "question_branching": assessment_config.get("branching", False),
                    "personalized_feedback": assessment_config.get("personalized", True),
                    "real_time_adjustment": assessment_config.get("real_time", True)
                },
                "configuration_metadata": {
                    "configured_timestamp": start_time.isoformat(),
                    "configuration_hash": self._calculate_metadata_hash(assessment_config),
                    "manager_id": self.manager_id,
                    "spatial_precision": "0.1mm"
                }
            }
            
            # Store assessment configuration
            self.assessment_configurations[assessment_id] = assessment_metadata
            self.scene_metadata["assessment_triggers"][assessment_id] = assessment_metadata
            
            # Create Blender scene properties for assessment
            assessment_properties = {
                f"malloc_assessment_{assessment_id}_type": assessment_config.get("type", "formative"),
                f"malloc_assessment_{assessment_id}_objectives": json.dumps(assessment_config.get("objectives", [])),
                f"malloc_assessment_{assessment_id}_criteria": json.dumps(assessment_config.get("criteria", [])),
                f"malloc_assessment_{assessment_id}_spatial": json.dumps(assessment_metadata["spatial_configuration"]),
                f"malloc_assessment_{assessment_id}_triggers": json.dumps(assessment_metadata["trigger_conditions"]),
                f"malloc_assessment_{assessment_id}_adaptive": json.dumps(assessment_metadata["adaptive_assessment"])
            }
            
            # Update scene properties
            self.scene_metadata["scene_properties"].update(assessment_properties)
            
            # Register with assessment model
            await self.assessment_model.register_spatial_assessment_configuration(assessment_metadata)
            
            execution_time = (datetime.now() - start_time).total_seconds() * 1000
            
            logger.info(f"Configured assessment metadata for '{assessment_id}' in {execution_time:.2f}ms")
            
            return {
                "status": "success",
                "assessment_id": assessment_id,
                "assessment_metadata": assessment_metadata,
                "spatial_placement": validated_placement,
                "scene_properties_added": len(assessment_properties),
                "execution_time_ms": execution_time,
                "educational_context": {
                    "assessment_type": assessment_metadata["assessment_type"],
                    "objectives_count": len(assessment_metadata["learning_objectives"]),
                    "criteria_count": len(assessment_metadata["assessment_criteria"]),
                    "adaptive_enabled": assessment_metadata["adaptive_assessment"]["difficulty_adaptation"]
                }
            }
            
        except Exception as e:
            logger.error(f"Failed to configure assessment metadata: {str(e)}")
            raise EducationalMetadataError(f"Assessment configuration failed: {str(e)}")
    
    async def enable_realtime_metadata_updates(
        self,
        update_frequency_seconds: float = 5.0,
        learner_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Enable real-time metadata updates based on learning progress.
        
        Educational Impact:
        Provides dynamic content adaptation through continuous metadata updates,
        enabling responsive and personalized learning experiences in VR.
        
        Args:
            update_frequency_seconds: Frequency of metadata updates
            learner_id: Optional learner ID for personalized updates
            
        Returns:
            Dict containing real-time update configuration
        """
        try:
            start_time = datetime.now()
            
            if self.real_time_updates_active:
                return {
                    "status": "already_active",
                    "message": "Real-time updates are already enabled"
                }
            
            # Configure real-time update parameters
            update_config = {
                "enabled": True,
                "update_frequency": update_frequency_seconds,
                "learner_id": learner_id,
                "update_types": {
                    "learning_progress": True,
                    "difficulty_adaptation": True,
                    "content_personalization": True,
                    "assessment_adjustment": True,
                    "engagement_tracking": True
                },
                "performance_monitoring": {
                    "max_update_time_ms": 50,  # Quest 3 requirement
                    "memory_limit_mb": 20,
                    "update_queue_size": 100
                },
                "started_timestamp": start_time.isoformat(),
                "manager_id": self.manager_id
            }
            
            # Initialize update tracking
            self.scene_metadata["real_time_updates"] = update_config
            self.real_time_updates_active = True
            
            # Add real-time update properties to scene
            realtime_properties = {
                "malloc_realtime_enabled": "true",
                "malloc_update_frequency": str(update_frequency_seconds),
                "malloc_learner_context": learner_id or "general",
                "malloc_update_started": start_time.isoformat(),
                "malloc_last_update": "never"
            }
            
            self.scene_metadata["scene_properties"].update(realtime_properties)
            
            # Start update monitoring task
            asyncio.create_task(self._real_time_update_loop(update_frequency_seconds, learner_id))
            
            execution_time = (datetime.now() - start_time).total_seconds() * 1000
            
            logger.info(f"Enabled real-time metadata updates in {execution_time:.2f}ms")
            
            return {
                "status": "enabled",
                "update_config": update_config,
                "execution_time_ms": execution_time,
                "educational_context": {
                    "personalized_updates": learner_id is not None,
                    "update_frequency_seconds": update_frequency_seconds,
                    "adaptive_features_enabled": True
                }
            }
            
        except Exception as e:
            logger.error(f"Failed to enable real-time updates: {str(e)}")
            raise EducationalMetadataError(f"Real-time update activation failed: {str(e)}")
    
    async def _real_time_update_loop(
        self,
        frequency: float,
        learner_id: Optional[str]
    ) -> None:
        """Continuous loop for real-time metadata updates."""
        try:
            while self.real_time_updates_active:
                update_start = datetime.now()
                
                try:
                    # Perform real-time metadata update
                    await self._perform_realtime_update(learner_id)
                    
                    # Check performance requirement (< 50ms)
                    update_time = (datetime.now() - update_start).total_seconds() * 1000
                    if update_time > 50:
                        logger.warning(f"Real-time update exceeded 50ms: {update_time:.2f}ms")
                    
                except Exception as update_error:
                    logger.error(f"Error in real-time update: {str(update_error)}")
                
                # Wait for next update cycle
                await asyncio.sleep(frequency)
                
        except asyncio.CancelledError:
            logger.info("Real-time update loop cancelled")
        except Exception as e:
            logger.error(f"Real-time update loop failed: {str(e)}")
            self.real_time_updates_active = False
    
    async def _perform_realtime_update(self, learner_id: Optional[str]) -> None:
        """Perform a single real-time metadata update."""
        update_time = datetime.now()
        
        # Get current learning state
        if learner_id:
            learner_progress = await self.learner_model.get_current_progress(learner_id)
            engagement_data = await self._get_current_engagement_data(learner_id)
            assessment_data = await self._get_current_assessment_data(learner_id)
        else:
            learner_progress = {}
            engagement_data = {}
            assessment_data = {}
        
        # Calculate learning equation progression
        if learner_id:
            progression_data = await self.equation_processor.calculate_learning_progression(
                learner_data=learner_progress,
                knowledge_data=self.scene_metadata.get("learning_units", {}),
                engagement_data=engagement_data,
                assessment_data=assessment_data
            )
        else:
            progression_data = {}
        
        # Update adaptive parameters
        updated_adaptive_params = await self._update_adaptive_parameters(
            learner_progress, engagement_data, assessment_data, progression_data
        )
        
        # Update scene metadata
        self.scene_metadata["adaptive_parameters"].update(updated_adaptive_params)
        self.scene_metadata["tracking_data"].update({
            "last_update": update_time.isoformat(),
            "learner_progress": learner_progress,
            "engagement_metrics": engagement_data,
            "assessment_results": assessment_data,
            "progression_state": progression_data
        })
        
        # Update scene properties
        self.scene_metadata["scene_properties"]["malloc_last_update"] = update_time.isoformat()
        self.scene_metadata["scene_properties"]["malloc_adaptive_state"] = json.dumps(updated_adaptive_params)
    
    async def _get_current_engagement_data(self, learner_id: str) -> Dict[str, Any]:
        """Get current engagement data for the learner."""
        # This would integrate with the engagement model
        return {
            "engagement_score": 0.75,  # Placeholder
            "interaction_frequency": 0.8,
            "attention_level": 0.7,
            "learning_momentum": 0.6
        }
    
    async def _get_current_assessment_data(self, learner_id: str) -> Dict[str, Any]:
        """Get current assessment data for the learner."""
        # This would integrate with the assessment model
        return {
            "current_competency": 0.7,  # Placeholder
            "recent_performance": 0.75,
            "skill_progression": 0.1,
            "assessment_confidence": 0.8
        }
    
    async def _update_adaptive_parameters(
        self,
        learner_progress: Dict[str, Any],
        engagement_data: Dict[str, Any],
        assessment_data: Dict[str, Any],
        progression_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Update adaptive parameters based on real-time data."""
        # Calculate adaptive adjustments
        engagement_score = engagement_data.get("engagement_score", 0.7)
        performance_score = assessment_data.get("recent_performance", 0.7)
        learning_momentum = progression_data.get("learning_momentum", 0.6)
        
        # Determine difficulty adjustment
        if performance_score > 0.8 and engagement_score > 0.7:
            difficulty_adjustment = min(2.0, self.scene_metadata["adaptive_parameters"].get("difficulty_level", 1.0) + 0.1)
        elif performance_score < 0.5 or engagement_score < 0.5:
            difficulty_adjustment = max(0.5, self.scene_metadata["adaptive_parameters"].get("difficulty_level", 1.0) - 0.1)
        else:
            difficulty_adjustment = self.scene_metadata["adaptive_parameters"].get("difficulty_level", 1.0)
        
        # Determine personalization level
        if learner_progress:
            personalization_level = "high" if engagement_score > 0.8 else "medium" if engagement_score > 0.6 else "low"
        else:
            personalization_level = "medium"
        
        # Determine content sequencing
        if learning_momentum > 0.7:
            content_sequencing = "accelerated"
        elif learning_momentum < 0.4:
            content_sequencing = "reinforcement"
        else:
            content_sequencing = "standard"
        
        return {
            "difficulty_level": difficulty_adjustment,
            "personalization_level": personalization_level,
            "content_sequencing": content_sequencing,
            "feedback_frequency": "real_time" if engagement_score > 0.6 else "frequent",
            "last_adaptation": datetime.now().isoformat()
        }
    
    async def detect_educational_objects(
        self,
        scene_scan_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Automatically detect and track educational objects in the scene.
        
        Educational Impact:
        Enables automatic identification of learning content and interactive elements,
        supporting seamless integration of educational materials in VR environments.
        
        Args:
            scene_scan_data: Data from scene scanning for object detection
            
        Returns:
            Dict containing detected educational objects and their metadata
        """
        try:
            start_time = datetime.now()
            
            detected_objects = []
            objects_data = scene_scan_data.get("objects", [])
            
            for obj_data in objects_data:
                obj_name = obj_data.get("name", "")
                custom_properties = obj_data.get("custom_properties", {})
                
                # Check if object has educational markers
                is_educational = any(
                    prop.startswith("malloc_") for prop in custom_properties.keys()
                ) or any(
                    keyword in obj_name.lower() 
                    for keyword in ["learning", "education", "knowledge", "assessment", "tutorial"]
                )
                
                if is_educational:
                    # Extract educational metadata
                    educational_object = {
                        "object_id": f"edu_obj_{len(detected_objects)}_{int(start_time.timestamp())}",
                        "object_name": obj_name,
                        "object_type": obj_data.get("type", "MESH"),
                        "location": obj_data.get("location", (0, 0, 0)),
                        "rotation": obj_data.get("rotation", (0, 0, 0)),
                        "scale": obj_data.get("scale", (1, 1, 1)),
                        "educational_metadata": {
                            "learning_unit": custom_properties.get("malloc_unit_id", "unknown"),
                            "learning_objectives": self._parse_json_property(
                                custom_properties.get("malloc_objectives", "[]")
                            ),
                            "content_type": custom_properties.get("malloc_content_type", "interactive"),
                            "difficulty_level": custom_properties.get("malloc_difficulty", "intermediate"),
                            "interaction_enabled": custom_properties.get("malloc_interactive", "true") == "true"
                        },
                        "tracking_configuration": {
                            "track_interactions": True,
                            "track_performance": True,
                            "track_engagement": True,
                            "spatial_precision": "0.1mm"
                        },
                        "detection_metadata": {
                            "detected_timestamp": start_time.isoformat(),
                            "detection_confidence": self._calculate_detection_confidence(obj_data, custom_properties),
                            "manager_id": self.manager_id
                        }
                    }
                    
                    detected_objects.append(educational_object)
                    self.educational_objects[educational_object["object_id"]] = educational_object
            
            # Update scene metadata with detected objects
            self.scene_metadata["detected_educational_objects"] = {
                "detection_timestamp": start_time.isoformat(),
                "objects_detected": len(detected_objects),
                "objects": detected_objects
            }
            
            execution_time = (datetime.now() - start_time).total_seconds() * 1000
            
            logger.info(f"Detected {len(detected_objects)} educational objects in {execution_time:.2f}ms")
            
            return {
                "status": "success",
                "objects_detected": len(detected_objects),
                "detected_objects": detected_objects,
                "execution_time_ms": execution_time,
                "educational_context": {
                    "learning_units_identified": len(set(
                        obj["educational_metadata"]["learning_unit"] 
                        for obj in detected_objects
                    )),
                    "interactive_objects": len([
                        obj for obj in detected_objects 
                        if obj["educational_metadata"]["interaction_enabled"]
                    ]),
                    "content_types": list(set(
                        obj["educational_metadata"]["content_type"] 
                        for obj in detected_objects
                    ))
                }
            }
            
        except Exception as e:
            logger.error(f"Failed to detect educational objects: {str(e)}")
            raise EducationalMetadataError(f"Object detection failed: {str(e)}")
    
    def _parse_json_property(self, json_string: str) -> Any:
        """Safely parse JSON property with fallback."""
        try:
            return json.loads(json_string)
        except (json.JSONDecodeError, TypeError):
            return []
    
    def _calculate_detection_confidence(
        self, 
        obj_data: Dict[str, Any], 
        custom_properties: Dict[str, str]
    ) -> float:
        """Calculate confidence level for educational object detection."""
        confidence = 0.0
        
        # Custom properties boost confidence
        educational_props = sum(1 for prop in custom_properties.keys() if prop.startswith("malloc_"))
        confidence += min(0.5, educational_props * 0.1)
        
        # Name-based detection
        obj_name = obj_data.get("name", "").lower()
        educational_keywords = ["learning", "education", "knowledge", "assessment", "tutorial", "interactive"]
        name_matches = sum(1 for keyword in educational_keywords if keyword in obj_name)
        confidence += min(0.3, name_matches * 0.1)
        
        # Object type considerations
        obj_type = obj_data.get("type", "")
        if obj_type in ["MESH", "EMPTY", "TEXT"]:
            confidence += 0.2
        
        return min(1.0, confidence)
    
    async def export_metadata_package(
        self,
        export_format: str = "json",
        include_tracking_data: bool = True
    ) -> Dict[str, Any]:
        """
        Export comprehensive metadata package for backup or transfer.
        
        Educational Impact:
        Enables metadata portability and backup for educational content preservation,
        supporting content reuse and cross-platform educational delivery.
        
        Args:
            export_format: Format for metadata export (json, yaml, xml)
            include_tracking_data: Whether to include learner tracking data
            
        Returns:
            Dict containing exported metadata package
        """
        try:
            start_time = datetime.now()
            
            # Create comprehensive metadata package
            metadata_package = {
                "export_metadata": {
                    "export_timestamp": start_time.isoformat(),
                    "export_format": export_format,
                    "manager_id": self.manager_id,
                    "scene_name": self.scene_name,
                    "metadata_version": "1.0",
                    "includes_tracking_data": include_tracking_data
                },
                "scene_metadata": {
                    key: value for key, value in self.scene_metadata.items()
                    if key != "tracking_data" or include_tracking_data
                },
                "educational_objects": self.educational_objects,
                "assessment_configurations": self.assessment_configurations,
                "learning_units": self.scene_metadata.get("learning_units", {}),
                "adaptive_parameters": self.scene_metadata.get("adaptive_parameters", {}),
                "scene_properties": self.scene_metadata.get("scene_properties", {})
            }
            
            # Add tracking data if requested
            if include_tracking_data:
                metadata_package["tracking_data"] = self.scene_metadata.get("tracking_data", {})
            
            # Format-specific processing
            if export_format == "json":
                exported_data = json.dumps(metadata_package, indent=2)
            elif export_format == "yaml":
                # Would need yaml library
                exported_data = str(metadata_package)  # Fallback to string
            else:
                exported_data = str(metadata_package)
            
            execution_time = (datetime.now() - start_time).total_seconds() * 1000
            
            logger.info(f"Exported metadata package in {execution_time:.2f}ms")
            
            return {
                "status": "success",
                "export_format": export_format,
                "exported_data": exported_data,
                "package_size_bytes": len(exported_data),
                "execution_time_ms": execution_time,
                "educational_context": {
                    "learning_units_exported": len(metadata_package["learning_units"]),
                    "educational_objects_exported": len(metadata_package["educational_objects"]),
                    "assessment_configs_exported": len(metadata_package["assessment_configurations"]),
                    "tracking_data_included": include_tracking_data
                }
            }
            
        except Exception as e:
            logger.error(f"Failed to export metadata package: {str(e)}")
            raise EducationalMetadataError(f"Metadata export failed: {str(e)}")
    
    async def get_metadata_status(self) -> Dict[str, Any]:
        """
        Get comprehensive status of the metadata management system.
        
        Returns:
            Dict containing detailed metadata system status
        """
        current_time = datetime.now()
        
        return {
            "manager_id": self.manager_id,
            "scene_name": self.scene_name,
            "status": "active",
            "created_timestamp": self.scene_metadata["created_timestamp"],
            "last_update": self.scene_metadata.get("tracking_data", {}).get("last_update", "never"),
            "real_time_updates_active": self.real_time_updates_active,
            "metadata_counts": {
                "learning_units": len(self.scene_metadata.get("learning_units", {})),
                "educational_objects": len(self.educational_objects),
                "assessment_configurations": len(self.assessment_configurations),
                "scene_properties": len(self.scene_metadata.get("scene_properties", {}))
            },
            "educational_metrics": {
                "learning_domains_covered": len(set(
                    unit.get("content_type", "general") 
                    for unit in self.scene_metadata.get("learning_units", {}).values()
                )),
                "difficulty_levels_available": len(set(
                    unit.get("difficulty_level", "intermediate") 
                    for unit in self.scene_metadata.get("learning_units", {}).values()
                )),
                "interactive_objects_count": len([
                    obj for obj in self.educational_objects.values()
                    if obj.get("educational_metadata", {}).get("interaction_enabled", False)
                ]),
                "assessment_triggers_configured": len(self.assessment_configurations)
            },
            "performance_metrics": {
                "system_uptime_hours": (current_time - datetime.fromisoformat(self.scene_metadata["created_timestamp"])).total_seconds() / 3600,
                "real_time_update_frequency": self.scene_metadata.get("real_time_updates", {}).get("update_frequency", "disabled"),
                "memory_efficiency": "optimized",
                "spatial_precision": "0.1mm"
            },
            "adaptive_features": {
                "personalization_active": self.scene_metadata.get("adaptive_parameters", {}).get("personalization_level", "medium") != "disabled",
                "difficulty_adaptation": self.scene_metadata.get("adaptive_parameters", {}).get("difficulty_adaptation", True),
                "content_sequencing": self.scene_metadata.get("adaptive_parameters", {}).get("content_sequencing", "adaptive"),
                "real_time_feedback": self.scene_metadata.get("adaptive_parameters", {}).get("feedback_frequency", "real_time") == "real_time"
            }
        }
    
    async def disable_realtime_updates(self) -> Dict[str, Any]:
        """
        Disable real-time metadata updates.
        
        Returns:
            Dict containing disable operation results
        """
        try:
            if not self.real_time_updates_active:
                return {
                    "status": "not_active",
                    "message": "Real-time updates were not active"
                }
            
            self.real_time_updates_active = False
            
            # Update scene properties
            self.scene_metadata["scene_properties"]["malloc_realtime_enabled"] = "false"
            self.scene_metadata["scene_properties"]["malloc_update_stopped"] = datetime.now().isoformat()
            
            logger.info("Disabled real-time metadata updates")
            
            return {
                "status": "disabled",
                "disabled_timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"Failed to disable real-time updates: {str(e)}")
            raise EducationalMetadataError(f"Disable operation failed: {str(e)}")
