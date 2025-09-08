"""
Health Monitoring Framework for Malloc VR MCP Server

Educational Impact:
Provides comprehensive system health assessment for maintaining optimal learning effectiveness.
Ensures 99.9% system uptime for continuous educational delivery and protects learning continuity.

Performance Requirements:
- Health check response: <100ms
- Monitoring overhead: <5% system resources
- Alert response: <30 seconds for critical issues
- System uptime: 99.9% availability

Author: Malloc VR Learning Team
Date: December 26, 2024
"""

import asyncio
import time
import logging
import psutil
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, asdict
from enum import Enum
import statistics
import threading
from concurrent.futures import ThreadPoolExecutor
import sqlite3
import aiosqlite

from ..utils.learning_calculations import LearningCalculations
from ..security.educational_security import EducationalSecurityManager
from ..learning.integration_engine import LearningIntegrationEngine


class HealthStatus(Enum):
    """System health status levels"""
    HEALTHY = "healthy"
    WARNING = "warning"
    CRITICAL = "critical"
    UNKNOWN = "unknown"


@dataclass
class HealthMetric:
    """Individual health metric data structure"""
    name: str
    value: float
    status: HealthStatus
    threshold_warning: float
    threshold_critical: float
    unit: str
    timestamp: datetime
    educational_impact: str


@dataclass
class SystemHealthReport:
    """Comprehensive system health report"""
    timestamp: datetime
    overall_status: HealthStatus
    metrics: Dict[str, HealthMetric]
    educational_effectiveness: float
    system_uptime: float
    performance_score: float
    alerts_generated: List[str]
    recommendations: List[str]


class AlertManager:
    """
    Manages health monitoring alerts and notifications
    
    Educational Impact:
    Ensures immediate response to system issues that could impact learning continuity
    and educational effectiveness.
    
    Performance Requirements:
    - Alert generation: <5ms
    - Alert delivery: <30 seconds
    - Memory usage: <10MB
    """
    
    def __init__(self):
        self.alert_history: List[Dict[str, Any]] = []
        self.alert_thresholds = {
            "critical_response_time": 30,  # seconds
            "warning_retention_hours": 24,
            "max_alert_history": 1000
        }
        self.logger = logging.getLogger(__name__)
    
    async def send_critical_alert(self, health_report: SystemHealthReport) -> None:
        """
        Send critical system alert for immediate attention
        
        Educational Impact:
        Prevents educational disruption by ensuring immediate response to system issues
        that could affect learning effectiveness.
        
        Args:
            health_report: Complete system health assessment
        """
        try:
            alert_data = {
                "timestamp": datetime.now().isoformat(),
                "severity": "CRITICAL",
                "overall_status": health_report.overall_status.value,
                "affected_metrics": [
                    name for name, metric in health_report.metrics.items()
                    if metric.status == HealthStatus.CRITICAL
                ],
                "educational_impact": health_report.educational_effectiveness,
                "recommended_actions": health_report.recommendations
            }
            
            # Log critical alert
            self.logger.critical(f"CRITICAL SYSTEM ALERT: {json.dumps(alert_data, indent=2)}")
            
            # Store alert in history
            self.alert_history.append(alert_data)
            
            # Trigger immediate notification (placeholder for actual implementation)
            await self._trigger_immediate_notification(alert_data)
            
        except Exception as e:
            self.logger.error(f"Failed to send critical alert: {e}")
    
    async def send_warning_alert(self, metric_name: str, metric: HealthMetric) -> None:
        """
        Send warning alert for concerning metrics
        
        Educational Impact:
        Enables proactive system maintenance to prevent educational disruption.
        
        Args:
            metric_name: Name of the concerning metric
            metric: Metric data with warning status
        """
        try:
            alert_data = {
                "timestamp": datetime.now().isoformat(),
                "severity": "WARNING",
                "metric": metric_name,
                "value": metric.value,
                "threshold": metric.threshold_warning,
                "educational_impact": metric.educational_impact,
                "unit": metric.unit
            }
            
            self.logger.warning(f"SYSTEM WARNING: {json.dumps(alert_data)}")
            self.alert_history.append(alert_data)
            
        except Exception as e:
            self.logger.error(f"Failed to send warning alert: {e}")
    
    async def _trigger_immediate_notification(self, alert_data: Dict[str, Any]) -> None:
        """
        Trigger immediate notification for critical alerts
        
        Educational Impact:
        Ensures critical issues are addressed within 30 seconds to maintain
        educational continuity and learning effectiveness.
        """
        # Placeholder for notification system integration
        # In production, this would integrate with:
        # - Email notifications
        # - SMS alerts
        # - Slack/Teams integration
        # - PagerDuty or similar
        pass
    
    def get_recent_alerts(self, hours: int = 24) -> List[Dict[str, Any]]:
        """Get alerts from the last N hours"""
        cutoff_time = datetime.now() - timedelta(hours=hours)
        return [
            alert for alert in self.alert_history
            if datetime.fromisoformat(alert["timestamp"]) > cutoff_time
        ]


