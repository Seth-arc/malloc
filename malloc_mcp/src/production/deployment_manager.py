"""
Production Deployment Manager for Malloc VR MCP Server

Educational Impact:
Provides scalable production deployment infrastructure to ensure reliable educational
service delivery with 99.9% uptime and support for 50+ concurrent learners.

Performance Requirements:
- Deployment time: <5 minutes
- Health check validation: <30 seconds
- Service startup: <60 seconds
- Scaling response: <2 minutes

Author: Malloc VR Learning Team
Date: December 26, 2024
"""

import asyncio
import os
import time
import logging
import json
import subprocess
import shutil
import yaml
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, asdict
from enum import Enum
from pathlib import Path
import tempfile
import psutil

from .health_monitoring import HealthMonitoringFramework, SystemHealthReport
from .performance_optimizer import PerformanceOptimizer
from .educational_analytics import EducationalAnalyticsPlatform


class DeploymentStatus(Enum):
    """Deployment status levels"""
    PENDING = "pending"
    DEPLOYING = "deploying"
    RUNNING = "running"
    SCALING = "scaling"
    UPDATING = "updating"
    STOPPING = "stopping"
    STOPPED = "stopped"
    FAILED = "failed"


class ServiceType(Enum):
    """Types of services in deployment"""
    MCP_SERVER = "mcp_server"
    WEBSOCKET_SERVER = "websocket_server"
    HEALTH_MONITOR = "health_monitor"
    PERFORMANCE_OPTIMIZER = "performance_optimizer"
    EDUCATIONAL_ANALYTICS = "educational_analytics"
    DATABASE = "database"


@dataclass
class DeploymentConfiguration:
    """Production deployment configuration"""
    environment: str  # "development", "staging", "production"
    instance_count: int
    memory_limit_mb: int
    cpu_limit_cores: float
    max_concurrent_learners: int
    enable_ssl: bool
    database_type: str  # "sqlite", "postgresql"
    logging_level: str
    backup_enabled: bool
    monitoring_interval: int
    auto_scaling_enabled: bool
    quest3_optimization: bool


@dataclass
class ServiceInstance:
    """Individual service instance"""
    service_type: ServiceType
    instance_id: str
    process_id: Optional[int]
    port: int
    status: DeploymentStatus
    memory_usage_mb: float
    cpu_usage_percent: float
    start_time: datetime
    health_status: str
    last_health_check: datetime


@dataclass
class DeploymentReport:
    """Comprehensive deployment status report"""
    deployment_id: str
    environment: str
    status: DeploymentStatus
    services: List[ServiceInstance]
    total_memory_usage_mb: float
    total_cpu_usage_percent: float
    concurrent_learners: int
    uptime_hours: float
    health_score: float
    performance_metrics: Dict[str, Any]
    deployment_time: datetime
    last_update: datetime


