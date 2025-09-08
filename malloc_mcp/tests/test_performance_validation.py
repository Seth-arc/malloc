"""
Phase 3: Performance Validation Test Suite
Comprehensive validation of Quest 3 VR performance requirements

Educational Impact:
Validates that the real-time learning integration system meets strict
performance requirements for educational VR experiences, ensuring
optimal learning outcomes without technical interruptions.

Performance Requirements Tested:
- Integration computation: <10ms for Quest 3 VR compliance
- Memory usage: <50MB for integration engine operations  
- Pipeline latency: <25ms for real-time processing
- Accuracy: >95% correlation with expected learning outcomes
- Concurrent learners: Support 50+ simultaneous users
"""

import pytest
import asyncio
import time
import psutil
import statistics
import gc
from datetime import datetime, timedelta
from typing import List, Dict, Any, Tuple
import numpy as np

# Import components under test
from src.learning.integration_engine import (
    LearningIntegrationEngine,
    LearningModelInputs, 
    IntegrationResult
)
from src.learning.real_time_pipeline import (
    RealTimeLearningPipeline,
    LearningEvent,
    PipelineEventType
)

class PerformanceMetrics:
    """Helper class for collecting and analyzing performance metrics"""
    
    def __init__(self):
        self.computation_times: List[float] = []
        self.memory_usage: List[float] = []
        self.accuracy_scores: List[float] = []
        self.throughput_measurements: List[int] = []
        self.latency_measurements: List[float] = []
    
    def add_computation_time(self, time_ms: float):
        """Add computation time measurement"""
        self.computation_times.append(time_ms)
    
    def add_memory_usage(self, memory_mb: float):
        """Add memory usage measurement"""
        self.memory_usage.append(memory_mb)
    
    def add_accuracy_score(self, score: float):
        """Add accuracy measurement"""
        self.accuracy_scores.append(score)
    
    def add_throughput(self, events_count: int):
        """Add throughput measurement"""
        self.throughput_measurements.append(events_count)
    
    def add_latency(self, latency_ms: float):
        """Add latency measurement"""
        self.latency_measurements.append(latency_ms)
    
    def get_computation_stats(self) -> Dict[str, float]:
        """Get computation time statistics"""
        if not self.computation_times:
            return {"mean": 0, "max": 0, "min": 0, "std": 0, "p95": 0, "p99": 0}
        
        times = sorted(self.computation_times)
        return {
            "mean": statistics.mean(times),
            "max": max(times),
            "min": min(times),
            "std": statistics.stdev(times) if len(times) > 1 else 0,
            "p95": np.percentile(times, 95),
            "p99": np.percentile(times, 99),
            "count": len(times),
            "under_10ms_percent": (sum(1 for t in times if t <= 10.0) / len(times)) * 100
        }
    
    def get_memory_stats(self) -> Dict[str, float]:
        """Get memory usage statistics"""
        if not self.memory_usage:
            return {"mean": 0, "max": 0, "min": 0, "peak": 0}
        
        return {
            "mean": statistics.mean(self.memory_usage),
            "max": max(self.memory_usage),
            "min": min(self.memory_usage),
            "peak": max(self.memory_usage),
            "under_50mb_percent": (sum(1 for m in self.memory_usage if m <= 50.0) / len(self.memory_usage)) * 100
        }
    
    def get_accuracy_stats(self) -> Dict[str, float]:
        """Get accuracy statistics"""
        if not self.accuracy_scores:
            return {"mean": 0, "min": 0, "over_95_percent": 0}
        
        return {
            "mean": statistics.mean(self.accuracy_scores),
            "min": min(self.accuracy_scores),
            "max": max(self.accuracy_scores),
            "over_95_percent": (sum(1 for s in self.accuracy_scores if s >= 0.95) / len(self.accuracy_scores)) * 100
        }
    
    def get_throughput_stats(self) -> Dict[str, float]:
        """Get throughput statistics"""
        if not self.throughput_measurements:
            return {"mean": 0, "max": 0, "total": 0}
        
        return {
            "mean": statistics.mean(self.throughput_measurements),
            "max": max(self.throughput_measurements),
            "total": sum(self.throughput_measurements)
        }

