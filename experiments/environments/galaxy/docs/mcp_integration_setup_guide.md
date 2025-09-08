# MCP Integration Setup Guide
## VR Solar System/Galaxy Explorer Project

**Document Version:** 1.0  
**Date:** September 2025  
**Project Phase:** 1 - Environment Setup & Configuration

---

## Executive Summary

This comprehensive technical guide provides detailed instructions for configuring the enhanced Model Context Protocol (MCP) server environment optimized for VR Solar System/Galaxy Explorer development. The integration enables AI-assisted astronomical content creation, procedural generation of celestial bodies, and intelligent optimization workflows while maintaining scientific accuracy and VR performance targets.

## 1. Prerequisites and System Requirements

### 1.1 Hardware Requirements

**Minimum Development System:**
- **CPU:** Intel i7-9700K / AMD Ryzen 7 3700X or equivalent (8+ cores)
- **RAM:** 32GB DDR4 (64GB recommended for large astronomical datasets)
- **GPU:** NVIDIA RTX 3070 / AMD RX 6700 XT (8GB+ VRAM for VR preview)
- **Storage:** 1TB NVMe SSD (fast I/O for large texture streaming)
- **Network:** Stable broadband (MCP requires reliable API connectivity)

**VR Development Addition:**
- **VR Headset:** Meta Quest 2/3, Valve Index, or equivalent
- **USB:** USB 3.0+ ports for headset connectivity
- **Space:** 2m × 2m minimum room-scale area for testing

### 1.2 Software Prerequisites

**Core Development Environment:**
```bash
# Required Software Versions
Python: 3.11+ (for MCP server functionality)
Node.js: 18.0+ (for Three.js development environment)
Blender: 4.4+ (with Python API access enabled)
Cursor IDE: Latest version with MCP support
Git: 2.40+ (for version control integration)
```

**Python Environment Setup:**
```bash
# Install UV package manager (required for MCP)
# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Verify UV installation
uv --version
```

**Astronomical Data Dependencies:**
```bash
# Install astronomical computation libraries
pip install skyfield astropy ephem numpy scipy
pip install astroquery # For real-time astronomical data
pip install pyproj # For coordinate system transformations
```

## 2. MCP Server Installation and Configuration

### 2.1 Core MCP Installation

**Step 1: Download and Install MCP Server**
```bash
# Create project directory
mkdir vr-solar-system-mcp
cd vr-solar-system-mcp

# Initialize UV project
uv init

# Install core MCP dependencies
uv add mcp
uv add anthropic
uv add openai  # Optional: for additional AI model support
```

**Step 2: Configure MCP Server for Astronomical Content**
```python
# mcp_config.py
import os
from mcp import MCPServer, MCPServerConfig

# Astronomical-specific configuration
ASTRONOMICAL_CONFIG = {
    "ephemeris_data_source": "JPL",
    "star_catalog": "hipparcos_tycho",
    "planet_texture_resolution": {
        "hero_assets": 4096,
        "mid_tier": 2048,
        "background": 1024
    },
    "performance_targets": {
        "max_triangles_per_planet": 25000,
        "star_field_density": 100000,
        "texture_memory_budget_mb": 512
    },
    "coordinate_systems": {
        "primary": "J2000_ecliptic",
        "galactic": "galactic_coordinates",
        "local": "vr_room_space"
    }
}

# Initialize MCP server with astronomical extensions
server = MCPServer(
    name="vr-solar-system-mcp",
    version="1.0.0",
    config=MCPServerConfig(
        astronomical_mode=True,
        vr_optimization=True,
        scientific_accuracy=True,
        custom_config=ASTRONOMICAL_CONFIG
    )
)
```

### 2.2 Enhanced MCP Features Configuration

**Astronomical Content Generation:**
```python
# astronomical_tools.py
class AstronomicalContentGenerator:
    def __init__(self):
        self.ephemeris = self.load_ephemeris_data()
        self.star_catalog = self.load_star_catalog()
        self.planet_templates = self.load_planet_templates()
    
    def generate_planet_surface(self, planet_name, detail_level="mid_tier"):
        """Generate scientifically accurate planetary surface"""
        planet_data = self.get_planet_characteristics(planet_name)
        surface_params = {
            "radius": planet_data["radius"],
            "gravity": planet_data["gravity"], 
            "atmosphere": planet_data["atmosphere"],
            "geology": planet_data["surface_composition"],
            "detail_level": detail_level
        }
        return self.create_procedural_surface(surface_params)
    
    def generate_constellation_map(self, observer_location, time_epoch):
        """Generate accurate constellation positions"""
        star_positions = self.calculate_star_positions(observer_location, time_epoch)
        constellation_data = self.map_constellations(star_positions)
        return self.optimize_for_vr(constellation_data)
```

