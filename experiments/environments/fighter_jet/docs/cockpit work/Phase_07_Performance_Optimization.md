# PHASE 7: PERFORMANCE OPTIMIZATION & QUALITY SCALING

## PRE-PHASE 7 VALIDATION:
```
CURSOR MUST VERIFY FROM PHASE 6:
✓ 3D spatial audio system is working correctly
✓ All audio effects enhance immersion without performance issues
✓ Interactive audio feedback is responsive and satisfying
✓ Ambient audio creates convincing cockpit atmosphere
✓ Audio performance benchmarks are met
✓ Audio synchronization with visual events is accurate
```

## Prompt 7.1: Advanced Performance Optimization & Dynamic Quality Scaling

**PREREQUISITE VALIDATION**:
```
CURSOR MUST VERIFY:
✓ All previous systems are functional and stable
✓ Performance monitoring is providing accurate metrics
✓ Visual and audio quality meets baseline requirements
✓ Memory usage is within acceptable limits
✓ Frame rate is consistently above minimum thresholds
```

**CURSOR RULES FOR THIS PROMPT**:
1. MUST implement intelligent performance scaling that maintains quality
2. ALL optimizations must be transparent to the user experience
3. MUST support wide range of hardware configurations
4. Performance scaling MUST prioritize critical systems over visual effects

**DETAILED IMPLEMENTATION**:
```
Create intelligent performance optimization system with dynamic quality scaling:

MANDATORY PERFORMANCE OPTIMIZATION COMPONENTS:

1. DYNAMIC QUALITY SCALING SYSTEM (COMPLETE IMPLEMENTATION):
   PerformanceOptimizer.js MUST implement:

   PERFORMANCE MONITORING:
   - Real-time frame time analysis with statistical smoothing
   - GPU memory usage tracking with allocation prediction
   - CPU usage monitoring for main thread and web workers
   - Thermal throttling detection and response

   ADAPTIVE QUALITY MANAGEMENT:
   - Dynamic LOD system with smooth quality transitions
   - Intelligent texture resolution scaling
   - Shader complexity reduction based on performance
   - Post-processing effect management with priority system

2. MULTI-THREADED OPTIMIZATION (COMPLETE IMPLEMENTATION):
   - Web Worker utilization for CPU-intensive tasks
   - OffscreenCanvas rendering for background operations
   - Async/await optimization for non-blocking operations
   - SharedArrayBuffer for efficient data sharing (where supported)

COMPLETE IMPLEMENTATION REQUIREMENTS:

PerformanceOptimizer.js MUST implement:
```javascript
class PerformanceOptimizer {
    constructor(renderer, sceneManager, audioManager) {
        this.renderer = renderer;
        this.sceneManager = sceneManager;
        this.audioManager = audioManager;
        
        // COMPLETE performance monitoring
        this.performanceMonitor = new PerformanceMonitor();
        this.frameAnalyzer = new FrameAnalyzer();
        this.memoryTracker = new MemoryTracker();
        this.thermalMonitor = new ThermalMonitor();
        
        // COMPLETE quality management
        this.qualityManager = new QualityManager();
        this.lodManager = new LODManager();
        this.textureManager = new TextureQualityManager();
        this.shaderManager = new ShaderQualityManager();
        this.effectsManager = new EffectsQualityManager();
        
        // COMPLETE optimization systems
        this.cullingSystem = new AdvancedCullingSystem();
        this.batchingSystem = new DrawCallBatcher();
        this.cacheManager = new RenderCacheManager();
        
        // Performance targets and thresholds
        this.performanceTargets = {
            targetFPS: 60,
            minFPS: 45,
            maxFrameTime: 16.67, // ms
            warningFrameTime: 20, // ms
            criticalFrameTime: 30, // ms
            maxMemoryUsage: 2048, // MB
            warningMemoryUsage: 1536, // MB
            maxGPUMemoryUsage: 1024 // MB
        };
        
        this.initializeOptimization();
    }
    
