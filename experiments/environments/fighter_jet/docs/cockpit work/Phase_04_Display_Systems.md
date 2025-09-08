# PHASE 4: CINEMA-QUALITY DISPLAY SYSTEMS

## PRE-PHASE 4 VALIDATION:
```
CURSOR MUST VERIFY FROM PHASE 3:
✓ Parametric cockpit geometry is fully functional
✓ Multi-layer glass systems render correctly
✓ Mechanical systems provide realistic physics
✓ All geometry components integrate properly
✓ Performance benchmarks are met (>45 FPS)
✓ Environmental effects enhance realism
✓ Memory usage is within acceptable limits
```

## Prompt 4.1: Photorealistic Display Simulation

**PREREQUISITE VALIDATION**:
```
CURSOR MUST VERIFY:
✓ Advanced renderer supports complex display rendering
✓ Material system can handle emissive materials
✓ Geometry system provides proper display mounting
✓ Asset manager can load display content
✓ Performance monitoring shows acceptable baseline
```

**CURSOR RULES FOR THIS PROMPT**:
1. MUST implement displays indistinguishable from real hardware
2. ALL display physics must be based on actual LCD/OLED/CRT technology
3. MUST support ultra-high resolution text rendering
4. Display quality must support extreme close-up inspection

**DETAILED IMPLEMENTATION**:
```
Create displays that are indistinguishable from real hardware:

MANDATORY DISPLAY SYSTEM COMPONENTS:

1. LCD/OLED DISPLAY PHYSICS (COMPLETE IMPLEMENTATION):
   DisplaySystem.js MUST implement:

   LIQUID CRYSTAL SIMULATION:
   - MUST implement proper liquid crystal director orientation simulation
   - MUST create realistic backlight uniformity with edge lighting simulation
   - MUST build color filter array simulation with proper subpixel rendering
   - MUST implement viewing angle color shift with proper gamma correction
   - MUST create realistic response time simulation with pixel persistence
   - MUST build proper black level simulation with backlight bleed

   OLED SIMULATION:
   - MUST implement individual pixel emission with proper OLED characteristics
   - MUST create realistic burn-in patterns and aging effects
   - MUST build proper color accuracy with wide gamut support
   - MUST implement infinite contrast ratio with true black levels
   - MUST create realistic power consumption modeling
   - MUST build proper temperature effects on OLED performance

2. CRT DISPLAY SIMULATION (COMPLETE IMPLEMENTATION):
   CRTSystem.js MUST implement:

   PHOSPHOR SIMULATION:
   - MUST implement proper phosphor persistence and decay curves
   - MUST create realistic electron beam scanning with proper timing
   - MUST build geometric distortion (pincushion, barrel) simulation
   - MUST implement proper color convergence and fringing effects
   - MUST create realistic burn-in patterns and ghost images
   - MUST build proper flicker simulation at various refresh rates

3. ULTRA-HIGH RESOLUTION TEXT RENDERING (COMPLETE IMPLEMENTATION):
   TextRenderer.js MUST implement:

   SUBPIXEL RENDERING:
   - MUST implement subpixel text rendering for maximum sharpness
   - MUST create proper font hinting and antialiasing
   - MUST build dynamic font loading with fallback systems
   - MUST implement proper kerning and typography spacing
   - MUST create realistic character spacing and baseline alignment
   - MUST build proper Unicode support for international characters

COMPLETE IMPLEMENTATION REQUIREMENTS:

DisplaySystem.js MUST implement:
```javascript
class DisplaySystem {
    constructor(renderer, materialSystem) {
        this.renderer = renderer;
        this.materialSystem = materialSystem;
        
        // COMPLETE display types
        this.lcdDisplays = new LCDDisplaySystem();
        this.oledDisplays = new OLEDDisplaySystem();
        this.crtDisplays = new CRTDisplaySystem();
        
        // COMPLETE rendering systems
        this.textRenderer = new TextRenderer();
        this.graphicsRenderer = new GraphicsRenderer();
        this.videoRenderer = new VideoRenderer();
        
        // COMPLETE display management
        this.displayManager = new DisplayManager();
        this.contentManager = new ContentManager();
        this.powerManager = new PowerManager();
        
        this.initializeDisplaySystem();
    }
    
    // MUST implement complete display creation
    createDisplay(displaySpec) {
        let display;
        
        switch (displaySpec.type) {
            case 'LCD':
                display = this.createLCDDisplay(displaySpec);
                break;
            case 'OLED':
                display = this.createOLEDDisplay(displaySpec);
                break;
            case 'CRT':
                display = this.createCRTDisplay(displaySpec);
                break;
            default:
                throw new Error(`Unsupported display type: ${displaySpec.type}`);
        }
        
        // COMPLETE display integration
        this.integrateDisplay(display, displaySpec);
        this.calibrateDisplay(display, displaySpec);
        this.validateDisplay(display);
        
        return display;
    }
    
    // MUST implement complete LCD display
    createLCDDisplay(spec) {
        const lcdDisplay = {
            // COMPLETE physical properties
            width: spec.width || 0.2, // 200mm
            height: spec.height || 0.15, // 150mm
            thickness: spec.thickness || 0.005, // 5mm
            resolution: spec.resolution || { width: 1920, height: 1440 },
            pixelPitch: this.calculatePixelPitch(spec),
            
            // COMPLETE LCD layers
            layers: {
                backlight: this.createBacklightSystem(spec),
                diffuser: this.createDiffuserLayer(spec),
                polarizer1: this.createPolarizerLayer(spec, 0),
                tftArray: this.createTFTArray(spec),
                liquidCrystal: this.createLiquidCrystalLayer(spec),
                colorFilter: this.createColorFilterArray(spec),
                polarizer2: this.createPolarizerLayer(spec, 90),
                coverGlass: this.createCoverGlass(spec)
            },
            
            // COMPLETE optical properties
            opticalProperties: {
                brightness: spec.brightness || 500, // nits
                contrast: spec.contrast || 1000,
                colorGamut: spec.colorGamut || 'sRGB',
                viewingAngle: spec.viewingAngle || 170, // degrees
                responseTime: spec.responseTime || 5 // milliseconds
            },
            
            // COMPLETE rendering system
            renderTarget: this.createDisplayRenderTarget(spec),
            contentCanvas: this.createContentCanvas(spec),
            
            // COMPLETE display state
            powerState: 'off',
            brightness: 0,
            content: null,
            lastUpdate: 0
        };
        
        return lcdDisplay;
    }
    
    // MUST implement complete backlight system
    createBacklightSystem(spec) {
        const backlight = {
            type: spec.backlightType || 'edge_lit_led',
            leds: [],
            lightGuide: null,
            uniformity: spec.uniformity || 0.85,
            efficiency: spec.efficiency || 0.4
        };
        
        switch (backlight.type) {
            case 'edge_lit_led':
                backlight.leds = this.createEdgeLitLEDs(spec);
                backlight.lightGuide = this.createLightGuide(spec);
                break;
            case 'direct_led':
                backlight.leds = this.createDirectLEDs(spec);
                break;
            case 'ccfl':
                backlight.ccfl = this.createCCFL(spec);
                break;
        }
        
        // COMPLETE uniformity simulation
        backlight.uniformityMap = this.generateUniformityMap(backlight, spec);
        
        return backlight;
    }
    
    // MUST implement complete liquid crystal simulation
    createLiquidCrystalLayer(spec) {
        const liquidCrystal = {
            thickness: 5e-6, // 5 micrometers
            material: spec.lcMaterial || 'TN', // Twisted Nematic
            tiltAngle: spec.tiltAngle || 2, // degrees
            twistAngle: spec.twistAngle || 90, // degrees
            
            // COMPLETE LC properties
            properties: {
                deltaEpsilon: 10.5, // dielectric anisotropy
                deltaEpsilonParallel: 19.2,
                deltaEpsilonPerpendicular: 8.7,
                elasticConstants: {
                    k11: 15.7e-12, // splay
                    k22: 6.8e-12,  // twist
                    k33: 19.5e-12  // bend
                }
            },
            
            // COMPLETE voltage response
            voltageResponse: this.createVoltageResponse(spec),
            
            // COMPLETE optical response
            opticalResponse: this.createOpticalResponse(spec)
        };
        
        return liquidCrystal;
    }
    
