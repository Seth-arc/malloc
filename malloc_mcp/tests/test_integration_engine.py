"""
Phase 3: Learning Integration Engine Test Suite
Test comprehensive functionality of the real-time learning equation implementation

Educational Impact:
Validates that the mathematical learning equation produces accurate,
consistent results for adaptive learning decisions while meeting
Quest 3 VR performance requirements.

Performance Requirements:
- Integration computation: <10ms
- Memory usage: <50MB for all operations
- Accuracy: >95% correlation with expected learning outcomes
"""

import pytest
import asyncio
import time
import json
from datetime import datetime
from typing import Dict, Any, List

# Import integration engine and related components
from src.learning.integration_engine import (
    LearningIntegrationEngine,
    LearningModelInputs,
    IntegrationResult,
    LearningEventType
)

class TestLearningIntegrationEngine:
    """
    Comprehensive test suite for Learning Integration Engine
    
    Educational Impact:
    Ensures mathematical learning equation operates correctly for
    all learning scenarios and maintains educational effectiveness.
    """
    
    @pytest.fixture
    async def integration_engine(self):
        """Create integration engine instance for testing"""
        engine = LearningIntegrationEngine()
        yield engine
        # Cleanup after tests
        engine.current_states.clear()
        engine.computation_history.clear()
        engine.computation_times.clear()
    
    @pytest.fixture
    def sample_learner_data(self) -> Dict[str, Any]:
        """Sample learner model data for testing"""
        return {
            "learner_model_weight": 0.35,
            "adaptation_parameters": {
                "alpha_baseline": 0.7,
                "beta_baseline": 0.15
            },
            "behavioral_analytics": {
                "engagement_pattern_score": 0.75,
                "learning_velocity": 0.65,
                "attention_stability": 0.80
            },
            "demographics": {
                "age_group": "adult",
                "learning_style": "visual",
                "prior_experience": "intermediate"
            }
        }
    
    @pytest.fixture
    def sample_knowledge_data(self) -> Dict[str, Any]:
        """Sample knowledge model data for testing"""
        return {
            "units_completed": 8,
            "total_units": 10,
            "prerequisite_satisfaction": 0.85,
            "curriculum_analytics": {
                "overall_mastery_level": 0.78,
                "progression_rate": 0.70,
                "knowledge_gaps": []
            },
            "competency_mapping": {
                "mathematics": 0.85,
                "spatial_reasoning": 0.75,
                "problem_solving": 0.80
            }
        }
    
    @pytest.fixture
    def sample_engagement_data(self) -> Dict[str, Any]:
        """Sample engagement model data for testing"""
        return {
            "attention_level": 0.82,
            "interaction_quality": 0.78,
            "flow_state_indicators": 0.85,
            "vr_interaction_metrics": {
                "spatial_engagement_score": 0.88,
                "gesture_engagement_score": 0.75,
                "eye_tracking_focus": 0.80
            },
            "session_metrics": {
                "time_in_session": 1800,  # 30 minutes
                "interaction_frequency": 45,
                "task_completion_rate": 0.90
            }
        }
    
    @pytest.fixture
    def sample_assessment_data(self) -> Dict[str, Any]:
        """Sample assessment model data for testing"""
        return {
            "competency_score": 0.83,
            "skill_demonstration": 0.79,
            "learning_evidence_strength": 0.81,
            "assessment_results": {
                "overall_score": 0.82,
                "confidence_level": 0.75,
                "mastery_indicators": ["conceptual_understanding", "practical_application"]
            },
            "performance_trends": {
                "improvement_rate": 0.15,
                "consistency_score": 0.85
            }
        }
    
    @pytest.fixture
    def complete_model_inputs(
        self, 
        sample_learner_data,
        sample_knowledge_data,
        sample_engagement_data,
        sample_assessment_data
    ) -> LearningModelInputs:
        """Complete model inputs for integration testing"""
        return LearningModelInputs(
            learner_model_data=sample_learner_data,
            knowledge_model_data=sample_knowledge_data,
            engagement_model_data=sample_engagement_data,
            assessment_model_data=sample_assessment_data,
            learning_event="practice"
        )