**VR Performance Optimization:**
```python
# vr_optimization.py
class VRPerformanceOptimizer:
    def __init__(self):
        self.target_fps = 90
        self.frame_budget_ms = 11.1
        self.polygon_budget = 300000
    
    def optimize_celestial_object(self, object_data, viewing_distance):
        """Optimize astronomical objects for VR performance"""
        lod_level = self.calculate_lod(viewing_distance)
        optimized_mesh = self.reduce_polygons(object_data, lod_level)
        optimized_textures = self.compress_textures(object_data, lod_level)
        
        return {
            "mesh": optimized_mesh,
            "textures": optimized_textures,
            "performance_impact": self.estimate_performance_cost(optimized_mesh)
        }
```

## 3. Cursor IDE Integration

### 3.1 Cursor MCP Configuration

**Create Cursor Configuration File:**
```json
// .cursor/mcp_servers.json
{
  "mcpServers": {
    "vr-solar-system": {
      "command": "uvx",
      "args": ["vr-solar-system-mcp"],
      "env": {
        "ANTHROPIC_API_KEY": "${ANTHROPIC_API_KEY}",
        "ASTRONOMICAL_DATA_PATH": "./data/astronomical",
        "VR_OPTIMIZATION_MODE": "true",
        "SCIENTIFIC_ACCURACY_LEVEL": "high"
      },
      "settings": {
        "astronomical_mode": true,
        "vr_preview_enabled": true,
        "performance_monitoring": true,
        "coordinate_system": "J2000_ecliptic"
      }
    }
  },
  "mcpClientSettings": {
    "timeout": 30000,
    "retryAttempts": 3,
    "bufferSize": "10MB",
    "astronomical_data_cache": true
  }
}
```

**Environment Variables Setup:**
```bash
# .env file for VR Solar System project
ANTHROPIC_API_KEY=your_anthropic_api_key_here
OPENAI_API_KEY=your_openai_api_key_here  # Optional
ASTRONOMICAL_DATA_PATH=./data/astronomical
BLENDER_EXECUTABLE_PATH=/Applications/Blender.app/Contents/MacOS/Blender
VR_HEADSET_TYPE=meta_quest_3
TEXTURE_CACHE_SIZE_GB=8
EPHEMERIS_UPDATE_INTERVAL_HOURS=24
```

### 3.2 Cursor Workspace Configuration

**Workspace Settings for Astronomical Development:**
```json
// .vscode/settings.json (Cursor uses VSCode config)
{
  "mcp.astronomical.enableRealTimeEphemeris": true,
  "mcp.vr.optimizationLevel": "aggressive",
  "mcp.blender.integrationMode": "direct",
  "files.associations": {
    "*.glb": "binary",
    "*.gltf": "json",
    "*.blend": "binary"
  },
  "astronomical.dataSource": "JPL_Horizons",
  "vr.performanceTarget": "90fps",
  "blender.pythonPath": "/Applications/Blender.app/Contents/Resources/4.4/python/bin/python3.11",
  "three.coordianteSystem": "right_handed_y_up"
}
```

## 4. Blender 4.4 MCP Integration

### 4.1 Blender MCP Addon Installation

**Download and Install Blender MCP Addon:**
```bash
# Download latest Blender MCP addon
curl -L https://github.com/anthropic/blender-mcp/releases/latest/download/blender_mcp_addon.zip -o blender_mcp_addon.zip

# Extract to Blender addons directory
# Windows: %APPDATA%\Blender Foundation\Blender\4.4\scripts\addons\
# macOS: ~/Library/Application Support/Blender/4.4/scripts/addons/
# Linux: ~/.config/blender/4.4/scripts/addons/
```

**Enable Addon in Blender:**
1. Open Blender 4.4
2. Navigate to Edit → Preferences → Add-ons
3. Click "Install..." and select the downloaded addon file
4. Search for "MCP" and enable "Interface: Blender MCP"
5. Configure addon preferences

