# AUDIO PHASE 2: SYSTEM AUDIO AND INTERACTIVE FEEDBACK

## PROJECT RULES & CONSTRAINTS

### MANDATORY DEVELOPMENT RULES FOR AUDIO PHASE 2:

1. **SYSTEM AUDIO COMPLETENESS**: 
   - Implement COMPLETE audio systems for all cockpit components
   - NEVER use placeholder sounds or generic audio clips
   - All system audio must match real military aviation specifications
   - All interactive feedback must provide immediate tactile correlation

2. **INTERACTIVE FEEDBACK PRECISION**: 
   - Every control interaction MUST have unique audio signature
   - Audio feedback timing MUST be <5ms from user input
   - All control sounds MUST match physical switch characteristics
   - Feedback audio MUST scale appropriately with interaction force/speed

3. **MILITARY SPECIFICATION COMPLIANCE**: 
   - All warning and alert sounds MUST comply with military audio standards
   - Audio frequency ranges MUST be optimized for pilot recognition
   - Alert priority system MUST follow established military protocols
   - All system sounds MUST be authentic to fighter jet operations

4. **REAL-TIME RESPONSIVENESS**: 
   - System state changes MUST trigger immediate audio feedback
   - Audio processing MUST maintain <10ms total system latency
   - All audio systems MUST update at 60 FPS minimum
   - Performance MUST remain stable under full system load

## PRE-PHASE 2 VALIDATION:
**CURSOR MUST CHECK:**
```
✓ Phase 1 audio foundation is complete and functional
✓ Spatial audio engine provides accurate 3D positioning
✓ Audio asset management system is working properly
✓ Performance monitoring maintains all benchmarks
✓ Web Audio API context is stable and optimized
✓ Three.js integration is seamless and responsive
```

## Prompt 2.1: Complete Cockpit System Audio Implementation

**PREREQUISITE VALIDATION**:
```
CURSOR MUST VERIFY FROM PHASE 1:
✓ Web Audio API foundation with spatial processing complete
✓ Advanced audio processing pipeline functional
✓ Audio asset management system operational
✓ Performance benchmarks consistently met
✓ Three.js integration working correctly
✓ Memory management within specified limits
```

**CURSOR RULES FOR THIS PROMPT**:
1. Create COMPLETE system audio for all cockpit components
2. Implement FULL interactive feedback system with tactile correlation
3. NO generic sounds - everything must be component-specific
4. Must support real-time system state synchronization

**DETAILED IMPLEMENTATION**:
```
Create comprehensive cockpit system audio with complete interactive feedback:

COCKPIT SYSTEM AUDIO ARCHITECTURE (create ALL components):
├── Flight Control Systems/
│   ├── Primary_Flight_Controls (COMPLETE stick and rudder audio)
│   ├── Secondary_Flight_Controls (FULL trim and flap systems)
│   ├── Autopilot_Systems (COMPLETE engagement and mode changes)
│   └── Flight_Management_Computer (FULL FMC interaction audio)
├── Engine Management Systems/
│   ├── Throttle_Controls (COMPLETE dual throttle system audio)
│   ├── Engine_Monitoring (FULL parameter change notifications)
│   ├── Fuel_Management (COMPLETE fuel system audio feedback)
│   └── Environmental_Controls (FULL ECS and pressurization audio)
├── Avionics Systems/
│   ├── Navigation_Systems (COMPLETE GPS, INS, and radio nav audio)
│   ├── Communication_Systems (FULL radio and intercom audio)
│   ├── Radar_Systems (COMPLETE radar operation and target audio)
│   └── Electronic_Warfare (FULL countermeasures and jamming audio)
├── Weapons Systems/
│   ├── Weapons_Control (COMPLETE targeting and firing audio)
│   ├── Countermeasures (FULL chaff, flare, and ECM audio)
│   ├── Targeting_Systems (COMPLETE lock-on and tracking audio)
│   └── Safety_Systems (FULL weapon safety and arming audio)
├── Display Systems/
│   ├── Multi_Function_Displays (COMPLETE MFD interaction audio)
│   ├── Head_Up_Display (FULL HUD mode and symbology audio)
│   ├── Warning_Panels (COMPLETE caution and warning audio)
│   └── Instrument_Panels (FULL analog gauge audio simulation)
└── Environmental Systems/
    ├── Life_Support (COMPLETE oxygen and pressurization audio)
    ├── Electrical_Systems (FULL power management audio)
    ├── Hydraulic_Systems (COMPLETE hydraulic operation audio)
    └── Emergency_Systems (FULL emergency procedure audio)

MANDATORY SYSTEM AUDIO IMPLEMENTATION:

1. Flight Control System Audio MUST include:
```javascript
// Complete Flight Control System Audio
class FlightControlSystemAudio {
    constructor(audioEngine, spatialEngine) {
        this.audioEngine = audioEngine;
        this.spatialEngine = spatialEngine;
        
        // Control stick audio system
        this.controlStickAudio = new ControlStickAudioSystem(audioEngine, spatialEngine);
        
        // Rudder pedal audio system
        this.rudderPedalAudio = new RudderPedalAudioSystem(audioEngine, spatialEngine);
        
        // Trim system audio
        this.trimSystemAudio = new TrimSystemAudioSystem(audioEngine, spatialEngine);
        
        // Autopilot system audio
        this.autopilotAudio = new AutopilotAudioSystem(audioEngine, spatialEngine);
        
        // Flight management computer audio
        this.fmcAudio = new FMCAudioSystem(audioEngine, spatialEngine);
        
        // System state tracking
        this.systemStates = {
            controlStick: { x: 0, y: 0, force: 0 },
            rudderPedals: { left: 0, right: 0, force: 0 },
            trimSettings: { pitch: 0, roll: 0, yaw: 0 },
            autopilot: { engaged: false, mode: 'off', altitude: 0, heading: 0 },
            fmc: { activeWaypoint: null, flightPlan: [], mode: 'nav' }
        };
        
        // Audio feedback parameters
        this.feedbackSettings = {
            stickDeadzone: 0.02,
            forceScaling: 2.0,
            trimClickInterval: 0.1,
            autopilotBeepDuration: 0.2
        };
        
        this.initializeSystemAudio();
    }
    
    initializeSystemAudio() {
        // Load all flight control audio assets
        this.loadFlightControlAssets();
        
        // Setup spatial positioning for all controls
        this.setupSpatialPositioning();
        
        // Initialize real-time feedback systems
        this.initializeFeedbackSystems();
        
        console.log('Flight Control System Audio initialized');
    }
    
    async loadFlightControlAssets() {
        const assetList = [
            // Control stick assets
            'stick_movement_x_positive', 'stick_movement_x_negative',
            'stick_movement_y_positive', 'stick_movement_y_negative',
            'stick_force_light', 'stick_force_medium', 'stick_force_heavy',
            'stick_center_detent', 'stick_limit_stop',
            
            // Rudder pedal assets
            'rudder_left_press', 'rudder_right_press',
            'rudder_movement_continuous', 'rudder_release',
            'rudder_force_feedback', 'rudder_center_return',
            
            // Trim system assets
            'trim_pitch_up', 'trim_pitch_down',
            'trim_roll_left', 'trim_roll_right',
            'trim_yaw_left', 'trim_yaw_right',
            'trim_motor_run', 'trim_motor_stop',
            
            // Autopilot assets
            'autopilot_engage', 'autopilot_disengage',
            'autopilot_mode_change', 'autopilot_altitude_capture',
            'autopilot_heading_capture', 'autopilot_disconnect_warning',
            
            // FMC assets
            'fmc_key_press', 'fmc_data_entry', 'fmc_page_change',
            'fmc_waypoint_sequence', 'fmc_route_modification',
            'fmc_error_tone', 'fmc_confirmation_beep'
        ];
        
        const loadPromises = assetList.map(assetId => 
            this.audioEngine.assetManager.loadAudioAsset(assetId, {
                category: 'flight_control',
                priority: 'high',
                preload: true
            })
        );
        
        await Promise.all(loadPromises);
        console.log('Flight control audio assets loaded');
    }
    
    setupSpatialPositioning() {
        // Define precise 3D positions for all flight controls in cockpit space
        this.controlPositions = {
            controlStick: { x: 0, y: 0.8, z: 0.2 },      // Center console, pilot's right hand
            rudderPedals: { x: 0, y: 0.3, z: 0.8 },      // Floor, pilot's feet
            trimControls: { x: -0.3, y: 0.9, z: 0.1 },   // Left console
            autopilotPanel: { x: 0.2, y: 1.1, z: -0.1 }, // Upper center console
            fmcDisplay: { x: 0.3, y: 0.9, z: 0 }         // Right console
        };
        
        // Configure spatial audio sources for each control group
        for (const [controlName, position] of Object.entries(this.controlPositions)) {
            this.spatialEngine.registerAudioSource(controlName, position, {
                refDistance: 0.5,
                maxDistance: 3.0,
                rolloffFactor: 2.0,
                reverbSend: 0.2
            });
        }
    }
    
    initializeFeedbackSystems() {
        // Setup real-time parameter monitoring for continuous feedback
        this.parameterMonitor = new ParameterMonitor();
        
        // Initialize force feedback audio correlation
        this.forceFeedbackProcessor = new ForceFeedbackAudioProcessor(this.audioEngine);
        
        // Setup continuous audio generation for moving controls
        this.continuousAudioGenerator = new ContinuousAudioGenerator(this.audioEngine);
        
        // Initialize haptic-audio correlation system
        this.hapticAudioCorrelator = new HapticAudioCorrelator();
    }
    