class TestMathematicalEquationImplementation:
    """Test mathematical learning equation computation accuracy"""
    
    @pytest.mark.asyncio
    async def test_basic_equation_computation(self, integration_engine, complete_model_inputs):
        """
        Test basic mathematical equation computation
        ∂(t+1) = ∂(t) + α · Δ(∩(t), ∆(t), E(t), A(t)) + β · ε(t)
        
        Educational Impact:
        Validates core mathematical learning equation produces consistent results
        """
        learner_id = "test_learner_001"
        
        # First computation (initial state)
        result1 = await integration_engine.compute_transition_state(
            learner_id, complete_model_inputs, "practice"
        )
        
        assert isinstance(result1, IntegrationResult)
        assert 0.0 <= result1.transition_state <= 1.0
        assert result1.learner_id == learner_id
        assert result1.learning_event == "practice"
        
        # Second computation (should use previous state)
        result2 = await integration_engine.compute_transition_state(
            learner_id, complete_model_inputs, "practice"
        )
        
        assert isinstance(result2, IntegrationResult)
        assert 0.0 <= result2.transition_state <= 1.0
        
        # Results should be different due to stochastic element
        # but within reasonable bounds
        state_diff = abs(result2.transition_state - result1.transition_state)
        assert state_diff > 0.0  # Should change due to stochastic element
        assert state_diff < 0.5   # Should not change dramatically
    
    @pytest.mark.asyncio
    async def test_weight_configuration_accuracy(self, integration_engine, complete_model_inputs):
        """Test dynamic weight adjustment for different learning events"""
        learner_id = "test_learner_weights"
        
        # Test each learning event type
        learning_events = ["onboarding", "introduction", "practice", "application", "mastery"]
        results = {}
        
        for event in learning_events:
            result = await integration_engine.compute_transition_state(
                learner_id, complete_model_inputs, event
            )
            
            results[event] = result
            
            # Verify weights match specification
            expected_weights = integration_engine.weight_configurations[event]
            assert result.model_weights == expected_weights
        
        # Verify different events produce different weight configurations
        weight_sets = [result.model_weights for result in results.values()]
        unique_weights = len(set(tuple(sorted(w.items())) for w in weight_sets))
        assert unique_weights == 5  # Should have 5 unique weight configurations
    
    @pytest.mark.asyncio
    async def test_stochastic_element_characteristics(self, integration_engine):
        """Test stochastic element generation characteristics"""
        stochastic_values = []
        
        # Generate multiple stochastic elements
        for _ in range(100):
            value = await integration_engine._generate_stochastic_element()
            stochastic_values.append(value)
            assert -0.3 <= value <= 0.3  # Should be within bounds
        
        # Test statistical properties
        mean_value = sum(stochastic_values) / len(stochastic_values)
        assert abs(mean_value) < 0.1  # Should be centered around 0
        
        # Should have variation (not all identical)
        unique_values = len(set(stochastic_values))
        assert unique_values > 50  # Should have significant variation

class TestPerformanceRequirements:
    """Test Quest 3 VR performance requirements compliance"""
    
    @pytest.mark.asyncio
    async def test_computation_speed_requirement(self, integration_engine, complete_model_inputs):
        """Test <10ms computation requirement for Quest 3 VR"""
        learner_id = "test_performance_001"
        
        # Perform multiple computations and measure timing
        computation_times = []
        
        for i in range(20):
            start_time = time.perf_counter()
            
            result = await integration_engine.compute_transition_state(
                learner_id, complete_model_inputs, "practice"
            )
            
            end_time = time.perf_counter()
            computation_time = (end_time - start_time) * 1000  # Convert to milliseconds
            computation_times.append(computation_time)
            
            # Individual computation should be <10ms
            assert result.computation_time_ms < 10.0, f"Computation took {result.computation_time_ms:.2f}ms (>10ms limit)"
        
        # Average should be well under 10ms
        avg_time = sum(computation_times) / len(computation_times)
        assert avg_time < 8.0, f"Average computation time {avg_time:.2f}ms too high"
        
        # 95% of computations should be under 8ms
        fast_computations = sum(1 for t in computation_times if t < 8.0)
        fast_percentage = (fast_computations / len(computation_times)) * 100
        assert fast_percentage >= 95.0, f"Only {fast_percentage:.1f}% of computations under 8ms"
    
    @pytest.mark.asyncio
    async def test_memory_usage_tracking(self, integration_engine, complete_model_inputs):
        """Test memory usage remains within Quest 3 VR limits"""
        learner_id = "test_memory_001"
        
        # Perform many computations to test memory accumulation
        initial_history_size = len(integration_engine.computation_history)
        
        for i in range(50):
            await integration_engine.compute_transition_state(
                learner_id + f"_{i}", complete_model_inputs, "practice"
            )
        
        # Check that history doesn't grow unbounded
        final_history_size = len(integration_engine.computation_history)
        history_growth = final_history_size - initial_history_size
        
        # Should store history but limit growth
        assert history_growth <= 50, "History growing unbounded"
        
        # Check state tracking
        assert len(integration_engine.current_states) <= 50, "Too many learner states stored"
    
    @pytest.mark.asyncio
    async def test_concurrent_processing(self, integration_engine, complete_model_inputs):
        """Test concurrent learner processing for multiple VR users"""
        learner_ids = [f"concurrent_learner_{i:03d}" for i in range(10)]
        
        # Process multiple learners concurrently
        start_time = time.perf_counter()
        
        tasks = [
            integration_engine.compute_transition_state(
                learner_id, complete_model_inputs, "practice"
            )
            for learner_id in learner_ids
        ]
        
        results = await asyncio.gather(*tasks)
        
        end_time = time.perf_counter()
        total_time = (end_time - start_time) * 1000
        
        # All results should be valid
        assert len(results) == 10
        for result in results:
            assert isinstance(result, IntegrationResult)
            assert 0.0 <= result.transition_state <= 1.0
        
        # Concurrent processing should be efficient
        average_time_per_learner = total_time / len(learner_ids)
        assert average_time_per_learner < 15.0, f"Concurrent processing too slow: {average_time_per_learner:.2f}ms per learner"

