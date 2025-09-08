# PHASE 6: ADVANCED AUDIO SYSTEMS & SPATIAL ACOUSTICS

## PRE-PHASE 6 VALIDATION:
```
CURSOR MUST VERIFY FROM PHASE 5:
✓ Custom shader library is fully functional
✓ Post-processing pipeline enhances visual quality
✓ Volumetric lighting creates cinematic atmosphere
✓ All shader effects integrate properly
✓ Performance benchmarks are met (>45 FPS)
✓ Temporal stability is maintained
✓ Memory usage is optimized
```

## Prompt 6.1: 3D Spatial Audio Implementation

**PREREQUISITE VALIDATION**:
```
CURSOR MUST VERIFY:
✓ Web Audio API is supported and functional
✓ Audio context can be created successfully
✓ Basic audio loading and playback works
✓ Performance monitoring shows acceptable baseline
✓ Memory management prevents audio-related leaks
```

**CURSOR RULES FOR THIS PROMPT**:
1. MUST create professional spatial audio system with realistic acoustics
2. ALL audio processing must be based on real acoustic physics
3. MUST support HRTF and binaural audio processing
4. Audio quality must be indistinguishable from professional audio systems

**DETAILED IMPLEMENTATION**:
```
Create a professional spatial audio system with realistic acoustics:

MANDATORY SPATIAL AUDIO COMPONENTS:

1. 3D AUDIO PROCESSING (COMPLETE IMPLEMENTATION):
   SpatialAudioSystem.js MUST implement:

   HRTF PROCESSING:
   - MUST implement Head-Related Transfer Function (HRTF) for spatial positioning
   - MUST create proper distance attenuation with realistic falloff curves
   - MUST build Doppler effect simulation for moving audio sources
   - MUST implement proper occlusion and obstruction modeling
   - MUST create realistic reverb zones with impulse response convolution
   - MUST build proper audio focus and directivity patterns

2. COCKPIT ACOUSTIC MODELING (COMPLETE IMPLEMENTATION):
   CockpitAcoustics.js MUST implement:

   ACOUSTIC PROPERTIES:
   - MUST calculate proper reverberation times for enclosed cockpit space
   - MUST implement material-based absorption coefficients for all surfaces
   - MUST create proper sound reflection patterns from curved surfaces
   - MUST build realistic sound transmission through materials
   - MUST implement proper acoustic coupling between adjacent spaces
   - MUST create frequency-dependent absorption and reflection characteristics

3. ENVIRONMENTAL AUDIO (COMPLETE IMPLEMENTATION):
   EnvironmentalAudio.js MUST implement:

   REALISTIC SOUNDSCAPES:
   - Wind noise generation with proper frequency spectrum
   - Engine sound simulation with realistic harmonics and modulation
   - Radio chatter with proper frequency response and static
   - Electrical system hum with proper harmonic content
   - Cooling fan noise with realistic blade-pass frequencies
   - Structural vibration transmission through solid materials

COMPLETE IMPLEMENTATION REQUIREMENTS:

SpatialAudioSystem.js MUST implement:
```javascript
class SpatialAudioSystem {
    constructor() {
        // COMPLETE audio context setup
        this.audioContext = this.createAudioContext();
        this.masterGain = this.audioContext.createGain();
        this.masterGain.connect(this.audioContext.destination);
        
        // COMPLETE spatial audio components
        this.hrtfProcessor = new HRTFProcessor(this.audioContext);
        this.reverbProcessor = new ReverbProcessor(this.audioContext);
        this.occlusionProcessor = new OcclusionProcessor(this.audioContext);
        this.dopplerProcessor = new DopplerProcessor(this.audioContext);
        
        // COMPLETE audio sources management
        this.audioSources = new Map();
        this.audioBuffers = new Map();
        this.audioLoaders = new AudioLoaderSystem();
        
        // COMPLETE listener properties
        this.listener = {
            position: new THREE.Vector3(0, 0, 0),
            orientation: {
                forward: new THREE.Vector3(0, 0, -1),
                up: new THREE.Vector3(0, 1, 0)
            },
            velocity: new THREE.Vector3(0, 0, 0)
        };
        
        // COMPLETE acoustic environment
        this.acousticEnvironment = new AcousticEnvironment();
        
        this.initializeSpatialAudio();
    }
    
    // MUST implement complete audio context creation
    createAudioContext() {
        const AudioContext = window.AudioContext || window.webkitAudioContext;
        
        if (!AudioContext) {
            throw new Error('Web Audio API not supported');
        }
        
        const context = new AudioContext({
            latencyHint: 'interactive',
            sampleRate: 48000
        });
        
        // COMPLETE context state management
        if (context.state === 'suspended') {
            // Will be resumed on first user interaction
            document.addEventListener('click', () => {
                if (context.state === 'suspended') {
                    context.resume();
                }
            }, { once: true });
        }
        
        return context;
    }
    
