# AUDIO PHASE 1: FOUNDATION AND SPATIAL AUDIO PIPELINE (WEB AUDIO API)

## PROJECT RULES & CONSTRAINTS

### MANDATORY DEVELOPMENT RULES FOR ALL AUDIO PHASES:

1. **WEB AUDIO API RESTRICTIONS**: 
   - Use ONLY Web Audio API for all audio processing
   - NO external audio libraries except for approved utilities (Tone.js for advanced features)
   - NO browser-specific audio implementations
   - NO deprecated audio methods (HTML5 Audio element for basic playback only)

2. **AUDIO ASSET COMPLETENESS**: 
   - Provide COMPLETE, production-ready audio assets for every prompt
   - NEVER use placeholders like "..." or "[audio file here]"
   - All audio files must be properly formatted and optimized
   - All spatial audio positioning must be fully implemented
   - All audio processing chains must be complete with full parameter control

3. **SPATIAL AUDIO CONSISTENCY**: 
   - Maintain perfect HRTF implementation across all audio sources
   - Ensure all audio positioning matches 3D cockpit geometry
   - Verify coordinate systems match (Web Audio API standard)
   - Test all spatial audio in VR/AR environments before approval

4. **QUALITY GATES**: 
   - Each phase MUST pass audio-specific validation before proceeding
   - Identify and fix ALL audio gaps that could limit final immersion
   - No phase advancement without successful spatial audio validation
   - All assets must meet professional aviation audio standards

5. **PERFORMANCE REQUIREMENTS**: 
   - Maintain <20ms latency for interactive audio feedback
   - Memory usage must not exceed 128MB for complete audio system
   - Audio processing must not exceed 10% CPU usage
   - Real-time audio must maintain stable performance at 60 FPS

## PRE-PHASE 1 VALIDATION:
**CURSOR MUST CHECK:**
```
✓ Web Audio API is supported and properly initialized
✓ HRTF processing is available and functional
✓ Audio context is configured for low-latency operation
✓ Spatial audio positioning system is calibrated
✓ No conflicting audio contexts or deprecated implementations exist
```

## Prompt 1.1: Web Audio API Foundation Setup

**PREREQUISITE VALIDATION**: None (Initial setup)

**CURSOR RULES FOR THIS PROMPT**:
1. Create COMPLETE Web Audio API architecture with all necessary audio nodes
2. Implement FULL spatial audio engine with HRTF processing
3. NO placeholder audio sources - everything must be production-ready
4. Must support both stereo and spatial audio with seamless switching

**DETAILED IMPLEMENTATION**:
```
Create a professional Web Audio API foundation with the following COMPLETE structure:

AUDIO SYSTEM ARCHITECTURE (create ALL components and setup):
├── Core Audio Engine/
│   ├── AudioContext_Manager (COMPLETE context lifecycle management)
│   ├── SpatialAudio_Engine (FULL HRTF implementation)
│   ├── AudioNode_Factory (COMPLETE node creation and management)
│   └── Performance_Monitor (Real-time performance tracking)
├── Audio Source Management/
│   ├── BufferSource_Pool (COMPLETE audio buffer management)
│   ├── StreamingAudio_Manager (FULL streaming audio pipeline)
│   ├── AudioLoader_System (COMPLETE asset loading and caching)
│   └── Format_Converter (Multi-format audio support)
├── Spatial Processing/
│   ├── HRTF_Processor (FULL head-related transfer function)
│   ├── Distance_Modeling (COMPLETE attenuation and filtering)
│   ├── Occlusion_System (FULL geometric audio blocking)
│   └── Reverb_Engine (Complete cockpit acoustic simulation)
├── Audio Mixing/
│   ├── MixingConsole_Core (COMPLETE multi-channel mixing)
│   ├── DynamicRange_Processor (FULL compression and limiting)
│   ├── EQ_System (Complete frequency management)
│   └── Priority_Manager (Audio importance hierarchy)
├── Interactive Audio/
│   ├── Control_Feedback (COMPLETE switch and button audio)
│   ├── System_Alerts (FULL warning and caution system)
│   ├── Engine_Audio (Complete propulsion audio simulation)
│   └── Environmental_Audio (Full ambient sound system)
└── Integration Layer/
    ├── ThreeJS_Bridge (COMPLETE 3D scene integration)
    ├── VR_AudioAdapter (FULL VR/AR audio support)
    ├── Performance_Optimizer (Complete resource management)
    └── Debug_Interface (Full audio system monitoring)

MANDATORY WEB AUDIO API SETUP REQUIREMENTS:

1. Audio Context Configuration MUST include:
   - Sample rate: 48kHz for spatial audio processing
   - Buffer size: 256 samples for low latency
   - Channel configuration: Stereo output with spatial processing
   - Latency hint: 'interactive' for real-time performance
   - State management: Proper context suspension/resumption
   - Error handling: Complete fallback and recovery systems

2. Spatial Audio Engine MUST implement:
   - HRTF panning with proper head modeling
   - Distance-based attenuation with realistic curves
   - Doppler effect processing for moving sources
   - Occlusion and obstruction modeling
   - Reverb processing with cockpit impulse response
   - Coordinate system integration with Three.js scene

3. Audio Node Architecture MUST include:
   - BufferSource nodes for short audio clips
   - MediaElementSource for streaming audio
   - PannerNode with HRTF configuration
   - ConvolverNode for reverb processing
   - GainNode for volume and mixing control
   - BiquadFilterNode for frequency processing
   - DynamicsCompressorNode for dynamic range control
   - AnalyserNode for real-time audio visualization

4. Performance Optimization MUST implement:
   - Audio buffer pooling and reuse
   - Lazy loading of non-critical audio assets
   - Automatic quality scaling based on device capabilities
   - Memory management with garbage collection optimization
   - CPU usage monitoring and automatic adjustment

COMPLETE IMPLEMENTATION REQUIREMENTS:

Core Audio Engine MUST include:
```javascript
// Web Audio API Foundation System
class CockpitAudioEngine {
    constructor(options = {}) {
        this.options = {
            sampleRate: 48000,
            bufferSize: 256,
            latencyHint: 'interactive',
            maxPolyphony: 64,
            spatialAudioEnabled: true,
            ...options
        };
        
        this.audioContext = null;
        this.masterGain = null;
        this.spatialEngine = null;
        this.mixingConsole = null;
        this.performanceMonitor = null;
        
        this.audioSources = new Map();
        this.activeVoices = new Set();
        this.audioBuffers = new Map();
        
        this.isInitialized = false;
        this.isRunning = false;
        
        this.initializeAudioSystem();
    }
    
    async initializeAudioSystem() {
        try {
            // Create AudioContext with optimal settings
            this.audioContext = new (window.AudioContext || window.webkitAudioContext)({
                sampleRate: this.options.sampleRate,
                latencyHint: this.options.latencyHint
            });
            
            // Wait for context to be running
            if (this.audioContext.state === 'suspended') {
                await this.audioContext.resume();
            }
            
            // Create master gain node
            this.masterGain = this.audioContext.createGain();
            this.masterGain.connect(this.audioContext.destination);
            
            // Initialize spatial audio engine
            this.spatialEngine = new SpatialAudioEngine(this.audioContext, this.masterGain);
            
            // Initialize mixing console
            this.mixingConsole = new AudioMixingConsole(this.audioContext, this.masterGain);
            
            // Initialize performance monitor
            this.performanceMonitor = new AudioPerformanceMonitor(this.audioContext);
            
            // Setup audio categories
            this.setupAudioCategories();
            
            // Load critical audio assets
            await this.loadCriticalAudioAssets();
            
            this.isInitialized = true;
            this.isRunning = true;
            
            console.log('Cockpit Audio Engine initialized successfully');
            console.log(`Sample Rate: ${this.audioContext.sampleRate}Hz`);
            console.log(`Base Latency: ${this.audioContext.baseLatency * 1000}ms`);
            
        } catch (error) {
            console.error('Failed to initialize audio system:', error);
            throw new Error(`Audio initialization failed: ${error.message}`);
        }
    }
    
    setupAudioCategories() {
        // Engine and Propulsion Audio
        this.engineAudio = new EngineAudioSystem(this.audioContext, this.spatialEngine);
        
        // Cockpit System Sounds
        this.systemAudio = new SystemAudioManager(this.audioContext, this.spatialEngine);
        
        // Warning and Alert Systems
        this.alertAudio = new AlertAudioSystem(this.audioContext, this.mixingConsole);
        
        // Environmental Audio
        this.environmentAudio = new EnvironmentalAudioSystem(this.audioContext, this.spatialEngine);
        
        // Communication Systems
        this.commAudio = new CommunicationAudioSystem(this.audioContext, this.mixingConsole);
        
        // Interactive Control Feedback
        this.controlAudio = new ControlFeedbackSystem(this.audioContext, this.spatialEngine);
    }
    
    async loadCriticalAudioAssets() {
        const criticalAssets = [
            { name: 'master_caution', url: '/audio/alerts/master_caution.ogg', priority: 'high' },
            { name: 'master_warning', url: '/audio/alerts/master_warning.ogg', priority: 'high' },
            { name: 'switch_toggle_01', url: '/audio/controls/switch_toggle_01.ogg', priority: 'medium' },
            { name: 'button_press_01', url: '/audio/controls/button_press_01.ogg', priority: 'medium' },
            { name: 'engine_idle', url: '/audio/engine/turbofan_idle_loop.ogg', priority: 'high' }
        ];
        
        const loadPromises = criticalAssets.map(asset => this.loadAudioAsset(asset));
        await Promise.all(loadPromises);
        
        console.log(`Loaded ${criticalAssets.length} critical audio assets`);
    }
    
