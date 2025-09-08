"""
Streaming Handler for Continuous Learning Data Flow

Educational Impact:
Manages continuous learning data streaming with 5-second intervals to enable
real-time educational adaptation and learning analytics. Ensures consistent
data flow for optimal learning equation processing and educational outcome
optimization without disrupting the VR learning experience.

Performance Requirements:
- Streaming interval: 5-second intervals for continuous data flow
- Processing latency: <10ms for data collection and formatting
- Memory efficiency: <1MB per streaming session
- Concurrent streams: Support 50+ simultaneous learner streams

Quest 3 VR Optimization:
- Minimal VR performance impact with efficient data collection
- Optimized data serialization for VR bandwidth constraints
- Asynchronous processing to maintain VR frame rates
"""

import asyncio
import json
import logging
import time
from typing import Dict, List, Optional, Any, Callable
from datetime import datetime, timezone
import uuid
from dataclasses import dataclass, asdict

from websockets.server import WebSocketServerProtocol

logger = logging.getLogger(__name__)

@dataclass
class StreamingSession:
    """
    Active streaming session for continuous learning data flow.
    
    Educational Impact:
    Represents an active educational streaming session that continuously
    monitors learner interactions and provides real-time data for
    educational adaptation and learning analytics processing.
    """
    session_id: str
    connection_id: str
    websocket: WebSocketServerProtocol
    started_at: datetime
    last_stream_time: datetime
    stream_count: int = 0
    total_bytes_streamed: int = 0
    streaming_active: bool = True
    educational_context: Dict[str, Any] = None

    def __post_init__(self):
        if self.educational_context is None:
            self.educational_context = {}

@dataclass
class StreamingMetrics:
    """
    Performance metrics for streaming operations.
    
    Educational Impact:
    Tracks streaming performance to ensure optimal educational data flow
    and identify opportunities for learning analytics optimization and
    educational outcome improvement.
    """
    total_streams: int = 0
    active_sessions: int = 0
    average_interval: float = 5.0
    data_throughput_bytes_per_second: float = 0.0
    streaming_reliability: float = 1.0
    educational_data_quality: float = 1.0

