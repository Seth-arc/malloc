"""
Phase 3: Comprehensive Integration Test Suite
Validates integration between all learning models and real-time processing

Educational Impact:
Ensures that the complete Phase 3 real-time integration system works
seamlessly with all five learning models to provide optimal educational
VR experiences with mathematical learning equation computation.

Integration Areas Tested:
- Learning Integration Engine with all five learning models
- Real-time pipeline processing with continuous adaptation
- Mathematical equation computation accuracy across models
- Performance compliance during full system operation
"""

import pytest
import asyncio
import time
import json
from datetime import datetime, timedelta
from typing import Dict, List, Any, Tuple

# Import all learning model components
from src.learning.learner_model import LearnerModelProcessor, LearnerProfileData
from src.learning.knowledge_model import KnowledgeModelProcessor, KnowledgeStructureData
from src.learning.engagement_model import EngagementModelProcessor, VRInteractionData
from src.learning.assessment_model import AssessmentModelProcessor, AssessmentConfiguration
from src.learning.transition_model import TransitionModelProcessor, TransitionConfiguration

# Import Phase 3 components
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

class IntegratedLearningSystem:
    """
    Complete learning system integrating all Phase 1, 2, and 3 components
    
    Educational Impact:
    Provides unified interface for comprehensive educational VR learning
    with real-time adaptation and mathematical learning equation computation.
    """
    
    def __init__(self):
        """Initialize complete integrated learning system"""
        
        # Phase 2: Learning model processors
        self.learner_processor = LearnerModelProcessor()
        self.knowledge_processor = KnowledgeModelProcessor()
        self.engagement_processor = EngagementModelProcessor()
        self.assessment_processor = AssessmentModelProcessor()
        self.transition_processor = TransitionModelProcessor()
        
        # Phase 3: Integration and real-time processing
        self.integration_engine = LearningIntegrationEngine()
        self.real_time_pipeline = RealTimeLearningPipeline(self.integration_engine)
        
        # System state
        self.active_learners: Dict[str, Dict[str, Any]] = {}
        self.session_metrics: Dict[str, Any] = {}
        
    async def initialize_system(self):
        """Initialize the complete learning system"""
        # Initialize learning model processors
        await self.learner_processor.initialize_processor()
        await self.knowledge_processor.initialize_processor()
        await self.engagement_processor.initialize_processor()
        await self.assessment_processor.initialize_processor()
        await self.transition_processor.initialize_processor()
        
        # Start real-time pipeline
        await self.real_time_pipeline.start_pipeline()
        
        print("Integrated learning system initialized")
    
    async def shutdown_system(self):
        """Shutdown the complete learning system"""
        await self.real_time_pipeline.stop_pipeline()
        print("Integrated learning system shutdown")
    
    async def create_comprehensive_learner_profile(self, learner_id: str) -> Dict[str, Any]:
        """Create comprehensive learner profile using all learning models"""
        
        # Create learner profile data
        learner_profile = LearnerProfileData(
            learner_id=learner_id,
            demographics={
                "age_group": "adult",
                "learning_style": "visual_kinesthetic",
                "prior_experience": "intermediate",
                "accessibility_needs": []
            },
            preferences={
                "content_difficulty": "adaptive",
                "interaction_style": "hands_on",
                "feedback_frequency": "moderate",
                "learning_pace": "self_paced"
            }
        )
        
        # Process through learner model
        learner_result = await self.learner_processor.process_learner_profile(learner_profile)
        
        # Create knowledge structure
        knowledge_structure = KnowledgeStructureData(
            knowledge_domain="spatial_mathematics",
            curriculum_units=[
                {
                    "unit_id": "basic_geometry",
                    "prerequisites": [],
                    "learning_objectives": ["understand_3d_shapes", "spatial_reasoning"],
                    "difficulty_level": 3,
                    "estimated_duration_minutes": 45
                },
                {
                    "unit_id": "advanced_transformations", 
                    "prerequisites": ["basic_geometry"],
                    "learning_objectives": ["3d_rotations", "coordinate_systems"],
                    "difficulty_level": 7,
                    "estimated_duration_minutes": 60
                }
            ]
        )
        
        # Process through knowledge model
        knowledge_result = await self.knowledge_processor.process_knowledge_structure(knowledge_structure)
        
        # Create VR interaction data
        vr_interaction = VRInteractionData(
            learner_id=learner_id,
            session_id=f"session_{learner_id}_{int(time.time())}",
            interaction_data={
                "gaze_tracking": {"focus_points": [(0.5, 0.3), (0.7, 0.6)], "attention_duration": 12.5},
                "hand_tracking": {"dominant_hand": "right", "gesture_count": 25, "precision_score": 0.85},
                "movement_tracking": {"position_changes": 45, "spatial_coverage": 0.75},
                "object_interactions": {"objects_touched": 8, "manipulation_quality": 0.80}
            }
        )
        
        # Process through engagement model
        engagement_result = await self.engagement_processor.process_vr_interaction(vr_interaction)
        
        # Create assessment configuration
        assessment_config = AssessmentConfiguration(
            assessment_id=f"comprehensive_assessment_{learner_id}",
            assessment_type="adaptive_spatial_reasoning",
            competency_domains=["spatial_visualization", "mathematical_reasoning", "problem_solving"],
            difficulty_range=(1, 10),
            max_questions=15,
            adaptive_parameters={
                "theta_initial": 0.0,
                "theta_range": (-3.0, 3.0),
                "stopping_criterion": "standard_error"
            }
        )
        
        # Process through assessment model
        assessment_result = await self.assessment_processor.process_assessment_configuration(assessment_config)
        
        # Compile comprehensive profile
        comprehensive_profile = {
            "learner_id": learner_id,
            "learner_data": learner_result,
            "knowledge_data": knowledge_result,
            "engagement_data": engagement_result,
            "assessment_data": assessment_result,
            "profile_created": datetime.now().isoformat(),
            "integration_ready": True
        }
        
        # Store in active learners
        self.active_learners[learner_id] = comprehensive_profile
        
        return comprehensive_profile
    
    async def process_learning_interaction(
        self,
        learner_id: str,
        interaction_type: str,
        interaction_data: Dict[str, Any],
        learning_event: str = "practice"
    ) -> IntegrationResult:
        """
        Process a learning interaction through the complete system
        
        Educational Impact:
        Demonstrates full system integration by processing learner interactions
        through all learning models and generating real-time adaptations.
        """
        
        # Ensure learner profile exists
        if learner_id not in self.active_learners:
            await self.create_comprehensive_learner_profile(learner_id)
        
        learner_profile = self.active_learners[learner_id]
        
        # Create model inputs from comprehensive profile
        model_inputs = LearningModelInputs(
            learner_model_data=learner_profile["learner_data"],
            knowledge_model_data=learner_profile["knowledge_data"],
            engagement_model_data=learner_profile["engagement_data"],
            assessment_model_data=learner_profile["assessment_data"],
            learning_event=learning_event
        )
        
        # Process through integration engine
        integration_result = await self.integration_engine.compute_transition_state(
            learner_id, model_inputs, learning_event
        )
        
        # Create real-time pipeline event
        pipeline_event = await self.real_time_pipeline.create_learner_interaction_event(
            learner_id=learner_id,
            interaction_type=interaction_type,
            interaction_data=interaction_data,
            learning_event=learning_event,
            priority=3
        )
        
        # Submit to pipeline for real-time processing
        pipeline_success = await self.real_time_pipeline.submit_learning_event(pipeline_event)
        
        if not pipeline_success:
            print(f"Warning: Pipeline processing failed for learner {learner_id}")
        
        return integration_result