    async loadAudioAsset(assetInfo) {
        try {
            const response = await fetch(assetInfo.url);
            if (!response.ok) {
                throw new Error(`Failed to fetch audio: ${response.status}`);
            }
            
            const arrayBuffer = await response.arrayBuffer();
            const audioBuffer = await this.audioContext.decodeAudioData(arrayBuffer);
            
            this.audioBuffers.set(assetInfo.name, {
                buffer: audioBuffer,
                priority: assetInfo.priority,
                loadTime: performance.now()
            });
            
            console.log(`Loaded audio asset: ${assetInfo.name} (${audioBuffer.duration.toFixed(2)}s)`);
            
        } catch (error) {
            console.error(`Failed to load audio asset ${assetInfo.name}:`, error);
            // Create silent buffer as fallback
            this.createSilentBuffer(assetInfo.name);
        }
    }
    
    createSilentBuffer(name, duration = 0.1) {
        const buffer = this.audioContext.createBuffer(2, this.audioContext.sampleRate * duration, this.audioContext.sampleRate);
        this.audioBuffers.set(name, {
            buffer: buffer,
            priority: 'low',
            loadTime: performance.now(),
            isSilent: true
        });
    }
    
    playAudioSource(sourceName, options = {}) {
        if (!this.isRunning || !this.audioBuffers.has(sourceName)) {
            console.warn(`Audio source not available: ${sourceName}`);
            return null;
        }
        
        const assetData = this.audioBuffers.get(sourceName);
        const source = this.audioContext.createBufferSource();
        source.buffer = assetData.buffer;
        
        // Configure source based on options
        if (options.loop) {
            source.loop = true;
            source.loopStart = options.loopStart || 0;
            source.loopEnd = options.loopEnd || source.buffer.duration;
        }
        
        // Create audio processing chain
        let audioChain = source;
        
        // Add spatial processing if position specified
        if (options.position && this.spatialEngine) {
            audioChain = this.spatialEngine.createSpatialSource(audioChain, options.position);
        }
        
        // Add gain control
        const gainNode = this.audioContext.createGain();
        gainNode.gain.setValueAtTime(options.volume || 1.0, this.audioContext.currentTime);
        audioChain.connect(gainNode);
        
        // Connect to appropriate mixer channel
        const mixerChannel = this.mixingConsole.getChannel(options.category || 'default');
        gainNode.connect(mixerChannel.input);
        
        // Start playback
        const startTime = this.audioContext.currentTime + (options.delay || 0);
        source.start(startTime);
        
        // Track active voice
        const voiceId = this.generateVoiceId();
        this.activeVoices.add({
            id: voiceId,
            source: source,
            gainNode: gainNode,
            startTime: startTime,
            category: options.category || 'default'
        });
        
        // Setup cleanup
        source.onended = () => {
            this.cleanupVoice(voiceId);
        };
        
        return {
            voiceId: voiceId,
            source: source,
            gainNode: gainNode,
            stop: (when = 0) => source.stop(this.audioContext.currentTime + when),
            setVolume: (volume, when = 0) => gainNode.gain.setValueAtTime(volume, this.audioContext.currentTime + when)
        };
    }
    
    generateVoiceId() {
        return `voice_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
    }
    
    cleanupVoice(voiceId) {
        for (const voice of this.activeVoices) {
            if (voice.id === voiceId) {
                this.activeVoices.delete(voice);
                break;
            }
        }
    }
    
    update(deltaTime, cockpitState) {
        if (!this.isRunning) return;
        
        // Update performance monitoring
        this.performanceMonitor.update(deltaTime);
        
        // Update spatial audio engine
        if (this.spatialEngine) {
            this.spatialEngine.update(deltaTime, cockpitState);
        }
        
        // Update audio subsystems
        this.engineAudio.update(deltaTime, cockpitState.engine);
        this.systemAudio.update(deltaTime, cockpitState.systems);
        this.alertAudio.update(deltaTime, cockpitState.alerts);
        this.environmentAudio.update(deltaTime, cockpitState.environment);
        this.commAudio.update(deltaTime, cockpitState.communications);
        this.controlAudio.update(deltaTime, cockpitState.controls);
        
        // Manage voice polyphony
        this.managePolyphony();
    }
    
    managePolyphony() {
        if (this.activeVoices.size <= this.options.maxPolyphony) return;
        
        // Sort voices by priority and age
        const voiceArray = Array.from(this.activeVoices);
        voiceArray.sort((a, b) => {
            const priorityA = this.getVoicePriority(a.category);
            const priorityB = this.getVoicePriority(b.category);
            
            if (priorityA !== priorityB) {
                return priorityA - priorityB; // Lower number = higher priority
            }
            
            return a.startTime - b.startTime; // Older voices first
        });
        
        // Stop lowest priority voices
        const voicesToStop = voiceArray.slice(this.options.maxPolyphony);
        voicesToStop.forEach(voice => {
            voice.source.stop();
        });
    }
    
    getVoicePriority(category) {
        const priorities = {
            'alert': 1,
            'warning': 2,
            'engine': 3,
            'control': 4,
            'system': 5,
            'environment': 6,
            'communication': 7,
            'default': 8
        };
        return priorities[category] || 8;
    }
    
    setMasterVolume(volume) {
        if (this.masterGain) {
            this.masterGain.gain.setValueAtTime(volume, this.audioContext.currentTime);
        }
    }
    
    suspend() {
        if (this.audioContext && this.audioContext.state === 'running') {
            this.audioContext.suspend();
            this.isRunning = false;
        }
    }
    
    resume() {
        if (this.audioContext && this.audioContext.state === 'suspended') {
            this.audioContext.resume();
            this.isRunning = true;
        }
    }
    
    dispose() {
        // Stop all active voices
        this.activeVoices.forEach(voice => {
            voice.source.stop();
        });
        this.activeVoices.clear();
        
        // Dispose subsystems
        if (this.engineAudio) this.engineAudio.dispose();
        if (this.systemAudio) this.systemAudio.dispose();
        if (this.alertAudio) this.alertAudio.dispose();
        if (this.environmentAudio) this.environmentAudio.dispose();
        if (this.commAudio) this.commAudio.dispose();
        if (this.controlAudio) this.controlAudio.dispose();
        
        // Close audio context
        if (this.audioContext) {
            this.audioContext.close();
        }
        
        this.isInitialized = false;
        this.isRunning = false;
    }
}

// Spatial Audio Engine Implementation
class SpatialAudioEngine {
    constructor(audioContext, masterGain) {
        this.audioContext = audioContext;
        this.masterGain = masterGain;
        
        // Setup listener (pilot head position)
        this.listener = audioContext.listener;
        this.listenerPosition = { x: 0, y: 1.2, z: 0.3 }; // Pilot eye position
        this.listenerOrientation = { forward: { x: 0, y: 0, z: -1 }, up: { x: 0, y: 1, z: 0 } };
        
        // Convolver for cockpit reverb
        this.convolver = audioContext.createConvolver();
        this.convolver.connect(masterGain);
        
        // Load cockpit impulse response
        this.loadCockpitImpulseResponse();
        
        // Active spatial sources
        this.spatialSources = new Map();
        
        this.updateListenerPosition();
    }
    
    async loadCockpitImpulseResponse() {
        try {
            // Load pre-recorded cockpit impulse response
            const response = await fetch('/audio/impulse_responses/cockpit_ir.wav');
            const arrayBuffer = await response.arrayBuffer();
            const impulseBuffer = await this.audioContext.decodeAudioData(arrayBuffer);
            
            this.convolver.buffer = impulseBuffer;
            console.log('Cockpit impulse response loaded successfully');
            
        } catch (error) {
            console.warn('Failed to load cockpit impulse response, creating synthetic IR');
            this.createSyntheticImpulseResponse();
        }
    }
    
    createSyntheticImpulseResponse() {
        // Create synthetic cockpit reverb
        const length = this.audioContext.sampleRate * 2; // 2 seconds
        const impulse = this.audioContext.createBuffer(2, length, this.audioContext.sampleRate);
        
        for (let channel = 0; channel < 2; channel++) {
            const channelData = impulse.getChannelData(channel);
            for (let i = 0; i < length; i++) {
                const decay = Math.pow(1 - (i / length), 2);
                channelData[i] = (Math.random() * 2 - 1) * decay * 0.1;
            }
        }
        
        this.convolver.buffer = impulse;
    }
    
    createSpatialSource(sourceNode, position, options = {}) {
        // Create panner node for 3D positioning
        const panner = this.audioContext.createPanner();
        
        // Configure panner for HRTF
        panner.panningModel = 'HRTF';
        panner.distanceModel = options.distanceModel || 'inverse';
        panner.refDistance = options.refDistance || 1;
        panner.maxDistance = options.maxDistance || 10;
        panner.rolloffFactor = options.rolloffFactor || 1;
        panner.coneInnerAngle = options.coneInnerAngle || 360;
        panner.coneOuterAngle = options.coneOuterAngle || 0;
        panner.coneOuterGain = options.coneOuterGain || 0;
        
        // Set initial position
        this.setSpatialSourcePosition(panner, position);
        
        // Create processing chain
        const dryGain = this.audioContext.createGain();
        const wetGain = this.audioContext.createGain();
        
        // Configure dry/wet mix
        const reverbSend = options.reverbSend || 0.3;
        dryGain.gain.setValueAtTime(1 - reverbSend, this.audioContext.currentTime);
        wetGain.gain.setValueAtTime(reverbSend, this.audioContext.currentTime);
        
        // Connect audio graph
        sourceNode.connect(panner);
        panner.connect(dryGain);
        panner.connect(wetGain);
        
        dryGain.connect(this.masterGain);
        wetGain.connect(this.convolver);
        
        // Store spatial source reference
        const sourceId = this.generateSourceId();
        this.spatialSources.set(sourceId, {
            panner: panner,
            position: { ...position },
            dryGain: dryGain,
            wetGain: wetGain,
            options: { ...options }
        });
        
        return {
            sourceId: sourceId,
            panner: panner,
            setPosition: (newPosition) => this.setSpatialSourcePosition(panner, newPosition),
            setReverbSend: (send) => {
                wetGain.gain.setValueAtTime(send, this.audioContext.currentTime);
                dryGain.gain.setValueAtTime(1 - send, this.audioContext.currentTime);
            },
            dispose: () => this.disposeSpatialSource(sourceId)
        };
    }
    
    setSpatialSourcePosition(panner, position) {
        const currentTime = this.audioContext.currentTime;
        
        if (panner.positionX) {
            // Use AudioParam interface if available (modern browsers)
            panner.positionX.setValueAtTime(position.x, currentTime);
            panner.positionY.setValueAtTime(position.y, currentTime);
            panner.positionZ.setValueAtTime(position.z, currentTime);
        } else {
            // Fallback to deprecated method
            panner.setPosition(position.x, position.y, position.z);
        }
    }
    
    updateListenerPosition(position, orientation) {
        if (position) {
            this.listenerPosition = { ...position };
        }
        
        if (orientation) {
            this.listenerOrientation = { ...orientation };
        }
        
        const currentTime = this.audioContext.currentTime;
        
        if (this.listener.positionX) {
            // Use AudioParam interface if available
            this.listener.positionX.setValueAtTime(this.listenerPosition.x, currentTime);
            this.listener.positionY.setValueAtTime(this.listenerPosition.y, currentTime);
            this.listener.positionZ.setValueAtTime(this.listenerPosition.z, currentTime);
            
            this.listener.forwardX.setValueAtTime(this.listenerOrientation.forward.x, currentTime);
            this.listener.forwardY.setValueAtTime(this.listenerOrientation.forward.y, currentTime);
            this.listener.forwardZ.setValueAtTime(this.listenerOrientation.forward.z, currentTime);
            
            this.listener.upX.setValueAtTime(this.listenerOrientation.up.x, currentTime);
            this.listener.upY.setValueAtTime(this.listenerOrientation.up.y, currentTime);
            this.listener.upZ.setValueAtTime(this.listenerOrientation.up.z, currentTime);
        } else {
            // Fallback to deprecated methods
            this.listener.setPosition(
                this.listenerPosition.x,
                this.listenerPosition.y,
                this.listenerPosition.z
            );
            
            this.listener.setOrientation(
                this.listenerOrientation.forward.x,
                this.listenerOrientation.forward.y,
                this.listenerOrientation.forward.z,
                this.listenerOrientation.up.x,
                this.listenerOrientation.up.y,
                this.listenerOrientation.up.z
            );
        }
    }
    
    generateSourceId() {
        return `spatial_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
    }
    