    updateControlStick(stickPosition, force, deltaTime) {
        const previousState = { ...this.systemStates.controlStick };
        this.systemStates.controlStick = { ...stickPosition, force };
        
        // Calculate movement deltas
        const deltaX = stickPosition.x - previousState.x;
        const deltaY = stickPosition.y - previousState.y;
        const deltaForce = force - previousState.force;
        
        // Generate movement audio if significant change
        if (Math.abs(deltaX) > this.feedbackSettings.stickDeadzone) {
            this.playStickMovementAudio('x', deltaX, force);
        }
        
        if (Math.abs(deltaY) > this.feedbackSettings.stickDeadzone) {
            this.playStickMovementAudio('y', deltaY, force);
        }
        
        // Generate force feedback audio
        if (Math.abs(deltaForce) > 0.1) {
            this.playStickForceAudio(force, deltaTime);
        }
        
        // Update continuous movement audio
        this.updateContinuousStickAudio(stickPosition, force);
        
        // Check for limit stops
        this.checkStickLimits(stickPosition);
    }
    
    playStickMovementAudio(axis, delta, force) {
        const direction = delta > 0 ? 'positive' : 'negative';
        const assetId = `stick_movement_${axis}_${direction}`;
        
        // Calculate audio parameters based on movement speed and force
        const volume = Math.min(Math.abs(delta) * 2.0, 1.0);
        const pitch = 1.0 + (force * 0.2); // Higher force = higher pitch
        
        this.audioEngine.playAudioSource(assetId, {
            position: this.controlPositions.controlStick,
            volume: volume,
            pitch: pitch,
            category: 'flight_control'
        });
    }
    
    playStickForceAudio(force, deltaTime) {
        let forceCategory = 'light';
        if (force > 0.6) forceCategory = 'heavy';
        else if (force > 0.3) forceCategory = 'medium';
        
        const assetId = `stick_force_${forceCategory}`;
        
        this.audioEngine.playAudioSource(assetId, {
            position: this.controlPositions.controlStick,
            volume: Math.min(force * this.feedbackSettings.forceScaling, 1.0),
            category: 'flight_control'
        });
    }
    
    updateContinuousStickAudio(position, force) {
        // Generate continuous audio for stick movement (mechanical friction, etc.)
        if (Math.abs(position.x) > 0.1 || Math.abs(position.y) > 0.1) {
            this.continuousAudioGenerator.updateStickMovement(position, force);
        } else {
            this.continuousAudioGenerator.stopStickMovement();
        }
    }
    
    checkStickLimits(position) {
        const limitThreshold = 0.95;
        
        if (Math.abs(position.x) > limitThreshold || Math.abs(position.y) > limitThreshold) {
            this.audioEngine.playAudioSource('stick_limit_stop', {
                position: this.controlPositions.controlStick,
                volume: 0.8,
                category: 'flight_control'
            });
        }
    }
    
    updateRudderPedals(pedalPositions, forces, deltaTime) {
        const previousState = { ...this.systemStates.rudderPedals };
        this.systemStates.rudderPedals = { ...pedalPositions, force: forces };
        
        // Handle left pedal
        if (Math.abs(pedalPositions.left - previousState.left) > 0.02) {
            this.playRudderPedalAudio('left', pedalPositions.left, forces.left);
        }
        
        // Handle right pedal
        if (Math.abs(pedalPositions.right - previousState.right) > 0.02) {
            this.playRudderPedalAudio('right', pedalPositions.right, forces.right);
        }
        
        // Update continuous pedal audio
        this.updateContinuousRudderAudio(pedalPositions, forces);
    }
    
    playRudderPedalAudio(side, position, force) {
        const assetId = `rudder_${side}_press`;
        
        this.audioEngine.playAudioSource(assetId, {
            position: this.controlPositions.rudderPedals,
            volume: Math.min(force * 1.5, 1.0),
            pitch: 1.0 + (Math.abs(position) * 0.3),
            category: 'flight_control'
        });
    }
    
    updateTrimSystem(trimInputs, deltaTime) {
        // Handle pitch trim
        if (trimInputs.pitch !== 0) {
            const direction = trimInputs.pitch > 0 ? 'up' : 'down';
            this.playTrimAudio('pitch', direction, Math.abs(trimInputs.pitch));
            this.systemStates.trimSettings.pitch += trimInputs.pitch * deltaTime;
        }
        
        // Handle roll trim
        if (trimInputs.roll !== 0) {
            const direction = trimInputs.roll > 0 ? 'right' : 'left';
            this.playTrimAudio('roll', direction, Math.abs(trimInputs.roll));
            this.systemStates.trimSettings.roll += trimInputs.roll * deltaTime;
        }
        
        // Handle yaw trim
        if (trimInputs.yaw !== 0) {
            const direction = trimInputs.yaw > 0 ? 'right' : 'left';
            this.playTrimAudio('yaw', direction, Math.abs(trimInputs.yaw));
            this.systemStates.trimSettings.yaw += trimInputs.yaw * deltaTime;
        }
    }
    
    playTrimAudio(axis, direction, intensity) {
        const assetId = `trim_${axis}_${direction}`;
        
        // Play trim click sound
        this.audioEngine.playAudioSource(assetId, {
            position: this.controlPositions.trimControls,
            volume: Math.min(intensity * 0.8, 1.0),
            category: 'flight_control'
        });
        
        // Play trim motor sound if continuous input
        if (intensity > 0.5) {
            this.audioEngine.playAudioSource('trim_motor_run', {
                position: this.controlPositions.trimControls,
                volume: 0.6,
                loop: true,
                category: 'flight_control'
            });
        }
    }
    
    updateAutopilot(autopilotState, deltaTime) {
        const previousState = { ...this.systemStates.autopilot };
        this.systemStates.autopilot = { ...autopilotState };
        
        // Handle autopilot engagement changes
        if (autopilotState.engaged !== previousState.engaged) {
            const assetId = autopilotState.engaged ? 'autopilot_engage' : 'autopilot_disengage';
            this.audioEngine.playAudioSource(assetId, {
                position: this.controlPositions.autopilotPanel,
                volume: 0.8,
                category: 'flight_control'
            });
        }
        
        // Handle mode changes
        if (autopilotState.mode !== previousState.mode) {
            this.audioEngine.playAudioSource('autopilot_mode_change', {
                position: this.controlPositions.autopilotPanel,
                volume: 0.7,
                category: 'flight_control'
            });
        }
        
        // Handle altitude capture
        if (autopilotState.altitudeCapture && !previousState.altitudeCapture) {
            this.audioEngine.playAudioSource('autopilot_altitude_capture', {
                position: this.controlPositions.autopilotPanel,
                volume: 0.8,
                category: 'flight_control'
            });
        }
        
        // Handle heading capture
        if (autopilotState.headingCapture && !previousState.headingCapture) {
            this.audioEngine.playAudioSource('autopilot_heading_capture', {
                position: this.controlPositions.autopilotPanel,
                volume: 0.8,
                category: 'flight_control'
            });
        }
    }
    
    updateFMC(fmcState, deltaTime) {
        const previousState = { ...this.systemStates.fmc };
        this.systemStates.fmc = { ...fmcState };
        
        // Handle waypoint sequencing
        if (fmcState.activeWaypoint !== previousState.activeWaypoint) {
            this.audioEngine.playAudioSource('fmc_waypoint_sequence', {
                position: this.controlPositions.fmcDisplay,
                volume: 0.6,
                category: 'flight_control'
            });
        }
        
        // Handle route modifications
        if (fmcState.flightPlan.length !== previousState.flightPlan.length) {
            this.audioEngine.playAudioSource('fmc_route_modification', {
                position: this.controlPositions.fmcDisplay,
                volume: 0.7,
                category: 'flight_control'
            });
        }
        
        // Handle mode changes
        if (fmcState.mode !== previousState.mode) {
            this.audioEngine.playAudioSource('fmc_mode_change', {
                position: this.controlPositions.fmcDisplay,
                volume: 0.6,
                category: 'flight_control'
            });
        }
    }
    
    handleFMCKeyPress(keyId, keyType) {
        let assetId = 'fmc_key_press';
        
        // Different sounds for different key types
        switch (keyType) {
            case 'data':
                assetId = 'fmc_data_entry';
                break;
            case 'function':
                assetId = 'fmc_page_change';
                break;
            case 'execute':
                assetId = 'fmc_confirmation_beep';
                break;
            case 'clear':
                assetId = 'fmc_error_tone';
                break;
        }
        
        this.audioEngine.playAudioSource(assetId, {
            position: this.controlPositions.fmcDisplay,
            volume: 0.8,
            category: 'flight_control'
        });
    }
    
    update(deltaTime, cockpitState) {
        // Update all flight control subsystems
        if (cockpitState.flightControls) {
            if (cockpitState.flightControls.controlStick) {
                this.updateControlStick(
                    cockpitState.flightControls.controlStick.position,
                    cockpitState.flightControls.controlStick.force,
                    deltaTime
                );
            }
            
            if (cockpitState.flightControls.rudderPedals) {
                this.updateRudderPedals(
                    cockpitState.flightControls.rudderPedals.positions,
                    cockpitState.flightControls.rudderPedals.forces,
                    deltaTime
                );
            }
            
            if (cockpitState.flightControls.trimSystem) {
                this.updateTrimSystem(
                    cockpitState.flightControls.trimSystem.inputs,
                    deltaTime
                );
            }
            
            if (cockpitState.flightControls.autopilot) {
                this.updateAutopilot(
                    cockpitState.flightControls.autopilot,
                    deltaTime
                );
            }
            
            if (cockpitState.flightControls.fmc) {
                this.updateFMC(
                    cockpitState.flightControls.fmc,
                    deltaTime
                );
            }
        }
        
        // Update continuous audio generators
        this.continuousAudioGenerator.update(deltaTime);
        
        // Update force feedback processor
        this.forceFeedbackProcessor.update(deltaTime);
    }
    