    // MUST implement complete 3D audio source creation
    create3DAudioSource(audioBuffer, position, options = {}) {
        const source = {
            // COMPLETE audio nodes
            bufferSource: this.audioContext.createBufferSource(),
            gainNode: this.audioContext.createGain(),
            pannerNode: this.audioContext.createPanner(),
            convolverNode: this.audioContext.createConvolver(),
            filterNode: this.audioContext.createBiquadFilter(),
            
            // COMPLETE spatial properties
            position: position.clone(),
            velocity: new THREE.Vector3(0, 0, 0),
            orientation: new THREE.Vector3(0, 0, -1),
            
            // COMPLETE audio properties
            volume: options.volume || 1.0,
            pitch: options.pitch || 1.0,
            loop: options.loop || false,
            autoplay: options.autoplay || false,
            
            // COMPLETE 3D audio properties
            rolloffFactor: options.rolloffFactor || 1.0,
            maxDistance: options.maxDistance || 1000.0,
            refDistance: options.refDistance || 1.0,
            coneInnerAngle: options.coneInnerAngle || 360,
            coneOuterAngle: options.coneOuterAngle || 360,
            coneOuterGain: options.coneOuterGain || 0.0,
            
            // COMPLETE state
            isPlaying: false,
            startTime: 0,
            pauseTime: 0
        };
        
        // COMPLETE audio buffer assignment
        source.bufferSource.buffer = audioBuffer;
        source.bufferSource.loop = source.loop;
        
        // COMPLETE panner configuration
        this.configurePannerNode(source.pannerNode, source);
        
        // COMPLETE audio graph connection
        this.connectAudioNodes(source);
        
        return source;
    }
    
    // MUST implement complete panner node configuration
    configurePannerNode(pannerNode, source) {
        // COMPLETE panning model
        pannerNode.panningModel = 'HRTF';
        pannerNode.distanceModel = 'inverse';
        
        // COMPLETE distance properties
        pannerNode.rolloffFactor = source.rolloffFactor;
        pannerNode.maxDistance = source.maxDistance;
        pannerNode.refDistance = source.refDistance;
        
        // COMPLETE cone properties
        pannerNode.coneInnerAngle = source.coneInnerAngle;
        pannerNode.coneOuterAngle = source.coneOuterAngle;
        pannerNode.coneOuterGain = source.coneOuterGain;
        
        // COMPLETE position and orientation
        this.updatePannerPosition(pannerNode, source.position);
        this.updatePannerOrientation(pannerNode, source.orientation);
    }
    
    // MUST implement complete audio node connection
    connectAudioNodes(source) {
        // COMPLETE audio processing chain
        source.bufferSource
            .connect(source.gainNode)
            .connect(source.filterNode)
            .connect(source.pannerNode)
            .connect(source.convolverNode)
            .connect(this.masterGain);
    }
    
    // MUST implement complete listener update
    updateListener(position, orientation, velocity) {
        this.listener.position.copy(position);
        this.listener.orientation.forward.copy(orientation.forward);
        this.listener.orientation.up.copy(orientation.up);
        this.listener.velocity.copy(velocity);
        
        // COMPLETE Web Audio API listener update
        const listener = this.audioContext.listener;
        
        if (listener.positionX) {
            // COMPLETE modern Web Audio API
            listener.positionX.setValueAtTime(position.x, this.audioContext.currentTime);
            listener.positionY.setValueAtTime(position.y, this.audioContext.currentTime);
            listener.positionZ.setValueAtTime(position.z, this.audioContext.currentTime);
            
            listener.forwardX.setValueAtTime(orientation.forward.x, this.audioContext.currentTime);
            listener.forwardY.setValueAtTime(orientation.forward.y, this.audioContext.currentTime);
            listener.forwardZ.setValueAtTime(orientation.forward.z, this.audioContext.currentTime);
            
            listener.upX.setValueAtTime(orientation.up.x, this.audioContext.currentTime);
            listener.upY.setValueAtTime(orientation.up.y, this.audioContext.currentTime);
            listener.upZ.setValueAtTime(orientation.up.z, this.audioContext.currentTime);
        } else {
            // COMPLETE legacy Web Audio API
            listener.setPosition(position.x, position.y, position.z);
            listener.setOrientation(
                orientation.forward.x, orientation.forward.y, orientation.forward.z,
                orientation.up.x, orientation.up.y, orientation.up.z
            );
        }
    }
    
    // MUST implement complete audio source update
    updateAudioSource(sourceId, position, velocity, orientation) {
        const source = this.audioSources.get(sourceId);
        if (!source) return;
        
        // COMPLETE position update
        source.position.copy(position);
        source.velocity.copy(velocity);
        source.orientation.copy(orientation);
        
        // COMPLETE panner update
        this.updatePannerPosition(source.pannerNode, position);
        this.updatePannerOrientation(source.pannerNode, orientation);
        
        // COMPLETE Doppler effect
        this.updateDopplerEffect(source, velocity);
        
        // COMPLETE occlusion and obstruction
        this.updateOcclusionObstruction(source);
    }
    
    // MUST implement complete Doppler effect
    updateDopplerEffect(source, velocity) {
        // COMPLETE Doppler shift calculation
        const speedOfSound = 343; // m/s at 20°C
        const listenerVelocity = this.listener.velocity;
        const sourceVelocity = velocity;
        
        // COMPLETE relative velocity calculation
        const sourceToListener = this.listener.position.clone().sub(source.position).normalize();
        const sourceVelComponent = sourceVelocity.dot(sourceToListener);
        const listenerVelComponent = listenerVelocity.dot(sourceToListener);
        
        // COMPLETE Doppler formula: f' = f * (v + vr) / (v + vs)
        const dopplerFactor = (speedOfSound + listenerVelComponent) / (speedOfSound + sourceVelComponent);
        
        // COMPLETE pitch adjustment
        source.bufferSource.playbackRate.setValueAtTime(
            source.pitch * dopplerFactor,
            this.audioContext.currentTime
        );
    }
}

class HRTFProcessor {
    constructor(audioContext) {
        this.audioContext = audioContext;
        
        // COMPLETE HRTF database
        this.hrtfDatabase = new HRTFDatabase();
        this.currentHRTF = null;
        
        // COMPLETE processing nodes
        this.convolverLeft = audioContext.createConvolver();
        this.convolverRight = audioContext.createConvolver();
        this.splitter = audioContext.createChannelSplitter(2);
        this.merger = audioContext.createChannelMerger(2);
        
        this.initializeHRTF();
    }
    
