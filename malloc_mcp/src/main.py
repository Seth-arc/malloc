"""
Malloc VR MCP Server Main Entry Point
Enterprise-grade educational VR MCP server startup and configuration.

This module provides the main entry point for the Malloc VR MCP Server
with comprehensive error handling, logging, and configuration management.

Educational Impact:
Main entry point ensures reliable server startup for educational
VR learning experiences with proper initialization sequence and
error recovery procedures.

Performance Requirements:
- Server startup: <10 seconds
- Memory allocation: <50MB during startup  
- Configuration loading: <2 seconds
- Component initialization: <5 seconds

Authors: Sethu Nguna
Version: 1.0.0
Last Updated: September 2025
License: Educational Use License
"""

import asyncio
import json
import logging
import sys
from pathlib import Path

# Local imports
from src.mcp.server_configuration import MCPServerConfiguration, ConfigurationManager
from src.mcp.malloc_vr_mcp_server import MallocVRMCPServer


def setup_logging() -> None:
    """
    Setup comprehensive logging for the Malloc VR MCP Server.
    
    Educational Impact:
    Proper logging enables troubleshooting of educational VR experiences
    and provides audit trails for learning analytics.
    """
    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    
    # Create logs directory if it doesn't exist
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)
    
    # Configure logging with both console and file output
    logging.basicConfig(
        level=logging.INFO,
        format=log_format,
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler(logs_dir / 'malloc_vr_mcp_server.log'),
            logging.FileHandler(logs_dir / 'educational_analytics.log')
        ]
    )
    
    # Set specific log levels for different components
    logging.getLogger('src.security').setLevel(logging.WARNING)  # Reduce security logging noise
    logging.getLogger('urllib3').setLevel(logging.WARNING)       # Reduce HTTP library noise


async def main() -> int:
    """
    Main entry point for Malloc VR MCP Server.
    
    Initializes configuration, creates server instance, and starts the
    educational VR learning server with comprehensive error handling.
    
    Educational Impact:
    Main entry point ensures reliable server startup for educational
    VR learning experiences with proper error handling and logging.
    Enables consistent educational service delivery.
    
    Returns:
        int: Exit code (0 for success, 1 for failure)
        
    Example:
        python -m src.main
        
    Environment Variables:
        MALLOC_VR_SERVER_NAME: Custom server name
        MALLOC_VR_MAX_LEARNERS: Maximum concurrent learners
        MALLOC_VR_DEBUG: Enable debug mode
        MALLOC_VR_FERPA_ENABLED: Enable FERPA compliance
        MALLOC_VR_DATABASE_PATH: Custom database path
    """
    logger = logging.getLogger(__name__)
    
    try:
        logger.info("=" * 60)
        logger.info("Starting Malloc VR MCP Server")
        logger.info("Educational VR Learning Platform v2.0.0")
        logger.info("=" * 60)
        
        # Initialize configuration manager
        config_manager = ConfigurationManager()
        config = config_manager.get_configuration()
        
        logger.info("Configuration Summary:")
        config_summary = config.get_summary()
        for category, details in config_summary.items():
            logger.info(f"  {category}: {details}")
        
        # Validate critical requirements
        await validate_system_requirements(config)
        
        # Create and initialize server
        logger.info("Creating MallocVRMCPServer instance...")
        server = MallocVRMCPServer(config)
        
        logger.info("Initializing server components...")
        init_result = await server.initialize_server()
        
        # Log initialization results
        if init_result.get("ready_for_learning_sessions", False):
            logger.info("✓ Server initialization successful")
            logger.info(f"✓ Server ID: {init_result['server_id']}")
            logger.info(f"✓ Initialization time: {init_result['initialization_duration_seconds']:.2f}s")
            logger.info(f"✓ FERPA compliance: {init_result['ferpa_compliance']}")
            logger.info(f"✓ Max concurrent learners: {init_result['max_concurrent_learners']}")
            logger.info(f"✓ Blender integration: {init_result['blender_integration']['available']}")
            logger.info(f"✓ WebSocket server: {init_result['websocket_server']['enabled']}")
            
            # Start the MCP server
            logger.info("Starting MCP server for educational VR learning...")
            logger.info("Server ready to accept educational learning requests")
            
            try:
                await server.run_mcp_server()
            except KeyboardInterrupt:
                logger.info("Received shutdown signal (Ctrl+C)")
            except Exception as e:
                logger.error(f"Server runtime error: {e}")
                return 1
            finally:
                logger.info("Initiating graceful server shutdown...")
                await server.shutdown_server()
                
        else:
            logger.error("✗ Server initialization failed")
            logger.error(f"Error: {init_result.get('error', 'Unknown initialization error')}")
            
            # Log detailed error information
            if 'error' in init_result:
                logger.error("Initialization failure details:")
                logger.error(f"  Error message: {init_result['error']}")
                logger.error("  Please check configuration and dependencies")
                
            return 1
        
        logger.info("=" * 60)
        logger.info("Malloc VR MCP Server shutdown completed successfully")
        logger.info("Educational VR learning sessions ended")
        logger.info("=" * 60)
        return 0
        
    except Exception as e:
        logger.error(f"Critical server startup failure: {e}")
        logger.error("Educational VR learning server could not be started")
        logger.exception("Full error details:")
        return 1