    dispose() {
        // Stop all continuous audio
        this.continuousAudioGenerator.dispose();
        
        // Dispose force feedback processor
        this.forceFeedbackProcessor.dispose();
        
        // Dispose subsystems
        this.controlStickAudio.dispose();
        this.rudderPedalAudio.dispose();
        this.trimSystemAudio.dispose();
        this.autopilotAudio.dispose();
        this.fmcAudio.dispose();
    }
}

// Continuous Audio Generator for moving controls
class ContinuousAudioGenerator {
    constructor(audioEngine) {
        this.audioEngine = audioEngine;
        this.activeGenerators = new Map();
        
        // Create noise generators for mechanical sounds
        this.mechanicalNoise = this.createMechanicalNoiseGenerator();
        this.frictionNoise = this.createFrictionNoiseGenerator();
    }
    
    createMechanicalNoiseGenerator() {
        const audioContext = this.audioEngine.audioContext;
        
        // Create filtered noise for mechanical sounds
        const bufferSize = audioContext.sampleRate * 2; // 2 seconds
        const buffer = audioContext.createBuffer(1, bufferSize, audioContext.sampleRate);
        const data = buffer.getChannelData(0);
        
        // Generate pink noise for more natural mechanical sound
        let b0 = 0, b1 = 0, b2 = 0, b3 = 0, b4 = 0, b5 = 0, b6 = 0;
        for (let i = 0; i < bufferSize; i++) {
            const white = Math.random() * 2 - 1;
            b0 = 0.99886 * b0 + white * 0.0555179;
            b1 = 0.99332 * b1 + white * 0.0750759;
            b2 = 0.96900 * b2 + white * 0.1538520;
            b3 = 0.86650 * b3 + white * 0.3104856;
            b4 = 0.55000 * b4 + white * 0.5329522;
            b5 = -0.7616 * b5 - white * 0.0168980;
            data[i] = (b0 + b1 + b2 + b3 + b4 + b5 + b6 + white * 0.5362) * 0.11;
            b6 = white * 0.115926;
        }
        
        return buffer;
    }
    
    createFrictionNoiseGenerator() {
        const audioContext = this.audioEngine.audioContext;
        
        // Create high-frequency noise for friction sounds
        const bufferSize = audioContext.sampleRate * 1; // 1 second
        const buffer = audioContext.createBuffer(1, bufferSize, audioContext.sampleRate);
        const data = buffer.getChannelData(0);
        
        for (let i = 0; i < bufferSize; i++) {
            // High-frequency filtered noise
            data[i] = (Math.random() * 2 - 1) * Math.sin(i * 0.01) * 0.3;
        }
        
        return buffer;
    }
    
    updateStickMovement(position, force) {
        const generatorId = 'stick_movement';
        
        if (!this.activeGenerators.has(generatorId)) {
            this.startContinuousGenerator(generatorId, 'mechanical', position);
        }
        
        const generator = this.activeGenerators.get(generatorId);
        
        // Update generator parameters based on stick position and force
        const movementIntensity = Math.sqrt(position.x * position.x + position.y * position.y);
        const volume = Math.min(movementIntensity * force * 0.3, 0.8);
        const filterFreq = 200 + (force * 800); // 200-1000 Hz based on force
        
        generator.gainNode.gain.setValueAtTime(volume, this.audioEngine.audioContext.currentTime);
        generator.filterNode.frequency.setValueAtTime(filterFreq, this.audioEngine.audioContext.currentTime);
    }
    
    stopStickMovement() {
        this.stopContinuousGenerator('stick_movement');
    }
    
    startContinuousGenerator(generatorId, type, position) {
        const audioContext = this.audioEngine.audioContext;
        
        // Create audio source
        const source = audioContext.createBufferSource();
        source.buffer = type === 'mechanical' ? this.mechanicalNoise : this.frictionNoise;
        source.loop = true;
        
        // Create processing chain
        const gainNode = audioContext.createGain();
        const filterNode = audioContext.createBiquadFilter();
        filterNode.type = 'bandpass';
        filterNode.frequency.setValueAtTime(500, audioContext.currentTime);
        filterNode.Q.setValueAtTime(2, audioContext.currentTime);
        
        // Connect processing chain
        source.connect(filterNode);
        filterNode.connect(gainNode);
        
        // Add spatial processing if position provided
        let outputNode = gainNode;
        if (position) {
            const spatialSource = this.audioEngine.spatialEngine.createSpatialSource(gainNode, position);
            outputNode = spatialSource.panner;
        } else {
            gainNode.connect(this.audioEngine.masterGain);
        }
        
        // Start source
        source.start();
        
        // Store generator reference
        this.activeGenerators.set(generatorId, {
            source: source,
            gainNode: gainNode,
            filterNode: filterNode,
            outputNode: outputNode,
            type: type
        });
    }
    
    stopContinuousGenerator(generatorId) {
        if (this.activeGenerators.has(generatorId)) {
            const generator = this.activeGenerators.get(generatorId);
            
            // Fade out and stop
            const fadeTime = 0.1;
            generator.gainNode.gain.exponentialRampToValueAtTime(
                0.001, 
                this.audioEngine.audioContext.currentTime + fadeTime
            );
            
            setTimeout(() => {
                generator.source.stop();
                this.activeGenerators.delete(generatorId);
            }, fadeTime * 1000);
        }
    }
    
    update(deltaTime) {
        // Update any time-based parameters for active generators
        for (const [id, generator] of this.activeGenerators) {
            // Add subtle parameter variations for realism
            const time = this.audioEngine.audioContext.currentTime;
            const variation = Math.sin(time * 2) * 0.1 + 1.0;
            
            if (generator.filterNode) {
                const currentFreq = generator.filterNode.frequency.value;
                generator.filterNode.frequency.setValueAtTime(
                    currentFreq * variation,
                    time
                );
            }
        }
    }
    
    dispose() {
        // Stop all active generators
        for (const [id, generator] of this.activeGenerators) {
            generator.source.stop();
        }
        this.activeGenerators.clear();
    }
}

// Force Feedback Audio Processor
class ForceFeedbackAudioProcessor {
    constructor(audioEngine) {
        this.audioEngine = audioEngine;
        
        // Force feedback parameters
        this.forceThresholds = {
            light: 0.2,
            medium: 0.5,
            heavy: 0.8
        };
        
        // Active force feedback sources
        this.activeForceSources = new Map();
        
        // Create force feedback synthesizer
        this.forceSynthesizer = this.createForceSynthesizer();
    }
    
    createForceSynthesizer() {
        const audioContext = this.audioEngine.audioContext;
        
        // Create oscillator for force feedback synthesis
        const oscillator = audioContext.createOscillator();
        oscillator.type = 'triangle';
        oscillator.frequency.setValueAtTime(40, audioContext.currentTime); // Low frequency rumble
        
        const gainNode = audioContext.createGain();
        gainNode.gain.setValueAtTime(0, audioContext.currentTime);
        
        const filterNode = audioContext.createBiquadFilter();
        filterNode.type = 'lowpass';
        filterNode.frequency.setValueAtTime(200, audioContext.currentTime);
        
        // Connect synthesis chain
        oscillator.connect(filterNode);
        filterNode.connect(gainNode);
        gainNode.connect(this.audioEngine.masterGain);
        
        oscillator.start();
        
        return {
            oscillator: oscillator,
            gainNode: gainNode,
            filterNode: filterNode
        };
    }
    
    processForceInput(controlId, force, position) {
        // Determine force category
        let forceCategory = 'light';
        if (force > this.forceThresholds.heavy) forceCategory = 'heavy';
        else if (force > this.forceThresholds.medium) forceCategory = 'medium';
        
        // Update force feedback synthesis
        this.updateForceSynthesis(controlId, force, forceCategory);
        
        // Generate discrete force feedback events
        this.generateForceEvents(controlId, force, forceCategory, position);
    }
    
    updateForceSynthesis(controlId, force, category) {
        const currentTime = this.audioEngine.audioContext.currentTime;
        
        // Update synthesizer parameters based on force
        const volume = Math.min(force * 0.5, 0.8);
        const frequency = 40 + (force * 60); // 40-100 Hz range
        
        this.forceSynthesizer.gainNode.gain.exponentialRampToValueAtTime(
            volume, currentTime + 0.05
        );
        
        this.forceSynthesizer.oscillator.frequency.exponentialRampToValueAtTime(
            frequency, currentTime + 0.05
        );
    }
    
    generateForceEvents(controlId, force, category, position) {
        // Generate discrete audio events for force changes
        if (force > this.forceThresholds.medium) {
            const assetId = `force_feedback_${category}`;
            
            this.audioEngine.playAudioSource(assetId, {
                position: position,
                volume: Math.min(force * 0.8, 1.0),
                category: 'force_feedback'
            });
        }
    }
    
    update(deltaTime) {
        // Update force feedback processing
        // Add any time-based force feedback effects here
    }
    
    dispose() {
        // Stop force synthesizer
        if (this.forceSynthesizer.oscillator) {
            this.forceSynthesizer.oscillator.stop();
        }
        
        this.activeForceSources.clear();
    }
}

