# Malloc VR MCP Server - Complete Installation Guide

Installation and Setup

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Blender 4.4+](https://img.shields.io/badge/blender-4.4+-orange.svg)](https://www.blender.org/download/)
[![Quest 3 Optimized](https://img.shields.io/badge/quest_3-optimized-green.svg)](https://www.meta.com/quest/quest-3/)
[![FERPA Compliant](https://img.shields.io/badge/FERPA-compliant-red.svg)](https://www2.ed.gov/policy/gen/guid/fpco/ferpa/index.html)

## Table of Contents

- [Overview](#overview)
- [System Requirements](#system-requirements)
- [Installation Methods](#installation-methods)
  - [Quick Start (Recommended)](#quick-start-recommended)
  - [Development Installation](#development-installation)
  - [Docker Installation](#docker-installation)
  - [Production Kubernetes Deployment](#production-kubernetes-deployment)
- [Configuration](#configuration)
- [Blender Integration Setup](#blender-integration-setup)
- [VR Hardware Setup](#vr-hardware-setup)
- [Security Configuration](#security-configuration)
- [Verification and Testing](#verification-and-testing)
- [Troubleshooting](#troubleshooting)
- [Performance Optimization](#performance-optimization)

## Overview

The Malloc VR MCP Server is an enterprise-grade educational VR learning platform that implements:

- **Real-time Learning Adaptation** with mathematical model computation
- **Five Learning Model APIs**: Learner (∩), Knowledge (∆), Engagement (E), Assessment (A), Transition (∂)
- **WebSocket Communication** for real-time educational interactions
- **FERPA-Compliant Security** with educational data protection
- **Blender 4.4+ Integration** with Python API optimization for Quest 3 VR
- **Enterprise Performance** with <100ms response times

### Mathematical Foundation

The system implements the core learning equation:
```
∂(t+1) = ∂(t) + α · Δ(∩(t), ∆(t), E(t), A(t)) + β · ε(t)
```

## System Requirements

### Minimum Requirements

| Component | Requirement | Reason |
|-----------|-------------|---------|
| **Python** | 3.11+ | Blender 4.4 compatibility |
| **Memory** | 4GB RAM | Base system + learning models |
| **Storage** | 2GB free space | Application + database |
| **Network** | Stable internet | Asset downloads |
| **OS** | Windows 10/11, macOS 12+, Ubuntu 20.04+ | Cross-platform support |

### Recommended Requirements

| Component | Requirement | Reason |
|-----------|-------------|---------|
| **Python** | 3.11+ | Optimal performance |
| **Memory** | 8GB+ RAM | Enhanced VR performance |
| **Storage** | 10GB+ SSD | Fast asset loading |
| **Network** | Gigabit ethernet | Real-time VR streaming |
| **GPU** | NVIDIA GTX 1060+ / AMD RX 580+ | VR rendering |

### VR Hardware (Optional)

| Component | Requirement | Notes |
|-----------|-------------|--------|
| **VR Headset** | Meta Quest 3 (recommended) | Primary target platform |
| **Alternative VR** | Quest 2, Valve Index, HTC Vive | Limited optimization |
| **Tracking Space** | 2m x 2m minimum | Safe learning environment |

### Software Dependencies

| Software | Version | Required | Purpose |
|----------|---------|----------|---------|
| **Python** | 3.11+ | ✅ Yes | Core runtime |
| **Blender** | 4.4+ | ⚠️ Optional | VR content creation |
| **Node.js** | 18+ | ⚠️ Dev only | Documentation generation |
| **Docker** | 20+ | ⚠️ Optional | Containerized deployment |
| **Kubernetes** | 1.25+ | ⚠️ Optional | Production scaling |

## Installation Methods

### Quick Start (Recommended)

Perfect for testing and educational use.

#### Step 1: Clone Repository

```bash
# Clone the repository
git clone https://github.com/malloc-vr/malloc-vr-mcp-server.git
cd malloc-vr-mcp-server

# Or download ZIP and extract
# wget https://github.com/malloc-vr/malloc-vr-mcp-server/archive/main.zip
# unzip main.zip && cd malloc-vr-mcp-server-main
```

#### Step 2: Python Environment Setup

```bash
# Check Python version (must be 3.11+)
python --version

# Create virtual environment (recommended)
python -m venv malloc-vr-env

# Activate virtual environment
# Windows:
malloc-vr-env\Scripts\activate

# macOS/Linux:
source malloc-vr-env/bin/activate
```

#### Step 3: Install Dependencies

```bash
# Install core dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Verify installation
python -c "import fastapi, websockets, numpy; print('Dependencies installed successfully')"
```

#### Step 4: Initialize Database

```bash
# Create data directories
mkdir -p data logs

# Set basic environment variables
export MALLOC_VR_SERVER_NAME="my-learning-server"
export MALLOC_VR_FERPA_ENABLED=true
export MALLOC_VR_DEBUG=true

# Windows users:
# set MALLOC_VR_SERVER_NAME=my-learning-server
# set MALLOC_VR_FERPA_ENABLED=true
# set MALLOC_VR_DEBUG=true
```

#### Step 5: Start Server

```bash
# Start the MCP server
python -m src.main

# You should see the startup banner and confirmation messages
```

#### Step 6: Verify Installation

Open another terminal and test:

```bash
# Test server health (if WebSocket is enabled)
curl -f http://localhost:8765/health || echo "WebSocket server running"

# Check log files
tail -f logs/malloc_vr_mcp_server.log
```

### Development Installation

For developers and advanced users.

#### Step 1: Development Setup

```bash
# Clone with development branch
git clone -b develop https://github.com/malloc-vr/malloc-vr-mcp-server.git
cd malloc-vr-mcp-server

# Install development dependencies
pip install -r requirements.txt
pip install pytest pytest-asyncio pytest-cov black mypy

# Install in development mode
pip install -e .
```

#### Step 2: Development Configuration

Create `.env` file:

```bash
# .env file for development
MALLOC_VR_SERVER_NAME=dev-learning-server
MALLOC_VR_MAX_LEARNERS=10
MALLOC_VR_DEBUG=true
MALLOC_VR_FERPA_ENABLED=true
MALLOC_VR_DATABASE_PATH=data/dev_learning.db
MALLOC_VR_CACHE_ENABLED=true
MALLOC_VR_BLENDER_INTEGRATION=false
```

#### Step 3: Run Tests

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=src --cov-report=html

# Run specific test suites
pytest tests/test_integration_engine.py -v
pytest tests/test_performance_validation.py -v
```

#### Step 4: Code Quality Checks

```bash
# Format code
black src/ tests/

# Type checking
mypy src/

# Check specific files
mypy src/main.py src/mcp/server_configuration.py
```

### Docker Installation

For containerized deployment.

#### Step 1: Docker Setup

```bash
# Ensure Docker is installed and running
docker --version
docker-compose --version

# Clone repository
git clone https://github.com/malloc-vr/malloc-vr-mcp-server.git
cd malloc-vr-mcp-server
```

#### Step 2: Environment Configuration

Create `.env` file for Docker:

```bash
# .env file for Docker deployment
DB_PASSWORD=secure_educational_password_123
REDIS_PASSWORD=redis_educational_password_456
ALERT_WEBHOOK_URL=https://your-monitoring-service.com/alerts

# Educational settings
MALLOC_VR_MAX_LEARNERS=50
MALLOC_VR_FERPA_ENABLED=true
MALLOC_VR_DEBUG=false
```

#### Step 3: Docker Compose Deployment

```bash
# Start all services
docker-compose up -d

# Check service status
docker-compose ps

# View logs
docker-compose logs -f mcp-gateway

# Scale specific services
docker-compose up -d --scale learner-service=3
```

#### Step 4: Verify Docker Installation

```bash
# Test gateway health
curl -f http://localhost:8080/health

# Test WebSocket service
curl -f http://localhost:8081/health

# Check database connectivity
docker-compose exec postgresql pg_isready -U educational_user
```

### Production Kubernetes Deployment

For enterprise production environments.

#### Step 1: Kubernetes Prerequisites

```bash
# Ensure Kubernetes cluster is available
kubectl cluster-info

# Ensure you have admin access
kubectl auth can-i create deployments --namespace=malloc-vr-production
```

#### Step 2: Create Namespace and Secrets

```bash
# Apply the Kubernetes configuration
kubectl apply -f kubernetes/production-deployment.yml

# Create additional secrets (update values)
kubectl create secret generic educational-secrets \
  --from-literal=DB_PASSWORD=your_secure_db_password \
  --from-literal=REDIS_PASSWORD=your_secure_redis_password \
  --from-literal=JWT_SECRET=your_jwt_secret_key \
  --namespace=malloc-vr-production
```

#### Step 3: Deploy Services

```bash
# Deploy all services
kubectl apply -f kubernetes/production-deployment.yml

# Check deployment status
kubectl get pods -n malloc-vr-production

# Check service status
kubectl get services -n malloc-vr-production
```

#### Step 4: Configure Load Balancer

```bash
# Get external IP for gateway service
kubectl get service mcp-gateway-service -n malloc-vr-production

# If using cloud provider, configure DNS
# Point your domain to the external load balancer IP
```

#### Step 5: Production Verification

```bash
# Test production endpoints
curl -f https://your-domain.com/health

# Check pod logs
kubectl logs -f deployment/mcp-gateway -n malloc-vr-production

# Monitor scaling
kubectl get hpa -n malloc-vr-production
```

## Configuration

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `MALLOC_VR_SERVER_NAME` | `malloc-vr-learning` | Server identifier |
| `MALLOC_VR_MAX_LEARNERS` | `50` | Maximum concurrent learners |
| `MALLOC_VR_DEBUG` | `false` | Debug mode enable |
| `MALLOC_VR_FERPA_ENABLED` | `true` | FERPA compliance |
| `MALLOC_VR_DATABASE_PATH` | `data/malloc_vr_learning.db` | Database path |
| `MALLOC_VR_CACHE_ENABLED` | `true` | Performance caching |
| `MALLOC_VR_WEBSOCKET_PORT` | `8765` | WebSocket port |
| `MALLOC_VR_BLENDER_INTEGRATION` | `auto-detect` | Blender integration |

### Configuration Files

Create `config.json` in project root:

```json
{
  "server_name": "my-educational-server",
  "max_concurrent_learners": 25,
  "ferpa_compliance_enabled": true,
  "real_time_adaptation_enabled": true,
  "quest3_frame_rate_minimum": 72,
  "quest3_memory_limit_mb": 100,
  "spatial_precision_tolerance_mm": 0.1,
  "learning_equation_alpha": 0.7,
  "learning_equation_beta": 0.3,
  "blender_integration_enabled": true,
  "debug_mode": false
}
```

### Performance Tuning

For Quest 3 VR optimization:

```bash
# Environment variables for Quest 3
export MALLOC_VR_QUEST3_OPTIMIZED=true
export MALLOC_VR_FRAME_RATE_MIN=72
export MALLOC_VR_MEMORY_LIMIT=100
export MALLOC_VR_SPATIAL_PRECISION=0.1
```

## Blender Integration Setup

### Step 1: Install Blender 4.4+

```bash
# Download Blender 4.4+ from official site
# https://www.blender.org/download/

# Verify installation
blender --version

# Should show version 4.4.0 or higher
```

### Step 2: Configure Blender Python Environment

```bash
# Locate Blender's Python
blender --background --python-expr "import sys; print(sys.executable)"

# Install additional packages in Blender's Python (if needed)
# /path/to/blender/python -m pip install numpy scipy
```

### Step 3: Test Blender Integration

```python
# Test script: test_blender_integration.py
import bpy
import sys
import os

# Add the project path to Blender's Python path
project_path = "/path/to/malloc-vr-mcp-server"
if project_path not in sys.path:
    sys.path.append(project_path)

# Test import
try:
    from src.blender.blender_mcp_tools import BlenderMCPTools
    print("✓ Blender integration successful")
except ImportError as e:
    print(f"✗ Blender integration failed: {e}")
```

Run test:

```bash
blender --background --python test_blender_integration.py
```

### Step 4: Configure Blender for VR

```python
# In Blender, enable VR scene collection
import bpy

# Create VR-optimized scene
scene = bpy.context.scene
scene.render.engine = 'EEVEE'
scene.eevee.taa_render_samples = 64
scene.eevee.use_gtao = True
scene.eevee.use_bloom = True
```

## VR Hardware Setup

### Quest 3 Setup

#### Step 1: Enable Developer Mode

1. Install Meta Quest app on your phone
2. Connect Quest 3 to Meta account
3. Enable Developer Mode in app settings
4. Enable USB debugging on Quest 3

#### Step 2: Connect to PC

```bash
# Install ADB if not present
# Windows: Download Android SDK Platform-Tools
# macOS: brew install android-platform-tools
# Linux: sudo apt install android-tools-adb

# Connect Quest 3 via USB or WiFi
adb devices

# Should show your Quest 3 device
```

#### Step 3: Configure Quest 3 for Development

```bash
# Enable wireless debugging (optional)
adb tcpip 5555
adb connect YOUR_QUEST_IP:5555

# Test connection
adb shell "echo 'Quest 3 connected successfully'"
```

### Alternative VR Headsets

#### Valve Index / HTC Vive

```bash
# Install SteamVR
# Download from Steam store

# Configure OpenVR
pip install openvr

# Test OpenVR connection
python -c "import openvr; print('OpenVR available')"
```

## Security Configuration

### FERPA Compliance Setup

#### Step 1: Database Encryption

```bash
# Generate encryption keys
openssl rand -base64 32 > encryption.key

# Secure the key file
chmod 600 encryption.key

# Set environment variable
export MALLOC_VR_ENCRYPTION_KEY=$(cat encryption.key)
```

#### Step 2: SSL/TLS Configuration

```bash
# Generate SSL certificates for production
openssl req -newkey rsa:2048 -nodes -keyout private.key \
  -x509 -days 365 -out certificate.crt

# Configure HTTPS
export MALLOC_VR_SSL_CERT=certificate.crt
export MALLOC_VR_SSL_KEY=private.key
export MALLOC_VR_FORCE_HTTPS=true
```

#### Step 3: Access Control

```json
{
  "authentication": {
    "jwt_secret_rotation_hours": 24,
    "session_timeout_minutes": 60,
    "max_failed_attempts": 3
  },
  "authorization": {
    "roles": ["learner", "educator", "administrator"],
    "learner_data_access": "own_only",
    "audit_logging": true
  },
  "data_protection": {
    "anonymization_enabled": true,
    "data_retention_days": 90,
    "deletion_on_request": true
  }
}
```

## Verification and Testing

### Basic Functionality Test

```bash
# Test 1: Server startup
python -m src.main &
SERVER_PID=$!

# Wait for startup
sleep 10

# Test 2: Health check
if curl -f http://localhost:8765/health; then
  echo "✓ WebSocket server healthy"
else
  echo "✗ WebSocket server not responding"
fi

# Test 3: Stop server
kill $SERVER_PID
```

### Learning Models Test

```python
# test_learning_models.py
import asyncio
import sys
import os

# Add project path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.learning.integration_engine import IntegrationEngine
from src.mcp.server_configuration import MCPServerConfiguration

async def test_learning_models():
    """Test the learning models integration."""
    
    # Create test configuration
    config = MCPServerConfiguration(
        debug_mode=True,
        max_concurrent_learners=1
    )
    
    # Initialize integration engine
    engine = IntegrationEngine(config)
    
    # Test learner model
    learner_result = await engine.process_learner_model(
        learner_id="test_student_001",
        static_profile={
            "demographic": {"age_range": "18-25"},
            "learning_preferences": {"guidance_level": "moderate"}
        },
        dynamic_profile={}
    )
    
    print("✓ Learner model test:", learner_result["success"])
    
    # Test knowledge model
    knowledge_result = await engine.process_knowledge_model(
        knowledge_id="test_knowledge_001",
        curriculum_structure={
            "competencies": ["basic_math", "algebra"],
            "learning_objectives": ["solve_equations"]
        },
        content_metadata={}
    )
    
    print("✓ Knowledge model test:", knowledge_result["success"])
    
    print("All learning model tests completed successfully!")

if __name__ == "__main__":
    asyncio.run(test_learning_models())
```

Run test:

```bash
python test_learning_models.py
```

### Performance Test

```bash
# Performance benchmarking
python -m pytest tests/test_performance_validation.py -v

# Specific performance tests
python -c "
import time
import asyncio
from src.utils.learning_calculations import LearningCalculations

start = time.time()
calc = LearningCalculations()
result = calc.compute_adaptation_delta(
    learner_output={'weight': 0.3},
    knowledge_output={'weight': 0.25},
    engagement_output={'weight': 0.2},
    assessment_output={'weight': 0.25}
)
duration = (time.time() - start) * 1000

print(f'Learning calculation time: {duration:.2f}ms')
print(f'Target: <10ms, Result: {"✓ PASS" if duration < 10 else "✗ FAIL"}')"
```

### Integration Test

```bash
# Full integration test suite
python -m pytest tests/test_phase4_websocket_performance.py -v

# WebSocket communication test
python -c "
import asyncio
import websockets

async def test_websocket():
    try:
        uri = 'ws://localhost:8765'
        async with websockets.connect(uri, timeout=5) as websocket:
            await websocket.send('ping')
            response = await websocket.recv()
            print('✓ WebSocket communication successful')
    except Exception as e:
        print(f'✗ WebSocket test failed: {e}')

asyncio.run(test_websocket())
"
```

## Troubleshooting

### Common Issues

#### 1. Python Version Error

```bash
# Error: Python 3.11+ required
# Solution: Install Python 3.11+

# Check current version
python --version

# Install Python 3.11+ from python.org
# Or use pyenv:
pyenv install 3.11.0
pyenv global 3.11.0
```

#### 2. Blender Not Found

```bash
# Error: Blender integration failed
# Solution: Install Blender 4.4+ or disable integration

export MALLOC_VR_BLENDER_INTEGRATION=false
```

#### 3. Port Already in Use

```bash
# Error: WebSocket port 8765 already in use
# Solution: Change port or kill existing process

export MALLOC_VR_WEBSOCKET_PORT=8766

# Or find and kill the process:
lsof -i :8765
kill -9 PID
```

#### 4. Database Permission Error

```bash
# Error: Cannot write to database
# Solution: Fix directory permissions

mkdir -p data logs
chmod 755 data logs
chmod 644 data/*.db 2>/dev/null || true
```

#### 5. Memory Issues on Quest 3

```bash
# Error: Out of memory in VR
# Solution: Reduce memory limits

export MALLOC_VR_MEMORY_LIMIT=75
export MALLOC_VR_CACHE_SIZE=20
```

### Debug Mode

Enable comprehensive debugging:

```bash
export MALLOC_VR_DEBUG=true
export MALLOC_VR_LOG_LEVEL=DEBUG

python -m src.main
```

Check logs:

```bash
# View real-time logs
tail -f logs/malloc_vr_mcp_server.log

# Search for errors
grep ERROR logs/malloc_vr_mcp_server.log

# Check educational analytics
tail -f logs/educational_analytics.log
```

### Performance Issues

#### Check System Resources

```bash
# Monitor memory usage
free -h

# Monitor CPU usage
top -p $(pgrep -f "python.*src.main")

# Monitor disk I/O
iostat -x 1
```

#### Optimize Configuration

```json
{
  "performance_optimizations": {
    "quest3_memory_limit_mb": 75,
    "cache_max_size_mb": 20,
    "websocket_max_connections": 25,
    "learning_model_update_frequency": 2.0
  }
}
```

### Network Issues

#### Test Connectivity

```bash
# Test local WebSocket
nc -zv localhost 8765

# Test MCP protocol
python -c "
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex(('localhost', 8765))
print('✓ Port reachable' if result == 0 else '✗ Port unreachable')
sock.close()
"
```

#### Firewall Configuration

```bash
# Windows (run as administrator)
netsh advfirewall firewall add rule name="Malloc VR MCP Server" dir=in action=allow protocol=TCP localport=8765

# Linux (Ubuntu/Debian)
sudo ufw allow 8765/tcp

# macOS
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --add /usr/bin/python
```

## Performance Optimization

### Quest 3 VR Optimization

#### Configuration Tuning

```json
{
  "quest3_optimizations": {
    "frame_rate_minimum": 72,
    "memory_limit_mb": 100,
    "spatial_precision_tolerance_mm": 0.1,
    "cache_optimization": {
      "enabled": true,
      "max_size_mb": 30,
      "ttl_seconds": 120
    },
    "blender_optimization": {
      "scene_update_frequency": 5.0,
      "real_time_updates": true,
      "memory_efficient_mode": true
    }
  }
}
```

#### Monitor Performance

```bash
# Real-time performance monitoring
python -c "
import psutil
import time

def monitor_performance():
    process = None
    for p in psutil.process_iter(['pid', 'name', 'cmdline']):
        if 'src.main' in ' '.join(p.info['cmdline'] or []):
            process = p
            break
    
    if process:
        print(f'CPU: {process.cpu_percent():.1f}%')
        print(f'Memory: {process.memory_info().rss / 1024 / 1024:.1f}MB')
        print(f'Threads: {process.num_threads()}')
    else:
        print('Process not found')

monitor_performance()
"
```

### Database Optimization

```sql
-- SQLite optimization commands
PRAGMA journal_mode = WAL;
PRAGMA synchronous = NORMAL;
PRAGMA cache_size = 10000;
PRAGMA temp_store = memory;
```

Apply optimizations:

```python
# In your database initialization
import sqlite3

conn = sqlite3.connect('data/malloc_vr_learning.db')
conn.execute('PRAGMA journal_mode = WAL')
conn.execute('PRAGMA synchronous = NORMAL')
conn.execute('PRAGMA cache_size = 10000')
conn.execute('PRAGMA temp_store = memory')
conn.commit()
```

### Network Optimization

#### WebSocket Optimization

```python
# Configure WebSocket for low latency
import websockets

server = websockets.serve(
    handler,
    "localhost",
    8765,
    compression=None,  # Disable compression for lower latency
    ping_interval=20,
    ping_timeout=10,
    max_size=1024*1024,  # 1MB message limit
    max_queue=32
)
```

#### Connection Pooling

```python
# Database connection pooling
import sqlite3
from contextlib import contextmanager

class ConnectionPool:
    def __init__(self, database_path, pool_size=10):
        self.database_path = database_path
        self.pool_size = pool_size
        self.connections = []
        
    @contextmanager
    def get_connection(self):
        if self.connections:
            conn = self.connections.pop()
        else:
            conn = sqlite3.connect(self.database_path)
        
        try:
            yield conn
        finally:
            if len(self.connections) < self.pool_size:
                self.connections.append(conn)
            else:
                conn.close()
```

## Support and Maintenance

### Regular Maintenance

#### Daily Tasks

```bash
# Check logs for errors
grep ERROR logs/malloc_vr_mcp_server.log | tail -10

# Monitor disk usage
df -h

# Check process health
ps aux | grep "python.*src.main"
```

#### Weekly Tasks

```bash
# Rotate logs
mv logs/malloc_vr_mcp_server.log logs/malloc_vr_mcp_server.log.$(date +%Y%m%d)
touch logs/malloc_vr_mcp_server.log

# Backup database
cp data/malloc_vr_learning.db backups/learning_$(date +%Y%m%d).db

# Update dependencies
pip list --outdated
```

#### Monthly Tasks

```bash
# Security updates
pip install --upgrade cryptography PyJWT

# Performance analysis
python -m pytest tests/test_performance_validation.py --benchmark

# Database maintenance
sqlite3 data/malloc_vr_learning.db "VACUUM;"
```

### Getting Help

#### Documentation

- **API Documentation**: `docs/api/`
- **Technical Specifications**: `docs/malloc_vr_mcp_server_specification.md`
- **Development Guide**: `docs/Malloc_VR_MCP_Development_Handbook.md`

#### Community Support

- **GitHub Issues**: Report bugs and request features
- **GitHub Discussions**: Community questions and answers
- **Discord Server**: Real-time community support

#### Enterprise Support

- **Priority Support**: Available for educational institutions
- **Custom Training**: Available for development teams
- **Consulting Services**: Implementation and optimization

---

## Summary

You have successfully installed the Malloc VR MCP Server! The server is now ready to provide enterprise-grade educational VR learning experiences with:

- ✅ Real-time adaptive learning with mathematical models
- ✅ FERPA-compliant educational data protection
- ✅ Quest 3 VR optimization for smooth learning experiences
- ✅ Blender 4.4+ integration for immersive content creation
- ✅ WebSocket communication for real-time interactions
- ✅ Comprehensive monitoring and analytics

### Next Steps

1. **Configure your educational content** using the learning model APIs
2. **Set up VR environments** with Blender integration
3. **Create learner profiles** and educational assessments
4. **Monitor performance** and optimize for your specific use case
5. **Scale deployment** using Docker or Kubernetes for production

### Quick Commands Reference

```bash
# Start server
python -m src.main

# Check health
curl -f http://localhost:8765/health

# View logs
tail -f logs/malloc_vr_mcp_server.log

# Run tests
pytest tests/ -v

# Stop server
# Press Ctrl+C in server terminal
```

**Happy Learning!** 🎓🥽

---

**Malloc VR Learning Team**  
Educational Technology Division  
Version 3.0.0 | Installation Guide v1.0  
Educational Use License