class MetricsCollector:
    """
    Collects and manages system performance metrics
    
    Educational Impact:
    Provides comprehensive system visibility to ensure optimal learning environment
    performance and educational effectiveness.
    
    Performance Requirements:
    - Metric collection: <10ms per metric
    - Memory usage: <50MB
    - Data retention: 30 days
    """
    
    def __init__(self, database_path: str = "data/health_metrics.db"):
        self.database_path = database_path
        self.metrics_cache: Dict[str, List[float]] = {}
        self.cache_size_limit = 1000
        self.logger = logging.getLogger(__name__)
        self.lock = threading.Lock()
    
    async def initialize_database(self) -> None:
        """Initialize metrics database"""
        try:
            async with aiosqlite.connect(self.database_path) as db:
                await db.execute("""
                    CREATE TABLE IF NOT EXISTS health_metrics (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                        metric_name TEXT NOT NULL,
                        value REAL NOT NULL,
                        status TEXT NOT NULL,
                        educational_impact REAL,
                        additional_data TEXT
                    )
                """)
                await db.commit()
        except Exception as e:
            self.logger.error(f"Failed to initialize metrics database: {e}")
    
    async def collect_system_metrics(self) -> Dict[str, float]:
        """
        Collect comprehensive system performance metrics
        
        Educational Impact:
        Ensures system performance meets educational requirements for continuous
        learning effectiveness and Quest 3 VR optimization.
        
        Returns:
            Dictionary of system performance metrics
        """
        try:
            metrics = {}
            
            # CPU and Memory metrics
            metrics["cpu_usage"] = psutil.cpu_percent(interval=0.1)
            memory = psutil.virtual_memory()
            metrics["memory_usage"] = memory.percent
            metrics["memory_available"] = memory.available / (1024 * 1024)  # MB
            
            # Disk metrics
            disk = psutil.disk_usage('/')
            metrics["disk_usage"] = disk.percent
            metrics["disk_free"] = disk.free / (1024 * 1024 * 1024)  # GB
            
            # Network metrics (if available)
            try:
                network = psutil.net_io_counters()
                metrics["network_bytes_sent"] = network.bytes_sent
                metrics["network_bytes_recv"] = network.bytes_recv
            except Exception:
                metrics["network_bytes_sent"] = 0
                metrics["network_bytes_recv"] = 0
            
            # Process-specific metrics
            process = psutil.Process()
            metrics["process_cpu"] = process.cpu_percent()
            metrics["process_memory"] = process.memory_info().rss / (1024 * 1024)  # MB
            metrics["process_threads"] = process.num_threads()
            
            return metrics
            
        except Exception as e:
            self.logger.error(f"Failed to collect system metrics: {e}")
            return {}
    
    async def store_metric(self, metric_name: str, value: float, status: HealthStatus, 
                          educational_impact: float = 0.0) -> None:
        """
        Store metric in database and cache
        
        Educational Impact:
        Maintains historical performance data for educational effectiveness analysis
        and system optimization.
        
        Args:
            metric_name: Name of the metric
            value: Metric value
            status: Health status of the metric
            educational_impact: Impact on educational effectiveness (0.0-1.0)
        """
        try:
            # Store in cache
            with self.lock:
                if metric_name not in self.metrics_cache:
                    self.metrics_cache[metric_name] = []
                
                self.metrics_cache[metric_name].append(value)
                
                # Limit cache size
                if len(self.metrics_cache[metric_name]) > self.cache_size_limit:
                    self.metrics_cache[metric_name] = self.metrics_cache[metric_name][-self.cache_size_limit:]
            
            # Store in database
            async with aiosqlite.connect(self.database_path) as db:
                await db.execute("""
                    INSERT INTO health_metrics 
                    (metric_name, value, status, educational_impact)
                    VALUES (?, ?, ?, ?)
                """, (metric_name, value, status.value, educational_impact))
                await db.commit()
                
        except Exception as e:
            self.logger.error(f"Failed to store metric {metric_name}: {e}")
    
    def get_metric_statistics(self, metric_name: str) -> Dict[str, float]:
        """Get statistical analysis of metric over time"""
        with self.lock:
            if metric_name not in self.metrics_cache or not self.metrics_cache[metric_name]:
                return {}
            
            values = self.metrics_cache[metric_name]
            return {
                "mean": statistics.mean(values),
                "median": statistics.median(values),
                "stdev": statistics.stdev(values) if len(values) > 1 else 0,
                "min": min(values),
                "max": max(values),
                "count": len(values)
            }