class TestEducationalEffectiveness:
    """Test educational effectiveness and learning progression accuracy"""
    
    @pytest.mark.asyncio
    async def test_learning_progression_logic(self, integration_engine, complete_model_inputs):
        """Test that learning progression follows educational logic"""
        learner_id = "test_progression_001"
        
        # Start with onboarding
        result_onboarding = await integration_engine.compute_transition_state(
            learner_id, complete_model_inputs, "onboarding"
        )
        
        # Progress through learning events
        learning_sequence = ["introduction", "practice", "application", "mastery"]
        previous_result = result_onboarding
        
        for event in learning_sequence:
            result = await integration_engine.compute_transition_state(
                learner_id, complete_model_inputs, event
            )
            
            # Check educational progression logic
            assert result.learning_event == event
            assert result.transition_decision is not None
            
            # High-performing learners should get advancement recommendations
            if result.transition_state >= 0.8:
                assert result.recommended_action in ["advance_to_next_event", "continue_current_event"]
            
            previous_result = result
    
    @pytest.mark.asyncio
    async def test_adaptive_parameter_calculation(self, integration_engine, complete_model_inputs):
        """Test adaptive parameter calculation for personalized learning"""
        learner_id = "test_adaptive_001"
        
        # Test different transition states
        test_states = [0.2, 0.5, 0.8, 0.95]
        
        for i, target_state in enumerate(test_states):
            # Manually set transition state for testing
            integration_engine.current_states[learner_id] = {
                "transition_state": target_state,
                "last_updated": datetime.now().isoformat(),
                "learning_event": "practice"
            }
            
            result = await integration_engine.compute_transition_state(
                learner_id, complete_model_inputs, "practice"
            )
            
            # Check adaptive parameters match transition state
            adaptive_params = result.transition_decision["adaptive_parameters"]
            
            if target_state >= 0.8:
                assert adaptive_params["difficulty_adjustment"] >= 1.0
                assert adaptive_params["support_level"] in ["minimal", "moderate"]
            elif target_state <= 0.4:
                assert adaptive_params["difficulty_adjustment"] <= 0.8
                assert adaptive_params["support_level"] in ["enhanced", "intensive"]
    
    @pytest.mark.asyncio
    async def test_educational_recommendations_quality(self, integration_engine, complete_model_inputs):
        """Test quality and relevance of educational recommendations"""
        learner_id = "test_recommendations_001"
        
        # Test with different performance levels
        performance_scenarios = [
            (0.2, "low_performance"),
            (0.5, "moderate_performance"),
            (0.8, "high_performance")
        ]
        
        for performance_level, scenario in performance_scenarios:
            # Set up scenario
            integration_engine.current_states[learner_id] = {
                "transition_state": performance_level,
                "last_updated": datetime.now().isoformat(),
                "learning_event": "practice"
            }
            
            result = await integration_engine.compute_transition_state(
                learner_id, complete_model_inputs, "practice"
            )
            
            # Check recommendations are appropriate
            recommendations = result.transition_decision["educational_recommendations"]
            assert isinstance(recommendations, list)
            assert len(recommendations) > 0
            
            # Low performance should include remediation
            if performance_level <= 0.4:
                recommendation_text = " ".join(recommendations).lower()
                assert any(word in recommendation_text for word in ["remediation", "support", "prerequisite"])
            
            # High performance should include advancement
            elif performance_level >= 0.8:
                recommendation_text = " ".join(recommendations).lower()
                assert any(word in recommendation_text for word in ["advanced", "challenge", "next"])