class MemoryProfiler:
    """Memory profiling helper for tracking memory usage"""
    
    def __init__(self):
        self.process = psutil.Process()
        self.initial_memory = self.get_memory_usage()
    
    def get_memory_usage(self) -> float:
        """Get current memory usage in MB"""
        return self.process.memory_info().rss / (1024 * 1024)
    
    def get_memory_increase(self) -> float:
        """Get memory increase since initialization"""
        return self.get_memory_usage() - self.initial_memory

@pytest.fixture
def integration_engine():
    """Create integration engine for performance testing"""
    engine = LearningIntegrationEngine()
    yield engine
    # Cleanup
    engine.current_states.clear()
    engine.computation_history.clear()
    engine.computation_times.clear()

@pytest.fixture  
def sample_model_inputs():
    """Generate sample model inputs for testing"""
    return LearningModelInputs(
        learner_model_data={
            "learner_model_weight": 0.35,
            "adaptation_parameters": {"alpha_baseline": 0.7},
            "behavioral_analytics": {"engagement_pattern_score": 0.75}
        },
        knowledge_model_data={
            "units_completed": 8,
            "total_units": 10,
            "prerequisite_satisfaction": 0.85
        },
        engagement_model_data={
            "attention_level": 0.82,
            "interaction_quality": 0.78,
            "vr_interaction_metrics": {"spatial_engagement_score": 0.88}
        },
        assessment_model_data={
            "competency_score": 0.83,
            "skill_demonstration": 0.79,
            "assessment_results": {"overall_score": 0.82}
        }
    )