    // MUST implement complete HRTF processing
    processHRTF(source, listenerPosition, listenerOrientation) {
        // COMPLETE spatial calculation
        const relativePosition = source.position.clone().sub(listenerPosition);
        const distance = relativePosition.length();
        
        // COMPLETE spherical coordinates
        const azimuth = Math.atan2(relativePosition.x, relativePosition.z);
        const elevation = Math.asin(relativePosition.y / distance);
        
        // COMPLETE HRTF lookup
        const hrtfData = this.hrtfDatabase.getHRTF(azimuth, elevation);
        
        if (hrtfData && hrtfData !== this.currentHRTF) {
            // COMPLETE HRTF impulse response update
            this.updateHRTFImpulseResponse(hrtfData);
            this.currentHRTF = hrtfData;
        }
    }
    
    // MUST implement complete HRTF impulse response update
    updateHRTFImpulseResponse(hrtfData) {
        // COMPLETE left ear impulse response
        const leftBuffer = this.audioContext.createBuffer(1, hrtfData.left.length, this.audioContext.sampleRate);
        leftBuffer.copyToChannel(hrtfData.left, 0);
        this.convolverLeft.buffer = leftBuffer;
        
        // COMPLETE right ear impulse response
        const rightBuffer = this.audioContext.createBuffer(1, hrtfData.right.length, this.audioContext.sampleRate);
        rightBuffer.copyToChannel(hrtfData.right, 0);
        this.convolverRight.buffer = rightBuffer;
    }
}

class CockpitAcoustics {
    constructor(audioContext) {
        this.audioContext = audioContext;
        
        // COMPLETE acoustic properties
        this.acousticProperties = {
            // COMPLETE material absorption coefficients (frequency dependent)
            materials: {
                aluminum: {
                    125: 0.05, 250: 0.05, 500: 0.06, 1000: 0.07, 2000: 0.09, 4000: 0.10
                },
                plastic: {
                    125: 0.08, 250: 0.10, 500: 0.12, 1000: 0.14, 2000: 0.16, 4000: 0.18
                },
                glass: {
                    125: 0.18, 250: 0.06, 500: 0.04, 1000: 0.03, 2000: 0.02, 4000: 0.02
                },
                fabric: {
                    125: 0.25, 250: 0.35, 500: 0.45, 1000: 0.55, 2000: 0.60, 4000: 0.65
                }
            },
            
            // COMPLETE cockpit dimensions
            volume: 2.5, // cubic meters
            surfaceArea: 15.0, // square meters
            averageAbsorption: 0.15
        };
        
        // COMPLETE reverb calculation
        this.reverbTime = this.calculateReverbTime();
        this.impulseResponse = this.generateImpulseResponse();
        
        this.initializeCockpitAcoustics();
    }
    
    // MUST implement complete reverberation time calculation
    calculateReverbTime() {
        // COMPLETE Sabine's formula: RT60 = 0.161 * V / A
        // where V = volume, A = total absorption
        
        const frequencies = [125, 250, 500, 1000, 2000, 4000];
        const reverbTimes = {};
        
        for (const freq of frequencies) {
            let totalAbsorption = 0;
            
            // COMPLETE material contribution calculation
            for (const [material, areas] of Object.entries(this.getMaterialAreas())) {
                const absorptionCoeff = this.acousticProperties.materials[material][freq];
                totalAbsorption += areas * absorptionCoeff;
            }
            
            // COMPLETE RT60 calculation
            reverbTimes[freq] = (0.161 * this.acousticProperties.volume) / totalAbsorption;
        }
        
        return reverbTimes;
    }
    
    // MUST implement complete impulse response generation
    generateImpulseResponse() {
        const sampleRate = this.audioContext.sampleRate;
        const duration = Math.max(...Object.values(this.reverbTime)); // seconds
        const length = Math.floor(duration * sampleRate);
        
        // COMPLETE impulse response buffer
        const impulseBuffer = this.audioContext.createBuffer(2, length, sampleRate);
        
        // COMPLETE left and right channels
        const leftChannel = impulseBuffer.getChannelData(0);
        const rightChannel = impulseBuffer.getChannelData(1);
        
        // COMPLETE early reflections and late reverberation
        this.generateEarlyReflections(leftChannel, rightChannel, sampleRate);
        this.generateLateReverberation(leftChannel, rightChannel, sampleRate);
        
        return impulseBuffer;
    }
    
    // MUST implement complete early reflections
    generateEarlyReflections(leftChannel, rightChannel, sampleRate) {
        // COMPLETE cockpit reflection points
        const reflections = [
            { delay: 0.003, gain: 0.8, pan: -0.3 }, // Left wall
            { delay: 0.004, gain: 0.7, pan: 0.3 },  // Right wall
            { delay: 0.006, gain: 0.6, pan: 0.0 },  // Ceiling
            { delay: 0.008, gain: 0.5, pan: 0.0 },  // Floor
            { delay: 0.012, gain: 0.4, pan: -0.1 }, // Instrument panel
            { delay: 0.015, gain: 0.3, pan: 0.1 }   // Canopy
        ];
        
        for (const reflection of reflections) {
            const delaySamples = Math.floor(reflection.delay * sampleRate);
            const leftGain = reflection.gain * (1 - Math.max(0, reflection.pan));
            const rightGain = reflection.gain * (1 + Math.min(0, reflection.pan));
            
            if (delaySamples < leftChannel.length) {
                leftChannel[delaySamples] += leftGain;
                rightChannel[delaySamples] += rightGain;
            }
        }
    }
    
