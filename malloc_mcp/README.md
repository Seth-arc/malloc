# Malloc VR MCP Server

Enterprise-grade Educational VR MCP Server with Real-time Adaptive Learning

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Blender 4.4+](https://img.shields.io/badge/blender-4.4+-orange.svg)](https://www.blender.org/download/)
[![Quest 3 Optimized](https://img.shields.io/badge/quest_3-optimized-green.svg)](https://www.meta.com/quest/quest-3/)
[![FERPA Compliant](https://img.shields.io/badge/FERPA-compliant-red.svg)](https://www2.ed.gov/policy/gen/guid/fpco/ferpa/index.html)

## Overview

The Malloc VR MCP Server is an advanced educational learning system implementing real-time adaptive VR learning experiences with mathematical model computation. It provides a comprehensive platform for personalized educational VR content delivery with FERPA-compliant security.

### Core Features

- **Real-time Learning Adaptation** with mathematical model computation
- **Five Learning Model APIs**: Learner (∩), Knowledge (∆), Engagement (E), Assessment (A), Transition (∂)
- **WebSocket Communication Protocol** for real-time educational interactions  
- **FERPA-Compliant Security** with educational data protection
- **Blender 4.4+ Integration** with Python API optimization for Quest 3 VR
- **Enterprise-grade Performance** with <100ms response times

### Mathematical Foundation

The system implements the core learning equation:

```
∂(t+1) = ∂(t) + α · Δ(∩(t), ∆(t), E(t), A(t)) + β · ε(t)
```

Where:
- `∩(t)` = Learner Model at time t
- `∆(t)` = Knowledge Model at time t
- `E(t)` = Engagement Model at time t  
- `A(t)` = Assessment Model at time t
- `α` = Adaptation strength parameter [0.1-1.0]
- `β` = Environmental noise factor [0.0-0.5]
- `ε(t)` = Environmental factors at time t

## Quick Start

### Prerequisites

- Python 3.11+ (required for Blender 4.4 compatibility)
- Blender 4.4+ (optional, for VR content creation)
- Quest 3 VR headset (recommended target platform)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/malloc-vr/malloc-vr-mcp-server.git
   cd malloc-vr-mcp-server
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Initialize the server:**
   ```bash
   python -m src.main
   ```

### Configuration

The server supports configuration via environment variables:

```bash
# Server Configuration
export MALLOC_VR_SERVER_NAME="my-learning-server"
export MALLOC_VR_MAX_LEARNERS=25
export MALLOC_VR_DEBUG=true

# Security Configuration  
export MALLOC_VR_FERPA_ENABLED=true
export MALLOC_VR_DATABASE_PATH="data/learning.db"

# Performance Configuration
export MALLOC_VR_CACHE_ENABLED=true
export MALLOC_VR_BLENDER_INTEGRATION=true
```

## Architecture

### Project Structure

```
src/
├── mcp/                    # MCP protocol implementation
│   ├── server_configuration.py
│   └── malloc_vr_mcp_server.py
├── learning/               # Learning model APIs (∩, ∆, E, A, ∂)
├── websocket/              # Real-time communication
├── security/               # FERPA-compliant security
│   └── educational_security.py
├── blender/                # Blender 4.4+ integration
├── utils/                  # Utility functions
│   └── learning_calculations.py
└── main.py                 # Main entry point

docs/                       # Documentation
tests/                      # Test suites
requirements.txt            # Python dependencies
```

### Learning Model APIs

The server provides 9 core educational tools via MCP protocol:

#### Core Learning Models
1. **`process_learner_model`** - Process learner profiles for personalization
2. **`process_knowledge_model`** - Organize curriculum structure and content
3. **`track_engagement`** - Monitor VR interactions and motivation
4. **`evaluate_assessment`** - Process competency-based assessments
5. **`make_transition_decision`** - Calculate learning progression decisions

#### Blender VR Integration
6. **`create_blender_knowledge_node`** - Create VR learning scenes
7. **`create_assessment_trigger`** - Add spatial assessment triggers
8. **`update_blender_scene_metadata`** - Real-time scene adaptation
9. **`track_blender_interaction`** - Monitor 3D spatial learning

## Performance Requirements

### Quest 3 VR Optimization
- **Minimum 72fps** maintained during all operations
- **Memory usage**: <100MB for basic server operations
- **Response latency**: <100ms for learning model updates
- **Spatial precision**: 0.1mm tolerance for educational objects

### Real-time Requirements
- **WebSocket latency**: <25ms for real-time adaptation
- **Data streaming**: 5-second intervals for continuous learning data
- **Concurrent connections**: Support 50+ simultaneous learners
- **Mathematical computation**: <100ms for learning equation processing

## Security & Compliance

### FERPA Compliance
- **Educational data protection** for all learner information
- **Secure data transmission** with encryption
- **Access control** with role-based permissions
- **Audit logging** for all educational data access
- **Data retention policies** following educational standards

### Security Features
- End-to-end encryption for learner data
- JWT-based session management
- k-anonymity principles for data anonymization
- Comprehensive audit trails
- Zero-trust security model

## Development

### Code Quality Standards

The project follows enterprise-grade development standards:

- **ESLint Compliance**: Educational-VR plugin rules
- **TypeScript Strict Mode**: Explicit return types required
- **JSDoc Documentation**: 100% coverage for public APIs
- **Testing Standards**: >95% coverage for educational components
- **Performance Monitoring**: Quest 3 VR metrics validation

### Testing

Run the test suite:

```bash
# Unit tests
pytest tests/unit/

# Integration tests  
pytest tests/integration/

# Performance tests
pytest tests/performance/

# Educational effectiveness tests
pytest tests/educational/
```

### Documentation

Generate API documentation:

```bash
# Generate JSDoc documentation
npm run docs

# View documentation
open docs/api/index.html
```

## Educational Impact

The Malloc VR MCP Server enables:

- **Personalized Learning Paths** through real-time adaptation
- **Spatial Learning Validation** for VR environments
- **Competency-Based Assessment** with objective measurement
- **Collaborative Learning Support** for multiple learners
- **Learning Analytics** with comprehensive data collection

### Learning Events Progression

The system guides learners through five progressive learning events:

1. **Onboarding** - Initial orientation and setup
2. **Introduction** - Core concept presentation
3. **Practice** - Guided skill development
4. **Application** - Independent problem solving
5. **Mastery** - Advanced competency demonstration

## API Reference

### MCP Tool Examples

#### Process Learner Model
```json
{
  "tool": "process_learner_model",
  "arguments": {
    "learner_id": "student_123",
    "static_profile": {
      "demographic": {
        "age_range": "18-25",
        "education_level": "undergraduate",
        "current_knowledge_level": "beginner"
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
}
```

#### Make Transition Decision
```json
{
  "tool": "make_transition_decision", 
  "arguments": {
    "learner_id": "student_123",
    "current_state": {
      "current_learning_event": "practice",
      "progress_percentage": 75
    },
    "model_inputs": {
      "learner_model_output": {"weight": 0.35},
      "knowledge_model_output": {"weight": 0.25},
      "engagement_model_output": {"weight": 0.20},
      "assessment_model_output": {"weight": 0.20}
    }
  }
}
```

## Contributing 

We welcome contributions to the Malloc VR MCP Server! Please read our [Contributing Guidelines](CONTRIBUTING.md) before submitting pull requests.

### Development Setup

1. Fork the repository
2. Create a feature branch
3. Install development dependencies
4. Run tests and ensure all pass
5. Submit a pull request

### Code Style

- Follow enterprise coding standards
- Include comprehensive JSDoc documentation
- Add educational impact statements
- Ensure Quest 3 performance compatibility
- Maintain FERPA compliance

## License

This project is licensed under the Educational Use License - see the [LICENSE](LICENSE) file for details.

## Support

- **Documentation**: [docs/](docs/)
- **Issues**: [GitHub Issues](https://github.com/malloc-vr/malloc-vr-mcp-server/issues)
- **Discussions**: [GitHub Discussions](https://github.com/malloc-vr/malloc-vr-mcp-server/discussions)

## Acknowledgments

- **Blender Foundation** for the open-source 3D creation suite
- **Meta** for Quest 3 VR platform support
- **Educational Technology Community** for FERPA compliance guidance
- **MCP Protocol Contributors** for the Model Context Protocol specification

---

**Malloc VR Learning Team**  
Version 2.0.0 | December 2024  
Educational Use License