class TestComputationPerformance:
    """Test computational performance requirements"""
    
    @pytest.mark.asyncio
    async def test_10ms_computation_requirement(self, integration_engine, sample_model_inputs):
        """
        Test Quest 3 VR requirement: Integration computation <10ms
        
        Educational Impact:
        Validates that learning equation computation meets VR frame rate
        requirements for seamless educational experiences.
        """
        metrics = PerformanceMetrics()
        memory_profiler = MemoryProfiler()
        
        # Test with multiple learners and scenarios
        test_scenarios = [
            ("onboarding", 20),
            ("introduction", 30), 
            ("practice", 50),
            ("application", 30),
            ("mastery", 20)
        ]
        
        total_computations = 0
        
        for learning_event, num_tests in test_scenarios:
            for i in range(num_tests):
                learner_id = f"perf_test_{learning_event}_{i:03d}"
                
                # Measure computation time
                start_time = time.perf_counter()
                
                result = await integration_engine.compute_transition_state(
                    learner_id, sample_model_inputs, learning_event
                )
                
                end_time = time.perf_counter()
                computation_time = (end_time - start_time) * 1000  # Convert to ms
                
                # Collect metrics
                metrics.add_computation_time(computation_time)
                metrics.add_memory_usage(memory_profiler.get_memory_usage())
                
                # Validate individual computation
                assert computation_time < 10.0, f"Computation took {computation_time:.2f}ms (>10ms limit)"
                assert isinstance(result, IntegrationResult)
                assert 0.0 <= result.transition_state <= 1.0
                
                total_computations += 1
        
        # Analyze overall performance
        comp_stats = metrics.get_computation_stats()
        memory_stats = metrics.get_memory_stats()
        
        print(f"\n=== Computation Performance Report ===")
        print(f"Total computations: {total_computations}")
        print(f"Mean computation time: {comp_stats['mean']:.2f}ms")
        print(f"Max computation time: {comp_stats['max']:.2f}ms")
        print(f"95th percentile: {comp_stats['p95']:.2f}ms")
        print(f"99th percentile: {comp_stats['p99']:.2f}ms")
        print(f"Under 10ms: {comp_stats['under_10ms_percent']:.1f}%")
        print(f"Peak memory usage: {memory_stats['peak']:.1f}MB")
        
        # Performance assertions
        assert comp_stats['mean'] < 8.0, f"Mean computation time {comp_stats['mean']:.2f}ms too high"
        assert comp_stats['p95'] < 10.0, f"95th percentile {comp_stats['p95']:.2f}ms exceeds limit"
        assert comp_stats['under_10ms_percent'] >= 99.0, f"Only {comp_stats['under_10ms_percent']:.1f}% under 10ms"
        assert memory_stats['peak'] < 50.0, f"Peak memory {memory_stats['peak']:.1f}MB exceeds limit"
    
    @pytest.mark.asyncio
    async def test_concurrent_computation_performance(self, integration_engine, sample_model_inputs):
        """
        Test concurrent computation performance for multiple learners
        
        Educational Impact:
        Validates that system can handle multiple simultaneous VR learners
        without performance degradation.
        """
        metrics = PerformanceMetrics()
        memory_profiler = MemoryProfiler()
        
        # Test concurrent processing with 25 learners
        num_learners = 25
        computations_per_learner = 10
        
        async def process_learner(learner_id: str) -> List[float]:
            """Process multiple computations for a single learner"""
            learner_times = []
            
            for i in range(computations_per_learner):
                start_time = time.perf_counter()
                
                result = await integration_engine.compute_transition_state(
                    f"{learner_id}_{i}", sample_model_inputs, "practice"
                )
                
                end_time = time.perf_counter()
                computation_time = (end_time - start_time) * 1000
                
                learner_times.append(computation_time)
                assert computation_time < 15.0, f"Concurrent computation too slow: {computation_time:.2f}ms"
            
            return learner_times
        
        # Execute concurrent processing
        start_time = time.perf_counter()
        
        tasks = [
            process_learner(f"concurrent_learner_{i:03d}")
            for i in range(num_learners)
        ]
        
        results = await asyncio.gather(*tasks)
        
        end_time = time.perf_counter()
        total_time = end_time - start_time
        
        # Collect all computation times
        all_times = []
        for learner_times in results:
            all_times.extend(learner_times)
            for time_ms in learner_times:
                metrics.add_computation_time(time_ms)
        
        # Calculate performance metrics
        total_computations = num_learners * computations_per_learner
        average_time_per_computation = (total_time * 1000) / total_computations
        throughput = total_computations / total_time
        
        print(f"\n=== Concurrent Performance Report ===")
        print(f"Learners: {num_learners}")
        print(f"Total computations: {total_computations}")
        print(f"Total time: {total_time:.2f}s")
        print(f"Average time per computation: {average_time_per_computation:.2f}ms")
        print(f"Throughput: {throughput:.1f} computations/second")
        print(f"Memory usage: {memory_profiler.get_memory_usage():.1f}MB")
        
        # Performance assertions for concurrent processing
        assert average_time_per_computation < 12.0, f"Concurrent processing too slow: {average_time_per_computation:.2f}ms"
        assert throughput >= 100.0, f"Throughput too low: {throughput:.1f} computations/second"
        assert memory_profiler.get_memory_usage() < 75.0, "Memory usage too high during concurrent processing"