    // MUST implement complete late reverberation
    generateLateReverberation(leftChannel, rightChannel, sampleRate) {
        // COMPLETE exponential decay based on RT60
        const rt60 = this.reverbTime[1000]; // Use 1kHz RT60 as reference
        const decayConstant = -6.91 / rt60; // -60dB decay
        
        // COMPLETE noise-based reverberation tail
        for (let i = Math.floor(0.05 * sampleRate); i < leftChannel.length; i++) {
            const time = i / sampleRate;
            const amplitude = Math.exp(decayConstant * time);
            
            // COMPLETE random noise with exponential decay
            const noise = (Math.random() * 2 - 1) * amplitude * 0.1;
            
            leftChannel[i] += noise * (0.5 + Math.random() * 0.5);
            rightChannel[i] += noise * (0.5 + Math.random() * 0.5);
        }
    }
}

class EnvironmentalAudio {
    constructor(audioContext) {
        this.audioContext = audioContext;
        
        // COMPLETE environmental sound sources
        this.environmentalSources = {
            wind: null,
            engine: null,
            electrical: null,
            cooling: null,
            radio: null,
            structural: null
        };
        
        // COMPLETE audio generators
        this.windGenerator = new WindNoiseGenerator(audioContext);
        this.engineGenerator = new EngineNoiseGenerator(audioContext);
        this.electricalGenerator = new ElectricalNoiseGenerator(audioContext);
        
        this.initializeEnvironmentalAudio();
    }
    
    // MUST implement complete wind noise generation
    generateWindNoise(airspeed, altitude) {
        const windSource = this.environmentalSources.wind;
        if (!windSource) return;
        
        // COMPLETE wind noise frequency spectrum
        const baseFrequency = 20 + (airspeed * 0.5); // Hz
        const intensity = Math.min(airspeed / 200, 1.0); // Normalize to 0-1
        
        // COMPLETE altitude effects
        const altitudeFactor = Math.exp(-altitude / 10000); // Exponential falloff
        const finalIntensity = intensity * altitudeFactor;
        
        // COMPLETE wind noise parameters
        windSource.gainNode.gain.setValueAtTime(
            finalIntensity * 0.3,
            this.audioContext.currentTime
        );
        
        windSource.filterNode.frequency.setValueAtTime(
            baseFrequency,
            this.audioContext.currentTime
        );
    }
    
    // MUST implement complete engine noise generation
    generateEngineNoise(rpm, throttle, engineTemp) {
        const engineSource = this.environmentalSources.engine;
        if (!engineSource) return;
        
        // COMPLETE engine harmonics
        const fundamentalFreq = (rpm / 60) * 2; // 2-blade propeller
        const harmonics = [1, 2, 3, 4, 6, 8]; // Harmonic series
        
        // COMPLETE throttle effects
        const throttleGain = 0.2 + (throttle * 0.8);
        
        // COMPLETE temperature effects
        const tempFactor = Math.max(0.5, Math.min(1.5, engineTemp / 200));
        
        // COMPLETE engine noise synthesis
        for (let i = 0; i < harmonics.length; i++) {
            const harmonic = harmonics[i];
            const frequency = fundamentalFreq * harmonic;
            const amplitude = throttleGain * tempFactor / (harmonic * harmonic);
            
            // Apply harmonic to engine oscillator
            this.updateEngineHarmonic(i, frequency, amplitude);
        }
    }
}

class InteractiveAudio {
    constructor(audioContext, spatialAudioSystem) {
        this.audioContext = audioContext;
        this.spatialAudio = spatialAudioSystem;
        
        // COMPLETE control interface audio
        this.controlSounds = new Map();
        this.loadControlSounds();
        
        // COMPLETE communication audio
        this.radioSystem = new RadioAudioSystem(audioContext);
        this.intercomSystem = new IntercomAudioSystem(audioContext);
        
        this.initializeInteractiveAudio();
    }
    
    // MUST implement complete control interface audio
    playControlSound(controlType, action, position) {
        const soundKey = `${controlType}_${action}`;
        const audioBuffer = this.controlSounds.get(soundKey);
        
        if (audioBuffer) {
            // COMPLETE 3D positioned control sound
            const source = this.spatialAudio.create3DAudioSource(audioBuffer, position, {
                volume: 0.8,
                maxDistance: 2.0,
                rolloffFactor: 2.0
            });
            
            // COMPLETE control-specific audio processing
            this.applyControlAudioProcessing(source, controlType, action);
            
            source.bufferSource.start();
        }
    }
    
    // MUST implement complete radio audio system
    processRadioAudio(audioData, frequency, signalStrength) {
        // COMPLETE radio frequency response
        const radioFilter = this.audioContext.createBiquadFilter();
        radioFilter.type = 'bandpass';
        radioFilter.frequency.value = 2000; // Typical radio bandwidth
        radioFilter.Q.value = 2.0;
        
        // COMPLETE static generation based on signal strength
        const staticLevel = Math.max(0, 1 - signalStrength);
        const staticGain = this.audioContext.createGain();
        staticGain.gain.value = staticLevel * 0.3;
        
        // COMPLETE radio processing chain
        const radioChain = this.createRadioProcessingChain(radioFilter, staticGain);
        
        return radioChain;
    }
}
```

VALIDATION REQUIREMENTS:
CURSOR MUST verify after implementation:
✓ 3D spatial audio positioning works correctly
✓ HRTF processing provides realistic spatial cues
✓ Cockpit acoustics model realistic reverberation
✓ Environmental audio enhances immersion
✓ Interactive audio provides proper feedback
✓ Performance remains above 45 FPS
✓ Audio latency is minimized
✓ Cross-platform audio compatibility

PERFORMANCE BENCHMARKS (MUST ACHIEVE):
✓ Audio processing latency: <20ms
✓ 3D audio update rate: 60 updates per second
✓ Memory usage for audio: <64MB
✓ CPU usage for audio: <10% of total
✓ Audio source limit: >32 simultaneous sources
✓ Reverb processing: <5ms additional latency
```