// Export flight control system audio
export { FlightControlSystemAudio, ContinuousAudioGenerator, ForceFeedbackAudioProcessor };
```

2. Engine Management System Audio MUST include:
```javascript
// Complete Engine Management System Audio
class EngineManagementSystemAudio {
    constructor(audioEngine, spatialEngine) {
        this.audioEngine = audioEngine;
        this.spatialEngine = spatialEngine;
        
        // Engine subsystems
        this.throttleAudio = new ThrottleSystemAudio(audioEngine, spatialEngine);
        this.engineMonitorAudio = new EngineMonitoringAudio(audioEngine, spatialEngine);
        this.fuelSystemAudio = new FuelSystemAudio(audioEngine, spatialEngine);
        this.environmentalAudio = new EnvironmentalControlAudio(audioEngine, spatialEngine);
        
        // System state tracking
        this.engineStates = {
            leftEngine: { rpm: 0, throttle: 0, temperature: 0, pressure: 0 },
            rightEngine: { rpm: 0, throttle: 0, temperature: 0, pressure: 0 },
            fuelSystem: { quantity: 1.0, flow: 0, pressure: 0 },
            environmental: { temperature: 20, pressure: 1.0, oxygenFlow: 0 }
        };
        
        // Audio positioning
        this.enginePositions = {
            leftEngine: { x: -2.0, y: 0, z: -8.0 },    // Left engine bay
            rightEngine: { x: 2.0, y: 0, z: -8.0 },    // Right engine bay
            throttleQuadrant: { x: -0.2, y: 0.8, z: 0.3 }, // Left console
            fuelPanel: { x: 0.3, y: 1.0, z: -0.2 },    // Upper right console
            environmentalPanel: { x: -0.4, y: 1.0, z: -0.1 } // Upper left console
        };
        
        this.initializeEngineAudio();
    }
    
    async initializeEngineAudio() {
        // Load engine management audio assets
        await this.loadEngineAssets();
        
        // Setup spatial positioning
        this.setupEnginePositioning();
        
        // Initialize real-time engine synthesis
        this.initializeEngineSynthesis();
        
        console.log('Engine Management System Audio initialized');
    }
    
    async loadEngineAssets() {
        const assetList = [
            // Throttle system assets
            'throttle_movement_forward', 'throttle_movement_back',
            'throttle_detent_military', 'throttle_detent_afterburner',
            'throttle_mechanical_click', 'throttle_friction_adjust',
            
            // Engine monitoring assets
            'engine_parameter_change', 'engine_limit_warning',
            'engine_normal_operation', 'engine_abnormal_operation',
            'compressor_stall_warning', 'engine_fire_warning',
            
            // Fuel system assets
            'fuel_pump_start', 'fuel_pump_stop', 'fuel_pump_running',
            'fuel_transfer_valve', 'fuel_quantity_low_warning',
            'fuel_flow_change', 'fuel_pressure_warning',
            
            // Environmental control assets
            'ecs_bleed_air_valve', 'ecs_temperature_change',
            'pressurization_valve', 'oxygen_flow_start',
            'oxygen_flow_stop', 'cabin_pressure_warning'
        ];
        
        const loadPromises = assetList.map(assetId => 
            this.audioEngine.assetManager.loadAudioAsset(assetId, {
                category: 'engine_management',
                priority: 'high',
                preload: true
            })
        );
        
        await Promise.all(loadPromises);
        console.log('Engine management audio assets loaded');
    }
    
    setupEnginePositioning() {
        // Configure spatial audio sources for engine components
        for (const [componentName, position] of Object.entries(this.enginePositions)) {
            this.spatialEngine.registerAudioSource(componentName, position, {
                refDistance: 1.0,
                maxDistance: 10.0,
                rolloffFactor: 1.5,
                reverbSend: 0.3
            });
        }
    }
    
    initializeEngineSynthesis() {
        // Initialize real-time engine audio synthesis
        this.leftEngineSynthesizer = new EngineAudioSynthesizer(
            this.audioEngine, 
            this.enginePositions.leftEngine
        );
        
        this.rightEngineSynthesizer = new EngineAudioSynthesizer(
            this.audioEngine, 
            this.enginePositions.rightEngine
        );
    }
    
    updateThrottleSystem(throttleInputs, deltaTime) {
        // Handle left throttle
        if (throttleInputs.left !== undefined) {
            this.updateThrottle('left', throttleInputs.left, deltaTime);
        }
        
        // Handle right throttle
        if (throttleInputs.right !== undefined) {
            this.updateThrottle('right', throttleInputs.right, deltaTime);
        }
    }
    
    updateThrottle(side, throttlePosition, deltaTime) {
        const engineKey = `${side}Engine`;
        const previousThrottle = this.engineStates[engineKey].throttle;
        const throttleDelta = throttlePosition - previousThrottle;
        
        // Update engine state
        this.engineStates[engineKey].throttle = throttlePosition;
        
        // Generate throttle movement audio
        if (Math.abs(throttleDelta) > 0.02) {
            const direction = throttleDelta > 0 ? 'forward' : 'back';
            const assetId = `throttle_movement_${direction}`;
            
            this.audioEngine.playAudioSource(assetId, {
                position: this.enginePositions.throttleQuadrant,
                volume: Math.min(Math.abs(throttleDelta) * 3.0, 1.0),
                pitch: 1.0 + (throttlePosition * 0.2),
                category: 'engine_management'
            });
        }
        
        // Check for detent positions
        this.checkThrottleDetents(side, throttlePosition, previousThrottle);
        
        // Update engine synthesis
        this.updateEngineSynthesis(side, throttlePosition);
    }
    
    checkThrottleDetents(side, currentPosition, previousPosition) {
        const militaryPowerDetent = 0.85;
        const afterburnerDetent = 0.95;
        
        // Check military power detent
        if (previousPosition < militaryPowerDetent && currentPosition >= militaryPowerDetent) {
            this.audioEngine.playAudioSource('throttle_detent_military', {
                position: this.enginePositions.throttleQuadrant,
                volume: 0.8,
                category: 'engine_management'
            });
        }
        
        // Check afterburner detent
        if (previousPosition < afterburnerDetent && currentPosition >= afterburnerDetent) {
            this.audioEngine.playAudioSource('throttle_detent_afterburner', {
                position: this.enginePositions.throttleQuadrant,
                volume: 0.9,
                category: 'engine_management'
            });
        }
    }
    
    updateEngineSynthesis(side, throttlePosition) {
        const synthesizer = side === 'left' ? this.leftEngineSynthesizer : this.rightEngineSynthesizer;
        
        // Calculate engine parameters from throttle position
        const rpm = this.calculateEngineRPM(throttlePosition);
        const temperature = this.calculateEngineTemperature(throttlePosition);
        const pressure = this.calculateEnginePressure(throttlePosition);
        
        // Update engine state
        const engineKey = `${side}Engine`;
        this.engineStates[engineKey].rpm = rpm;
        this.engineStates[engineKey].temperature = temperature;
        this.engineStates[engineKey].pressure = pressure;
        
        // Update synthesizer
        synthesizer.updateEngineParameters(throttlePosition, rpm, throttlePosition > 0.95);
    }
    
    calculateEngineRPM(throttlePosition) {
        // Realistic engine RPM curve
        const idleRPM = 65; // 65% N1
        const maxRPM = 105; // 105% N1
        
        // Non-linear RPM response
        const rpmCurve = Math.pow(throttlePosition, 0.8);
        return idleRPM + (maxRPM - idleRPM) * rpmCurve;
    }
    
    calculateEngineTemperature(throttlePosition) {
        // Engine temperature based on throttle position
        const idleTemp = 400; // Celsius
        const maxTemp = 1200; // Celsius
        
        return idleTemp + (maxTemp - idleTemp) * Math.pow(throttlePosition, 1.2);
    }
    
    calculateEnginePressure(throttlePosition) {
        // Engine pressure based on throttle position
        const idlePressure = 14.7; // PSI
        const maxPressure = 45.0; // PSI
        
        return idlePressure + (maxPressure - idlePressure) * throttlePosition;
    }
    
    updateEngineMonitoring(engineData, deltaTime) {
        // Monitor left engine
        if (engineData.left) {
            this.monitorEngineParameters('left', engineData.left);
        }
        
        // Monitor right engine
        if (engineData.right) {
            this.monitorEngineParameters('right', engineData.right);
        }
    }
    
    monitorEngineParameters(side, engineData) {
        const engineKey = `${side}Engine`;
        const previousState = { ...this.engineStates[engineKey] };
        
        // Check for parameter limit exceedances
        if (engineData.temperature > 1100) { // Red line temperature
            this.triggerEngineWarning('temperature', side, engineData.temperature);
        }
        
        if (engineData.rpm > 103) { // Over-speed condition
            this.triggerEngineWarning('overspeed', side, engineData.rpm);
        }
        
        if (engineData.pressure < 10) { // Low oil pressure
            this.triggerEngineWarning('oil_pressure', side, engineData.pressure);
        }
        
        // Generate parameter change audio for significant changes
        this.generateParameterChangeAudio(side, previousState, engineData);
    }
    
    triggerEngineWarning(warningType, side, value) {
        let assetId = 'engine_limit_warning';
        
        switch (warningType) {
            case 'temperature':
                assetId = 'engine_temperature_warning';
                break;
            case 'overspeed':
                assetId = 'engine_overspeed_warning';
                break;
            case 'oil_pressure':
                assetId = 'engine_oil_pressure_warning';
                break;
            case 'fire':
                assetId = 'engine_fire_warning';
                break;
        }
        
        const enginePosition = side === 'left' ? 
            this.enginePositions.leftEngine : 
            this.enginePositions.rightEngine;
        
        this.audioEngine.playAudioSource(assetId, {
            position: enginePosition,
            volume: 0.9,
            priority: 'critical',
            category: 'engine_warning'
        });
    }
    