    // MUST implement complete color filter array
    createColorFilterArray(spec) {
        const colorFilter = {
            pattern: spec.cfaPattern || 'RGB_stripe',
            pixelGeometry: spec.pixelGeometry || 'rectangular',
            
            // COMPLETE color filters
            filters: {
                red: {
                    transmittance: this.getRedFilterTransmittance(),
                    peakWavelength: 630, // nm
                    bandwidth: 100 // nm
                },
                green: {
                    transmittance: this.getGreenFilterTransmittance(),
                    peakWavelength: 530, // nm
                    bandwidth: 80 // nm
                },
                blue: {
                    transmittance: this.getBlueFilterTransmittance(),
                    peakWavelength: 460, // nm
                    bandwidth: 90 // nm
                }
            },
            
            // COMPLETE subpixel layout
            subpixelLayout: this.generateSubpixelLayout(spec)
        };
        
        return colorFilter;
    }
}

class TextRenderer {
    constructor() {
        this.fontManager = new FontManager();
        this.glyphCache = new GlyphCache();
        this.subpixelRenderer = new SubpixelRenderer();
        this.hintingEngine = new HintingEngine();
    }
    
    // MUST implement complete text rendering
    renderText(text, font, size, position, display) {
        // COMPLETE font loading and validation
        const loadedFont = this.fontManager.loadFont(font);
        this.validateFont(loadedFont, size);
        
        // COMPLETE text layout
        const textLayout = this.layoutText(text, loadedFont, size);
        const glyphs = this.shapeText(textLayout);
        
        // COMPLETE subpixel rendering
        const renderedGlyphs = [];
        for (const glyph of glyphs) {
            const renderedGlyph = this.renderGlyph(glyph, loadedFont, size, display);
            renderedGlyphs.push(renderedGlyph);
        }
        
        // COMPLETE text composition
        const compositeText = this.compositeGlyphs(renderedGlyphs, position);
        
        return compositeText;
    }
    
    // MUST implement complete subpixel rendering
    renderGlyph(glyph, font, size, display) {
        const pixelDensity = this.calculatePixelDensity(display);
        const subpixelLayout = display.layers.colorFilter.subpixelLayout;
        
        // COMPLETE glyph rasterization
        const rasterizedGlyph = this.rasterizeGlyph(glyph, font, size, pixelDensity);
        
        // COMPLETE subpixel optimization
        const subpixelGlyph = this.optimizeForSubpixels(
            rasterizedGlyph,
            subpixelLayout,
            display.opticalProperties
        );
        
        // COMPLETE hinting application
        const hintedGlyph = this.applyHinting(subpixelGlyph, font, size);
        
        return hintedGlyph;
    }
    
    // MUST implement complete font hinting
    applyHinting(glyph, font, size) {
        const hintingInstructions = font.getHintingInstructions(glyph.unicode);
        
        // COMPLETE grid fitting
        const gridFittedGlyph = this.applyGridFitting(glyph, size);
        
        // COMPLETE stem alignment
        const stemAlignedGlyph = this.alignStems(gridFittedGlyph, hintingInstructions);
        
        // COMPLETE contrast enhancement
        const enhancedGlyph = this.enhanceContrast(stemAlignedGlyph);
        
        return enhancedGlyph;
    }
}

class CRTSystem {
    constructor() {
        this.electronGun = new ElectronGun();
        this.deflectionSystem = new DeflectionSystem();
        this.phosphorScreen = new PhosphorScreen();
        this.shadowMask = new ShadowMask();
    }
    
    // MUST implement complete CRT simulation
    createCRTDisplay(spec) {
        const crtDisplay = {
            // COMPLETE CRT geometry
            screenSize: spec.screenSize || 0.35, // 14 inch diagonal
            aspectRatio: spec.aspectRatio || 4/3,
            curvature: spec.curvature || 0.1, // screen curvature
            
            // COMPLETE electron gun system
            electronGuns: this.createElectronGuns(spec),
            
            // COMPLETE deflection system
            deflectionCoils: this.createDeflectionCoils(spec),
            
            // COMPLETE phosphor screen
            phosphorScreen: this.createPhosphorScreen(spec),
            
            // COMPLETE shadow mask
            shadowMask: this.createShadowMask(spec),
            
            // COMPLETE CRT properties
            properties: {
                brightness: spec.brightness || 100, // cd/m²
                contrast: spec.contrast || 100,
                refreshRate: spec.refreshRate || 60, // Hz
                persistence: spec.persistence || 16, // ms
                convergence: spec.convergence || 0.1 // mm
            },
            
            // COMPLETE rendering state
            scanPosition: { x: 0, y: 0 },
            beamIntensity: { r: 0, g: 0, b: 0 },
            lastScanTime: 0
        };
        
        return crtDisplay;
    }
    
    // MUST implement complete phosphor simulation
    createPhosphorScreen(spec) {
        const phosphorScreen = {
            phosphorType: spec.phosphorType || 'P22',
            
            // COMPLETE phosphor properties
            phosphors: {
                red: {
                    material: 'Y2O2S:Eu',
                    peakWavelength: 627, // nm
                    persistence: 1.2, // ms
                    efficiency: 0.15
                },
                green: {
                    material: 'ZnS:Cu,Al',
                    peakWavelength: 530, // nm
                    persistence: 16, // ms
                    efficiency: 0.25
                },
                blue: {
                    material: 'ZnS:Ag',
                    peakWavelength: 460, // nm
                    persistence: 0.1, // ms
                    efficiency: 0.08
                }
            },
            
            // COMPLETE phosphor layout
            phosphorDots: this.generatePhosphorDots(spec),
            
            // COMPLETE aging simulation
            agingFactors: this.calculateAgingFactors(spec)
        };
        
        return phosphorScreen;
    }
    
    // MUST implement complete electron beam simulation
    simulateElectronBeam(crtDisplay, scanline, deltaTime) {
        const electronGuns = crtDisplay.electronGuns;
        const phosphorScreen = crtDisplay.phosphorScreen;
        
        // COMPLETE beam deflection
        const deflection = this.calculateDeflection(
            crtDisplay.scanPosition,
            crtDisplay.deflectionCoils
        );
        
        // COMPLETE beam focus
        const focusedBeam = this.calculateBeamFocus(
            electronGuns,
            deflection,
            crtDisplay.properties.convergence
        );
        
        // COMPLETE phosphor excitation
        const excitation = this.calculatePhosphorExcitation(
            focusedBeam,
            phosphorScreen,
            scanline
        );
        
        // COMPLETE phosphor emission
        const emission = this.calculatePhosphorEmission(
            excitation,
            phosphorScreen.phosphors,
            deltaTime
        );
        
        // COMPLETE persistence simulation
        const persistentEmission = this.simulatePhosphorPersistence(
            emission,
            phosphorScreen.persistence,
            deltaTime
        );
        
        return persistentEmission;
    }
}
```

SHADER REQUIREMENTS:
MUST create complete display shaders:

lcd_display_vertex.glsl:
```glsl
#version 300 es
precision highp float;

in vec3 position;
in vec2 uv;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

out vec2 vUv;
out vec3 vWorldPosition;

void main() {
    vec4 worldPosition = modelMatrix * vec4(position, 1.0);
    vWorldPosition = worldPosition.xyz;
    vUv = uv;
    
    gl_Position = projectionMatrix * viewMatrix * worldPosition;
}
```

lcd_display_fragment.glsl:
```glsl
#version 300 es
precision highp float;

in vec2 vUv;
in vec3 vWorldPosition;

uniform sampler2D contentTexture;
uniform sampler2D backlightTexture;
uniform sampler2D uniformityMap;
uniform float brightness;
uniform float contrast;
uniform vec3 cameraPosition;
uniform float time;

