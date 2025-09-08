"""
Comprehensive Educational Security Framework
Addresses VR-specific and educational data threats
Implements lines 3775-4019 from Malloc_MCP_Server_Development_Pathway.md
"""

from .threat_modeling import (
    EducationalThreatVector,
    SecurityIncident,
    EducationalSecurityMonitor
)

from .ferpa_compliance import (
    FERPAComplianceValidator
)

__all__ = [
    'EducationalThreatVector',
    'SecurityIncident',
    'EducationalSecurityMonitor',
    'FERPAComplianceValidator'
]