**Blender MCP Addon Configuration:**
```python
# Blender addon preferences
addon_prefs = {
    "mcp_server_url": "http://localhost:8000",
    "astronomical_mode": True,
    "vr_optimization": True,
    "coordinate_system": "blender_z_up_to_threejs_y_up",
    "texture_optimization": "vr_performance",
    "mesh_optimization": "lod_aware",
    "scientific_accuracy": "high",
    "asset_libraries": {
        "poly_haven": True,
        "nasa_3d_resources": True,
        "esa_archives": True
    }
}
```

### 4.2 Astronomical Asset Libraries Integration

**Enable Specialized Asset Libraries:**
```python
# Blender MCP astronomical libraries configuration
ASTRONOMICAL_LIBRARIES = {
    "poly_haven": {
        "enabled": True,
        "hdri_space_environments": True,
        "planetary_textures": True,
        "star_field_hdris": True
    },
    "nasa_3d_resources": {
        "enabled": True,
        "spacecraft_models": True,
        "planetary_data": True,
        "mission_assets": True
    },
    "procedural_generation": {
        "enabled": True,
        "planet_surface_generator": True,
        "asteroid_field_generator": True,
        "star_system_generator": True,
        "ring_system_generator": True
    }
}
```

**Custom Astronomical Tools:**
```python
# Custom Blender operators for astronomical content
import bpy
import bmesh
from mathutils import Vector
import numpy as np

class MESH_OT_generate_planet(bpy.types.Operator):
    """Generate scientifically accurate planet mesh"""
    bl_idname = "mesh.generate_planet"
    bl_label = "Generate Planet"
    bl_options = {'REGISTER', 'UNDO'}
    
    planet_name: bpy.props.StringProperty(name="Planet Name", default="Earth")
    detail_level: bpy.props.EnumProperty(
        name="Detail Level",
        items=[
            ('LOW', 'Low (Background)', 'Low detail for distant viewing'),
            ('MEDIUM', 'Medium (Mid-tier)', 'Medium detail for general use'),
            ('HIGH', 'High (Hero)', 'High detail for close examination')
        ],
        default='MEDIUM'
    )
    
    def execute(self, context):
        # Generate planet using MCP astronomical data
        planet_data = self.get_planet_data(self.planet_name)
        mesh = self.create_planet_mesh(planet_data, self.detail_level)
        return {'FINISHED'}
```

## 5. Integration Testing and Validation

### 5.1 Connection Verification

**MCP Server Connection Test:**
```python
# test_mcp_connection.py
import asyncio
from mcp_client import MCPClient

async def test_mcp_connection():
    """Test MCP server connection and basic functionality"""
    client = MCPClient("http://localhost:8000")
    
    try:
        # Test basic connection
        await client.connect()
        print("✓ MCP server connection successful")
        
        # Test astronomical data access
        earth_data = await client.get_planet_data("Earth")
        print(f"✓ Earth data retrieved: radius={earth_data['radius']}km")
        
        # Test VR optimization capabilities
        optimized_earth = await client.optimize_for_vr(earth_data, "medium")
        print(f"✓ VR optimization: {optimized_earth['polygon_count']} triangles")
        
        # Test Blender integration
        blend_file = await client.generate_blender_scene("solar_system_overview")
        print(f"✓ Blender scene generated: {blend_file}")
        
    except Exception as e:
        print(f"✗ MCP connection failed: {e}")
        return False
    
    return True

# Run connection test
if __name__ == "__main__":
    asyncio.run(test_mcp_connection())
```

**Blender Integration Test:**
```python
# blender_mcp_test.py (run within Blender)
import bpy

def test_blender_mcp_integration():
    """Test Blender MCP addon functionality"""
    tests = []
    
    # Test 1: MCP addon is enabled
    try:
        addon = bpy.context.preferences.addons.get('blender_mcp')
        tests.append(("MCP Addon Enabled", addon is not None))
    except:
        tests.append(("MCP Addon Enabled", False))
    
    # Test 2: Astronomical data access
    try:
        bpy.ops.mesh.generate_planet(planet_name="Mars")
        mars_obj = bpy.context.active_object
        tests.append(("Mars Generation", mars_obj.name.startswith("Mars")))
    except:
        tests.append(("Mars Generation", False))
    
    # Test 3: VR export settings
    try:
        bpy.context.scene.world.mcp_vr_settings.target_fps = 90
        tests.append(("VR Settings Access", True))
    except:
        tests.append(("VR Settings Access", False))
    
    # Print test results
    for test_name, result in tests:
        status = "✓" if result else "✗"
        print(f"{status} {test_name}")
    
    return all(result for _, result in tests)

# Run Blender test
test_blender_mcp_integration()
```