    // MUST implement complete performance optimization
    optimizePerformance(deltaTime) {
        // COMPLETE performance measurement
        const performanceMetrics = this.performanceMonitor.getMetrics();
        
        // COMPLETE quality adjustment decision
        const qualityAdjustment = this.determineQualityAdjustment(performanceMetrics);
        
        if (qualityAdjustment !== 0) {
            // COMPLETE quality scaling
            this.applyQualityScaling(qualityAdjustment);
        }
        
        // COMPLETE optimization techniques
        this.optimizeRendering(performanceMetrics);
        this.optimizeMemory(performanceMetrics);
        this.optimizeAudio(performanceMetrics);
        
        // COMPLETE performance reporting
        this.updatePerformanceReport(performanceMetrics);
    }
    
    // MUST implement complete quality adjustment determination
    determineQualityAdjustment(metrics) {
        let adjustment = 0;
        
        // COMPLETE frame time analysis
        if (metrics.averageFrameTime > this.performanceTargets.criticalFrameTime) {
            adjustment = -2; // Aggressive quality reduction
        } else if (metrics.averageFrameTime > this.performanceTargets.warningFrameTime) {
            adjustment = -1; // Moderate quality reduction
        } else if (metrics.averageFrameTime < this.performanceTargets.maxFrameTime * 0.8) {
            adjustment = 1; // Quality improvement possible
        }
        
        // COMPLETE memory pressure analysis
        if (metrics.memoryUsage > this.performanceTargets.warningMemoryUsage) {
            adjustment = Math.min(adjustment, -1);
        }
        
        // COMPLETE thermal throttling response
        if (metrics.thermalState === 'throttling') {
            adjustment = Math.min(adjustment, -2);
        }
        
        return adjustment;
    }
    
    // MUST implement complete quality scaling
    applyQualityScaling(adjustment) {
        const currentQuality = this.qualityManager.getCurrentQuality();
        const newQuality = Math.max(0, Math.min(4, currentQuality + adjustment));
        
        if (newQuality !== currentQuality) {
            // COMPLETE LOD adjustment
            this.lodManager.setQualityLevel(newQuality);
            
            // COMPLETE texture quality adjustment
            this.textureManager.setQualityLevel(newQuality);
            
            // COMPLETE shader quality adjustment
            this.shaderManager.setQualityLevel(newQuality);
            
            // COMPLETE effects quality adjustment
            this.effectsManager.setQualityLevel(newQuality);
            
            this.qualityManager.setCurrentQuality(newQuality);
        }
    }
    
    // MUST implement complete rendering optimization
    optimizeRendering(metrics) {
        // COMPLETE frustum culling optimization
        this.cullingSystem.optimizeCulling(metrics.visibleObjects);
        
        // COMPLETE draw call batching
        this.batchingSystem.optimizeBatching(metrics.drawCalls);
        
        // COMPLETE render state caching
        this.cacheManager.optimizeCaching(metrics.stateChanges);
        
        // COMPLETE shader optimization
        this.optimizeShaders(metrics);
    }
    
    // MUST implement complete memory optimization
    optimizeMemory(metrics) {
        if (metrics.memoryUsage > this.performanceTargets.warningMemoryUsage) {
            // COMPLETE texture memory optimization
            this.textureManager.optimizeMemory();
            
            // COMPLETE geometry memory optimization
            this.sceneManager.optimizeGeometryMemory();
            
            // COMPLETE audio memory optimization
            this.audioManager.optimizeMemory();
            
            // COMPLETE garbage collection optimization
            this.triggerOptimizedGC();
        }
    }
}

class PerformanceMonitor {
    constructor() {
        this.frameTimings = [];
        this.memoryUsage = [];
        this.gpuMemoryUsage = [];
        this.drawCallCounts = [];
        
        // COMPLETE performance tracking
        this.performanceObserver = new PerformanceObserver((list) => {
            this.processPerformanceEntries(list.getEntries());
        });
        
        if (typeof PerformanceObserver !== 'undefined') {
            this.performanceObserver.observe({ entryTypes: ['measure', 'navigation'] });
        }
        
        this.initializeMonitoring();
    }
    