// LCD layer properties
uniform float liquidCrystalThickness;
uniform float polarizer1Angle;
uniform float polarizer2Angle;
uniform vec3 colorFilterTransmittance;

out vec4 fragColor;

// COMPLETE LCD simulation
vec3 simulateLCD(vec2 uv, vec3 content) {
    // COMPLETE backlight simulation
    vec3 backlight = texture(backlightTexture, uv).rgb;
    float uniformity = texture(uniformityMap, uv).r;
    backlight *= uniformity;
    
    // COMPLETE polarizer simulation
    float polarizer1 = cos(polarizer1Angle);
    float polarizer2 = cos(polarizer2Angle);
    float polarization = polarizer1 * polarizer2;
    
    // COMPLETE liquid crystal modulation
    float lcModulation = content.r; // Simplified - should be per-pixel voltage
    float transmission = sin(lcModulation * 3.14159) * polarization;
    
    // COMPLETE color filter simulation
    vec3 filteredColor = content * colorFilterTransmittance;
    
    // COMPLETE final LCD output
    vec3 lcdOutput = backlight * transmission * filteredColor;
    
    return lcdOutput;
}

// COMPLETE viewing angle simulation
vec3 simulateViewingAngle(vec3 color, vec3 viewDir, vec3 normal) {
    float viewAngle = acos(dot(viewDir, normal));
    float angleFactor = cos(viewAngle);
    
    // COMPLETE color shift simulation
    vec3 colorShift = vec3(
        1.0 - 0.1 * (1.0 - angleFactor),
        1.0 - 0.05 * (1.0 - angleFactor),
        1.0 - 0.15 * (1.0 - angleFactor)
    );
    
    return color * colorShift;
}

// COMPLETE subpixel rendering
vec3 renderSubpixels(vec2 uv) {
    vec2 pixelSize = 1.0 / textureSize(contentTexture, 0);
    
    // COMPLETE subpixel sampling
    vec3 subpixelR = texture(contentTexture, uv + vec2(-pixelSize.x/3.0, 0.0)).rgb;
    vec3 subpixelG = texture(contentTexture, uv).rgb;
    vec3 subpixelB = texture(contentTexture, uv + vec2(pixelSize.x/3.0, 0.0)).rgb;
    
    return vec3(subpixelR.r, subpixelG.g, subpixelB.b);
}

void main() {
    // COMPLETE content sampling
    vec3 content = renderSubpixels(vUv);
    
    // COMPLETE LCD simulation
    vec3 lcdColor = simulateLCD(vUv, content);
    
    // COMPLETE viewing angle effects
    vec3 viewDir = normalize(cameraPosition - vWorldPosition);
    vec3 normal = vec3(0.0, 0.0, 1.0); // Display normal
    lcdColor = simulateViewingAngle(lcdColor, viewDir, normal);
    
    // COMPLETE brightness and contrast
    lcdColor = (lcdColor - 0.5) * contrast + 0.5;
    lcdColor *= brightness;
    
    fragColor = vec4(lcdColor, 1.0);
}
```

crt_display_fragment.glsl:
```glsl
#version 300 es
precision highp float;

in vec2 vUv;
in vec3 vWorldPosition;

uniform sampler2D contentTexture;
uniform float time;
uniform float refreshRate;
uniform vec3 phosphorPersistence;
uniform float scanlineIntensity;
uniform float curvature;

out vec4 fragColor;

// COMPLETE CRT curvature simulation
vec2 applyCRTCurvature(vec2 uv, float curvature) {
    vec2 centered = uv - 0.5;
    float r2 = dot(centered, centered);
    vec2 curved = centered * (1.0 + curvature * r2);
    return curved + 0.5;
}

// COMPLETE phosphor persistence simulation
vec3 simulatePhosphorPersistence(vec3 color, vec2 uv, float time) {
    // COMPLETE persistence calculation
    float timeSinceExcitation = mod(time * refreshRate, 1.0);
    
    vec3 persistence = exp(-timeSinceExcitation / phosphorPersistence);
    
    return color * persistence;
}

// COMPLETE scanline simulation
float simulateScanlines(vec2 uv, float time) {
    float scanline = sin(uv.y * 800.0) * 0.04;
    float scanlineMovement = sin(time * refreshRate * 2.0 * 3.14159) * 0.02;
    
    return 1.0 - (scanline + scanlineMovement) * scanlineIntensity;
}

// COMPLETE electron beam simulation
vec3 simulateElectronBeam(vec2 uv, float time) {
    // COMPLETE beam position calculation
    float beamY = mod(time * refreshRate, 1.0);
    float beamDistance = abs(uv.y - beamY);
    
    // COMPLETE beam intensity
    float beamIntensity = exp(-beamDistance * 50.0);
    
    return vec3(beamIntensity);
}

void main() {
    // COMPLETE CRT curvature
    vec2 curvedUV = applyCRTCurvature(vUv, curvature);
    
    // Check if UV is within screen bounds
    if (curvedUV.x < 0.0 || curvedUV.x > 1.0 || curvedUV.y < 0.0 || curvedUV.y > 1.0) {
        fragColor = vec4(0.0, 0.0, 0.0, 1.0);
        return;
    }
    
    // COMPLETE content sampling
    vec3 content = texture(contentTexture, curvedUV).rgb;
    
    // COMPLETE phosphor simulation
    vec3 phosphorColor = simulatePhosphorPersistence(content, curvedUV, time);
    
    // COMPLETE scanline effects
    float scanlineFactor = simulateScanlines(curvedUV, time);
    phosphorColor *= scanlineFactor;
    
    // COMPLETE electron beam effects
    vec3 beamEffect = simulateElectronBeam(curvedUV, time);
    phosphorColor += beamEffect * 0.1;
    
    fragColor = vec4(phosphorColor, 1.0);
}
```

VALIDATION REQUIREMENTS:
CURSOR MUST verify after implementation:
✓ All display types render correctly
✓ Text rendering is ultra-sharp and clear
✓ LCD simulation shows proper backlight uniformity
✓ OLED displays have true black levels
✓ CRT displays show realistic phosphor persistence
✓ Viewing angle effects are accurate
✓ Performance remains above 45 FPS
✓ All display shaders compile without errors

PERFORMANCE BENCHMARKS (MUST ACHIEVE):
✓ Display rendering: <3ms per display per frame
✓ Text rendering: <1ms per text element
✓ Subpixel rendering: <0.5ms additional overhead
✓ CRT simulation: <2ms per CRT display
✓ LCD simulation: <1.5ms per LCD display
✓ OLED simulation: <1ms per OLED display
```

**GAP IDENTIFICATION FOR PHASE 4.1**:
```
CURSOR MUST CHECK FOR THESE CRITICAL GAPS:
❌ Poor display physics reducing realism
❌ Inadequate text rendering quality
❌ Missing subpixel rendering causing blurry text
❌ Poor backlight simulation breaking LCD realism
❌ Missing phosphor persistence in CRT displays
❌ Inadequate viewing angle simulation
❌ Performance issues with complex display rendering
❌ Missing color accuracy calibration
❌ Poor contrast and brightness control
❌ Inadequate display aging simulation
```

## Prompt 4.2: Real-Time Avionics Data Simulation

**PREREQUISITE VALIDATION**:
```
CURSOR MUST VERIFY FROM PHASE 4.1:
✓ Display systems render with photorealistic quality
✓ Text rendering is ultra-sharp and clear
✓ All display types (LCD/OLED/CRT) work correctly
✓ Subpixel rendering enhances text clarity
✓ Performance benchmarks are met
✓ All display shaders compile without errors
```

**CURSOR RULES FOR THIS PROMPT**:
1. MUST implement convincing real-time avionics data that behaves like actual aircraft systems
2. ALL flight data must be based on real aircraft physics and performance
3. MUST support realistic system failures and emergency procedures
4. Data accuracy must be sufficient for training applications

