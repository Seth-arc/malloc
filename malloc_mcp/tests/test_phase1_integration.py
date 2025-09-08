"""
Phase 1 Integration Tests
Comprehensive integration testing for Phase 1 foundation architecture.

This module tests the complete Phase 1 implementation including MCP server,
security manager, configuration, and learning calculations.

Educational Impact:
Integration testing ensures that all Phase 1 components work together
correctly to provide reliable educational VR learning experiences.

Test Coverage:
- MCP server initialization
- Security manager functionality
- Configuration validation
- Learning calculations
- Database operations
- Performance monitoring

Authors: Malloc VR Learning Team
Version: 2.0.0
Last Updated: December 2024
License: Educational Use License
"""

import asyncio
import json
import pytest
from typing import Dict, Any
import tempfile
import os

# Test imports
from src.mcp.server_configuration import MCPServerConfiguration, ConfigurationManager
from src.security.educational_security import (
    EducationalSecurityManager, EncryptionContext, DataAccessLevel
)
from src.mcp.malloc_vr_mcp_server import MallocVRMCPServer
from src.utils.learning_calculations import (
    calculate_learner_model_weight, calculate_engagement_score,
    LearningEquationCalculator
)


class TestPhase1Integration:
    """Integration tests for Phase 1 foundation architecture."""
    
    @pytest.fixture
    async def test_config(self):
        """Create test configuration with temporary database."""
        with tempfile.NamedTemporaryFile(suffix='.db', delete=False) as tmp_db:
            config = MCPServerConfiguration(
                database_path=tmp_db.name,
                debug_mode=True,
                max_concurrent_learners=5,
                cache_enabled=True,
                ferpa_compliance_enabled=True
            )
            yield config
            # Cleanup
            if os.path.exists(tmp_db.name):
                os.unlink(tmp_db.name)
    
    @pytest.fixture
    async def security_manager(self, test_config):
        """Create test security manager."""
        return EducationalSecurityManager(test_config)
    
    @pytest.fixture
    async def mcp_server(self, test_config):
        """Create test MCP server."""
        return MallocVRMCPServer(test_config)
    
    async def test_configuration_validation(self, test_config):
        """Test configuration validation and settings."""
        # Test configuration validation
        test_config.validate_configuration()
        
        # Test Quest 3 optimized settings
        quest3_settings = test_config.get_quest3_optimized_settings()
        assert quest3_settings["frame_rate_minimum"] >= 72
        assert quest3_settings["memory_limit_mb"] <= 100
        assert quest3_settings["spatial_precision_mm"] == 0.1
        
        # Test FERPA compliance settings
        ferpa_settings = test_config.get_ferpa_compliance_settings()
        assert ferpa_settings["enabled"] is True
        assert ferpa_settings["encryption_enabled"] is True
        assert ferpa_settings["audit_logging"] is True
        
        # Test performance thresholds
        thresholds = test_config.get_performance_thresholds()
        assert thresholds["learner_model_processing"] == 100
        assert thresholds["encryption_operation"] == 50
    
    async def test_security_manager_functionality(self, security_manager):
        """Test security manager encryption and audit features."""
        # Test learner data encryption
        test_learner_data = {
            "learner_id": "test_student_123",
            "static_profile": {
                "demographic": {
                    "age": 20,
                    "location": "New York, NY",
                    "education_level": "undergraduate"
                }
            }
        }
        
        encryption_context = EncryptionContext(
            data_type="test_learner_profile",
            access_level=DataAccessLevel.EDUCATIONAL
        )
        
        # Test encryption
        encrypted_data = await security_manager.encrypt_learner_data(
            test_learner_data, encryption_context
        )
        assert isinstance(encrypted_data, str)
        assert len(encrypted_data) > 0
        
        # Test decryption
        decrypted_result = await security_manager.decrypt_learner_data(encrypted_data)
        assert decrypted_result["data"]["learner_id"] == "test_student_123"
        
        # Test anonymization
        anonymized_data = await security_manager.anonymize_learner_identifiers(test_learner_data)
        assert anonymized_data["learner_id"] != "test_student_123"
        assert anonymized_data["learner_id"].startswith("anon_")
        
        # Test audit logs
        audit_logs = await security_manager.get_audit_logs(
            learner_id=test_learner_data["learner_id"]
        )
        assert len(audit_logs) >= 2  # Encryption and decryption events
    
    async def test_mcp_server_initialization(self, mcp_server):
        """Test MCP server initialization and component setup."""
        # Test server initialization
        init_result = await mcp_server.initialize_server()
        
        assert init_result["ready_for_learning_sessions"] is True
        assert "server_id" in init_result
        assert init_result["ferpa_compliance"] is True
        assert init_result["max_concurrent_learners"] == 5
        
        # Test Blender integration status
        blender_status = init_result["blender_integration"]
        assert "available" in blender_status
        
        # Test security validation
        security_status = init_result["security_validation"]
        assert security_status["encryption_working"] is True
        assert security_status["ferpa_compliance_enabled"] is True
    
    async def test_learning_calculations(self):
        """Test learning calculation utilities."""
        # Test learner model weight calculation
        static_profile = {
            "demographic": {
                "current_knowledge_level": "beginner",
                "age_range": "18-25",
                "education_level": "undergraduate"
            },
            "learning_preferences": {
                "guidance_level": "moderate",
                "interaction_style": "guided"
            }
        }
        
        dynamic_profile = {
            "learning_history": {},
            "behavioral_patterns": {}
        }
        
        learner_weight = await calculate_learner_model_weight(static_profile, dynamic_profile)
        assert 0.25 <= learner_weight <= 0.40
        
        # Test engagement score calculation
        interaction_data = {
            "duration_minutes": 20,
            "interaction_count": 25,
            "attention_metrics": {
                "focus_duration": 18,
                "distraction_events": 2
            },
            "motivation_indicators": {
                "task_completion_rate": 0.8,
                "retry_attempts": 3,
                "help_seeking_frequency": 2
            }
        }
        
        engagement_score = await calculate_engagement_score(interaction_data)
        assert 0.0 <= engagement_score <= 1.0
        
        # Test learning equation calculator
        calculator = LearningEquationCalculator()
        
        current_state = {"transition_value": 0.5}
        learner_model = {"weight": 0.35}
        knowledge_model = {"weight": 0.25}
        engagement_model = {"weight": 0.20}
        assessment_model = {"weight": 0.20}
        
        equation_result = await calculator.calculate_learning_equation(
            current_state, learner_model, knowledge_model,
            engagement_model, assessment_model
        )
        
        assert "transition_value" in equation_result
        assert "confidence" in equation_result
        assert "model_integration" in equation_result
        assert 0.0 <= equation_result["transition_value"] <= 1.0
        assert 0.0 <= equation_result["confidence"] <= 1.0
    
    async def test_tool_processing_integration(self, mcp_server):
        """Test MCP tool processing with real data."""
        # Initialize server
        await mcp_server.initialize_server()
        
        # Test learner model processing
        learner_args = {
            "learner_id": "integration_test_student",
            "static_profile": {
                "demographic": {
                    "age_range": "18-25",
                    "education_level": "undergraduate",
                    "current_knowledge_level": "intermediate"
                },
                "learning_preferences": {
                    "guidance_level": "moderate",
                    "interaction_style": "guided",
                    "time_commitment": 30
                }
            },
            "dynamic_profile": {
                "learning_history": {},
                "behavioral_patterns": {}
            }
        }
        
        learner_result = await mcp_server.handle_learner_model_processing(learner_args)
        assert learner_result["status"] == "success"
        assert "learner_model_weight" in learner_result
        assert "adaptation_parameters" in learner_result
        
        # Test engagement tracking
        engagement_args = {
            "session_id": "test_session_123",
            "learner_id": "integration_test_student",
            "interaction_data": {
                "duration_minutes": 25,
                "interaction_count": 30,
                "attention_metrics": {
                    "focus_duration": 22,
                    "distraction_events": 1
                },
                "motivation_indicators": {
                    "task_completion_rate": 0.9,
                    "retry_attempts": 2,
                    "help_seeking_frequency": 1
                }
            }
        }
        
        engagement_result = await mcp_server.handle_engagement_tracking(engagement_args)
        assert engagement_result["status"] == "success"
        assert "engagement_score" in engagement_result
        assert "engagement_model_weight" in engagement_result
        
        # Test transition decision
        transition_args = {
            "learner_id": "integration_test_student",
            "current_state": {
                "current_learning_event": "practice",
                "progress_percentage": 75
            },
            "model_inputs": {
                "learner_model_output": learner_result,
                "knowledge_model_output": {"weight": 0.25},
                "engagement_model_output": engagement_result,
                "assessment_model_output": {"weight": 0.20}
            }
        }
        
        transition_result = await mcp_server.handle_transition_decision(transition_args)
        assert transition_result["status"] == "success"
        assert "next_learning_event" in transition_result
        assert "transition_confidence" in transition_result
    
    async def test_performance_monitoring(self, mcp_server):
        """Test performance monitoring and validation."""
        # Initialize server
        await mcp_server.initialize_server()
        
        # Test performance metrics initialization
        assert mcp_server.performance_metrics.total_requests == 0
        assert mcp_server.performance_metrics.average_response_time_ms == 0.0
        
        # Simulate tool execution and performance tracking
        await mcp_server.update_performance_metrics("test_tool", 50.0, True)
        
        assert mcp_server.performance_metrics.total_requests == 1
        assert mcp_server.performance_metrics.average_response_time_ms == 50.0
        assert mcp_server.performance_metrics.error_rate == 0.0
        
        # Test performance validation
        await mcp_server.validate_performance_requirements("test_tool", 50.0)
        # Should not raise any exceptions for good performance
        
        # Test cache functionality
        cache_key = "test_cache_key"
        test_data = {"test": "data"}
        
        await mcp_server._store_in_cache(cache_key, test_data, 60)
        cached_result = await mcp_server._get_from_cache(cache_key)
        
        assert cached_result is not None
        assert cached_result["data"]["test"] == "data"