### 5.2 Performance Validation

**VR Performance Benchmarking:**
```python
# vr_performance_test.py
import time
import psutil
import subprocess

class VRPerformanceBenchmark:
    def __init__(self):
        self.target_fps = 90
        self.frame_budget_ms = 11.1
        
    def benchmark_planetary_generation(self, planet_name):
        """Benchmark planet generation performance"""
        start_time = time.time()
        start_memory = psutil.virtual_memory().used
        
        # Generate planet through MCP
        result = subprocess.run([
            "uvx", "vr-solar-system-mcp", 
            "generate-planet", planet_name, "--vr-optimized"
        ], capture_output=True, text=True)
        
        end_time = time.time()
        end_memory = psutil.virtual_memory().used
        
        return {
            "generation_time_seconds": end_time - start_time,
            "memory_usage_mb": (end_memory - start_memory) / 1024 / 1024,
            "success": result.returncode == 0,
            "output": result.stdout
        }
    
    def validate_vr_performance(self, scene_complexity):
        """Validate scene meets VR performance targets"""
        benchmarks = {
            "earth_surface": self.benchmark_planetary_generation("Earth"),
            "jupiter_system": self.benchmark_planetary_generation("Jupiter"), 
            "saturn_rings": self.benchmark_planetary_generation("Saturn"),
            "solar_system_overview": self.benchmark_system_generation()
        }
        
        # Performance validation
        for test_name, result in benchmarks.items():
            meets_target = result["generation_time_seconds"] < 5.0  # 5s max generation
            memory_ok = result["memory_usage_mb"] < 1000  # 1GB max memory
            
            print(f"{test_name}:")
            print(f"  Generation Time: {result['generation_time_seconds']:.2f}s {'✓' if meets_target else '✗'}")
            print(f"  Memory Usage: {result['memory_usage_mb']:.1f}MB {'✓' if memory_ok else '✗'}")
            print(f"  Success: {'✓' if result['success'] else '✗'}")
```

## 6. Troubleshooting and Diagnostics

### 6.1 Common Issues and Solutions

**Issue: MCP Server Connection Timeout**
```bash
# Diagnosis steps:
1. Check UV installation: uv --version
2. Verify Python environment: python --version
3. Test network connectivity: curl http://localhost:8000
4. Check firewall settings
5. Restart MCP server: uvx vr-solar-system-mcp --restart

# Solution:
# Increase timeout in Cursor configuration
"mcpClientSettings": {
  "timeout": 60000,  # Increase to 60 seconds
  "retryAttempts": 5
}
```

**Issue: Blender MCP Addon Not Loading**
```python
# Diagnosis script (run in Blender Python console):
import sys
print("Python version:", sys.version)
print("Python path:", sys.path)

import addon_utils
addons = addon_utils.modules()
mcp_addon = next((addon for addon in addons if 'mcp' in addon.__name__), None)
print("MCP addon found:", mcp_addon is not None)

# Solution steps:
# 1. Verify Blender Python version compatibility
# 2. Check addon installation path
# 3. Reinstall addon with correct Python dependencies
# 4. Enable developer extras in Blender preferences
```

**Issue: Astronomical Data Loading Errors**
```python
# Diagnosis:
def diagnose_astronomical_data():
    import os
    
    data_path = os.environ.get('ASTRONOMICAL_DATA_PATH', './data/astronomical')
    print(f"Data path: {data_path}")
    print(f"Path exists: {os.path.exists(data_path)}")
    
    required_files = [
        'planets.json',
        'star_catalog.txt', 
        'ephemeris_data.bsp',
        'constellation_lines.dat'
    ]
    
    for file in required_files:
        file_path = os.path.join(data_path, file)
        exists = os.path.exists(file_path)
        print(f"{file}: {'✓' if exists else '✗'}")
        
        if not exists:
            print(f"  Download from: https://data.astronomical.org/{file}")

# Solution: Download missing astronomical data files
```