    generateParameterChangeAudio(side, previousState, currentState) {
        // Generate subtle audio cues for parameter changes
        const parameterChanges = {
            rpm: Math.abs(currentState.rpm - previousState.rpm),
            temperature: Math.abs(currentState.temperature - previousState.temperature),
            pressure: Math.abs(currentState.pressure - previousState.pressure)
        };
        
        // Only generate audio for significant changes
        if (parameterChanges.rpm > 5 || 
            parameterChanges.temperature > 50 || 
            parameterChanges.pressure > 2) {
            
            const enginePosition = side === 'left' ? 
                this.enginePositions.leftEngine : 
                this.enginePositions.rightEngine;
            
            this.audioEngine.playAudioSource('engine_parameter_change', {
                position: enginePosition,
                volume: 0.4,
                pitch: 1.0 + (currentState.rpm / 100 - 1) * 0.3,
                category: 'engine_monitoring'
            });
        }
    }
    
    updateFuelSystem(fuelData, deltaTime) {
        const previousState = { ...this.engineStates.fuelSystem };
        this.engineStates.fuelSystem = { ...fuelData };
        
        // Handle fuel quantity changes
        if (Math.abs(fuelData.quantity - previousState.quantity) > 0.01) {
            this.handleFuelQuantityChange(fuelData.quantity, previousState.quantity);
        }
        
        // Handle fuel flow changes
        if (Math.abs(fuelData.flow - previousState.flow) > 100) { // 100 lbs/hr threshold
            this.handleFuelFlowChange(fuelData.flow, previousState.flow);
        }
        
        // Check for fuel warnings
        this.checkFuelWarnings(fuelData);
    }
    
    handleFuelQuantityChange(currentQuantity, previousQuantity) {
        // Generate fuel transfer audio for significant changes
        if (Math.abs(currentQuantity - previousQuantity) > 0.05) {
            this.audioEngine.playAudioSource('fuel_transfer_valve', {
                position: this.enginePositions.fuelPanel,
                volume: 0.6,
                category: 'fuel_system'
            });
        }
    }
    
    handleFuelFlowChange(currentFlow, previousFlow) {
        this.audioEngine.playAudioSource('fuel_flow_change', {
            position: this.enginePositions.fuelPanel,
            volume: Math.min(Math.abs(currentFlow - previousFlow) / 1000, 0.8),
            pitch: 1.0 + (currentFlow / 5000) * 0.2,
            category: 'fuel_system'
        });
    }
    
    checkFuelWarnings(fuelData) {
        // Low fuel quantity warning
        if (fuelData.quantity < 0.2) { // 20% fuel remaining
            this.audioEngine.playAudioSource('fuel_quantity_low_warning', {
                position: this.enginePositions.fuelPanel,
                volume: 0.8,
                priority: 'high',
                category: 'fuel_warning'
            });
        }
        
        // Fuel pressure warning
        if (fuelData.pressure < 15) { // Low fuel pressure
            this.audioEngine.playAudioSource('fuel_pressure_warning', {
                position: this.enginePositions.fuelPanel,
                volume: 0.9,
                priority: 'critical',
                category: 'fuel_warning'
            });
        }
    }
    
    updateEnvironmentalControls(environmentalData, deltaTime) {
        const previousState = { ...this.engineStates.environmental };
        this.engineStates.environmental = { ...environmentalData };
        
        // Handle temperature changes
        if (Math.abs(environmentalData.temperature - previousState.temperature) > 2) {
            this.handleTemperatureChange(environmentalData.temperature, previousState.temperature);
        }
        
        // Handle pressure changes
        if (Math.abs(environmentalData.pressure - previousState.pressure) > 0.1) {
            this.handlePressureChange(environmentalData.pressure, previousState.pressure);
        }
        
        // Handle oxygen flow changes
        if (Math.abs(environmentalData.oxygenFlow - previousState.oxygenFlow) > 0.1) {
            this.handleOxygenFlowChange(environmentalData.oxygenFlow, previousState.oxygenFlow);
        }
    }
    
    handleTemperatureChange(currentTemp, previousTemp) {
        this.audioEngine.playAudioSource('ecs_temperature_change', {
            position: this.enginePositions.environmentalPanel,
            volume: Math.min(Math.abs(currentTemp - previousTemp) / 10, 0.7),
            pitch: 1.0 + (currentTemp - 20) / 50 * 0.3,
            category: 'environmental_control'
        });
    }
    
    handlePressureChange(currentPressure, previousPressure) {
        this.audioEngine.playAudioSource('pressurization_valve', {
            position: this.enginePositions.environmentalPanel,
            volume: Math.min(Math.abs(currentPressure - previousPressure) * 2, 0.8),
            category: 'environmental_control'
        });
    }
    
    handleOxygenFlowChange(currentFlow, previousFlow) {
        const assetId = currentFlow > previousFlow ? 'oxygen_flow_start' : 'oxygen_flow_stop';
        
        this.audioEngine.playAudioSource(assetId, {
            position: this.enginePositions.environmentalPanel,
            volume: 0.7,
            category: 'environmental_control'
        });
    }
    
    update(deltaTime, cockpitState) {
        // Update all engine management subsystems
        if (cockpitState.engineManagement) {
            if (cockpitState.engineManagement.throttles) {
                this.updateThrottleSystem(cockpitState.engineManagement.throttles, deltaTime);
            }
            
            if (cockpitState.engineManagement.engines) {
                this.updateEngineMonitoring(cockpitState.engineManagement.engines, deltaTime);
            }
            
            if (cockpitState.engineManagement.fuel) {
                this.updateFuelSystem(cockpitState.engineManagement.fuel, deltaTime);
            }
            
            if (cockpitState.engineManagement.environmental) {
                this.updateEnvironmentalControls(cockpitState.engineManagement.environmental, deltaTime);
            }
        }
        
        // Update engine synthesizers
        this.leftEngineSynthesizer.update(deltaTime);
        this.rightEngineSynthesizer.update(deltaTime);
    }
    
    dispose() {
        // Dispose engine synthesizers
        this.leftEngineSynthesizer.dispose();
        this.rightEngineSynthesizer.dispose();
        
        // Dispose subsystems
        this.throttleAudio.dispose();
        this.engineMonitorAudio.dispose();
        this.fuelSystemAudio.dispose();
        this.environmentalAudio.dispose();
    }
}

// Export engine management system audio
export { EngineManagementSystemAudio };
```

VALIDATION CHECKPOINT:
After implementation, CURSOR MUST verify:
✓ All cockpit system audio responds to real-time state changes
✓ Interactive feedback provides immediate tactile correlation
✓ System audio matches military aviation specifications
✓ Performance remains stable with full system audio active
✓ Spatial positioning accurately reflects cockpit geometry
✓ Audio latency remains below 5ms for all interactions
✓ Memory usage stays within allocated limits
✓ All audio systems integrate seamlessly with Three.js scene

QUALITY GATE:
✓ System audio provides authentic military aviation experience
✓ Interactive feedback enhances immersion without distraction
✓ All controls have unique and recognizable audio signatures
✓ Performance benchmarks maintained under full system load
✓ Audio system responds correctly to all cockpit state changes
✓ Spatial audio positioning matches physical control locations
```

**GAP IDENTIFICATION FOR PHASE 2.1**:
```
CURSOR MUST CHECK FOR THESE POTENTIAL GAPS:
❌ Missing system audio causing silent cockpit operations
❌ Poor interactive feedback reducing immersion quality
❌ Incorrect spatial positioning breaking audio realism
❌ Performance issues causing audio dropouts or latency
❌ Missing military specification compliance
❌ Inadequate real-time responsiveness
❌ Poor integration with Three.js scene updates
❌ Missing tactile correlation with physical interactions
```

## Prompt 2.2: Warning and Alert System Implementation

**PREREQUISITE VALIDATION**:
```
CURSOR MUST VERIFY FROM PHASE 2.1:
✓ Complete cockpit system audio implementation functional
✓ Interactive feedback system providing tactile correlation
✓ All system audio responding to real-time state changes
✓ Performance benchmarks maintained with full system load
✓ Spatial positioning accurate for all cockpit components
✓ Audio latency below 5ms for all interactive elements
```

**CURSOR RULES FOR THIS PROMPT**:
1. MUST implement complete military-specification alert system
2. ALL warning priorities must follow established military protocols
3. MUST provide hierarchical audio priority management
4. Alert system MUST be instantly recognizable by trained pilots

