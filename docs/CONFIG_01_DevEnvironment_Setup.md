# Elite VR Learning MCP: Project Setup & Environment Configuration

**Version:** 1.0  
**Date:** August 30, 2025  
**Purpose:** Complete project initialization and development environment setup  
**Target:** Enterprise-grade development environment for educational VR MCP system

---

## Understanding the Development Environment Architecture

Your Elite VR Learning MCP system requires a sophisticated multi-technology development environment that seamlessly integrates Node.js for MCP server components, Unity for VR development, Python for Blender integration, and TypeScript for educational analytics. The key insight here is that each technology serves a specific educational purpose: Node.js handles the intelligent coordination between tools, Unity creates the immersive learning experiences, Python enables dynamic asset creation, and TypeScript manages the complex learning analytics that make your system adaptive.

Think of this setup like creating a symphony orchestra where each instrument (technology) must be perfectly tuned and coordinated. The package configurations below ensure that all components work together harmoniously while maintaining the performance standards required for Quest 3 VR delivery.

---

## MCP Server Package Configuration

### package.json (Root MCP Server)

```json
{
  "name": "@elite-vr-learning/mcp-server",
  "version": "1.0.0",
  "description": "Elite VR Learning Experience Model Context Protocol Server with Educational AI Integration",
  "type": "module",
  "main": "dist/index.js",
  "bin": {
    "elite-vr-mcp": "./dist/bin/server.js"
  },
  "scripts": {
    "build": "tsc --build",
    "dev": "tsx watch --clear-screen=false src/index.ts",
    "start": "node dist/index.js",
    "test": "jest --coverage --detectOpenHandles",
    "test:watch": "jest --watch --detectOpenHandles",
    "test:educational": "jest --testPathPattern=educational --coverage",
    "test:integration": "jest --testPathPattern=integration --runInBand",
    "lint": "eslint src/**/*.ts --fix",
    "format": "prettier --write src/**/*.ts",
    "validate": "npm run lint && npm run test && npm run build",
    "docker:build": "docker build -t elite-vr-mcp-server .",
    "docker:run": "docker run -p 3000:3000 -e NODE_ENV=development elite-vr-mcp-server",
    "prepare": "husky install"
  },
  "dependencies": {
    "@modelcontextprotocol/sdk": "^0.5.0",
    "@anthropic-ai/sdk": "^0.27.0",
    "express": "^4.18.2",
    "cors": "^2.8.5",
    "helmet": "^7.1.0",
    "winston": "^3.11.0",
    "joi": "^17.11.0",
    "uuid": "^9.0.1",
    "dotenv": "^16.3.1",
    "compression": "^1.7.4",
    "rate-limiter-flexible": "^4.0.1",
    "ioredis": "^5.3.2",
    "mongoose": "^8.0.3",
    "jsonwebtoken": "^9.0.2",
    "bcryptjs": "^2.4.3",
    "multer": "^1.4.5-lts.1",
    "sharp": "^0.33.1",
    "ws": "^8.14.2",
    "socket.io": "^4.7.4",
    "@quest3/sdk": "^2.1.0",
    "three": "^0.158.0",
    "cannon-es": "^0.20.0",
    "xapi-statements": "^1.0.3",
    "ml-regression": "^6.0.1",
    "compromise": "^14.10.0",
    "natural": "^6.8.0"
  },
  "devDependencies": {
    "@types/node": "^20.10.4",
    "@types/express": "^4.17.21",
    "@types/cors": "^2.8.17",
    "@types/uuid": "^9.0.7",
    "@types/jsonwebtoken": "^9.0.5",
    "@types/bcryptjs": "^2.4.6",
    "@types/multer": "^1.4.11",
    "@types/ws": "^8.5.10",
    "@types/jest": "^29.5.8",
    "@types/supertest": "^2.0.16",
    "typescript": "^5.3.3",
    "tsx": "^4.6.2",
    "jest": "^29.7.0",
    "ts-jest": "^29.1.1",
    "supertest": "^6.3.3",
    "eslint": "^8.55.0",
    "@typescript-eslint/parser": "^6.14.0",
    "@typescript-eslint/eslint-plugin": "^6.14.0",
    "eslint-config-prettier": "^9.1.0",
    "eslint-plugin-prettier": "^5.0.1",
    "prettier": "^3.1.1",
    "husky": "^8.0.3",
    "lint-staged": "^15.2.0",
    "nodemon": "^3.0.2",
    "concurrently": "^8.2.2"
  },
  "engines": {
    "node": ">=20.0.0",
    "npm": ">=10.0.0"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/your-org/elite-vr-learning-mcp.git"
  },
  "keywords": [
    "mcp",
    "educational-vr",
    "quest3",
    "adaptive-learning",
    "embodied-cognition",
    "xapi",
    "blender-integration",
    "unity-integration"
  ],
  "author": "Elite VR Learning Development Team",
  "license": "MIT",
  "lint-staged": {
    "src/**/*.{ts,tsx}": [
      "eslint --fix",
      "prettier --write",
      "jest --bail --findRelatedTests --passWithNoTests"
    ]
  },
  "jest": {
    "preset": "ts-jest",
    "testEnvironment": "node",
    "testMatch": [
      "**/__tests__/**/*.test.ts",
      "**/?(*.)+(spec|test).ts"
    ],
    "collectCoverageFrom": [
      "src/**/*.ts",
      "!src/**/*.d.ts",
      "!src/types/**/*",
      "!src/**/__tests__/**/*"
    ],
    "coverageThreshold": {
      "global": {
        "branches": 85,
        "functions": 90,
        "lines": 90,
        "statements": 90
      }
    }
  }
}
```