    disposeSpatialSource(sourceId) {
        if (this.spatialSources.has(sourceId)) {
            this.spatialSources.delete(sourceId);
        }
    }
    
    update(deltaTime, cockpitState) {
        // Update listener position based on pilot head tracking
        if (cockpitState.pilot && cockpitState.pilot.headPosition) {
            this.updateListenerPosition(
                cockpitState.pilot.headPosition,
                cockpitState.pilot.headOrientation
            );
        }
        
        // Update spatial source positions based on cockpit state
        for (const [sourceId, spatialSource] of this.spatialSources) {
            // Update positions for moving sources (if any)
            // This would be expanded based on specific moving audio sources
        }
    }
    
    dispose() {
        this.spatialSources.clear();
        if (this.convolver) {
            this.convolver.disconnect();
        }
    }
}

// Audio Performance Monitor
class AudioPerformanceMonitor {
    constructor(audioContext) {
        this.audioContext = audioContext;
        this.metrics = {
            cpuUsage: 0,
            memoryUsage: 0,
            latency: 0,
            activeVoices: 0,
            droppedFrames: 0
        };
        
        this.lastUpdateTime = performance.now();
        this.updateInterval = 1000; // Update every second
    }
    
    update(deltaTime) {
        const currentTime = performance.now();
        
        if (currentTime - this.lastUpdateTime >= this.updateInterval) {
            this.updateMetrics();
            this.lastUpdateTime = currentTime;
        }
    }
    
    updateMetrics() {
        // Calculate audio latency
        this.metrics.latency = (this.audioContext.baseLatency + this.audioContext.outputLatency) * 1000;
        
        // Estimate CPU usage (simplified)
        this.metrics.cpuUsage = this.estimateCPUUsage();
        
        // Memory usage estimation
        this.metrics.memoryUsage = this.estimateMemoryUsage();
        
        // Log performance warnings
        if (this.metrics.latency > 50) {
            console.warn(`High audio latency detected: ${this.metrics.latency.toFixed(2)}ms`);
        }
        
        if (this.metrics.cpuUsage > 15) {
            console.warn(`High audio CPU usage detected: ${this.metrics.cpuUsage.toFixed(1)}%`);
        }
    }
    
    estimateCPUUsage() {
        // Simplified CPU usage estimation based on active processing
        // In a real implementation, this would use more sophisticated monitoring
        return Math.min(this.metrics.activeVoices * 0.5, 100);
    }
    
    estimateMemoryUsage() {
        // Simplified memory usage estimation
        // In a real implementation, this would track actual buffer memory usage
        return this.metrics.activeVoices * 2; // MB estimate
    }
    
    getMetrics() {
        return { ...this.metrics };
    }
}

// Export the main audio engine
export { CockpitAudioEngine, SpatialAudioEngine, AudioPerformanceMonitor };
```

VALIDATION CHECKPOINT:
After implementation, CURSOR MUST verify:
✓ Web Audio API context is properly initialized and running
✓ Spatial audio engine provides accurate 3D positioning
✓ Audio buffer management handles loading and caching efficiently
✓ Performance monitoring tracks all critical metrics
✓ Audio processing chain maintains low latency
✓ HRTF processing provides realistic spatial audio
✓ Memory usage remains within specified limits
✓ CPU usage stays below 10% threshold

QUALITY GATE:
✓ Spatial audio positioning matches 3D cockpit geometry
✓ Audio latency remains below 20ms for interactive sounds
✓ Performance monitoring provides accurate real-time metrics
✓ Audio buffer management prevents memory leaks
✓ HRTF processing delivers immersive spatial experience
✓ Audio system integrates seamlessly with Three.js scene
```

**GAP IDENTIFICATION FOR PHASE 1.1**:
```
CURSOR MUST CHECK FOR THESE POTENTIAL GAPS:
❌ Missing Web Audio API initialization causing system failure
❌ Improper spatial audio setup limiting 3D immersion
❌ Inadequate performance monitoring preventing optimization
❌ Poor audio buffer management causing memory issues
❌ Missing HRTF implementation reducing spatial accuracy
❌ Incorrect coordinate system integration with Three.js
❌ Insufficient error handling causing system instability
❌ Missing audio context state management
```

## Prompt 1.2: Advanced Audio Processing Pipeline

**PREREQUISITE VALIDATION**:
```
CURSOR MUST VERIFY FROM PHASE 1.1:
✓ Web Audio API foundation is complete and functional
✓ Spatial audio engine provides accurate 3D positioning
✓ Audio buffer management system is working properly
✓ Performance monitoring tracks all critical metrics
✓ Audio context is properly initialized and managed
✓ HRTF processing delivers spatial audio experience
```

**CURSOR RULES FOR THIS PROMPT**:
1. MUST implement ALL advanced Web Audio API features for professional audio
2. Each audio system MUST have complete real-time processing capabilities
3. MUST validate each audio processor maintains performance requirements
4. Audio quality MUST be measured and optimized continuously

