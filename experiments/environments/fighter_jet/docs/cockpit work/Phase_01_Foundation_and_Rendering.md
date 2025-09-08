# PHASE 1: ADVANCED PROJECT FOUNDATION & RENDERING PIPELINE

## PROJECT RULES & CONSTRAINTS

### MANDATORY DEVELOPMENT RULES FOR ALL PHASES:

1. **LANGUAGE RESTRICTIONS**: 
   - Use ONLY HTML, CSS, and Vanilla JavaScript
   - NO frameworks, libraries, or preprocessors except Three.js
   - NO React, Vue, Angular, TypeScript, SASS, or any build tools

2. **CODE COMPLETENESS**: 
   - Provide COMPLETE, executable code for every prompt
   - NEVER use placeholders like "..." or "[rest of code]"
   - All functions must be fully implemented
   - All variables must be properly defined and initialized

3. **CROSS-FILE CONSISTENCY**: 
   - Maintain perfect alignment between HTML, CSS, and JavaScript
   - Ensure all class names, IDs, and selectors match across files
   - Verify DOM manipulation targets correct HTML elements

4. **QUALITY GATES**: 
   - Each phase MUST pass validation before proceeding
   - Identify and fix ALL gaps that could limit final quality
   - No phase advancement without successful completion verification

5. **PERFORMANCE REQUIREMENTS**: 
   - Maintain 60 FPS on mid-range hardware
   - Memory usage must not exceed 2GB on desktop, 1GB on mobile
   - Loading time must not exceed 10 seconds on broadband

## PRE-PHASE 1 VALIDATION:
**CURSOR MUST CHECK:**
```
✓ Project directory structure is empty or properly initialized
✓ Development environment supports WebGL 2.0
✓ Browser developer tools are accessible
✓ No conflicting files or dependencies exist
```

## Prompt 1.1: Enterprise-Grade Project Architecture Setup

**PREREQUISITE VALIDATION**: None (Initial setup)

**CURSOR RULES FOR THIS PROMPT**:
1. Create COMPLETE file structure with all necessary files
2. Implement FULL error handling and graceful degradation
3. NO placeholder code - everything must be functional
4. Must support both development and production environments

**DETAILED IMPLEMENTATION**:
```
Create a professional Three.js project with the following COMPLETE architecture:

PROJECT STRUCTURE (create ALL files with FULL implementation):
├── index.html
├── src/
│   ├── main.js (COMPLETE entry point with module system)
│   ├── core/
│   │   ├── Renderer.js (FULL WebGL 2.0 renderer with ALL extensions)
│   │   ├── SceneManager.js (COMPLETE scene graph management)
│   │   ├── AssetManager.js (FULL progressive loading with queue management)
│   │   ├── PerformanceManager.js (COMPLETE adaptive quality system)
│   │   ├── InputManager.js (FULL input handling for all devices)
│   │   ├── ErrorHandler.js (COMPREHENSIVE error handling system)
│   │   └── EventSystem.js (COMPLETE event dispatch system)
│   ├── utils/
│   │   ├── MathUtils.js (FULL mathematical utility functions)
│   │   ├── GeometryUtils.js (COMPLETE geometry helper functions)
│   │   ├── ColorUtils.js (FULL color space conversion utilities)
│   │   └── ValidationUtils.js (COMPLETE validation and testing utilities)
│   └── config/
│       ├── RenderConfig.js (FULL rendering configuration)
│       ├── QualitySettings.js (COMPLETE quality preset definitions)
│       └── Constants.js (ALL project constants and enumerations)
├── assets/ (create directory structure with README files)
│   ├── models/
│   ├── textures/
│   ├── audio/
│   └── shaders/
├── styles.css (COMPLETE styling with responsive design)
└── README.md (FULL project documentation)

MANDATORY IMPLEMENTATION REQUIREMENTS:

1. index.html MUST include:
   - Proper DOCTYPE and meta tags for performance
   - Complete viewport configuration for all devices
   - Full WebGL context setup with error handling
   - Loading screen with progress indication
   - Proper ARIA attributes for accessibility
   - Meta tags for SEO and social sharing

2. main.js MUST implement:
   - Complete module loading system without build tools
   - Full error boundary with user-friendly error messages
   - Complete performance monitoring from startup
   - Full window resize handling with proper debouncing
   - Complete visibility API integration for performance
   - Proper memory leak prevention

3. Renderer.js MUST include:
   - ALL WebGL 2.0 extensions with feature detection
   - Complete HDR rendering pipeline setup
   - Full shadow system with multiple techniques
   - Complete anti-aliasing with multiple methods
   - Full color management with proper gamma
   - Complete performance monitoring integration

4. SceneManager.js MUST implement:
   - Full scene graph with hierarchical transforms
   - Complete culling system (frustum + occlusion)
   - Full LOD system with smooth transitions
   - Complete object pooling for dynamic objects
   - Full spatial partitioning for performance
   - Complete scene serialization/deserialization

VALIDATION CHECKPOINT:
After implementation, CURSOR MUST verify:
✓ All files compile without errors
✓ WebGL context initializes successfully
✓ Performance monitoring shows baseline metrics
✓ Error handling catches and reports issues properly
✓ Loading system works without placeholder content
✓ Memory usage is within acceptable limits (<100MB initially)

QUALITY GATE:
✓ 60 FPS empty scene rendering
✓ Error-free console output
✓ Proper responsive behavior on all screen sizes
✓ All utility functions have comprehensive error handling
✓ Complete documentation in code comments
```