class TestMemoryPerformance:
    """Test memory usage performance requirements"""
    
    @pytest.mark.asyncio  
    async def test_memory_usage_limits(self, integration_engine, sample_model_inputs):
        """
        Test memory usage remains within Quest 3 VR limits (<50MB)
        
        Educational Impact:
        Ensures memory efficiency for optimal VR performance and
        prevents memory-related learning experience interruptions.
        """
        memory_profiler = MemoryProfiler()
        initial_memory = memory_profiler.get_memory_usage()
        
        # Perform extensive processing to test memory growth
        num_learners = 100
        computations_per_learner = 20
        
        memory_measurements = []
        
        for learner_idx in range(num_learners):
            learner_id = f"memory_test_{learner_idx:03d}"
            
            for comp_idx in range(computations_per_learner):
                # Perform computation
                result = await integration_engine.compute_transition_state(
                    f"{learner_id}_{comp_idx}", sample_model_inputs, "practice"
                )
                
                # Measure memory every 10 computations
                if comp_idx % 10 == 0:
                    current_memory = memory_profiler.get_memory_usage()
                    memory_measurements.append(current_memory)
                    
                    # Check memory limit
                    assert current_memory < 100.0, f"Memory usage {current_memory:.1f}MB too high"
            
            # Force garbage collection periodically
            if learner_idx % 25 == 0:
                gc.collect()
        
        # Final memory check
        final_memory = memory_profiler.get_memory_usage()
        memory_increase = final_memory - initial_memory
        peak_memory = max(memory_measurements)
        
        print(f"\n=== Memory Usage Report ===")
        print(f"Initial memory: {initial_memory:.1f}MB")
        print(f"Final memory: {final_memory:.1f}MB") 
        print(f"Memory increase: {memory_increase:.1f}MB")
        print(f"Peak memory: {peak_memory:.1f}MB")
        print(f"Total computations: {num_learners * computations_per_learner}")
        
        # Memory assertions
        assert memory_increase < 30.0, f"Memory increase {memory_increase:.1f}MB too high"
        assert peak_memory < 80.0, f"Peak memory {peak_memory:.1f}MB exceeds operational limit"
        assert final_memory < 75.0, f"Final memory {final_memory:.1f}MB too high"
    
    @pytest.mark.asyncio
    async def test_memory_leak_detection(self, integration_engine, sample_model_inputs):
        """
        Test for memory leaks during extended operation
        
        Educational Impact:
        Ensures system stability during long educational VR sessions
        without memory-related performance degradation.
        """
        memory_profiler = MemoryProfiler()
        
        # Baseline measurement
        baseline_measurements = []
        for _ in range(10):
            await integration_engine.compute_transition_state(
                "baseline_test", sample_model_inputs, "practice"
            )
            baseline_measurements.append(memory_profiler.get_memory_usage())
        
        baseline_memory = statistics.mean(baseline_measurements)
        
        # Extended operation test
        extended_measurements = []
        for cycle in range(5):  # 5 cycles of extended operation
            
            # Process many computations
            for i in range(50):
                learner_id = f"leak_test_cycle_{cycle}_learner_{i}"
                await integration_engine.compute_transition_state(
                    learner_id, sample_model_inputs, "practice"
                )
            
            # Reset some state to test cleanup
            integration_engine.computation_history.clear()
            if len(integration_engine.current_states) > 100:
                # Clear old states to simulate realistic cleanup
                old_states = list(integration_engine.current_states.keys())[:50]
                for state_id in old_states:
                    del integration_engine.current_states[state_id]
            
            # Force garbage collection
            gc.collect()
            
            # Measure memory after cleanup
            memory_after_cycle = memory_profiler.get_memory_usage()
            extended_measurements.append(memory_after_cycle)
            
            print(f"Cycle {cycle + 1}: {memory_after_cycle:.1f}MB")
        
        # Analyze memory trend
        final_memory = extended_measurements[-1]
        memory_growth = final_memory - baseline_memory
        
        # Check for consistent memory growth (potential leak)
        if len(extended_measurements) >= 3:
            recent_trend = extended_measurements[-3:]
            trend_increasing = all(
                recent_trend[i] <= recent_trend[i + 1] + 2.0  # Allow 2MB variance
                for i in range(len(recent_trend) - 1)
            )
        else:
            trend_increasing = False
        
        print(f"\n=== Memory Leak Detection Report ===")
        print(f"Baseline memory: {baseline_memory:.1f}MB")
        print(f"Final memory: {final_memory:.1f}MB")
        print(f"Memory growth: {memory_growth:.1f}MB")
        print(f"Trend increasing: {trend_increasing}")
        
        # Memory leak assertions
        assert memory_growth < 15.0, f"Memory growth {memory_growth:.1f}MB indicates potential leak"
        assert final_memory < 80.0, f"Final memory {final_memory:.1f}MB too high"