This package configuration reflects several important architectural decisions. The dependency on `@modelcontextprotocol/sdk` ensures you're building on the official MCP foundation, while educational-specific packages like `xapi-statements` and `natural` enable the sophisticated learning analytics your system requires. The inclusion of Three.js and Cannon physics engine supports the spatial precision requirements you've documented, and the Quest 3 SDK integration enables direct communication with VR hardware.

### Unity Package Manifest (Packages/manifest.json)

```json
{
  "dependencies": {
    "com.unity.xr.interaction.toolkit": "2.5.2",
    "com.unity.xr.openxr": "1.9.1",
    "com.unity.xr.management": "4.4.0",
    "com.unity.render-pipelines.universal": "14.0.9",
    "com.unity.addressables": "1.21.19",
    "com.unity.analytics": "5.0.0",
    "com.unity.cinemachine": "2.9.7",
    "com.unity.inputsystem": "1.7.0",
    "com.unity.netcode.gameobjects": "1.7.1",
    "com.unity.services.core": "1.12.0",
    "com.unity.services.analytics": "5.0.0",
    "com.unity.ugui": "1.0.0",
    "com.unity.textmeshpro": "3.0.6",
    "com.unity.timeline": "1.7.6",
    "com.unity.mathematics": "1.3.1",
    "com.unity.collections": "2.2.1",
    "com.unity.burst": "1.8.12",
    "com.unity.jobs": "0.70.0-preview.7",
    "com.unity.probuilder": "5.2.2",
    "com.unity.test-framework": "1.3.9"
  },
  "scopedRegistries": [
    {
      "name": "Elite VR Learning Registry",
      "url": "https://registry.elite-vr-learning.com",
      "scopes": [
        "com.elite-vr-learning"
      ]
    },
    {
      "name": "Meta XR Registry",
      "url": "https://npm.developer.oculus.com",
      "scopes": [
        "com.meta.xr"
      ]
    }
  ],
  "testables": [
    "com.unity.xr.interaction.toolkit",
    "com.elite-vr-learning.educational-framework"
  ]
}
```

The Unity package selection prioritizes Quest 3 compatibility through OpenXR while maintaining performance optimization capabilities through URP and the Jobs system. The inclusion of Addressables supports your dynamic content loading requirements, essential for educational scenarios that adapt based on learner profiles.

### Python Requirements for Blender Integration

