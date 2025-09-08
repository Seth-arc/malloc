"""
Malloc VR MCP Server Configuration Module
Enterprise-grade educational VR MCP server configuration management.

This module provides comprehensive configuration management for the Malloc VR
MCP server with educational enhancements, performance optimization, and 
FERPA compliance settings.

Educational Impact:
Proper configuration ensures optimal learning experiences with consistent
performance across different educational scenarios and learner profiles.
All settings follow educational VR best practices and Quest 3 optimization.

Performance Requirements:
- Quest 3 VR optimization: <72fps minimum performance maintained
- Memory usage: <100MB for basic server operations
- Response latency: <100ms for learning model updates
- Spatial precision: 0.1mm tolerance for educational objects

Authors: Sethu Nguna
Version: 1.0.0
Last Updated: September 2025
License: Educational Use License
"""

from dataclasses import dataclass, field
from typing import Dict, List, Any, Optional
import logging
import os

# Configure logging for educational context
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

try:
    import bpy
    import bmesh
    import mathutils
    BLENDER_AVAILABLE = True
    logger.info("Blender 4.4+ integration available")
except ImportError:
    BLENDER_AVAILABLE = False
    logger.warning("Blender not available - running in standalone mode")


@dataclass
class MCPServerConfiguration:
    """
    Comprehensive MCP server configuration for educational VR learning.
    
    This configuration class centralizes all server settings with enterprise-grade
    defaults and validation. All settings follow educational VR best practices
    and Quest 3 performance optimization requirements.
    
    Educational Impact:
    Proper configuration ensures optimal learning experiences with consistent
    performance across different educational scenarios and learner profiles.
    Configuration supports adaptive learning through dynamic parameter adjustment.
    
    Performance Considerations:
    - Memory limits ensure Quest 3 VR comfort during extended learning sessions
    - Latency thresholds maintain real-time learning adaptation effectiveness
    - Security settings protect learner privacy per FERPA requirements
    - Cache settings optimize response times for educational interactions
    
    Example:
        config = MCPServerConfiguration(
            max_concurrent_learners=25,
            ferpa_compliance_enabled=True,
            real_time_adaptation_enabled=True
        )
        
        # Validate configuration
        config.validate_configuration()
        
        # Get performance-optimized settings
        performance_config = config.get_quest3_optimized_settings()
    
    Attributes:
        server_name: Human-readable server identifier for educational context
        server_version: Semantic version following educational software standards
        protocol_version: MCP protocol version for compatibility validation
        max_concurrent_learners: Maximum simultaneous learning sessions
        learning_model_update_frequency: Hz rate for real-time adaptation
        real_time_adaptation_enabled: Enable/disable adaptive learning features
        max_learning_model_latency_ms: Maximum response time for learning models
        max_engagement_processing_ms: Maximum time for engagement data processing
        max_assessment_evaluation_ms: Maximum time for assessment processing
        max_transition_decision_ms: Maximum time for learning progression decisions
        ferpa_compliance_enabled: Enable FERPA-compliant data protection
        data_retention_days: Data retention policy in days
        encryption_enabled: Enable data encryption for learner privacy
        anonymization_enabled: Enable learner data anonymization
        blender_integration_enabled: Enable Blender 4.4+ integration
        blender_api_version: Required Blender API version
        spatial_precision_tolerance_mm: Spatial precision tolerance in millimeters
        database_path: SQLite database file path for development
        cache_enabled: Enable performance caching
        cache_ttl_seconds: Cache time-to-live in seconds
        websocket_enabled: Enable WebSocket communication
        websocket_port: WebSocket server port
        debug_mode: Enable debug logging and metrics
        performance_monitoring_enabled: Enable performance metrics collection
    """
    
    # Core MCP server settings
    server_name: str = "malloc-vr-learning"
    server_version: str = "2.0.0"
    protocol_version: str = "2024-11-05"
    
    # Educational learning settings
    max_concurrent_learners: int = 50
    learning_model_update_frequency: float = 5.0  # Hz
    real_time_adaptation_enabled: bool = True
    
    # Performance requirements (from spec lines 669-678)
    max_learning_model_latency_ms: int = 100
    max_engagement_processing_ms: int = 50
    max_assessment_evaluation_ms: int = 200
    max_transition_decision_ms: int = 500
    quest3_frame_rate_minimum: int = 72
    quest3_memory_limit_mb: int = 100
    
    # Security and privacy (from spec lines 628-661)
    ferpa_compliance_enabled: bool = True
    data_retention_days: int = 90
    encryption_enabled: bool = True
    anonymization_enabled: bool = True
    jwt_secret_rotation_hours: int = 24
    
    # Blender integration settings
    blender_integration_enabled: bool = BLENDER_AVAILABLE
    blender_api_version: str = "4.4+"
    spatial_precision_tolerance_mm: float = 0.1
    blender_scene_update_frequency: float = 10.0  # Hz
    
    # Database and caching configuration
    database_path: str = "data/malloc_vr_learning.db"
    database_pool_size: int = 10
    cache_enabled: bool = True
    cache_ttl_seconds: int = 300
    cache_max_size_mb: int = 50
    
    # Communication settings
    websocket_enabled: bool = True
    websocket_port: int = 8765
    websocket_max_connections: int = 100
    mcp_stdio_enabled: bool = True
    
    # Development and debugging
    debug_mode: bool = False
    performance_monitoring_enabled: bool = True
    educational_analytics_enabled: bool = True
    audit_logging_enabled: bool = True
    
    # Learning equation parameters (from spec lines 91-105)
    learning_equation_alpha: float = 0.7  # Adaptation strength
    learning_equation_beta: float = 0.3   # Environmental noise factor
    
    # Dynamic weighting ranges (from spec lines 106-129)
    learner_weight_range: tuple = (0.25, 0.40)
    knowledge_weight_range: tuple = (0.20, 0.35)
    engagement_weight_range: tuple = (0.15, 0.30)
    assessment_weight_range: tuple = (0.20, 0.35)
    
    def __post_init__(self) -> None:
        """
        Post-initialization validation and setup.
        
        Validates configuration parameters and sets up derived settings
        following enterprise standards and educational requirements.
        
        Educational Impact:
        Proper validation ensures that all learning experiences operate
        within safe and effective parameters, preventing configuration
        errors that could impact educational outcomes.
        
        Raises:
            ConfigurationError: If configuration parameters are invalid
            EnvironmentError: If required environment is not available
        """
        self.validate_configuration()
        self._setup_derived_settings()
        
        if self.debug_mode:
            logger.info(f"MCPServerConfiguration initialized: {self.get_summary()}")
    
    def validate_configuration(self) -> None:
        """
        Validate all configuration parameters against educational requirements.
        
        Ensures that all settings are within acceptable ranges for educational
        VR applications and Quest 3 performance requirements.
        
        Educational Impact:
        Configuration validation prevents performance issues that could
        disrupt learning experiences and ensures FERPA compliance.
        
        Raises:
            ValueError: If any configuration parameter is invalid
            EnvironmentError: If required dependencies are not available
        """
        # Validate performance requirements
        if self.max_learning_model_latency_ms <= 0:
            raise ValueError("Learning model latency must be positive")
        
        if self.max_learning_model_latency_ms > 1000:
            raise ValueError("Learning model latency too high for real-time learning")
        
        if self.quest3_frame_rate_minimum < 60:
            raise ValueError("Quest 3 frame rate minimum must be at least 60fps")
        
        if self.quest3_memory_limit_mb < 50:
            raise ValueError("Quest 3 memory limit too restrictive")
        
        # Validate learning parameters
        if not 0.1 <= self.learning_equation_alpha <= 1.0:
            raise ValueError("Learning equation alpha must be between 0.1 and 1.0")
        
        if not 0.0 <= self.learning_equation_beta <= 0.5:
            raise ValueError("Learning equation beta must be between 0.0 and 0.5")
        
        # Validate weight ranges
        if not self._validate_weight_range(self.learner_weight_range):
            raise ValueError("Invalid learner weight range")
        
        if not self._validate_weight_range(self.knowledge_weight_range):
            raise ValueError("Invalid knowledge weight range")
        
        if not self._validate_weight_range(self.engagement_weight_range):
            raise ValueError("Invalid engagement weight range")
        
        if not self._validate_weight_range(self.assessment_weight_range):
            raise ValueError("Invalid assessment weight range")
        
        # Validate spatial precision
        if self.spatial_precision_tolerance_mm <= 0:
            raise ValueError("Spatial precision tolerance must be positive")
        
        if self.spatial_precision_tolerance_mm > 1.0:
            logger.warning("Spatial precision tolerance is quite large for educational content")
        
        # Validate concurrent learners
        if self.max_concurrent_learners <= 0:
            raise ValueError("Maximum concurrent learners must be positive")
        
        if self.max_concurrent_learners > 1000:
            logger.warning("Very high concurrent learners limit may impact performance")
        
        logger.info("Configuration validation passed")
    
    def _validate_weight_range(self, weight_range: tuple) -> bool:
        """
        Validate that weight range is valid for learning equation.
        
        Args:
            weight_range: Tuple of (min_weight, max_weight)
            
        Returns:
            bool: True if weight range is valid
        """
        if len(weight_range) != 2:
            return False
        
        min_weight, max_weight = weight_range
        
        if not 0.0 <= min_weight <= max_weight <= 1.0:
            return False
        
        if max_weight - min_weight < 0.05:  # Minimum range for adaptation
            return False
        
        return True
    
    def _setup_derived_settings(self) -> None:
        """
        Setup derived configuration settings based on primary settings.
        
        Educational Impact:
        Derived settings ensure consistency across all components and
        optimize performance based on primary configuration choices.
        """
        # Create data directory if it doesn't exist
        data_dir = os.path.dirname(self.database_path)
        if data_dir and not os.path.exists(data_dir):
            os.makedirs(data_dir, exist_ok=True)
        
        # Adjust cache settings based on memory limits
        if self.cache_max_size_mb > self.quest3_memory_limit_mb * 0.3:
            self.cache_max_size_mb = int(self.quest3_memory_limit_mb * 0.3)
            logger.info(f"Adjusted cache size to {self.cache_max_size_mb}MB for Quest 3 compatibility")
        
        # Adjust WebSocket connections based on concurrent learners
        if self.websocket_max_connections < self.max_concurrent_learners:
            self.websocket_max_connections = self.max_concurrent_learners + 10
            logger.info(f"Adjusted WebSocket connections to {self.websocket_max_connections}")
    
    def get_quest3_optimized_settings(self) -> Dict[str, Any]:
        """
        Get Quest 3 VR optimized configuration settings.
        
        Returns optimized settings specifically tuned for Quest 3 VR performance
        while maintaining educational effectiveness.
        
        Educational Impact:
        Quest 3 optimization ensures smooth VR learning experiences without
        compromising educational content quality or learning analytics.
        
        Returns:
            Dict[str, Any]: Optimized settings for Quest 3 VR
        """
        return {
            "frame_rate_minimum": self.quest3_frame_rate_minimum,
            "memory_limit_mb": self.quest3_memory_limit_mb,
            "spatial_precision_mm": self.spatial_precision_tolerance_mm,
            "max_latency_ms": min(self.max_learning_model_latency_ms, 50),
            "cache_optimization": {
                "enabled": self.cache_enabled,
                "max_size_mb": min(self.cache_max_size_mb, 30),
                "ttl_seconds": min(self.cache_ttl_seconds, 120)
            },
            "blender_optimization": {
                "scene_update_frequency": min(self.blender_scene_update_frequency, 5.0),
                "real_time_updates": True,
                "memory_efficient_mode": True
            }
        }
    
    def get_ferpa_compliance_settings(self) -> Dict[str, Any]:
        """
        Get FERPA compliance configuration settings.
        
        Returns settings specifically related to FERPA compliance and
        educational data protection requirements.
        
        Educational Impact:
        FERPA compliance settings ensure that all learner data is handled
        according to educational privacy regulations, building trust and
        enabling personalized learning without privacy concerns.
        
        Returns:
            Dict[str, Any]: FERPA compliance settings
        """
        return {
            "enabled": self.ferpa_compliance_enabled,
            "data_retention_days": self.data_retention_days,
            "encryption_enabled": self.encryption_enabled,
            "anonymization_enabled": self.anonymization_enabled,
            "audit_logging": self.audit_logging_enabled,
            "jwt_rotation_hours": self.jwt_secret_rotation_hours,
            "minimal_data_collection": True,
            "consent_management": True,
            "data_export_rights": True,
            "deletion_rights": True
        }
    
    def get_performance_thresholds(self) -> Dict[str, int]:
        """
        Get performance threshold settings for monitoring.
        
        Returns performance thresholds used for monitoring and alerting
        on system performance relative to educational requirements.
        
        Educational Impact:
        Performance thresholds ensure that learning experiences remain
        responsive and effective, triggering optimizations when needed.
        
        Returns:
            Dict[str, int]: Performance thresholds in milliseconds
        """
        return {
            "learner_model_processing": self.max_learning_model_latency_ms,
            "engagement_tracking": self.max_engagement_processing_ms,
            "assessment_evaluation": self.max_assessment_evaluation_ms,
            "transition_decision": self.max_transition_decision_ms,
            "database_query": 25,
            "cache_access": 5,
            "encryption_operation": 50,
            "websocket_response": 25
        }
    
    def get_summary(self) -> Dict[str, Any]:
        """
        Get a summary of the current configuration.
        
        Returns a comprehensive summary of all major configuration settings
        useful for logging, debugging, and validation.
        
        Returns:
            Dict[str, Any]: Configuration summary
        """
        return {
            "server_info": {
                "name": self.server_name,
                "version": self.server_version,
                "protocol_version": self.protocol_version
            },
            "educational_settings": {
                "max_concurrent_learners": self.max_concurrent_learners,
                "real_time_adaptation": self.real_time_adaptation_enabled,
                "ferpa_compliance": self.ferpa_compliance_enabled
            },
            "performance_settings": {
                "quest3_optimized": True,
                "frame_rate_minimum": self.quest3_frame_rate_minimum,
                "memory_limit_mb": self.quest3_memory_limit_mb,
                "max_latency_ms": self.max_learning_model_latency_ms
            },
            "integration_settings": {
                "blender_available": self.blender_integration_enabled,
                "websocket_enabled": self.websocket_enabled,
                "caching_enabled": self.cache_enabled
            }
        }