**DETAILED IMPLEMENTATION**:
```
Create convincing real-time avionics data that behaves like actual aircraft systems:

MANDATORY AVIONICS DATA SYSTEMS:

1. FLIGHT DATA SIMULATION (COMPLETE IMPLEMENTATION):
   FlightDataSystem.js MUST implement:

   AIRCRAFT DYNAMICS:
   - MUST implement proper aircraft dynamics model with 6-DOF motion
   - MUST create realistic atmospheric conditions with proper physics
   - MUST build proper navigation calculations with GPS/INS fusion
   - MUST implement realistic autopilot behavior and control laws
   - MUST create proper engine performance modeling
   - MUST build realistic fuel consumption and weight/balance calculations

   SENSOR SIMULATION:
   - MUST implement realistic sensor noise and drift
   - MUST create proper sensor failure modes
   - MUST build realistic sensor update rates
   - MUST implement proper sensor fusion algorithms
   - MUST create environmental effects on sensors

2. PRIMARY FLIGHT DISPLAY (COMPLETE IMPLEMENTATION):
   PrimaryFlightDisplay.js MUST implement:

   FLIGHT INSTRUMENTS:
   - Attitude indicator with proper gyroscopic behavior and precession
   - Altimeter with barometric and radar altitude sources
   - Airspeed indicator with proper pitot-static system modeling
   - Heading indicator with magnetic variation and deviation
   - Vertical speed indicator with proper dampening and response
   - Flight path vector with proper ground track calculation

3. NAVIGATION DISPLAY (COMPLETE IMPLEMENTATION):
   NavigationDisplay.js MUST implement:

   NAVIGATION SYSTEMS:
   - Moving map with proper projection and scaling
   - Waypoint navigation with bearing and distance calculations
   - Weather radar simulation with realistic precipitation patterns
   - Traffic display with TCAS resolution advisories
   - Terrain awareness with proper ground proximity warnings
   - Route planning with proper great circle calculations

COMPLETE IMPLEMENTATION REQUIREMENTS:

FlightDataSystem.js MUST implement:
```javascript
class FlightDataSystem {
    constructor() {
        // COMPLETE aircraft model
        this.aircraftModel = new AircraftModel();
        this.atmosphereModel = new AtmosphereModel();
        this.engineModel = new EngineModel();
        this.fuelSystem = new FuelSystem();
        
        // COMPLETE navigation systems
        this.gpsSystem = new GPSSystem();
        this.insSystem = new INSSystem();
        this.navigationComputer = new NavigationComputer();
        
        // COMPLETE sensor systems
        this.airDataSystem = new AirDataSystem();
        this.attitudeSystem = new AttitudeSystem();
        this.magneticSystem = new MagneticSystem();
        
        // COMPLETE flight state
        this.flightState = this.initializeFlightState();
        
        this.initializeAvionicsData();
    }
    
    // MUST implement complete flight state update
    updateFlightData(deltaTime) {
        // COMPLETE atmospheric conditions
        const atmosphere = this.updateAtmosphericConditions();
        
        // COMPLETE aircraft dynamics
        const forces = this.calculateForces(this.flightState, atmosphere);
        const moments = this.calculateMoments(this.flightState, atmosphere);
        
        // COMPLETE 6-DOF integration
        const newState = this.integrate6DOF(
            this.flightState,
            forces,
            moments,
            deltaTime
        );
        
        // COMPLETE sensor updates
        this.updateSensors(newState, atmosphere, deltaTime);
        
        // COMPLETE navigation updates
        this.updateNavigation(newState, deltaTime);
        
        // COMPLETE system updates
        this.updateSystems(newState, deltaTime);
        
        this.flightState = newState;
        
        return this.flightState;
    }
    
    // MUST implement complete aircraft dynamics
    calculateForces(state, atmosphere) {
        const forces = {
            thrust: this.calculateThrust(state),
            drag: this.calculateDrag(state, atmosphere),
            lift: this.calculateLift(state, atmosphere),
            weight: this.calculateWeight(state),
            sideForce: this.calculateSideForce(state, atmosphere)
        };
        
        // COMPLETE force summation in body frame
        const totalForces = {
            x: forces.thrust - forces.drag,
            y: forces.sideForce,
            z: forces.lift - forces.weight * Math.cos(state.attitude.pitch)
        };
        
        return totalForces;
    }
    
    // MUST implement complete moment calculations
    calculateMoments(state, atmosphere) {
        const moments = {
            roll: this.calculateRollMoment(state, atmosphere),
            pitch: this.calculatePitchMoment(state, atmosphere),
            yaw: this.calculateYawMoment(state, atmosphere)
        };
        
        return moments;
    }
    
    // MUST implement complete 6-DOF integration
    integrate6DOF(state, forces, moments, deltaTime) {
        const newState = { ...state };
        
        // COMPLETE translational motion
        const acceleration = {
            x: forces.x / this.aircraftModel.mass,
            y: forces.y / this.aircraftModel.mass,
            z: forces.z / this.aircraftModel.mass
        };
        
        newState.velocity.x += acceleration.x * deltaTime;
        newState.velocity.y += acceleration.y * deltaTime;
        newState.velocity.z += acceleration.z * deltaTime;
        
        newState.position.x += newState.velocity.x * deltaTime;
        newState.position.y += newState.velocity.y * deltaTime;
        newState.position.z += newState.velocity.z * deltaTime;
        
        // COMPLETE rotational motion
        const angularAcceleration = {
            roll: moments.roll / this.aircraftModel.inertia.xx,
            pitch: moments.pitch / this.aircraftModel.inertia.yy,
            yaw: moments.yaw / this.aircraftModel.inertia.zz
        };
        
        newState.angularVelocity.roll += angularAcceleration.roll * deltaTime;
        newState.angularVelocity.pitch += angularAcceleration.pitch * deltaTime;
        newState.angularVelocity.yaw += angularAcceleration.yaw * deltaTime;
        
        newState.attitude.roll += newState.angularVelocity.roll * deltaTime;
        newState.attitude.pitch += newState.angularVelocity.pitch * deltaTime;
        newState.attitude.yaw += newState.angularVelocity.yaw * deltaTime;
        
        return newState;
    }
}

class PrimaryFlightDisplay {
    constructor(displaySystem) {
        this.displaySystem = displaySystem;
        
        // COMPLETE flight instruments
        this.attitudeIndicator = new AttitudeIndicator();
        this.altimeter = new Altimeter();
        this.airspeedIndicator = new AirspeedIndicator();
        this.headingIndicator = new HeadingIndicator();
        this.verticalSpeedIndicator = new VerticalSpeedIndicator();
        this.flightPathVector = new FlightPathVector();
        
        // COMPLETE display elements
        this.displayCanvas = this.createDisplayCanvas();
        this.symbologyRenderer = new SymbologyRenderer();
        
        this.initializePFD();
    }
    
    // MUST implement complete PFD rendering
    renderPFD(flightData) {
        // COMPLETE display clearing
        this.clearDisplay();
        
        // COMPLETE attitude indicator
        this.renderAttitudeIndicator(flightData.attitude);
        
        // COMPLETE airspeed indicator
        this.renderAirspeedIndicator(flightData.airspeed);
        
        // COMPLETE altimeter
        this.renderAltimeter(flightData.altitude);
        
        // COMPLETE heading indicator
        this.renderHeadingIndicator(flightData.heading);
        
        // COMPLETE vertical speed indicator
        this.renderVerticalSpeedIndicator(flightData.verticalSpeed);
        
        // COMPLETE flight path vector
        this.renderFlightPathVector(flightData.flightPath);
        
        // COMPLETE warning and caution displays
        this.renderWarningsAndCautions(flightData.warnings);
        
        // COMPLETE display update
        this.updateDisplay();
    }
    