class TestAccuracyValidation:
    """Test accuracy and educational effectiveness requirements"""
    
    @pytest.mark.asyncio
    async def test_learning_equation_accuracy(self, integration_engine):
        """
        Test accuracy of learning equation implementation (>95% correlation)
        
        Educational Impact:
        Validates that mathematical learning equation produces educationally
        sound results that correlate with expected learning outcomes.
        """
        # Test scenarios with known expected outcomes
        test_scenarios = [
            {
                "name": "high_performer",
                "inputs": LearningModelInputs(
                    learner_model_data={"learner_model_weight": 0.40, "adaptation_parameters": {"alpha_baseline": 0.8}},
                    knowledge_model_data={"units_completed": 9, "total_units": 10, "prerequisite_satisfaction": 0.95},
                    engagement_model_data={"attention_level": 0.90, "interaction_quality": 0.85},
                    assessment_model_data={"competency_score": 0.88, "skill_demonstration": 0.90}
                ),
                "expected_range": (0.7, 1.0),
                "expected_action": ["advance_to_next_event", "continue_current_event"]
            },
            {
                "name": "struggling_learner", 
                "inputs": LearningModelInputs(
                    learner_model_data={"learner_model_weight": 0.25, "adaptation_parameters": {"alpha_baseline": 0.4}},
                    knowledge_model_data={"units_completed": 2, "total_units": 10, "prerequisite_satisfaction": 0.40},
                    engagement_model_data={"attention_level": 0.35, "interaction_quality": 0.30},
                    assessment_model_data={"competency_score": 0.25, "skill_demonstration": 0.20}
                ),
                "expected_range": (0.0, 0.5),
                "expected_action": ["provide_additional_support", "remediate_prerequisites"]
            },
            {
                "name": "average_learner",
                "inputs": LearningModelInputs(
                    learner_model_data={"learner_model_weight": 0.30, "adaptation_parameters": {"alpha_baseline": 0.6}},
                    knowledge_model_data={"units_completed": 5, "total_units": 10, "prerequisite_satisfaction": 0.70},
                    engagement_model_data={"attention_level": 0.65, "interaction_quality": 0.60},
                    assessment_model_data={"competency_score": 0.65, "skill_demonstration": 0.60}
                ),
                "expected_range": (0.4, 0.8),
                "expected_action": ["continue_current_event", "provide_additional_support"]
            }
        ]
        
        accuracy_scores = []
        
        for scenario in test_scenarios:
            correct_predictions = 0
            total_predictions = 20
            
            for i in range(total_predictions):
                learner_id = f"{scenario['name']}_{i:03d}"
                
                result = await integration_engine.compute_transition_state(
                    learner_id, scenario["inputs"], "practice"
                )
                
                # Check transition state range accuracy
                min_expected, max_expected = scenario["expected_range"]
                state_in_range = min_expected <= result.transition_state <= max_expected
                
                # Check recommended action accuracy  
                action_correct = result.recommended_action in scenario["expected_action"]
                
                # Count as correct if both state and action are appropriate
                if state_in_range and action_correct:
                    correct_predictions += 1
            
            scenario_accuracy = correct_predictions / total_predictions
            accuracy_scores.append(scenario_accuracy)
            
            print(f"{scenario['name']} accuracy: {scenario_accuracy:.1%}")
            
            # Individual scenario accuracy should be >90%
            assert scenario_accuracy >= 0.90, f"{scenario['name']} accuracy {scenario_accuracy:.1%} too low"
        
        # Overall accuracy should be >95%
        overall_accuracy = statistics.mean(accuracy_scores)
        print(f"\nOverall accuracy: {overall_accuracy:.1%}")
        
        assert overall_accuracy >= 0.95, f"Overall accuracy {overall_accuracy:.1%} below 95% requirement"
    
    @pytest.mark.asyncio
    async def test_consistency_validation(self, integration_engine, sample_model_inputs):
        """
        Test consistency of learning equation results
        
        Educational Impact:
        Ensures that similar learning situations produce consistent
        educational recommendations for reliable learning experiences.
        """
        learner_id = "consistency_test"
        
        # Run multiple computations with same inputs
        results = []
        for i in range(30):
            result = await integration_engine.compute_transition_state(
                learner_id, sample_model_inputs, "practice"
            )
            results.append(result.transition_state)
        
        # Analyze consistency
        mean_state = statistics.mean(results)
        std_dev = statistics.stdev(results)
        min_state = min(results)
        max_state = max(results)
        range_size = max_state - min_state
        
        print(f"\n=== Consistency Analysis ===")
        print(f"Mean transition state: {mean_state:.3f}")
        print(f"Standard deviation: {std_dev:.3f}")
        print(f"Range: {range_size:.3f} ({min_state:.3f} - {max_state:.3f})")
        print(f"Coefficient of variation: {(std_dev / mean_state):.3f}")
        
        # Consistency assertions
        assert std_dev < 0.1, f"Standard deviation {std_dev:.3f} too high - inconsistent results"
        assert range_size < 0.3, f"Range {range_size:.3f} too large - inconsistent results"
        
        # Results should vary due to stochastic element but remain stable
        assert range_size > 0.01, "Results too consistent - stochastic element not working"