class ConfigurationManager:
    """
    Manages deployment configurations
    
    Educational Impact:
    Ensures optimal system configuration for educational effectiveness
    and performance requirements across different deployment environments.
    
    Performance Requirements:
    - Configuration load: <100ms
    - Validation: <50ms
    - Environment switching: <200ms
    """
    
    def __init__(self, config_dir: str = "config/deployment"):
        self.config_dir = Path(config_dir)
        self.logger = logging.getLogger(__name__)
        self.current_config: Optional[DeploymentConfiguration] = None
        
        # Default configurations
        self.default_configs = {
            "development": DeploymentConfiguration(
                environment="development",
                instance_count=1,
                memory_limit_mb=512,
                cpu_limit_cores=1.0,
                max_concurrent_learners=5,
                enable_ssl=False,
                database_type="sqlite",
                logging_level="DEBUG",
                backup_enabled=False,
                monitoring_interval=30,
                auto_scaling_enabled=False,
                quest3_optimization=True
            ),
            "staging": DeploymentConfiguration(
                environment="staging",
                instance_count=2,
                memory_limit_mb=1024,
                cpu_limit_cores=2.0,
                max_concurrent_learners=25,
                enable_ssl=True,
                database_type="postgresql",
                logging_level="INFO",
                backup_enabled=True,
                monitoring_interval=15,
                auto_scaling_enabled=True,
                quest3_optimization=True
            ),
            "production": DeploymentConfiguration(
                environment="production",
                instance_count=3,
                memory_limit_mb=2048,
                cpu_limit_cores=4.0,
                max_concurrent_learners=50,
                enable_ssl=True,
                database_type="postgresql",
                logging_level="WARNING",
                backup_enabled=True,
                monitoring_interval=10,
                auto_scaling_enabled=True,
                quest3_optimization=True
            )
        }
    
    async def load_configuration(self, environment: str) -> DeploymentConfiguration:
        """
        Load deployment configuration for environment
        
        Educational Impact:
        Ensures appropriate system configuration for educational requirements
        and performance expectations in different deployment scenarios.
        
        Args:
            environment: Deployment environment name
        
        Returns:
            Deployment configuration
        """
        try:
            config_file = self.config_dir / f"{environment}.yaml"
            
            if config_file.exists():
                # Load from file
                with open(config_file, 'r') as f:
                    config_data = yaml.safe_load(f)
                
                config = DeploymentConfiguration(**config_data)
                self.logger.info(f"Loaded configuration for {environment} from file")
            else:
                # Use default configuration
                config = self.default_configs.get(environment)
                if not config:
                    raise ValueError(f"No default configuration for environment: {environment}")
                
                # Save default to file
                await self.save_configuration(config)
                self.logger.info(f"Created default configuration for {environment}")
            
            # Validate configuration
            self._validate_configuration(config)
            self.current_config = config
            
            return config
            
        except Exception as e:
            self.logger.error(f"Failed to load configuration for {environment}: {e}")
            raise
    
    async def save_configuration(self, config: DeploymentConfiguration) -> None:
        """Save configuration to file"""
        try:
            # Ensure config directory exists
            self.config_dir.mkdir(parents=True, exist_ok=True)
            
            config_file = self.config_dir / f"{config.environment}.yaml"
            
            with open(config_file, 'w') as f:
                yaml.dump(asdict(config), f, default_flow_style=False)
            
            self.logger.info(f"Saved configuration for {config.environment}")
            
        except Exception as e:
            self.logger.error(f"Failed to save configuration: {e}")
            raise
    
    def _validate_configuration(self, config: DeploymentConfiguration) -> None:
        """Validate deployment configuration"""
        errors = []
        
        # Memory validation
        if config.memory_limit_mb < 256:
            errors.append("Memory limit too low for educational VR operations")
        
        # CPU validation
        if config.cpu_limit_cores < 0.5:
            errors.append("CPU limit too low for real-time learning processing")
        
        # Learner capacity validation
        if config.max_concurrent_learners > config.instance_count * 20:
            errors.append("Too many concurrent learners per instance")
        
        # Production requirements
        if config.environment == "production":
            if not config.enable_ssl:
                errors.append("SSL required for production environment")
            if config.database_type != "postgresql":
                errors.append("PostgreSQL required for production environment")
            if not config.backup_enabled:
                errors.append("Backups required for production environment")
        
        if errors:
            raise ValueError(f"Configuration validation failed: {'; '.join(errors)}")
    
    def get_service_ports(self, base_port: int = 8000) -> Dict[ServiceType, int]:
        """Get port assignments for services"""
        return {
            ServiceType.MCP_SERVER: base_port,
            ServiceType.WEBSOCKET_SERVER: base_port + 1,
            ServiceType.HEALTH_MONITOR: base_port + 2,
            ServiceType.PERFORMANCE_OPTIMIZER: base_port + 3,
            ServiceType.EDUCATIONAL_ANALYTICS: base_port + 4,
            ServiceType.DATABASE: base_port + 10
        }


