"""
Learning Models Integration Package
Phase 2: Learning Model APIs Implementation

Educational Impact:
Integrates all five learning model APIs (Learner, Knowledge, Engagement, Assessment, Transition)
to provide comprehensive adaptive learning capabilities with mathematical foundation.

Performance Requirements:
- Quest 3 VR: All model APIs maintain >72fps performance
- Memory usage: <150MB total for all model operations
- Response times: Meet individual model specifications

This package implements the core learning equation:
∂(t+1) = ∂(t) + α · Δ(∩(t), ∆(t), E(t), A(t)) + β · ε(t)
"""

from .learner_model import LearnerModelProcessor, LearnerProfileData
from .knowledge_model import KnowledgeModelProcessor, KnowledgeStructureData, BlenderKnowledgeIntegration
from .engagement_model import EngagementModelProcessor, VRInteractionData, AttentionMetrics
from .assessment_model import AssessmentModelProcessor, AssessmentConfiguration, AssessmentResponse, AssessmentType, CompetencyLevel
from .transition_model import TransitionModelProcessor, TransitionConfiguration, LearningStateData, TransitionType, LearningState
from .integration_engine import LearningIntegrationEngine, LearningModelInputs, IntegrationResult

__all__ = [
    # Learner Model
    'LearnerModelProcessor',
    'LearnerProfileData',
    
    # Knowledge Model
    'KnowledgeModelProcessor',
    'KnowledgeStructureData',
    'BlenderKnowledgeIntegration',
    
    # Engagement Model
    'EngagementModelProcessor',
    'VRInteractionData',
    'AttentionMetrics',
    
    # Assessment Model
    'AssessmentModelProcessor',
    'AssessmentConfiguration',
    'AssessmentResponse',
    'AssessmentType',
    'CompetencyLevel',
    
    # Transition Model
    'TransitionModelProcessor',
    'TransitionConfiguration',
    'LearningStateData',
    'TransitionType',
    'LearningState',
    
    # Integration Engine
    'LearningIntegrationEngine',
    'LearningModelInputs',
    'IntegrationResult'
]

# Package version
__version__ = "3.0.0"

# Educational metadata
EDUCATIONAL_METADATA = {
    "learning_equation": "∂(t+1) = ∂(t) + α · Δ(∩(t), ∆(t), E(t), A(t)) + β · ε(t)",
    "model_count": 5,
    "integration_engine": True,
    "real_time_computation": True,
    "mathematical_foundation": "adaptive_learning_theory",
    "spatial_precision": "0.1mm",
    "quest3_optimized": True,
    "ferpa_compliant": True,
    "computation_target": "<10ms",
    "phase": "3_real_time_integration"
}