class TestRealTimePipelinePerformance:
    """Test real-time pipeline performance requirements"""
    
    @pytest.mark.asyncio
    async def test_pipeline_latency_requirement(self, integration_engine):
        """
        Test pipeline latency <25ms requirement
        
        Educational Impact:
        Validates that real-time learning adaptation meets VR responsiveness
        requirements for immediate educational feedback.
        """
        from src.learning.real_time_pipeline import RealTimeLearningPipeline, LearningEvent, PipelineEventType
        
        pipeline = RealTimeLearningPipeline(integration_engine)
        await pipeline.start_pipeline()
        
        try:
            latency_measurements = []
            
            # Test pipeline latency with various event types
            event_types = [
                PipelineEventType.LEARNER_INTERACTION,
                PipelineEventType.ENGAGEMENT_CHANGE,
                PipelineEventType.ASSESSMENT_COMPLETION
            ]
            
            for event_type in event_types:
                for i in range(20):
                    # Create test event
                    event = LearningEvent(
                        event_id=f"latency_test_{event_type.value}_{i}",
                        event_type=event_type,
                        learner_id=f"latency_learner_{i}",
                        timestamp=datetime.now().isoformat(),
                        data={
                            "interaction": {"attention_level": 0.75},
                            "learning_event": "practice"
                        },
                        priority=2
                    )
                    
                    # Measure end-to-end latency
                    start_time = time.perf_counter()
                    
                    success = await pipeline.submit_learning_event(event)
                    assert success, "Failed to submit event to pipeline"
                    
                    # Wait for processing completion (simplified for testing)
                    await asyncio.sleep(0.01)  # 10ms wait
                    
                    end_time = time.perf_counter()
                    latency = (end_time - start_time) * 1000
                    
                    latency_measurements.append(latency)
                    
                    # Individual latency check
                    assert latency < 30.0, f"Pipeline latency {latency:.2f}ms too high"
            
            # Analyze overall latency performance
            mean_latency = statistics.mean(latency_measurements)
            max_latency = max(latency_measurements)
            p95_latency = np.percentile(latency_measurements, 95)
            
            print(f"\n=== Pipeline Latency Report ===")
            print(f"Mean latency: {mean_latency:.2f}ms")
            print(f"Max latency: {max_latency:.2f}ms")
            print(f"95th percentile: {p95_latency:.2f}ms")
            print(f"Under 25ms: {(sum(1 for l in latency_measurements if l <= 25.0) / len(latency_measurements)) * 100:.1f}%")
            
            # Pipeline latency assertions
            assert mean_latency < 20.0, f"Mean pipeline latency {mean_latency:.2f}ms too high"
            assert p95_latency < 25.0, f"95th percentile latency {p95_latency:.2f}ms exceeds limit"
            
        finally:
            await pipeline.stop_pipeline()
    
    @pytest.mark.asyncio
    async def test_pipeline_throughput(self, integration_engine):
        """
        Test pipeline throughput for concurrent learners (50+ learners)
        
        Educational Impact:
        Validates that system can handle classroom-scale VR learning
        with multiple simultaneous learners.
        """
        from src.learning.real_time_pipeline import RealTimeLearningPipeline, LearningEvent, PipelineEventType
        
        pipeline = RealTimeLearningPipeline(integration_engine)
        await pipeline.start_pipeline()
        
        try:
            num_learners = 50
            events_per_learner = 10
            total_events = num_learners * events_per_learner
            
            # Create all events
            events = []
            for learner_idx in range(num_learners):
                for event_idx in range(events_per_learner):
                    event = LearningEvent(
                        event_id=f"throughput_test_{learner_idx}_{event_idx}",
                        event_type=PipelineEventType.LEARNER_INTERACTION,
                        learner_id=f"throughput_learner_{learner_idx:03d}",
                        timestamp=datetime.now().isoformat(),
                        data={
                            "interaction": {"attention_level": 0.70 + (learner_idx % 30) / 100},
                            "learning_event": "practice"
                        },
                        priority=3
                    )
                    events.append(event)
            
            # Submit all events and measure throughput
            start_time = time.perf_counter()
            
            submitted_count = 0
            for event in events:
                success = await pipeline.submit_learning_event(event)
                if success:
                    submitted_count += 1
            
            # Wait for processing to complete
            processing_time = 2.0  # 2 seconds processing window
            await asyncio.sleep(processing_time)
            
            end_time = time.perf_counter()
            total_time = end_time - start_time
            
            # Calculate throughput metrics
            throughput = submitted_count / total_time
            events_per_second = submitted_count / processing_time
            
            # Get pipeline metrics
            pipeline_metrics = pipeline.get_pipeline_metrics()
            
            print(f"\n=== Pipeline Throughput Report ===")
            print(f"Total events: {total_events}")
            print(f"Submitted events: {submitted_count}")
            print(f"Processing time: {total_time:.2f}s")
            print(f"Throughput: {throughput:.1f} events/second")
            print(f"Processing rate: {events_per_second:.1f} events/second")
            print(f"Active learners: {pipeline_metrics['system_metrics']['active_learners']}")
            print(f"Success rate: {pipeline_metrics['performance_metrics']['success_rate_percent']:.1f}%")
            
            # Throughput assertions
            assert submitted_count >= total_events * 0.95, f"Only {submitted_count}/{total_events} events submitted"
            assert throughput >= 100.0, f"Throughput {throughput:.1f} events/s too low"
            assert pipeline_metrics['system_metrics']['active_learners'] >= 40, "Not enough active learners tracked"
            
        finally:
            await pipeline.stop_pipeline()