**DETAILED IMPLEMENTATION**:
```
Implement comprehensive military-specification warning and alert system:

MANDATORY WARNING AND ALERT SYSTEM FEATURES:

1. MILITARY SPECIFICATION ALERT HIERARCHY (COMPLETE IMPLEMENTATION):
   - MUST implement proper military alert priority levels:
     * Level 1 (Critical): Immediate life-threatening conditions
     * Level 2 (Warning): Serious system malfunctions requiring immediate action
     * Level 3 (Caution): System degradation requiring monitoring
     * Level 4 (Advisory): Information requiring pilot awareness
   - MUST support proper alert audio characteristics:
     * Critical alerts: Continuous tone, 1000Hz, 85dB minimum
     * Warning alerts: Intermittent tone, 800Hz, 80dB minimum
     * Caution alerts: Single tone, 600Hz, 75dB minimum
     * Advisory alerts: Chime or voice, 500Hz, 70dB minimum

2. REAL-TIME ALERT PROCESSING (ALL FEATURES REQUIRED):
   - Immediate alert triggering with <2ms latency
   - Automatic alert prioritization and queuing
   - Alert acknowledgment and silencing system
   - Alert history and logging for post-flight analysis
   - Integration with cockpit warning light systems
   - Voice alert synthesis for critical warnings

3. AUTHENTIC MILITARY ALERT SOUNDS (FULL IMPLEMENTATION):
   - Master Caution: Distinctive two-tone chime
   - Master Warning: Continuous warbling tone
   - Fire Warning: Distinctive bell sound
   - Missile Warning: Rapid beeping tone
   - Altitude Warning: Distinctive "whoop whoop" sound
   - Stall Warning: Stick shaker audio correlation
   - Gear Warning: Horn sound for unsafe gear conditions

Complete Alert System Implementation:
```javascript
// Military Specification Warning and Alert System
class MilitaryAlertSystem {
    constructor(audioEngine, spatialEngine) {
        this.audioEngine = audioEngine;
        this.spatialEngine = spatialEngine;
        
        // Alert priority levels (military specification)
        this.alertPriorities = {
            CRITICAL: 1,    // Immediate life threat
            WARNING: 2,     // Serious malfunction
            CAUTION: 3,     // System degradation
            ADVISORY: 4     // Information only
        };
        
        // Alert audio specifications (military standard)
        this.alertSpecs = {
            CRITICAL: {
                frequency: 1000,
                pattern: 'continuous',
                volume: 0.95,
                duration: null, // Continuous until acknowledged
                repetition: null
            },
            WARNING: {
                frequency: 800,
                pattern: 'intermittent',
                volume: 0.85,
                duration: 0.5,
                repetition: 1.0 // 1 second intervals
            },
            CAUTION: {
                frequency: 600,
                pattern: 'single',
                volume: 0.75,
                duration: 1.0,
                repetition: null
            },
            ADVISORY: {
                frequency: 500,
                pattern: 'chime',
                volume: 0.65,
                duration: 0.3,
                repetition: null
            }
        };
        
        // Active alerts management
        this.activeAlerts = new Map();
        this.alertQueue = new PriorityQueue();
        this.acknowledgedAlerts = new Set();
        this.alertHistory = [];
        
        // Alert audio sources
        this.alertSources = new Map();
        
        // Voice alert system
        this.voiceAlertSystem = new VoiceAlertSystem(audioEngine);
        
        // Alert positioning (warning panel location)
        this.alertPosition = { x: 0, y: 1.2, z: -0.1 };
        
        this.initializeAlertSystem();
    }
    
    async initializeAlertSystem() {
        // Load military specification alert audio assets
        await this.loadMilitaryAlertAssets();
        
        // Setup alert audio synthesis
        this.setupAlertSynthesis();
        
        // Initialize voice alert system
        await this.voiceAlertSystem.initialize();
        
        // Setup spatial positioning for alert panel
        this.setupAlertPositioning();
        
        console.log('Military Alert System initialized');
    }
    
    async loadMilitaryAlertAssets() {
        const militaryAlertAssets = [
            // Master alerts
            'master_caution_chime', 'master_warning_tone',
            
            // Fire warning system
            'fire_warning_bell', 'fire_warning_continuous',
            
            // Flight safety alerts
            'altitude_warning_whoop', 'stall_warning_horn',
            'overspeed_warning_clacker', 'pull_up_warning',
            
            // Missile warning system
            'missile_warning_beep', 'rwr_warning_tone',
            'chaff_flare_warning', 'lock_on_warning',
            
            // Landing gear warnings
            'gear_warning_horn', 'gear_unsafe_warning',
            'gear_retract_warning', 'gear_extend_warning',
            
            // Engine warnings
            'engine_fire_bell', 'engine_failure_tone',
            'compressor_stall_warning', 'engine_overheat_warning',
            
            // Fuel system warnings
            'fuel_low_warning', 'fuel_critical_warning',
            'fuel_imbalance_warning', 'fuel_pump_failure',
            
            // Electrical system warnings
            'electrical_failure_tone', 'generator_failure_warning',
            'battery_low_warning', 'electrical_fire_warning',
            
            // Hydraulic system warnings
            'hydraulic_failure_tone', 'hydraulic_low_pressure',
            'flight_control_failure', 'utility_hydraulic_failure',
            
            // Environmental warnings
            'cabin_pressure_warning', 'oxygen_low_warning',
            'temperature_warning', 'pressurization_failure',
            
            // Navigation warnings
            'navigation_failure_tone', 'gps_failure_warning',
            'ins_failure_warning', 'compass_failure_warning',
            
            // Communication warnings
            'radio_failure_tone', 'communication_jam_warning',
            'encryption_failure_warning', 'datalink_failure'
        ];
        
        const loadPromises = militaryAlertAssets.map(assetId => 
            this.audioEngine.assetManager.loadAudioAsset(assetId, {
                category: 'military_alerts',
                priority: 'critical',
                preload: true
            })
        );
        
        await Promise.all(loadPromises);
        console.log('Military alert audio assets loaded');
    }
    
    setupAlertSynthesis() {
        // Create alert tone synthesizers for each priority level
        this.alertSynthesizers = new Map();
        
        for (const [priority, specs] of Object.entries(this.alertSpecs)) {
            const synthesizer = this.createAlertSynthesizer(specs);
            this.alertSynthesizers.set(priority, synthesizer);
        }
    }
    
    createAlertSynthesizer(specs) {
        const audioContext = this.audioEngine.audioContext;
        
        // Create oscillator for alert tone
        const oscillator = audioContext.createOscillator();
        oscillator.frequency.setValueAtTime(specs.frequency, audioContext.currentTime);
        
        // Set waveform based on alert type
        switch (specs.pattern) {
            case 'continuous':
                oscillator.type = 'sine';
                break;
            case 'intermittent':
                oscillator.type = 'square';
                break;
            case 'single':
                oscillator.type = 'triangle';
                break;
            case 'chime':
                oscillator.type = 'sine';
                break;
        }
        
        // Create gain envelope for alert pattern
        const gainNode = audioContext.createGain();
        gainNode.gain.setValueAtTime(0, audioContext.currentTime);
        
        // Create filter for tone shaping
        const filterNode = audioContext.createBiquadFilter();
        filterNode.type = 'bandpass';
        filterNode.frequency.setValueAtTime(specs.frequency, audioContext.currentTime);
        filterNode.Q.setValueAtTime(5, audioContext.currentTime);
        
        // Connect synthesis chain
        oscillator.connect(filterNode);
        filterNode.connect(gainNode);
        
        // Add spatial processing
        const spatialSource = this.spatialEngine.createSpatialSource(gainNode, this.alertPosition);
        
        // Start oscillator
        oscillator.start();
        
        return {
            oscillator: oscillator,
            gainNode: gainNode,
            filterNode: filterNode,
            spatialSource: spatialSource,
            specs: specs,
            isActive: false
        };
    }
    
    setupAlertPositioning() {
        // Configure spatial audio for alert panel
        this.spatialEngine.registerAudioSource('alert_panel', this.alertPosition, {
            refDistance: 0.8,
            maxDistance: 5.0,
            rolloffFactor: 1.0,
            reverbSend: 0.1 // Minimal reverb for clarity
        });
    }
    
    triggerAlert(alertId, alertType, priority, data = {}) {
        const currentTime = performance.now();
        
        // Create alert object
        const alert = {
            id: alertId,
            type: alertType,
            priority: this.alertPriorities[priority],
            priorityName: priority,
            timestamp: currentTime,
            data: data,
            acknowledged: false,
            active: true
        };
        
        // Add to alert history
        this.alertHistory.push(alert);
        
        // Check if alert is already active
        if (this.activeAlerts.has(alertId)) {
            console.log(`Alert ${alertId} already active, updating data`);
            const existingAlert = this.activeAlerts.get(alertId);
            existingAlert.data = { ...existingAlert.data, ...data };
            return;
        }
        
        // Add to active alerts
        this.activeAlerts.set(alertId, alert);
        
        // Add to priority queue
        this.alertQueue.enqueue(alert, alert.priority);
        
        // Process alert immediately
        this.processAlert(alert);
        
        console.log(`Alert triggered: ${alertId} (${priority})`);
    }
    
    processAlert(alert) {
        // Determine audio asset to play
        const audioAsset = this.getAlertAudioAsset(alert.type, alert.priorityName);
        
        // Play alert audio
        if (audioAsset) {
            this.playAlertAudio(audioAsset, alert);
        }
        
        // Start synthesized alert tone if required
        if (this.requiresSynthesizedTone(alert.type)) {
            this.startAlertTone(alert.priorityName, alert);
        }
        
        // Trigger voice alert if critical
        if (alert.priority <= this.alertPriorities.WARNING) {
            this.voiceAlertSystem.announceAlert(alert);
        }
        
        // Handle alert pattern (continuous, intermittent, etc.)
        this.handleAlertPattern(alert);
    }
    
    getAlertAudioAsset(alertType, priority) {
        // Map alert types to specific audio assets
        const alertAudioMap = {
            'master_caution': 'master_caution_chime',
            'master_warning': 'master_warning_tone',
            'fire_warning': 'fire_warning_bell',
            'missile_warning': 'missile_warning_beep',
            'altitude_warning': 'altitude_warning_whoop',
            'stall_warning': 'stall_warning_horn',
            'gear_warning': 'gear_warning_horn',
            'engine_fire': 'engine_fire_bell',
            'fuel_low': 'fuel_low_warning',
            'hydraulic_failure': 'hydraulic_failure_tone',
            'electrical_failure': 'electrical_failure_tone',
            'cabin_pressure': 'cabin_pressure_warning',
            'navigation_failure': 'navigation_failure_tone',
            'radio_failure': 'radio_failure_tone'
        };
        
        return alertAudioMap[alertType] || null;
    }
    