**DETAILED IMPLEMENTATION**:
```
Configure advanced Web Audio API processing pipeline for professional-quality output:

MANDATORY ADVANCED AUDIO PROCESSING FEATURES:

1. DYNAMIC RANGE PROCESSING (COMPLETE IMPLEMENTATION REQUIRED):
   - MUST implement multi-band compression for engine audio:
     * Low-frequency compression for engine rumble (20-200Hz)
     * Mid-frequency processing for mechanical sounds (200Hz-2kHz)
     * High-frequency enhancement for detail sounds (2kHz-20kHz)
     * Automatic gain control to prevent clipping
   - MUST support adaptive dynamics based on flight conditions:
     * Altitude-based atmospheric filtering
     * Speed-based Doppler effect processing
     * G-force impact on audio perception
     * Environmental condition adaptation (weather, time of day)
   - MUST implement real-time limiter for hearing protection:
     * Peak limiting at safe levels for extended use
     * Soft knee compression for natural sound
     * Look-ahead processing to prevent audio artifacts
     * Emergency volume reduction for sudden loud sounds

2. ADVANCED FILTERING SYSTEM (ALL TECHNIQUES REQUIRED):
   - Frequency-based audio enhancement:
     * MUST implement parametric EQ with 8+ bands
     * MUST use high-quality IIR filters for smooth response
     * MUST implement automatic frequency balancing
     * MUST support real-time frequency analysis and adjustment
   - Environmental audio filtering:
     * MUST implement altitude-based high-frequency rolloff
     * MUST add atmospheric absorption modeling
     * MUST simulate cockpit acoustic properties
     * MUST implement material-based sound transmission

3. REAL-TIME AUDIO SYNTHESIS (COMPLETE IMPLEMENTATION):
   - Procedural engine audio generation:
     * MUST implement turbofan engine synthesis using oscillators
     * MUST create realistic engine spool-up/down transitions
     * MUST generate afterburner ignition and operation sounds
     * MUST synthesize compressor stall and surge effects
   - Interactive control audio synthesis:
     * MUST generate switch click variations based on switch type
     * MUST create button press feedback with tactile correlation
     * MUST synthesize rotary control detent clicks
     * MUST generate lever movement audio with mechanical accuracy

4. ADVANCED SPATIAL PROCESSING (FULL IMPLEMENTATION):
   - Enhanced HRTF implementation:
     * MUST support multiple HRTF datasets for different head sizes
     * MUST implement smooth HRTF interpolation for head movement
     * MUST add personalized HRTF calibration system
     * MUST support binaural rendering for headphone optimization
   - Complex occlusion modeling:
     * MUST implement ray-casting for accurate sound blocking
     * MUST support partial occlusion with frequency-dependent filtering
     * MUST add material-based sound transmission properties
     * MUST implement dynamic occlusion based on cockpit geometry

COMPLETE IMPLEMENTATION REQUIREMENTS:

Advanced Audio Processing MUST include:
```javascript
// Advanced Audio Processing Pipeline
class AdvancedAudioProcessor {
    constructor(audioContext, spatialEngine) {
        this.audioContext = audioContext;
        this.spatialEngine = spatialEngine;
        
        // Initialize processing modules
        this.dynamicsProcessor = new DynamicsProcessor(audioContext);
        this.filterSystem = new AdvancedFilterSystem(audioContext);
        this.synthesisEngine = new AudioSynthesisEngine(audioContext);
        this.occlusionProcessor = new OcclusionProcessor(audioContext);
        
        // Processing chains for different audio categories
        this.processingChains = new Map();
        this.setupProcessingChains();
        
        // Real-time analysis
        this.audioAnalyzer = new RealTimeAudioAnalyzer(audioContext);
        
        // Performance optimization
        this.processingOptimizer = new ProcessingOptimizer();
    }
    
    setupProcessingChains() {
        // Engine Audio Processing Chain
        this.processingChains.set('engine', {
            compressor: this.createMultibandCompressor('engine'),
            filter: this.createEngineFilter(),
            synthesizer: this.synthesisEngine.createEngineProcessor(),
            spatializer: this.spatialEngine
        });
        
        // Control Audio Processing Chain
        this.processingChains.set('control', {
            synthesizer: this.synthesisEngine.createControlProcessor(),
            filter: this.createControlFilter(),
            spatializer: this.spatialEngine,
            limiter: this.createSafetyLimiter()
        });
        
        // Alert Audio Processing Chain
        this.processingChains.set('alert', {
            filter: this.createAlertFilter(),
            compressor: this.createAlertCompressor(),
            priority: this.createPriorityProcessor(),
            limiter: this.createSafetyLimiter()
        });
        
        // Environmental Audio Processing Chain
        this.processingChains.set('environment', {
            filter: this.createEnvironmentalFilter(),
            reverb: this.createEnvironmentalReverb(),
            occlusion: this.occlusionProcessor,
            spatializer: this.spatialEngine
        });
    }
    
    createMultibandCompressor(category) {
        return new MultibandCompressor(this.audioContext, {
            lowBand: { frequency: 200, ratio: 4, threshold: -20, attack: 0.003, release: 0.1 },
            midBand: { frequency: 2000, ratio: 3, threshold: -15, attack: 0.005, release: 0.05 },
            highBand: { frequency: 8000, ratio: 2, threshold: -10, attack: 0.001, release: 0.02 }
        });
    }
    
    createEngineFilter() {
        const filter = new ParametricEQ(this.audioContext, [
            { type: 'highpass', frequency: 20, Q: 0.7 },
            { type: 'peaking', frequency: 60, Q: 2, gain: 3 },    // Engine rumble
            { type: 'peaking', frequency: 200, Q: 1.5, gain: 2 }, // Turbine whine
            { type: 'peaking', frequency: 800, Q: 1, gain: -2 },  // Reduce harshness
            { type: 'peaking', frequency: 3000, Q: 2, gain: 4 },  // Air flow detail
            { type: 'highshelf', frequency: 8000, gain: -3 }      // Smooth high end
        ]);
        return filter;
    }
    
    processAudio(inputNode, category, options = {}) {
        const chain = this.processingChains.get(category);
        if (!chain) {
            console.warn(`No processing chain found for category: ${category}`);
            return inputNode;
        }
        
        let processedNode = inputNode;
        
        // Apply processing chain in order
        if (chain.synthesizer && options.synthesize) {
            processedNode = chain.synthesizer.process(processedNode, options);
        }
        
        if (chain.filter) {
            processedNode = chain.filter.process(processedNode, options);
        }
        
        if (chain.compressor) {
            processedNode = chain.compressor.process(processedNode, options);
        }
        
        if (chain.occlusion && options.position) {
            processedNode = chain.occlusion.process(processedNode, options.position);
        }
        
        if (chain.spatializer && options.position) {
            processedNode = chain.spatializer.createSpatialSource(processedNode, options.position);
        }
        
        if (chain.limiter) {
            processedNode = chain.limiter.process(processedNode, options);
        }
        
        return processedNode;
    }
}

// Multiband Compressor Implementation
class MultibandCompressor {
    constructor(audioContext, config) {
        this.audioContext = audioContext;
        this.config = config;
        
        // Create frequency splitting filters
        this.lowpassFilter = audioContext.createBiquadFilter();
        this.lowpassFilter.type = 'lowpass';
        this.lowpassFilter.frequency.setValueAtTime(config.lowBand.frequency, audioContext.currentTime);
        
        this.bandpassFilter = audioContext.createBiquadFilter();
        this.bandpassFilter.type = 'bandpass';
        this.bandpassFilter.frequency.setValueAtTime(config.midBand.frequency, audioContext.currentTime);
        this.bandpassFilter.Q.setValueAtTime(2, audioContext.currentTime);
        
        this.highpassFilter = audioContext.createBiquadFilter();
        this.highpassFilter.type = 'highpass';
        this.highpassFilter.frequency.setValueAtTime(config.highBand.frequency, audioContext.currentTime);
        
        // Create compressors for each band
        this.lowCompressor = this.createCompressor(config.lowBand);
        this.midCompressor = this.createCompressor(config.midBand);
        this.highCompressor = this.createCompressor(config.highBand);
        
        // Create output mixer
        this.outputMixer = audioContext.createGain();
        
        // Connect processing chain
        this.setupProcessingChain();
    }
    
    createCompressor(bandConfig) {
        const compressor = this.audioContext.createDynamicsCompressor();
        compressor.threshold.setValueAtTime(bandConfig.threshold, this.audioContext.currentTime);
        compressor.knee.setValueAtTime(2, this.audioContext.currentTime);
        compressor.ratio.setValueAtTime(bandConfig.ratio, this.audioContext.currentTime);
        compressor.attack.setValueAtTime(bandConfig.attack, this.audioContext.currentTime);
        compressor.release.setValueAtTime(bandConfig.release, this.audioContext.currentTime);
        return compressor;
    }
    
    setupProcessingChain() {
        // Connect filters to compressors
        this.lowpassFilter.connect(this.lowCompressor);
        this.bandpassFilter.connect(this.midCompressor);
        this.highpassFilter.connect(this.highCompressor);
        
        // Connect compressors to output mixer
        this.lowCompressor.connect(this.outputMixer);
        this.midCompressor.connect(this.outputMixer);
        this.highCompressor.connect(this.outputMixer);
    }
    
    process(inputNode, options = {}) {
        // Connect input to all frequency bands
        inputNode.connect(this.lowpassFilter);
        inputNode.connect(this.bandpassFilter);
        inputNode.connect(this.highpassFilter);
        
        // Apply dynamic adjustments based on options
        if (options.altitude) {
            this.adjustForAltitude(options.altitude);
        }
        
        if (options.speed) {
            this.adjustForSpeed(options.speed);
        }
        
        return this.outputMixer;
    }
    
    adjustForAltitude(altitude) {
        // Simulate atmospheric effects at different altitudes
        const altitudeNormalized = Math.min(altitude / 50000, 1); // Normalize to 50,000 ft
        
        // Reduce high frequencies at higher altitudes
        const highFreqReduction = altitudeNormalized * 0.3;
        this.highCompressor.threshold.setValueAtTime(
            this.config.highBand.threshold - (highFreqReduction * 10),
            this.audioContext.currentTime
        );
    }
    