**GAP IDENTIFICATION FOR PHASE 1.1**:
```
CURSOR MUST CHECK FOR THESE POTENTIAL GAPS:
❌ Missing error handling that could cause silent failures
❌ Incomplete WebGL extension support limiting visual quality
❌ Missing performance monitoring preventing optimization
❌ Inadequate memory management causing leaks
❌ Missing responsive design breaking mobile experience
❌ Incomplete module system causing loading issues
❌ Missing accessibility features limiting user access
❌ Inadequate browser compatibility testing
```

## Prompt 1.2: Cinema-Quality Renderer Configuration

**PREREQUISITE VALIDATION**:
```
CURSOR MUST VERIFY FROM PHASE 1.1:
✓ Renderer.js exists and initializes WebGL context
✓ SceneManager.js successfully creates and manages scenes
✓ PerformanceManager.js reports baseline metrics
✓ No console errors from previous implementation
✓ Memory usage baseline is established (<100MB)
```

**CURSOR RULES FOR THIS PROMPT**:
1. MUST implement ALL advanced rendering features, no exceptions
2. Each feature MUST have fallback for unsupported hardware
3. MUST validate each feature works before proceeding to next
4. Performance impact of each feature MUST be measured and optimized

**DETAILED IMPLEMENTATION**:
```
Configure the WebGL renderer for photorealistic, film-quality output with COMPLETE implementation:

MANDATORY ADVANCED RENDERING FEATURES:

1. HDR RENDERING PIPELINE (COMPLETE IMPLEMENTATION REQUIRED):
   - MUST implement floating-point framebuffers (RGBA16F minimum)
   - MUST support tone mapping operators:
     * ACES Filmic (primary - FULL implementation)
     * Uncharted 2 (fallback - COMPLETE algorithm)
     * Reinhard with adaptive luminance (FULL implementation)
   - MUST implement proper gamma correction throughout pipeline
   - MUST support wide color gamut (Rec.2020, DCI-P3) with fallbacks
   - MUST implement proper color space conversions

2. ADVANCED SHADOW SYSTEM (ALL TECHNIQUES REQUIRED):
   - Cascade Shadow Maps (MINIMUM 4 cascades, FULL implementation):
     * MUST implement automatic cascade distribution
     * MUST implement cascade blending to eliminate seams
     * MUST implement shadow receiver culling for performance
   - Percentage Closer Filtering (MINIMUM 16 samples):
     * MUST implement Poisson disk sampling
     * MUST implement variable penumbra based on distance
     * MUST implement proper shadow acne elimination
   - Contact-hardening shadows (FULL PCSS implementation):
     * MUST implement blocker search pass
     * MUST implement variable filter kernel based on blockers
     * MUST implement proper bias and normal offset

3. ANTI-ALIASING PIPELINE (ALL METHODS REQUIRED):
   - Temporal Anti-Aliasing (TAA) - COMPLETE implementation:
     * MUST implement proper velocity buffer generation
     * MUST implement history buffer management
     * MUST implement rejection sampling for disocclusion
     * MUST implement sharpening to counteract blur
   - Multi-Sample Anti-Aliasing (MSAA) - FULL support:
     * MUST support 2x, 4x, 8x with automatic selection
     * MUST implement custom resolve for better quality
     * MUST implement coverage sampling for transparency
   - Screen-Space Anti-Aliasing fallbacks:
     * FXAA with high-quality preset (COMPLETE implementation)
     * SMAA with all passes (FULL temporal integration)

4. POST-PROCESSING PIPELINE (COMPLETE IMPLEMENTATION):
   - Screen-Space Ambient Occlusion (SSAO/HBAO+):
     * MUST implement minimum 32 samples with temporal filtering
     * MUST implement horizon-based AO for better quality
     * MUST implement bilateral upsampling for performance
   - Screen-Space Reflections (SSR):
     * MUST implement hierarchical depth buffer tracing
     * MUST implement temporal filtering for stability
     * MUST implement roughness-based blur for realistic reflections
   - Volumetric Lighting:
     * MUST implement ray marching through shadow maps
     * MUST implement temporal filtering for noise reduction
     * MUST implement proper scattering phase functions

IMPLEMENTATION REQUIREMENTS:

Renderer.js MUST be extended with:
```javascript
class AdvancedRenderer {
    constructor(canvas, options = {}) {
        // COMPLETE WebGL 2.0 context setup
        this.gl = this.initializeWebGL2Context(canvas);
        this.extensions = this.loadAllExtensions();
        this.capabilities = this.detectCapabilities();
        
        // COMPLETE HDR pipeline setup
        this.hdrFramebuffer = this.createHDRFramebuffer();
        this.toneMapper = this.createToneMapper();
        this.colorManager = this.createColorManager();
        
        // COMPLETE shadow system
        this.shadowMapper = this.createAdvancedShadowMapper();
        this.cascadeShadows = this.createCascadeShadowMaps();
        
        // COMPLETE anti-aliasing
        this.taaManager = this.createTAAManager();
        this.msaaManager = this.createMSAAManager();
        
        // COMPLETE post-processing
        this.postProcessor = this.createPostProcessor();
        this.ssaoPass = this.createSSAOPass();
        this.ssrPass = this.createSSRPass();
        this.volumetricPass = this.createVolumetricPass();
        
        this.validateSetup();
    }
    