    playAlertAudio(audioAsset, alert) {
        const alertSpecs = this.alertSpecs[alert.priorityName];
        
        const audioSource = this.audioEngine.playAudioSource(audioAsset, {
            position: this.alertPosition,
            volume: alertSpecs.volume,
            priority: 'critical',
            category: 'military_alerts',
            loop: alertSpecs.pattern === 'continuous'
        });
        
        // Store audio source reference for potential stopping
        if (audioSource) {
            this.alertSources.set(alert.id, audioSource);
        }
    }
    
    requiresSynthesizedTone(alertType) {
        // Some alerts use synthesized tones instead of or in addition to samples
        const synthesizedAlerts = [
            'altitude_warning', 'stall_warning', 'overspeed_warning',
            'pull_up_warning', 'missile_warning'
        ];
        
        return synthesizedAlerts.includes(alertType);
    }
    
    startAlertTone(priority, alert) {
        const synthesizer = this.alertSynthesizers.get(priority);
        if (!synthesizer || synthesizer.isActive) return;
        
        const specs = synthesizer.specs;
        const currentTime = this.audioEngine.audioContext.currentTime;
        
        // Start tone based on pattern
        switch (specs.pattern) {
            case 'continuous':
                synthesizer.gainNode.gain.setValueAtTime(specs.volume, currentTime);
                synthesizer.isActive = true;
                break;
                
            case 'intermittent':
                this.startIntermittentTone(synthesizer, specs);
                break;
                
            case 'single':
                this.playSingleTone(synthesizer, specs);
                break;
                
            case 'chime':
                this.playChimeTone(synthesizer, specs);
                break;
        }
    }
    
    startIntermittentTone(synthesizer, specs) {
        const currentTime = this.audioEngine.audioContext.currentTime;
        synthesizer.isActive = true;
        
        // Create intermittent pattern
        const patternDuration = specs.duration + specs.repetition;
        let time = currentTime;
        
        const playPattern = () => {
            if (!synthesizer.isActive) return;
            
            // Tone on
            synthesizer.gainNode.gain.setValueAtTime(specs.volume, time);
            synthesizer.gainNode.gain.setValueAtTime(specs.volume, time + specs.duration);
            
            // Tone off
            synthesizer.gainNode.gain.setValueAtTime(0, time + specs.duration + 0.01);
            
            time += patternDuration;
            
            // Schedule next pattern
            setTimeout(() => playPattern(), patternDuration * 1000);
        };
        
        playPattern();
    }
    
    playSingleTone(synthesizer, specs) {
        const currentTime = this.audioEngine.audioContext.currentTime;
        
        // Play single tone with envelope
        synthesizer.gainNode.gain.setValueAtTime(0, currentTime);
        synthesizer.gainNode.gain.linearRampToValueAtTime(specs.volume, currentTime + 0.05);
        synthesizer.gainNode.gain.setValueAtTime(specs.volume, currentTime + specs.duration - 0.05);
        synthesizer.gainNode.gain.linearRampToValueAtTime(0, currentTime + specs.duration);
    }
    
    playChimeTone(synthesizer, specs) {
        const currentTime = this.audioEngine.audioContext.currentTime;
        
        // Create chime pattern (two-tone)
        const firstToneFreq = specs.frequency;
        const secondToneFreq = specs.frequency * 1.25; // Perfect fourth interval
        
        // First tone
        synthesizer.oscillator.frequency.setValueAtTime(firstToneFreq, currentTime);
        synthesizer.gainNode.gain.setValueAtTime(0, currentTime);
        synthesizer.gainNode.gain.linearRampToValueAtTime(specs.volume, currentTime + 0.02);
        synthesizer.gainNode.gain.linearRampToValueAtTime(0, currentTime + specs.duration / 2);
        
        // Second tone
        synthesizer.oscillator.frequency.setValueAtTime(secondToneFreq, currentTime + specs.duration / 2);
        synthesizer.gainNode.gain.linearRampToValueAtTime(specs.volume, currentTime + specs.duration / 2 + 0.02);
        synthesizer.gainNode.gain.linearRampToValueAtTime(0, currentTime + specs.duration);
    }
    
    handleAlertPattern(alert) {
        const specs = this.alertSpecs[alert.priorityName];
        
        // Set up alert timing and repetition
        if (specs.repetition && alert.priority > this.alertPriorities.CRITICAL) {
            // Schedule alert repetition for non-critical alerts
            setTimeout(() => {
                if (this.activeAlerts.has(alert.id) && !this.acknowledgedAlerts.has(alert.id)) {
                    this.processAlert(alert);
                }
            }, specs.repetition * 1000);
        }
    }
    
    acknowledgeAlert(alertId) {
        if (!this.activeAlerts.has(alertId)) {
            console.warn(`Cannot acknowledge non-existent alert: ${alertId}`);
            return false;
        }
        
        const alert = this.activeAlerts.get(alertId);
        alert.acknowledged = true;
        this.acknowledgedAlerts.add(alertId);
        
        // Stop alert audio
        this.stopAlertAudio(alertId);
        
        // Stop synthesized tone
        this.stopAlertTone(alert.priorityName);
        
        console.log(`Alert acknowledged: ${alertId}`);
        return true;
    }
    
    silenceAlert(alertId) {
        if (!this.activeAlerts.has(alertId)) {
            console.warn(`Cannot silence non-existent alert: ${alertId}`);
            return false;
        }
        
        const alert = this.activeAlerts.get(alertId);
        
        // Stop alert audio
        this.stopAlertAudio(alertId);
        
        // Stop synthesized tone
        this.stopAlertTone(alert.priorityName);
        
        // Remove from active alerts but keep in history
        alert.active = false;
        this.activeAlerts.delete(alertId);
        
        console.log(`Alert silenced: ${alertId}`);
        return true;
    }
    
    stopAlertAudio(alertId) {
        if (this.alertSources.has(alertId)) {
            const audioSource = this.alertSources.get(alertId);
            audioSource.stop();
            this.alertSources.delete(alertId);
        }
    }
    
    stopAlertTone(priority) {
        const synthesizer = this.alertSynthesizers.get(priority);
        if (synthesizer && synthesizer.isActive) {
            const currentTime = this.audioEngine.audioContext.currentTime;
            synthesizer.gainNode.gain.exponentialRampToValueAtTime(0.001, currentTime + 0.1);
            synthesizer.isActive = false;
        }
    }
    
    clearAllAlerts() {
        // Stop all active alerts
        for (const [alertId, alert] of this.activeAlerts) {
            this.silenceAlert(alertId);
        }
        
        // Clear acknowledged alerts
        this.acknowledgedAlerts.clear();
        
        console.log('All alerts cleared');
    }
    
    getActiveAlerts() {
        return Array.from(this.activeAlerts.values())
            .sort((a, b) => a.priority - b.priority);
    }
    
    getAlertHistory() {
        return [...this.alertHistory].sort((a, b) => b.timestamp - a.timestamp);
    }
    
    update(deltaTime, cockpitState) {
        // Process alert queue
        this.processAlertQueue();
        
        // Update voice alert system
        this.voiceAlertSystem.update(deltaTime);
        
        // Check for new alerts based on cockpit state
        this.monitorSystemStates(cockpitState);
    }
    
    processAlertQueue() {
        // Process highest priority alerts first
        while (!this.alertQueue.isEmpty()) {
            const alert = this.alertQueue.dequeue();
            if (this.activeAlerts.has(alert.id) && !this.acknowledgedAlerts.has(alert.id)) {
                // Alert is still active and not acknowledged, continue processing
                this.processAlert(alert);
            }
        }
    }
    
    monitorSystemStates(cockpitState) {
        // Monitor various systems for alert conditions
        if (cockpitState.engine) {
            this.monitorEngineAlerts(cockpitState.engine);
        }
        
        if (cockpitState.fuel) {
            this.monitorFuelAlerts(cockpitState.fuel);
        }
        
        if (cockpitState.flight) {
            this.monitorFlightAlerts(cockpitState.flight);
        }
        
        if (cockpitState.electrical) {
            this.monitorElectricalAlerts(cockpitState.electrical);
        }
        
        if (cockpitState.hydraulic) {
            this.monitorHydraulicAlerts(cockpitState.hydraulic);
        }
    }
    
    monitorEngineAlerts(engineState) {
        // Engine fire detection
        if (engineState.leftEngine?.fire || engineState.rightEngine?.fire) {
            this.triggerAlert('engine_fire', 'engine_fire', 'CRITICAL', {
                engine: engineState.leftEngine?.fire ? 'left' : 'right'
            });
        }
        
        // Engine overheat
        if (engineState.leftEngine?.temperature > 1100 || engineState.rightEngine?.temperature > 1100) {
            this.triggerAlert('engine_overheat', 'engine_overheat', 'WARNING', {
                temperature: Math.max(engineState.leftEngine?.temperature || 0, engineState.rightEngine?.temperature || 0)
            });
        }
        
        // Compressor stall
        if (engineState.leftEngine?.compressorStall || engineState.rightEngine?.compressorStall) {
            this.triggerAlert('compressor_stall', 'compressor_stall', 'WARNING', {
                engine: engineState.leftEngine?.compressorStall ? 'left' : 'right'
            });
        }
    }
    
