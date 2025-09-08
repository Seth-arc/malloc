"""
Blender Integration Module for Malloc VR MCP Server

Educational Impact:
This module provides comprehensive Blender integration for educational VR learning experiences,
implementing the complete specifications from lines 5356-5437 of the development pathway.

Performance Requirements:
- Quest 3 VR: <72fps maintained during Blender operations
- Response time: <100ms for Blender MCP tool operations
- Memory usage: <50MB for Blender integration components
- Spatial precision: 0.1mm tolerance for educational objects

The module includes:
- Core Blender MCP tools (create_blender_knowledge_node, create_assessment_trigger, etc.)
- VRAssessmentTrigger class for embedded assessment triggers
- BlenderKnowledgeIntegration for knowledge model integration
- BlenderViewportIntegration for VR learning environment simulation
- Comprehensive interaction tracking and educational metadata systems

Reference: docs/Malloc_MCP_Server_Development_Pathway.md lines 5356-5437
"""

from .blender_mcp_tools import (
    create_blender_knowledge_node,
    create_assessment_trigger,
    update_blender_scene_metadata,
    track_blender_interaction
)

from .vr_assessment_trigger import VRAssessmentTrigger
from .blender_knowledge_integration import BlenderKnowledgeIntegration
from .blender_viewport_integration import BlenderViewportIntegration
from .interaction_tracking import BlenderInteractionTracker
from .educational_metadata import EducationalMetadataManager
from .learning_models_integration import BlenderLearningModelsIntegration

__all__ = [
    'create_blender_knowledge_node',
    'create_assessment_trigger', 
    'update_blender_scene_metadata',
    'track_blender_interaction',
    'VRAssessmentTrigger',
    'BlenderKnowledgeIntegration',
    'BlenderViewportIntegration',
    'BlenderInteractionTracker',
    'EducationalMetadataManager',
    'BlenderLearningModelsIntegration'
]