    // MUST implement complete metrics collection
    getMetrics() {
        return {
            // COMPLETE frame timing metrics
            averageFrameTime: this.calculateAverageFrameTime(),
            frameTimeVariance: this.calculateFrameTimeVariance(),
            worstFrameTime: this.getWorstFrameTime(),
            
            // COMPLETE memory metrics
            memoryUsage: this.getCurrentMemoryUsage(),
            memoryTrend: this.getMemoryTrend(),
            gpuMemoryUsage: this.getGPUMemoryUsage(),
            
            // COMPLETE rendering metrics
            drawCalls: this.getAverageDrawCalls(),
            visibleObjects: this.getVisibleObjectCount(),
            stateChanges: this.getRenderStateChanges(),
            
            // COMPLETE system metrics
            thermalState: this.getThermalState(),
            batteryLevel: this.getBatteryLevel(),
            networkLatency: this.getNetworkLatency()
        };
    }
    
    // MUST implement complete frame time analysis
    calculateAverageFrameTime() {
        if (this.frameTimings.length === 0) return 16.67;
        
        const recentFrames = this.frameTimings.slice(-60); // Last 60 frames
        const sum = recentFrames.reduce((a, b) => a + b, 0);
        return sum / recentFrames.length;
    }
    
    // MUST implement complete memory usage tracking
    getCurrentMemoryUsage() {
        if (performance.memory) {
            return {
                used: performance.memory.usedJSHeapSize / (1024 * 1024), // MB
                total: performance.memory.totalJSHeapSize / (1024 * 1024), // MB
                limit: performance.memory.jsHeapSizeLimit / (1024 * 1024) // MB
            };
        }
        
        // COMPLETE fallback estimation
        return this.estimateMemoryUsage();
    }
}

class QualityManager {
    constructor() {
        this.currentQuality = 2; // Default to medium quality
        this.qualityLevels = {
            0: 'Ultra Low',
            1: 'Low', 
            2: 'Medium',
            3: 'High',
            4: 'Ultra High'
        };
        
        // COMPLETE quality settings for each level
        this.qualitySettings = {
            0: { // Ultra Low
                lodBias: 2.0,
                textureScale: 0.25,
                shadowResolution: 512,
                postProcessing: false,
                antiAliasing: false,
                volumetricLighting: false,
                particleCount: 0.1
            },
            1: { // Low
                lodBias: 1.5,
                textureScale: 0.5,
                shadowResolution: 1024,
                postProcessing: false,
                antiAliasing: 'FXAA',
                volumetricLighting: false,
                particleCount: 0.3
            },
            2: { // Medium
                lodBias: 1.0,
                textureScale: 0.75,
                shadowResolution: 2048,
                postProcessing: true,
                antiAliasing: 'FXAA',
                volumetricLighting: true,
                particleCount: 0.6
            },
            3: { // High
                lodBias: 0.5,
                textureScale: 1.0,
                shadowResolution: 4096,
                postProcessing: true,
                antiAliasing: 'MSAA',
                volumetricLighting: true,
                particleCount: 0.8
            },
            4: { // Ultra High
                lodBias: 0.0,
                textureScale: 1.0,
                shadowResolution: 8192,
                postProcessing: true,
                antiAliasing: 'TAA',
                volumetricLighting: true,
                particleCount: 1.0
            }
        };
    }
    
    // MUST implement complete quality level management
    setCurrentQuality(level) {
        if (level >= 0 && level <= 4 && level !== this.currentQuality) {
            const oldQuality = this.currentQuality;
            this.currentQuality = level;
            
            // COMPLETE quality transition
            this.transitionQuality(oldQuality, level);
        }
    }
    