    // MUST implement every method completely - no placeholders
    initializeWebGL2Context(canvas) {
        // COMPLETE implementation with all error handling
    }
    
    loadAllExtensions() {
        // COMPLETE implementation loading ALL available extensions
    }
    
    // ... ALL other methods MUST be fully implemented
}
```

VALIDATION REQUIREMENTS:
After each feature implementation, CURSOR MUST verify:
✓ Feature works on target hardware
✓ Fallbacks function properly on limited hardware  
✓ Performance impact is within acceptable limits
✓ No visual artifacts or rendering errors
✓ Memory usage increase is reasonable

PERFORMANCE BENCHMARKS (MUST ACHIEVE):
✓ HDR pipeline: <5% performance impact
✓ Shadow system: <20% performance impact  
✓ Anti-aliasing: <15% performance impact
✓ Post-processing: <25% total performance impact
✓ Combined system: Maintain >45 FPS on mid-range GPU
```

**GAP IDENTIFICATION FOR PHASE 1.2**:
```
CURSOR MUST CHECK FOR THESE CRITICAL GAPS:
❌ Missing WebGL extension fallbacks causing white screens
❌ Incomplete HDR support limiting color accuracy
❌ Poor shadow quality destroying realism
❌ Missing anti-aliasing causing jagged edges
❌ Incomplete post-processing reducing visual fidelity
❌ Performance issues preventing smooth operation
❌ Memory leaks in framebuffer management
❌ Missing error handling causing crashes
❌ Inadequate quality scaling options
❌ Browser compatibility issues
```