    adjustForSpeed(speed) {
        // Adjust compression based on aircraft speed
        const speedNormalized = Math.min(speed / 1000, 1); // Normalize to Mach 1+
        
        // Increase compression at higher speeds for wind noise simulation
        const compressionIncrease = speedNormalized * 2;
        this.midCompressor.ratio.setValueAtTime(
            this.config.midBand.ratio + compressionIncrease,
            this.audioContext.currentTime
        );
    }
}

// Parametric EQ Implementation
class ParametricEQ {
    constructor(audioContext, bands) {
        this.audioContext = audioContext;
        this.bands = [];
        
        // Create filter nodes for each EQ band
        bands.forEach((bandConfig, index) => {
            const filter = audioContext.createBiquadFilter();
            filter.type = bandConfig.type;
            filter.frequency.setValueAtTime(bandConfig.frequency, audioContext.currentTime);
            
            if (bandConfig.Q) {
                filter.Q.setValueAtTime(bandConfig.Q, audioContext.currentTime);
            }
            
            if (bandConfig.gain) {
                filter.gain.setValueAtTime(bandConfig.gain, audioContext.currentTime);
            }
            
            this.bands.push({
                filter: filter,
                config: bandConfig
            });
        });
        
        // Chain filters together
        this.chainFilters();
    }
    
    chainFilters() {
        for (let i = 0; i < this.bands.length - 1; i++) {
            this.bands[i].filter.connect(this.bands[i + 1].filter);
        }
    }
    
    process(inputNode, options = {}) {
        if (this.bands.length === 0) return inputNode;
        
        // Connect input to first filter
        inputNode.connect(this.bands[0].filter);
        
        // Apply dynamic EQ adjustments
        if (options.environmentalFactors) {
            this.applyEnvironmentalEQ(options.environmentalFactors);
        }
        
        // Return last filter in chain
        return this.bands[this.bands.length - 1].filter;
    }
    
    applyEnvironmentalEQ(factors) {
        // Adjust EQ based on environmental conditions
        if (factors.altitude) {
            this.adjustForAltitude(factors.altitude);
        }
        
        if (factors.weather) {
            this.adjustForWeather(factors.weather);
        }
        
        if (factors.timeOfDay) {
            this.adjustForTimeOfDay(factors.timeOfDay);
        }
    }
    
    adjustForAltitude(altitude) {
        // High altitude reduces high-frequency content
        const altitudeEffect = Math.min(altitude / 40000, 1);
        
        this.bands.forEach(band => {
            if (band.config.frequency > 4000) {
                const reduction = altitudeEffect * 6; // Up to 6dB reduction
                band.filter.gain.setValueAtTime(
                    band.config.gain - reduction,
                    this.audioContext.currentTime
                );
            }
        });
    }
    
    setBandGain(bandIndex, gain) {
        if (bandIndex >= 0 && bandIndex < this.bands.length) {
            this.bands[bandIndex].filter.gain.setValueAtTime(gain, this.audioContext.currentTime);
            this.bands[bandIndex].config.gain = gain;
        }
    }
    
    setBandFrequency(bandIndex, frequency) {
        if (bandIndex >= 0 && bandIndex < this.bands.length) {
            this.bands[bandIndex].filter.frequency.setValueAtTime(frequency, this.audioContext.currentTime);
            this.bands[bandIndex].config.frequency = frequency;
        }
    }
}

// Audio Synthesis Engine
class AudioSynthesisEngine {
    constructor(audioContext) {
        this.audioContext = audioContext;
        this.oscillators = new Map();
        this.noiseGenerators = new Map();
        this.envelopes = new Map();
    }
    
    createEngineProcessor() {
        return new EngineAudioSynthesizer(this.audioContext);
    }
    
    createControlProcessor() {
        return new ControlAudioSynthesizer(this.audioContext);
    }
}

// Engine Audio Synthesizer
class EngineAudioSynthesizer {
    constructor(audioContext) {
        this.audioContext = audioContext;
        
        // Create oscillators for different engine components
        this.turbineOscillator = audioContext.createOscillator();
        this.turbineOscillator.type = 'sawtooth';
        this.turbineOscillator.frequency.setValueAtTime(200, audioContext.currentTime);
        
        this.fanOscillator = audioContext.createOscillator();
        this.fanOscillator.type = 'triangle';
        this.fanOscillator.frequency.setValueAtTime(80, audioContext.currentTime);
        
        // Create noise generator for air flow
        this.noiseBuffer = this.createNoiseBuffer();
        this.noiseSource = audioContext.createBufferSource();
        this.noiseSource.buffer = this.noiseBuffer;
        this.noiseSource.loop = true;
        
        // Create filters for shaping
        this.turbineFilter = audioContext.createBiquadFilter();
        this.turbineFilter.type = 'bandpass';
        this.turbineFilter.frequency.setValueAtTime(1000, audioContext.currentTime);
        this.turbineFilter.Q.setValueAtTime(5, audioContext.currentTime);
        
        this.fanFilter = audioContext.createBiquadFilter();
        this.fanFilter.type = 'lowpass';
        this.fanFilter.frequency.setValueAtTime(300, audioContext.currentTime);
        
        this.noiseFilter = audioContext.createBiquadFilter();
        this.noiseFilter.type = 'highpass';
        this.noiseFilter.frequency.setValueAtTime(2000, audioContext.currentTime);
        
        // Create gain controls
        this.turbineGain = audioContext.createGain();
        this.fanGain = audioContext.createGain();
        this.noiseGain = audioContext.createGain();
        this.masterGain = audioContext.createGain();
        
        // Connect synthesis chain
        this.setupSynthesisChain();
        
        // Start oscillators
        this.turbineOscillator.start();
        this.fanOscillator.start();
        this.noiseSource.start();
    }
    
    createNoiseBuffer() {
        const bufferSize = this.audioContext.sampleRate * 2; // 2 seconds of noise
        const buffer = this.audioContext.createBuffer(1, bufferSize, this.audioContext.sampleRate);
        const data = buffer.getChannelData(0);
        
        for (let i = 0; i < bufferSize; i++) {
            data[i] = Math.random() * 2 - 1;
        }
        
        return buffer;
    }
    
    setupSynthesisChain() {
        // Connect oscillators through filters to gain controls
        this.turbineOscillator.connect(this.turbineFilter);
        this.turbineFilter.connect(this.turbineGain);
        
        this.fanOscillator.connect(this.fanFilter);
        this.fanFilter.connect(this.fanGain);
        
        this.noiseSource.connect(this.noiseFilter);
        this.noiseFilter.connect(this.noiseGain);
        
        // Mix all components
        this.turbineGain.connect(this.masterGain);
        this.fanGain.connect(this.masterGain);
        this.noiseGain.connect(this.masterGain);
    }
    
    updateEngineParameters(throttlePosition, rpm, afterburner = false) {
        const currentTime = this.audioContext.currentTime;
        
        // Update turbine frequency based on RPM
        const turbineFreq = 200 + (rpm / 100) * 800; // 200-1000 Hz range
        this.turbineOscillator.frequency.exponentialRampToValueAtTime(turbineFreq, currentTime + 0.1);
        
        // Update fan frequency
        const fanFreq = 60 + (throttlePosition * 120); // 60-180 Hz range
        this.fanOscillator.frequency.exponentialRampToValueAtTime(fanFreq, currentTime + 0.1);
        
        // Update gain levels based on throttle
        this.turbineGain.gain.exponentialRampToValueAtTime(0.1 + (throttlePosition * 0.4), currentTime + 0.1);
        this.fanGain.gain.exponentialRampToValueAtTime(0.2 + (throttlePosition * 0.3), currentTime + 0.1);
        this.noiseGain.gain.exponentialRampToValueAtTime(0.05 + (throttlePosition * 0.2), currentTime + 0.1);
        
        // Afterburner effect
        if (afterburner) {
            this.addAfterburnerEffect();
        } else {
            this.removeAfterburnerEffect();
        }
    }
    
    addAfterburnerEffect() {
        // Add high-frequency content and increase overall level for afterburner
        const currentTime = this.audioContext.currentTime;
        
        this.noiseFilter.frequency.exponentialRampToValueAtTime(4000, currentTime + 0.05);
        this.noiseGain.gain.exponentialRampToValueAtTime(0.8, currentTime + 0.05);
        this.turbineGain.gain.exponentialRampToValueAtTime(0.9, currentTime + 0.05);
    }
    
    removeAfterburnerEffect() {
        // Return to normal engine operation
        const currentTime = this.audioContext.currentTime;
        
        this.noiseFilter.frequency.exponentialRampToValueAtTime(2000, currentTime + 0.2);
        // Gain levels will be set by updateEngineParameters
    }
    
    process(inputNode, options = {}) {
        // Update synthesis based on engine parameters
        if (options.engineState) {
            this.updateEngineParameters(
                options.engineState.throttle,
                options.engineState.rpm,
                options.engineState.afterburner
            );
        }
        
        return this.masterGain;
    }
}

// Export advanced processing classes
export { 
    AdvancedAudioProcessor, 
    MultibandCompressor, 
    ParametricEQ, 
    AudioSynthesisEngine,
    EngineAudioSynthesizer 
};
```

VALIDATION REQUIREMENTS:
CURSOR MUST verify after implementation:
✓ All advanced processing modules work without performance degradation
✓ Multiband compression provides natural dynamic control
✓ Parametric EQ responds correctly to environmental changes
✓ Audio synthesis generates realistic engine and control sounds
✓ Spatial processing maintains HRTF accuracy with complex audio
✓ Performance optimization keeps CPU usage below 10%
✓ Real-time parameter changes occur smoothly without artifacts
✓ All processing chains maintain audio quality standards

PERFORMANCE BENCHMARKS (MUST ACHIEVE):
✓ Advanced processing latency: <5ms additional delay
✓ Multiband compression: <2% CPU usage per instance
✓ Parametric EQ: <1% CPU usage per band
✓ Audio synthesis: <3% CPU usage per synthesizer
✓ Real-time parameter updates: <1ms response time
✓ Memory usage: <32MB for all advanced processing
```