async def validate_system_requirements(config: MCPServerConfiguration) -> None:
    """
    Validate system requirements for educational VR learning.
    
    Educational Impact:
    System validation ensures that educational VR experiences can be
    delivered with the required performance and reliability standards.
    
    Args:
        config: Server configuration to validate
        
    Raises:
        SystemError: If critical requirements are not met
        ConfigurationError: If configuration is invalid
    """
    logger = logging.getLogger(__name__)
    
    logger.info("Validating system requirements...")
    
    # Check Python version
    python_version = sys.version_info
    if python_version < (3, 11):
        raise SystemError(
            f"Python 3.11+ required for Blender 4.4 compatibility, "
            f"found {python_version.major}.{python_version.minor}"
        )
    logger.info(f"✓ Python version: {python_version.major}.{python_version.minor}")
    
    # Check critical directories
    required_dirs = ["data", "logs"]
    for dir_name in required_dirs:
        Path(dir_name).mkdir(exist_ok=True)
    logger.info("✓ Required directories created")
    
    # Validate configuration
    try:
        config.validate_configuration()
        logger.info("✓ Configuration validation passed")
    except Exception as e:
        raise SystemError(f"Configuration validation failed: {e}")
    
    # Check performance requirements
    quest3_settings = config.get_quest3_optimized_settings()
    if quest3_settings["frame_rate_minimum"] < 60:
        logger.warning("Frame rate minimum below 60fps - may impact VR experience")
    
    if quest3_settings["memory_limit_mb"] > 150:
        logger.warning("Memory limit above 150MB - may impact Quest 3 performance")
    
    logger.info("✓ Quest 3 VR requirements validated")
    
    # Check FERPA compliance settings
    ferpa_settings = config.get_ferpa_compliance_settings()
    if not ferpa_settings["enabled"]:
        logger.warning("FERPA compliance disabled - not recommended for educational use")
    else:
        logger.info("✓ FERPA compliance enabled for educational data protection")
    
    logger.info("System requirements validation completed")


def print_startup_banner() -> None:
    """Print startup banner with system information."""
    banner = """
    ╔══════════════════════════════════════════════════════════════╗
    ║                    Malloc VR MCP Server                      ║
    ║                Educational VR Learning Platform              ║
    ║                         Version 2.0.0                       ║
    ╠══════════════════════════════════════════════════════════════╣
    ║  Features:                                                   ║
    ║  • Real-time Adaptive Learning                              ║
    ║  • FERPA-Compliant Security                                 ║
    ║  • Blender 4.4+ Integration                                ║
    ║  • Quest 3 VR Optimization                                 ║
    ║  • Mathematical Learning Models                             ║
    ║  • WebSocket Communication                                  ║
    ╚══════════════════════════════════════════════════════════════╝
    """
    print(banner)


if __name__ == "__main__":
    # Setup logging before any other operations
    setup_logging()
    
    # Print startup banner
    print_startup_banner()
    
    # Run the main server
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