# Test utilities
async def run_integration_tests():
    """Run all Phase 1 integration tests."""
    test_instance = TestPhase1Integration()
    
    # Create test configuration
    with tempfile.NamedTemporaryFile(suffix='.db', delete=False) as tmp_db:
        config = MCPServerConfiguration(
            database_path=tmp_db.name,
            debug_mode=True,
            max_concurrent_learners=5
        )
        
        try:
            # Run tests
            print("Running Phase 1 Integration Tests...")
            
            await test_instance.test_configuration_validation(config)
            print("✓ Configuration validation test passed")
            
            security_manager = EducationalSecurityManager(config)
            await test_instance.test_security_manager_functionality(security_manager)
            print("✓ Security manager test passed")
            
            mcp_server = MallocVRMCPServer(config)
            await test_instance.test_mcp_server_initialization(mcp_server)
            print("✓ MCP server initialization test passed")
            
            await test_instance.test_learning_calculations()
            print("✓ Learning calculations test passed")
            
            await test_instance.test_tool_processing_integration(mcp_server)
            print("✓ Tool processing integration test passed")
            
            await test_instance.test_performance_monitoring(mcp_server)
            print("✓ Performance monitoring test passed")
            
            print("\n🎉 All Phase 1 integration tests passed!")
            print("Foundation architecture is ready for Phase 2")
            
        finally:
            # Cleanup
            if os.path.exists(tmp_db.name):
                os.unlink(tmp_db.name)


if __name__ == "__main__":
    asyncio.run(run_integration_tests())
