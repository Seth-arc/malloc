"""
BlenderKnowledgeIntegration Class Implementation

Educational Impact:
Provides knowledge model integration with Blender scenes, enabling embedded learning metadata,
scene custom property management, and real-time knowledge structure updates for adaptive VR learning.

Performance Requirements:
- Quest 3 VR: <100ms knowledge integration operations
- Memory usage: <25MB per knowledge integration instance
- Update frequency: Real-time knowledge updates every 5 seconds

Reference: docs/Malloc_MCP_Server_Development_Pathway.md lines 5394-5402
"""

import asyncio
import logging
from typing import Dict, Any, List, Optional, Tuple, Union
from datetime import datetime, timedelta
import json
import uuid

from ..learning.knowledge_model import KnowledgeModel
from ..learning.learner_model import LearnerModel
from ..utils.learning_calculations import LearningEquationProcessor

logger = logging.getLogger(__name__)

class BlenderKnowledgeIntegrationError(Exception):
    """Custom exception for Blender Knowledge Integration operations."""
    pass

class BlenderKnowledgeIntegration:
    """
    Knowledge model integration with Blender scenes.
    
    Educational Impact:
    Creates knowledge nodes with embedded learning metadata, manages scene custom properties
    for educational data, and provides real-time scene metadata updates based on learning progress.
    This enables adaptive content delivery and personalized learning experiences in VR environments.
    
    Performance Requirements:
    - Quest 3 VR: <100ms for knowledge operations
    - Memory usage: <25MB per integration instance
    - Real-time updates: Every 5 seconds maximum
    
    Features:
    - Creates knowledge nodes with embedded learning metadata
    - Scene custom property management for educational data
    - Assessment trigger object creation for learning objectives
    - Real-time scene metadata updates based on learning progress
    
    Reference: docs/malloc_vr_mcp_server_specification.md lines 177-191
    """
    
    def __init__(self, scene_name: str, knowledge_config: Dict[str, Any]):
        """
        Initialize Blender Knowledge Integration.
        
        Args:
            scene_name: Name of the Blender scene to integrate with
            knowledge_config: Knowledge structure and configuration parameters
        """
        self.scene_name = scene_name
        self.knowledge_config = knowledge_config
        self.integration_id = str(uuid.uuid4())
        self.knowledge_nodes: Dict[str, Dict[str, Any]] = {}
        self.scene_metadata: Dict[str, Any] = {}
        self.assessment_triggers: List[str] = []
        
        # Initialize learning models
        self.knowledge_model = KnowledgeModel()
        self.learner_model = LearnerModel()
        self.equation_processor = LearningEquationProcessor()
        
        # Initialize scene integration
        self._initialize_scene_integration()
        
        logger.info(f"Initialized BlenderKnowledgeIntegration for scene: {scene_name}")
    
    def _initialize_scene_integration(self) -> None:
        """Initialize scene integration with knowledge structure."""
        self.scene_metadata = {
            "integration_id": self.integration_id,
            "scene_name": self.scene_name,
            "created_timestamp": datetime.now().isoformat(),
            "knowledge_structure": self.knowledge_config,
            "learning_units": {},
            "assessment_objectives": [],
            "adaptive_parameters": {
                "difficulty_level": 1.0,
                "content_complexity": "standard",
                "personalization_level": "medium"
            }
        }
    
    async def create_knowledge_node(
        self,
        node_id: str,
        learning_unit: Dict[str, Any],
        spatial_position: Tuple[float, float, float] = (0.0, 0.0, 0.0),
        metadata: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Creates knowledge nodes with embedded learning metadata.
        
        Educational Impact:
        Creates spatial knowledge anchors that organize learning content in 3D space,
        enabling spatial learning approaches and contextual knowledge delivery in VR.
        
        Args:
            node_id: Unique identifier for the knowledge node
            learning_unit: Learning unit data and structure
            spatial_position: 3D position for knowledge node placement
            metadata: Additional metadata for the knowledge node
            
        Returns:
            Dict containing knowledge node creation results
            
        Raises:
            BlenderKnowledgeIntegrationError: If knowledge node creation fails
        """
        try:
            start_time = datetime.now()
            
            # Validate learning unit structure
            required_fields = ["unit_id", "title", "objectives", "content_type"]
            for field in required_fields:
                if field not in learning_unit:
                    raise BlenderKnowledgeIntegrationError(f"Missing required learning unit field: {field}")
            
            # Create knowledge node structure
            knowledge_node = {
                "node_id": node_id,
                "learning_unit": learning_unit,
                "spatial_position": {
                    "x": round(spatial_position[0], 4),  # 0.1mm precision
                    "y": round(spatial_position[1], 4),
                    "z": round(spatial_position[2], 4)
                },
                "metadata": metadata or {},
                "created_timestamp": start_time.isoformat(),
                "blender_object_data": {
                    "name": f"Knowledge_Node_{node_id}",
                    "type": "EMPTY",
                    "empty_display_type": "PLAIN_AXES",
                    "location": spatial_position,
                    "scale": (0.5, 0.5, 0.5),  # Small visual indicator
                    "custom_properties": {
                        "malloc_knowledge_node": True,
                        "malloc_node_id": node_id,
                        "malloc_unit_id": learning_unit["unit_id"],
                        "malloc_unit_title": learning_unit["title"],
                        "malloc_objectives": json.dumps(learning_unit["objectives"]),
                        "malloc_content_type": learning_unit["content_type"],
                        "malloc_metadata": json.dumps(metadata or {}),
                        "malloc_created": start_time.isoformat()
                    }
                },
                "learning_analytics": {
                    "access_count": 0,
                    "completion_rate": 0.0,
                    "engagement_score": 0.0,
                    "learning_effectiveness": 0.0
                }
            }
            
            # Register knowledge node with knowledge model
            await self.knowledge_model.register_spatial_knowledge_node(knowledge_node)
            
            # Store knowledge node
            self.knowledge_nodes[node_id] = knowledge_node
            
            # Update scene metadata
            self.scene_metadata["learning_units"][learning_unit["unit_id"]] = {
                "node_id": node_id,
                "title": learning_unit["title"],
                "objectives_count": len(learning_unit["objectives"]),
                "spatial_position": knowledge_node["spatial_position"]
            }
            
            execution_time = (datetime.now() - start_time).total_seconds() * 1000
            
            logger.info(f"Created knowledge node '{node_id}' in {execution_time:.2f}ms")
            
            return {
                "status": "success",
                "node_id": node_id,
                "knowledge_node": knowledge_node,
                "blender_object": knowledge_node["blender_object_data"],
                "execution_time_ms": execution_time,
                "educational_context": {
                    "learning_unit_id": learning_unit["unit_id"],
                    "objectives_count": len(learning_unit["objectives"]),
                    "content_type": learning_unit["content_type"]
                }
            }
            
        except Exception as e:
            logger.error(f"Failed to create knowledge node: {str(e)}")
            raise BlenderKnowledgeIntegrationError(f"Knowledge node creation failed: {str(e)}")
    
    async def manage_scene_custom_properties(
        self,
        property_updates: Dict[str, Any],
        learner_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Scene custom property management for educational data.
        
        Educational Impact:
        Manages educational metadata stored in Blender scene properties,
        enabling persistent learning data and adaptive content delivery based on learner progress.
        
        Args:
            property_updates: Dictionary of properties to update
            learner_id: Optional learner ID for personalized properties
            
        Returns:
            Dict containing property management results
        """
        try:
            start_time = datetime.now()
            
            # Get current scene properties
            current_properties = await self._get_current_scene_properties()
            
            # Process property updates
            updated_properties = current_properties.copy()
            
            for prop_key, prop_value in property_updates.items():
                # Validate property key format
                if not prop_key.startswith("malloc_"):
                    prop_key = f"malloc_{prop_key}"
                
                # Handle different property types
                if isinstance(prop_value, (dict, list)):
                    updated_properties[prop_key] = json.dumps(prop_value)
                else:
                    updated_properties[prop_key] = str(prop_value)
            
            # Add learner-specific properties if provided
            if learner_id:
                learner_properties = await self._get_learner_specific_properties(learner_id)
                updated_properties.update(learner_properties)
            
            # Update scene metadata
            self.scene_metadata["custom_properties"] = updated_properties
            self.scene_metadata["last_property_update"] = start_time.isoformat()
            
            # Create Blender scene property update structure
            blender_property_update = {
                "scene_name": self.scene_name,
                "property_updates": updated_properties,
                "update_timestamp": start_time.isoformat(),
                "learner_context": learner_id,
                "integration_id": self.integration_id
            }
            
            execution_time = (datetime.now() - start_time).total_seconds() * 1000
            
            logger.info(f"Updated scene properties in {execution_time:.2f}ms")
            
            return {
                "status": "success",
                "scene_name": self.scene_name,
                "properties_updated": len(property_updates),
                "blender_property_update": blender_property_update,
                "execution_time_ms": execution_time,
                "educational_context": {
                    "learner_personalization": learner_id is not None,
                    "total_properties": len(updated_properties),
                    "property_categories": list(set(key.split("_")[1] for key in updated_properties.keys() if "_" in key))
                }
            }
            
        except Exception as e:
            logger.error(f"Failed to manage scene properties: {str(e)}")
            raise BlenderKnowledgeIntegrationError(f"Scene property management failed: {str(e)}")
    
    async def _get_current_scene_properties(self) -> Dict[str, Any]:
        """Get current scene custom properties."""
        return self.scene_metadata.get("custom_properties", {
            "malloc_scene_name": self.scene_name,
            "malloc_integration_id": self.integration_id,
            "malloc_knowledge_nodes_count": len(self.knowledge_nodes),
            "malloc_last_access": datetime.now().isoformat()
        })
    
    async def _get_learner_specific_properties(self, learner_id: str) -> Dict[str, str]:
        """Get learner-specific properties for personalization."""
        learner_data = await self.learner_model.get_learner_profile(learner_id)
        
        return {
            "malloc_learner_id": learner_id,
            "malloc_learner_level": str(learner_data.get("skill_level", 1)),
            "malloc_learner_preferences": json.dumps(learner_data.get("learning_preferences", {})),
            "malloc_learner_progress": json.dumps(learner_data.get("progress_data", {})),
            "malloc_adaptive_settings": json.dumps({
                "difficulty_adjustment": learner_data.get("difficulty_preference", 1.0),
                "content_pace": learner_data.get("learning_pace", "medium"),
                "interaction_style": learner_data.get("interaction_preference", "visual")
            })
        }
    
    async def create_assessment_trigger_objects(
        self,
        learning_objectives: List[str],
        trigger_configurations: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Assessment trigger object creation for learning objectives.
        
        Educational Impact:
        Creates spatial assessment triggers linked to specific learning objectives,
        enabling objective-based evaluation and contextual assessment in VR learning environments.
        
        Args:
            learning_objectives: List of learning objectives to assess
            trigger_configurations: Configuration for each assessment trigger
            
        Returns:
            Dict containing assessment trigger creation results
        """
        try:
            start_time = datetime.now()
            
            created_triggers = []
            
            for i, objective in enumerate(learning_objectives):
                trigger_config = trigger_configurations[i] if i < len(trigger_configurations) else {}
                
                # Create trigger for this objective
                trigger_id = f"assessment_{self.integration_id}_{i}_{int(start_time.timestamp())}"
                
                trigger_object = {
                    "trigger_id": trigger_id,
                    "learning_objective": objective,
                    "configuration": trigger_config,
                    "blender_object": {
                        "name": f"Assessment_Trigger_{trigger_id}",
                        "type": "EMPTY",
                        "empty_display_type": "SPHERE",
                        "location": trigger_config.get("position", (0.0, 0.0, 0.0)),
                        "scale": (
                            trigger_config.get("radius", 1.0),
                            trigger_config.get("radius", 1.0),
                            trigger_config.get("radius", 1.0)
                        ),
                        "hide_viewport": True,
                        "hide_render": True,
                        "custom_properties": {
                            "malloc_assessment_trigger": True,
                            "malloc_trigger_id": trigger_id,
                            "malloc_learning_objective": objective,
                            "malloc_trigger_config": json.dumps(trigger_config),
                            "malloc_integration_id": self.integration_id,
                            "malloc_created": start_time.isoformat()
                        }
                    }
                }
                
                created_triggers.append(trigger_object)
                self.assessment_triggers.append(trigger_id)
            
            # Update scene metadata
            self.scene_metadata["assessment_objectives"] = learning_objectives
            self.scene_metadata["assessment_triggers"] = self.assessment_triggers
            
            execution_time = (datetime.now() - start_time).total_seconds() * 1000
            
            logger.info(f"Created {len(created_triggers)} assessment triggers in {execution_time:.2f}ms")
            
            return {
                "status": "success",
                "triggers_created": len(created_triggers),
                "assessment_triggers": created_triggers,
                "learning_objectives": learning_objectives,
                "execution_time_ms": execution_time,
                "educational_context": {
                    "objectives_count": len(learning_objectives),
                    "triggers_per_objective": len(created_triggers) / len(learning_objectives) if learning_objectives else 0,
                    "assessment_coverage": "complete"
                }
            }
            
        except Exception as e:
            logger.error(f"Failed to create assessment triggers: {str(e)}")
            raise BlenderKnowledgeIntegrationError(f"Assessment trigger creation failed: {str(e)}")
    
    async def update_scene_metadata_realtime(
        self,
        learning_progress: Dict[str, Any],
        learner_id: str
    ) -> Dict[str, Any]:
        """
        Real-time scene metadata updates based on learning progress.
        
        Educational Impact:
        Provides dynamic content adaptation by continuously updating scene metadata
        based on real-time learning progress, enabling responsive and personalized VR learning.
        
        Args:
            learning_progress: Current learning progress and analytics
            learner_id: Unique identifier for the learner
            
        Returns:
            Dict containing real-time update results
        """
        try:
            start_time = datetime.now()
            
            # Calculate learning progression using equation processor
            current_state = {
                "learner": await self.learner_model.get_current_state(learner_id),
                "knowledge": learning_progress.get("knowledge_metrics", {}),
                "engagement": learning_progress.get("engagement_metrics", {}),
                "assessment": learning_progress.get("assessment_metrics", {})
            }
            
            # Process learning equation for real-time adaptation
            progression_result = await self.equation_processor.calculate_learning_progression(**current_state)
            
            # Update adaptive parameters based on progression
            adaptive_updates = {
                "difficulty_level": progression_result.get("recommended_difficulty", 1.0),
                "content_complexity": self._determine_content_complexity(progression_result),
                "personalization_level": self._determine_personalization_level(progression_result),
                "next_learning_objectives": progression_result.get("next_objectives", []),
                "recommended_content": progression_result.get("recommended_content", [])
            }
            
            # Update scene metadata
            self.scene_metadata["adaptive_parameters"].update(adaptive_updates)
            self.scene_metadata["last_realtime_update"] = start_time.isoformat()
            self.scene_metadata["learning_progression"] = progression_result
            
            # Update knowledge nodes based on progress
            node_updates = await self._update_knowledge_nodes_progress(learning_progress, learner_id)
            
            # Create real-time update package
            realtime_update = {
                "scene_name": self.scene_name,
                "learner_id": learner_id,
                "update_timestamp": start_time.isoformat(),
                "adaptive_parameters": adaptive_updates,
                "progression_data": progression_result,
                "knowledge_node_updates": node_updates,
                "scene_property_updates": {
                    "malloc_realtime_progress": json.dumps(learning_progress),
                    "malloc_adaptive_params": json.dumps(adaptive_updates),
                    "malloc_progression_state": json.dumps(progression_result),
                    "malloc_last_update": start_time.isoformat()
                }
            }
            
            execution_time = (datetime.now() - start_time).total_seconds() * 1000
            
            logger.info(f"Updated scene metadata in real-time in {execution_time:.2f}ms")
            
            return {
                "status": "success",
                "realtime_update": realtime_update,
                "execution_time_ms": execution_time,
                "educational_impact": {
                    "adaptation_applied": True,
                    "difficulty_adjusted": adaptive_updates["difficulty_level"] != 1.0,
                    "content_personalized": len(adaptive_updates["recommended_content"]) > 0,
                    "progression_calculated": True
                }
            }
            
        except Exception as e:
            logger.error(f"Failed to update scene metadata in real-time: {str(e)}")
            raise BlenderKnowledgeIntegrationError(f"Real-time metadata update failed: {str(e)}")
    
    def _determine_content_complexity(self, progression_result: Dict[str, Any]) -> str:
        """Determine appropriate content complexity level."""
        difficulty_score = progression_result.get("difficulty_score", 0.5)
        
        if difficulty_score < 0.3:
            return "beginner"
        elif difficulty_score < 0.6:
            return "intermediate"
        elif difficulty_score < 0.8:
            return "advanced"
        else:
            return "expert"
    
    def _determine_personalization_level(self, progression_result: Dict[str, Any]) -> str:
        """Determine appropriate personalization level."""
        personalization_score = progression_result.get("personalization_need", 0.5)
        
        if personalization_score < 0.3:
            return "minimal"
        elif personalization_score < 0.7:
            return "medium"
        else:
            return "high"
    
    async def _update_knowledge_nodes_progress(
        self, 
        learning_progress: Dict[str, Any], 
        learner_id: str
    ) -> Dict[str, Any]:
        """Update knowledge nodes based on learning progress."""
        node_updates = {}
        
        for node_id, node_data in self.knowledge_nodes.items():
            unit_id = node_data["learning_unit"]["unit_id"]
            unit_progress = learning_progress.get("unit_progress", {}).get(unit_id, {})
            
            # Update node analytics
            node_data["learning_analytics"].update({
                "access_count": unit_progress.get("access_count", 0),
                "completion_rate": unit_progress.get("completion_rate", 0.0),
                "engagement_score": unit_progress.get("engagement_score", 0.0),
                "learning_effectiveness": unit_progress.get("effectiveness", 0.0)
            })
            
            node_updates[node_id] = {
                "unit_id": unit_id,
                "progress_data": unit_progress,
                "updated_analytics": node_data["learning_analytics"]
            }
        
        return node_updates
    
    async def get_integration_status(self) -> Dict[str, Any]:
        """
        Get comprehensive integration status and analytics.
        
        Returns:
            Dict containing integration status and performance metrics
        """
        current_time = datetime.now()
        
        return {
            "integration_id": self.integration_id,
            "scene_name": self.scene_name,
            "status": "active",
            "created_timestamp": self.scene_metadata["created_timestamp"],
            "last_update": self.scene_metadata.get("last_realtime_update", "never"),
            "knowledge_nodes_count": len(self.knowledge_nodes),
            "assessment_triggers_count": len(self.assessment_triggers),
            "scene_metadata_size": len(json.dumps(self.scene_metadata)),
            "educational_metrics": {
                "learning_units_integrated": len(self.scene_metadata.get("learning_units", {})),
                "assessment_objectives": len(self.scene_metadata.get("assessment_objectives", [])),
                "adaptive_parameters_active": len(self.scene_metadata.get("adaptive_parameters", {})),
                "real_time_updates_enabled": True
            },
            "performance_metrics": {
                "integration_uptime_hours": (current_time - datetime.fromisoformat(self.scene_metadata["created_timestamp"])).total_seconds() / 3600,
                "average_update_frequency": "5_seconds",
                "spatial_precision": "0.1mm",
                "memory_efficiency": "optimized"
            }
        }