**GAP IDENTIFICATION FOR PHASE 6.1**:
```
CURSOR MUST CHECK FOR THESE CRITICAL GAPS:
❌ Poor spatial audio positioning reducing immersion
❌ Missing HRTF processing limiting 3D audio quality
❌ Inadequate cockpit acoustic modeling
❌ Poor environmental audio integration
❌ High audio latency disrupting experience
❌ Missing Doppler effect implementation
❌ Inadequate occlusion and obstruction modeling
❌ Poor cross-platform audio compatibility
❌ Missing frequency-dependent acoustic properties
❌ Inadequate reverb quality
```

## Prompt 6.2: Interactive Audio Systems

**PREREQUISITE VALIDATION**:
```
CURSOR MUST VERIFY FROM PHASE 6.1:
✓ 3D spatial audio system is fully functional
✓ HRTF processing provides realistic spatial cues
✓ Cockpit acoustics model works correctly
✓ Environmental audio enhances immersion
✓ Performance benchmarks are met
✓ Audio latency is acceptable (<20ms)
```

**CURSOR RULES FOR THIS PROMPT**:
1. MUST build sophisticated interactive audio systems
2. ALL audio interactions must provide realistic feedback
3. MUST support professional communication systems simulation
4. Interactive audio quality must match real aircraft systems

**DETAILED IMPLEMENTATION**:
```
Build sophisticated interactive audio systems:

MANDATORY INTERACTIVE AUDIO COMPONENTS:

1. CONTROL INTERFACE AUDIO (COMPLETE IMPLEMENTATION):
   ControlInterfaceAudio.js MUST implement:

   MECHANICAL CONTROL SOUNDS:
   - Individual switch actuation sounds with proper mechanical characteristics
   - Rotary control audio with detent clicking and smooth rotation
   - Button press feedback with proper tactile response timing
   - Relay clicking and electromagnetic switching sounds
   - Display system audio with proper electronic characteristics
   - Warning system audio with proper urgency and attention-getting characteristics

2. COMMUNICATION SYSTEMS (COMPLETE IMPLEMENTATION):
   CommunicationAudio.js MUST implement:

   RADIO SYSTEMS:
   - Radio static generation with proper white/pink noise characteristics
   - Frequency tuning effects with realistic signal strength variation
   - Squelch control with proper noise gate behavior
   - Air traffic control simulation with realistic communication protocols
   - Intercom systems with proper electronic filtering
   - Emergency communication systems with priority override

3. SYSTEM STATUS AUDIO (COMPLETE IMPLEMENTATION):
   SystemStatusAudio.js MUST implement:

   WARNING AND ALERT SYSTEMS:
   - Master caution and warning audio with proper alert characteristics
   - System-specific warning tones with appropriate urgency levels
   - Positive confirmation tones for successful system operations
   - Negative feedback tones for system failures or invalid inputs
   - Background system monitoring with subtle audio cues
   - Audio checklists with proper pacing and confirmation requirements

COMPLETE IMPLEMENTATION REQUIREMENTS:

ControlInterfaceAudio.js MUST implement:
```javascript
class ControlInterfaceAudio {
    constructor(audioContext, spatialAudioSystem) {
        this.audioContext = audioContext;
        this.spatialAudio = spatialAudioSystem;
        
        // COMPLETE control sound library
        this.controlSounds = new Map();
        this.controlAudioProcessors = new Map();
        
        // COMPLETE mechanical audio simulation
        this.mechanicalSimulator = new MechanicalAudioSimulator(audioContext);
        this.tactileFeedbackGenerator = new TactileFeedbackGenerator(audioContext);
        
        // COMPLETE control types
        this.controlTypes = {
            toggle_switch: new ToggleSwitchAudio(),
            rotary_switch: new RotarySwitchAudio(),
            push_button: new PushButtonAudio(),
            slider: new SliderAudio(),
            key_switch: new KeySwitchAudio(),
            circuit_breaker: new CircuitBreakerAudio()
        };
        
        this.initializeControlInterfaceAudio();
    }
    
    // MUST implement complete control interaction audio
    playControlInteraction(controlType, action, position, parameters = {}) {
        const controlAudio = this.controlTypes[controlType];
        if (!controlAudio) return;
        
        // COMPLETE control-specific audio generation
        const audioBuffer = controlAudio.generateSound(action, parameters);
        
        if (audioBuffer) {
            // COMPLETE 3D positioned audio
            const source = this.spatialAudio.create3DAudioSource(audioBuffer, position, {
                volume: parameters.volume || 0.8,
                maxDistance: 2.0,
                rolloffFactor: 2.0,
                refDistance: 0.1
            });
            
            // COMPLETE mechanical audio processing
            this.applyMechanicalProcessing(source, controlType, action, parameters);
            
            // COMPLETE tactile feedback simulation
            this.generateTactileFeedback(controlType, action, parameters);
            
            source.bufferSource.start();
            
            return source;
        }
    }
    
    // MUST implement complete mechanical processing
    applyMechanicalProcessing(source, controlType, action, parameters) {
        switch (controlType) {
            case 'toggle_switch':
                this.applyToggleSwitchProcessing(source, action, parameters);
                break;
            case 'rotary_switch':
                this.applyRotarySwitchProcessing(source, action, parameters);
                break;
            case 'push_button':
                this.applyPushButtonProcessing(source, action, parameters);
                break;
            // COMPLETE processing for all control types
        }
    }
    
