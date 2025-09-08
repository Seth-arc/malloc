"""
Real-time Learning Processing Pipeline
Phase 3: Continuous Learning Adaptation System

Educational Impact:
Enables continuous, real-time adaptation of learning experiences based on
learner interactions, maintaining optimal learning progression without
interruption to the VR learning environment.

Performance Requirements:
- Quest 3 VR: Maintain >72fps during continuous processing
- Pipeline latency: <25ms end-to-end processing
- Memory usage: <75MB for pipeline operations
- Processing capacity: 50+ concurrent learners
"""

import asyncio
import logging
import json
import time
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Callable, Set
from dataclasses import dataclass, field
from enum import Enum
import weakref
from concurrent.futures import ThreadPoolExecutor
import queue

# Import learning components
from .integration_engine import (
    LearningIntegrationEngine, 
    LearningModelInputs, 
    IntegrationResult
)
from .learner_model import LearnerModelProcessor
from .knowledge_model import KnowledgeModelProcessor
from .engagement_model import EngagementModelProcessor
from .assessment_model import AssessmentModelProcessor

class PipelineEventType(Enum):
    """Types of real-time learning events processed by the pipeline"""
    LEARNER_INTERACTION = "learner_interaction"
    KNOWLEDGE_UPDATE = "knowledge_update" 
    ENGAGEMENT_CHANGE = "engagement_change"
    ASSESSMENT_COMPLETION = "assessment_completion"
    LEARNING_ADAPTATION = "learning_adaptation"
    SYSTEM_OPTIMIZATION = "system_optimization"

@dataclass
class LearningEvent:
    """
    Structure for real-time learning events in the pipeline
    
    Educational Impact:
    Standardizes learning event data for consistent processing
    and educational decision-making across the pipeline.
    """
    event_id: str
    event_type: PipelineEventType
    learner_id: str
    timestamp: str
    data: Dict[str, Any]
    priority: int = 5  # 1=highest, 10=lowest
    processing_deadline: Optional[str] = None
    retry_count: int = 0
    max_retries: int = 3
    
    def __post_init__(self):
        if self.processing_deadline is None:
            # Set deadline to 25ms from creation for real-time requirement
            deadline = datetime.now() + timedelta(milliseconds=25)
            self.processing_deadline = deadline.isoformat()

@dataclass
class PipelineMetrics:
    """Performance and educational metrics for the pipeline"""
    events_processed: int = 0
    total_processing_time_ms: float = 0.0
    average_latency_ms: float = 0.0
    missed_deadlines: int = 0
    successful_adaptations: int = 0
    failed_adaptations: int = 0
    active_learners: int = 0
    queue_depth: int = 0
    last_updated: str = field(default_factory=lambda: datetime.now().isoformat())

