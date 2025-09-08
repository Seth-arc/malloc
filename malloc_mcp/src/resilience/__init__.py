"""
Educational Resilience Framework
Implements circuit breaker and bulkhead patterns for educational continuity
Implements lines 3534-3761 from Malloc_MCP_Server_Development_Pathway.md
"""

from .circuit_breaker import (
    EducationalServiceState,
    EducationalResilienceConfig,
    EducationalCircuitBreaker
)

from .bulkhead_pattern import (
    EducationalBulkheadPattern
)

__all__ = [
    'EducationalServiceState',
    'EducationalResilienceConfig', 
    'EducationalCircuitBreaker',
    'EducationalBulkheadPattern'
]