    // MUST implement complete quality transition
    transitionQuality(fromLevel, toLevel) {
        const fromSettings = this.qualitySettings[fromLevel];
        const toSettings = this.qualitySettings[toLevel];
        
        // COMPLETE smooth transition animation
        const transitionDuration = 1000; // ms
        const startTime = performance.now();
        
        const animate = (currentTime) => {
            const elapsed = currentTime - startTime;
            const progress = Math.min(elapsed / transitionDuration, 1.0);
            
            // COMPLETE interpolated settings
            const interpolatedSettings = this.interpolateSettings(
                fromSettings, 
                toSettings, 
                progress
            );
            
            // COMPLETE settings application
            this.applyQualitySettings(interpolatedSettings);
            
            if (progress < 1.0) {
                requestAnimationFrame(animate);
            }
        };
        
        requestAnimationFrame(animate);
    }
}

class LODManager {
    constructor() {
        this.lodLevels = new Map();
        this.currentQualityLevel = 2;
        this.lodBias = 1.0;
        
        // COMPLETE LOD calculation parameters
        this.lodDistances = {
            high: 10,    // meters
            medium: 50,  // meters  
            low: 200,    // meters
            veryLow: 500 // meters
        };
    }
    
    // MUST implement complete LOD calculation
    calculateLOD(object, cameraPosition) {
        const distance = object.position.distanceTo(cameraPosition);
        const adjustedDistance = distance * this.lodBias;
        
        // COMPLETE LOD level determination
        if (adjustedDistance < this.lodDistances.high) {
            return 0; // Highest detail
        } else if (adjustedDistance < this.lodDistances.medium) {
            return 1; // High detail
        } else if (adjustedDistance < this.lodDistances.low) {
            return 2; // Medium detail
        } else if (adjustedDistance < this.lodDistances.veryLow) {
            return 3; // Low detail
        } else {
            return 4; // Lowest detail
        }
    }
    
    // MUST implement complete LOD updates
    updateLODs(scene, camera) {
        scene.traverse((object) => {
            if (object.userData.lodLevels) {
                const requiredLOD = this.calculateLOD(object, camera.position);
                this.setObjectLOD(object, requiredLOD);
            }
        });
    }
    
    // MUST implement complete object LOD setting
    setObjectLOD(object, lodLevel) {
        const lodLevels = object.userData.lodLevels;
        
        if (lodLevels && lodLevels[lodLevel]) {
            // COMPLETE geometry switching
            if (object.geometry !== lodLevels[lodLevel].geometry) {
                object.geometry = lodLevels[lodLevel].geometry;
            }
            
            // COMPLETE material switching
            if (lodLevels[lodLevel].material && object.material !== lodLevels[lodLevel].material) {
                object.material = lodLevels[lodLevel].material;
            }
            
            // COMPLETE visibility management
            object.visible = lodLevel < 5; // Hide at maximum distance
        }
    }
}
```

VALIDATION REQUIREMENTS:
CURSOR MUST verify after implementation:
✓ Performance optimization maintains stable frame rates
✓ Quality scaling is smooth and imperceptible
✓ Memory usage stays within acceptable limits
✓ All systems continue to function during optimization
✓ User experience remains consistent across quality levels
✓ Performance monitoring provides accurate metrics
✓ Optimization decisions are made intelligently
✓ System responds appropriately to performance pressure

PERFORMANCE BENCHMARKS (MUST ACHIEVE):
✓ Frame rate stability: >95% of frames within 10% of target
✓ Quality transition time: <1 second for smooth transitions
✓ Memory optimization: <10% memory reduction when needed
✓ Performance monitoring overhead: <1% of frame time
✓ LOD switching: Imperceptible to user
✓ Optimization response time: <100ms to performance changes
```

**GAP IDENTIFICATION FOR PHASE 7.1**:
```
CURSOR MUST CHECK FOR THESE CRITICAL GAPS:
❌ Poor performance monitoring leading to incorrect optimization decisions
❌ Aggressive quality scaling that degrades user experience
❌ Memory leaks that aren't caught by optimization systems
❌ Performance optimization that breaks critical functionality
❌ Inadequate thermal throttling response
❌ Poor LOD transitions causing visual popping
❌ Optimization overhead that reduces performance
❌ Missing fallback systems for unsupported optimizations
❌ Inadequate cross-platform performance scaling
❌ Poor integration between optimization systems
```

