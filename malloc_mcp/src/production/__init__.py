"""
Production Infrastructure for Malloc VR MCP Server

Educational Impact:
Provides comprehensive production-grade infrastructure for educational VR learning
with 99.9% uptime, scalable deployment, and continuous monitoring.

Components:
- Health Monitoring Framework: System health assessment and alerting
- Performance Optimizer: Real-time performance tuning for Quest 3 VR
- Educational Analytics: Learning effectiveness tracking and insights
- Deployment Manager: Scalable production deployment infrastructure

Author: Malloc VR Learning Team
Date: December 26, 2024
"""

from .health_monitoring import (
    HealthMonitoringFramework,
    LearningSystemDiagnostics,
    SystemHealthReport,
    HealthStatus,
    create_health_monitoring_framework,
    setup_health_monitoring_logging
)

from .performance_optimizer import (
    PerformanceOptimizer,
    LearningDataCache,
    PerformanceMetrics,
    OptimizationLevel,
    create_performance_optimizer,
    setup_performance_logging
)

from .educational_analytics import (
    EducationalAnalyticsPlatform,
    LearningDataProcessor,
    AdaptationEffectivenessAnalyzer,
    LearningOutcome,
    EducationalInsight,
    AdaptationAnalysis,
    LearningEventType,
    create_educational_analytics_platform,
    setup_analytics_logging
)

from .deployment_manager import (
    ProductionDeploymentManager,
    ConfigurationManager,
    ServiceManager,
    DeploymentConfiguration,
    ServiceInstance,
    DeploymentReport,
    DeploymentStatus,
    ServiceType,
    create_production_deployment,
    setup_deployment_logging,
    quick_deployment_health_check
)

__all__ = [
    # Health Monitoring
    "HealthMonitoringFramework",
    "LearningSystemDiagnostics", 
    "SystemHealthReport",
    "HealthStatus",
    "create_health_monitoring_framework",
    "setup_health_monitoring_logging",
    
    # Performance Optimization
    "PerformanceOptimizer",
    "LearningDataCache",
    "PerformanceMetrics",
    "OptimizationLevel", 
    "create_performance_optimizer",
    "setup_performance_logging",
    
    # Educational Analytics
    "EducationalAnalyticsPlatform",
    "LearningDataProcessor",
    "AdaptationEffectivenessAnalyzer",
    "LearningOutcome",
    "EducationalInsight",
    "AdaptationAnalysis",
    "LearningEventType",
    "create_educational_analytics_platform",
    "setup_analytics_logging",
    
    # Deployment Management
    "ProductionDeploymentManager",
    "ConfigurationManager",
    "ServiceManager",
    "DeploymentConfiguration",
    "ServiceInstance", 
    "DeploymentReport",
    "DeploymentStatus",
    "ServiceType",
    "create_production_deployment",
    "setup_deployment_logging",
    "quick_deployment_health_check"
]


def setup_production_logging() -> None:
    """Set up comprehensive logging for all production components"""
    setup_health_monitoring_logging()
    setup_performance_logging()
    setup_analytics_logging()
    setup_deployment_logging()


async def initialize_production_infrastructure(environment: str = "production") -> dict:
    """
    Initialize complete production infrastructure
    
    Educational Impact:
    Establishes comprehensive production environment for educational VR learning
    with monitoring, optimization, analytics, and deployment management.
    
    Args:
        environment: Deployment environment (development, staging, production)
    
    Returns:
        Dictionary containing all initialized production components
    """
    # Set up logging
    setup_production_logging()
    
    # Initialize core components
    health_monitor = await create_health_monitoring_framework()
    performance_optimizer = await create_performance_optimizer()
    analytics_platform = await create_educational_analytics_platform()
    deployment_manager = await create_production_deployment(environment)
    
    return {
        "health_monitor": health_monitor,
        "performance_optimizer": performance_optimizer, 
        "analytics_platform": analytics_platform,
        "deployment_manager": deployment_manager,
        "environment": environment
    }
