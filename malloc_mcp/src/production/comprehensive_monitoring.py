"""
Comprehensive Production Monitoring and Health Management
Implements production-ready monitoring with educational metrics
"""

import asyncio
import logging
from typing import Dict, Any, List, Optional
from datetime import datetime, timedelta
from dataclasses import dataclass
import json
import psutil
import time

# Configure logging for production monitoring
logger = logging.getLogger(__name__)


@dataclass
class EducationalMetric:
    """Educational-specific metric definition"""
    name: str
    value: float
    unit: str
    timestamp: datetime
    learner_context: Dict[str, Any]
    critical_threshold: Optional[float] = None
    warning_threshold: Optional[float] = None


@dataclass
class HealthCheckResult:
    """Health check result with educational context"""
    service_name: str
    healthy: bool
    response_time_ms: float
    educational_impact: str
    vr_performance_impact: str
    ferpa_compliance_status: str
    issues: List[str]
    timestamp: datetime


class ComprehensiveEducationalMonitoring:
    """
    Comprehensive monitoring system for educational VR services
    
    Educational Focus:
    - Monitors learning continuity metrics
    - Tracks VR performance for Quest 3 optimization
    - Ensures FERPA compliance monitoring
    - Validates spatial precision maintenance
    
    Performance Requirements:
    - Quest 3 VR: <5ms monitoring overhead
    - Response time: <100ms for health checks
    - Memory usage: <200MB for monitoring system
    """
    
    def __init__(self):
        self.monitoring_interval = 30  # seconds
        self.health_checks = {}
        self.educational_metrics = {}
        self.alert_handlers = []
        
        # Educational monitoring targets
        self.performance_targets = {
            'learning_model_response_ms': 100,
            'engagement_processing_ms': 50,
            'assessment_evaluation_ms': 200,
            'transition_decision_ms': 500,
            'integration_computation_ms': 10,
            'concurrent_learners_supported': 50,
            'vr_fps_target': 72,
            'spatial_precision_tolerance': 0.0001
        }
        
        # System health thresholds
        self.health_thresholds = {
            'cpu_usage_warning': 70,
            'cpu_usage_critical': 85,
            'memory_usage_warning': 80,
            'memory_usage_critical': 90,
            'disk_usage_warning': 75,
            'disk_usage_critical': 85,
            'response_time_warning': 100,
            'response_time_critical': 500
        }
        
        # Educational quality metrics
        self.educational_quality_targets = {
            'learning_model_accuracy': 0.90,
            'engagement_correlation': 0.85,
            'assessment_validity': 0.95,
            'ferpa_compliance_rate': 1.0,
            'real_time_adaptation_latency': 100
        }
        
        # Monitoring state
        self.monitoring_active = False
        self.last_health_check = None
        self.system_metrics_history = []
        self.educational_metrics_history = []
        
    async def start_comprehensive_monitoring(self):
        """Start comprehensive educational monitoring system"""
        
        logger.info("Starting comprehensive educational monitoring system")
        
        self.monitoring_active = True
        
        # Start monitoring tasks
        await asyncio.gather(
            self._monitor_system_health(),
            self._monitor_educational_performance(),
            self._monitor_vr_performance(),
            self._monitor_ferpa_compliance(),
            self._monitor_learning_continuity(),
            return_exceptions=True
        )
    
    async def _monitor_system_health(self):
        """Monitor basic system health metrics"""
        
        while self.monitoring_active:
            try:
                # Collect system metrics
                cpu_percent = psutil.cpu_percent(interval=1)
                memory = psutil.virtual_memory()
                disk = psutil.disk_usage('/')
                
                # Check system health
                system_health = {
                    'cpu_usage': cpu_percent,
                    'memory_usage': memory.percent,
                    'disk_usage': disk.percent,
                    'memory_available_gb': memory.available / (1024**3),
                    'disk_free_gb': disk.free / (1024**3),
                    'timestamp': datetime.now()
                }
                
                # Store metrics
                self.system_metrics_history.append(system_health)
                
                # Keep only last 1000 measurements
                if len(self.system_metrics_history) > 1000:
                    self.system_metrics_history = self.system_metrics_history[-1000:]
                
                # Check thresholds and alert if necessary
                await self._check_system_health_thresholds(system_health)
                
                # Wait for next monitoring cycle
                await asyncio.sleep(self.monitoring_interval)
                
            except Exception as e:
                logger.error(f"System health monitoring error: {e}")
                await asyncio.sleep(5)  # Short retry delay
    
    async def _monitor_educational_performance(self):
        """Monitor educational-specific performance metrics"""
        
        while self.monitoring_active:
            try:
                # Simulate educational performance monitoring
                # In production, these would be real metrics from services
                
                educational_metrics = {
                    'active_learning_sessions': await self._get_active_learning_sessions_count(),
                    'learning_model_avg_response_ms': await self._get_learning_model_response_time(),
                    'assessment_processing_avg_ms': await self._get_assessment_processing_time(),
                    'spatial_precision_accuracy': await self._get_spatial_precision_accuracy(),
                    'engagement_tracking_latency_ms': await self._get_engagement_tracking_latency(),
                    'learning_progression_rate': await self._get_learning_progression_rate(),
                    'timestamp': datetime.now()
                }
                
                # Store educational metrics
                self.educational_metrics_history.append(educational_metrics)
                
                # Keep only last 1000 measurements
                if len(self.educational_metrics_history) > 1000:
                    self.educational_metrics_history = self.educational_metrics_history[-1000:]
                
                # Check educational performance thresholds
                await self._check_educational_performance_thresholds(educational_metrics)
                
                await asyncio.sleep(self.monitoring_interval)
                
            except Exception as e:
                logger.error(f"Educational performance monitoring error: {e}")
                await asyncio.sleep(5)
    
    async def _monitor_vr_performance(self):
        """Monitor VR-specific performance metrics for Quest 3 optimization"""
        
        while self.monitoring_active:
            try:
                vr_metrics = {
                    'average_fps': await self._get_vr_fps_metrics(),
                    'frame_time_ms': await self._get_vr_frame_time(),
                    'spatial_tracking_latency_ms': await self._get_spatial_tracking_latency(),
                    'vr_comfort_score': await self._get_vr_comfort_score(),
                    'motion_sickness_incidents': await self._get_motion_sickness_incidents(),
                    'vr_session_duration_avg_minutes': await self._get_vr_session_duration(),
                    'timestamp': datetime.now()
                }
                
                # Check VR performance against Quest 3 targets
                await self._check_vr_performance_thresholds(vr_metrics)
                
                await asyncio.sleep(15)  # More frequent VR monitoring
                
            except Exception as e:
                logger.error(f"VR performance monitoring error: {e}")
                await asyncio.sleep(5)
    
    async def _monitor_ferpa_compliance(self):
        """Monitor FERPA compliance metrics"""
        
        while self.monitoring_active:
            try:
                ferpa_metrics = {
                    'data_encryption_rate': await self._get_data_encryption_rate(),
                    'access_control_violations': await self._get_access_control_violations(),
                    'data_retention_compliance': await self._get_data_retention_compliance(),
                    'cross_learner_data_leakage_incidents': await self._get_data_leakage_incidents(),
                    'consent_tracking_accuracy': await self._get_consent_tracking_accuracy(),
                    'audit_log_completeness': await self._get_audit_log_completeness(),
                    'timestamp': datetime.now()
                }
                
                # Check FERPA compliance thresholds
                await self._check_ferpa_compliance_thresholds(ferpa_metrics)
                
                await asyncio.sleep(60)  # FERPA monitoring every minute
                
            except Exception as e:
                logger.error(f"FERPA compliance monitoring error: {e}")
                await asyncio.sleep(10)
    
    async def _monitor_learning_continuity(self):
        """Monitor learning continuity and educational effectiveness"""
        
        while self.monitoring_active:
            try:
                continuity_metrics = {
                    'learning_session_interruptions': await self._get_session_interruptions(),
                    'assessment_completion_rate': await self._get_assessment_completion_rate(),
                    'learning_progression_consistency': await self._get_progression_consistency(),
                    'adaptive_algorithm_effectiveness': await self._get_adaptive_effectiveness(),
                    'learner_satisfaction_score': await self._get_learner_satisfaction(),
                    'educational_goal_achievement_rate': await self._get_goal_achievement_rate(),
                    'timestamp': datetime.now()
                }
                
                # Check learning continuity thresholds
                await self._check_learning_continuity_thresholds(continuity_metrics)
                
                await asyncio.sleep(120)  # Learning continuity every 2 minutes
                
            except Exception as e:
                logger.error(f"Learning continuity monitoring error: {e}")
                await asyncio.sleep(10)
    
    async def perform_comprehensive_health_check(self) -> Dict[str, Any]:
        """Perform comprehensive health check of all educational services"""
        
        logger.info("Performing comprehensive educational health check")
        
        health_results = {
            'overall_health': True,
            'timestamp': datetime.now().isoformat(),
            'services': {},
            'educational_metrics': {},
            'vr_performance': {},
            'ferpa_compliance': {},
            'recommendations': []
        }
        
        # Check individual service health
        services_to_check = [
            'mcp-gateway',
            'learner-service',
            'knowledge-service',
            'engagement-service',
            'assessment-service',
            'transition-service',
            'websocket-service',
            'blender-service'
        ]
        
        for service in services_to_check:
            service_health = await self._check_service_health(service)
            health_results['services'][service] = service_health
            
            if not service_health.healthy:
                health_results['overall_health'] = False
        
        # Check educational metrics
        health_results['educational_metrics'] = await self._get_educational_health_summary()
        
        # Check VR performance
        health_results['vr_performance'] = await self._get_vr_performance_summary()
        
        # Check FERPA compliance
        health_results['ferpa_compliance'] = await self._get_ferpa_compliance_summary()
        
        # Generate recommendations
        health_results['recommendations'] = await self._generate_health_recommendations(health_results)
        
        self.last_health_check = health_results
        
        return health_results
    
    async def _check_service_health(self, service_name: str) -> HealthCheckResult:
        """Check health of individual educational service"""
        
        start_time = time.time()
        
        try:
            # Simulate health check (in production, would make actual HTTP request)
            await asyncio.sleep(0.01)  # Simulate network delay
            
            response_time_ms = (time.time() - start_time) * 1000
            
            # Determine health based on response time and service status
            healthy = response_time_ms < self.health_thresholds['response_time_critical']
            
            # Assess educational impact
            educational_impact = self._assess_service_educational_impact(service_name, healthy)
            vr_performance_impact = self._assess_service_vr_impact(service_name, healthy)
            ferpa_compliance_status = self._assess_service_ferpa_impact(service_name, healthy)
            
            issues = []
            if response_time_ms > self.health_thresholds['response_time_warning']:
                issues.append(f"High response time: {response_time_ms:.1f}ms")
            
            return HealthCheckResult(
                service_name=service_name,
                healthy=healthy,
                response_time_ms=response_time_ms,
                educational_impact=educational_impact,
                vr_performance_impact=vr_performance_impact,
                ferpa_compliance_status=ferpa_compliance_status,
                issues=issues,
                timestamp=datetime.now()
            )
            
        except Exception as e:
            return HealthCheckResult(
                service_name=service_name,
                healthy=False,
                response_time_ms=(time.time() - start_time) * 1000,
                educational_impact="learning_disruption_possible",
                vr_performance_impact="vr_experience_degraded",
                ferpa_compliance_status="compliance_at_risk",
                issues=[f"Health check failed: {str(e)}"],
                timestamp=datetime.now()
            )
    
    # Threshold checking methods
    
    async def _check_system_health_thresholds(self, metrics: Dict[str, Any]):
        """Check system health metrics against thresholds"""
        
        alerts = []
        
        # CPU usage alerts
        if metrics['cpu_usage'] > self.health_thresholds['cpu_usage_critical']:
            alerts.append({
                'level': 'CRITICAL',
                'metric': 'cpu_usage',
                'value': metrics['cpu_usage'],
                'threshold': self.health_thresholds['cpu_usage_critical'],
                'educational_impact': 'learning_performance_degraded'
            })
        elif metrics['cpu_usage'] > self.health_thresholds['cpu_usage_warning']:
            alerts.append({
                'level': 'WARNING',
                'metric': 'cpu_usage',
                'value': metrics['cpu_usage'],
                'threshold': self.health_thresholds['cpu_usage_warning']
            })
        
        # Memory usage alerts
        if metrics['memory_usage'] > self.health_thresholds['memory_usage_critical']:
            alerts.append({
                'level': 'CRITICAL',
                'metric': 'memory_usage',
                'value': metrics['memory_usage'],
                'threshold': self.health_thresholds['memory_usage_critical'],
                'educational_impact': 'spatial_precision_at_risk'
            })
        
        # Send alerts if any
        for alert in alerts:
            await self._send_alert(alert)
    
    async def _check_educational_performance_thresholds(self, metrics: Dict[str, Any]):
        """Check educational performance metrics against targets"""
        
        alerts = []
        
        # Learning model response time
        if metrics['learning_model_avg_response_ms'] > self.performance_targets['learning_model_response_ms']:
            alerts.append({
                'level': 'WARNING',
                'metric': 'learning_model_response_time',
                'value': metrics['learning_model_avg_response_ms'],
                'target': self.performance_targets['learning_model_response_ms'],
                'educational_impact': 'adaptive_learning_delayed'
            })
        
        # Spatial precision accuracy
        if metrics['spatial_precision_accuracy'] < self.performance_targets['spatial_precision_tolerance']:
            alerts.append({
                'level': 'CRITICAL',
                'metric': 'spatial_precision_accuracy',
                'value': metrics['spatial_precision_accuracy'],
                'target': self.performance_targets['spatial_precision_tolerance'],
                'educational_impact': 'vr_learning_precision_compromised'
            })
        
        for alert in alerts:
            await self._send_alert(alert)
    
    async def _check_vr_performance_thresholds(self, metrics: Dict[str, Any]):
        """Check VR performance metrics against Quest 3 targets"""
        
        alerts = []
        
        # FPS monitoring
        if metrics['average_fps'] < self.performance_targets['vr_fps_target']:
            alerts.append({
                'level': 'CRITICAL',
                'metric': 'vr_fps',
                'value': metrics['average_fps'],
                'target': self.performance_targets['vr_fps_target'],
                'educational_impact': 'vr_comfort_compromised',
                'vr_impact': 'motion_sickness_risk'
            })
        
        # VR comfort score
        if metrics['vr_comfort_score'] < 0.8:
            alerts.append({
                'level': 'WARNING',
                'metric': 'vr_comfort_score',
                'value': metrics['vr_comfort_score'],
                'target': 0.9,
                'educational_impact': 'learning_engagement_at_risk'
            })
        
        for alert in alerts:
            await self._send_alert(alert)
    
    async def _send_alert(self, alert: Dict[str, Any]):
        """Send alert to configured alert handlers"""
        
        logger.warning(
            f"Educational monitoring alert",
            extra={
                'alert_level': alert['level'],
                'metric': alert['metric'],
                'value': alert.get('value'),
                'threshold_or_target': alert.get('threshold', alert.get('target')),
                'educational_impact': alert.get('educational_impact', 'unknown')
            }
        )
        
        # In production, would send to alerting systems (PagerDuty, Slack, etc.)
        for handler in self.alert_handlers:
            try:
                await handler(alert)
            except Exception as e:
                logger.error(f"Alert handler failed: {e}")
    
    # Metric collection methods (simulated - would be real in production)
    
    async def _get_active_learning_sessions_count(self) -> int:
        """Get count of active learning sessions"""
        # Simulate active sessions count
        return 25
    
    async def _get_learning_model_response_time(self) -> float:
        """Get average learning model response time"""
        return 85.0  # ms
    
    async def _get_assessment_processing_time(self) -> float:
        """Get average assessment processing time"""
        return 150.0  # ms
    
    async def _get_spatial_precision_accuracy(self) -> float:
        """Get spatial precision accuracy"""
        return 0.0001  # 0.1mm
    
    async def _get_engagement_tracking_latency(self) -> float:
        """Get engagement tracking latency"""
        return 45.0  # ms
    
    async def _get_learning_progression_rate(self) -> float:
        """Get learning progression rate"""
        return 0.75  # progression score
    
    async def _get_vr_fps_metrics(self) -> float:
        """Get VR FPS metrics"""
        return 74.0  # fps
    
    async def _get_vr_frame_time(self) -> float:
        """Get VR frame time"""
        return 13.5  # ms
    
    async def _get_spatial_tracking_latency(self) -> float:
        """Get spatial tracking latency"""
        return 20.0  # ms
    
    async def _get_vr_comfort_score(self) -> float:
        """Get VR comfort score"""
        return 0.85
    
    async def _get_motion_sickness_incidents(self) -> int:
        """Get motion sickness incidents count"""
        return 0
    
    async def _get_vr_session_duration(self) -> float:
        """Get average VR session duration"""
        return 45.0  # minutes
    
    # Helper methods for impact assessment
    
    def _assess_service_educational_impact(self, service_name: str, healthy: bool) -> str:
        """Assess educational impact of service health"""
        
        if not healthy:
            impact_map = {
                'learner-service': 'personalization_lost',
                'assessment-service': 'assessment_unavailable',
                'engagement-service': 'adaptation_disabled',
                'spatial-service': 'vr_precision_compromised',
                'blender-service': 'content_creation_disabled'
            }
            return impact_map.get(service_name, 'educational_continuity_at_risk')
        
        return 'no_impact'
    
    def _assess_service_vr_impact(self, service_name: str, healthy: bool) -> str:
        """Assess VR performance impact of service health"""
        
        if not healthy:
            vr_critical_services = ['spatial-service', 'engagement-service', 'blender-service']
            if service_name in vr_critical_services:
                return 'vr_experience_degraded'
        
        return 'no_vr_impact'
    
    def _assess_service_ferpa_impact(self, service_name: str, healthy: bool) -> str:
        """Assess FERPA compliance impact of service health"""
        
        if not healthy:
            ferpa_critical_services = ['learner-service', 'assessment-service']
            if service_name in ferpa_critical_services:
                return 'compliance_at_risk'
        
        return 'compliance_maintained'
    
    def get_monitoring_status(self) -> Dict[str, Any]:
        """Get comprehensive monitoring status"""
        
        return {
            'monitoring_active': self.monitoring_active,
            'last_health_check': self.last_health_check.get('timestamp') if self.last_health_check else None,
            'system_metrics_count': len(self.system_metrics_history),
            'educational_metrics_count': len(self.educational_metrics_history),
            'performance_targets': self.performance_targets,
            'health_thresholds': self.health_thresholds,
            'alert_handlers_count': len(self.alert_handlers)
        }