## Prompt 7.2: Multi-Platform Optimization & Hardware Adaptation

**PREREQUISITE VALIDATION**:
```
CURSOR MUST VERIFY FROM PHASE 7.1:
✓ Performance optimization system is working correctly
✓ Quality scaling maintains user experience
✓ Memory optimization prevents excessive usage
✓ Performance monitoring provides accurate data
✓ LOD system works smoothly
✓ All optimization systems integrate properly
```

**CURSOR RULES FOR THIS PROMPT**:
1. MUST optimize for various hardware configurations and platforms
2. ALL optimizations must maintain functionality across platforms
3. MUST provide appropriate fallbacks for unsupported features
4. Platform detection must be accurate and comprehensive

**DETAILED IMPLEMENTATION**:
```
Optimize for various hardware configurations and platforms:

MANDATORY MULTI-PLATFORM COMPONENTS:

1. HARDWARE DETECTION & ADAPTATION (COMPLETE IMPLEMENTATION):
   HardwareDetector.js MUST implement:

   COMPREHENSIVE DETECTION:
   - GPU capability detection with vendor-specific optimizations
   - CPU performance profiling and core count detection
   - Memory availability detection and optimization
   - Display capability detection (HDR, high refresh rate, resolution)
   - Input device detection and adaptation
   - Network performance detection for asset streaming

2. PLATFORM-SPECIFIC OPTIMIZATIONS (COMPLETE IMPLEMENTATION):
   PlatformOptimizer.js MUST implement:

   DESKTOP OPTIMIZATIONS:
   - High-end GPU capability utilization
   - Multi-core CPU optimization
   - Large memory buffer management
   - High-resolution display support
   - Advanced input device support

   MOBILE OPTIMIZATIONS:
   - Thermal management and throttling
   - Battery life optimization
   - Touch interface optimization
   - Limited memory management
   - Network-conscious asset loading

COMPLETE IMPLEMENTATION REQUIREMENTS:

HardwareDetector.js MUST implement:
```javascript
class HardwareDetector {
    constructor() {
        this.hardwareProfile = {
            platform: 'unknown',
            gpu: { vendor: 'unknown', model: 'unknown', memory: 0 },
            cpu: { cores: 1, architecture: 'unknown' },
            memory: { total: 0, available: 0 },
            display: { width: 1920, height: 1080, pixelRatio: 1, hdr: false },
            input: { touch: false, gamepad: false, keyboard: true, mouse: true },
            network: { type: 'unknown', speed: 'unknown' },
            capabilities: new Set()
        };
        
        this.detectHardware();
    }
    
    // MUST implement complete hardware detection
    detectHardware() {
        this.detectPlatform();
        this.detectGPU();
        this.detectCPU();
        this.detectMemory();
        this.detectDisplay();
        this.detectInput();
        this.detectNetwork();
        this.detectCapabilities();
    }
    
    // MUST implement complete GPU detection
    detectGPU() {
        const canvas = document.createElement('canvas');
        const gl = canvas.getContext('webgl2') || canvas.getContext('webgl');
        
        if (gl) {
            const debugInfo = gl.getExtension('WEBGL_debug_renderer_info');
            if (debugInfo) {
                const vendor = gl.getParameter(debugInfo.UNMASKED_VENDOR_WEBGL);
                const renderer = gl.getParameter(debugInfo.UNMASKED_RENDERER_WEBGL);
                
                this.hardwareProfile.gpu.vendor = this.parseGPUVendor(vendor);
                this.hardwareProfile.gpu.model = this.parseGPUModel(renderer);
            }
            
            // COMPLETE GPU memory estimation
            this.hardwareProfile.gpu.memory = this.estimateGPUMemory(gl);
        }
    }
    
    // MUST implement complete CPU detection
    detectCPU() {
        this.hardwareProfile.cpu.cores = navigator.hardwareConcurrency || 4;
        this.hardwareProfile.cpu.architecture = this.detectCPUArchitecture();
    }
    