```txt
# Elite VR Learning MCP - Blender Integration Requirements
# Python 3.10+ compatibility for Blender 4.4 LTS

# Core Blender API Extensions
bpy>=4.0.0
bmesh>=1.0.0
mathutils>=3.0.0

# USD Integration for Unity Pipeline
usd-core>=23.08
pxr>=0.23.08

# Educational Asset Processing
numpy>=1.24.3
scipy>=1.11.1
scikit-learn>=1.3.0
opencv-python>=4.8.0.74
pillow>=10.0.0

# 3D Geometry and Optimization
trimesh>=3.23.5
pyglet>=2.0.10
networkx>=3.1
shapely>=2.0.1

# AI and Machine Learning for Content Generation
torch>=2.0.1
torchvision>=0.15.2
transformers>=4.33.2
diffusers>=0.20.2
accelerate>=0.21.0

# Educational Content Analysis
nltk>=3.8.1
spacy>=3.6.1
textblob>=0.17.1

# Data Processing and Analytics
pandas>=2.0.3
matplotlib>=3.7.2
seaborn>=0.12.2
plotly>=5.15.0

# API Integration and Communication
requests>=2.31.0
websockets>=11.0.3
aiohttp>=3.8.5
fastapi>=0.103.1
uvicorn>=0.23.2

# Testing and Quality Assurance
pytest>=7.4.2
pytest-asyncio>=0.21.1
pytest-cov>=4.1.0
black>=23.7.0
isort>=5.12.0
flake8>=6.1.0
mypy>=1.5.1

# Development and Debugging
ipython>=8.15.0
jupyter>=1.0.0
rich>=13.5.2
typer>=0.9.0

# Educational VR Specific
# Note: These would be your custom packages
elite-vr-educational-tools>=1.0.0
quest3-optimization-toolkit>=1.0.0
spatial-precision-manager>=1.0.0
```

This requirements file balances cutting-edge AI capabilities with educational stability. The inclusion of PyTorch and Transformers enables sophisticated content generation, while traditional scientific computing libraries like NumPy and SciPy provide the mathematical foundation for your spatial precision algorithms.

### Docker Development Environment

```dockerfile
# Elite VR Learning MCP Development Environment
FROM node:20-alpine AS base

# Install system dependencies for educational VR development
RUN apk add --no-cache \
    python3 \
    py3-pip \
    git \
    openssh \
    curl \
    wget \
    unzip \
    build-base \
    linux-headers \
    libc6-compat \
    && rm -rf /var/cache/apk/*

# Create development user with appropriate permissions
RUN addgroup -g 1001 -S developer && \
    adduser -S developer -u 1001 -G developer

WORKDIR /app

# Copy package files for dependency installation
COPY package*.json ./
COPY requirements.txt ./

# Install Node.js dependencies with educational VR optimizations
RUN npm ci --only=production && \
    npm cache clean --force

# Install Python dependencies for Blender integration
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy application source
COPY --chown=developer:developer . .

# Build the MCP server
RUN npm run build

# Switch to development user
USER developer

# Health check for MCP server
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:3000/health || exit 1

EXPOSE 3000 8080

# Development command with hot reload
CMD ["npm", "run", "dev"]
```

The Docker configuration creates a consistent development environment that matches your production requirements while enabling hot reload for rapid development iteration. The health check ensures your MCP server is responding correctly during development.

### Environment Variable Configuration