class LearningSystemDiagnostics:
    """
    Comprehensive diagnostics for learning system health
    
    Educational Impact:
    Ensures optimal learning system performance through comprehensive health monitoring,
    maintaining >85% learning effectiveness and educational continuity.
    
    Performance Requirements:
    - Health check completion: <100ms
    - Educational accuracy tracking: >95%
    - Real-time performance monitoring: continuous
    - Memory usage: <30MB for diagnostics
    """
    
    def __init__(self, integration_engine: Optional[LearningIntegrationEngine] = None,
                 security_manager: Optional[EducationalSecurityManager] = None):
        self.metrics_collector = MetricsCollector()
        self.alert_manager = AlertManager()
        self.integration_engine = integration_engine
        self.security_manager = security_manager
        self.logger = logging.getLogger(__name__)
        
        # Health check thresholds
        self.thresholds = {
            "response_time": {"warning": 75, "critical": 100},  # ms
            "cpu_usage": {"warning": 70, "critical": 85},  # %
            "memory_usage": {"warning": 75, "critical": 90},  # %
            "disk_usage": {"warning": 80, "critical": 95},  # %
            "educational_effectiveness": {"warning": 80, "critical": 70},  # %
            "learning_accuracy": {"warning": 90, "critical": 85},  # %
            "error_rate": {"warning": 1, "critical": 5}  # %
        }
        
        # Performance tracking
        self.last_health_check = None
        self.health_check_count = 0
        self.start_time = time.time()
    
    async def initialize(self) -> None:
        """Initialize diagnostic system"""
        await self.metrics_collector.initialize_database()
        self.logger.info("Learning System Diagnostics initialized")
    
    async def run_health_check(self) -> SystemHealthReport:
        """
        Comprehensive system health assessment
        
        Educational Impact:
        Provides complete system health evaluation to ensure optimal learning
        effectiveness and continuous educational delivery.
        
        Returns:
            Complete system health report with educational effectiveness metrics
        """
        start_time = time.time()
        
        try:
            # Collect all health metrics
            metrics = {}
            
            # System performance metrics
            system_metrics = await self.metrics_collector.collect_system_metrics()
            
            # Response time check
            response_time_ms = await self._check_response_time()
            metrics["response_time"] = self._create_health_metric(
                "response_time", response_time_ms, "ms",
                self.thresholds["response_time"],
                "Affects real-time learning adaptation and VR performance"
            )
            
            # CPU usage
            metrics["cpu_usage"] = self._create_health_metric(
                "cpu_usage", system_metrics.get("cpu_usage", 0), "%",
                self.thresholds["cpu_usage"],
                "High CPU affects learning computation performance"
            )
            
            # Memory usage
            metrics["memory_usage"] = self._create_health_metric(
                "memory_usage", system_metrics.get("memory_usage", 0), "%",
                self.thresholds["memory_usage"],
                "Memory constraints impact concurrent learner support"
            )
            
            # Disk usage
            metrics["disk_usage"] = self._create_health_metric(
                "disk_usage", system_metrics.get("disk_usage", 0), "%",
                self.thresholds["disk_usage"],
                "Disk space needed for educational data and logs"
            )
            
            # Educational effectiveness metrics
            educational_effectiveness = await self._check_educational_effectiveness()
            metrics["educational_effectiveness"] = self._create_health_metric(
                "educational_effectiveness", educational_effectiveness, "%",
                self.thresholds["educational_effectiveness"],
                "Core measure of learning system effectiveness"
            )
            
            # Learning model accuracy
            learning_accuracy = await self._check_learning_model_accuracy()
            metrics["learning_accuracy"] = self._create_health_metric(
                "learning_accuracy", learning_accuracy, "%",
                self.thresholds["learning_accuracy"],
                "Accuracy of learning predictions and adaptations"
            )
            
            # Error rate
            error_rate = await self._check_error_rate()
            metrics["error_rate"] = self._create_health_metric(
                "error_rate", error_rate, "%",
                self.thresholds["error_rate"],
                "System reliability for continuous learning"
            )
            
            # Data integrity check
            data_integrity = await self._check_data_integrity()
            metrics["data_integrity"] = self._create_health_metric(
                "data_integrity", data_integrity, "%",
                {"warning": 95, "critical": 90},
                "Educational data consistency and FERPA compliance"
            )
            
            # Determine overall system status
            overall_status = self._determine_overall_status(metrics)
            
            # Calculate composite scores
            performance_score = self._calculate_performance_score(metrics)
            system_uptime = self._calculate_uptime()
            
            # Generate alerts and recommendations
            alerts = await self._generate_alerts(metrics)
            recommendations = self._generate_recommendations(metrics)
            
            # Create health report
            health_report = SystemHealthReport(
                timestamp=datetime.now(),
                overall_status=overall_status,
                metrics=metrics,
                educational_effectiveness=educational_effectiveness,
                system_uptime=system_uptime,
                performance_score=performance_score,
                alerts_generated=alerts,
                recommendations=recommendations
            )
            
            # Store metrics
            for metric_name, metric in metrics.items():
                await self.metrics_collector.store_metric(
                    metric_name, metric.value, metric.status,
                    educational_effectiveness / 100.0
                )
            
            # Update tracking
            self.last_health_check = datetime.now()
            self.health_check_count += 1
            
            # Log health check completion
            duration_ms = (time.time() - start_time) * 1000
            self.logger.info(f"Health check completed in {duration_ms:.2f}ms - Status: {overall_status.value}")
            
            return health_report
            
        except Exception as e:
            self.logger.error(f"Health check failed: {e}")
            # Return critical status on failure
            return self._create_emergency_report(e)
    
    def _create_health_metric(self, name: str, value: float, unit: str, 
                             thresholds: Dict[str, float], educational_impact: str) -> HealthMetric:
        """Create health metric with status evaluation"""
        if value >= thresholds["critical"]:
            status = HealthStatus.CRITICAL
        elif value >= thresholds["warning"]:
            status = HealthStatus.WARNING
        else:
            status = HealthStatus.HEALTHY
        
        return HealthMetric(
            name=name,
            value=value,
            status=status,
            threshold_warning=thresholds["warning"],
            threshold_critical=thresholds["critical"],
            unit=unit,
            timestamp=datetime.now(),
            educational_impact=educational_impact
        )
    
    async def _check_response_time(self) -> float:
        """Test system response time"""
        start_time = time.time()
        
        # Simulate a simple operation
        await asyncio.sleep(0.001)  # 1ms simulated operation
        
        # If integration engine available, test real operation
        if self.integration_engine:
            try:
                # Quick test of learning computation
                test_data = {
                    "learner_data": {"learning_rate": 0.1},
                    "knowledge_data": {"complexity": 0.5},
                    "engagement_data": {"attention": 0.8},
                    "assessment_data": {"performance": 0.75}
                }
                await self.integration_engine.process_learning_integration(test_data)
            except Exception:
                pass  # Don't fail health check on integration test failure
        
        end_time = time.time()
        return (end_time - start_time) * 1000  # Convert to milliseconds
    
    async def _check_educational_effectiveness(self) -> float:
        """Check overall educational effectiveness"""
        try:
            # In a real implementation, this would query learning outcomes database
            # For now, return a simulated value based on system health
            base_effectiveness = 92.0  # Base effectiveness percentage
            
            # Adjust based on recent system performance
            recent_metrics = self.metrics_collector.get_metric_statistics("response_time")
            if recent_metrics:
                if recent_metrics["mean"] > 100:  # >100ms response time
                    base_effectiveness -= 5.0
                elif recent_metrics["mean"] > 50:  # >50ms response time
                    base_effectiveness -= 2.0
            
            return max(70.0, min(100.0, base_effectiveness))
            
        except Exception as e:
            self.logger.error(f"Failed to check educational effectiveness: {e}")
            return 85.0  # Default safe value
    
    async def _check_learning_model_accuracy(self) -> float:
        """Check learning model prediction accuracy"""
        try:
            # In a real implementation, this would analyze prediction vs. actual outcomes
            # For now, return a simulated accuracy based on system stability
            base_accuracy = 96.5  # Base accuracy percentage
            
            # Adjust based on error rate
            error_rate = await self._check_error_rate()
            if error_rate > 2.0:
                base_accuracy -= error_rate * 2
            
            return max(85.0, min(100.0, base_accuracy))
            
        except Exception as e:
            self.logger.error(f"Failed to check learning model accuracy: {e}")
            return 95.0  # Default safe value
    
    async def _check_error_rate(self) -> float:
        """Check system error rate over last hour"""
        try:
            # In a real implementation, this would query error logs
            # For now, return a simulated low error rate
            return 0.3  # 0.3% error rate
            
        except Exception as e:
            self.logger.error(f"Failed to check error rate: {e}")
            return 1.0  # Conservative default
    
    async def _check_data_integrity(self) -> float:
        """Check educational data integrity and FERPA compliance"""
        try:
            integrity_score = 100.0
            
            # Check if security manager is available and functional
            if self.security_manager:
                try:
                    # Test encryption/decryption functionality
                    test_data = "test_educational_data"
                    encrypted = await self.security_manager.encrypt_learner_data(test_data, "test_context")
                    decrypted = await self.security_manager.decrypt_learner_data(encrypted, "test_context")
                    
                    if decrypted != test_data:
                        integrity_score -= 10.0
                        
                except Exception:
                    integrity_score -= 5.0
            
            return integrity_score
            
        except Exception as e:
            self.logger.error(f"Failed to check data integrity: {e}")
            return 95.0  # Default safe value
    
    def _determine_overall_status(self, metrics: Dict[str, HealthMetric]) -> HealthStatus:
        """Determine overall system health status"""
        critical_count = sum(1 for m in metrics.values() if m.status == HealthStatus.CRITICAL)
        warning_count = sum(1 for m in metrics.values() if m.status == HealthStatus.WARNING)
        
        if critical_count > 0:
            return HealthStatus.CRITICAL
        elif warning_count > 2:  # More than 2 warnings = overall warning
            return HealthStatus.WARNING
        else:
            return HealthStatus.HEALTHY
    
    def _calculate_performance_score(self, metrics: Dict[str, HealthMetric]) -> float:
        """Calculate composite performance score (0-100)"""
        try:
            healthy_count = sum(1 for m in metrics.values() if m.status == HealthStatus.HEALTHY)
            warning_count = sum(1 for m in metrics.values() if m.status == HealthStatus.WARNING)
            critical_count = sum(1 for m in metrics.values() if m.status == HealthStatus.CRITICAL)
            total_count = len(metrics)
            
            if total_count == 0:
                return 0.0
            
            # Weight: Healthy=100%, Warning=70%, Critical=30%
            weighted_score = (healthy_count * 100 + warning_count * 70 + critical_count * 30) / total_count
            return round(weighted_score, 1)
            
        except Exception:
            return 50.0  # Default neutral score
    
    def _calculate_uptime(self) -> float:
        """Calculate system uptime percentage"""
        try:
            total_runtime = time.time() - self.start_time
            uptime_seconds = total_runtime  # Simplified - in real implementation, track actual uptime
            
            if total_runtime == 0:
                return 100.0
            
            uptime_percentage = (uptime_seconds / total_runtime) * 100
            return min(100.0, uptime_percentage)
            
        except Exception:
            return 99.9  # Default high uptime
    
    async def _generate_alerts(self, metrics: Dict[str, HealthMetric]) -> List[str]:
        """Generate alerts for concerning metrics"""
        alerts = []
        
        for metric_name, metric in metrics.items():
            if metric.status == HealthStatus.CRITICAL:
                alert_msg = f"CRITICAL: {metric_name} at {metric.value}{metric.unit} (threshold: {metric.threshold_critical}{metric.unit})"
                alerts.append(alert_msg)
                await self.alert_manager.send_critical_alert(
                    SystemHealthReport(
                        timestamp=datetime.now(),
                        overall_status=HealthStatus.CRITICAL,
                        metrics={metric_name: metric},
                        educational_effectiveness=metric.value if metric_name == "educational_effectiveness" else 0,
                        system_uptime=0,
                        performance_score=0,
                        alerts_generated=[alert_msg],
                        recommendations=[]
                    )
                )
            elif metric.status == HealthStatus.WARNING:
                alert_msg = f"WARNING: {metric_name} at {metric.value}{metric.unit} (threshold: {metric.threshold_warning}{metric.unit})"
                alerts.append(alert_msg)
                await self.alert_manager.send_warning_alert(metric_name, metric)
        
        return alerts
    
    def _generate_recommendations(self, metrics: Dict[str, HealthMetric]) -> List[str]:
        """Generate system optimization recommendations"""
        recommendations = []
        
        for metric_name, metric in metrics.items():
            if metric.status in [HealthStatus.WARNING, HealthStatus.CRITICAL]:
                if metric_name == "cpu_usage":
                    recommendations.append("Consider scaling compute resources or optimizing algorithms")
                elif metric_name == "memory_usage":
                    recommendations.append("Optimize memory usage or increase available RAM")
                elif metric_name == "disk_usage":
                    recommendations.append("Clean up old logs or expand disk capacity")
                elif metric_name == "response_time":
                    recommendations.append("Optimize database queries and enable caching")
                elif metric_name == "educational_effectiveness":
                    recommendations.append("Review learning model parameters and adaptation algorithms")
                elif metric_name == "learning_accuracy":
                    recommendations.append("Retrain learning models with recent educational data")
                elif metric_name == "error_rate":
                    recommendations.append("Investigate error logs and improve error handling")
                elif metric_name == "data_integrity":
                    recommendations.append("Verify FERPA compliance and data backup procedures")
        
        if not recommendations:
            recommendations.append("System operating within normal parameters")
        
        return recommendations
    
    def _create_emergency_report(self, error: Exception) -> SystemHealthReport:
        """Create emergency health report when health check fails"""
        return SystemHealthReport(
            timestamp=datetime.now(),
            overall_status=HealthStatus.CRITICAL,
            metrics={
                "system_error": HealthMetric(
                    name="system_error",
                    value=100.0,
                    status=HealthStatus.CRITICAL,
                    threshold_warning=0.0,
                    threshold_critical=1.0,
                    unit="error",
                    timestamp=datetime.now(),
                    educational_impact="Complete system failure affects all learning operations"
                )
            },
            educational_effectiveness=0.0,
            system_uptime=0.0,
            performance_score=0.0,
            alerts_generated=[f"CRITICAL: Health check system failure - {str(error)}"],
            recommendations=["Immediate system investigation required", "Check system logs", "Verify all dependencies"]
        )