    monitorFuelAlerts(fuelState) {
        // Low fuel warning
        if (fuelState.totalQuantity < 0.2) { // 20% fuel remaining
            this.triggerAlert('fuel_low', 'fuel_low', 'CAUTION', {
                quantity: fuelState.totalQuantity
            });
        }
        
        // Critical fuel warning
        if (fuelState.totalQuantity < 0.1) { // 10% fuel remaining
            this.triggerAlert('fuel_critical', 'fuel_critical', 'WARNING', {
                quantity: fuelState.totalQuantity
            });
        }
        
        // Fuel imbalance
        if (Math.abs(fuelState.leftTank - fuelState.rightTank) > 0.15) {
            this.triggerAlert('fuel_imbalance', 'fuel_imbalance', 'CAUTION', {
                imbalance: Math.abs(fuelState.leftTank - fuelState.rightTank)
            });
        }
    }
    
    monitorFlightAlerts(flightState) {
        // Altitude warning
        if (flightState.altitude < 500 && flightState.verticalSpeed < -1000) {
            this.triggerAlert('altitude_warning', 'altitude_warning', 'CRITICAL', {
                altitude: flightState.altitude,
                verticalSpeed: flightState.verticalSpeed
            });
        }
        
        // Stall warning
        if (flightState.angleOfAttack > 18) { // Degrees
            this.triggerAlert('stall_warning', 'stall_warning', 'WARNING', {
                angleOfAttack: flightState.angleOfAttack
            });
        }
        
        // Overspeed warning
        if (flightState.airspeed > 450) { // Knots
            this.triggerAlert('overspeed_warning', 'overspeed_warning', 'WARNING', {
                airspeed: flightState.airspeed
            });
        }
        
        // Landing gear warning
        if (flightState.altitude < 1000 && flightState.gearPosition !== 'down' && flightState.throttle < 0.3) {
            this.triggerAlert('gear_warning', 'gear_warning', 'CAUTION', {
                altitude: flightState.altitude,
                gearPosition: flightState.gearPosition
            });
        }
    }
    
    monitorElectricalAlerts(electricalState) {
        // Generator failure
        if (!electricalState.leftGenerator || !electricalState.rightGenerator) {
            this.triggerAlert('generator_failure', 'electrical_failure', 'WARNING', {
                leftGenerator: electricalState.leftGenerator,
                rightGenerator: electricalState.rightGenerator
            });
        }
        
        // Battery low
        if (electricalState.batteryVoltage < 22) { // 24V system
            this.triggerAlert('battery_low', 'battery_low', 'CAUTION', {
                voltage: electricalState.batteryVoltage
            });
        }
    }
    
    monitorHydraulicAlerts(hydraulicState) {
        // Hydraulic system failure
        if (hydraulicState.system1Pressure < 2000 || hydraulicState.system2Pressure < 2000) {
            this.triggerAlert('hydraulic_failure', 'hydraulic_failure', 'WARNING', {
                system1Pressure: hydraulicState.system1Pressure,
                system2Pressure: hydraulicState.system2Pressure
            });
        }
        
        // Utility hydraulic failure
        if (hydraulicState.utilityPressure < 1500) {
            this.triggerAlert('utility_hydraulic_failure', 'utility_hydraulic_failure', 'CAUTION', {
                utilityPressure: hydraulicState.utilityPressure
            });
        }
    }
    
    dispose() {
        // Stop all active alerts
        this.clearAllAlerts();
        
        // Dispose synthesizers
        for (const [priority, synthesizer] of this.alertSynthesizers) {
            synthesizer.oscillator.stop();
        }
        this.alertSynthesizers.clear();
        
        // Dispose voice alert system
        this.voiceAlertSystem.dispose();
        
        // Clear all data structures
        this.activeAlerts.clear();
        this.acknowledgedAlerts.clear();
        this.alertSources.clear();
        this.alertHistory.length = 0;
    }
}

// Voice Alert System for critical warnings
class VoiceAlertSystem {
    constructor(audioEngine) {
        this.audioEngine = audioEngine;
        this.speechSynthesis = window.speechSynthesis;
        this.voiceQueue = [];
        this.isPlaying = false;
        
        // Voice alert phrases (military standard)
        this.alertPhrases = {
            'engine_fire': 'Engine fire, engine fire',
            'missile_warning': 'Missile, missile, missile',
            'altitude_warning': 'Pull up, pull up',
            'stall_warning': 'Stall, stall, stall',
            'fuel_critical': 'Fuel critical, fuel critical',
            'hydraulic_failure': 'Hydraulic failure',
            'electrical_failure': 'Electrical failure',
            'cabin_pressure': 'Cabin pressure, cabin pressure'
        };
    }
    
    async initialize() {
        // Wait for voices to be loaded
        if (this.speechSynthesis.getVoices().length === 0) {
            await new Promise(resolve => {
                this.speechSynthesis.addEventListener('voiceschanged', resolve, { once: true });
            });
        }
        
        // Select appropriate voice (prefer male, authoritative voice)
        const voices = this.speechSynthesis.getVoices();
        this.selectedVoice = voices.find(voice => 
            voice.lang.startsWith('en') && 
            voice.name.toLowerCase().includes('male')
        ) || voices[0];
        
        console.log('Voice Alert System initialized');
    }
    
    announceAlert(alert) {
        const phrase = this.alertPhrases[alert.type];
        if (!phrase) return;
        
        // Create speech utterance
        const utterance = new SpeechSynthesisUtterance(phrase);
        utterance.voice = this.selectedVoice;
        utterance.rate = 1.2; // Slightly faster for urgency
        utterance.pitch = 1.0;
        utterance.volume = 0.9;
        
        // Add to queue
        this.voiceQueue.push(utterance);
        
        // Process queue
        this.processVoiceQueue();
    }
    
    processVoiceQueue() {
        if (this.isPlaying || this.voiceQueue.length === 0) return;
        
        const utterance = this.voiceQueue.shift();
        this.isPlaying = true;
        
        utterance.onend = () => {
            this.isPlaying = false;
            // Process next in queue
            setTimeout(() => this.processVoiceQueue(), 500);
        };
        
        utterance.onerror = () => {
            this.isPlaying = false;
            console.warn('Voice alert synthesis error');
        };
        
        this.speechSynthesis.speak(utterance);
    }
    
    update(deltaTime) {
        // Update voice alert system
        // Handle any time-based voice alert processing
    }
    
    dispose() {
        // Cancel any ongoing speech
        this.speechSynthesis.cancel();
        this.voiceQueue.length = 0;
        this.isPlaying = false;
    }
}

// Export military alert system
export { MilitaryAlertSystem, VoiceAlertSystem };
```

VALIDATION REQUIREMENTS:
CURSOR MUST verify after implementation:
✓ All military specification alert priorities implemented correctly
✓ Alert audio meets military standard frequency and volume requirements
✓ Alert acknowledgment and silencing systems work properly
✓ Voice alert system provides clear, authoritative announcements
✓ Alert hierarchy properly prioritizes critical over non-critical alerts
✓ Real-time alert processing maintains <2ms latency
✓ Alert history and logging capture all alert events
✓ Integration with cockpit systems triggers appropriate alerts

PERFORMANCE BENCHMARKS (MUST ACHIEVE):
✓ Alert triggering latency: <2ms from system state change
✓ Voice alert synthesis: <500ms from alert trigger
✓ Alert audio clarity: >95% intelligibility in noisy environment
✓ Alert prioritization: 100% correct priority ordering
✓ Memory usage: <16MB for complete alert system
✓ CPU usage: <2% for alert processing and synthesis
```

**GAP IDENTIFICATION FOR PHASE 2.2**:
```
CURSOR MUST CHECK FOR THESE CRITICAL GAPS:
❌ Missing military specification compliance
❌ Incorrect alert priority implementation
❌ Poor voice alert synthesis quality
❌ Missing alert acknowledgment system
❌ Inadequate real-time alert processing
❌ Missing integration with cockpit systems
❌ Poor alert audio clarity or volume
❌ Missing alert history and logging
```

## PHASE 2 COMPLETION CHECKLIST

### ✅ **SYSTEM AUDIO VALIDATION REQUIREMENTS**
- [ ] Complete cockpit system audio for all components functional
- [ ] Interactive feedback system providing immediate tactile correlation
- [ ] Military specification warning and alert system operational
- [ ] All system audio responding to real-time cockpit state changes
- [ ] Voice alert system providing clear military-standard announcements
- [ ] Alert prioritization system following established military protocols
- [ ] Performance benchmarks maintained with full system audio active
- [ ] Spatial positioning accurate for all cockpit audio sources

### ✅ **QUALITY GATES**
- [ ] System audio provides authentic military aviation experience
- [ ] Interactive feedback enhances immersion without distraction
- [ ] All controls have unique and recognizable audio signatures
- [ ] Alert system instantly recognizable by trained pilots
- [ ] Audio latency below 5ms for all interactive elements
- [ ] Military specification compliance verified for all alerts
- [ ] Real-time responsiveness maintained under full system load

### ✅ **PERFORMANCE BENCHMARKS**
- [ ] Interactive feedback latency: <5ms from user input
- [ ] System audio processing: <3% CPU usage total
- [ ] Alert triggering latency: <2ms from state change
- [ ] Voice alert synthesis: <500ms response time
- [ ] Memory usage: <64MB for complete system audio
- [ ] Audio clarity: >95% intelligibility in operational environment
- [ ] Spatial accuracy: Perfect correlation with cockpit geometry
- [ ] Alert prioritization: 100% correct military protocol compliance

**PHASE 2 MUST BE 100% COMPLETE BEFORE PROCEEDING TO PHASE 3**

---

*This document serves as the definitive guide for Audio Phase 2 development in the Fighter Jet Cockpit project. All system audio and interactive feedback must follow these processes and meet these standards to achieve the target authentic military aviation experience.*