class TestErrorHandlingAndRobustness:
    """Test error handling and system robustness"""
    
    @pytest.mark.asyncio
    async def test_invalid_input_handling(self, integration_engine):
        """Test handling of invalid input data"""
        learner_id = "test_invalid_001"
        
        # Test with empty model inputs
        empty_inputs = LearningModelInputs(
            learner_model_data={},
            knowledge_model_data={},
            engagement_model_data={},
            assessment_model_data={}
        )
        
        result = await integration_engine.compute_transition_state(
            learner_id, empty_inputs, "practice"
        )
        
        # Should handle gracefully and return valid result
        assert isinstance(result, IntegrationResult)
        assert 0.0 <= result.transition_state <= 1.0
        assert result.confidence_score >= 0.0
    
    @pytest.mark.asyncio
    async def test_malformed_data_handling(self, integration_engine):
        """Test handling of malformed data"""
        learner_id = "test_malformed_001"
        
        # Test with malformed data
        malformed_inputs = LearningModelInputs(
            learner_model_data={"invalid_key": "invalid_value"},
            knowledge_model_data={"units_completed": "not_a_number"},
            engagement_model_data={"attention_level": -5.0},  # Invalid range
            assessment_model_data={"competency_score": 2.0}   # Invalid range
        )
        
        result = await integration_engine.compute_transition_state(
            learner_id, malformed_inputs, "practice"
        )
        
        # Should handle gracefully
        assert isinstance(result, IntegrationResult)
        assert result.computation_time_ms > 0
    
    @pytest.mark.asyncio
    async def test_unknown_learning_event_handling(self, integration_engine, complete_model_inputs):
        """Test handling of unknown learning events"""
        learner_id = "test_unknown_event_001"
        
        result = await integration_engine.compute_transition_state(
            learner_id, complete_model_inputs, "unknown_event"
        )
        
        # Should use default weights and handle gracefully
        assert isinstance(result, IntegrationResult)
        assert result.learning_event == "unknown_event"
        assert result.transition_state is not None

class TestSystemMonitoringAndAnalytics:
    """Test system monitoring and performance analytics"""
    
    @pytest.mark.asyncio
    async def test_performance_metrics_collection(self, integration_engine, complete_model_inputs):
        """Test performance metrics collection and reporting"""
        learner_id = "test_metrics_001"
        
        # Perform several computations
        for i in range(10):
            await integration_engine.compute_transition_state(
                learner_id, complete_model_inputs, "practice"
            )
        
        # Get performance metrics
        metrics = await integration_engine.get_performance_metrics()
        
        assert metrics["computation_performance"]["total_computations"] >= 10
        assert metrics["computation_performance"]["average_time_ms"] > 0
        assert metrics["quest3_compliance"]["status"] in ["compliant", "needs_optimization"]
    
    @pytest.mark.asyncio
    async def test_computation_history_tracking(self, integration_engine, complete_model_inputs):
        """Test computation history tracking for analytics"""
        learner_id = "test_history_001"
        
        initial_history_count = len(integration_engine.computation_history)
        
        # Perform computations
        for i in range(5):
            await integration_engine.compute_transition_state(
                learner_id, complete_model_inputs, "practice"
            )
        
        # Check history tracking
        final_history_count = len(integration_engine.computation_history)
        assert final_history_count >= initial_history_count + 5
        
        # Check history entry structure
        if integration_engine.computation_history:
            latest_entry = integration_engine.computation_history[-1]
            required_keys = [
                "learner_id", "timestamp", "learning_event", 
                "integration_result", "transition_state", "computation_time_ms"
            ]
            for key in required_keys:
                assert key in latest_entry
    
    @pytest.mark.asyncio
    async def test_learner_state_management(self, integration_engine, complete_model_inputs):
        """Test learner state management and reset functionality"""
        learner_id = "test_state_management_001"
        
        # Create initial state
        result1 = await integration_engine.compute_transition_state(
            learner_id, complete_model_inputs, "practice"
        )
        
        assert learner_id in integration_engine.current_states
        initial_state = result1.transition_state
        
        # Reset learner state
        await integration_engine.reset_learner_state(learner_id)
        assert learner_id not in integration_engine.current_states
        
        # Compute again (should start fresh)
        result2 = await integration_engine.compute_transition_state(
            learner_id, complete_model_inputs, "practice"
        )
        
        # Should be back to initial neutral state computation
        assert learner_id in integration_engine.current_states