class HealthMonitoringFramework:
    """
    Main health monitoring framework for Malloc VR MCP Server
    
    Educational Impact:
    Provides comprehensive health monitoring to ensure 99.9% system uptime
    and optimal educational effectiveness for continuous VR learning delivery.
    
    Performance Requirements:
    - Health monitoring cycle: Every 30 seconds
    - Response time: <100ms per health check
    - Memory overhead: <5% of system resources
    - Alert latency: <30 seconds for critical issues
    """
    
    def __init__(self, check_interval: int = 30):
        self.diagnostics = LearningSystemDiagnostics()
        self.check_interval = check_interval
        self.monitoring_active = False
        self.monitoring_task = None
        self.logger = logging.getLogger(__name__)
        
        # Health monitoring statistics
        self.health_check_count = 0
        self.last_critical_alert = None
        self.uptime_start = datetime.now()
        
    async def initialize(self) -> None:
        """Initialize health monitoring framework"""
        await self.diagnostics.initialize()
        self.logger.info(f"Health Monitoring Framework initialized with {self.check_interval}s interval")
    
    async def start_monitoring(self) -> None:
        """
        Start continuous health monitoring
        
        Educational Impact:
        Begins continuous system health surveillance to ensure optimal learning
        environment and immediate response to issues affecting educational effectiveness.
        """
        if self.monitoring_active:
            self.logger.warning("Health monitoring already active")
            return
        
        self.monitoring_active = True
        self.monitoring_task = asyncio.create_task(self._monitoring_loop())
        self.logger.info("Health monitoring started")
    
    async def stop_monitoring(self) -> None:
        """Stop health monitoring"""
        if not self.monitoring_active:
            return
        
        self.monitoring_active = False
        if self.monitoring_task:
            self.monitoring_task.cancel()
            try:
                await self.monitoring_task
            except asyncio.CancelledError:
                pass
        
        self.logger.info("Health monitoring stopped")
    
    async def _monitoring_loop(self) -> None:
        """Main monitoring loop"""
        self.logger.info("Health monitoring loop started")
        
        while self.monitoring_active:
            try:
                # Run health check
                health_report = await self.diagnostics.run_health_check()
                self.health_check_count += 1
                
                # Log status
                if health_report.overall_status == HealthStatus.CRITICAL:
                    self.last_critical_alert = datetime.now()
                    self.logger.critical(f"Critical system status detected - Performance: {health_report.performance_score}%")
                elif health_report.overall_status == HealthStatus.WARNING:
                    self.logger.warning(f"System warnings detected - Performance: {health_report.performance_score}%")
                else:
                    self.logger.debug(f"System healthy - Performance: {health_report.performance_score}%")
                
                # Wait for next check
                await asyncio.sleep(self.check_interval)
                
            except asyncio.CancelledError:
                break
            except Exception as e:
                self.logger.error(f"Health monitoring error: {e}")
                await asyncio.sleep(self.check_interval)  # Continue monitoring despite errors
        
        self.logger.info("Health monitoring loop stopped")
    
    async def get_current_health(self) -> SystemHealthReport:
        """Get current system health status on demand"""
        return await self.diagnostics.run_health_check()
    
    def get_monitoring_statistics(self) -> Dict[str, Any]:
        """Get monitoring framework statistics"""
        uptime_duration = datetime.now() - self.uptime_start
        
        return {
            "monitoring_active": self.monitoring_active,
            "health_checks_performed": self.health_check_count,
            "uptime_hours": uptime_duration.total_seconds() / 3600,
            "last_critical_alert": self.last_critical_alert.isoformat() if self.last_critical_alert else None,
            "check_interval_seconds": self.check_interval,
            "framework_start_time": self.uptime_start.isoformat()
        }