    // MUST implement complete toggle switch processing
    applyToggleSwitchProcessing(source, action, parameters) {
        // COMPLETE switch mechanism simulation
        const mechanicalFilter = this.audioContext.createBiquadFilter();
        mechanicalFilter.type = 'bandpass';
        mechanicalFilter.frequency.value = 2000 + (Math.random() * 500); // Mechanical resonance
        mechanicalFilter.Q.value = 5.0;
        
        // COMPLETE spring tension simulation
        const springTension = parameters.springTension || 0.5;
        const compressionGain = this.audioContext.createGain();
        compressionGain.gain.value = 0.8 + (springTension * 0.4);
        
        // COMPLETE contact bounce simulation
        if (action === 'activate' || action === 'deactivate') {
            const bounceDelay = this.audioContext.createDelay(0.1);
            bounceDelay.delayTime.value = 0.002 + (Math.random() * 0.003); // 2-5ms bounce
            
            // COMPLETE processing chain
            source.filterNode.disconnect();
            source.filterNode
                .connect(mechanicalFilter)
                .connect(compressionGain)
                .connect(bounceDelay)
                .connect(source.pannerNode);
        }
    }
    
    // MUST implement complete rotary switch processing
    applyRotarySwitchProcessing(source, action, parameters) {
        if (action === 'rotate') {
            // COMPLETE detent mechanism
            const detentCount = parameters.detentCount || 8;
            const rotationAngle = parameters.rotationAngle || 0;
            const detentAngle = 360 / detentCount;
            
            // COMPLETE detent click generation
            const nearDetent = (rotationAngle % detentAngle) < (detentAngle * 0.1);
            
            if (nearDetent) {
                // COMPLETE detent click audio
                const detentClick = this.generateDetentClick(parameters);
                this.playDetentClick(detentClick, source.position);
            }
            
            // COMPLETE rotation friction
            const frictionFilter = this.audioContext.createBiquadFilter();
            frictionFilter.type = 'lowpass';
            frictionFilter.frequency.value = 1000 - (parameters.friction || 0.5) * 300;
            
            source.filterNode.disconnect();
            source.filterNode.connect(frictionFilter).connect(source.pannerNode);
        }
    }
}

class CommunicationAudio {
    constructor(audioContext) {
        this.audioContext = audioContext;
        
        // COMPLETE radio systems
        this.radioSystems = new Map();
        this.intercomSystem = new IntercomSystem(audioContext);
        this.emergencySystem = new EmergencyCommSystem(audioContext);
        
        // COMPLETE communication processors
        this.radioProcessor = new RadioProcessor(audioContext);
        this.staticGenerator = new StaticGenerator(audioContext);
        this.squelchProcessor = new SquelchProcessor(audioContext);
        
        // COMPLETE frequency bands
        this.frequencyBands = {
            vhf: { min: 118.0, max: 137.0 }, // MHz
            uhf: { min: 225.0, max: 400.0 }, // MHz
            hf: { min: 2.0, max: 30.0 }      // MHz
        };
        
        this.initializeCommunicationAudio();
    }
    
    // MUST implement complete radio system
    createRadioSystem(radioId, band, frequency) {
        const radio = {
            id: radioId,
            band: band,
            frequency: frequency,
            volume: 0.8,
            squelch: 0.3,
            signalStrength: 0.0,
            
            // COMPLETE audio processing nodes
            inputGain: this.audioContext.createGain(),
            outputGain: this.audioContext.createGain(),
            bandpassFilter: this.audioContext.createBiquadFilter(),
            staticMixer: this.audioContext.createGain(),
            squelchGate: this.audioContext.createGain(),
            
            // COMPLETE radio state
            isTransmitting: false,
            isReceiving: false,
            lastActivity: 0
        };
        
        // COMPLETE radio filter configuration
        this.configureRadioFilter(radio);
        
        // COMPLETE audio routing
        this.connectRadioAudio(radio);
        
        this.radioSystems.set(radioId, radio);
        
        return radio;
    }
    
    // MUST implement complete radio filter configuration
    configureRadioFilter(radio) {
        // COMPLETE frequency-dependent filtering
        const bandConfig = this.frequencyBands[radio.band];
        
        radio.bandpassFilter.type = 'bandpass';
        radio.bandpassFilter.frequency.value = 2500; // Typical radio bandwidth center
        radio.bandpassFilter.Q.value = 2.0;
        
        // COMPLETE band-specific characteristics
        switch (radio.band) {
            case 'vhf':
                radio.bandpassFilter.frequency.value = 2800;
                radio.bandpassFilter.Q.value = 1.8;
                break;
            case 'uhf':
                radio.bandpassFilter.frequency.value = 3000;
                radio.bandpassFilter.Q.value = 2.2;
                break;
            case 'hf':
                radio.bandpassFilter.frequency.value = 2200;
                radio.bandpassFilter.Q.value = 1.5;
                break;
        }
    }
    
    // MUST implement complete radio transmission
    transmitRadio(radioId, audioData, duration) {
        const radio = this.radioSystems.get(radioId);
        if (!radio) return;
        
        // COMPLETE transmission state
        radio.isTransmitting = true;
        radio.lastActivity = this.audioContext.currentTime;
        
        // COMPLETE transmission processing
        const transmissionProcessor = this.createTransmissionProcessor(radio);
        
        // COMPLETE audio routing for transmission
        audioData
            .connect(transmissionProcessor.preEmphasis)
            .connect(transmissionProcessor.compressor)
            .connect(transmissionProcessor.limiter)
            .connect(radio.bandpassFilter)
            .connect(radio.outputGain);
        
        // COMPLETE transmission timeout
        setTimeout(() => {
            radio.isTransmitting = false;
            this.disconnectTransmission(radio);
        }, duration * 1000);
    }
    