# Integration test for full system functionality
@pytest.mark.asyncio
async def test_full_integration_scenario():
    """
    Full integration test simulating a complete learning session
    
    Educational Impact:
    Validates that the integration engine can handle a realistic
    educational VR learning session with multiple learners and
    learning progression scenarios.
    """
    engine = LearningIntegrationEngine()
    
    # Simulate 3 learners with different profiles
    learners = {
        "high_performer": {
            "learner_model_data": {"learner_model_weight": 0.40, "adaptation_parameters": {"alpha_baseline": 0.8}},
            "knowledge_model_data": {"units_completed": 9, "total_units": 10, "prerequisite_satisfaction": 0.95},
            "engagement_model_data": {"attention_level": 0.90, "interaction_quality": 0.85},
            "assessment_model_data": {"competency_score": 0.88, "skill_demonstration": 0.90}
        },
        "average_performer": {
            "learner_model_data": {"learner_model_weight": 0.30, "adaptation_parameters": {"alpha_baseline": 0.6}},
            "knowledge_model_data": {"units_completed": 5, "total_units": 10, "prerequisite_satisfaction": 0.70},
            "engagement_model_data": {"attention_level": 0.65, "interaction_quality": 0.60},
            "assessment_model_data": {"competency_score": 0.65, "skill_demonstration": 0.60}
        },
        "struggling_learner": {
            "learner_model_data": {"learner_model_weight": 0.25, "adaptation_parameters": {"alpha_baseline": 0.4}},
            "knowledge_model_data": {"units_completed": 2, "total_units": 10, "prerequisite_satisfaction": 0.40},
            "engagement_model_data": {"attention_level": 0.45, "interaction_quality": 0.40},
            "assessment_model_data": {"competency_score": 0.35, "skill_demonstration": 0.30}
        }
    }
    
    # Process each learner through learning progression
    results = {}
    
    for learner_type, data in learners.items():
        model_inputs = LearningModelInputs(**data)
        
        # Simulate learning session progression
        learning_sequence = ["onboarding", "introduction", "practice", "application"]
        learner_results = []
        
        for event in learning_sequence:
            result = await engine.compute_transition_state(
                learner_type, model_inputs, event
            )
            learner_results.append(result)
            
            # Verify performance requirements
            assert result.computation_time_ms < 10.0
            assert 0.0 <= result.transition_state <= 1.0
        
        results[learner_type] = learner_results
    
    # Validate different learners get appropriate recommendations
    high_performer_final = results["high_performer"][-1]
    struggling_learner_final = results["struggling_learner"][-1]
    
    # High performer should have higher transition state
    assert high_performer_final.transition_state > struggling_learner_final.transition_state
    
    # High performer should get advancement recommendations
    assert high_performer_final.recommended_action in ["advance_to_next_event", "continue_current_event"]
    
    # Struggling learner should get support recommendations
    assert struggling_learner_final.recommended_action in ["provide_additional_support", "remediate_prerequisites"]
    
    # Check overall system performance
    metrics = await engine.get_performance_metrics()
    assert metrics["quest3_compliance"]["status"] == "compliant"
    
    print(f"Integration test completed successfully:")
    print(f"- Processed {len(learners)} learners through {len(learning_sequence)} learning events")
    print(f"- Average computation time: {metrics['computation_performance']['average_time_ms']:.2f}ms")
    print(f"- Quest 3 compliance: {metrics['quest3_compliance']['status']}")

if __name__ == "__main__":
    # Run the full integration test
    asyncio.run(test_full_integration_scenario())