**GAP IDENTIFICATION FOR PHASE 1.2**:
```
CURSOR MUST CHECK FOR THESE CRITICAL GAPS:
❌ Missing advanced processing causing poor audio quality
❌ Incomplete multiband compression limiting dynamic range
❌ Poor parametric EQ implementation reducing frequency control
❌ Missing audio synthesis preventing realistic engine sounds
❌ Inadequate spatial processing reducing immersion quality
❌ Performance bottlenecks causing audio dropouts
❌ Missing real-time parameter control limiting interactivity
❌ Insufficient optimization causing CPU overload
```

## Prompt 1.3: Audio Asset Management & Integration Pipeline

**PREREQUISITE VALIDATION**:
```
CURSOR MUST VERIFY FROM PHASES 1.1-1.2:
✓ Complete Web Audio API foundation with spatial processing
✓ Advanced audio processing pipeline with all modules functional
✓ Multiband compression and parametric EQ working correctly
✓ Audio synthesis generating realistic engine and control sounds
✓ Performance monitoring maintaining all benchmarks
✓ Spatial audio engine providing accurate 3D positioning
✓ Real-time processing maintaining low latency requirements
```

**CURSOR RULES FOR THIS PROMPT**:
1. MUST implement complete audio asset management system
2. ALL audio formats must be supported with optimal compression
3. MUST implement automated quality validation for all audio assets
4. Integration pipeline MUST be tested and validated with Three.js

**DETAILED IMPLEMENTATION**:
```
Implement comprehensive audio asset management and Three.js integration pipeline:

MANDATORY AUDIO ASSET MANAGEMENT FEATURES:

1. INTELLIGENT AUDIO LOADING SYSTEM (COMPLETE IMPLEMENTATION):
   - MUST implement progressive audio loading based on priority:
     * Critical alerts and warnings: Immediate preload
     * Interactive controls: Load on scene initialization
     * Environmental audio: Stream on demand
     * Background ambience: Lazy load with fade-in
   - MUST support multiple audio formats with automatic fallback:
     * Primary: OGG Vorbis for optimal compression and quality
     * Fallback: MP3 for broad browser compatibility
     * Lossless: WAV for critical audio assets
     * Streaming: WebM for large environmental audio
   - MUST implement intelligent caching with memory management:
     * LRU cache for frequently used audio assets
     * Automatic cache cleanup based on memory pressure
     * Persistent cache using IndexedDB for offline capability
     * Cache warming for predicted audio needs

2. AUDIO QUALITY OPTIMIZATION PIPELINE (ALL FEATURES REQUIRED):
   - Automatic audio format conversion and optimization:
     * MUST implement real-time audio analysis for optimal encoding
     * MUST use perceptual audio coding for maximum compression
     * MUST maintain psychoacoustic quality standards
     * MUST implement adaptive bitrate based on content complexity
   - Dynamic quality scaling based on device capabilities:
     * MUST detect device audio capabilities and adjust accordingly
     * MUST implement quality profiles (Low, Medium, High, Ultra)
     * MUST support automatic quality switching based on performance
     * MUST maintain seamless quality transitions without artifacts

3. COMPREHENSIVE AUDIO VALIDATION SYSTEM (FULL IMPLEMENTATION):
   - Automated audio asset quality assurance:
     * MUST validate audio format compliance and compatibility
     * MUST check for audio artifacts (clipping, distortion, noise)
     * MUST verify spatial audio metadata and positioning data
     * MUST validate loop points and seamless playback capability
   - Performance impact assessment:
     * MUST measure CPU usage for each audio processing chain
     * MUST validate memory usage and garbage collection impact
     * MUST test audio latency under various system loads
     * MUST verify real-time performance with full audio system

4. THREE.JS INTEGRATION PIPELINE (COMPLETE IMPLEMENTATION):
   - Seamless coordinate system integration:
     * MUST synchronize audio positioning with Three.js object transforms
     * MUST implement automatic audio source tracking for moving objects
     * MUST support dynamic audio attachment to Three.js meshes
     * MUST maintain spatial accuracy during scene transformations
   - Performance optimization for real-time rendering:
     * MUST implement audio LOD system matching visual LOD
     * MUST support audio culling based on camera distance and orientation
     * MUST implement automatic quality scaling based on frame rate
     * MUST maintain 60 FPS performance with full audio system active

COMPLETE IMPLEMENTATION REQUIREMENTS:

Audio Asset Management System MUST include:
```javascript
// Comprehensive Audio Asset Management System
class AudioAssetManager {
    constructor(audioEngine) {
        this.audioEngine = audioEngine;
        this.audioContext = audioEngine.audioContext;
        
        // Asset storage and caching
        this.assetCache = new Map();
        this.loadingQueue = new PriorityQueue();
        this.streamingAssets = new Map();
        
        // Quality management
        this.qualityProfiles = this.initializeQualityProfiles();
        this.currentQualityProfile = 'high';
        this.deviceCapabilities = null;
        
        // Format support detection
        this.supportedFormats = this.detectSupportedFormats();
        
        // Performance monitoring
        this.performanceMetrics = {
            loadTimes: [],
            memoryUsage: 0,
            cacheHitRate: 0,
            streamingLatency: 0
        };
        
        // IndexedDB for persistent caching
        this.persistentCache = null;
        this.initializePersistentCache();
        
        // Asset validation system
        this.validator = new AudioAssetValidator(this.audioContext);
        
        // Three.js integration
        this.threeJSBridge = new ThreeJSAudioBridge(this.audioEngine);
    }
    
    initializeQualityProfiles() {
        return {
            'ultra': {
                sampleRate: 48000,
                bitRate: 320,
                spatialQuality: 'hrtf',
                reverbQuality: 'high',
                processingQuality: 'maximum'
            },
            'high': {
                sampleRate: 48000,
                bitRate: 192,
                spatialQuality: 'hrtf',
                reverbQuality: 'medium',
                processingQuality: 'high'
            },
            'medium': {
                sampleRate: 44100,
                bitRate: 128,
                spatialQuality: 'stereo',
                reverbQuality: 'low',
                processingQuality: 'medium'
            },
            'low': {
                sampleRate: 22050,
                bitRate: 96,
                spatialQuality: 'mono',
                reverbQuality: 'off',
                processingQuality: 'low'
            }
        };
    }
    
    detectSupportedFormats() {
        const audio = document.createElement('audio');
        const formats = {
            ogg: audio.canPlayType('audio/ogg; codecs="vorbis"') !== '',
            mp3: audio.canPlayType('audio/mpeg') !== '',
            wav: audio.canPlayType('audio/wav') !== '',
            webm: audio.canPlayType('audio/webm') !== '',
            aac: audio.canPlayType('audio/aac') !== ''
        };
        
        console.log('Supported audio formats:', formats);
        return formats;
    }
    
    async initializePersistentCache() {
        try {
            this.persistentCache = await this.openIndexedDB('CockpitAudioCache', 1);
            console.log('Persistent audio cache initialized');
        } catch (error) {
            console.warn('Failed to initialize persistent cache:', error);
        }
    }
    
    openIndexedDB(name, version) {
        return new Promise((resolve, reject) => {
            const request = indexedDB.open(name, version);
            
            request.onerror = () => reject(request.error);
            request.onsuccess = () => resolve(request.result);
            
            request.onupgradeneeded = (event) => {
                const db = event.target.result;
                
                // Create object stores
                if (!db.objectStoreNames.contains('audioAssets')) {
                    const store = db.createObjectStore('audioAssets', { keyPath: 'id' });
                    store.createIndex('priority', 'priority', { unique: false });
                    store.createIndex('lastAccessed', 'lastAccessed', { unique: false });
                }
            };
        });
    }
    
    async loadAudioAsset(assetId, options = {}) {
        const startTime = performance.now();
        
        // Check cache first
        if (this.assetCache.has(assetId)) {
            const cachedAsset = this.assetCache.get(assetId);
            cachedAsset.lastAccessed = Date.now();
            this.updateCacheHitRate(true);
            return cachedAsset.buffer;
        }
        
        // Check persistent cache
        if (this.persistentCache) {
            const persistentAsset = await this.getFromPersistentCache(assetId);
            if (persistentAsset) {
                const audioBuffer = await this.audioContext.decodeAudioData(persistentAsset.data);
                this.cacheAudioAsset(assetId, audioBuffer, persistentAsset.metadata);
                this.updateCacheHitRate(true);
                return audioBuffer;
            }
        }
        
        this.updateCacheHitRate(false);
        
        // Load from network
        const assetMetadata = this.getAssetMetadata(assetId);
        const audioBuffer = await this.loadFromNetwork(assetMetadata, options);
        
        // Validate audio quality
        const validationResult = await this.validator.validateAudioAsset(audioBuffer, assetMetadata);
        if (!validationResult.isValid) {
            console.warn(`Audio asset validation failed for ${assetId}:`, validationResult.issues);
        }
        
        // Cache the loaded asset
        this.cacheAudioAsset(assetId, audioBuffer, assetMetadata);
        
        // Store in persistent cache
        if (this.persistentCache && assetMetadata.cacheable) {
            await this.storeToPersistentCache(assetId, audioBuffer, assetMetadata);
        }
        
        // Update performance metrics
        const loadTime = performance.now() - startTime;
        this.performanceMetrics.loadTimes.push(loadTime);
        
        console.log(`Loaded audio asset ${assetId} in ${loadTime.toFixed(2)}ms`);
        
        return audioBuffer;
    }
    