class ServiceManager:
    """
    Manages individual service instances
    
    Educational Impact:
    Ensures reliable service operation for continuous educational delivery
    with proper health monitoring and performance optimization.
    
    Performance Requirements:
    - Service startup: <60 seconds
    - Health checks: <10 seconds
    - Service restart: <30 seconds
    """
    
    def __init__(self, config: DeploymentConfiguration):
        self.config = config
        self.logger = logging.getLogger(__name__)
        self.services: Dict[str, ServiceInstance] = {}
        self.service_processes: Dict[str, subprocess.Popen] = {}
        
        # Service management
        self.shutdown_event = asyncio.Event()
        self.monitoring_task: Optional[asyncio.Task] = None
        
    async def start_service(self, service_type: ServiceType, instance_id: str, port: int) -> ServiceInstance:
        """
        Start individual service instance
        
        Educational Impact:
        Ensures educational services are properly initialized and ready
        to support learner interactions and adaptive learning processes.
        
        Args:
            service_type: Type of service to start
            instance_id: Unique instance identifier
            port: Port number for service
        
        Returns:
            Started service instance
        """
        try:
            self.logger.info(f"Starting {service_type.value} instance {instance_id} on port {port}")
            
            # Create service instance record
            service = ServiceInstance(
                service_type=service_type,
                instance_id=instance_id,
                process_id=None,
                port=port,
                status=DeploymentStatus.DEPLOYING,
                memory_usage_mb=0.0,
                cpu_usage_percent=0.0,
                start_time=datetime.now(),
                health_status="starting",
                last_health_check=datetime.now()
            )
            
            # Start service process
            process = await self._start_service_process(service_type, port)
            
            if process:
                service.process_id = process.pid
                service.status = DeploymentStatus.RUNNING
                service.health_status = "healthy"
                
                # Store service and process
                self.services[instance_id] = service
                self.service_processes[instance_id] = process
                
                self.logger.info(f"Successfully started {service_type.value} instance {instance_id}")
            else:
                service.status = DeploymentStatus.FAILED
                service.health_status = "failed"
                self.logger.error(f"Failed to start {service_type.value} instance {instance_id}")
            
            return service
            
        except Exception as e:
            self.logger.error(f"Error starting service {service_type.value} instance {instance_id}: {e}")
            raise
    
    async def _start_service_process(self, service_type: ServiceType, port: int) -> Optional[subprocess.Popen]:
        """Start service process based on type"""
        try:
            python_executable = "python"
            
            if service_type == ServiceType.MCP_SERVER:
                cmd = [python_executable, "-m", "src.main", "--port", str(port)]
            elif service_type == ServiceType.WEBSOCKET_SERVER:
                cmd = [python_executable, "-m", "src.websocket.websocket_server", "--port", str(port)]
            elif service_type == ServiceType.HEALTH_MONITOR:
                cmd = [python_executable, "-c", f"from src.production.health_monitoring import HealthMonitoringFramework; import asyncio; asyncio.run(HealthMonitoringFramework().start_monitoring())"]
            elif service_type == ServiceType.PERFORMANCE_OPTIMIZER:
                cmd = [python_executable, "-c", f"from src.production.performance_optimizer import PerformanceOptimizer; import asyncio; asyncio.run(PerformanceOptimizer().start_monitoring())"]
            elif service_type == ServiceType.EDUCATIONAL_ANALYTICS:
                cmd = [python_executable, "-c", f"from src.production.educational_analytics import EducationalAnalyticsPlatform; import asyncio; platform = EducationalAnalyticsPlatform(); asyncio.run(platform.initialize())"]
            else:
                self.logger.warning(f"Unknown service type: {service_type}")
                return None
            
            # Set environment variables
            env = os.environ.copy()
            env.update({
                "MALLOC_VR_ENVIRONMENT": self.config.environment,
                "MALLOC_VR_PORT": str(port),
                "MALLOC_VR_MEMORY_LIMIT": str(self.config.memory_limit_mb),
                "MALLOC_VR_CPU_LIMIT": str(self.config.cpu_limit_cores),
                "MALLOC_VR_MAX_LEARNERS": str(self.config.max_concurrent_learners)
            })
            
            # Start process
            process = subprocess.Popen(
                cmd,
                env=env,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            # Wait a moment to check if process started successfully
            await asyncio.sleep(2)
            
            if process.poll() is None:  # Process is running
                return process
            else:
                # Process exited
                stdout, stderr = process.communicate()
                self.logger.error(f"Service process exited immediately. stdout: {stdout}, stderr: {stderr}")
                return None
                
        except Exception as e:
            self.logger.error(f"Failed to start service process: {e}")
            return None
    
    async def stop_service(self, instance_id: str) -> bool:
        """Stop service instance"""
        try:
            if instance_id not in self.services:
                self.logger.warning(f"Service instance {instance_id} not found")
                return False
            
            service = self.services[instance_id]
            service.status = DeploymentStatus.STOPPING
            
            # Stop process
            if instance_id in self.service_processes:
                process = self.service_processes[instance_id]
                process.terminate()
                
                try:
                    process.wait(timeout=10)  # Wait up to 10 seconds
                except subprocess.TimeoutExpired:
                    process.kill()  # Force kill if it doesn't stop
                
                del self.service_processes[instance_id]
            
            service.status = DeploymentStatus.STOPPED
            service.health_status = "stopped"
            
            self.logger.info(f"Stopped service instance {instance_id}")
            return True
            
        except Exception as e:
            self.logger.error(f"Error stopping service {instance_id}: {e}")
            return False
    
    async def check_service_health(self, instance_id: str) -> bool:
        """Check health of service instance"""
        try:
            if instance_id not in self.services:
                return False
            
            service = self.services[instance_id]
            
            # Check if process is running
            if instance_id in self.service_processes:
                process = self.service_processes[instance_id]
                if process.poll() is not None:  # Process has exited
                    service.status = DeploymentStatus.FAILED
                    service.health_status = "process_died"
                    return False
            
            # Update resource usage
            if service.process_id:
                try:
                    proc = psutil.Process(service.process_id)
                    service.memory_usage_mb = proc.memory_info().rss / (1024 * 1024)
                    service.cpu_usage_percent = proc.cpu_percent()
                except psutil.NoSuchProcess:
                    service.status = DeploymentStatus.FAILED
                    service.health_status = "process_not_found"
                    return False
            
            service.last_health_check = datetime.now()
            service.health_status = "healthy"
            return True
            
        except Exception as e:
            self.logger.error(f"Health check failed for {instance_id}: {e}")
            return False
    
    async def start_monitoring(self) -> None:
        """Start service monitoring"""
        if self.monitoring_task and not self.monitoring_task.done():
            return
        
        self.monitoring_task = asyncio.create_task(self._monitoring_loop())
        self.logger.info("Service monitoring started")
    
    async def stop_monitoring(self) -> None:
        """Stop service monitoring"""
        self.shutdown_event.set()
        
        if self.monitoring_task:
            try:
                await self.monitoring_task
            except asyncio.CancelledError:
                pass
        
        self.logger.info("Service monitoring stopped")
    
    async def _monitoring_loop(self) -> None:
        """Service monitoring loop"""
        while not self.shutdown_event.is_set():
            try:
                # Check health of all services
                for instance_id in list(self.services.keys()):
                    await self.check_service_health(instance_id)
                
                # Wait for next check
                await asyncio.sleep(self.config.monitoring_interval)
                
            except asyncio.CancelledError:
                break
            except Exception as e:
                self.logger.error(f"Service monitoring error: {e}")
                await asyncio.sleep(self.config.monitoring_interval)
    
    def get_service_summary(self) -> Dict[str, Any]:
        """Get summary of all services"""
        total_memory = sum(s.memory_usage_mb for s in self.services.values())
        total_cpu = sum(s.cpu_usage_percent for s in self.services.values())
        
        running_services = [s for s in self.services.values() if s.status == DeploymentStatus.RUNNING]
        failed_services = [s for s in self.services.values() if s.status == DeploymentStatus.FAILED]
        
        return {
            "total_services": len(self.services),
            "running_services": len(running_services),
            "failed_services": len(failed_services),
            "total_memory_mb": round(total_memory, 2),
            "total_cpu_percent": round(total_cpu, 2),
            "services": [
                {
                    "instance_id": s.instance_id,
                    "service_type": s.service_type.value,
                    "status": s.status.value,
                    "health": s.health_status,
                    "memory_mb": round(s.memory_usage_mb, 2),
                    "cpu_percent": round(s.cpu_usage_percent, 2),
                    "uptime_hours": (datetime.now() - s.start_time).total_seconds() / 3600
                }
                for s in self.services.values()
            ]
        }


class ProductionDeploymentManager:
    """
    Main production deployment manager
    
    Educational Impact:
    Provides comprehensive production deployment management for reliable
    educational VR service delivery with 99.9% uptime and scalable performance.
    
    Performance Requirements:
    - Full deployment: <5 minutes
    - Service scaling: <2 minutes
    - Health validation: <30 seconds
    - Recovery time: <1 minute
    """
    
    def __init__(self, environment: str = "production"):
        self.environment = environment
        self.logger = logging.getLogger(__name__)
        
        # Core components
        self.config_manager = ConfigurationManager()
        self.config: Optional[DeploymentConfiguration] = None
        self.service_manager: Optional[ServiceManager] = None
        
        # Deployment tracking
        self.deployment_id = f"deploy_{int(time.time())}"
        self.deployment_start_time = datetime.now()
        self.current_status = DeploymentStatus.PENDING
        
        # Integration components
        self.health_monitor: Optional[HealthMonitoringFramework] = None
        self.performance_optimizer: Optional[PerformanceOptimizer] = None
        self.analytics_platform: Optional[EducationalAnalyticsPlatform] = None
        
    async def initialize(self) -> None:
        """Initialize deployment manager"""
        try:
            # Load configuration
            self.config = await self.config_manager.load_configuration(self.environment)
            
            # Initialize service manager
            self.service_manager = ServiceManager(self.config)
            
            self.logger.info(f"Deployment manager initialized for {self.environment}")
            
        except Exception as e:
            self.logger.error(f"Failed to initialize deployment manager: {e}")
            raise
    
    async def deploy_full_system(self) -> DeploymentReport:
        """
        Deploy complete production system
        
        Educational Impact:
        Establishes full educational VR infrastructure for reliable learning
        delivery with comprehensive monitoring and optimization capabilities.
        
        Returns:
            Complete deployment status report
        """
        try:
            self.logger.info(f"Starting full system deployment for {self.environment}")
            self.current_status = DeploymentStatus.DEPLOYING
            
            # Get service ports
            service_ports = self.config_manager.get_service_ports()
            
            # Deploy core services
            deployed_services = []
            
            # Deploy MCP servers (multiple instances for load balancing)
            for i in range(self.config.instance_count):
                instance_id = f"mcp_server_{i}"
                port = service_ports[ServiceType.MCP_SERVER] + i
                
                service = await self.service_manager.start_service(
                    ServiceType.MCP_SERVER, instance_id, port
                )
                deployed_services.append(service)
            
            # Deploy WebSocket server
            websocket_service = await self.service_manager.start_service(
                ServiceType.WEBSOCKET_SERVER,
                "websocket_server_main",
                service_ports[ServiceType.WEBSOCKET_SERVER]
            )
            deployed_services.append(websocket_service)
            
            # Initialize and start monitoring components
            await self._deploy_monitoring_services(service_ports)
            
            # Start service monitoring
            await self.service_manager.start_monitoring()
            
            # Wait for all services to be healthy
            await self._wait_for_services_healthy(timeout_seconds=60)
            
            # Validate deployment
            deployment_valid = await self._validate_deployment()
            
            if deployment_valid:
                self.current_status = DeploymentStatus.RUNNING
                self.logger.info("Full system deployment completed successfully")
            else:
                self.current_status = DeploymentStatus.FAILED
                self.logger.error("Deployment validation failed")
            
            return await self.get_deployment_report()
            
        except Exception as e:
            self.logger.error(f"Deployment failed: {e}")
            self.current_status = DeploymentStatus.FAILED
            raise
    
    async def _deploy_monitoring_services(self, service_ports: Dict[ServiceType, int]) -> None:
        """Deploy monitoring and optimization services"""
        try:
            # Initialize health monitoring
            self.health_monitor = HealthMonitoringFramework(check_interval=self.config.monitoring_interval)
            await self.health_monitor.initialize()
            await self.health_monitor.start_monitoring()
            
            # Initialize performance optimizer
            self.performance_optimizer = PerformanceOptimizer(
                target_fps=72.0,
                max_response_time_ms=100.0
            )
            await self.performance_optimizer.initialize()
            
            # Initialize educational analytics
            self.analytics_platform = EducationalAnalyticsPlatform()
            await self.analytics_platform.initialize()
            
            self.logger.info("Monitoring services deployed successfully")
            
        except Exception as e:
            self.logger.error(f"Failed to deploy monitoring services: {e}")
            raise
    
    async def _wait_for_services_healthy(self, timeout_seconds: int = 60) -> bool:
        """Wait for all services to be healthy"""
        start_time = time.time()
        
        while time.time() - start_time < timeout_seconds:
            all_healthy = True
            
            for instance_id in self.service_manager.services.keys():
                healthy = await self.service_manager.check_service_health(instance_id)
                if not healthy:
                    all_healthy = False
                    break
            
            if all_healthy:
                self.logger.info("All services are healthy")
                return True
            
            await asyncio.sleep(2)  # Check every 2 seconds
        
        self.logger.warning(f"Services not all healthy after {timeout_seconds} seconds")
        return False
    
    async def _validate_deployment(self) -> bool:
        """Validate deployment health and functionality"""
        try:
            validation_checks = []
            
            # Check service health
            service_summary = self.service_manager.get_service_summary()
            running_services = service_summary["running_services"]
            total_services = service_summary["total_services"]
            
            if running_services == total_services:
                validation_checks.append("✓ All services running")
            else:
                validation_checks.append(f"✗ Only {running_services}/{total_services} services running")
                return False
            
            # Check system health
            if self.health_monitor:
                health_report = await self.health_monitor.get_current_health()
                if health_report.overall_status.value in ["healthy", "warning"]:
                    validation_checks.append("✓ System health acceptable")
                else:
                    validation_checks.append("✗ System health critical")
                    return False
            
            # Check performance
            if self.performance_optimizer:
                acceptable, issues = self.performance_optimizer.is_performance_acceptable()
                if acceptable:
                    validation_checks.append("✓ Performance acceptable")
                else:
                    validation_checks.append(f"✗ Performance issues: {', '.join(issues)}")
                    return False
            
            self.logger.info(f"Deployment validation: {'; '.join(validation_checks)}")
            return True
            
        except Exception as e:
            self.logger.error(f"Deployment validation failed: {e}")
            return False
    
    async def scale_deployment(self, new_instance_count: int) -> bool:
        """
        Scale deployment to new instance count
        
        Educational Impact:
        Adjusts system capacity to support varying numbers of concurrent learners
        while maintaining educational service quality and performance.
        
        Args:
            new_instance_count: New number of instances to run
        
        Returns:
            True if scaling successful
        """
        try:
            self.logger.info(f"Scaling deployment from {self.config.instance_count} to {new_instance_count} instances")
            self.current_status = DeploymentStatus.SCALING
            
            current_count = self.config.instance_count
            service_ports = self.config_manager.get_service_ports()
            
            if new_instance_count > current_count:
                # Scale up - add new instances
                for i in range(current_count, new_instance_count):
                    instance_id = f"mcp_server_{i}"
                    port = service_ports[ServiceType.MCP_SERVER] + i
                    
                    await self.service_manager.start_service(
                        ServiceType.MCP_SERVER, instance_id, port
                    )
            
            elif new_instance_count < current_count:
                # Scale down - remove instances
                for i in range(new_instance_count, current_count):
                    instance_id = f"mcp_server_{i}"
                    await self.service_manager.stop_service(instance_id)
            
            # Update configuration
            self.config.instance_count = new_instance_count
            await self.config_manager.save_configuration(self.config)
            
            # Wait for scaling to complete
            await asyncio.sleep(10)
            
            # Validate scaling
            healthy = await self._wait_for_services_healthy(timeout_seconds=30)
            
            if healthy:
                self.current_status = DeploymentStatus.RUNNING
                self.logger.info(f"Successfully scaled to {new_instance_count} instances")
                return True
            else:
                self.logger.error("Scaling validation failed")
                return False
                
        except Exception as e:
            self.logger.error(f"Scaling failed: {e}")
            self.current_status = DeploymentStatus.FAILED
            return False
    
    async def stop_deployment(self) -> bool:
        """Stop entire deployment"""
        try:
            self.logger.info("Stopping deployment")
            self.current_status = DeploymentStatus.STOPPING
            
            # Stop monitoring
            if self.health_monitor:
                await self.health_monitor.stop_monitoring()
            
            if self.performance_optimizer:
                await self.performance_optimizer.stop_monitoring()
            
            # Stop service monitoring
            if self.service_manager:
                await self.service_manager.stop_monitoring()
                
                # Stop all services
                for instance_id in list(self.service_manager.services.keys()):
                    await self.service_manager.stop_service(instance_id)
            
            self.current_status = DeploymentStatus.STOPPED
            self.logger.info("Deployment stopped successfully")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to stop deployment: {e}")
            return False
    
    async def get_deployment_report(self) -> DeploymentReport:
        """Get comprehensive deployment status report"""
        try:
            # Get service information
            services = []
            total_memory = 0.0
            total_cpu = 0.0
            
            if self.service_manager:
                for service in self.service_manager.services.values():
                    services.append(service)
                    total_memory += service.memory_usage_mb
                    total_cpu += service.cpu_usage_percent
            
            # Calculate uptime
            uptime_hours = (datetime.now() - self.deployment_start_time).total_seconds() / 3600
            
            # Get health score
            health_score = 100.0  # Default
            performance_metrics = {}
            
            if self.health_monitor:
                try:
                    health_report = await self.health_monitor.get_current_health()
                    health_score = health_report.performance_score
                except Exception:
                    pass
            
            if self.performance_optimizer:
                try:
                    performance_metrics = self.performance_optimizer.get_performance_summary()
                except Exception:
                    pass
            
            # Estimate concurrent learners (simplified)
            concurrent_learners = min(
                self.config.max_concurrent_learners,
                max(1, int(total_cpu / 10))  # Rough estimation
            )
            
            return DeploymentReport(
                deployment_id=self.deployment_id,
                environment=self.environment,
                status=self.current_status,
                services=services,
                total_memory_usage_mb=round(total_memory, 2),
                total_cpu_usage_percent=round(total_cpu, 2),
                concurrent_learners=concurrent_learners,
                uptime_hours=round(uptime_hours, 2),
                health_score=round(health_score, 1),
                performance_metrics=performance_metrics,
                deployment_time=self.deployment_start_time,
                last_update=datetime.now()
            )
            
        except Exception as e:
            self.logger.error(f"Failed to generate deployment report: {e}")
            # Return minimal report on error
            return DeploymentReport(
                deployment_id=self.deployment_id,
                environment=self.environment,
                status=self.current_status,
                services=[],
                total_memory_usage_mb=0.0,
                total_cpu_usage_percent=0.0,
                concurrent_learners=0,
                uptime_hours=0.0,
                health_score=0.0,
                performance_metrics={},
                deployment_time=self.deployment_start_time,
                last_update=datetime.now()
            )
    
    async def get_deployment_logs(self, lines: int = 100) -> List[str]:
        """Get recent deployment logs"""
        try:
            logs = []
            
            # Get service logs
            if self.service_manager:
                for instance_id, process in self.service_manager.service_processes.items():
                    try:
                        # Get stdout/stderr (simplified - in production would use proper logging)
                        logs.append(f"=== {instance_id} ===")
                        logs.append(f"Process PID: {process.pid}")
                        logs.append(f"Return code: {process.returncode}")
                    except Exception:
                        pass
            
            return logs[-lines:]  # Return last N lines
            
        except Exception as e:
            self.logger.error(f"Failed to get deployment logs: {e}")
            return [f"Error retrieving logs: {str(e)}"]


# Utility functions for deployment management

async def create_production_deployment(environment: str = "production") -> ProductionDeploymentManager:
    """
    Create and initialize production deployment manager
    
    Educational Impact:
    Establishes production-ready educational VR infrastructure with
    comprehensive monitoring and optimization for reliable learning delivery.
    
    Args:
        environment: Deployment environment
    
    Returns:
        Initialized production deployment manager
    """
    manager = ProductionDeploymentManager(environment)
    await manager.initialize()
    return manager


def setup_deployment_logging() -> None:
    """Set up specialized logging for deployment management"""
    # Create deployment specific logger
    deploy_logger = logging.getLogger("malloc_vr.deployment")
    deploy_logger.setLevel(logging.INFO)
    
    # Create file handler for deployment logs
    try:
        handler = logging.FileHandler("logs/production_deployment.log")
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        deploy_logger.addHandler(handler)
    except Exception as e:
        print(f"Warning: Could not set up deployment log file: {e}")


async def quick_deployment_health_check(manager: ProductionDeploymentManager) -> Dict[str, Any]:
    """Perform quick health check of deployment"""
    try:
        report = await manager.get_deployment_report()
        
        # Basic health assessment
        healthy_services = sum(1 for s in report.services if s.status == DeploymentStatus.RUNNING)
        total_services = len(report.services)
        
        health_status = "healthy" if healthy_services == total_services else "degraded"
        if healthy_services == 0:
            health_status = "failed"
        
        return {
            "overall_health": health_status,
            "services_running": f"{healthy_services}/{total_services}",
            "uptime_hours": report.uptime_hours,
            "memory_usage_mb": report.total_memory_usage_mb,
            "cpu_usage_percent": report.total_cpu_usage_percent,
            "concurrent_learners": report.concurrent_learners,
            "health_score": report.health_score,
            "last_check": datetime.now().isoformat()
        }
        
    except Exception as e:
        return {
            "overall_health": "error",
            "error_message": str(e),
            "last_check": datetime.now().isoformat()
        }