```env
# Elite VR Learning MCP - Environment Configuration Template
# Copy to .env for local development, customize for deployment stages

# Core Application Settings
NODE_ENV=development
PORT=3000
HOST=localhost
APP_NAME="Elite VR Learning MCP"
APP_VERSION=1.0.0

# MCP Protocol Configuration
MCP_PROTOCOL_VERSION=2024-11-05
MCP_SERVER_TIMEOUT=30000
MCP_MAX_CONCURRENT_REQUESTS=100
MCP_ENABLE_LOGGING=true

# Educational Context Configuration
EDUCATIONAL_FRAMEWORK=constructivist_embodied
LEARNING_ANALYTICS_ENABLED=true
XAPI_ENDPOINT=https://your-lrs-endpoint.com/xapi
XAPI_USERNAME=your_lrs_username
XAPI_PASSWORD=your_lrs_password
XAPI_VERSION=1.0.3

# Quest 3 Integration Settings
QUEST3_SDK_ENABLED=true
QUEST3_PERFORMANCE_TARGET=90
QUEST3_MIN_FRAMERATE=72
QUEST3_MAX_LATENCY=20
QUEST3_OPTIMIZATION_LEVEL=educational

# Blender Integration Configuration
BLENDER_EXECUTABLE_PATH=/usr/local/blender/blender
BLENDER_PYTHON_PATH=/usr/local/blender/python/bin/python3
BLENDER_SCRIPTS_PATH=./blender-scripts
BLENDER_EXPORT_QUALITY=high_educational

# Unity Integration Settings
UNITY_PROJECT_PATH=./unity-project
UNITY_BUILD_TARGET=Android
UNITY_XR_BACKEND=OpenXR
UNITY_RENDER_PIPELINE=URP
UNITY_OPTIMIZATION=quest3_educational

# Database Configuration
DATABASE_TYPE=mongodb
DATABASE_HOST=localhost
DATABASE_PORT=27017
DATABASE_NAME=elite_vr_learning
DATABASE_USER=elite_vr_user
DATABASE_PASSWORD=secure_educational_password

# Redis Configuration (for session management)
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0
REDIS_PASSWORD=redis_secure_password

# Security Configuration
JWT_SECRET=your_super_secure_jwt_secret_for_educational_privacy
JWT_EXPIRATION=24h
BCRYPT_ROUNDS=12
SESSION_SECRET=your_session_secret_for_educational_security

# File Storage Configuration
STORAGE_TYPE=local
STORAGE_PATH=./storage
MAX_FILE_SIZE=50MB
ALLOWED_FILE_TYPES=.blend,.usd,.fbx,.obj,.png,.jpg,.mp4

# Logging Configuration
LOG_LEVEL=info
LOG_FORMAT=combined
LOG_DIRECTORY=./logs
LOG_ROTATION=daily
LOG_MAX_SIZE=100MB

# Educational Privacy & Compliance
FERPA_COMPLIANCE=true
COPPA_COMPLIANCE=true
GDPR_COMPLIANCE=true
DATA_RETENTION_DAYS=2555  # 7 years for educational records
PRIVACY_BY_DESIGN=true

# Performance Monitoring
MONITORING_ENABLED=true
METRICS_COLLECTION=true
ERROR_TRACKING=sentry
SENTRY_DSN=your_sentry_dsn_for_error_tracking

# Development Tools
HOT_RELOAD=true
DEBUG_MODE=true
PROFILING_ENABLED=true
TESTING_DATABASE=elite_vr_learning_test
```

These environment variables provide comprehensive configuration options while maintaining security best practices through the use of environment-specific secrets. Notice how educational compliance settings are built into the configuration, reflecting the pedagogical focus of your system.

### Development Automation Scripts