    // MUST implement complete attitude indicator
    renderAttitudeIndicator(attitudeData) {
        const canvas = this.displayCanvas;
        const ctx = canvas.getContext('2d');
        
        // COMPLETE attitude sphere
        const centerX = canvas.width / 2;
        const centerY = canvas.height / 2;
        const radius = Math.min(canvas.width, canvas.height) * 0.3;
        
        ctx.save();
        ctx.translate(centerX, centerY);
        ctx.rotate(attitudeData.roll * Math.PI / 180);
        
        // COMPLETE sky and ground
        const pitchOffset = attitudeData.pitch * radius / 90;
        
        // Sky (blue)
        ctx.fillStyle = '#4A90E2';
        ctx.fillRect(-radius, -radius - pitchOffset, radius * 2, radius + pitchOffset);
        
        // Ground (brown)
        ctx.fillStyle = '#8B4513';
        ctx.fillRect(-radius, -pitchOffset, radius * 2, radius + pitchOffset);
        
        // COMPLETE pitch lines
        this.renderPitchLines(ctx, attitudeData.pitch, radius);
        
        ctx.restore();
        
        // COMPLETE aircraft symbol
        this.renderAircraftSymbol(ctx, centerX, centerY);
        
        // COMPLETE roll pointer
        this.renderRollPointer(ctx, centerX, centerY, attitudeData.roll, radius);
    }
    
    // MUST implement complete airspeed indicator
    renderAirspeedIndicator(airspeedData) {
        const canvas = this.displayCanvas;
        const ctx = canvas.getContext('2d');
        
        // COMPLETE airspeed tape
        const tapeX = 50;
        const tapeY = 100;
        const tapeHeight = canvas.height - 200;
        const tapeWidth = 80;
        
        // COMPLETE speed range calculation
        const currentSpeed = airspeedData.indicated;
        const minSpeed = Math.floor((currentSpeed - 100) / 10) * 10;
        const maxSpeed = Math.ceil((currentSpeed + 100) / 10) * 10;
        
        // COMPLETE tape background
        ctx.fillStyle = 'rgba(0, 0, 0, 0.8)';
        ctx.fillRect(tapeX, tapeY, tapeWidth, tapeHeight);
        
        // COMPLETE speed markings
        for (let speed = minSpeed; speed <= maxSpeed; speed += 10) {
            const y = tapeY + tapeHeight * (maxSpeed - speed) / (maxSpeed - minSpeed);
            
            ctx.strokeStyle = '#FFFFFF';
            ctx.lineWidth = 1;
            ctx.beginPath();
            ctx.moveTo(tapeX + tapeWidth - 20, y);
            ctx.lineTo(tapeX + tapeWidth, y);
            ctx.stroke();
            
            // COMPLETE speed labels
            if (speed % 20 === 0) {
                ctx.fillStyle = '#FFFFFF';
                ctx.font = '12px monospace';
                ctx.textAlign = 'right';
                ctx.fillText(speed.toString(), tapeX + tapeWidth - 25, y + 4);
            }
        }
        
        // COMPLETE current speed indicator
        const currentY = tapeY + tapeHeight * (maxSpeed - currentSpeed) / (maxSpeed - minSpeed);
        
        ctx.fillStyle = '#00FF00';
        ctx.fillRect(tapeX + tapeWidth, currentY - 10, 60, 20);
        
        ctx.fillStyle = '#000000';
        ctx.font = '14px monospace';
        ctx.textAlign = 'center';
        ctx.fillText(Math.round(currentSpeed).toString(), tapeX + tapeWidth + 30, currentY + 4);
        
        // COMPLETE speed trend vector
        if (airspeedData.trend !== 0) {
            const trendLength = airspeedData.trend * 10; // 10 pixels per knot/second
            ctx.strokeStyle = '#FFFF00';
            ctx.lineWidth = 2;
            ctx.beginPath();
            ctx.moveTo(tapeX + tapeWidth + 60, currentY);
            ctx.lineTo(tapeX + tapeWidth + 60, currentY - trendLength);
            ctx.stroke();
        }
    }
}

class NavigationDisplay {
    constructor(displaySystem) {
        this.displaySystem = displaySystem;
        
        // COMPLETE navigation systems
        this.mapRenderer = new MapRenderer();
        this.waypointSystem = new WaypointSystem();
        this.weatherRadar = new WeatherRadar();
        this.trafficSystem = new TrafficSystem();
        this.terrainSystem = new TerrainSystem();
        
        // COMPLETE display properties
        this.mapRange = 50; // nautical miles
        this.mapMode = 'PLAN'; // PLAN, ARC, ROSE
        this.displayMode = 'NAV'; // NAV, WXR, TCAS, TERR
        
        this.initializeNavigationDisplay();
    }
    
    // MUST implement complete navigation display
    renderNavigationDisplay(navigationData) {
        // COMPLETE display clearing
        this.clearDisplay();
        
        // COMPLETE map rendering
        this.renderMap(navigationData);
        
        // COMPLETE waypoint rendering
        this.renderWaypoints(navigationData.waypoints);
        
        // COMPLETE route rendering
        this.renderRoute(navigationData.route);
        
        // COMPLETE aircraft position
        this.renderAircraftPosition(navigationData.position);
        
        // COMPLETE range and bearing information
        this.renderRangeAndBearing(navigationData);
        
        // COMPLETE mode-specific overlays
        switch (this.displayMode) {
            case 'WXR':
                this.renderWeatherRadar(navigationData.weather);
                break;
            case 'TCAS':
                this.renderTraffic(navigationData.traffic);
                break;
            case 'TERR':
                this.renderTerrain(navigationData.terrain);
                break;
        }
        
        // COMPLETE display update
        this.updateDisplay();
    }
    
    // MUST implement complete weather radar simulation
    renderWeatherRadar(weatherData) {
        const canvas = this.displayCanvas;
        const ctx = canvas.getContext('2d');
        
        // COMPLETE weather cell rendering
        for (const cell of weatherData.cells) {
            const screenPos = this.worldToScreen(cell.position);
            const intensity = cell.intensity; // 0-1 scale
            
            // COMPLETE intensity color mapping
            let color;
            if (intensity < 0.2) {
                color = '#00FF00'; // Green - light precipitation
            } else if (intensity < 0.5) {
                color = '#FFFF00'; // Yellow - moderate precipitation
            } else if (intensity < 0.8) {
                color = '#FF8000'; // Orange - heavy precipitation
            } else {
                color = '#FF0000'; // Red - severe precipitation
            }
            
            // COMPLETE weather cell shape
            const cellRadius = cell.size * this.getPixelsPerNauticalMile();
            
            ctx.fillStyle = color;
            ctx.globalAlpha = 0.6;
            ctx.beginPath();
            ctx.arc(screenPos.x, screenPos.y, cellRadius, 0, 2 * Math.PI);
            ctx.fill();
            ctx.globalAlpha = 1.0;
        }
        
        // COMPLETE radar sweep animation
        this.renderRadarSweep(ctx);
    }
    
    // MUST implement complete traffic display
    renderTraffic(trafficData) {
        const canvas = this.displayCanvas;
        const ctx = canvas.getContext('2d');
        
        for (const traffic of trafficData.contacts) {
            const screenPos = this.worldToScreen(traffic.position);
            
            // COMPLETE traffic symbol
            let symbol, color;
            
            switch (traffic.threatLevel) {
                case 'TRAFFIC_ADVISORY':
                    symbol = '◊';
                    color = '#FFFF00';
                    break;
                case 'RESOLUTION_ADVISORY':
                    symbol = '■';
                    color = '#FF0000';
                    break;
                default:
                    symbol = '◊';
                    color = '#00FFFF';
            }
            
            // COMPLETE symbol rendering
            ctx.fillStyle = color;
            ctx.font = '16px monospace';
            ctx.textAlign = 'center';
            ctx.fillText(symbol, screenPos.x, screenPos.y);
            
            // COMPLETE altitude and trend information
            const altitudeText = `${Math.round(traffic.altitude / 100)}`;
            const trendArrow = traffic.verticalRate > 100 ? '↑' : 
                             traffic.verticalRate < -100 ? '↓' : '';
            
            ctx.font = '10px monospace';
            ctx.fillText(altitudeText + trendArrow, screenPos.x, screenPos.y + 20);
        }
    }
}