    // MUST implement complete memory detection
    detectMemory() {
        if (navigator.deviceMemory) {
            this.hardwareProfile.memory.total = navigator.deviceMemory * 1024; // MB
        } else {
            this.hardwareProfile.memory.total = this.estimateMemory();
        }
        
        if (performance.memory) {
            this.hardwareProfile.memory.available = 
                (performance.memory.jsHeapSizeLimit - performance.memory.usedJSHeapSize) / (1024 * 1024);
        }
    }
    
    // MUST implement complete capability detection
    detectCapabilities() {
        const canvas = document.createElement('canvas');
        const gl = canvas.getContext('webgl2') || canvas.getContext('webgl');
        
        if (gl) {
            // COMPLETE WebGL capabilities
            if (gl instanceof WebGL2RenderingContext) {
                this.hardwareProfile.capabilities.add('webgl2');
            }
            
            // COMPLETE extension detection
            const extensions = [
                'EXT_texture_filter_anisotropic',
                'WEBGL_compressed_texture_s3tc',
                'WEBGL_compressed_texture_etc',
                'WEBGL_compressed_texture_astc',
                'OES_texture_float',
                'OES_texture_half_float',
                'EXT_color_buffer_float'
            ];
            
            extensions.forEach(ext => {
                if (gl.getExtension(ext)) {
                    this.hardwareProfile.capabilities.add(ext);
                }
            });
        }
        
        // COMPLETE other capabilities
        if ('serviceWorker' in navigator) {
            this.hardwareProfile.capabilities.add('serviceWorker');
        }
        
        if ('SharedArrayBuffer' in window) {
            this.hardwareProfile.capabilities.add('sharedArrayBuffer');
        }
        
        if ('OffscreenCanvas' in window) {
            this.hardwareProfile.capabilities.add('offscreenCanvas');
        }
    }
}

class PlatformOptimizer {
    constructor(hardwareProfile) {
        this.hardwareProfile = hardwareProfile;
        this.optimizations = new Map();
        
        this.initializePlatformOptimizations();
    }
    
    // MUST implement complete platform optimization
    initializePlatformOptimizations() {
        switch (this.hardwareProfile.platform) {
            case 'desktop':
                this.initializeDesktopOptimizations();
                break;
            case 'mobile':
                this.initializeMobileOptimizations();
                break;
            case 'tablet':
                this.initializeTabletOptimizations();
                break;
            default:
                this.initializeGenericOptimizations();
        }
    }
    
    // MUST implement complete desktop optimizations
    initializeDesktopOptimizations() {
        // COMPLETE high-end GPU utilization
        if (this.hardwareProfile.gpu.memory > 4096) { // 4GB+ VRAM
            this.optimizations.set('textureQuality', 'ultra');
            this.optimizations.set('shadowResolution', 4096);
            this.optimizations.set('postProcessing', 'full');
        } else if (this.hardwareProfile.gpu.memory > 2048) { // 2GB+ VRAM
            this.optimizations.set('textureQuality', 'high');
            this.optimizations.set('shadowResolution', 2048);
            this.optimizations.set('postProcessing', 'standard');
        }
        
        // COMPLETE multi-core CPU optimization
        if (this.hardwareProfile.cpu.cores >= 8) {
            this.optimizations.set('workerThreads', 4);
            this.optimizations.set('asyncLoading', true);
        } else if (this.hardwareProfile.cpu.cores >= 4) {
            this.optimizations.set('workerThreads', 2);
            this.optimizations.set('asyncLoading', true);
        }
        
        // COMPLETE memory management
        if (this.hardwareProfile.memory.total >= 16384) { // 16GB+ RAM
            this.optimizations.set('cacheSize', 'large');
            this.optimizations.set('preloadDistance', 'far');
        }
    }
    