class LearningEventProcessor:
    """
    Individual event processor for specific learning event types
    
    Educational Impact:
    Specialized processing for different learning events ensures
    appropriate educational responses and optimal learning outcomes.
    """
    
    def __init__(self, event_type: PipelineEventType):
        self.event_type = event_type
        self.logger = logging.getLogger(f"{__name__}.{event_type.value}")
    
    async def process_event(
        self, 
        event: LearningEvent, 
        integration_engine: LearningIntegrationEngine
    ) -> Dict[str, Any]:
        """
        Process a specific learning event type
        
        Args:
            event: Learning event to process
            integration_engine: Integration engine for computation
            
        Returns:
            Processing result with educational recommendations
        """
        try:
            if self.event_type == PipelineEventType.LEARNER_INTERACTION:
                return await self._process_learner_interaction(event, integration_engine)
            elif self.event_type == PipelineEventType.KNOWLEDGE_UPDATE:
                return await self._process_knowledge_update(event, integration_engine)
            elif self.event_type == PipelineEventType.ENGAGEMENT_CHANGE:
                return await self._process_engagement_change(event, integration_engine)
            elif self.event_type == PipelineEventType.ASSESSMENT_COMPLETION:
                return await self._process_assessment_completion(event, integration_engine)
            elif self.event_type == PipelineEventType.LEARNING_ADAPTATION:
                return await self._process_learning_adaptation(event, integration_engine)
            else:
                return await self._process_generic_event(event, integration_engine)
                
        except Exception as e:
            self.logger.error(f"Event processing failed for {event.event_id}: {e}")
            return {
                "status": "error",
                "event_id": event.event_id,
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }
    
    async def _process_learner_interaction(
        self, 
        event: LearningEvent, 
        integration_engine: LearningIntegrationEngine
    ) -> Dict[str, Any]:
        """Process learner interaction events (VR gestures, gaze, movement)"""
        try:
            # Extract interaction data
            interaction_data = event.data.get("interaction", {})
            current_learning_event = event.data.get("learning_event", "practice")
            
            # Create minimal model inputs for quick processing
            model_inputs = LearningModelInputs(
                learner_model_data=event.data.get("learner_data", {}),
                knowledge_model_data=event.data.get("knowledge_data", {}),
                engagement_model_data=interaction_data,
                assessment_model_data=event.data.get("assessment_data", {}),
                learning_event=current_learning_event
            )
            
            # Compute transition state
            result = await integration_engine.compute_transition_state(
                event.learner_id, model_inputs, current_learning_event
            )
            
            return {
                "status": "processed",
                "event_id": event.event_id,
                "learner_id": event.learner_id,
                "transition_result": {
                    "transition_state": result.transition_state,
                    "recommended_action": result.recommended_action,
                    "confidence_score": result.confidence_score
                },
                "immediate_adaptations": await self._generate_immediate_adaptations(result),
                "processing_time_ms": result.computation_time_ms,
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            self.logger.error(f"Learner interaction processing failed: {e}")
            raise
    
    async def _process_engagement_change(
        self, 
        event: LearningEvent, 
        integration_engine: LearningIntegrationEngine
    ) -> Dict[str, Any]:
        """Process engagement level changes (attention, focus, interaction quality)"""
        try:
            engagement_data = event.data.get("engagement", {})
            attention_level = engagement_data.get("attention_level", 0.5)
            
            # Quick adaptation for significant attention changes
            if attention_level < 0.3:
                # Low attention - immediate intervention needed
                return {
                    "status": "processed",
                    "event_id": event.event_id,
                    "urgent_adaptation": True,
                    "recommendations": [
                        "Reduce content complexity immediately",
                        "Introduce attention-grabbing elements",
                        "Consider break suggestion"
                    ],
                    "adaptation_priority": "high",
                    "timestamp": datetime.now().isoformat()
                }
            elif attention_level > 0.8:
                # High attention - opportunity for acceleration
                return {
                    "status": "processed",
                    "event_id": event.event_id,
                    "optimization_opportunity": True,
                    "recommendations": [
                        "Increase content complexity",
                        "Introduce advanced challenges",
                        "Accelerate learning pace"
                    ],
                    "adaptation_priority": "medium",
                    "timestamp": datetime.now().isoformat()
                }
            else:
                # Normal attention - standard processing
                return {
                    "status": "processed",
                    "event_id": event.event_id,
                    "adaptation_priority": "low",
                    "timestamp": datetime.now().isoformat()
                }
                
        except Exception as e:
            self.logger.error(f"Engagement change processing failed: {e}")
            raise
    
    async def _process_assessment_completion(
        self, 
        event: LearningEvent, 
        integration_engine: LearningIntegrationEngine
    ) -> Dict[str, Any]:
        """Process assessment completion events"""
        try:
            assessment_data = event.data.get("assessment", {})
            performance_score = assessment_data.get("performance_score", 0.5)
            
            # Determine progression recommendations
            if performance_score >= 0.85:
                progression_recommendation = "advance_to_next_level"
                adaptation_strength = "moderate"
            elif performance_score >= 0.60:
                progression_recommendation = "continue_current_level"
                adaptation_strength = "minimal"
            else:
                progression_recommendation = "provide_remediation"
                adaptation_strength = "significant"
            
            return {
                "status": "processed",
                "event_id": event.event_id,
                "learner_id": event.learner_id,
                "progression_recommendation": progression_recommendation,
                "adaptation_strength": adaptation_strength,
                "performance_score": performance_score,
                "next_learning_event": await self._determine_next_event(
                    event.data.get("current_event", "practice"), 
                    performance_score
                ),
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            self.logger.error(f"Assessment completion processing failed: {e}")
            raise
    
    async def _process_knowledge_update(
        self, 
        event: LearningEvent, 
        integration_engine: LearningIntegrationEngine
    ) -> Dict[str, Any]:
        """Process knowledge state updates"""
        try:
            knowledge_data = event.data.get("knowledge", {})
            mastery_level = knowledge_data.get("mastery_level", 0.5)
            
            return {
                "status": "processed",
                "event_id": event.event_id,
                "knowledge_adaptation": {
                    "mastery_level": mastery_level,
                    "recommended_difficulty": self._calculate_difficulty_adjustment(mastery_level),
                    "prerequisite_check": mastery_level >= 0.7
                },
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            self.logger.error(f"Knowledge update processing failed: {e}")
            raise
    
    async def _process_learning_adaptation(
        self, 
        event: LearningEvent, 
        integration_engine: LearningIntegrationEngine
    ) -> Dict[str, Any]:
        """Process learning adaptation events"""
        return {
            "status": "processed",
            "event_id": event.event_id,
            "adaptation_applied": True,
            "timestamp": datetime.now().isoformat()
        }
    
    async def _process_generic_event(
        self, 
        event: LearningEvent, 
        integration_engine: LearningIntegrationEngine
    ) -> Dict[str, Any]:
        """Process generic events"""
        return {
            "status": "processed", 
            "event_id": event.event_id,
            "event_type": event.event_type.value,
            "timestamp": datetime.now().isoformat()
        }
    
    async def _generate_immediate_adaptations(self, result: IntegrationResult) -> List[Dict[str, Any]]:
        """Generate immediate adaptations based on integration result"""
        adaptations = []
        
        if result.transition_state < 0.3:
            adaptations.append({
                "type": "difficulty_reduction",
                "strength": "significant",
                "reason": "Low transition state requires immediate support"
            })
        elif result.transition_state > 0.8:
            adaptations.append({
                "type": "challenge_increase", 
                "strength": "moderate",
                "reason": "High transition state indicates readiness for advancement"
            })
        
        if result.confidence_score < 0.5:
            adaptations.append({
                "type": "provide_hints",
                "strength": "moderate",
                "reason": "Low confidence requires additional guidance"
            })
        
        return adaptations
    
    def _calculate_difficulty_adjustment(self, mastery_level: float) -> float:
        """Calculate difficulty adjustment based on mastery level"""
        if mastery_level >= 0.8:
            return 1.2  # Increase difficulty
        elif mastery_level <= 0.4:
            return 0.7  # Decrease difficulty
        else:
            return 1.0  # Maintain current difficulty
    
    async def _determine_next_event(self, current_event: str, performance_score: float) -> str:
        """Determine next learning event based on performance"""
        event_progression = {
            "onboarding": "introduction",
            "introduction": "practice",
            "practice": "application", 
            "application": "mastery",
            "mastery": "mastery"
        }
        
        if performance_score >= 0.75:
            return event_progression.get(current_event, current_event)
        else:
            return current_event  # Stay at current level

class RealTimeLearningPipeline:
    """
    Real-time learning processing pipeline for continuous adaptation
    
    Educational Impact:
    Enables seamless, continuous learning adaptation without interrupting
    the VR learning experience, maintaining optimal educational effectiveness
    through real-time processing of learning events.
    
    Performance Requirements:
    - Quest 3 VR: Maintain >72fps during pipeline operations
    - End-to-end latency: <25ms for learning event processing
    - Memory usage: <75MB for all pipeline operations
    - Concurrent learners: Support 50+ simultaneous learners
    """
    
    def __init__(self, integration_engine: LearningIntegrationEngine):
        """
        Initialize the real-time learning pipeline
        
        Args:
            integration_engine: Learning integration engine for computations
        """
        self.integration_engine = integration_engine
        self.logger = logging.getLogger(__name__)
        
        # Event processing queues with priority support
        self.high_priority_queue = asyncio.Queue(maxsize=100)
        self.normal_priority_queue = asyncio.Queue(maxsize=500)
        self.low_priority_queue = asyncio.Queue(maxsize=1000)
        
        # Event processors for different event types
        self.event_processors = {
            event_type: LearningEventProcessor(event_type)
            for event_type in PipelineEventType
        }
        
        # Pipeline state and metrics
        self.is_running = False
        self.active_learners: Set[str] = set()
        self.metrics = PipelineMetrics()
        self.processing_tasks: List[asyncio.Task] = []
        
        # Performance monitoring
        self.latency_measurements: List[float] = []
        self.throughput_measurements: List[int] = []
        
        # Pipeline configuration
        self.max_concurrent_processors = 10
        self.queue_check_interval = 0.001  # 1ms for real-time processing
        self.metrics_update_interval = 5.0   # 5 seconds
        
        # Event callbacks for integration with MCP server
        self.adaptation_callbacks: List[Callable] = []
        
        self.logger.info("Real-time learning pipeline initialized")
    
    async def start_pipeline(self):
        """
        Start the real-time learning processing pipeline
        
        Educational Impact:
        Initiates continuous learning adaptation processing to maintain
        optimal educational experiences for all active learners.
        """
        if self.is_running:
            self.logger.warning("Pipeline already running")
            return
        
        self.is_running = True
        self.logger.info("Starting real-time learning pipeline...")
        
        try:
            # Start event processing workers
            for i in range(self.max_concurrent_processors):
                task = asyncio.create_task(self._event_processing_worker(f"worker_{i}"))
                self.processing_tasks.append(task)
            
            # Start metrics collection
            metrics_task = asyncio.create_task(self._metrics_collection_worker())
            self.processing_tasks.append(metrics_task)
            
            # Start queue monitoring
            monitor_task = asyncio.create_task(self._queue_monitoring_worker())
            self.processing_tasks.append(monitor_task)
            
            self.logger.info(f"Pipeline started with {len(self.processing_tasks)} workers")
            
        except Exception as e:
            self.logger.error(f"Pipeline startup failed: {e}")
            await self.stop_pipeline()
            raise
    
    async def stop_pipeline(self):
        """
        Stop the real-time learning processing pipeline
        
        Educational Impact:
        Gracefully shuts down learning adaptation processing while
        preserving learner state and educational continuity.
        """
        if not self.is_running:
            return
        
        self.is_running = False
        self.logger.info("Stopping real-time learning pipeline...")
        
        # Cancel all processing tasks
        for task in self.processing_tasks:
            task.cancel()
        
        # Wait for tasks to complete
        if self.processing_tasks:
            await asyncio.gather(*self.processing_tasks, return_exceptions=True)
        
        self.processing_tasks.clear()
        self.logger.info("Real-time learning pipeline stopped")
    
    async def submit_learning_event(self, event: LearningEvent) -> bool:
        """
        Submit a learning event for real-time processing
        
        Educational Impact:
        Enables immediate processing of learning events to maintain
        continuous adaptation and optimal learning experiences.
        
        Args:
            event: Learning event to process
            
        Returns:
            bool: True if event was successfully queued
        """
        if not self.is_running:
            self.logger.warning("Pipeline not running, cannot submit event")
            return False
        
        try:
            # Add learner to active set
            self.active_learners.add(event.learner_id)
            
            # Route to appropriate queue based on priority
            if event.priority <= 2:
                await self.high_priority_queue.put(event)
            elif event.priority <= 5:
                await self.normal_priority_queue.put(event)
            else:
                await self.low_priority_queue.put(event)
            
            self.logger.debug(f"Event {event.event_id} queued for processing")
            return True
            
        except asyncio.QueueFull:
            self.logger.error(f"Queue full, dropping event {event.event_id}")
            return False
        except Exception as e:
            self.logger.error(f"Failed to submit event {event.event_id}: {e}")
            return False
    
    async def _event_processing_worker(self, worker_id: str):
        """
        Event processing worker for handling learning events
        
        Educational Impact:
        Continuous processing of learning events ensures real-time
        adaptation and maintains educational effectiveness.
        
        Args:
            worker_id: Unique identifier for this worker
        """
        self.logger.info(f"Event processing worker {worker_id} started")
        
        while self.is_running:
            try:
                # Get next event from priority queues
                event = await self._get_next_event()
                
                if event is None:
                    await asyncio.sleep(self.queue_check_interval)
                    continue
                
                # Check processing deadline
                deadline = datetime.fromisoformat(event.processing_deadline)
                now = datetime.now()
                
                if now > deadline:
                    self.metrics.missed_deadlines += 1
                    self.logger.warning(f"Event {event.event_id} missed deadline by {(now - deadline).total_seconds() * 1000:.2f}ms")
                
                # Process the event
                start_time = time.perf_counter()
                
                try:
                    processor = self.event_processors[event.event_type]
                    result = await processor.process_event(event, self.integration_engine)
                    
                    # Calculate processing time
                    processing_time = (time.perf_counter() - start_time) * 1000
                    
                    # Update metrics
                    self.metrics.events_processed += 1
                    self.metrics.total_processing_time_ms += processing_time
                    self.latency_measurements.append(processing_time)
                    
                    # Trigger adaptation callbacks
                    await self._trigger_adaptation_callbacks(event, result)
                    
                    if result.get("status") == "processed":
                        self.metrics.successful_adaptations += 1
                    else:
                        self.metrics.failed_adaptations += 1
                    
                    self.logger.debug(f"Event {event.event_id} processed in {processing_time:.2f}ms")
                    
                except Exception as e:
                    self.logger.error(f"Event processing failed for {event.event_id}: {e}")
                    self.metrics.failed_adaptations += 1
                    
                    # Retry logic
                    if event.retry_count < event.max_retries:
                        event.retry_count += 1
                        await self.submit_learning_event(event)
                
            except asyncio.CancelledError:
                break
            except Exception as e:
                self.logger.error(f"Worker {worker_id} error: {e}")
                await asyncio.sleep(0.1)  # Brief pause before continuing
        
        self.logger.info(f"Event processing worker {worker_id} stopped")
    
    async def _get_next_event(self) -> Optional[LearningEvent]:
        """Get next event from priority queues"""
        try:
            # Check high priority queue first
            if not self.high_priority_queue.empty():
                return await asyncio.wait_for(
                    self.high_priority_queue.get(), timeout=0.001
                )
            
            # Check normal priority queue
            if not self.normal_priority_queue.empty():
                return await asyncio.wait_for(
                    self.normal_priority_queue.get(), timeout=0.001
                )
            
            # Check low priority queue
            if not self.low_priority_queue.empty():
                return await asyncio.wait_for(
                    self.low_priority_queue.get(), timeout=0.001
                )
            
            return None
            
        except asyncio.TimeoutError:
            return None
    
    async def _metrics_collection_worker(self):
        """Collect and update pipeline performance metrics"""
        self.logger.info("Metrics collection worker started")
        
        while self.is_running:
            try:
                await asyncio.sleep(self.metrics_update_interval)
                
                # Update metrics
                self.metrics.active_learners = len(self.active_learners)
                self.metrics.queue_depth = (
                    self.high_priority_queue.qsize() +
                    self.normal_priority_queue.qsize() +
                    self.low_priority_queue.qsize()
                )
                
                # Calculate average latency
                if self.latency_measurements:
                    self.metrics.average_latency_ms = sum(self.latency_measurements) / len(self.latency_measurements)
                    
                    # Keep only recent measurements (last 100)
                    if len(self.latency_measurements) > 100:
                        self.latency_measurements = self.latency_measurements[-100:]
                
                self.metrics.last_updated = datetime.now().isoformat()
                
                # Log performance summary
                if self.metrics.events_processed > 0:
                    success_rate = (self.metrics.successful_adaptations / self.metrics.events_processed) * 100
                    self.logger.info(
                        f"Pipeline metrics: {self.metrics.events_processed} events, "
                        f"{self.metrics.average_latency_ms:.2f}ms avg latency, "
                        f"{success_rate:.1f}% success rate, "
                        f"{self.metrics.active_learners} active learners"
                    )
                
            except asyncio.CancelledError:
                break
            except Exception as e:
                self.logger.error(f"Metrics collection error: {e}")
        
        self.logger.info("Metrics collection worker stopped")
    
    async def _queue_monitoring_worker(self):
        """Monitor queue depths and performance"""
        self.logger.info("Queue monitoring worker started")
        
        while self.is_running:
            try:
                await asyncio.sleep(1.0)  # Check every second
                
                total_queue_depth = (
                    self.high_priority_queue.qsize() +
                    self.normal_priority_queue.qsize() +
                    self.low_priority_queue.qsize()
                )
                
                # Warn about queue buildup
                if total_queue_depth > 100:
                    self.logger.warning(f"High queue depth: {total_queue_depth} events")
                
                # Check for pipeline congestion
                if self.metrics.average_latency_ms > 20.0:
                    self.logger.warning(f"High pipeline latency: {self.metrics.average_latency_ms:.2f}ms")
                
                # Performance threshold checking
                if self.metrics.average_latency_ms > 25.0:
                    self.logger.error("Pipeline exceeding 25ms latency requirement")
                
            except asyncio.CancelledError:
                break
            except Exception as e:
                self.logger.error(f"Queue monitoring error: {e}")
        
        self.logger.info("Queue monitoring worker stopped")
    
    async def _trigger_adaptation_callbacks(self, event: LearningEvent, result: Dict[str, Any]):
        """Trigger registered adaptation callbacks"""
        try:
            for callback in self.adaptation_callbacks:
                try:
                    if asyncio.iscoroutinefunction(callback):
                        await callback(event, result)
                    else:
                        callback(event, result)
                except Exception as e:
                    self.logger.error(f"Adaptation callback failed: {e}")
                    
        except Exception as e:
            self.logger.error(f"Callback triggering failed: {e}")
    
    def register_adaptation_callback(self, callback: Callable):
        """
        Register callback for learning adaptations
        
        Educational Impact:
        Enables integration with VR environment and MCP server
        for immediate application of learning adaptations.
        
        Args:
            callback: Function to call when adaptations are made
        """
        self.adaptation_callbacks.append(callback)
        self.logger.info("Adaptation callback registered")
    
    def get_pipeline_metrics(self) -> Dict[str, Any]:
        """
        Get current pipeline performance metrics
        
        Educational Impact:
        Provides visibility into pipeline performance for system
        optimization and educational effectiveness monitoring.
        
        Returns:
            Dictionary containing comprehensive pipeline metrics
        """
        return {
            "performance_metrics": {
                "events_processed": self.metrics.events_processed,
                "average_latency_ms": round(self.metrics.average_latency_ms, 2),
                "missed_deadlines": self.metrics.missed_deadlines,
                "success_rate_percent": round(
                    (self.metrics.successful_adaptations / max(self.metrics.events_processed, 1)) * 100, 1
                ),
                "throughput_events_per_second": self._calculate_throughput()
            },
            "system_metrics": {
                "active_learners": self.metrics.active_learners,
                "queue_depth": self.metrics.queue_depth,
                "worker_count": len(self.processing_tasks),
                "pipeline_running": self.is_running
            },
            "educational_metrics": {
                "successful_adaptations": self.metrics.successful_adaptations,
                "failed_adaptations": self.metrics.failed_adaptations,
                "real_time_compliance": self.metrics.average_latency_ms <= 25.0,
                "quest3_compliance": self.metrics.average_latency_ms <= 10.0
            },
            "timestamp": self.metrics.last_updated
        }
    
    def _calculate_throughput(self) -> float:
        """Calculate events per second throughput"""
        if len(self.throughput_measurements) < 2:
            return 0.0
        
        time_window = len(self.throughput_measurements) * self.metrics_update_interval
        events_in_window = sum(self.throughput_measurements)
        return events_in_window / time_window if time_window > 0 else 0.0
    
    async def create_learner_interaction_event(
        self,
        learner_id: str,
        interaction_type: str,
        interaction_data: Dict[str, Any],
        learning_event: str = "practice",
        priority: int = 3
    ) -> LearningEvent:
        """
        Create a learner interaction event for processing
        
        Educational Impact:
        Standardizes learner interaction data for consistent processing
        and immediate educational adaptation.
        
        Args:
            learner_id: Unique learner identifier
            interaction_type: Type of interaction (gesture, gaze, movement, etc.)
            interaction_data: Detailed interaction data
            learning_event: Current learning event context
            priority: Processing priority (1=highest, 10=lowest)
            
        Returns:
            LearningEvent ready for pipeline processing
        """
        event_id = f"interaction_{learner_id}_{int(time.time() * 1000)}"
        
        return LearningEvent(
            event_id=event_id,
            event_type=PipelineEventType.LEARNER_INTERACTION,
            learner_id=learner_id,
            timestamp=datetime.now().isoformat(),
            data={
                "interaction_type": interaction_type,
                "interaction": interaction_data,
                "learning_event": learning_event,
                "learner_data": {},  # Populated by MCP server
                "knowledge_data": {},  # Populated by MCP server
                "assessment_data": {}  # Populated by MCP server
            },
            priority=priority
        )
    
    async def process_immediate_adaptation(
        self,
        learner_id: str,
        adaptation_type: str,
        adaptation_data: Dict[str, Any]
    ) -> bool:
        """
        Process immediate adaptation for urgent learning needs
        
        Educational Impact:
        Enables immediate response to critical learning situations
        such as low attention or learning difficulties.
        
        Args:
            learner_id: Unique learner identifier
            adaptation_type: Type of adaptation needed
            adaptation_data: Adaptation parameters
            
        Returns:
            bool: True if adaptation was successfully processed
        """
        try:
            # Create high-priority adaptation event
            event = LearningEvent(
                event_id=f"urgent_adaptation_{learner_id}_{int(time.time() * 1000)}",
                event_type=PipelineEventType.LEARNING_ADAPTATION,
                learner_id=learner_id,
                timestamp=datetime.now().isoformat(),
                data={
                    "adaptation_type": adaptation_type,
                    "adaptation_data": adaptation_data,
                    "immediate": True
                },
                priority=1  # Highest priority
            )
            
            return await self.submit_learning_event(event)
            
        except Exception as e:
            self.logger.error(f"Immediate adaptation processing failed: {e}")
            return False