class EngineDisplay {
    constructor(displaySystem) {
        this.displaySystem = displaySystem;
        
        // COMPLETE engine parameters
        this.engineParameters = [
            'N1', 'N2', 'EGT', 'FF', 'OIL_PRESS', 'OIL_TEMP'
        ];
        
        this.initializeEngineDisplay();
    }
    
    // MUST implement complete engine display
    renderEngineDisplay(engineData) {
        const canvas = this.displayCanvas;
        const ctx = canvas.getContext('2d');
        
        // COMPLETE engine parameter display
        for (let i = 0; i < engineData.engines.length; i++) {
            const engine = engineData.engines[i];
            const x = 100 + i * 200;
            
            // COMPLETE N1 display
            this.renderN1Gauge(ctx, x, 100, engine.n1);
            
            // COMPLETE N2 display
            this.renderN2Gauge(ctx, x, 200, engine.n2);
            
            // COMPLETE EGT display
            this.renderEGTGauge(ctx, x, 300, engine.egt);
            
            // COMPLETE fuel flow display
            this.renderFuelFlowGauge(ctx, x, 400, engine.fuelFlow);
            
            // COMPLETE oil parameters
            this.renderOilParameters(ctx, x, 500, engine.oil);
        }
        
        // COMPLETE engine warnings
        this.renderEngineWarnings(ctx, engineData.warnings);
    }
}
```

VALIDATION REQUIREMENTS:
CURSOR MUST verify after implementation:
✓ All avionics data behaves realistically
✓ Flight instruments respond correctly to aircraft state
✓ Navigation systems provide accurate information
✓ Weather radar shows realistic precipitation patterns
✓ Traffic display shows proper threat levels
✓ Engine parameters reflect realistic values
✓ System failures are handled appropriately
✓ Performance remains above 45 FPS

PERFORMANCE BENCHMARKS (MUST ACHIEVE):
✓ Flight data updates: <2ms per frame
✓ PFD rendering: <3ms per frame
✓ Navigation display: <4ms per frame
✓ Weather radar: <2ms per frame
✓ Traffic display: <1ms per frame
✓ Engine display: <2ms per frame
```

**GAP IDENTIFICATION FOR PHASE 4.2**:
```
CURSOR MUST CHECK FOR THESE CRITICAL GAPS:
❌ Unrealistic flight data reducing training value
❌ Poor instrument response breaking immersion
❌ Inaccurate navigation calculations
❌ Unrealistic weather radar patterns
❌ Poor traffic display functionality
❌ Missing system failure simulation
❌ Inadequate sensor modeling
❌ Poor autopilot behavior
❌ Missing emergency procedures
❌ Inadequate fuel system modeling
```

## Prompt 4.3: Advanced HUD System Implementation

**PREREQUISITE VALIDATION**:
```
CURSOR MUST VERIFY FROM PHASE 4.2:
✓ Avionics data systems provide realistic flight information
✓ All flight instruments respond correctly
✓ Navigation systems work accurately
✓ Weather and traffic displays are functional
✓ Engine displays show realistic parameters
✓ Performance benchmarks are met
```

**CURSOR RULES FOR THIS PROMPT**:
1. MUST implement military-specification HUD system with extreme realism
2. ALL HUD symbology must conform to military standards
3. MUST support proper optical simulation with realistic limitations
4. HUD quality must be indistinguishable from real military HUD systems

**DETAILED IMPLEMENTATION**:
```
Create a military-specification HUD system with extreme realism:

MANDATORY HUD SYSTEM COMPONENTS:

1. HUD OPTICS SIMULATION (COMPLETE IMPLEMENTATION):
   HUDOpticsSystem.js MUST implement:

   COLLIMATED DISPLAY:
   - MUST implement proper collimated light projection with infinite focus
   - MUST create realistic combiner glass optical properties
   - MUST build proper field-of-view calculations (typically 20° × 30°)
   - MUST implement brightness adaptation for varying light conditions
   - MUST create realistic ghosting and multiple reflection effects
   - MUST build proper optical distortion at field-of-view edges

   OPTICAL PHYSICS:
   - MUST implement proper waveguide optics simulation
   - MUST create realistic beam splitter characteristics
   - MUST build proper angular reflection properties
   - MUST implement temperature compensation for optical alignment
   - MUST create realistic optical aberrations

2. MILITARY HUD SYMBOLOGY (COMPLETE IMPLEMENTATION):
   HUDSymbology.js MUST implement:

   FLIGHT SYMBOLOGY:
   - Flight path vector with proper lateral and vertical deviation
   - Velocity vector with ground track and drift correction
   - Altitude and airspeed scales with proper graduation
   - Heading scale with magnetic/true bearing selection
   - Angle of attack and sideslip indicators
   - G-force and load factor displays

   WEAPON SYMBOLOGY:
   - Weapon aiming symbols with proper ballistics calculation
   - Target designation and tracking symbols
   - Weapon status and selection indicators
   - Range and bearing to target
   - Time to impact calculations
   - Weapon envelope displays

3. ADVANCED HUD FEATURES (COMPLETE IMPLEMENTATION):
   AdvancedHUDFeatures.js MUST implement:

   OPERATIONAL MODES:
   - Night vision goggle (NVG) compatibility with green phosphor simulation
   - Declutter modes for reduced symbol density
   - Emergency backup modes with essential flight information only
   - Landing mode with approach guidance
   - Air-to-air mode with combat symbology
   - Air-to-ground mode with targeting information

COMPLETE IMPLEMENTATION REQUIREMENTS:

HUDSystem.js MUST implement:
```javascript
class HUDSystem {
    constructor(renderer, displaySystem, flightDataSystem) {
        this.renderer = renderer;
        this.displaySystem = displaySystem;
        this.flightDataSystem = flightDataSystem;
        
        // COMPLETE HUD optics
        this.hudOptics = new HUDOptics();
        this.combinerGlass = new CombinerGlass();
        this.projectionSystem = new ProjectionSystem();
        
        // COMPLETE symbology systems
        this.flightSymbology = new FlightSymbology();
        this.weaponSymbology = new WeaponSymbology();
        this.navigationSymbology = new NavigationSymbology();
        this.systemSymbology = new SystemSymbology();
        
        // COMPLETE HUD modes
        this.hudModes = new HUDModes();
        this.declutterSystem = new DeclutterSystem();
        
        // COMPLETE HUD state
        this.hudState = this.initializeHUDState();
        
        this.initializeHUD();
    }
    
    // MUST implement complete HUD rendering
    renderHUD(flightData, weaponData, navigationData) {
        // COMPLETE HUD clearing
        this.clearHUD();
        
        // COMPLETE mode-specific rendering
        switch (this.hudState.currentMode) {
            case 'NAV':
                this.renderNavigationMode(flightData, navigationData);
                break;
            case 'A2A':
                this.renderAirToAirMode(flightData, weaponData);
                break;
            case 'A2G':
                this.renderAirToGroundMode(flightData, weaponData);
                break;
            case 'LANDING':
                this.renderLandingMode(flightData, navigationData);
                break;
            case 'EMERGENCY':
                this.renderEmergencyMode(flightData);
                break;
        }
        
        // COMPLETE declutter application
        this.applyDeclutter();
        
        // COMPLETE optical effects
        this.applyOpticalEffects();
        
        // COMPLETE HUD update
        this.updateHUD();
    }
    
    // MUST implement complete navigation mode
    renderNavigationMode(flightData, navigationData) {
        // COMPLETE flight path vector
        this.renderFlightPathVector(flightData.flightPath);
        
        // COMPLETE velocity vector
        this.renderVelocityVector(flightData.velocity);
        
        // COMPLETE altitude ladder
        this.renderAltitudeLadder(flightData.altitude);
        
        // COMPLETE airspeed scale
        this.renderAirspeedScale(flightData.airspeed);
        
        // COMPLETE heading scale
        this.renderHeadingScale(flightData.heading);
        
        // COMPLETE navigation information
        this.renderNavigationInfo(navigationData);
        
        // COMPLETE flight director
        if (flightData.autopilot.engaged) {
            this.renderFlightDirector(flightData.autopilot);
        }
    }
    