    // MUST implement complete radio reception
    receiveRadio(radioId, signalStrength, audioData) {
        const radio = this.radioSystems.get(radioId);
        if (!radio) return;
        
        // COMPLETE signal strength processing
        radio.signalStrength = signalStrength;
        
        // COMPLETE static generation
        const staticLevel = this.calculateStaticLevel(signalStrength, radio.squelch);
        this.updateRadioStatic(radio, staticLevel);
        
        // COMPLETE squelch processing
        const squelchOpen = signalStrength > radio.squelch;
        radio.squelchGate.gain.setValueAtTime(
            squelchOpen ? 1.0 : 0.0,
            this.audioContext.currentTime
        );
        
        if (squelchOpen && audioData) {
            // COMPLETE reception processing
            radio.isReceiving = true;
            radio.lastActivity = this.audioContext.currentTime;
            
            audioData
                .connect(radio.bandpassFilter)
                .connect(radio.squelchGate)
                .connect(radio.outputGain);
        }
    }
    
    // MUST implement complete static generation
    calculateStaticLevel(signalStrength, squelchThreshold) {
        // COMPLETE static calculation
        if (signalStrength >= squelchThreshold) {
            // COMPLETE signal present - minimal static
            return Math.max(0, (squelchThreshold - signalStrength) * 0.1);
        } else {
            // COMPLETE no signal - full static
            return Math.min(1.0, (squelchThreshold - signalStrength) * 2.0);
        }
    }
    
    // MUST implement complete intercom system
    processIntercom(audioData, channel, priority) {
        const intercom = this.intercomSystem;
        
        // COMPLETE channel routing
        const channelProcessor = intercom.getChannelProcessor(channel);
        
        // COMPLETE priority handling
        if (priority > intercom.currentPriority) {
            // COMPLETE priority override
            intercom.currentPriority = priority;
            intercom.activeChannel = channel;
            
            // COMPLETE ducking of lower priority audio
            this.duckLowerPriorityAudio(priority);
        }
        
        // COMPLETE intercom processing
        audioData
            .connect(channelProcessor.inputGain)
            .connect(channelProcessor.compressor)
            .connect(channelProcessor.equalizer)
            .connect(intercom.masterOutput);
        
        return channelProcessor;
    }
}

class SystemStatusAudio {
    constructor(audioContext) {
        this.audioContext = audioContext;
        
        // COMPLETE warning system
        this.warningSystem = new WarningAudioSystem(audioContext);
        this.cautionSystem = new CautionAudioSystem(audioContext);
        this.advisorySystem = new AdvisoryAudioSystem(audioContext);
        
        // COMPLETE system tones
        this.systemTones = new Map();
        this.generateSystemTones();
        
        // COMPLETE audio priorities
        this.audioPriorities = {
            emergency: 10,
            warning: 8,
            caution: 6,
            advisory: 4,
            confirmation: 2,
            background: 1
        };
        
        this.initializeSystemStatusAudio();
    }
    
    // MUST implement complete warning audio
    playWarningAudio(warningType, urgency, parameters = {}) {
        const priority = this.audioPriorities[urgency] || 5;
        
        // COMPLETE warning tone generation
        const warningTone = this.generateWarningTone(warningType, urgency, parameters);
        
        // COMPLETE spatial positioning
        const position = parameters.position || new THREE.Vector3(0, 0, 0);
        
        // COMPLETE warning audio source
        const warningSource = this.spatialAudio.create3DAudioSource(warningTone, position, {
            volume: this.calculateWarningVolume(urgency),
            loop: parameters.continuous || false,
            priority: priority
        });
        
        // COMPLETE urgency-based processing
        this.applyUrgencyProcessing(warningSource, urgency);
        
        // COMPLETE attention-getting characteristics
        this.applyAttentionCharacteristics(warningSource, warningType, urgency);
        
        warningSource.bufferSource.start();
        
        return warningSource;
    }
    
    // MUST implement complete warning tone generation
    generateWarningTone(warningType, urgency, parameters) {
        const duration = parameters.duration || 2.0; // seconds
        const sampleRate = this.audioContext.sampleRate;
        const length = duration * sampleRate;
        
        // COMPLETE warning tone buffer
        const buffer = this.audioContext.createBuffer(1, length, sampleRate);
        const data = buffer.getChannelData(0);
        
        // COMPLETE tone characteristics based on warning type
        let frequency, modulation, envelope;
        
        switch (warningType) {
            case 'master_warning':
                frequency = 1000; // Hz
                modulation = { type: 'warble', rate: 4.0, depth: 0.3 };
                envelope = { attack: 0.1, decay: 0.2, sustain: 0.8, release: 0.5 };
                break;
                
            case 'fire_warning':
                frequency = 800; // Hz
                modulation = { type: 'pulse', rate: 2.0, depth: 1.0 };
                envelope = { attack: 0.05, decay: 0.1, sustain: 0.9, release: 0.3 };
                break;
                
            case 'altitude_warning':
                frequency = 1200; // Hz
                modulation = { type: 'sweep', rate: 1.0, depth: 0.5 };
                envelope = { attack: 0.2, decay: 0.3, sustain: 0.7, release: 0.8 };
                break;
                
            // COMPLETE warning types
        }
        
        // COMPLETE tone synthesis
        for (let i = 0; i < length; i++) {
            const time = i / sampleRate;
            
            // COMPLETE base frequency
            let currentFreq = frequency;
            
            // COMPLETE modulation application
            switch (modulation.type) {
                case 'warble':
                    currentFreq *= 1 + modulation.depth * Math.sin(2 * Math.PI * modulation.rate * time);
                    break;
                case 'pulse':
                    currentFreq *= Math.sin(2 * Math.PI * modulation.rate * time) > 0 ? 1 : 0;
                    break;
                case 'sweep':
                    currentFreq *= 1 + modulation.depth * Math.sin(2 * Math.PI * modulation.rate * time * time);
                    break;
            }
            
            // COMPLETE envelope application
            const envelopeGain = this.calculateEnvelopeGain(time, duration, envelope);
            
            // COMPLETE harmonic content for urgency
            const harmonicContent = this.calculateHarmonicContent(urgency);
            
            // COMPLETE waveform generation
            let sample = 0;
            for (let harmonic = 1; harmonic <= harmonicContent.harmonics; harmonic++) {
                const harmonicGain = harmonicContent.gains[harmonic - 1] || 0;
                sample += harmonicGain * Math.sin(2 * Math.PI * currentFreq * harmonic * time);
            }
            
            data[i] = sample * envelopeGain;
        }
        
        return buffer;
    }
    