    // MUST implement complete mobile optimizations
    initializeMobileOptimizations() {
        // COMPLETE thermal management
        this.optimizations.set('thermalThrottling', true);
        this.optimizations.set('adaptiveQuality', true);
        
        // COMPLETE battery optimization
        this.optimizations.set('powerSaving', true);
        this.optimizations.set('backgroundThrottling', true);
        
        // COMPLETE memory constraints
        this.optimizations.set('textureCompression', 'aggressive');
        this.optimizations.set('geometryLOD', 'aggressive');
        this.optimizations.set('cacheSize', 'small');
        
        // COMPLETE touch optimization
        this.optimizations.set('touchLatency', 'low');
        this.optimizations.set('gestureRecognition', true);
        
        // COMPLETE network optimization
        this.optimizations.set('assetStreaming', 'conservative');
        this.optimizations.set('compressionLevel', 'high');
    }
    
    // MUST implement complete optimization application
    applyOptimizations(renderer, sceneManager, assetManager) {
        for (const [optimization, value] of this.optimizations) {
            this.applyOptimization(optimization, value, renderer, sceneManager, assetManager);
        }
    }
    
    // MUST implement complete individual optimization application
    applyOptimization(type, value, renderer, sceneManager, assetManager) {
        switch (type) {
            case 'textureQuality':
                this.applyTextureQualityOptimization(value, renderer);
                break;
            case 'shadowResolution':
                this.applyShadowOptimization(value, renderer);
                break;
            case 'workerThreads':
                this.applyWorkerThreadOptimization(value, assetManager);
                break;
            case 'thermalThrottling':
                this.applyThermalOptimization(value, renderer);
                break;
            // COMPLETE optimization implementations
        }
    }
}

class QualityPresetManager {
    constructor(hardwareProfile) {
        this.hardwareProfile = hardwareProfile;
        this.presets = this.generateQualityPresets();
        this.recommendedPreset = this.determineRecommendedPreset();
    }
    
    // MUST implement complete quality preset generation
    generateQualityPresets() {
        return {
            ultra: {
                name: 'Ultra',
                description: 'Maximum visual quality for high-end systems',
                requirements: {
                    gpuMemory: 6144, // 6GB
                    systemMemory: 16384, // 16GB
                    cpuCores: 8
                },
                settings: {
                    renderScale: 1.0,
                    textureQuality: 1.0,
                    shadowResolution: 4096,
                    antiAliasing: 'TAA',
                    postProcessing: 'full',
                    volumetricLighting: true,
                    particleDensity: 1.0,
                    lodBias: 0.0
                }
            },
            high: {
                name: 'High',
                description: 'Excellent quality for modern systems',
                requirements: {
                    gpuMemory: 4096, // 4GB
                    systemMemory: 8192, // 8GB
                    cpuCores: 4
                },
                settings: {
                    renderScale: 1.0,
                    textureQuality: 0.8,
                    shadowResolution: 2048,
                    antiAliasing: 'MSAA',
                    postProcessing: 'standard',
                    volumetricLighting: true,
                    particleDensity: 0.8,
                    lodBias: 0.5
                }
            },
            medium: {
                name: 'Medium',
                description: 'Balanced quality and performance',
                requirements: {
                    gpuMemory: 2048, // 2GB
                    systemMemory: 4096, // 4GB
                    cpuCores: 2
                },
                settings: {
                    renderScale: 0.8,
                    textureQuality: 0.6,
                    shadowResolution: 1024,
                    antiAliasing: 'FXAA',
                    postProcessing: 'basic',
                    volumetricLighting: false,
                    particleDensity: 0.5,
                    lodBias: 1.0
                }
            },
            low: {
                name: 'Low',
                description: 'Performance optimized for older systems',
                requirements: {
                    gpuMemory: 1024, // 1GB
                    systemMemory: 2048, // 2GB
                    cpuCores: 1
                },
                settings: {
                    renderScale: 0.6,
                    textureQuality: 0.4,
                    shadowResolution: 512,
                    antiAliasing: false,
                    postProcessing: false,
                    volumetricLighting: false,
                    particleDensity: 0.2,
                    lodBias: 2.0
                }
            }
        };
    }
    