    async loadFromNetwork(assetMetadata, options = {}) {
        const urls = this.getAssetUrls(assetMetadata);
        let lastError = null;
        
        // Try each format in order of preference
        for (const url of urls) {
            try {
                const response = await fetch(url);
                if (!response.ok) {
                    throw new Error(`HTTP ${response.status}: ${response.statusText}`);
                }
                
                const arrayBuffer = await response.arrayBuffer();
                
                // Apply quality optimization if needed
                const optimizedBuffer = await this.optimizeAudioBuffer(arrayBuffer, assetMetadata);
                
                const audioBuffer = await this.audioContext.decodeAudioData(optimizedBuffer);
                return audioBuffer;
                
            } catch (error) {
                console.warn(`Failed to load audio from ${url}:`, error);
                lastError = error;
                continue;
            }
        }
        
        throw new Error(`Failed to load audio asset: ${lastError?.message || 'All formats failed'}`);
    }
    
    getAssetUrls(assetMetadata) {
        const baseUrl = assetMetadata.baseUrl || '/audio/';
        const urls = [];
        
        // Order formats by preference and browser support
        const formatPreference = ['ogg', 'webm', 'mp3', 'wav'];
        
        for (const format of formatPreference) {
            if (this.supportedFormats[format] && assetMetadata.formats[format]) {
                urls.push(`${baseUrl}${assetMetadata.formats[format]}`);
            }
        }
        
        return urls;
    }
    
    async optimizeAudioBuffer(arrayBuffer, assetMetadata) {
        const currentProfile = this.qualityProfiles[this.currentQualityProfile];
        
        // If current quality matches source, return as-is
        if (assetMetadata.sampleRate === currentProfile.sampleRate && 
            assetMetadata.bitRate >= currentProfile.bitRate) {
            return arrayBuffer;
        }
        
        // For now, return original buffer
        // In production, this would implement real-time transcoding
        console.log(`Audio optimization needed for quality profile: ${this.currentQualityProfile}`);
        return arrayBuffer;
    }
    
    cacheAudioAsset(assetId, audioBuffer, metadata) {
        const cacheEntry = {
            id: assetId,
            buffer: audioBuffer,
            metadata: metadata,
            lastAccessed: Date.now(),
            memorySize: this.calculateBufferSize(audioBuffer)
        };
        
        this.assetCache.set(assetId, cacheEntry);
        this.updateMemoryUsage();
        
        // Implement LRU cache cleanup if memory limit exceeded
        this.enforceMemoryLimit();
    }
    
    calculateBufferSize(audioBuffer) {
        // Estimate memory usage: channels * length * 4 bytes per float32 sample
        return audioBuffer.numberOfChannels * audioBuffer.length * 4;
    }
    
    updateMemoryUsage() {
        let totalMemory = 0;
        for (const [id, entry] of this.assetCache) {
            totalMemory += entry.memorySize;
        }
        this.performanceMetrics.memoryUsage = totalMemory;
    }
    
    enforceMemoryLimit() {
        const maxMemory = 128 * 1024 * 1024; // 128MB limit
        
        if (this.performanceMetrics.memoryUsage <= maxMemory) return;
        
        // Sort cache entries by last accessed time (LRU)
        const sortedEntries = Array.from(this.assetCache.entries())
            .sort((a, b) => a[1].lastAccessed - b[1].lastAccessed);
        
        // Remove oldest entries until under memory limit
        while (this.performanceMetrics.memoryUsage > maxMemory && sortedEntries.length > 0) {
            const [assetId, entry] = sortedEntries.shift();
            this.assetCache.delete(assetId);
            this.performanceMetrics.memoryUsage -= entry.memorySize;
            console.log(`Evicted audio asset ${assetId} from cache (LRU)`);
        }
    }
    
    updateCacheHitRate(isHit) {
        // Simple moving average for cache hit rate
        const alpha = 0.1;
        this.performanceMetrics.cacheHitRate = 
            this.performanceMetrics.cacheHitRate * (1 - alpha) + (isHit ? 1 : 0) * alpha;
    }
    
    async getFromPersistentCache(assetId) {
        if (!this.persistentCache) return null;
        
        try {
            const transaction = this.persistentCache.transaction(['audioAssets'], 'readonly');
            const store = transaction.objectStore('audioAssets');
            const request = store.get(assetId);
            
            return new Promise((resolve, reject) => {
                request.onsuccess = () => resolve(request.result);
                request.onerror = () => reject(request.error);
            });
        } catch (error) {
            console.warn('Failed to read from persistent cache:', error);
            return null;
        }
    }
    
    async storeToPersistentCache(assetId, audioBuffer, metadata) {
        if (!this.persistentCache) return;
        
        try {
            // Convert AudioBuffer back to ArrayBuffer for storage
            const arrayBuffer = await this.audioBufferToArrayBuffer(audioBuffer);
            
            const cacheEntry = {
                id: assetId,
                data: arrayBuffer,
                metadata: metadata,
                timestamp: Date.now()
            };
            
            const transaction = this.persistentCache.transaction(['audioAssets'], 'readwrite');
            const store = transaction.objectStore('audioAssets');
            await store.put(cacheEntry);
            
        } catch (error) {
            console.warn('Failed to store to persistent cache:', error);
        }
    }
    
    async audioBufferToArrayBuffer(audioBuffer) {
        // This is a simplified conversion - in production would use proper encoding
        const length = audioBuffer.length * audioBuffer.numberOfChannels;
        const arrayBuffer = new ArrayBuffer(length * 4);
        const view = new Float32Array(arrayBuffer);
        
        let offset = 0;
        for (let channel = 0; channel < audioBuffer.numberOfChannels; channel++) {
            const channelData = audioBuffer.getChannelData(channel);
            view.set(channelData, offset);
            offset += channelData.length;
        }
        
        return arrayBuffer;
    }
    
    getAssetMetadata(assetId) {
        // This would typically come from a configuration file or API
        const assetDatabase = {
            'master_caution': {
                baseUrl: '/audio/alerts/',
                formats: {
                    ogg: 'master_caution.ogg',
                    mp3: 'master_caution.mp3',
                    wav: 'master_caution.wav'
                },
                sampleRate: 48000,
                bitRate: 192,
                priority: 'critical',
                cacheable: true,
                category: 'alert'
            },
            'engine_idle': {
                baseUrl: '/audio/engine/',
                formats: {
                    ogg: 'turbofan_idle_loop.ogg',
                    webm: 'turbofan_idle_loop.webm'
                },
                sampleRate: 48000,
                bitRate: 256,
                priority: 'high',
                cacheable: true,
                category: 'engine',
                looping: true
            }
            // ... more asset definitions
        };
        
        return assetDatabase[assetId] || null;
    }
    
    setQualityProfile(profileName) {
        if (!this.qualityProfiles[profileName]) {
            console.warn(`Unknown quality profile: ${profileName}`);
            return;
        }
        
        this.currentQualityProfile = profileName;
        console.log(`Audio quality profile set to: ${profileName}`);
        
        // Notify audio engine of quality change
        this.audioEngine.updateQualitySettings(this.qualityProfiles[profileName]);
    }
    
    getPerformanceMetrics() {
        return {
            ...this.performanceMetrics,
            cacheSize: this.assetCache.size,
            averageLoadTime: this.performanceMetrics.loadTimes.length > 0 
                ? this.performanceMetrics.loadTimes.reduce((a, b) => a + b) / this.performanceMetrics.loadTimes.length 
                : 0
        };
    }
    
    dispose() {
        // Clear all caches
        this.assetCache.clear();
        this.streamingAssets.clear();
        
        // Close persistent cache
        if (this.persistentCache) {
            this.persistentCache.close();
        }
        
        // Dispose validator and bridge
        if (this.validator) {
            this.validator.dispose();
        }
        
        if (this.threeJSBridge) {
            this.threeJSBridge.dispose();
        }
    }
}

// Audio Asset Validator
class AudioAssetValidator {
    constructor(audioContext) {
        this.audioContext = audioContext;
        this.analyser = audioContext.createAnalyser();
        this.analyser.fftSize = 2048;
    }
    