## Prompt 1.3: Professional Asset Streaming & Management System

**PREREQUISITE VALIDATION**:
```
CURSOR MUST VERIFY FROM PHASES 1.1-1.2:
✓ Advanced renderer is working without errors
✓ All rendering features are functional with fallbacks
✓ Performance benchmarks are met
✓ HDR pipeline is properly configured
✓ Shadow system is rendering correctly
✓ Anti-aliasing is working on all supported hardware
✓ Post-processing effects are visible and performant
```

**CURSOR RULES FOR THIS PROMPT**:
1. MUST implement complete asset streaming without external dependencies
2. ALL file formats must be supported with proper validation
3. MUST implement progressive loading with visual feedback
4. Memory management MUST prevent any leaks or excessive usage

**DETAILED IMPLEMENTATION**:
```
Implement a professional-grade asset streaming system with COMPLETE functionality:

MANDATORY ASSET MANAGEMENT FEATURES:

1. PROGRESSIVE LOADING SYSTEM (COMPLETE IMPLEMENTATION):
   AssetManager.js MUST implement:
   - COMPLETE texture streaming with multiple resolution levels
   - FULL geometry streaming with LOD management
   - COMPLETE audio streaming with seamless playback
   - FULL shader compilation with caching
   - COMPLETE dependency resolution and loading queues
   - FULL error recovery and retry mechanisms

2. ADVANCED COMPRESSION SUPPORT (ALL FORMATS):
   - Texture compression (MUST support ALL available formats):
     * Desktop: DXT1/DXT5, ETC2, ASTC
     * Mobile: ETC1/ETC2, PVRTC, ASTC
     * Universal: Basis Universal with fallbacks
   - Geometry compression:
     * Draco compression for complex meshes (FULL implementation)
     * Custom compression for simple geometry
     * Instancing data compression
   - Audio compression:
     * Spatial audio preservation during compression
     * Multiple quality levels with automatic selection
     * Streaming-optimized formats

3. INTELLIGENT CACHING SYSTEM (COMPLETE IMPLEMENTATION):
   - MUST implement LRU cache with configurable limits
   - MUST support persistent caching with IndexedDB
   - MUST implement cache validation and invalidation
   - MUST support predictive preloading
   - MUST implement cache compression to maximize storage

COMPLETE IMPLEMENTATION REQUIREMENTS:

AssetManager.js MUST include:
```javascript
class AssetManager {
    constructor(options = {}) {
        this.loadQueue = new PriorityQueue();
        this.cache = new IntelligentCache();
        this.compressor = new AssetCompressor();
        this.validator = new AssetValidator();
        this.progressTracker = new LoadingProgressTracker();
        
        // COMPLETE streaming setup
        this.textureStreamer = new TextureStreamer();
        this.geometryStreamer = new GeometryStreamer();
        this.audioStreamer = new AudioStreamer();
        this.shaderCache = new ShaderCache();
        
        this.initializeStorage();
    }
    
    // MUST implement complete loading with ALL error handling
    async loadAsset(url, options = {}) {
        // COMPLETE implementation with:
        // - Progress tracking
        // - Error recovery with retries
        // - Compression detection and decompression
        // - Cache integration
        // - Validation and verification
        // - Memory management
    }
    
    // MUST implement complete texture streaming
    async loadTexture(url, options = {}) {
        // COMPLETE implementation supporting:
        // - Multiple resolutions (8K, 4K, 2K, 1K)
        // - All compression formats with fallbacks
        // - Progressive loading from low to high resolution
        // - Memory usage optimization
        // - Error handling and recovery
    }
    