class ConfigurationManager:
    """
    Configuration manager for Malloc VR MCP Server with environment support.
    
    Provides centralized configuration management with support for environment
    variables, configuration files, and runtime configuration updates.
    
    Educational Impact:
    Centralized configuration management ensures consistent behavior across
    different deployment environments while maintaining educational effectiveness.
    """
    
    def __init__(self, config_file_path: Optional[str] = None):
        """
        Initialize configuration manager.
        
        Args:
            config_file_path: Optional path to configuration file
        """
        self.config_file_path = config_file_path
        self._config = None
        
    def get_configuration(self) -> MCPServerConfiguration:
        """
        Get the current server configuration.
        
        Loads configuration from environment variables, config files,
        and defaults in that order of precedence.
        
        Returns:
            MCPServerConfiguration: Current configuration
        """
        if self._config is None:
            self._config = self._load_configuration()
        
        return self._config
    
    def _load_configuration(self) -> MCPServerConfiguration:
        """
        Load configuration from multiple sources.
        
        Educational Impact:
        Flexible configuration loading supports different deployment
        scenarios while maintaining educational requirements.
        
        Returns:
            MCPServerConfiguration: Loaded configuration
        """
        # Start with defaults
        config_dict = {}
        
        # Override with environment variables
        env_overrides = self._load_from_environment()
        config_dict.update(env_overrides)
        
        # Override with config file if provided
        if self.config_file_path and os.path.exists(self.config_file_path):
            file_config = self._load_from_file()
            config_dict.update(file_config)
        
        # Create configuration object
        try:
            config = MCPServerConfiguration(**config_dict)
            logger.info("Configuration loaded successfully")
            return config
        except Exception as e:
            logger.error(f"Configuration loading failed: {e}")
            # Return default configuration on error
            return MCPServerConfiguration()
    
    def _load_from_environment(self) -> Dict[str, Any]:
        """
        Load configuration settings from environment variables.
        
        Returns:
            Dict[str, Any]: Environment variable configuration
        """
        env_config = {}
        
        # Map environment variables to config fields
        env_mapping = {
            "MALLOC_VR_SERVER_NAME": ("server_name", str),
            "MALLOC_VR_MAX_LEARNERS": ("max_concurrent_learners", int),
            "MALLOC_VR_DEBUG": ("debug_mode", bool),
            "MALLOC_VR_FERPA_ENABLED": ("ferpa_compliance_enabled", bool),
            "MALLOC_VR_WEBSOCKET_PORT": ("websocket_port", int),
            "MALLOC_VR_DATABASE_PATH": ("database_path", str),
            "MALLOC_VR_CACHE_ENABLED": ("cache_enabled", bool),
            "MALLOC_VR_BLENDER_INTEGRATION": ("blender_integration_enabled", bool)
        }
        
        for env_var, (config_key, config_type) in env_mapping.items():
            value = os.getenv(env_var)
            if value is not None:
                try:
                    if config_type == bool:
                        env_config[config_key] = value.lower() in ('true', '1', 'yes', 'on')
                    elif config_type == int:
                        env_config[config_key] = int(value)
                    elif config_type == float:
                        env_config[config_key] = float(value)
                    else:
                        env_config[config_key] = value
                except ValueError as e:
                    logger.warning(f"Invalid value for {env_var}: {value} ({e})")
        
        return env_config
    
    def _load_from_file(self) -> Dict[str, Any]:
        """
        Load configuration from file.
        
        Returns:
            Dict[str, Any]: File-based configuration
        """
        try:
            import json
            with open(self.config_file_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            logger.warning(f"Failed to load config file {self.config_file_path}: {e}")
            return {}