@pytest.fixture
async def integrated_system():
    """Create and initialize integrated learning system for testing"""
    system = IntegratedLearningSystem()
    await system.initialize_system()
    yield system
    await system.shutdown_system()

class TestComprehensiveIntegration:
    """Test comprehensive integration across all learning models"""
    
    @pytest.mark.asyncio
    async def test_full_system_initialization(self, integrated_system):
        """
        Test that all system components initialize correctly
        
        Educational Impact:
        Validates that the complete educational VR system can be
        initialized and is ready for learning sessions.
        """
        system = integrated_system
        
        # Verify all processors are initialized
        assert system.learner_processor is not None
        assert system.knowledge_processor is not None
        assert system.engagement_processor is not None
        assert system.assessment_processor is not None
        assert system.transition_processor is not None
        
        # Verify integration engine is operational
        assert system.integration_engine is not None
        assert len(system.integration_engine.weight_configurations) == 5
        
        # Verify real-time pipeline is running
        assert system.real_time_pipeline is not None
        assert system.real_time_pipeline.is_running
        
        print("✅ Full system initialization validated")
    
    @pytest.mark.asyncio
    async def test_comprehensive_learner_profile_creation(self, integrated_system):
        """
        Test creation of comprehensive learner profiles using all models
        
        Educational Impact:
        Validates that learner profiles integrate data from all learning
        models for comprehensive educational personalization.
        """
        system = integrated_system
        learner_id = "integration_test_learner_001"
        
        # Create comprehensive profile
        start_time = time.perf_counter()
        profile = await system.create_comprehensive_learner_profile(learner_id)
        end_time = time.perf_counter()
        
        creation_time = (end_time - start_time) * 1000
        
        # Validate profile completeness
        assert profile["learner_id"] == learner_id
        assert "learner_data" in profile
        assert "knowledge_data" in profile
        assert "engagement_data" in profile
        assert "assessment_data" in profile
        assert profile["integration_ready"] is True
        
        # Validate profile is stored in system
        assert learner_id in system.active_learners
        
        # Validate performance (profile creation should be fast)
        assert creation_time < 500.0, f"Profile creation took {creation_time:.2f}ms (too slow)"
        
        print(f"✅ Comprehensive learner profile created in {creation_time:.2f}ms")
    
    @pytest.mark.asyncio
    async def test_learning_interaction_processing(self, integrated_system):
        """
        Test processing of learning interactions through complete system
        
        Educational Impact:
        Validates that learner interactions are processed through all
        learning models and generate appropriate educational adaptations.
        """
        system = integrated_system
        learner_id = "interaction_test_learner_001"
        
        # Create comprehensive profile first
        await system.create_comprehensive_learner_profile(learner_id)
        
        # Test different interaction types
        interaction_scenarios = [
            {
                "type": "vr_gesture",
                "data": {"gesture": "point", "accuracy": 0.85, "confidence": 0.90},
                "learning_event": "practice",
                "expected_adaptation": True
            },
            {
                "type": "gaze_focus",
                "data": {"focus_duration": 8.5, "attention_quality": 0.75},
                "learning_event": "application", 
                "expected_adaptation": True
            },
            {
                "type": "object_manipulation",
                "data": {"manipulation_type": "rotate", "precision": 0.92, "time_to_complete": 4.2},
                "learning_event": "mastery",
                "expected_adaptation": True
            }
        ]
        
        interaction_results = []
        
        for scenario in interaction_scenarios:
            start_time = time.perf_counter()
            
            result = await system.process_learning_interaction(
                learner_id=learner_id,
                interaction_type=scenario["type"],
                interaction_data=scenario["data"],
                learning_event=scenario["learning_event"]
            )
            
            end_time = time.perf_counter()
            processing_time = (end_time - start_time) * 1000
            
            # Validate integration result
            assert isinstance(result, IntegrationResult)
            assert result.learner_id == learner_id
            assert result.learning_event == scenario["learning_event"]
            assert 0.0 <= result.transition_state <= 1.0
            assert result.computation_time_ms < 10.0  # Quest 3 requirement
            
            # Validate educational decisions
            assert result.transition_decision is not None
            assert "recommended_action" in result.transition_decision
            assert "confidence_score" in result.transition_decision
            assert "educational_recommendations" in result.transition_decision
            
            interaction_results.append({
                "scenario": scenario["type"],
                "processing_time_ms": processing_time,
                "transition_state": result.transition_state,
                "recommended_action": result.recommended_action,
                "computation_time_ms": result.computation_time_ms
            })
            
            print(f"Processed {scenario['type']}: {result.transition_state:.3f} in {processing_time:.2f}ms")
        
        # Validate overall processing performance
        avg_processing_time = sum(r["processing_time_ms"] for r in interaction_results) / len(interaction_results)
        avg_computation_time = sum(r["computation_time_ms"] for r in interaction_results) / len(interaction_results)
        
        assert avg_processing_time < 50.0, f"Average processing time {avg_processing_time:.2f}ms too high"
        assert avg_computation_time < 8.0, f"Average computation time {avg_computation_time:.2f}ms too high"
        
        print(f"✅ Learning interactions processed (avg: {avg_processing_time:.2f}ms total, {avg_computation_time:.2f}ms computation)")
    
    @pytest.mark.asyncio
    async def test_mathematical_equation_integration(self, integrated_system):
        """
        Test mathematical learning equation integration across all models
        
        Educational Impact:
        Validates that the mathematical learning equation correctly integrates
        data from all five learning models for optimal educational decisions.
        """
        system = integrated_system
        
        # Test learners with different characteristics
        test_learners = [
            {
                "id": "high_performer",
                "learning_style": "visual_kinesthetic",
                "prior_experience": "advanced",
                "expected_transition_range": (0.6, 1.0)
            },
            {
                "id": "average_learner",
                "learning_style": "auditory",
                "prior_experience": "intermediate",
                "expected_transition_range": (0.4, 0.8)
            },
            {
                "id": "struggling_learner",
                "learning_style": "kinesthetic",
                "prior_experience": "beginner",
                "expected_transition_range": (0.0, 0.6)
            }
        ]
        
        equation_results = []
        
        for learner_spec in test_learners:
            learner_id = f"equation_test_{learner_spec['id']}"
            
            # Create profile for this learner
            await system.create_comprehensive_learner_profile(learner_id)
            
            # Process multiple interactions to see equation progression
            transition_states = []
            
            for interaction_num in range(10):
                result = await system.process_learning_interaction(
                    learner_id=learner_id,
                    interaction_type="comprehensive_interaction",
                    interaction_data={
                        "performance_quality": 0.7 + (interaction_num * 0.02),  # Gradual improvement
                        "engagement_level": 0.65 + (interaction_num * 0.015),
                        "interaction_number": interaction_num
                    },
                    learning_event="practice"
                )
                
                transition_states.append(result.transition_state)
            
            # Analyze equation behavior
            initial_state = transition_states[0]
            final_state = transition_states[-1]
            state_progression = final_state - initial_state
            
            min_expected, max_expected = learner_spec["expected_transition_range"]
            
            # Validate equation produces appropriate results
            assert min_expected <= final_state <= max_expected, \
                f"Final state {final_state:.3f} outside expected range {learner_spec['expected_transition_range']}"
            
            # Should show progression (or at least not regression)
            assert state_progression >= -0.1, f"Significant regression detected: {state_progression:.3f}"
            
            equation_results.append({
                "learner_type": learner_spec["id"],
                "initial_state": initial_state,
                "final_state": final_state,
                "progression": state_progression,
                "within_expected_range": min_expected <= final_state <= max_expected
            })
            
            print(f"{learner_spec['id']}: {initial_state:.3f} → {final_state:.3f} (Δ{state_progression:+.3f})")
        
        # Validate overall equation behavior
        all_within_range = all(r["within_expected_range"] for r in equation_results)
        assert all_within_range, "Some learners outside expected transition ranges"
        
        print("✅ Mathematical equation integration validated across learner types")
    
    @pytest.mark.asyncio
    async def test_real_time_pipeline_integration(self, integrated_system):
        """
        Test real-time pipeline integration with learning models
        
        Educational Impact:
        Validates that real-time processing maintains educational effectiveness
        while meeting VR performance requirements.
        """
        system = integrated_system
        
        # Create multiple learners for concurrent processing
        num_learners = 15
        learner_ids = []
        
        for i in range(num_learners):
            learner_id = f"pipeline_test_learner_{i:03d}"
            await system.create_comprehensive_learner_profile(learner_id)
            learner_ids.append(learner_id)
        
        # Generate concurrent learning events
        total_events = 100
        events_submitted = 0
        events_processed = 0
        
        start_time = time.perf_counter()
        
        # Submit events concurrently
        for event_num in range(total_events):
            learner_id = learner_ids[event_num % num_learners]
            
            # Process interaction through system
            try:
                result = await system.process_learning_interaction(
                    learner_id=learner_id,
                    interaction_type="pipeline_test",
                    interaction_data={
                        "event_number": event_num,
                        "interaction_quality": 0.6 + (event_num % 10) * 0.04,
                        "timestamp": datetime.now().isoformat()
                    },
                    learning_event="practice"
                )
                
                events_submitted += 1
                
                if result.computation_time_ms < 10.0:
                    events_processed += 1
                
            except Exception as e:
                print(f"Event {event_num} failed: {e}")
        
        end_time = time.perf_counter()
        total_time = end_time - start_time
        
        # Get pipeline metrics
        pipeline_metrics = system.real_time_pipeline.get_pipeline_metrics()
        
        # Calculate performance metrics
        throughput = events_submitted / total_time
        success_rate = (events_processed / events_submitted) * 100 if events_submitted > 0 else 0
        
        print(f"\n=== Real-time Pipeline Integration Report ===")
        print(f"Events submitted: {events_submitted}/{total_events}")
        print(f"Events processed successfully: {events_processed}")
        print(f"Success rate: {success_rate:.1f}%")
        print(f"Throughput: {throughput:.1f} events/second")
        print(f"Average latency: {pipeline_metrics['performance_metrics']['average_latency_ms']:.2f}ms")
        print(f"Active learners: {pipeline_metrics['system_metrics']['active_learners']}")
        
        # Performance assertions
        assert events_submitted >= total_events * 0.95, f"Only {events_submitted}/{total_events} events submitted"
        assert success_rate >= 95.0, f"Success rate {success_rate:.1f}% too low"
        assert throughput >= 20.0, f"Throughput {throughput:.1f} events/s too low"
        assert pipeline_metrics['performance_metrics']['average_latency_ms'] <= 25.0, "Pipeline latency too high"
        
        print("✅ Real-time pipeline integration validated")
    
    @pytest.mark.asyncio
    async def test_learning_progression_across_events(self, integrated_system):
        """
        Test learning progression across different learning events
        
        Educational Impact:
        Validates that learners can progress through learning events
        (onboarding → introduction → practice → application → mastery)
        with appropriate educational guidance.
        """
        system = integrated_system
        learner_id = "progression_test_learner"
        
        # Create comprehensive profile
        await system.create_comprehensive_learner_profile(learner_id)
        
        # Define learning event progression
        learning_events = ["onboarding", "introduction", "practice", "application", "mastery"]
        progression_results = []
        
        for event_index, learning_event in enumerate(learning_events):
            # Simulate performance improvement over time
            base_performance = 0.4 + (event_index * 0.15)  # Gradual improvement
            
            event_results = []
            
            # Process multiple interactions in this learning event
            for interaction in range(8):
                interaction_performance = base_performance + (interaction * 0.02)
                
                result = await system.process_learning_interaction(
                    learner_id=learner_id,
                    interaction_type="progression_test",
                    interaction_data={
                        "performance_level": interaction_performance,
                        "learning_event": learning_event,
                        "interaction_index": interaction
                    },
                    learning_event=learning_event
                )
                
                event_results.append({
                    "interaction": interaction,
                    "transition_state": result.transition_state,
                    "recommended_action": result.recommended_action,
                    "confidence_score": result.confidence_score
                })
            
            # Analyze progression within event
            initial_state = event_results[0]["transition_state"]
            final_state = event_results[-1]["transition_state"]
            within_event_progression = final_state - initial_state
            
            progression_results.append({
                "learning_event": learning_event,
                "initial_state": initial_state,
                "final_state": final_state,
                "progression": within_event_progression,
                "interactions": len(event_results),
                "avg_confidence": sum(r["confidence_score"] for r in event_results) / len(event_results)
            })
            
            print(f"{learning_event}: {initial_state:.3f} → {final_state:.3f} (Δ{within_event_progression:+.3f})")
        
        # Validate overall learning progression
        overall_initial = progression_results[0]["initial_state"]
        overall_final = progression_results[-1]["final_state"]
        overall_progression = overall_final - overall_initial
        
        print(f"\nOverall progression: {overall_initial:.3f} → {overall_final:.3f} (Δ{overall_progression:+.3f})")
        
        # Assertions for educational progression
        assert overall_progression > 0.2, f"Insufficient overall progression: {overall_progression:.3f}"
        assert overall_final > overall_initial, "No improvement across learning events"
        
        # Each event should show some progression or maintenance
        for result in progression_results:
            assert result["progression"] >= -0.05, f"Significant regression in {result['learning_event']}"
            assert result["avg_confidence"] >= 0.4, f"Low confidence in {result['learning_event']}"
        
        print("✅ Learning progression across events validated")
    
    @pytest.mark.asyncio
    async def test_adaptive_difficulty_adjustment(self, integrated_system):
        """
        Test adaptive difficulty adjustment based on learner performance
        
        Educational Impact:
        Validates that the system automatically adjusts difficulty based
        on learner performance to maintain optimal challenge levels.
        """
        system = integrated_system
        
        # Test scenarios with different performance patterns
        adaptation_scenarios = [
            {
                "name": "consistently_high_performance",
                "performance_pattern": [0.85, 0.88, 0.90, 0.87, 0.92, 0.89, 0.91, 0.94],
                "expected_adaptation": "increase_difficulty"
            },
            {
                "name": "consistently_low_performance", 
                "performance_pattern": [0.25, 0.22, 0.28, 0.20, 0.26, 0.24, 0.27, 0.23],
                "expected_adaptation": "decrease_difficulty"
            },
            {
                "name": "variable_performance",
                "performance_pattern": [0.60, 0.45, 0.70, 0.55, 0.65, 0.50, 0.68, 0.58],
                "expected_adaptation": "maintain_difficulty"
            }
        ]
        
        adaptation_results = []
        
        for scenario in adaptation_scenarios:
            learner_id = f"adaptation_test_{scenario['name']}"
            await system.create_comprehensive_learner_profile(learner_id)
            
            scenario_results = []
            
            for performance in scenario["performance_pattern"]:
                result = await system.process_learning_interaction(
                    learner_id=learner_id,
                    interaction_type="performance_test",
                    interaction_data={
                        "performance_score": performance,
                        "difficulty_context": "adaptive_test"
                    },
                    learning_event="practice"
                )
                
                # Extract adaptive parameters
                adaptive_params = result.transition_decision.get("adaptive_parameters", {})
                difficulty_adjustment = adaptive_params.get("difficulty_adjustment", 1.0)
                
                scenario_results.append({
                    "performance": performance,
                    "transition_state": result.transition_state,
                    "difficulty_adjustment": difficulty_adjustment,
                    "recommended_action": result.recommended_action
                })
            
            # Analyze adaptation pattern
            avg_performance = sum(r["performance"] for r in scenario_results) / len(scenario_results)
            final_difficulty = scenario_results[-1]["difficulty_adjustment"]
            
            # Determine actual adaptation
            if final_difficulty > 1.1:
                actual_adaptation = "increase_difficulty"
            elif final_difficulty < 0.9:
                actual_adaptation = "decrease_difficulty"
            else:
                actual_adaptation = "maintain_difficulty"
            
            adaptation_match = actual_adaptation == scenario["expected_adaptation"]
            
            adaptation_results.append({
                "scenario": scenario["name"],
                "avg_performance": avg_performance,
                "final_difficulty": final_difficulty,
                "expected_adaptation": scenario["expected_adaptation"],
                "actual_adaptation": actual_adaptation,
                "adaptation_match": adaptation_match
            })
            
            print(f"{scenario['name']}: {avg_performance:.2f} performance → {actual_adaptation} (expected: {scenario['expected_adaptation']})")
        
        # Validate adaptive behavior
        adaptation_accuracy = sum(1 for r in adaptation_results if r["adaptation_match"]) / len(adaptation_results)
        
        print(f"\nAdaptive difficulty accuracy: {adaptation_accuracy:.1%}")
        
        assert adaptation_accuracy >= 0.67, f"Adaptive accuracy {adaptation_accuracy:.1%} too low"  # At least 2/3 correct
        
        print("✅ Adaptive difficulty adjustment validated")