    // MUST implement complete confirmation audio
    playConfirmationAudio(actionType, success, position) {
        const confirmationType = success ? 'positive' : 'negative';
        
        // COMPLETE confirmation tone selection
        const toneBuffer = this.systemTones.get(`${actionType}_${confirmationType}`);
        
        if (toneBuffer) {
            const confirmationSource = this.spatialAudio.create3DAudioSource(toneBuffer, position, {
                volume: 0.6,
                maxDistance: 1.5,
                rolloffFactor: 1.5
            });
            
            confirmationSource.bufferSource.start();
        }
    }
    
    // MUST implement complete system monitoring audio
    updateSystemMonitoringAudio(systemStates) {
        // COMPLETE background system audio
        for (const [systemId, state] of Object.entries(systemStates)) {
            this.updateSystemAudio(systemId, state);
        }
    }
    
    // MUST implement complete system audio update
    updateSystemAudio(systemId, state) {
        const systemAudio = this.systemAudioSources.get(systemId);
        
        if (systemAudio) {
            // COMPLETE state-based audio modification
            switch (state.status) {
                case 'normal':
                    systemAudio.gainNode.gain.setValueAtTime(0.1, this.audioContext.currentTime);
                    break;
                case 'caution':
                    systemAudio.gainNode.gain.setValueAtTime(0.3, this.audioContext.currentTime);
                    break;
                case 'warning':
                    systemAudio.gainNode.gain.setValueAtTime(0.6, this.audioContext.currentTime);
                    break;
                case 'failed':
                    systemAudio.gainNode.gain.setValueAtTime(0.0, this.audioContext.currentTime);
                    break;
            }
            
            // COMPLETE frequency modulation based on system health
            const healthFactor = state.health || 1.0;
            const baseFrequency = systemAudio.baseFrequency || 60; // Hz
            const modulatedFrequency = baseFrequency * (0.8 + 0.4 * healthFactor);
            
            if (systemAudio.oscillator) {
                systemAudio.oscillator.frequency.setValueAtTime(
                    modulatedFrequency,
                    this.audioContext.currentTime
                );
            }
        }
    }
}
```

VALIDATION REQUIREMENTS:
CURSOR MUST verify after implementation:
✓ Control interface audio provides realistic feedback
✓ Communication systems simulate real radio behavior
✓ Warning and alert systems are attention-getting
✓ Interactive audio responds correctly to user actions
✓ Audio priorities work correctly
✓ System status audio provides useful feedback
✓ Performance remains above 45 FPS
✓ Audio latency is minimized

PERFORMANCE BENCHMARKS (MUST ACHIEVE):
✓ Interactive audio latency: <10ms
✓ Radio processing latency: <15ms
✓ Warning system response: <5ms
✓ Simultaneous interactive sources: >16
✓ CPU usage for interactive audio: <5%
✓ Memory usage: <32MB additional
```

**GAP IDENTIFICATION FOR PHASE 6.2**:
```
CURSOR MUST CHECK FOR THESE CRITICAL GAPS:
❌ Poor control interface audio reducing tactile feedback
❌ Unrealistic radio communication simulation
❌ Inadequate warning system attention-getting characteristics
❌ Missing confirmation audio for user actions
❌ Poor audio priority management
❌ High interactive audio latency
❌ Missing system status audio feedback
❌ Inadequate emergency communication systems
❌ Poor squelch and static simulation
❌ Missing intercom system functionality
```

## PHASE 6 COMPLETION CHECKLIST

### ✅ **VALIDATION REQUIREMENTS**
- [ ] 3D spatial audio positioning works correctly
- [ ] HRTF processing provides realistic spatial cues
- [ ] Cockpit acoustics model realistic reverberation
- [ ] Environmental audio enhances immersion
- [ ] Interactive audio provides proper feedback
- [ ] Communication systems simulate real behavior
- [ ] Warning systems are attention-getting
- [ ] Performance remains above 45 FPS

### ✅ **QUALITY GATES**
- [ ] Audio quality matches professional systems
- [ ] Spatial positioning is accurate and convincing
- [ ] Interactive feedback is immediate and realistic
- [ ] Communication clarity is maintained
- [ ] Warning urgency is properly conveyed
- [ ] Cross-platform compatibility is ensured
- [ ] Audio latency is minimized

### ✅ **PERFORMANCE BENCHMARKS**
- [ ] Audio processing latency: <20ms
- [ ] Interactive audio latency: <10ms
- [ ] 3D audio update rate: 60 updates per second
- [ ] Memory usage for audio: <96MB total
- [ ] CPU usage for audio: <15% of total
- [ ] Simultaneous audio sources: >48 total

**PHASE 6 MUST BE 100% COMPLETE BEFORE PROCEEDING TO PHASE 7**
