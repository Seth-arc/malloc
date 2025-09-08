"""
Educational API Versioning Framework
Maintains learning continuity across system updates
Implements lines 3252-3394 from Malloc_MCP_Server_Development_Pathway.md
"""

from .api_versioning import (
    APIVersion,
    EducationalCompatibilityMatrix,
    EducationalDataMigrationService,
    VersionedAPIGateway
)

from .schema_migration import (
    EducationalSchemaMigration,
    LearnerProfileSchemaMigration_V2_0
)

__all__ = [
    'APIVersion',
    'EducationalCompatibilityMatrix', 
    'EducationalDataMigrationService',
    'VersionedAPIGateway',
    'EducationalSchemaMigration',
    'LearnerProfileSchemaMigration_V2_0'
]