# Comprehensive system validation test
@pytest.mark.asyncio 
async def test_complete_system_validation():
    """
    Complete Phase 3 system validation test
    
    Educational Impact:
    Comprehensive validation that the complete Phase 3 system meets
    all educational, performance, and integration requirements for
    production educational VR deployment.
    """
    print("\n" + "="*70)
    print("PHASE 3 COMPLETE SYSTEM VALIDATION")
    print("="*70)
    
    # Initialize complete system
    system = IntegratedLearningSystem()
    await system.initialize_system()
    
    try:
        # Test comprehensive learner scenario
        num_test_learners = 10
        interactions_per_learner = 20
        total_interactions = num_test_learners * interactions_per_learner
        
        print(f"Testing {num_test_learners} learners with {interactions_per_learner} interactions each")
        print(f"Total interactions: {total_interactions}")
        
        # Create test learners
        test_learners = []
        for i in range(num_test_learners):
            learner_id = f"complete_validation_learner_{i:03d}"
            await system.create_comprehensive_learner_profile(learner_id)
            test_learners.append(learner_id)
        
        # Process all interactions
        start_time = time.perf_counter()
        successful_interactions = 0
        performance_metrics = []
        
        for learner_idx, learner_id in enumerate(test_learners):
            learner_start = time.perf_counter()
            
            for interaction_num in range(interactions_per_learner):
                try:
                    interaction_start = time.perf_counter()
                    
                    result = await system.process_learning_interaction(
                        learner_id=learner_id,
                        interaction_type="validation_test",
                        interaction_data={
                            "learner_index": learner_idx,
                            "interaction_number": interaction_num,
                            "performance_variance": 0.6 + (interaction_num % 5) * 0.08,
                            "engagement_level": 0.7 + (interaction_num % 3) * 0.05
                        },
                        learning_event=["practice", "application"][interaction_num % 2]
                    )
                    
                    interaction_end = time.perf_counter()
                    interaction_time = (interaction_end - interaction_start) * 1000
                    
                    # Validate result quality
                    if (0.0 <= result.transition_state <= 1.0 and
                        result.computation_time_ms < 10.0 and
                        interaction_time < 50.0):
                        successful_interactions += 1
                        performance_metrics.append({
                            "computation_time": result.computation_time_ms,
                            "total_time": interaction_time,
                            "transition_state": result.transition_state,
                            "confidence": result.confidence_score
                        })
                
                except Exception as e:
                    print(f"Interaction failed for {learner_id}[{interaction_num}]: {e}")
            
            learner_end = time.perf_counter()
            learner_time = learner_end - learner_start
            print(f"Learner {learner_idx + 1}/{num_test_learners} completed in {learner_time:.2f}s")
        
        end_time = time.perf_counter()
        total_time = end_time - start_time
        
        # Calculate comprehensive metrics
        success_rate = (successful_interactions / total_interactions) * 100
        throughput = total_interactions / total_time
        
        if performance_metrics:
            avg_computation_time = sum(m["computation_time"] for m in performance_metrics) / len(performance_metrics)
            avg_total_time = sum(m["total_time"] for m in performance_metrics) / len(performance_metrics)
            avg_confidence = sum(m["confidence"] for m in performance_metrics) / len(performance_metrics)
        else:
            avg_computation_time = avg_total_time = avg_confidence = 0.0
        
        # Get system metrics
        pipeline_metrics = system.real_time_pipeline.get_pipeline_metrics()
        integration_metrics = await system.integration_engine.get_performance_metrics()
        
        # Generate comprehensive report
        print(f"\n=== COMPLETE SYSTEM VALIDATION REPORT ===")
        print(f"Total test time: {total_time:.2f}s")
        print(f"Total interactions: {total_interactions}")
        print(f"Successful interactions: {successful_interactions}")
        print(f"Success rate: {success_rate:.1f}%")
        print(f"Throughput: {throughput:.1f} interactions/second")
        print(f"")
        print(f"PERFORMANCE METRICS:")
        print(f"  Average computation time: {avg_computation_time:.2f}ms")
        print(f"  Average total time: {avg_total_time:.2f}ms")
        print(f"  Average confidence: {avg_confidence:.3f}")
        print(f"")
        print(f"SYSTEM METRICS:")
        print(f"  Pipeline latency: {pipeline_metrics['performance_metrics']['average_latency_ms']:.2f}ms")
        print(f"  Pipeline success rate: {pipeline_metrics['performance_metrics']['success_rate_percent']:.1f}%")
        print(f"  Active learners: {pipeline_metrics['system_metrics']['active_learners']}")
        print(f"  Integration engine compliance: {integration_metrics['quest3_compliance']['status']}")
        
        # Final validation assertions
        print(f"\n=== VALIDATION RESULTS ===")
        
        # Success rate requirement
        success_requirement_met = success_rate >= 95.0
        print(f"✓ Success rate ≥95%: {success_requirement_met} ({success_rate:.1f}%)")
        assert success_requirement_met, f"Success rate {success_rate:.1f}% below requirement"
        
        # Performance requirements
        computation_requirement_met = avg_computation_time < 10.0
        print(f"✓ Computation <10ms: {computation_requirement_met} ({avg_computation_time:.2f}ms)")
        assert computation_requirement_met, f"Computation time {avg_computation_time:.2f}ms exceeds requirement"
        
        total_time_requirement_met = avg_total_time < 50.0
        print(f"✓ Total processing <50ms: {total_time_requirement_met} ({avg_total_time:.2f}ms)")
        assert total_time_requirement_met, f"Total time {avg_total_time:.2f}ms exceeds requirement"
        
        # Throughput requirement
        throughput_requirement_met = throughput >= 10.0
        print(f"✓ Throughput ≥10 interactions/s: {throughput_requirement_met} ({throughput:.1f}/s)")
        assert throughput_requirement_met, f"Throughput {throughput:.1f}/s below requirement"
        
        # System integration requirements
        integration_requirement_met = integration_metrics['quest3_compliance']['status'] == 'compliant'
        print(f"✓ Quest 3 compliance: {integration_requirement_met}")
        assert integration_requirement_met, "Quest 3 compliance not met"
        
        print(f"\n🎉 PHASE 3 COMPLETE SYSTEM VALIDATION SUCCESSFUL!")
        print(f"🎉 ALL EDUCATIONAL VR REQUIREMENTS VALIDATED!")
        print(f"🎉 READY FOR PRODUCTION DEPLOYMENT!")
        
    finally:
        await system.shutdown_system()

if __name__ == "__main__":
    # Run complete system validation
    asyncio.run(test_complete_system_validation())