    // MUST implement complete geometry streaming  
    async loadGeometry(url, options = {}) {
        // COMPLETE implementation supporting:
        // - Draco decompression
        // - LOD level selection
        // - Progressive loading
        // - Memory optimization
        // - Validation and error handling
    }
    
    // ALL other methods MUST be fully implemented
}

class IntelligentCache {
    constructor(maxSize = '1GB') {
        this.storage = new Map();
        this.lruOrder = new DoublyLinkedList();
        this.persistentStorage = new IndexedDBManager();
        this.compressionEngine = new CompressionEngine();
        this.maxSize = this.parseSize(maxSize);
        this.currentSize = 0;
    }
    
    // COMPLETE implementation with ALL methods
}

class LoadingProgressTracker {
    constructor() {
        this.totalAssets = 0;
        this.loadedAssets = 0;
        this.failedAssets = 0;
        this.progress = 0;
        this.estimatedTimeRemaining = 0;
        this.loadingSpeed = 0;
    }
    
    // COMPLETE implementation with ALL progress tracking
}
```

VALIDATION REQUIREMENTS:
CURSOR MUST verify after implementation:
✓ All asset types load without errors
✓ Progressive loading provides smooth experience
✓ Cache system properly manages memory
✓ Compression/decompression works correctly
✓ Error recovery successfully handles failures
✓ Loading progress is accurate and responsive
✓ Memory usage stays within limits
✓ Loading performance meets targets (<10s total)

PERFORMANCE BENCHMARKS (MUST ACHIEVE):
✓ Texture loading: <2s for 4K textures
✓ Geometry loading: <1s for complex models
✓ Cache hit ratio: >80% for repeated assets
✓ Memory efficiency: >90% effective usage
✓ Loading UI responsiveness: 60 FPS during loading
✓ Error recovery: <3s retry delays
```

**GAP IDENTIFICATION FOR PHASE 1.3**:
```
CURSOR MUST CHECK FOR THESE CRITICAL GAPS:
❌ Missing compression support limiting asset quality
❌ Poor loading performance causing user frustration
❌ Memory leaks during asset streaming
❌ Missing error recovery causing loading failures
❌ Inadequate progress feedback confusing users
❌ Cache inefficiency causing repeated downloads
❌ Missing validation allowing corrupted assets
❌ Poor mobile performance due to excessive memory usage
❌ Missing fallback systems for unsupported formats
❌ Inadequate dependency management causing load order issues
```

## PHASE 1 COMPLETION CHECKLIST

### ✅ **VALIDATION REQUIREMENTS**
- [ ] All files compile without errors
- [ ] WebGL 2.0 context initializes successfully
- [ ] All rendering features work with proper fallbacks
- [ ] Performance benchmarks are met (>45 FPS)
- [ ] Memory usage is within limits (<100MB baseline)
- [ ] Asset streaming works smoothly
- [ ] Error handling prevents crashes
- [ ] Loading system provides good user experience

### ✅ **QUALITY GATES**
- [ ] 60 FPS empty scene rendering
- [ ] Error-free console output
- [ ] Responsive behavior on all screen sizes
- [ ] Comprehensive error handling throughout
- [ ] Complete documentation in code comments
- [ ] All advanced rendering features functional
- [ ] Asset loading performance meets targets

### ✅ **PERFORMANCE BENCHMARKS**
- [ ] HDR pipeline: <5% performance impact
- [ ] Shadow system: <20% performance impact
- [ ] Anti-aliasing: <15% performance impact
- [ ] Post-processing: <25% total performance impact
- [ ] Texture loading: <2s for 4K textures
- [ ] Geometry loading: <1s for complex models
- [ ] Cache hit ratio: >80% for repeated assets

**PHASE 1 MUST BE 100% COMPLETE BEFORE PROCEEDING TO PHASE 2**