    // MUST implement complete flight path vector
    renderFlightPathVector(flightPathData) {
        const fpv = this.calculateFPVPosition(flightPathData);
        
        // COMPLETE FPV symbol
        const fpvSymbol = {
            center: fpv.position,
            radius: 15, // pixels
            crossLength: 30, // pixels
            color: '#00FF00'
        };
        
        // COMPLETE FPV rendering
        this.drawCircle(fpvSymbol.center, fpvSymbol.radius, fpvSymbol.color);
        this.drawCross(fpvSymbol.center, fpvSymbol.crossLength, fpvSymbol.color);
        
        // COMPLETE lateral deviation
        if (Math.abs(flightPathData.lateralDeviation) > 0.1) {
            const deviationLine = {
                start: { x: fpv.position.x - 50, y: fpv.position.y },
                end: { x: fpv.position.x + 50, y: fpv.position.y },
                offset: flightPathData.lateralDeviation * 100, // pixels per degree
                color: '#FFFF00'
            };
            
            this.drawDeviationLine(deviationLine);
        }
        
        // COMPLETE vertical deviation
        if (Math.abs(flightPathData.verticalDeviation) > 0.1) {
            const deviationLine = {
                start: { x: fpv.position.x, y: fpv.position.y - 50 },
                end: { x: fpv.position.x, y: fpv.position.y + 50 },
                offset: flightPathData.verticalDeviation * 100, // pixels per degree
                color: '#FFFF00'
            };
            
            this.drawDeviationLine(deviationLine);
        }
    }
    
    // MUST implement complete altitude ladder
    renderAltitudeLadder(altitudeData) {
        const currentAltitude = altitudeData.barometric;
        const centerX = this.hudState.fieldOfView.width * 0.8;
        const centerY = this.hudState.fieldOfView.height * 0.5;
        
        // COMPLETE altitude range
        const altitudeRange = 1000; // feet above and below current
        const pixelsPerFoot = 0.5;
        
        // COMPLETE major altitude lines (every 500 feet)
        for (let alt = Math.floor((currentAltitude - altitudeRange) / 500) * 500;
             alt <= currentAltitude + altitudeRange;
             alt += 500) {
            
            const y = centerY - (alt - currentAltitude) * pixelsPerFoot;
            
            // COMPLETE altitude line
            this.drawLine(
                { x: centerX - 30, y: y },
                { x: centerX + 30, y: y },
                '#FFFFFF',
                2
            );
            
            // COMPLETE altitude label
            this.drawText(
                alt.toString(),
                { x: centerX + 40, y: y + 5 },
                '#FFFFFF',
                '14px monospace'
            );
        }
        
        // COMPLETE minor altitude lines (every 100 feet)
        for (let alt = Math.floor((currentAltitude - altitudeRange) / 100) * 100;
             alt <= currentAltitude + altitudeRange;
             alt += 100) {
            
            if (alt % 500 !== 0) { // Skip major lines
                const y = centerY - (alt - currentAltitude) * pixelsPerFoot;
                
                this.drawLine(
                    { x: centerX - 15, y: y },
                    { x: centerX + 15, y: y },
                    '#FFFFFF',
                    1
                );
            }
        }
        
        // COMPLETE current altitude indicator
        this.drawRectangle(
            { x: centerX - 40, y: centerY - 15 },
            { width: 80, height: 30 },
            '#000000',
            '#00FF00'
        );
        
        this.drawText(
            Math.round(currentAltitude).toString(),
            { x: centerX, y: centerY + 5 },
            '#000000',
            '16px monospace',
            'center'
        );
        
        // COMPLETE altitude trend vector
        if (altitudeData.trend !== 0) {
            const trendLength = altitudeData.trend * 0.1; // pixels per fpm
            this.drawLine(
                { x: centerX + 50, y: centerY },
                { x: centerX + 50, y: centerY - trendLength },
                '#FFFF00',
                3
            );
        }
    }
    
    // MUST implement complete weapon symbology
    renderWeaponSymbology(weaponData) {
        if (!weaponData.selectedWeapon) return;
        
        const weapon = weaponData.selectedWeapon;
        
        // COMPLETE weapon status
        this.renderWeaponStatus(weapon);
        
        // COMPLETE aiming reticle
        this.renderAimingReticle(weapon, weaponData.target);
        
        // COMPLETE weapon envelope
        this.renderWeaponEnvelope(weapon, weaponData.target);
        
        // COMPLETE target information
        if (weaponData.target) {
            this.renderTargetInformation(weaponData.target);
        }
    }
    
    // MUST implement complete aiming reticle
    renderAimingReticle(weapon, target) {
        const reticleCenter = this.calculateAimingPoint(weapon, target);
        
        switch (weapon.type) {
            case 'GUN':
                this.renderGunReticle(reticleCenter, weapon);
                break;
            case 'MISSILE':
                this.renderMissileReticle(reticleCenter, weapon);
                break;
            case 'BOMB':
                this.renderBombReticle(reticleCenter, weapon);
                break;
        }
    }
    
    // MUST implement complete gun reticle
    renderGunReticle(center, weapon) {
        // COMPLETE gun cross
        const crossSize = 20;
        this.drawLine(
            { x: center.x - crossSize, y: center.y },
            { x: center.x + crossSize, y: center.y },
            '#00FF00',
            2
        );
        this.drawLine(
            { x: center.x, y: center.y - crossSize },
            { x: center.x, y: center.y + crossSize },
            '#00FF00',
            2
        );
        
        // COMPLETE range circle
        const rangeCircleRadius = this.calculateRangeCircleRadius(weapon);
        this.drawCircle(center, rangeCircleRadius, '#00FF00', false);
        
        // COMPLETE bullet impact point
        const impactPoint = this.calculateBulletImpactPoint(weapon);
        this.drawCircle(impactPoint, 5, '#FFFF00');
        
        // COMPLETE gun status
        this.drawText(
            `${weapon.ammunition} RDS`,
            { x: center.x + 30, y: center.y - 20 },
            '#00FF00',
            '12px monospace'
        );
    }
}

class HUDOptics {
    constructor() {
        this.combinerAngle = 60; // degrees
        this.fieldOfView = { horizontal: 20, vertical: 30 }; // degrees
        this.collimationDistance = Infinity; // meters
        this.brightness = 0.8; // 0-1 scale
        
        // COMPLETE optical properties
        this.opticalProperties = {
            transmittance: 0.85,
            reflectance: 0.15,
            ior: 1.52, // index of refraction
            dispersion: 0.02 // chromatic dispersion
        };
        
        this.initializeOptics();
    }
    
    // MUST implement complete optical simulation
    simulateHUDOptics(symbologyImage, viewingAngle, ambientLight) {
        // COMPLETE brightness adaptation
        const adaptedBrightness = this.calculateAdaptedBrightness(
            this.brightness,
            ambientLight
        );
        
        // COMPLETE optical distortion
        const distortedImage = this.applyOpticalDistortion(
            symbologyImage,
            viewingAngle
        );
        
        // COMPLETE ghosting effects
        const ghostedImage = this.applyGhostingEffects(
            distortedImage,
            this.opticalProperties
        );
        
        // COMPLETE chromatic aberration
        const chromaticImage = this.applyChromaticAberration(
            ghostedImage,
            this.opticalProperties.dispersion
        );
        
        // COMPLETE final brightness application
        const finalImage = this.applyBrightness(chromaticImage, adaptedBrightness);
        
        return finalImage;
    }
    