    // MUST implement complete preset recommendation
    determineRecommendedPreset() {
        const profile = this.hardwareProfile;
        
        // COMPLETE scoring system
        let score = 0;
        
        // GPU scoring
        if (profile.gpu.memory >= 6144) score += 40;
        else if (profile.gpu.memory >= 4096) score += 30;
        else if (profile.gpu.memory >= 2048) score += 20;
        else score += 10;
        
        // CPU scoring
        if (profile.cpu.cores >= 8) score += 20;
        else if (profile.cpu.cores >= 4) score += 15;
        else if (profile.cpu.cores >= 2) score += 10;
        else score += 5;
        
        // Memory scoring
        if (profile.memory.total >= 16384) score += 20;
        else if (profile.memory.total >= 8192) score += 15;
        else if (profile.memory.total >= 4096) score += 10;
        else score += 5;
        
        // Platform adjustments
        if (profile.platform === 'mobile') score *= 0.6;
        else if (profile.platform === 'tablet') score *= 0.8;
        
        // COMPLETE preset selection
        if (score >= 75) return 'ultra';
        else if (score >= 55) return 'high';
        else if (score >= 35) return 'medium';
        else return 'low';
    }
}
```

VALIDATION REQUIREMENTS:
CURSOR MUST verify after implementation:
✓ Hardware detection accurately identifies system capabilities
✓ Platform-specific optimizations improve performance
✓ Quality presets match hardware capabilities
✓ Fallback systems work on unsupported platforms
✓ Mobile optimizations preserve battery life
✓ Desktop optimizations utilize available resources
✓ Cross-platform functionality is maintained
✓ Performance scaling adapts to different hardware

PERFORMANCE BENCHMARKS (MUST ACHIEVE):
✓ Hardware detection: <100ms initialization time
✓ Platform optimization: >20% performance improvement on target platforms
✓ Quality preset accuracy: >90% appropriate recommendations
✓ Mobile battery impact: <10% additional drain
✓ Desktop resource utilization: >80% of available capabilities
✓ Cross-platform compatibility: >95% feature parity
```

**GAP IDENTIFICATION FOR PHASE 7.2**:
```
CURSOR MUST CHECK FOR THESE CRITICAL GAPS:
❌ Inaccurate hardware detection leading to poor optimization choices
❌ Platform-specific optimizations that break functionality
❌ Missing fallbacks for unsupported hardware features
❌ Poor mobile performance due to inadequate thermal management
❌ Desktop optimizations that don't utilize available resources
❌ Quality presets that don't match actual hardware capabilities
❌ Cross-platform inconsistencies in user experience
❌ Missing battery optimization for mobile devices
❌ Inadequate network optimization for different connection types
❌ Poor integration between platform detection and optimization systems
```

## PHASE 7 COMPLETION CHECKLIST

### ✅ **VALIDATION REQUIREMENTS**
- [ ] Performance optimization maintains stable frame rates
- [ ] Quality scaling is smooth and imperceptible
- [ ] Hardware detection accurately identifies capabilities
- [ ] Platform-specific optimizations improve performance
- [ ] Memory usage stays within acceptable limits
- [ ] All systems continue to function during optimization
- [ ] Cross-platform functionality is maintained
- [ ] User experience remains consistent

### ✅ **QUALITY GATES**
- [ ] Performance monitoring provides accurate metrics
- [ ] Optimization decisions are made intelligently
- [ ] Quality presets match hardware capabilities
- [ ] Mobile optimizations preserve battery life
- [ ] Desktop optimizations utilize available resources
- [ ] LOD transitions are imperceptible
- [ ] Thermal throttling responds appropriately

### ✅ **PERFORMANCE BENCHMARKS**
- [ ] Frame rate stability: >95% of frames within 10% of target
- [ ] Quality transition time: <1 second for smooth transitions
- [ ] Hardware detection: <100ms initialization time
- [ ] Platform optimization: >20% performance improvement
- [ ] Memory optimization: <10% reduction when needed
- [ ] Performance monitoring overhead: <1% of frame time
- [ ] Cross-platform compatibility: >95% feature parity

**PHASE 7 MUST BE 100% COMPLETE BEFORE PROCEEDING TO PHASE 8**
