# FIGHTER JET COCKPIT DEVELOPMENT - COMPREHENSIVE PROJECT RULES

## TABLE OF CONTENTS
1. [Project Overview](#project-overview)
2. [Mandatory Development Standards](#mandatory-development-standards)
3. [Technical Architecture Requirements](#technical-architecture-requirements)
4. [Quality Gates & Validation](#quality-gates--validation)
5. [Performance Requirements](#performance-requirements)
6. [Code Quality Standards](#code-quality-standards)
7. [Asset Management Rules](#asset-management-rules)
8. [Phase-Specific Requirements](#phase-specific-requirements)
9. [Testing & Validation Protocols](#testing--validation-protocols)
10. [Documentation Standards](#documentation-standards)
11. [Deployment & Production Rules](#deployment--production-rules)
12. [Maintenance & Support Guidelines](#maintenance--support-guidelines)

---

## PROJECT OVERVIEW

### Project Scope
This project aims to create a **studio-quality, photorealistic fighter jet cockpit** using Three.js that demonstrates advanced web-based 3D rendering capabilities. The final product must be indistinguishable from professional flight simulation software and serve as a showcase for cutting-edge web graphics technology.

### Target Audience
- **Primary**: Aviation enthusiasts and professionals
- **Secondary**: 3D graphics developers and WebGL enthusiasts
- **Tertiary**: General public interested in military aviation

### Success Criteria
- Photorealistic visual quality matching professional flight simulators
- Smooth 60 FPS performance on mid-range hardware
- Interactive functionality demonstrating real cockpit systems
- Cross-platform compatibility (desktop and mobile)
- Professional-grade code architecture suitable for production use

---

## MANDATORY DEVELOPMENT STANDARDS

### 1. TECHNOLOGY STACK RESTRICTIONS

#### **ABSOLUTE REQUIREMENTS**
- **Languages**: ONLY HTML5, CSS3, and Vanilla JavaScript ES6+
- **3D Library**: Three.js (latest stable version) - NO OTHER 3D FRAMEWORKS
- **Build Tools**: NONE - Pure vanilla implementation required
- **Frameworks**: STRICTLY FORBIDDEN - No React, Vue, Angular, Svelte, etc.
- **Preprocessors**: FORBIDDEN - No SASS, LESS, TypeScript, Babel, etc.
- **Bundlers**: NOT ALLOWED - No Webpack, Rollup, Parcel, Vite, etc.

#### **PERMITTED LIBRARIES** (Limited Exceptions)
- Three.js core library and official examples
- Web APIs (WebGL, Web Audio, etc.)
- Standard browser APIs only

### 2. CODE COMPLETENESS MANDATE

#### **ZERO PLACEHOLDER POLICY**
- **NEVER** use placeholders like `...`, `[rest of code]`, `// TODO`, or `// Implementation here`
- **ALL** functions must be fully implemented with complete logic
- **ALL** variables must be properly declared, initialized, and used
- **ALL** classes must have complete method implementations
- **ALL** event handlers must be fully functional

#### **IMPLEMENTATION VERIFICATION**
Before submitting any code:
- ✅ Every function has a complete implementation
- ✅ All variables are properly defined and initialized
- ✅ No syntax errors or undefined references
- ✅ All imports/exports are correctly specified
- ✅ Code executes without runtime errors

### 3. CROSS-FILE CONSISTENCY REQUIREMENTS

#### **NAMING CONSISTENCY**
- **HTML IDs/Classes** must match exactly with CSS selectors and JavaScript references
- **CSS Class Names** must follow consistent naming convention (kebab-case)
- **JavaScript Variables** must use camelCase consistently
- **File Names** must use kebab-case for consistency

#### **DEPENDENCY MANAGEMENT**
- All file dependencies must be explicitly documented
- Load order must be clearly specified
- No circular dependencies allowed
- All external resources must have fallback handling

---

## TECHNICAL ARCHITECTURE REQUIREMENTS

### 1. WEBGL & RENDERING STANDARDS

#### **WebGL 2.0 REQUIREMENTS**
- **Mandatory**: WebGL 2.0 context with fallback to WebGL 1.0
- **Extensions**: Must detect and utilize all available WebGL extensions
- **Error Handling**: Comprehensive WebGL error detection and recovery
- **Context Loss**: Proper handling of WebGL context loss/restore

#### **RENDERING PIPELINE SPECIFICATIONS**
```javascript
// MANDATORY Renderer Configuration
const renderer = new THREE.WebGLRenderer({
    canvas: canvas,
    antialias: true,
    alpha: false,
    powerPreference: "high-performance",
    stencil: false,
    depth: true,
    logarithmicDepthBuffer: true
});

// REQUIRED Settings
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap;
renderer.physicallyCorrectLights = true;
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 1.0;
renderer.outputEncoding = THREE.sRGBEncoding;
```

### 2. SCENE ARCHITECTURE STANDARDS

#### **COORDINATE SYSTEM**
- **Forward**: Negative Z-axis (-Z)
- **Up**: Positive Y-axis (+Y)
- **Right**: Positive X-axis (+X)
- **Units**: Meters (1 unit = 1 meter)
- **Scale**: Real-world proportions mandatory

#### **CAMERA SPECIFICATIONS**
```javascript
// MANDATORY Camera Setup
const camera = new THREE.PerspectiveCamera(
    75,                                    // FOV (field of view)
    window.innerWidth / window.innerHeight, // Aspect ratio
    0.01,                                  // Near clipping plane
    1000                                   // Far clipping plane
);

// Pilot Eye Position (REQUIRED)
camera.position.set(0, 1.2, 0.3); // X, Y, Z in meters
```

### 3. LIGHTING SYSTEM REQUIREMENTS

#### **LIGHTING HIERARCHY** (All Required)
1. **Primary Directional Light**: Sun/external lighting through canopy
2. **Ambient Light**: Global illumination (low intensity)
3. **Point Lights**: Instrument backlighting (minimum 8 lights)
4. **Spot Lights**: Focused task lighting (minimum 4 lights)
5. **Emissive Materials**: Display screens and indicators

#### **SHADOW SYSTEM SPECIFICATIONS**
```javascript
// MANDATORY Shadow Configuration
directionalLight.castShadow = true;
directionalLight.shadow.mapSize.width = 2048;
directionalLight.shadow.mapSize.height = 2048;
directionalLight.shadow.camera.near = 0.5;
directionalLight.shadow.camera.far = 50;
directionalLight.shadow.camera.left = -10;
directionalLight.shadow.camera.right = 10;
directionalLight.shadow.camera.top = 10;
directionalLight.shadow.camera.bottom = -10;
directionalLight.shadow.bias = -0.0001;
```

---

## QUALITY GATES & VALIDATION

### 1. PHASE COMPLETION CRITERIA

#### **PHASE ADVANCEMENT RULES**
- **NO** advancement to next phase without completing ALL requirements of current phase
- **ALL** validation checkpoints must pass before proceeding
- **ALL** performance benchmarks must be met
- **ALL** visual quality standards must be achieved

#### **VALIDATION CHECKPOINT TEMPLATE**
```markdown
## Phase X.Y Validation Checklist
- [ ] All code compiles without errors
- [ ] All features function as specified
- [ ] Performance benchmarks met
- [ ] Visual quality meets standards
- [ ] Cross-browser compatibility verified
- [ ] Memory usage within limits
- [ ] No console errors or warnings
- [ ] User interaction works correctly
```

### 2. VISUAL QUALITY STANDARDS

#### **PHOTOREALISM REQUIREMENTS**
- **Materials**: Must be indistinguishable from real-world references
- **Lighting**: Must accurately simulate real cockpit lighting conditions
- **Textures**: Minimum 4K resolution for primary surfaces
- **Details**: Must withstand close inspection (0.1m viewing distance)
- **Animations**: Must be smooth and realistic (no stuttering or popping)

#### **REFERENCE VALIDATION**
- All visual elements must be compared against real F-22/F-35 cockpit photographs
- Color accuracy must be validated against known military specifications
- Proportions must match real-world measurements within 2% tolerance
- Surface materials must exhibit correct physical properties (reflectance, roughness, etc.)

### 3. FUNCTIONAL REQUIREMENTS

#### **INTERACTIVITY STANDARDS**
- **Response Time**: All interactions must respond within 16ms (60 FPS)
- **Feedback**: Visual and/or audio feedback required for all interactive elements
- **State Management**: All control states must be persistent and consistent
- **Error Handling**: Graceful handling of invalid user inputs

#### **SYSTEM INTEGRATION**
- All cockpit systems must be functionally interconnected
- Display content must update in real-time based on control inputs
- Warning systems must activate appropriately
- Navigation systems must provide accurate information

---

## PERFORMANCE REQUIREMENTS

### 1. FRAME RATE STANDARDS

#### **MINIMUM PERFORMANCE TARGETS**
- **Desktop (Mid-range)**: 60 FPS sustained, 45 FPS minimum
- **Desktop (Low-end)**: 45 FPS sustained, 30 FPS minimum
- **Mobile (High-end)**: 30 FPS sustained, 24 FPS minimum
- **Mobile (Mid-range)**: 24 FPS sustained, 20 FPS minimum

#### **PERFORMANCE MONITORING**
```javascript
// MANDATORY Performance Monitoring
class PerformanceMonitor {
    constructor() {
        this.frameCount = 0;
        this.lastTime = performance.now();
        this.fps = 0;
        this.frameTime = 0;
        this.memoryUsage = 0;
    }
    
    update() {
        const currentTime = performance.now();
        this.frameTime = currentTime - this.lastTime;
        this.lastTime = currentTime;
        this.frameCount++;
        
        if (this.frameCount % 60 === 0) {
            this.fps = 1000 / this.frameTime;
            this.memoryUsage = performance.memory ? 
                performance.memory.usedJSHeapSize / 1024 / 1024 : 0;
            
            // Log performance warnings
            if (this.fps < 45) {
                console.warn(`Low FPS detected: ${this.fps.toFixed(1)}`);
            }
            if (this.memoryUsage > 512) {
                console.warn(`High memory usage: ${this.memoryUsage.toFixed(1)}MB`);
            }
        }
    }
}
```

### 2. MEMORY USAGE LIMITS

#### **MEMORY ALLOCATION TARGETS**
- **Desktop**: Maximum 2GB total, 1GB for textures
- **Mobile**: Maximum 1GB total, 512MB for textures
- **Geometry**: Maximum 256MB for all 3D models
- **Audio**: Maximum 128MB for all audio assets

#### **MEMORY OPTIMIZATION REQUIREMENTS**
- Implement texture compression (DXT/ETC formats)
- Use geometry instancing for repeated objects
- Implement Level of Detail (LOD) systems
- Proper disposal of unused resources
- Memory leak prevention and detection

### 3. LOADING TIME REQUIREMENTS

#### **LOADING PERFORMANCE TARGETS**
- **Initial Load**: Maximum 10 seconds on broadband (25 Mbps)
- **Asset Streaming**: Maximum 2 seconds for individual assets
- **Scene Transitions**: Maximum 1 second between modes
- **Progressive Loading**: Visible content within 3 seconds

#### **LOADING OPTIMIZATION STRATEGIES**
- Implement progressive asset loading
- Use texture streaming for large assets
- Compress all assets appropriately
- Implement efficient caching strategies
- Provide meaningful loading progress indicators

---

## CODE QUALITY STANDARDS

### 1. JAVASCRIPT CODING STANDARDS

#### **ES6+ REQUIREMENTS**
```javascript
// MANDATORY: Use modern JavaScript features
class CockpitSystem {
    constructor(options = {}) {
        this.name = options.name ?? 'Unknown System';
        this.enabled = options.enabled ?? false;
        this.components = new Map();
        this.eventListeners = new Set();
    }
    
    // Use arrow functions for methods when appropriate
    initialize = async () => {
        try {
            await this.loadAssets();
            this.setupEventListeners();
            this.enabled = true;
        } catch (error) {
            console.error(`Failed to initialize ${this.name}:`, error);
            throw error;
        }
    }
    
    // Use destructuring and spread operators
    updateComponent(id, { position, rotation, scale, ...properties }) {
        const component = this.components.get(id);
        if (!component) {
            throw new Error(`Component ${id} not found`);
        }
        
        Object.assign(component, {
            position: position ?? component.position,
            rotation: rotation ?? component.rotation,
            scale: scale ?? component.scale,
            ...properties
        });
    }
}
```

#### **ERROR HANDLING REQUIREMENTS**
- **ALL** functions must have proper error handling
- **ALL** async operations must use try-catch blocks
- **ALL** user inputs must be validated
- **ALL** external resource loading must handle failures gracefully

### 2. DOCUMENTATION STANDARDS

#### **INLINE DOCUMENTATION REQUIREMENTS**
```javascript
/**
 * Manages the primary flight display system
 * @class PrimaryFlightDisplay
 * @description Handles attitude indicator, altitude, airspeed, and heading information
 */
class PrimaryFlightDisplay {
    /**
     * Creates a new Primary Flight Display
     * @param {Object} options - Configuration options
     * @param {number} options.width - Display width in pixels (default: 512)
     * @param {number} options.height - Display height in pixels (default: 512)
     * @param {string} options.colorScheme - Color scheme ('green'|'amber'|'white')
     * @throws {Error} When invalid dimensions are provided
     */
    constructor(options = {}) {
        // Implementation with full documentation
    }
    
    /**
     * Updates the attitude indicator
     * @param {number} pitch - Pitch angle in degrees (-90 to 90)
     * @param {number} roll - Roll angle in degrees (-180 to 180)
     * @param {number} heading - Heading in degrees (0 to 360)
     * @returns {void}
     * @throws {RangeError} When angles are outside valid ranges
     */
    updateAttitude(pitch, roll, heading) {
        // Validate inputs
        if (pitch < -90 || pitch > 90) {
            throw new RangeError(`Invalid pitch angle: ${pitch}. Must be between -90 and 90 degrees.`);
        }
        // Full implementation...
    }
}
```

### 3. FILE ORGANIZATION STANDARDS

#### **DIRECTORY STRUCTURE** (Mandatory)
```
fighter-jet-cockpit/
├── index.html                 # Main entry point
├── styles.css                 # Global styles
├── main.js                    # Application entry point
├── src/
│   ├── core/                  # Core engine components
│   │   ├── Renderer.js        # WebGL renderer management
│   │   ├── SceneManager.js    # Scene graph management
│   │   ├── AssetManager.js    # Asset loading and caching
│   │   ├── InputManager.js    # User input handling
│   │   └── PerformanceManager.js # Performance monitoring
│   ├── systems/               # Cockpit systems
│   │   ├── FlightDisplays.js  # Flight display systems
│   │   ├── NavigationSystem.js # Navigation and GPS
│   │   ├── WeaponSystems.js   # Weapon management
│   │   └── EnvironmentalSystems.js # Environmental controls
│   ├── components/            # Reusable components
│   │   ├── Switch.js          # Switch controls
│   │   ├── Button.js          # Button controls
│   │   ├── Display.js         # Display screens
│   │   └── Indicator.js       # Status indicators
│   ├── materials/             # Material definitions
│   │   ├── MetalMaterials.js  # Metal surface materials
│   │   ├── PlasticMaterials.js # Plastic surface materials
│   │   └── GlassMaterials.js  # Glass and transparent materials
│   ├── shaders/               # Custom GLSL shaders
│   │   ├── cockpit.vert       # Vertex shaders
│   │   ├── cockpit.frag       # Fragment shaders
│   │   └── post-processing/   # Post-processing shaders
│   └── utils/                 # Utility functions
│       ├── MathUtils.js       # Mathematical utilities
│       ├── ColorUtils.js      # Color manipulation
│       └── ValidationUtils.js # Input validation
├── assets/                    # Static assets
│   ├── models/                # 3D models
│   ├── textures/              # Texture maps
│   ├── audio/                 # Audio files
│   └── fonts/                 # Typography assets
├── docs/                      # Documentation
└── tests/                     # Test files
```

---

## ASSET MANAGEMENT RULES

### 1. 3D MODEL REQUIREMENTS

#### **MODEL SPECIFICATIONS**
- **Format**: glTF 2.0 (.glb) preferred, OBJ/MTL as fallback
- **Polygon Count**: Maximum 100K triangles per major component
- **UV Mapping**: Non-overlapping UVs, 0-1 space utilization >90%
- **Normals**: Smooth normals with proper hard edges where appropriate
- **Materials**: PBR workflow (Albedo, Normal, Roughness, Metallic, AO)

#### **GEOMETRY OPTIMIZATION**
```javascript
// MANDATORY Geometry Optimization
class GeometryOptimizer {
    static optimizeGeometry(geometry) {
        // Remove duplicate vertices
        geometry.mergeVertices();
        
        // Compute vertex normals if missing
        if (!geometry.attributes.normal) {
            geometry.computeVertexNormals();
        }
        
        // Compute tangents for normal mapping
        if (geometry.attributes.uv && !geometry.attributes.tangent) {
            geometry.computeTangents();
        }
        
        // Optimize for GPU cache
        geometry = BufferGeometryUtils.mergeVertices(geometry);
        
        return geometry;
    }
}
```

### 2. TEXTURE REQUIREMENTS

#### **TEXTURE SPECIFICATIONS**
- **Resolution**: 4K (4096x4096) for primary surfaces, 2K for secondary
- **Format**: PNG for albedo/normal, JPG for roughness/metallic/AO
- **Compression**: Use basis universal when supported
- **Mipmaps**: Generate full mipmap chains for all textures
- **Color Space**: sRGB for albedo, Linear for all other maps

#### **TEXTURE OPTIMIZATION**
```javascript
// MANDATORY Texture Loading and Optimization
class TextureManager {
    static loadTexture(url, options = {}) {
        const loader = new THREE.TextureLoader();
        const texture = loader.load(url);
        
        // Apply standard settings
        texture.wrapS = THREE.RepeatWrapping;
        texture.wrapT = THREE.RepeatWrapping;
        texture.generateMipmaps = true;
        texture.minFilter = THREE.LinearMipmapLinearFilter;
        texture.magFilter = THREE.LinearFilter;
        texture.anisotropy = Math.min(4, renderer.capabilities.getMaxAnisotropy());
        
        // Set color space based on texture type
        if (options.isAlbedo) {
            texture.encoding = THREE.sRGBEncoding;
        }
        
        return texture;
    }
}
```

### 3. AUDIO REQUIREMENTS

#### **AUDIO SPECIFICATIONS**
- **Format**: OGG Vorbis primary, MP3 fallback
- **Quality**: 44.1kHz, 16-bit minimum
- **Compression**: Variable bitrate, 128kbps average
- **3D Audio**: Positional audio for all cockpit sounds
- **Mixing**: Proper audio ducking and level management

---

## PHASE-SPECIFIC REQUIREMENTS

### PHASE 1: FOUNDATION & RENDERING PIPELINE

#### **Phase 1.1: Project Architecture Setup**
**Validation Criteria:**
- [ ] Complete file structure created with all required directories
- [ ] WebGL 2.0 context initializes successfully with fallback
- [ ] Error handling system catches and reports all issues
- [ ] Performance monitoring displays real-time metrics
- [ ] Memory usage baseline established (<100MB)
- [ ] Cross-browser compatibility verified (Chrome, Firefox, Safari, Edge)

**Performance Benchmarks:**
- 60 FPS empty scene rendering
- <500ms initial load time for core files
- <50MB memory usage for basic setup
- Error-free console output

#### **Phase 1.2: Advanced Renderer Configuration**
**Validation Criteria:**
- [ ] HDR rendering pipeline functional with tone mapping
- [ ] Shadow system renders correctly with PCF soft shadows
- [ ] Anti-aliasing eliminates jagged edges effectively
- [ ] Post-processing effects enhance visual quality
- [ ] Color management maintains accuracy throughout pipeline
- [ ] Performance impact within acceptable limits

**Performance Benchmarks:**
- HDR pipeline: <5% performance impact
- Shadow system: <20% performance impact
- Anti-aliasing: <15% performance impact
- Combined system: >45 FPS on mid-range GPU

#### **Phase 1.3: Asset Streaming System**
**Validation Criteria:**
- [ ] Progressive loading provides smooth user experience
- [ ] All supported asset formats load without errors
- [ ] Caching system reduces redundant downloads
- [ ] Error recovery handles network failures gracefully
- [ ] Loading progress accurately reflects actual progress
- [ ] Memory management prevents leaks during streaming

**Performance Benchmarks:**
- Texture loading: <2s for 4K textures
- Geometry loading: <1s for complex models
- Cache hit ratio: >80% for repeated assets
- Memory efficiency: >90% effective usage

### PHASE 2: LIGHTING & MATERIALS

#### **Phase 2.1: Physically Accurate Lighting**
**Validation Criteria:**
- [ ] Sun position calculations match real-world solar data
- [ ] Sky model produces realistic atmospheric colors
- [ ] Interior lighting provides appropriate illumination levels
- [ ] Light temperature and intensity values are physically accurate
- [ ] Shadows enhance depth perception and realism
- [ ] Performance remains smooth with full lighting system

**Performance Benchmarks:**
- Sky rendering: <3ms per frame
- Atmospheric scattering: <2ms per frame
- Interior lighting: <1ms per frame
- Total lighting overhead: <15% of frame time

#### **Phase 2.2: Advanced PBR+ Materials**
**Validation Criteria:**
- [ ] All materials exhibit physically correct behavior
- [ ] Fresnel effects are accurate for all material types
- [ ] Roughness and metallic properties render correctly
- [ ] Advanced features (clearcoat, anisotropy) enhance realism
- [ ] Material switching works without visual artifacts
- [ ] Weathering effects add authentic aging appearance

**Performance Benchmarks:**
- Material shader compilation: <500ms total
- Per-material rendering overhead: <0.1ms
- Texture memory usage: <512MB for all materials
- Material switching: <1ms delay

### PHASE 3: GEOMETRY & ARCHITECTURE

#### **Phase 3.1: Cockpit Spatial Layout**
**Validation Criteria:**
- [ ] Cockpit dimensions match real fighter jet specifications
- [ ] Pilot viewing angles and ergonomics are accurate
- [ ] All major components are positioned correctly
- [ ] Coordinate system is consistent throughout
- [ ] Collision detection works for interactive elements
- [ ] Scale relationships are maintained accurately

#### **Phase 3.2: Detailed Component Modeling**
**Validation Criteria:**
- [ ] All components have appropriate level of detail
- [ ] UV mapping is efficient and artifact-free
- [ ] Geometry topology supports smooth shading
- [ ] Interactive elements have proper collision geometry
- [ ] Manufacturing details add authenticity
- [ ] Performance impact is within acceptable limits

---

## TESTING & VALIDATION PROTOCOLS

### 1. AUTOMATED TESTING REQUIREMENTS

#### **UNIT TESTING**
```javascript
// MANDATORY Test Structure
class CockpitSystemTest {
    static runAllTests() {
        console.log('Running Cockpit System Tests...');
        
        this.testRendererInitialization();
        this.testAssetLoading();
        this.testUserInteraction();
        this.testPerformanceMetrics();
        this.testErrorHandling();
        
        console.log('All tests completed.');
    }
    
    static testRendererInitialization() {
        console.log('Testing renderer initialization...');
        
        const canvas = document.createElement('canvas');
        const renderer = new THREE.WebGLRenderer({ canvas });
        
        console.assert(renderer.getContext(), 'WebGL context should be created');
        console.assert(renderer.capabilities.isWebGL2, 'WebGL 2.0 should be supported');
        
        console.log('✓ Renderer initialization test passed');
    }
    
    // Additional test methods...
}
```

#### **PERFORMANCE TESTING**
```javascript
// MANDATORY Performance Validation
class PerformanceValidator {
    static validateFrameRate(targetFPS = 60, duration = 5000) {
        return new Promise((resolve) => {
            const startTime = performance.now();
            let frameCount = 0;
            let minFPS = Infinity;
            let maxFPS = 0;
            
            function measureFrame() {
                frameCount++;
                const currentTime = performance.now();
                const elapsed = currentTime - startTime;
                
                if (elapsed >= 1000) { // Calculate FPS every second
                    const fps = frameCount / (elapsed / 1000);
                    minFPS = Math.min(minFPS, fps);
                    maxFPS = Math.max(maxFPS, fps);
                    frameCount = 0;
                }
                
                if (elapsed < duration) {
                    requestAnimationFrame(measureFrame);
                } else {
                    resolve({
                        averageFPS: frameCount / (elapsed / 1000),
                        minFPS,
                        maxFPS,
                        passed: minFPS >= targetFPS * 0.75 // Allow 25% tolerance
                    });
                }
            }
            
            requestAnimationFrame(measureFrame);
        });
    }
}
```

### 2. CROSS-BROWSER TESTING

#### **BROWSER COMPATIBILITY MATRIX**
| Feature | Chrome | Firefox | Safari | Edge | Mobile Chrome | Mobile Safari |
|---------|--------|---------|--------|------|---------------|---------------|
| WebGL 2.0 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| HDR Rendering | ✅ | ✅ | ✅ | ✅ | ⚠️ | ⚠️ |
| Shadow Mapping | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Post Processing | ✅ | ✅ | ✅ | ✅ | ⚠️ | ⚠️ |
| Audio API | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

**Legend:**
- ✅ Full Support
- ⚠️ Limited Support (may require fallbacks)
- ❌ Not Supported

### 3. USER ACCEPTANCE TESTING

#### **USABILITY TESTING CHECKLIST**
- [ ] Intuitive navigation without instructions
- [ ] Responsive feedback for all interactions
- [ ] Clear visual hierarchy and information organization
- [ ] Accessible design for users with disabilities
- [ ] Consistent behavior across different devices
- [ ] Graceful degradation on lower-end hardware

---

## DOCUMENTATION STANDARDS

### 1. CODE DOCUMENTATION

#### **INLINE DOCUMENTATION REQUIREMENTS**
- **ALL** classes must have comprehensive JSDoc comments
- **ALL** public methods must document parameters and return values
- **ALL** complex algorithms must have explanatory comments
- **ALL** configuration options must be documented with examples

### 2. TECHNICAL DOCUMENTATION

#### **ARCHITECTURE DOCUMENTATION**
- System architecture diagrams showing component relationships
- Data flow diagrams for complex interactions
- Performance optimization strategies and their implementations
- Browser compatibility notes and fallback strategies

#### **API DOCUMENTATION**
- Complete API reference for all public interfaces
- Usage examples for common scenarios
- Error handling and troubleshooting guides
- Performance considerations for each API

### 3. USER DOCUMENTATION

#### **USER GUIDE REQUIREMENTS**
- Interactive tutorial for first-time users
- Comprehensive control reference
- Troubleshooting guide for common issues
- System requirements and compatibility information

---

## DEPLOYMENT & PRODUCTION RULES

### 1. BUILD PROCESS

#### **PRODUCTION BUILD REQUIREMENTS**
- Asset minification and compression
- Progressive Web App (PWA) configuration
- Service worker implementation for offline capability
- CDN integration for global performance
- Error reporting and analytics integration

### 2. PERFORMANCE MONITORING

#### **PRODUCTION MONITORING**
```javascript
// MANDATORY Production Monitoring
class ProductionMonitor {
    constructor() {
        this.metrics = {
            loadTime: 0,
            fps: 0,
            memoryUsage: 0,
            errorCount: 0,
            userInteractions: 0
        };
        
        this.setupErrorReporting();
        this.setupPerformanceTracking();
        this.setupUserAnalytics();
    }
    
    setupErrorReporting() {
        window.addEventListener('error', (event) => {
            this.reportError({
                message: event.message,
                filename: event.filename,
                lineno: event.lineno,
                colno: event.colno,
                stack: event.error?.stack
            });
        });
        
        window.addEventListener('unhandledrejection', (event) => {
            this.reportError({
                message: 'Unhandled Promise Rejection',
                reason: event.reason
            });
        });
    }
    
    reportError(errorData) {
        // Send error data to monitoring service
        console.error('Production Error:', errorData);
        
        // Implement actual error reporting here
        // Example: send to analytics service, log to server, etc.
    }
}
```

### 3. SECURITY REQUIREMENTS

#### **SECURITY CHECKLIST**
- [ ] Content Security Policy (CSP) implemented
- [ ] All external resources loaded over HTTPS
- [ ] No sensitive data exposed in client-side code
- [ ] Input validation for all user interactions
- [ ] Proper error handling without information disclosure

---

## MAINTENANCE & SUPPORT GUIDELINES

### 1. VERSION CONTROL

#### **GIT WORKFLOW REQUIREMENTS**
- **Branching Strategy**: GitFlow with feature branches
- **Commit Messages**: Conventional Commits format
- **Code Reviews**: Required for all changes
- **Testing**: All tests must pass before merge

#### **COMMIT MESSAGE FORMAT**
```
type(scope): description

[optional body]

[optional footer]
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes
- `refactor`: Code refactoring
- `test`: Test additions or modifications
- `chore`: Maintenance tasks

### 2. ISSUE TRACKING

#### **BUG REPORT TEMPLATE**
```markdown
## Bug Report

### Description
Brief description of the issue

### Steps to Reproduce
1. Step one
2. Step two
3. Step three

### Expected Behavior
What should happen

### Actual Behavior
What actually happens

### Environment
- Browser: [e.g., Chrome 95.0.4638.69]
- OS: [e.g., Windows 10]
- Device: [e.g., Desktop, Mobile]
- Screen Resolution: [e.g., 1920x1080]

### Additional Information
Any additional context or screenshots
```

### 3. PERFORMANCE MONITORING

#### **CONTINUOUS MONITORING**
- Real-time performance metrics collection
- Automated alerts for performance degradation
- Regular performance regression testing
- User experience metrics tracking

---

## COMPLIANCE & STANDARDS

### 1. WEB STANDARDS COMPLIANCE

#### **ACCESSIBILITY (WCAG 2.1 AA)**
- [ ] Keyboard navigation support
- [ ] Screen reader compatibility
- [ ] Color contrast ratios meet requirements
- [ ] Alternative text for visual elements
- [ ] Focus indicators clearly visible

#### **PERFORMANCE (Web Vitals)**
- [ ] Largest Contentful Paint (LCP) < 2.5s
- [ ] First Input Delay (FID) < 100ms
- [ ] Cumulative Layout Shift (CLS) < 0.1

### 2. BROWSER STANDARDS

#### **PROGRESSIVE ENHANCEMENT**
- Core functionality works without JavaScript
- Enhanced features activate progressively
- Graceful degradation on unsupported browsers
- Responsive design for all screen sizes

---

## CONCLUSION

These comprehensive project rules ensure the development of a professional-grade, photorealistic fighter jet cockpit demonstration that meets the highest standards of web-based 3D graphics. Adherence to these rules is mandatory for all development phases, and any deviations must be explicitly approved and documented.

**Remember**: The goal is not just to create a functional demo, but to establish a new benchmark for what's possible with web-based 3D graphics technology. Every line of code, every texture, and every interaction should reflect this commitment to excellence.

---

*Last Updated: [Current Date]*
*Version: 1.0*
*Status: Active*