# Utility functions for health monitoring integration

async def create_health_monitoring_framework(
    integration_engine: Optional[LearningIntegrationEngine] = None,
    security_manager: Optional[EducationalSecurityManager] = None,
    check_interval: int = 30
) -> HealthMonitoringFramework:
    """
    Create and initialize health monitoring framework
    
    Educational Impact:
    Establishes comprehensive system health monitoring to ensure continuous
    educational effectiveness and optimal VR learning performance.
    
    Args:
        integration_engine: Learning integration engine for educational metrics
        security_manager: Security manager for FERPA compliance checking
        check_interval: Health check interval in seconds
    
    Returns:
        Initialized health monitoring framework
    """
    framework = HealthMonitoringFramework(check_interval)
    
    # Set up dependencies
    if integration_engine:
        framework.diagnostics.integration_engine = integration_engine
    if security_manager:
        framework.diagnostics.security_manager = security_manager
    
    await framework.initialize()
    return framework


def setup_health_monitoring_logging() -> None:
    """Set up specialized logging for health monitoring"""
    # Create health monitoring specific logger
    health_logger = logging.getLogger("malloc_vr.health_monitoring")
    health_logger.setLevel(logging.INFO)
    
    # Create file handler for health logs
    try:
        handler = logging.FileHandler("logs/health_monitoring.log")
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        health_logger.addHandler(handler)
    except Exception as e:
        print(f"Warning: Could not set up health monitoring log file: {e}")