### 6.2 Diagnostic Tools

**MCP Health Check Script:**
```bash
#!/bin/bash
# mcp_health_check.sh

echo "=== MCP Health Check for VR Solar System Explorer ==="

# Check UV installation
echo "Checking UV package manager..."
if command -v uv &> /dev/null; then
    echo "✓ UV installed: $(uv --version)"
else
    echo "✗ UV not found. Install with: curl -LsSf https://astral.sh/uv/install.sh | sh"
fi

# Check Python environment
echo "Checking Python environment..."
python_version=$(python --version 2>&1)
echo "✓ Python: $python_version"

# Check MCP server
echo "Checking MCP server..."
if pgrep -f "vr-solar-system-mcp" > /dev/null; then
    echo "✓ MCP server running"
else
    echo "✗ MCP server not running. Start with: uvx vr-solar-system-mcp"
fi

# Check Blender
echo "Checking Blender installation..."
blender_path="${BLENDER_EXECUTABLE_PATH:-blender}"
if command -v "$blender_path" &> /dev/null; then
    blender_version=$("$blender_path" --version | head -n 1)
    echo "✓ Blender: $blender_version"
else
    echo "✗ Blender not found. Set BLENDER_EXECUTABLE_PATH environment variable"
fi

# Check astronomical data
echo "Checking astronomical data..."
if [ -d "${ASTRONOMICAL_DATA_PATH:-./data/astronomical}" ]; then
    echo "✓ Astronomical data directory exists"
else
    echo "✗ Astronomical data directory missing. Create: mkdir -p ./data/astronomical"
fi

echo "=== Health Check Complete ==="
```

## 7. Team Coordination and Best Practices

### 7.1 Team Setup Procedures

**Individual Developer Setup:**
1. **Initial Setup (30 minutes):**
   - Install UV package manager
   - Configure Cursor IDE with MCP settings
   - Install Blender 4.4 and MCP addon
   - Download astronomical data packages

2. **Team Synchronization (15 minutes):**
   - Clone project repository with MCP configuration
   - Sync environment variables from team vault
   - Verify MCP server connection
   - Run integration tests

3. **Validation (10 minutes):**
   - Generate test planetary scene
   - Export to VR format
   - Confirm scientific accuracy benchmarks

**Team Configuration Management:**
```yaml
# team_config.yml
team_settings:
  mcp_server_version: "1.0.0"
  blender_version: "4.4.0"
  cursor_version: "latest"
  
  shared_resources:
    astronomical_data: "s3://team-bucket/astronomical-data/"
    texture_library: "s3://team-bucket/textures/"
    reference_models: "s3://team-bucket/reference-models/"
  
  performance_targets:
    vr_fps: 90
    texture_memory_mb: 512
    polygon_budget: 300000
  
  quality_standards:
    scientific_accuracy: "high"
    educational_level: "university"
    accessibility: "wcag_aa"
```

### 7.2 Version Control Integration

**Git Hooks for MCP Validation:**
```bash
#!/bin/bash
# .git/hooks/pre-commit
# Validate MCP configuration before commits

echo "Validating MCP configuration..."

# Check MCP server configuration
if [ ! -f ".cursor/mcp_servers.json" ]; then
    echo "Error: MCP server configuration missing"
    exit 1
fi

# Validate Blender scenes
for blend_file in *.blend; do
    if [ -f "$blend_file" ]; then
        echo "Validating $blend_file..."
        # Add Blender validation script here
    fi
done

# Check astronomical data integrity
python scripts/validate_astronomical_data.py

echo "MCP validation complete ✓"
```

---

## Appendices

### Appendix A: Complete Environment Variables Reference
[Comprehensive list of all environment variables and their purposes]

### Appendix B: MCP Server API Documentation
[Technical API reference for custom astronomical functions]

### Appendix C: Blender Addon Python API
[Complete reference for Blender MCP addon functions]

### Appendix D: Performance Optimization Guidelines
[Detailed guidelines for maintaining VR performance with MCP-generated content]

### Appendix E: Astronomical Data Sources
[List of scientific data sources and update procedures]

---

**Document Prepared By:** MCP Integration Team  
**Reviewed By:** VR Development Architecture Committee  
**Approved By:** Technical Infrastructure Director  
**Next Review Date:** December 2025