    // MUST implement complete brightness adaptation
    calculateAdaptedBrightness(hudBrightness, ambientLight) {
        // COMPLETE automatic brightness control
        const targetContrast = 3.0; // minimum contrast ratio
        const requiredBrightness = ambientLight * targetContrast;
        
        // COMPLETE brightness limits
        const minBrightness = 0.1;
        const maxBrightness = 1.0;
        
        const adaptedBrightness = Math.max(
            minBrightness,
            Math.min(maxBrightness, requiredBrightness)
        );
        
        return adaptedBrightness;
    }
    
    // MUST implement complete optical distortion
    applyOpticalDistortion(image, viewingAngle) {
        // COMPLETE field-of-view distortion
        const distortionFactor = this.calculateDistortionFactor(viewingAngle);
        
        // COMPLETE barrel/pincushion distortion
        const distortedImage = this.applyBarrelDistortion(image, distortionFactor);
        
        return distortedImage;
    }
}

class HUDModes {
    constructor() {
        this.modes = {
            NAV: new NavigationMode(),
            A2A: new AirToAirMode(),
            A2G: new AirToGroundMode(),
            LANDING: new LandingMode(),
            EMERGENCY: new EmergencyMode()
        };
        
        this.currentMode = 'NAV';
        this.declutterLevel = 0; // 0-3 scale
    }
    
    // MUST implement complete mode switching
    switchMode(newMode, flightData) {
        if (!this.modes[newMode]) {
            throw new Error(`Invalid HUD mode: ${newMode}`);
        }
        
        // COMPLETE mode transition
        this.modes[this.currentMode].exit();
        this.currentMode = newMode;
        this.modes[this.currentMode].enter(flightData);
        
        // COMPLETE mode-specific configuration
        this.configureForMode(newMode);
    }
    
    // MUST implement complete declutter system
    applyDeclutter(symbologyList) {
        const declutteredSymbology = [];
        
        for (const symbol of symbologyList) {
            if (symbol.priority <= this.declutterLevel) {
                declutteredSymbology.push(symbol);
            }
        }
        
        return declutteredSymbology;
    }
}
```

SHADER REQUIREMENTS:
MUST create complete HUD shaders:

hud_vertex.glsl:
```glsl
#version 300 es
precision highp float;

in vec3 position;
in vec2 uv;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;
uniform float combinerAngle;

out vec2 vUv;
out vec3 vWorldPosition;
out float vCombinerFactor;

void main() {
    vec4 worldPosition = modelMatrix * vec4(position, 1.0);
    vWorldPosition = worldPosition.xyz;
    vUv = uv;
    
    // COMPLETE combiner glass angle calculation
    vec3 viewDirection = normalize((inverse(viewMatrix) * vec4(0.0, 0.0, 0.0, 1.0)).xyz - worldPosition.xyz);
    vec3 combinerNormal = vec3(sin(radians(combinerAngle)), 0.0, cos(radians(combinerAngle)));
    vCombinerFactor = max(0.0, dot(viewDirection, combinerNormal));
    
    gl_Position = projectionMatrix * viewMatrix * worldPosition;
}
```

hud_fragment.glsl:
```glsl
#version 300 es
precision highp float;

in vec2 vUv;
in vec3 vWorldPosition;
in float vCombinerFactor;

uniform sampler2D hudSymbology;
uniform float brightness;
uniform float ambientLight;
uniform vec3 hudColor;
uniform float ghostingIntensity;
uniform float chromaticAberration;

out vec4 fragColor;

// COMPLETE HUD symbology rendering
vec3 renderHUDSymbology(vec2 uv) {
    vec4 symbology = texture(hudSymbology, uv);
    return symbology.rgb * symbology.a;
}

// COMPLETE ghosting effects
vec3 applyGhosting(vec3 color, vec2 uv) {
    vec2 ghostOffset = vec2(0.002, 0.001);
    vec3 ghostColor = texture(hudSymbology, uv + ghostOffset).rgb * 0.3;
    return color + ghostColor * ghostingIntensity;
}

// COMPLETE chromatic aberration
vec3 applyChromaticAberration(vec2 uv) {
    vec2 aberrationOffset = vec2(chromaticAberration * 0.001, 0.0);
    
    float r = texture(hudSymbology, uv - aberrationOffset).r;
    float g = texture(hudSymbology, uv).g;
    float b = texture(hudSymbology, uv + aberrationOffset).b;
    
    return vec3(r, g, b);
}

// COMPLETE brightness adaptation
float calculateAdaptedBrightness(float hudBrightness, float ambient) {
    float targetContrast = 3.0;
    float requiredBrightness = ambient * targetContrast;
    return clamp(requiredBrightness, 0.1, 1.0);
}

void main() {
    // COMPLETE symbology rendering
    vec3 symbology = applyChromaticAberration(vUv);
    
    // COMPLETE ghosting effects
    symbology = applyGhosting(symbology, vUv);
    
    // COMPLETE brightness adaptation
    float adaptedBrightness = calculateAdaptedBrightness(brightness, ambientLight);
    symbology *= adaptedBrightness;
    
    // COMPLETE combiner glass effects
    symbology *= vCombinerFactor;
    
    // COMPLETE HUD color application
    vec3 finalColor = symbology * hudColor;
    
    // COMPLETE alpha calculation for transparency
    float alpha = length(symbology) * vCombinerFactor;
    
    fragColor = vec4(finalColor, alpha);
}
```

VALIDATION REQUIREMENTS:
CURSOR MUST verify after implementation:
✓ HUD symbology conforms to military standards
✓ Optical simulation produces realistic effects
✓ All HUD modes function correctly
✓ Brightness adaptation works properly
✓ Ghosting and aberration effects are realistic
✓ Weapon symbology is accurate
✓ Declutter system functions correctly
✓ Performance remains above 45 FPS

PERFORMANCE BENCHMARKS (MUST ACHIEVE):
✓ HUD rendering: <2ms per frame
✓ Symbology generation: <1ms per frame
✓ Optical effects: <1ms per frame
✓ Mode switching: <10ms per switch
✓ Brightness adaptation: <0.1ms per update
✓ Weapon calculations: <0.5ms per frame
```

**GAP IDENTIFICATION FOR PHASE 4.3**:
```
CURSOR MUST CHECK FOR THESE CRITICAL GAPS:
❌ Non-standard HUD symbology reducing authenticity
❌ Poor optical simulation breaking realism
❌ Missing brightness adaptation causing visibility issues
❌ Inadequate weapon symbology limiting functionality
❌ Poor mode switching disrupting user experience
❌ Missing declutter system causing information overload
❌ Inadequate ghosting effects reducing realism
❌ Poor chromatic aberration simulation
❌ Missing NVG compatibility
❌ Inadequate emergency mode functionality
```

## PHASE 4 COMPLETION CHECKLIST

### ✅ **VALIDATION REQUIREMENTS**
- [ ] All display types render with photorealistic quality
- [ ] Text rendering is ultra-sharp and clear
- [ ] Avionics data behaves realistically
- [ ] Flight instruments respond correctly
- [ ] Navigation systems provide accurate information
- [ ] HUD symbology conforms to military standards
- [ ] Optical simulation produces realistic effects
- [ ] All display modes function correctly
- [ ] Performance remains above 45 FPS

### ✅ **QUALITY GATES**
- [ ] Display physics are indistinguishable from real hardware
- [ ] Subpixel rendering enhances text clarity
- [ ] Flight data supports training applications
- [ ] Weather and traffic displays are functional
- [ ] HUD brightness adaptation works properly
- [ ] All shaders compile without errors
- [ ] Memory usage is within acceptable limits

### ✅ **PERFORMANCE BENCHMARKS**
- [ ] Display rendering: <3ms per display per frame
- [ ] Text rendering: <1ms per text element
- [ ] Flight data updates: <2ms per frame
- [ ] PFD rendering: <3ms per frame
- [ ] Navigation display: <4ms per frame
- [ ] HUD rendering: <2ms per frame
- [ ] Overall system: >45 FPS with all displays active

**PHASE 4 MUST BE 100% COMPLETE BEFORE PROCEEDING TO PHASE 5**