```bash
#!/bin/bash
# Elite VR Learning MCP - Development Environment Setup Script
# ./scripts/setup-dev-env.sh

set -e

echo "🎓 Setting up Elite VR Learning MCP Development Environment..."

# Check system requirements
check_system_requirements() {
    echo "📋 Checking system requirements..."
    
    # Check Node.js version
    if ! command -v node &> /dev/null; then
        echo "❌ Node.js is required but not installed"
        exit 1
    fi
    
    NODE_VERSION=$(node --version | sed 's/v//')
    REQUIRED_NODE_VERSION="20.0.0"
    
    if [ "$(printf '%s\n' "$REQUIRED_NODE_VERSION" "$NODE_VERSION" | sort -V | head -n1)" != "$REQUIRED_NODE_VERSION" ]; then
        echo "❌ Node.js version $REQUIRED_NODE_VERSION or higher is required"
        exit 1
    fi
    
    # Check Python version for Blender integration
    if ! command -v python3 &> /dev/null; then
        echo "❌ Python 3.10+ is required for Blender integration"
        exit 1
    fi
    
    echo "✅ System requirements satisfied"
}

# Setup Node.js dependencies
setup_nodejs() {
    echo "📦 Installing Node.js dependencies..."
    npm ci
    echo "✅ Node.js dependencies installed"
}

# Setup Python environment for Blender
setup_python_environment() {
    echo "🐍 Setting up Python environment for Blender integration..."
    
    # Create virtual environment
    python3 -m venv venv-blender
    source venv-blender/bin/activate
    
    # Upgrade pip
    pip install --upgrade pip
    
    # Install requirements
    pip install -r requirements.txt
    
    echo "✅ Python environment configured"
}

# Setup Unity project structure
setup_unity_project() {
    echo "🎮 Configuring Unity project structure..."
    
    # Create Unity project directories if they don't exist
    mkdir -p unity-project/Assets/Scripts/Educational
    mkdir -p unity-project/Assets/Scripts/VR
    mkdir -p unity-project/Assets/Scripts/Analytics
    mkdir -p unity-project/Assets/Prefabs/Educational
    mkdir -p unity-project/Assets/Materials/Educational
    mkdir -p unity-project/Assets/Scenes/Educational
    
    echo "✅ Unity project structure created"
}

# Setup Blender integration
setup_blender_integration() {
    echo "🎨 Setting up Blender integration..."
    
    # Create Blender scripts directory
    mkdir -p blender-scripts/educational
    mkdir -p blender-scripts/optimization
    mkdir -p blender-scripts/export
    
    # Create Blender add-on structure
    mkdir -p blender-addons/elite_vr_learning
    
    echo "✅ Blender integration configured"
}

# Setup development tools
setup_development_tools() {
    echo "🔧 Configuring development tools..."
    
    # Setup Git hooks
    npx husky install
    
    # Create necessary directories
    mkdir -p logs
    mkdir -p storage/assets
    mkdir -p storage/exports
    mkdir -p storage/temp
    
    # Copy environment template
    if [ ! -f .env ]; then
        cp .env.template .env
        echo "📝 Environment template copied - please configure .env file"
    fi
    
    echo "✅ Development tools configured"
}

# Verify installation
verify_installation() {
    echo "🔍 Verifying installation..."
    
    # Run linting
    npm run lint
    
    # Run tests
    npm run test
    
    # Build project
    npm run build
    
    echo "✅ Installation verified successfully"
}

# Main execution
main() {
    check_system_requirements
    setup_nodejs
    setup_python_environment
    setup_unity_project
    setup_blender_integration
    setup_development_tools
    verify_installation
    
    echo ""
    echo "🎉 Elite VR Learning MCP Development Environment Setup Complete!"
    echo ""
    echo "Next steps:"
    echo "1. Configure your .env file with appropriate values"
    echo "2. Start development server: npm run dev"
    echo "3. Open Unity project in Unity Editor"
    echo "4. Install Blender add-ons from blender-addons/ directory"
    echo ""
    echo "📚 See README.md for detailed development guidelines"
}

main "$@"
```

This setup script automates the entire development environment configuration process, ensuring consistency across different development machines and reducing setup time from hours to minutes. The script includes comprehensive error checking and provides clear feedback about each step.

The project setup documents I've provided create a robust foundation for your educational VR development. Each configuration reflects the sophisticated requirements of your system: the Node.js setup enables your MCP server architecture, the Unity configuration optimizes for Quest 3 performance while maintaining educational flexibility, and the Python environment supports your advanced Blender integration needs.

The key insight behind these configurations is that they're not just development conveniences—they're integral to maintaining the quality and performance standards your educational VR system requires. The testing configurations ensure your adaptive learning algorithms work correctly, the Docker setup provides consistent environments for collaborative development, and the automation scripts reduce the cognitive load on developers so they can focus on creating exceptional educational experiences rather than wrestling with toolchain complexity.