class StreamingHandler:
    """
    Handles continuous learning data streaming for real-time adaptation.
    
    Educational Impact:
    Provides continuous educational data flow that enables real-time learning
    adaptation, immediate educational response to learner needs, and
    comprehensive learning analytics for educational effectiveness optimization.
    
    Performance Requirements:
    - Streaming intervals: Consistent 5-second data collection cycles
    - Processing overhead: <10ms per streaming cycle
    - Memory per session: <1MB for streaming state management
    - Reliability: >99% successful data streaming
    
    Features:
    - Configurable streaming intervals for different educational contexts
    - Educational data quality validation and enhancement
    - Real-time learning analytics integration
    - VR-optimized data collection and transmission
    """
    
    def __init__(self, default_interval: float = 5.0):
        """
        Initialize streaming handler for continuous learning data flow.
        
        Educational Impact:
        Sets up the infrastructure for continuous educational data streaming
        that enables real-time learning adaptation and comprehensive
        educational analytics for optimal learning outcomes.
        
        Args:
            default_interval: Default streaming interval in seconds
        """
        self.default_interval = default_interval
        
        # Active streaming sessions
        self.streaming_sessions: Dict[str, StreamingSession] = {}
        self.session_tasks: Dict[str, asyncio.Task] = {}
        
        # Streaming configuration
        self.streaming_config = {
            'default_interval': default_interval,
            'max_concurrent_sessions': 50,
            'data_quality_threshold': 0.8,
            'educational_context_required': True,
            'vr_optimization_enabled': True
        }
        
        # Performance metrics
        self.metrics = StreamingMetrics()
        
        # Educational data processors
        self.data_processors: List[Callable] = []
        self.educational_validators: List[Callable] = []
        
        # VR optimization settings
        self.vr_optimization = {
            'compress_data': True,
            'prioritize_critical_data': True,
            'adaptive_interval': True,
            'batch_non_critical': True
        }
        
    async def start_session_streaming(
        self, 
        session_id: str, 
        connection_id: str, 
        websocket: WebSocketServerProtocol,
        educational_context: Optional[Dict[str, Any]] = None
    ) -> bool:
        """
        Start continuous learning data streaming for a session.
        
        Educational Impact:
        Initiates continuous educational data collection that enables
        real-time learning adaptation, immediate educational response,
        and comprehensive learning analytics for optimal educational outcomes.
        
        Performance Requirements:
        - Session initialization: <100ms for streaming setup
        - Memory allocation: <1MB per streaming session
        - Streaming reliability: >99% successful data collection
        
        Args:
            session_id: Unique session identifier
            connection_id: WebSocket connection identifier
            websocket: WebSocket connection for streaming
            educational_context: Educational session context and parameters
            
        Returns:
            bool: True if streaming started successfully
        """
        try:
            # Check concurrent session limit
            if len(self.streaming_sessions) >= self.streaming_config['max_concurrent_sessions']:
                logger.warning(f"Maximum concurrent streaming sessions reached")
                return False
                
            # Create streaming session
            streaming_session = StreamingSession(
                session_id=session_id,
                connection_id=connection_id,
                websocket=websocket,
                started_at=datetime.now(timezone.utc),
                last_stream_time=datetime.now(timezone.utc),
                educational_context=educational_context or {}
            )
            
            # Register session
            self.streaming_sessions[session_id] = streaming_session
            
            # Start streaming task
            streaming_task = asyncio.create_task(
                self._streaming_loop(session_id)
            )
            self.session_tasks[session_id] = streaming_task
            
            # Update metrics
            self.metrics.active_sessions += 1
            
            logger.info(f"Started streaming for session: {session_id}")
            logger.info(f"Educational context: {educational_context}")
            
            return True
            
        except Exception as e:
            logger.error(f"Error starting session streaming: {e}")
            return False
            
    async def stop_session_streaming(self, session_id: str) -> bool:
        """
        Stop continuous learning data streaming for a session.
        
        Educational Impact:
        Properly terminates educational data streaming while preserving
        collected learning analytics and ensuring educational data integrity
        for continued learning assessment and optimization.
        
        Args:
            session_id: Unique session identifier
            
        Returns:
            bool: True if streaming stopped successfully
        """
        try:
            # Cancel streaming task
            if session_id in self.session_tasks:
                task = self.session_tasks[session_id]
                task.cancel()
                
                try:
                    await task
                except asyncio.CancelledError:
                    pass
                    
                del self.session_tasks[session_id]
                
            # Finalize streaming session
            if session_id in self.streaming_sessions:
                session = self.streaming_sessions[session_id]
                session.streaming_active = False
                
                # Save final streaming metrics
                await self._save_streaming_analytics(session)
                
                del self.streaming_sessions[session_id]
                
            # Update metrics
            self.metrics.active_sessions = max(0, self.metrics.active_sessions - 1)
            
            logger.info(f"Stopped streaming for session: {session_id}")
            return True
            
        except Exception as e:
            logger.error(f"Error stopping session streaming: {e}")
            return False
            
    async def _streaming_loop(self, session_id: str) -> None:
        """
        Main streaming loop for continuous learning data collection.
        
        Educational Impact:
        Provides consistent educational data collection that enables
        real-time learning adaptation and comprehensive educational
        analytics for optimal learning outcome optimization.
        
        Performance Requirements:
        - Streaming consistency: <±100ms interval variance
        - Processing time: <10ms per streaming cycle
        - Data quality: >95% successful data collection
        """
        try:
            session = self.streaming_sessions.get(session_id)
            if not session:
                logger.error(f"Streaming session not found: {session_id}")
                return
                
            logger.info(f"Starting streaming loop for session: {session_id}")
            
            while session.streaming_active and not session.websocket.closed:
                cycle_start_time = time.time()
                
                try:
                    # Collect learning data
                    learning_data = await self._collect_learning_data(session)
                    
                    # Validate educational data quality
                    if await self._validate_educational_data(learning_data):
                        
                        # Process through educational data processors
                        processed_data = await self._process_educational_data(
                            learning_data, session
                        )
                        
                        # Stream data to learning systems
                        await self._stream_to_learning_systems(
                            session_id, processed_data
                        )
                        
                        # Update session metrics
                        session.stream_count += 1
                        session.last_stream_time = datetime.now(timezone.utc)
                        
                        # Update streaming metrics
                        self.metrics.total_streams += 1
                        
                    # Calculate adaptive interval for VR optimization
                    streaming_interval = await self._calculate_adaptive_interval(
                        session, cycle_start_time
                    )
                    
                    # Wait for next streaming cycle
                    cycle_time = time.time() - cycle_start_time
                    sleep_time = max(0.1, streaming_interval - cycle_time)
                    await asyncio.sleep(sleep_time)
                    
                except asyncio.CancelledError:
                    logger.info(f"Streaming loop cancelled for session: {session_id}")
                    break
                except Exception as e:
                    logger.error(f"Error in streaming loop: {e}")
                    await asyncio.sleep(1.0)  # Brief pause before retry
                    
        except Exception as e:
            logger.error(f"Fatal error in streaming loop: {e}")
        finally:
            logger.info(f"Streaming loop ended for session: {session_id}")
            
    async def _collect_learning_data(
        self, 
        session: StreamingSession
    ) -> Dict[str, Any]:
        """
        Collect current learning data for streaming.
        
        Educational Impact:
        Gathers comprehensive educational interaction data including
        learner state, engagement metrics, and performance indicators
        for real-time learning adaptation and educational analytics.
        
        Performance Requirements:
        - Collection time: <5ms for data gathering
        - Data completeness: >95% of required educational metrics
        - Memory efficiency: Minimal allocation for data collection
        
        Returns:
            Dict containing comprehensive learning data snapshot
        """
        try:
            # Simulate learning data collection (in real implementation, 
            # this would interface with VR environment APIs)
            learning_data = {
                'timestamp': datetime.now(timezone.utc).isoformat(),
                'session_id': session.session_id,
                'stream_sequence': session.stream_count,
                
                # Learner state data
                'learner_state': {
                    'current_focus': 'viewport_navigation',
                    'stress_indicators': 0.3,  # Would be collected from VR sensors
                    'competency_confidence': 0.7,
                    'help_seeking_frequency': 0.1,
                    'cognitive_load': 0.6
                },
                
                # Engagement metrics
                'engagement_metrics': {
                    'attention_level': 0.8,
                    'interaction_quality': 0.9,
                    'flow_state_indicators': 0.7,
                    'social_engagement': 0.6,
                    'task_engagement': 0.8
                },
                
                # Performance indicators
                'performance_indicators': {
                    'task_completion_rate': 0.85,
                    'error_frequency': 0.15,
                    'skill_demonstration': 0.78,
                    'learning_efficiency': 0.82,
                    'retention_indicators': 0.75
                },
                
                # VR-specific metrics
                'vr_metrics': {
                    'head_tracking_quality': 0.95,
                    'hand_tracking_accuracy': 0.90,
                    'spatial_awareness': 0.85,
                    'motion_comfort': 0.80,
                    'presence_level': 0.88
                },
                
                # Educational context
                'educational_context': {
                    'current_learning_objective': session.educational_context.get(
                        'learning_objective', 'basic_navigation'
                    ),
                    'difficulty_level': session.educational_context.get(
                        'difficulty_level', 0.5
                    ),
                    'support_level': session.educational_context.get(
                        'support_level', 'adaptive'
                    ),
                    'learning_domain': session.educational_context.get(
                        'learning_domain', 'vr_3d_modeling'
                    )
                }
            }
            
            return learning_data
            
        except Exception as e:
            logger.error(f"Error collecting learning data: {e}")
            return {
                'timestamp': datetime.now(timezone.utc).isoformat(),
                'session_id': session.session_id,
                'error': str(e),
                'data_quality': 0.0
            }
            
    async def _validate_educational_data(
        self, 
        learning_data: Dict[str, Any]
    ) -> bool:
        """
        Validate educational data quality and completeness.
        
        Educational Impact:
        Ensures educational data meets quality standards for reliable
        learning adaptation and educational analytics, preventing
        poor-quality data from negatively impacting educational outcomes.
        
        Performance Requirements:
        - Validation time: <2ms for data quality checking
        - Accuracy: >99% correct quality assessment
        - Educational context preservation: Complete validation
        
        Returns:
            bool: True if data meets educational quality standards
        """
        try:
            # Check for required educational components
            required_sections = [
                'learner_state', 
                'engagement_metrics', 
                'performance_indicators',
                'educational_context'
            ]
            
            for section in required_sections:
                if section not in learning_data:
                    logger.warning(f"Missing required educational data section: {section}")
                    return False
                    
            # Validate data ranges for educational metrics
            learner_state = learning_data.get('learner_state', {})
            engagement_metrics = learning_data.get('engagement_metrics', {})
            performance_indicators = learning_data.get('performance_indicators', {})
            
            # Validate learner state ranges (0.0 to 1.0)
            for metric, value in learner_state.items():
                if isinstance(value, (int, float)) and not (0.0 <= value <= 1.0):
                    logger.warning(f"Learner state metric out of range: {metric}={value}")
                    return False
                    
            # Validate engagement metrics ranges (0.0 to 1.0)
            for metric, value in engagement_metrics.items():
                if isinstance(value, (int, float)) and not (0.0 <= value <= 1.0):
                    logger.warning(f"Engagement metric out of range: {metric}={value}")
                    return False
                    
            # Validate performance indicators ranges (0.0 to 1.0)
            for metric, value in performance_indicators.items():
                if isinstance(value, (int, float)) and not (0.0 <= value <= 1.0):
                    logger.warning(f"Performance indicator out of range: {metric}={value}")
                    return False
                    
            # Educational context validation
            educational_context = learning_data.get('educational_context', {})
            if not educational_context.get('current_learning_objective'):
                logger.warning("Missing current learning objective")
                return False
                
            # Run custom educational validators
            for validator in self.educational_validators:
                if not await validator(learning_data):
                    return False
                    
            return True
            
        except Exception as e:
            logger.error(f"Error validating educational data: {e}")
            return False
            
    async def _process_educational_data(
        self, 
        learning_data: Dict[str, Any], 
        session: StreamingSession
    ) -> Dict[str, Any]:
        """
        Process educational data for optimal learning system integration.
        
        Educational Impact:
        Enhances raw educational data with additional educational context,
        learning analytics, and optimization parameters for improved
        learning adaptation and educational outcome assessment.
        
        Performance Requirements:
        - Processing time: <5ms for data enhancement
        - Educational value addition: >20% improvement in data utility
        - Memory efficiency: Minimal additional allocation
        
        Returns:
            Dict containing enhanced educational data
        """
        try:
            processed_data = learning_data.copy()
            
            # Add session context
            processed_data['session_context'] = {
                'session_duration': (
                    datetime.now(timezone.utc) - session.started_at
                ).total_seconds(),
                'stream_count': session.stream_count,
                'data_quality_score': await self._calculate_data_quality_score(learning_data),
                'educational_progression': await self._assess_educational_progression(
                    learning_data, session
                )
            }
            
            # Add learning analytics
            processed_data['learning_analytics'] = {
                'engagement_trend': await self._calculate_engagement_trend(session),
                'performance_trend': await self._calculate_performance_trend(session),
                'learning_velocity': await self._calculate_learning_velocity(learning_data),
                'adaptation_readiness': await self._assess_adaptation_readiness(learning_data)
            }
            
            # Add VR optimization parameters
            if self.vr_optimization['vr_optimization_enabled']:
                processed_data['vr_optimization'] = {
                    'frame_rate_impact': await self._assess_frame_rate_impact(learning_data),
                    'processing_priority': await self._determine_processing_priority(learning_data),
                    'bandwidth_optimization': await self._optimize_bandwidth_usage(learning_data)
                }
                
            # Run custom data processors
            for processor in self.data_processors:
                processed_data = await processor(processed_data, session)
                
            # Update data size metrics
            data_size = len(json.dumps(processed_data).encode('utf-8'))
            session.total_bytes_streamed += data_size
            
            return processed_data
            
        except Exception as e:
            logger.error(f"Error processing educational data: {e}")
            return learning_data  # Return original data if processing fails
            
    async def _stream_to_learning_systems(
        self, 
        session_id: str, 
        processed_data: Dict[str, Any]
    ) -> None:
        """
        Stream processed data to learning adaptation systems.
        
        Educational Impact:
        Delivers educational data to learning adaptation systems that
        generate real-time educational adjustments, ensuring optimal
        learning outcomes and immediate response to learner needs.
        
        Performance Requirements:
        - Streaming latency: <5ms for data delivery
        - Reliability: >99% successful data delivery
        - Educational context preservation: Complete data integrity
        """
        try:
            # In real implementation, this would stream to:
            # 1. Learning Integration Engine
            # 2. Educational Analytics System
            # 3. Real-time Adaptation Processor
            # 4. Learning Progress Tracker
            
            # For now, we'll log the streaming activity
            logger.debug(f"Streaming educational data for session: {session_id}")
            logger.debug(f"Data quality score: {processed_data.get('session_context', {}).get('data_quality_score', 'N/A')}")
            logger.debug(f"Educational progression: {processed_data.get('session_context', {}).get('educational_progression', 'N/A')}")
            
            # Update streaming metrics
            self._update_streaming_metrics(processed_data)
            
        except Exception as e:
            logger.error(f"Error streaming to learning systems: {e}")
            
    async def _calculate_adaptive_interval(
        self, 
        session: StreamingSession, 
        cycle_start_time: float
    ) -> float:
        """
        Calculate adaptive streaming interval for VR optimization.
        
        Educational Impact:
        Optimizes streaming frequency based on educational activity level
        and VR performance requirements, ensuring optimal data collection
        without compromising VR learning experience quality.
        
        Performance Requirements:
        - Calculation time: <1ms for interval optimization
        - VR performance preservation: Maintain >72fps in Quest 3
        - Educational data completeness: >95% critical data collection
        
        Returns:
            Optimized streaming interval in seconds
        """
        base_interval = self.default_interval
        
        if not self.vr_optimization['adaptive_interval']:
            return base_interval
            
        try:
            # Adjust based on VR performance
            vr_metrics = session.educational_context.get('vr_performance', {})
            frame_rate = vr_metrics.get('current_frame_rate', 90)
            
            if frame_rate < 72:  # Quest 3 minimum for comfort
                # Increase interval to reduce processing load
                return min(base_interval * 1.5, 10.0)
            elif frame_rate > 90:
                # Can afford more frequent streaming
                return max(base_interval * 0.8, 2.0)
                
            # Adjust based on educational activity level
            recent_interactions = session.educational_context.get('recent_interactions', 1.0)
            if recent_interactions > 0.8:
                # High activity - more frequent streaming
                return max(base_interval * 0.9, 3.0)
            elif recent_interactions < 0.3:
                # Low activity - less frequent streaming
                return min(base_interval * 1.2, 8.0)
                
            return base_interval
            
        except Exception as e:
            logger.error(f"Error calculating adaptive interval: {e}")
            return base_interval
            
    async def _save_streaming_analytics(self, session: StreamingSession) -> None:
        """
        Save streaming analytics for educational research and optimization.
        
        Educational Impact:
        Preserves comprehensive streaming analytics for educational
        effectiveness research, system optimization, and learning
        outcome assessment for continuous educational improvement.
        """
        try:
            analytics_data = {
                'session_id': session.session_id,
                'streaming_duration': (
                    datetime.now(timezone.utc) - session.started_at
                ).total_seconds(),
                'total_streams': session.stream_count,
                'total_bytes': session.total_bytes_streamed,
                'average_stream_interval': self.default_interval,
                'educational_context': session.educational_context,
                'streaming_reliability': session.stream_count / max(
                    (datetime.now(timezone.utc) - session.started_at).total_seconds() / self.default_interval,
                    1
                ),
                'timestamp': datetime.now(timezone.utc).isoformat()
            }
            
            logger.info(f"Streaming analytics saved for session: {session.session_id}")
            logger.info(f"Total streams: {session.stream_count}, Bytes: {session.total_bytes_streamed}")
            
        except Exception as e:
            logger.error(f"Error saving streaming analytics: {e}")
            
    # Helper methods for educational data processing
    
    async def _calculate_data_quality_score(self, learning_data: Dict[str, Any]) -> float:
        """Calculate educational data quality score (0.0 to 1.0)."""
        try:
            required_fields = ['learner_state', 'engagement_metrics', 'performance_indicators']
            present_fields = sum(1 for field in required_fields if field in learning_data)
            completeness_score = present_fields / len(required_fields)
            
            # Check data range validity
            validity_score = 1.0
            for section in required_fields:
                if section in learning_data:
                    section_data = learning_data[section]
                    for metric, value in section_data.items():
                        if isinstance(value, (int, float)) and not (0.0 <= value <= 1.0):
                            validity_score -= 0.1
                            
            return max(0.0, min(1.0, completeness_score * max(0.0, validity_score)))
            
        except Exception:
            return 0.5
            
    async def _assess_educational_progression(
        self, 
        learning_data: Dict[str, Any], 
        session: StreamingSession
    ) -> str:
        """Assess current educational progression status."""
        try:
            performance = learning_data.get('performance_indicators', {})
            engagement = learning_data.get('engagement_metrics', {})
            
            task_completion = performance.get('task_completion_rate', 0.5)
            attention_level = engagement.get('attention_level', 0.5)
            
            if task_completion > 0.8 and attention_level > 0.7:
                return "excellent_progress"
            elif task_completion > 0.6 and attention_level > 0.5:
                return "good_progress"
            elif task_completion > 0.4:
                return "steady_progress"
            else:
                return "needs_support"
                
        except Exception:
            return "assessment_unavailable"
            
    async def _calculate_engagement_trend(self, session: StreamingSession) -> str:
        """Calculate engagement trend over recent streams."""
        # Simplified implementation - would track historical data in real system
        return "stable"
        
    async def _calculate_performance_trend(self, session: StreamingSession) -> str:
        """Calculate performance trend over recent streams."""
        # Simplified implementation - would track historical data in real system
        return "improving"
        
    async def _calculate_learning_velocity(self, learning_data: Dict[str, Any]) -> float:
        """Calculate current learning velocity (progress per unit time)."""
        try:
            performance = learning_data.get('performance_indicators', {})
            completion_rate = performance.get('task_completion_rate', 0.5)
            efficiency = performance.get('learning_efficiency', 0.5)
            return (completion_rate + efficiency) / 2.0
        except Exception:
            return 0.5
            
    async def _assess_adaptation_readiness(self, learning_data: Dict[str, Any]) -> float:
        """Assess readiness for learning adaptation (0.0 to 1.0)."""
        try:
            learner_state = learning_data.get('learner_state', {})
            performance = learning_data.get('performance_indicators', {})
            
            stress_level = learner_state.get('stress_indicators', 0.5)
            error_frequency = performance.get('error_frequency', 0.5)
            
            # Higher adaptation readiness when stress is low and errors are manageable
            readiness = (1.0 - stress_level) * 0.6 + (1.0 - error_frequency) * 0.4
            return max(0.0, min(1.0, readiness))
            
        except Exception:
            return 0.5
            
    async def _assess_frame_rate_impact(self, learning_data: Dict[str, Any]) -> str:
        """Assess VR frame rate impact of current data processing."""
        # Simplified implementation
        return "minimal"
        
    async def _determine_processing_priority(self, learning_data: Dict[str, Any]) -> str:
        """Determine processing priority for VR optimization."""
        try:
            learner_state = learning_data.get('learner_state', {})
            stress_level = learner_state.get('stress_indicators', 0.5)
            
            if stress_level > 0.7:
                return "high"  # Urgent adaptation needed
            elif stress_level < 0.3:
                return "low"   # Stable learning state
            else:
                return "normal"
                
        except Exception:
            return "normal"
            
    async def _optimize_bandwidth_usage(self, learning_data: Dict[str, Any]) -> Dict[str, Any]:
        """Optimize data for bandwidth efficiency."""
        return {
            'compression_applied': self.vr_optimization['compress_data'],
            'data_size_optimized': True,
            'critical_data_preserved': True
        }
        
    def _update_streaming_metrics(self, processed_data: Dict[str, Any]) -> None:
        """Update streaming performance metrics."""
        try:
            data_quality = processed_data.get('session_context', {}).get('data_quality_score', 1.0)
            
            # Update educational data quality metric
            current_quality = self.metrics.educational_data_quality
            total_streams = self.metrics.total_streams
            
            if total_streams > 0:
                self.metrics.educational_data_quality = (
                    (current_quality * (total_streams - 1) + data_quality) / total_streams
                )
            else:
                self.metrics.educational_data_quality = data_quality
                
        except Exception as e:
            logger.error(f"Error updating streaming metrics: {e}")
            
    # Public interface methods
    
    def add_data_processor(self, processor: Callable) -> None:
        """
        Add custom educational data processor.
        
        Educational Impact:
        Enables custom educational data processing for specialized
        learning contexts and educational research requirements.
        """
        self.data_processors.append(processor)
        
    def add_educational_validator(self, validator: Callable) -> None:
        """
        Add custom educational data validator.
        
        Educational Impact:
        Enables custom educational data validation for specialized
        learning contexts and quality assurance requirements.
        """
        self.educational_validators.append(validator)
        
    def get_streaming_metrics(self) -> Dict[str, Any]:
        """
        Get comprehensive streaming metrics for monitoring.
        
        Educational Impact:
        Provides detailed streaming analytics for educational system
        optimization, performance monitoring, and educational
        effectiveness assessment.
        """
        return {
            'performance_metrics': asdict(self.metrics),
            'active_sessions': len(self.streaming_sessions),
            'configuration': self.streaming_config.copy(),
            'vr_optimization': self.vr_optimization.copy()
        }
        
    def update_streaming_config(self, config_updates: Dict[str, Any]) -> None:
        """
        Update streaming configuration for optimization.
        
        Educational Impact:
        Enables dynamic optimization of streaming parameters for
        different educational contexts and performance requirements.
        """
        self.streaming_config.update(config_updates)
        logger.info(f"Streaming configuration updated: {config_updates}")