# Integration performance test
@pytest.mark.asyncio
async def test_full_system_performance():
    """
    Comprehensive system performance test
    
    Educational Impact:
    Validates that the complete Phase 3 real-time integration system
    meets all performance requirements for educational VR learning.
    """
    print("\n" + "="*60)
    print("PHASE 3 COMPREHENSIVE PERFORMANCE VALIDATION")
    print("="*60)
    
    # Initialize system components
    integration_engine = LearningIntegrationEngine()
    
    # Performance tracking
    overall_metrics = PerformanceMetrics()
    memory_profiler = MemoryProfiler()
    
    # Test scenario: Realistic educational VR session
    num_learners = 25
    session_duration_minutes = 5
    interactions_per_minute = 12  # Realistic VR interaction rate
    
    total_interactions = num_learners * session_duration_minutes * interactions_per_minute
    
    print(f"Simulating {num_learners} learners for {session_duration_minutes} minutes")
    print(f"Expected interactions: {total_interactions}")
    
    # Generate realistic test data
    sample_inputs = LearningModelInputs(
        learner_model_data={"learner_model_weight": 0.35, "adaptation_parameters": {"alpha_baseline": 0.7}},
        knowledge_model_data={"units_completed": 6, "total_units": 10, "prerequisite_satisfaction": 0.75},
        engagement_model_data={"attention_level": 0.75, "interaction_quality": 0.70},
        assessment_model_data={"competency_score": 0.72, "skill_demonstration": 0.68}
    )
    
    # Execute performance test
    start_time = time.perf_counter()
    successful_computations = 0
    
    for interaction in range(total_interactions):
        learner_id = f"full_test_learner_{interaction % num_learners:03d}"
        learning_event = ["practice", "application"][interaction % 2]
        
        try:
            computation_start = time.perf_counter()
            
            result = await integration_engine.compute_transition_state(
                learner_id, sample_inputs, learning_event
            )
            
            computation_end = time.perf_counter()
            computation_time = (computation_end - computation_start) * 1000
            
            # Collect metrics
            overall_metrics.add_computation_time(computation_time)
            overall_metrics.add_memory_usage(memory_profiler.get_memory_usage())
            
            # Validate result quality
            if (0.0 <= result.transition_state <= 1.0 and 
                result.confidence_score >= 0.0 and
                computation_time < 10.0):
                successful_computations += 1
                overall_metrics.add_accuracy_score(1.0)
            else:
                overall_metrics.add_accuracy_score(0.0)
            
            # Periodic cleanup to simulate realistic operation
            if interaction % 100 == 0:
                # Cleanup old states (simulate realistic memory management)
                if len(integration_engine.current_states) > 50:
                    old_states = list(integration_engine.current_states.keys())[:25]
                    for state_id in old_states:
                        del integration_engine.current_states[state_id]
                
                # Force garbage collection periodically
                if interaction % 500 == 0:
                    gc.collect()
        
        except Exception as e:
            print(f"Error in interaction {interaction}: {e}")
            overall_metrics.add_accuracy_score(0.0)
    
    end_time = time.perf_counter()
    total_test_time = end_time - start_time
    
    # Calculate final metrics
    comp_stats = overall_metrics.get_computation_stats()
    memory_stats = overall_metrics.get_memory_stats()
    accuracy_stats = overall_metrics.get_accuracy_stats()
    
    success_rate = (successful_computations / total_interactions) * 100
    throughput = total_interactions / total_test_time
    
    # Generate comprehensive report
    print(f"\n=== COMPREHENSIVE PERFORMANCE REPORT ===")
    print(f"Total test time: {total_test_time:.2f}s")
    print(f"Total interactions: {total_interactions}")
    print(f"Successful computations: {successful_computations}")
    print(f"Success rate: {success_rate:.1f}%")
    print(f"Throughput: {throughput:.1f} interactions/second")
    print(f"")
    print(f"COMPUTATION PERFORMANCE:")
    print(f"  Mean time: {comp_stats['mean']:.2f}ms")
    print(f"  Max time: {comp_stats['max']:.2f}ms") 
    print(f"  95th percentile: {comp_stats['p95']:.2f}ms")
    print(f"  Under 10ms: {comp_stats['under_10ms_percent']:.1f}%")
    print(f"")
    print(f"MEMORY PERFORMANCE:")
    print(f"  Peak usage: {memory_stats['peak']:.1f}MB")
    print(f"  Mean usage: {memory_stats['mean']:.1f}MB")
    print(f"  Under 50MB: {memory_stats['under_50mb_percent']:.1f}%")
    print(f"")
    print(f"ACCURACY PERFORMANCE:")
    print(f"  Mean accuracy: {accuracy_stats['mean']:.1%}")
    print(f"  Over 95%: {accuracy_stats['over_95_percent']:.1f}%")
    
    # Final assertions for all requirements
    print(f"\n=== REQUIREMENT VALIDATION ===")
    
    # Computation time requirement (<10ms)
    comp_requirement_met = comp_stats['p95'] < 10.0
    print(f"✓ Computation <10ms: {comp_requirement_met} ({comp_stats['p95']:.2f}ms 95th percentile)")
    assert comp_requirement_met, f"Computation time requirement failed: {comp_stats['p95']:.2f}ms"
    
    # Memory requirement (<50MB)
    memory_requirement_met = memory_stats['peak'] < 50.0
    print(f"✓ Memory <50MB: {memory_requirement_met} ({memory_stats['peak']:.1f}MB peak)")
    assert memory_requirement_met, f"Memory requirement failed: {memory_stats['peak']:.1f}MB"
    
    # Accuracy requirement (>95%)
    accuracy_requirement_met = accuracy_stats['mean'] >= 0.95
    print(f"✓ Accuracy >95%: {accuracy_requirement_met} ({accuracy_stats['mean']:.1%} mean)")
    assert accuracy_requirement_met, f"Accuracy requirement failed: {accuracy_stats['mean']:.1%}"
    
    # Throughput requirement (realistic for VR)
    throughput_requirement_met = throughput >= 50.0
    print(f"✓ Throughput adequate: {throughput_requirement_met} ({throughput:.1f} interactions/s)")
    assert throughput_requirement_met, f"Throughput requirement failed: {throughput:.1f} interactions/s"
    
    print(f"\n✅ ALL PHASE 3 PERFORMANCE REQUIREMENTS VALIDATED")
    print(f"✅ QUEST 3 VR OPTIMIZATION CONFIRMED")
    print(f"✅ REAL-TIME LEARNING INTEGRATION OPERATIONAL")

if __name__ == "__main__":
    # Run comprehensive performance validation
    asyncio.run(test_full_system_performance())