    async validateAudioAsset(audioBuffer, metadata) {
        const issues = [];
        let isValid = true;
        
        // Check basic properties
        if (audioBuffer.duration === 0) {
            issues.push('Audio buffer has zero duration');
            isValid = false;
        }
        
        if (audioBuffer.sampleRate !== metadata.sampleRate) {
            issues.push(`Sample rate mismatch: expected ${metadata.sampleRate}, got ${audioBuffer.sampleRate}`);
        }
        
        // Check for clipping
        const clippingResult = this.detectClipping(audioBuffer);
        if (clippingResult.hasClipping) {
            issues.push(`Clipping detected: ${clippingResult.clippedSamples} samples`);
            if (clippingResult.clippedSamples > audioBuffer.length * 0.01) {
                isValid = false; // More than 1% clipped samples is critical
            }
        }
        
        // Check for silence
        const silenceResult = this.detectSilence(audioBuffer);
        if (silenceResult.isSilent) {
            issues.push('Audio buffer contains only silence');
            isValid = false;
        }
        
        // Check frequency content
        const frequencyResult = this.analyzeFrequencyContent(audioBuffer);
        if (frequencyResult.hasIssues) {
            issues.push(...frequencyResult.issues);
        }
        
        return {
            isValid: isValid,
            issues: issues,
            metrics: {
                clipping: clippingResult,
                silence: silenceResult,
                frequency: frequencyResult
            }
        };
    }
    
    detectClipping(audioBuffer) {
        let clippedSamples = 0;
        const threshold = 0.99;
        
        for (let channel = 0; channel < audioBuffer.numberOfChannels; channel++) {
            const channelData = audioBuffer.getChannelData(channel);
            for (let i = 0; i < channelData.length; i++) {
                if (Math.abs(channelData[i]) >= threshold) {
                    clippedSamples++;
                }
            }
        }
        
        return {
            hasClipping: clippedSamples > 0,
            clippedSamples: clippedSamples,
            clippingPercentage: (clippedSamples / (audioBuffer.length * audioBuffer.numberOfChannels)) * 100
        };
    }
    
    detectSilence(audioBuffer) {
        const silenceThreshold = 0.001; // -60dB
        let nonSilentSamples = 0;
        
        for (let channel = 0; channel < audioBuffer.numberOfChannels; channel++) {
            const channelData = audioBuffer.getChannelData(channel);
            for (let i = 0; i < channelData.length; i++) {
                if (Math.abs(channelData[i]) > silenceThreshold) {
                    nonSilentSamples++;
                }
            }
        }
        
        const silencePercentage = ((audioBuffer.length * audioBuffer.numberOfChannels - nonSilentSamples) / 
                                 (audioBuffer.length * audioBuffer.numberOfChannels)) * 100;
        
        return {
            isSilent: nonSilentSamples === 0,
            silencePercentage: silencePercentage,
            nonSilentSamples: nonSilentSamples
        };
    }
    
    analyzeFrequencyContent(audioBuffer) {
        // This is a simplified frequency analysis
        // In production, this would use FFT analysis for detailed frequency content validation
        const issues = [];
        
        // Check if audio has reasonable frequency distribution
        // This would be expanded with actual FFT analysis
        
        return {
            hasIssues: issues.length > 0,
            issues: issues
        };
    }
    
    dispose() {
        if (this.analyser) {
            this.analyser.disconnect();
        }
    }
}

// Three.js Integration Bridge
class ThreeJSAudioBridge {
    constructor(audioEngine) {
        this.audioEngine = audioEngine;
        this.spatialEngine = audioEngine.spatialEngine;
        
        // Track audio sources attached to Three.js objects
        this.attachedSources = new Map();
        
        // Performance optimization
        this.updateQueue = [];
        this.lastUpdateTime = 0;
        this.updateInterval = 16; // ~60 FPS
    }
    
    attachAudioToObject(threeJSObject, audioSourceId, options = {}) {
        const audioSource = this.audioEngine.playAudioSource(audioSourceId, {
            ...options,
            position: threeJSObject.position
        });
        
        if (audioSource) {
            this.attachedSources.set(threeJSObject.uuid, {
                object: threeJSObject,
                audioSource: audioSource,
                options: options,
                lastPosition: threeJSObject.position.clone()
            });
            
            console.log(`Attached audio ${audioSourceId} to Three.js object ${threeJSObject.uuid}`);
        }
        
        return audioSource;
    }
    
    detachAudioFromObject(threeJSObject) {
        const attachment = this.attachedSources.get(threeJSObject.uuid);
        if (attachment) {
            attachment.audioSource.stop();
            this.attachedSources.delete(threeJSObject.uuid);
            console.log(`Detached audio from Three.js object ${threeJSObject.uuid}`);
        }
    }
    
    updateAudioPositions(deltaTime) {
        const currentTime = performance.now();
        
        if (currentTime - this.lastUpdateTime < this.updateInterval) {
            return; // Skip update to maintain performance
        }
        
        for (const [uuid, attachment] of this.attachedSources) {
            const { object, audioSource, lastPosition } = attachment;
            
            // Check if object has moved
            if (!object.position.equals(lastPosition)) {
                // Update spatial audio position
                if (audioSource.spatialSource) {
                    audioSource.spatialSource.setPosition(object.position);
                }
                
                // Update last known position
                lastPosition.copy(object.position);
            }
        }
        
        this.lastUpdateTime = currentTime;
    }
    
    setListenerFromCamera(camera) {
        if (this.spatialEngine) {
            const position = camera.position;
            const forward = new THREE.Vector3(0, 0, -1).applyQuaternion(camera.quaternion);
            const up = new THREE.Vector3(0, 1, 0).applyQuaternion(camera.quaternion);
            
            this.spatialEngine.updateListenerPosition(
                position,
                { forward: forward, up: up }
            );
        }
    }
    
    dispose() {
        // Stop all attached audio sources
        for (const [uuid, attachment] of this.attachedSources) {
            attachment.audioSource.stop();
        }
        
        this.attachedSources.clear();
    }
}

// Priority Queue for asset loading
class PriorityQueue {
    constructor() {
        this.items = [];
    }
    
    enqueue(item, priority) {
        const queueItem = { item, priority };
        let added = false;
        
        for (let i = 0; i < this.items.length; i++) {
            if (queueItem.priority > this.items[i].priority) {
                this.items.splice(i, 0, queueItem);
                added = true;
                break;
            }
        }
        
        if (!added) {
            this.items.push(queueItem);
        }
    }
    
    dequeue() {
        return this.items.shift()?.item;
    }
    
    isEmpty() {
        return this.items.length === 0;
    }
}

// Export asset management classes
export { 
    AudioAssetManager, 
    AudioAssetValidator, 
    ThreeJSAudioBridge, 
    PriorityQueue 
};
```

VALIDATION REQUIREMENTS:
CURSOR MUST verify after implementation:
✓ Audio asset management system loads all formats correctly
✓ Quality optimization maintains perceptual audio quality
✓ Caching system provides efficient memory management
✓ Persistent cache enables offline audio capability
✓ Asset validation detects all common audio issues
✓ Three.js integration maintains spatial accuracy
✓ Performance optimization keeps system responsive
✓ All audio formats fallback gracefully

PERFORMANCE BENCHMARKS (MUST ACHIEVE):
✓ Asset loading time: <2 seconds for critical assets
✓ Cache hit rate: >80% for frequently used assets
✓ Memory usage: <128MB for complete audio system
✓ Persistent cache access: <100ms for cached assets
✓ Three.js position updates: <1ms per attached source
✓ Quality switching: <500ms transition time
✓ Asset validation: <50ms per audio file
✓ Network fallback: <5 seconds maximum load time
```

**GAP IDENTIFICATION FOR PHASE 1.3**:
```
CURSOR MUST CHECK FOR THESE CRITICAL GAPS:
❌ Missing asset management causing loading failures
❌ Incomplete quality optimization reducing audio fidelity
❌ Poor caching implementation causing memory issues
❌ Missing format fallback preventing broad compatibility
❌ Inadequate validation allowing corrupted audio assets
❌ Incomplete Three.js integration breaking spatial accuracy
❌ Performance bottlenecks causing audio dropouts
❌ Missing persistent cache reducing offline capability
```

## PHASE 1 COMPLETION CHECKLIST

### ✅ **WEB AUDIO API VALIDATION REQUIREMENTS**
- [ ] Complete audio engine with spatial processing functional
- [ ] Advanced audio processing pipeline maintaining quality standards
- [ ] Asset management system supporting all required formats
- [ ] Audio validation system detecting all common issues
- [ ] Three.js integration providing accurate spatial positioning
- [ ] Performance monitoring maintaining all specified benchmarks
- [ ] Quality optimization system adapting to device capabilities
- [ ] Persistent caching enabling offline audio functionality

### ✅ **QUALITY GATES**
- [ ] Spatial audio positioning matches 3D cockpit geometry perfectly
- [ ] Audio latency remains below 20ms for all interactive sounds
- [ ] Performance metrics stay within specified limits continuously
- [ ] Asset loading system handles all formats with graceful fallback
- [ ] Audio processing maintains professional aviation quality standards
- [ ] Memory management prevents leaks and maintains efficiency
- [ ] Real-time parameter changes occur smoothly without artifacts

### ✅ **PERFORMANCE BENCHMARKS**
- [ ] Audio system initialization: <2 seconds complete startup
- [ ] Spatial audio processing: <5ms additional latency
- [ ] Asset loading: <2 seconds for critical audio assets
- [ ] Memory usage: <128MB for complete audio system
- [ ] CPU usage: <10% for all audio processing combined
- [ ] Cache hit rate: >80% for frequently accessed assets
- [ ] Three.js integration: <1ms per position update
- [ ] Quality switching: <500ms seamless transition

**PHASE 1 MUST BE 100% COMPLETE BEFORE PROCEEDING TO PHASE 2**

---

*This document serves as the definitive guide for Audio Phase 1 development in the Fighter Jet Cockpit project. All audio work must follow these processes and meet these standards to achieve the target immersive audio experience and Three.js compatibility.*
