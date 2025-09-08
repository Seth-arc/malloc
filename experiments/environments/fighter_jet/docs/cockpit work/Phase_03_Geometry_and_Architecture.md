# PHASE 3: ADVANCED GEOMETRY & COCKPIT ARCHITECTURE

## PRE-PHASE 3 VALIDATION:
```
CURSOR MUST VERIFY FROM PHASE 2:
✓ Lighting system is fully functional with realistic illumination
✓ Material system renders photorealistic surfaces
✓ All PBR+ features work correctly
✓ Surface detail systems enhance realism at all viewing distances
✓ Performance benchmarks are met (>45 FPS)
✓ All shaders compile without errors
✓ Memory usage is within acceptable limits
```

## Prompt 3.1: Parametric Cockpit Geometry System

**PREREQUISITE VALIDATION**:
```
CURSOR MUST VERIFY:
✓ Advanced renderer supports complex geometry
✓ Material system can handle multiple material types
✓ Asset manager can load high-poly models
✓ Performance monitoring shows acceptable baseline
✓ Memory management prevents leaks
```

**CURSOR RULES FOR THIS PROMPT**:
1. MUST implement mathematically accurate cockpit ergonomics
2. ALL geometry must be based on real fighter jet specifications
3. MUST support parametric modification for different aircraft types
4. Geometry quality must support extreme close-up inspection

**DETAILED IMPLEMENTATION**:
```
Create a sophisticated parametric geometry system for the cockpit:

MANDATORY GEOMETRY SYSTEM COMPONENTS:

1. MATHEMATICAL FOUNDATION (COMPLETE IMPLEMENTATION):
   CockpitGeometry.js MUST implement:

   ERGONOMIC CALCULATIONS:
   - MUST implement proper cockpit ergonomics using anthropometric data
   - MUST support 5th to 95th percentile pilot dimensions
   - MUST calculate proper sight line clearances
   - MUST implement reach envelope calculations
   - MUST support adjustable seat positioning

   PARAMETRIC SURFACE GENERATION:
   - MUST use NURBS curves for smooth panel transitions
   - MUST implement proper surface continuity (G2 minimum)
   - MUST support real-time parameter modification
   - MUST generate proper UV coordinates automatically
   - MUST maintain topology consistency during parameter changes

2. MAIN INSTRUMENT PANEL (ULTRA-HIGH DETAIL):
   InstrumentPanel.js MUST implement:

   DISPLAY INTEGRATION:
   - 5 main displays with proper LCD/OLED construction simulation
   - Individual pixel addressability for ultra-sharp text rendering
   - Multi-layer display simulation (polarizer, liquid crystal, backlight)
   - Proper viewing angle color shift simulation
   - Backlight bleeding and uniformity variations
   - Screen door effect simulation for close viewing

   PHYSICAL CONTROLS:
   - Individual key switches with proper travel and tactile feedback
   - Rotary encoders with detent positions and smooth rotation
   - Toggle switches with realistic spring mechanics
   - Push buttons with proper depression and return characteristics
   - Slider controls with friction and positional accuracy

3. STRUCTURAL ENGINEERING (COMPLETE IMPLEMENTATION):
   - MUST implement proper load-bearing structure representation
   - MUST create realistic joint and connection details
   - MUST build proper cable management systems
   - MUST add environmental sealing and gasket details
   - MUST include thermal expansion joint representation
   - MUST create proper vibration isolation mounting

COMPLETE IMPLEMENTATION REQUIREMENTS:

CockpitGeometry.js MUST implement:
```javascript
class CockpitGeometry {
    constructor(renderer, materialSystem) {
        this.renderer = renderer;
        this.materialSystem = materialSystem;
        
        // COMPLETE parametric system
        this.parametricEngine = new ParametricEngine();
        this.nurbsGenerator = new NURBSGenerator();
        this.ergonomicsCalculator = new ErgonomicsCalculator();
        
        // COMPLETE geometry components
        this.instrumentPanel = new InstrumentPanelGeometry();
        this.sideConsoles = new SideConsoleGeometry();
        this.overheadPanel = new OverheadPanelGeometry();
        this.canopyStructure = new CanopyStructureGeometry();
        this.seatGeometry = new SeatGeometry();
        
        // COMPLETE detail systems
        this.detailGenerator = new DetailGenerator();
        this.fastenerSystem = new FastenerSystem();
        this.cableManagement = new CableManagementSystem();
        
        this.initializeGeometry();
    }
    
    // MUST implement complete cockpit generation
    generateCockpit(parameters = {}) {
        const cockpitSpec = this.validateParameters(parameters);
        
        // COMPLETE ergonomic calculations
        const ergonomics = this.calculateErgonomics(cockpitSpec);
        const sightLines = this.calculateSightLines(ergonomics);
        const reachEnvelopes = this.calculateReachEnvelopes(ergonomics);
        
        // COMPLETE geometry generation
        const mainPanel = this.generateMainInstrumentPanel(cockpitSpec, ergonomics);
        const leftConsole = this.generateLeftConsole(cockpitSpec, ergonomics);
        const rightConsole = this.generateRightConsole(cockpitSpec, ergonomics);
        const overhead = this.generateOverheadPanel(cockpitSpec, ergonomics);
        const canopy = this.generateCanopyStructure(cockpitSpec);
        const seat = this.generateSeat(cockpitSpec, ergonomics);
        
        // COMPLETE assembly and validation
        const cockpit = this.assembleCockpit({
            mainPanel,
            leftConsole,
            rightConsole,
            overhead,
            canopy,
            seat
        });
        
        this.validateCockpitGeometry(cockpit, sightLines, reachEnvelopes);
        return cockpit;
    }
    
    // MUST implement complete ergonomic calculations
    calculateErgonomics(cockpitSpec) {
        const pilotDimensions = cockpitSpec.pilotDimensions || this.getStandardPilotDimensions();
        
        return {
            // Eye position calculations
            eyePosition: this.calculateEyePosition(pilotDimensions, cockpitSpec.seatPosition),
            eyeEllipse: this.calculateEyeEllipse(pilotDimensions),
            
            // Reach calculations
            armReach: this.calculateArmReach(pilotDimensions),
            legReach: this.calculateLegReach(pilotDimensions),
            
            // Clearance calculations
            headClearance: this.calculateHeadClearance(pilotDimensions),
            shoulderClearance: this.calculateShoulderClearance(pilotDimensions),
            
            // Control accessibility
            controlAccessibility: this.calculateControlAccessibility(pilotDimensions)
        };
    }
    
    // MUST implement complete main instrument panel
    generateMainInstrumentPanel(cockpitSpec, ergonomics) {
        const panelGeometry = new THREE.BufferGeometry();
        
        // COMPLETE panel surface generation
        const panelSurface = this.generatePanelSurface(cockpitSpec.panelCurvature, ergonomics.eyePosition);
        const displayCutouts = this.generateDisplayCutouts(cockpitSpec.displays);
        const controlCutouts = this.generateControlCutouts(cockpitSpec.controls);
        
        // COMPLETE detail generation
        const panelLines = this.generatePanelLines(panelSurface);
        const fasteners = this.generateFasteners(panelSurface, cockpitSpec.fastenerSpacing);
        const ventilationGrilles = this.generateVentilationGrilles(panelSurface);
        
        // COMPLETE geometry assembly
        const combinedGeometry = this.combineGeometries([
            panelSurface,
            displayCutouts,
            controlCutouts,
            panelLines,
            fasteners,
            ventilationGrilles
        ]);
        
        // COMPLETE UV mapping
        this.generateOptimalUVMapping(combinedGeometry);
        
        return combinedGeometry;
    }
    
    // MUST implement complete display cutout generation
    generateDisplayCutouts(displaySpecs) {
        const cutouts = [];
        
        for (const display of displaySpecs) {
            const cutout = this.generateDisplayCutout({
                position: display.position,
                size: display.size,
                bezelWidth: display.bezelWidth,
                mountingDepth: display.mountingDepth,
                coolingRequirements: display.coolingRequirements
            });
            
            // Add mounting hardware
            const mountingHardware = this.generateMountingHardware(display);
            const coolingVents = this.generateCoolingVents(display);
            const cableRouting = this.generateCableRouting(display);
            
            cutouts.push({
                cutout,
                mountingHardware,
                coolingVents,
                cableRouting
            });
        }
        
        return cutouts;
    }
    
    // MUST implement complete control generation
    generateControlCutouts(controlSpecs) {
        const controls = [];
        
        for (const control of controlSpecs) {
            let controlGeometry;
            
            switch (control.type) {
                case 'rotary_switch':
                    controlGeometry = this.generateRotarySwitch(control);
                    break;
                case 'toggle_switch':
                    controlGeometry = this.generateToggleSwitch(control);
                    break;
                case 'push_button':
                    controlGeometry = this.generatePushButton(control);
                    break;
                case 'slider':
                    controlGeometry = this.generateSlider(control);
                    break;
                case 'key_switch':
                    controlGeometry = this.generateKeySwitch(control);
                    break;
                // COMPLETE implementation for all control types
            }
            
            controls.push(controlGeometry);
        }
        
        return controls;
    }
}

class InstrumentPanelGeometry {
    constructor() {
        this.displaySystem = new DisplaySystem();
        this.controlSystem = new ControlSystem();
        this.structuralSystem = new StructuralSystem();
    }
    
    // MUST implement complete display system
    generateDisplaySystem(displaySpecs) {
        const displays = [];
        
        for (const spec of displaySpecs) {
            const display = {
                // COMPLETE LCD/OLED construction
                screen: this.generateScreenGeometry(spec),
                backlight: this.generateBacklightSystem(spec),
                polarizers: this.generatePolarizers(spec),
                liquidCrystal: this.generateLiquidCrystalLayer(spec),
                colorFilters: this.generateColorFilters(spec),
                
                // COMPLETE housing and mounting
                housing: this.generateDisplayHousing(spec),
                bezel: this.generateDisplayBezel(spec),
                mounting: this.generateDisplayMounting(spec),
                
                // COMPLETE cooling and power
                cooling: this.generateCoolingSystem(spec),
                powerConnectors: this.generatePowerConnectors(spec),
                dataConnectors: this.generateDataConnectors(spec)
            };
            
            displays.push(display);
        }
        
        return displays;
    }
    
    // MUST implement complete screen geometry with pixel-level detail
    generateScreenGeometry(spec) {
        const screenGeometry = new THREE.PlaneGeometry(spec.width, spec.height);
        
        // Generate individual pixels for close-up viewing
        if (spec.pixelLevelDetail) {
            const pixelGeometry = this.generatePixelGeometry(spec);
            screenGeometry.merge(pixelGeometry);
        }
        
        // Add screen door effect for LCD displays
        if (spec.type === 'LCD') {
            const screenDoorGeometry = this.generateScreenDoorEffect(spec);
            screenGeometry.merge(screenDoorGeometry);
        }
        
        return screenGeometry;
    }
}

class ControlSystem {
    constructor() {
        this.switchLibrary = new SwitchLibrary();
        this.buttonLibrary = new ButtonLibrary();
        this.encoderLibrary = new EncoderLibrary();
    }
    
    // MUST implement complete rotary switch
    generateRotarySwitch(spec) {
        const switchGeometry = new THREE.Group();
        
        // COMPLETE switch body
        const body = this.generateSwitchBody(spec);
        const shaft = this.generateSwitchShaft(spec);
        const detentMechanism = this.generateDetentMechanism(spec);
        
        // COMPLETE switch cap
        const cap = this.generateSwitchCap(spec);
        const positionIndicator = this.generatePositionIndicator(spec);
        const labeling = this.generateSwitchLabeling(spec);
        
        // COMPLETE mounting hardware
        const mounting = this.generateSwitchMounting(spec);
        const nutAndWasher = this.generateNutAndWasher(spec);
        
        switchGeometry.add(body, shaft, detentMechanism, cap, positionIndicator, labeling, mounting, nutAndWasher);
        
        return switchGeometry;
    }
    
    // MUST implement complete toggle switch
    generateToggleSwitch(spec) {
        const toggleGeometry = new THREE.Group();
        
        // COMPLETE toggle mechanism
        const body = this.generateToggleBody(spec);
        const actuator = this.generateToggleActuator(spec);
        const springMechanism = this.generateSpringMechanism(spec);
        const contacts = this.generateSwitchContacts(spec);
        
        // COMPLETE switch positions
        const positions = this.generateSwitchPositions(spec);
        const detents = this.generateToggleDetents(spec);
        
        toggleGeometry.add(body, actuator, springMechanism, contacts, positions, detents);
        
        return toggleGeometry;
    }
}
```

VALIDATION REQUIREMENTS:
CURSOR MUST verify after implementation:
✓ All geometry renders without errors
✓ Parametric system allows real-time modification
✓ Ergonomic calculations produce realistic results
✓ Display systems have proper pixel-level detail
✓ Control systems have realistic mechanical properties
✓ Performance remains above 45 FPS with full detail
✓ Memory usage stays within acceptable limits
✓ UV mapping is optimal for texture application

PERFORMANCE BENCHMARKS (MUST ACHIEVE):
✓ Geometry generation: <5s for complete cockpit
✓ Parametric updates: <1s for parameter changes
✓ Rendering performance: >45 FPS with full detail
✓ Memory usage: <512MB for all geometry
✓ LOD transitions: Imperceptible to user
✓ UV mapping generation: <2s per component
```

**GAP IDENTIFICATION FOR PHASE 3.1**:
```
CURSOR MUST CHECK FOR THESE CRITICAL GAPS:
❌ Inaccurate ergonomic calculations affecting pilot comfort
❌ Poor parametric system limiting customization
❌ Missing pixel-level detail reducing display realism
❌ Inadequate control detail breaking immersion
❌ Poor performance with high-detail geometry
❌ Missing structural details reducing authenticity
❌ Inadequate UV mapping causing texture issues
❌ Missing fastener and connection details
❌ Poor cable management system
❌ Inadequate cooling system representation
```

## Prompt 3.2: Advanced Canopy & Glass Systems

**PREREQUISITE VALIDATION**:
```
CURSOR MUST VERIFY FROM PHASE 3.1:
✓ Cockpit geometry system is working correctly
✓ Parametric system allows real-time modifications
✓ Display systems render with pixel-level detail
✓ Control systems have realistic mechanical properties
✓ Performance benchmarks are met
✓ Memory usage is within acceptable limits
```

**CURSOR RULES FOR THIS PROMPT**:
1. MUST implement multi-layer glass construction with optical accuracy
2. ALL glass properties must be based on real-world optical physics
3. MUST support dynamic environmental effects on glass surfaces
4. Glass rendering quality must be indistinguishable from reality

**DETAILED IMPLEMENTATION**:
```
Implement ultra-realistic glass and transparency systems:

MANDATORY GLASS SYSTEM COMPONENTS:

1. MULTI-LAYER GLASS CONSTRUCTION (COMPLETE IMPLEMENTATION):
   CanopySystem.js MUST implement:

   LAYER STRUCTURE:
   - Outer layer: Bird-strike resistant polycarbonate (6mm thickness)
   - Heating layer: Conductive heating elements with proper pattern
   - Middle layer: Structural laminate with proper optical properties
   - Inner layer: Anti-reflective coated glass (3mm thickness)
   - Air gaps: Proper optical properties and thermal insulation

   OPTICAL PROPERTIES:
   - MUST implement proper Fresnel reflections with IOR variation
   - MUST create realistic refraction with chromatic dispersion
   - MUST build proper transparency falloff with thickness
   - MUST implement anti-reflective coating simulation
   - MUST create realistic surface imperfection rendering

2. ADVANCED GLASS RENDERING (COMPLETE IMPLEMENTATION):
   GlassRenderer.js MUST implement:

   PHYSICAL ACCURACY:
   - Index of refraction values for all materials
   - Proper Abbe numbers for chromatic dispersion
   - Accurate transmission coefficients
   - Proper reflection coefficients at all angles
   - Temperature-dependent optical properties

   ENVIRONMENTAL EFFECTS:
   - Dynamic condensation formation and evaporation
   - Ice formation patterns with realistic crystal structures
   - Rain drop simulation with proper physics and optics
   - Dust accumulation with electrostatic effects
   - Thermal stress visualization with color changes

3. HUD GLASS SYSTEM (COMPLETE IMPLEMENTATION):
   HUDGlass.js MUST implement:

   WAVEGUIDE OPTICS:
   - Proper waveguide optics for HUD projection
   - Realistic combiner glass with angular reflection
   - Proper parallax correction for head movement
   - Brightness adaptation for varying light conditions
   - Ghosting and double-image effects for realism

COMPLETE IMPLEMENTATION REQUIREMENTS:

CanopySystem.js MUST implement:
```javascript
class CanopySystem {
    constructor(renderer, materialSystem) {
        this.renderer = renderer;
        this.materialSystem = materialSystem;
        
        // COMPLETE glass systems
        this.glassRenderer = new GlassRenderer();
        this.opticsCalculator = new OpticsCalculator();
        this.environmentalEffects = new EnvironmentalEffects();
        
        // COMPLETE canopy components
        this.outerLayer = new PolycarbonateLayer();
        this.heatingLayer = new HeatingLayer();
        this.structuralLayer = new StructuralLayer();
        this.innerLayer = new AntiReflectiveLayer();
        
        // COMPLETE HUD system
        this.hudGlass = new HUDGlass();
        this.combinerGlass = new CombinerGlass();
        
        this.initializeCanopySystem();
    }
    
    // MUST implement complete canopy generation
    generateCanopy(canopySpec) {
        const canopyGeometry = new THREE.Group();
        
        // COMPLETE layer generation
        const layers = this.generateGlassLayers(canopySpec);
        const frame = this.generateCanopyFrame(canopySpec);
        const seals = this.generateCanopySeals(canopySpec);
        const hardware = this.generateCanopyHardware(canopySpec);
        
        // COMPLETE optical system
        const opticalProperties = this.calculateOpticalProperties(layers);
        const refractionSystem = this.setupRefractionSystem(opticalProperties);
        const reflectionSystem = this.setupReflectionSystem(opticalProperties);
        
        // COMPLETE environmental systems
        const condensationSystem = this.setupCondensationSystem(canopySpec);
        const iceFormationSystem = this.setupIceFormationSystem(canopySpec);
        const rainEffectSystem = this.setupRainEffectSystem(canopySpec);
        
        canopyGeometry.add(layers, frame, seals, hardware);
        
        return {
            geometry: canopyGeometry,
            opticalProperties,
            refractionSystem,
            reflectionSystem,
            environmentalSystems: {
                condensationSystem,
                iceFormationSystem,
                rainEffectSystem
            }
        };
    }
    
    // MUST implement complete glass layer generation
    generateGlassLayers(canopySpec) {
        const layers = new THREE.Group();
        
        // COMPLETE outer polycarbonate layer
        const outerLayer = this.generateOuterLayer({
            thickness: 0.006, // 6mm
            material: 'polycarbonate',
            birdStrikeResistant: true,
            opticalClarity: 0.92,
            thermalExpansion: 6.5e-5
        });
        
        // COMPLETE heating layer
        const heatingLayer = this.generateHeatingLayer({
            pattern: 'serpentine',
            resistance: 12.0, // ohms per square
            powerDensity: 2000, // watts per square meter
            transparency: 0.98
        });
        
        // COMPLETE structural layer
        const structuralLayer = this.generateStructuralLayer({
            thickness: 0.002, // 2mm
            material: 'laminated_glass',
            tensileStrength: 50e6, // 50 MPa
            opticalClarity: 0.95
        });
        
        // COMPLETE inner AR layer
        const innerLayer = this.generateInnerLayer({
            thickness: 0.003, // 3mm
            material: 'ar_coated_glass',
            coating: 'multi_layer_ar',
            reflectance: 0.005, // 0.5% reflection
            opticalClarity: 0.99
        });
        
        layers.add(outerLayer, heatingLayer, structuralLayer, innerLayer);
        
        return layers;
    }
    
    // MUST implement complete optical properties calculation
    calculateOpticalProperties(layers) {
        const opticalProperties = {
            totalThickness: 0,
            combinedIOR: 1.0,
            combinedTransmission: 1.0,
            combinedReflection: 0.0,
            chromaticDispersion: {},
            thermalProperties: {}
        };
        
        for (const layer of layers.children) {
            const layerProps = this.getLayerOpticalProperties(layer);
            
            // COMPLETE optical calculations
            opticalProperties.totalThickness += layerProps.thickness;
            opticalProperties.combinedIOR = this.calculateCombinedIOR(
                opticalProperties.combinedIOR,
                layerProps.ior,
                layerProps.thickness
            );
            
            opticalProperties.combinedTransmission *= layerProps.transmission;
            opticalProperties.combinedReflection += layerProps.reflection * 
                (1 - opticalProperties.combinedReflection);
            
            // COMPLETE chromatic dispersion calculation
            this.addChromaticDispersion(opticalProperties.chromaticDispersion, layerProps.abbe);
            
            // COMPLETE thermal properties
            this.addThermalProperties(opticalProperties.thermalProperties, layerProps.thermal);
        }
        
        return opticalProperties;
    }
}

class GlassRenderer {
    constructor() {
        this.refractionShader = new RefractionShader();
        this.reflectionShader = new ReflectionShader();
        this.chromaticDispersionShader = new ChromaticDispersionShader();
        this.environmentalShader = new EnvironmentalShader();
    }
    
    // MUST implement complete glass rendering
    renderGlass(glassObject, scene, camera) {
        // COMPLETE multi-pass rendering
        const passes = [
            this.renderRefractionPass(glassObject, scene, camera),
            this.renderReflectionPass(glassObject, scene, camera),
            this.renderChromaticDispersionPass(glassObject, scene, camera),
            this.renderEnvironmentalEffectsPass(glassObject, scene, camera)
        ];
        
        // COMPLETE pass combination
        const finalResult = this.combinePasses(passes);
        
        return finalResult;
    }
    
    // MUST implement complete refraction pass
    renderRefractionPass(glassObject, scene, camera) {
        const refractionRenderTarget = new THREE.WebGLRenderTarget(
            this.renderer.domElement.width,
            this.renderer.domElement.height,
            {
                format: THREE.RGBAFormat,
                type: THREE.FloatType,
                minFilter: THREE.LinearFilter,
                magFilter: THREE.LinearFilter
            }
        );
        
        // COMPLETE refraction calculation
        const refractionCamera = this.calculateRefractionCamera(camera, glassObject);
        const refractionScene = this.prepareRefractionScene(scene, glassObject);
        
        this.renderer.setRenderTarget(refractionRenderTarget);
        this.renderer.render(refractionScene, refractionCamera);
        this.renderer.setRenderTarget(null);
        
        return refractionRenderTarget.texture;
    }
}

class EnvironmentalEffects {
    constructor() {
        this.condensationSystem = new CondensationSystem();
        this.iceFormationSystem = new IceFormationSystem();
        this.rainSystem = new RainSystem();
        this.dustSystem = new DustSystem();
    }
    
    // MUST implement complete condensation system
    updateCondensation(glassObject, environmentalConditions) {
        const temperature = environmentalConditions.temperature;
        const humidity = environmentalConditions.humidity;
        const dewPoint = this.calculateDewPoint(temperature, humidity);
        
        // COMPLETE condensation physics
        const condensationRate = this.calculateCondensationRate(
            temperature,
            dewPoint,
            glassObject.surfaceTemperature
        );
        
        const condensationPattern = this.generateCondensationPattern(
            glassObject,
            condensationRate,
            environmentalConditions.airflow
        );
        
        // COMPLETE condensation rendering
        this.updateCondensationTexture(glassObject, condensationPattern);
        this.updateOpticalProperties(glassObject, condensationPattern);
        
        return condensationPattern;
    }
    
    // MUST implement complete ice formation
    updateIceFormation(glassObject, environmentalConditions) {
        if (environmentalConditions.temperature > 273.15) return null; // Above freezing
        
        // COMPLETE ice crystal formation
        const nucleationSites = this.findNucleationSites(glassObject);
        const crystalGrowth = this.simulateCrystalGrowth(
            nucleationSites,
            environmentalConditions.temperature,
            environmentalConditions.humidity
        );
        
        const icePattern = this.generateIcePattern(crystalGrowth);
        
        // COMPLETE ice rendering
        this.updateIceTexture(glassObject, icePattern);
        this.updateIceGeometry(glassObject, icePattern);
        
        return icePattern;
    }
}

class HUDGlass {
    constructor() {
        this.waveguideOptics = new WaveguideOptics();
        this.combinerGlass = new CombinerGlass();
        this.projectionSystem = new ProjectionSystem();
    }
    
    // MUST implement complete HUD glass system
    generateHUDGlass(hudSpec) {
        const hudGlass = new THREE.Group();
        
        // COMPLETE combiner glass
        const combinerGlass = this.generateCombinerGlass({
            angle: hudSpec.combinerAngle || 60, // degrees
            thickness: 0.003, // 3mm
            coating: 'dichroic',
            reflectanceSpectrum: this.getDichroicSpectrum(),
            transmittanceSpectrum: this.getTransmittanceSpectrum()
        });
        
        // COMPLETE waveguide system
        const waveguide = this.generateWaveguide({
            length: hudSpec.waveguideLength || 0.15, // 150mm
            width: hudSpec.waveguideWidth || 0.10, // 100mm
            thickness: 0.005, // 5mm
            ior: 1.52, // optical glass
            totalInternalReflection: true
        });
        
        // COMPLETE projection optics
        const projectionOptics = this.generateProjectionOptics({
            focalLength: hudSpec.focalLength || 0.05, // 50mm
            aperture: hudSpec.aperture || 2.8,
            fieldOfView: hudSpec.fieldOfView || 20, // degrees
            collimation: 'infinite' // collimated to infinity
        });
        
        hudGlass.add(combinerGlass, waveguide, projectionOptics);
        
        return hudGlass;
    }
    
    // MUST implement complete parallax correction
    updateParallaxCorrection(hudGlass, headPosition, eyePosition) {
        // COMPLETE parallax calculation
        const parallaxOffset = this.calculateParallaxOffset(headPosition, eyePosition);
        const correctionMatrix = this.generateCorrectionMatrix(parallaxOffset);
        
        // COMPLETE optical adjustment
        this.adjustCombinerAngle(hudGlass.combinerGlass, correctionMatrix);
        this.adjustWaveguideAlignment(hudGlass.waveguide, correctionMatrix);
        this.adjustProjectionAlignment(hudGlass.projectionOptics, correctionMatrix);
        
        return correctionMatrix;
    }
}
```

SHADER REQUIREMENTS:
MUST create complete glass shaders:

glass_vertex.glsl:
```glsl
#version 300 es
precision highp float;

in vec3 position;
in vec3 normal;
in vec2 uv;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;
uniform mat3 normalMatrix;

out vec3 vWorldPosition;
out vec3 vWorldNormal;
out vec2 vUv;
out vec3 vViewDirection;
out vec3 vReflectionDirection;

void main() {
    vec4 worldPosition = modelMatrix * vec4(position, 1.0);
    vWorldPosition = worldPosition.xyz;
    vWorldNormal = normalize(normalMatrix * normal);
    vUv = uv;
    
    vec3 cameraPosition = (inverse(viewMatrix) * vec4(0.0, 0.0, 0.0, 1.0)).xyz;
    vViewDirection = normalize(cameraPosition - vWorldPosition);
    vReflectionDirection = reflect(-vViewDirection, vWorldNormal);
    
    gl_Position = projectionMatrix * viewMatrix * worldPosition;
}
```

glass_fragment.glsl:
```glsl
#version 300 es
precision highp float;

in vec3 vWorldPosition;
in vec3 vWorldNormal;
in vec2 vUv;
in vec3 vViewDirection;
in vec3 vReflectionDirection;

uniform float ior;
uniform float thickness;
uniform vec3 absorption;
uniform float roughness;
uniform sampler2D environmentMap;
uniform sampler2D refractionMap;
uniform sampler2D condensationMap;
uniform sampler2D iceMap;

out vec4 fragColor;

// COMPLETE Fresnel calculation
float calculateFresnel(vec3 viewDir, vec3 normal, float ior) {
    float cosTheta = max(dot(viewDir, normal), 0.0);
    float sinTheta = sqrt(1.0 - cosTheta * cosTheta);
    float sinThetaT = sinTheta / ior;
    
    if (sinThetaT >= 1.0) return 1.0; // Total internal reflection
    
    float cosThetaT = sqrt(1.0 - sinThetaT * sinThetaT);
    
    float rs = (ior * cosTheta - cosThetaT) / (ior * cosTheta + cosThetaT);
    float rp = (cosTheta - ior * cosThetaT) / (cosTheta + ior * cosThetaT);
    
    return 0.5 * (rs * rs + rp * rp);
}

// COMPLETE chromatic dispersion
vec3 calculateChromaticDispersion(vec3 viewDir, vec3 normal, float baseIOR) {
    float iorRed = baseIOR - 0.01;
    float iorGreen = baseIOR;
    float iorBlue = baseIOR + 0.01;
    
    vec3 refractionRed = refract(-viewDir, normal, 1.0 / iorRed);
    vec3 refractionGreen = refract(-viewDir, normal, 1.0 / iorGreen);
    vec3 refractionBlue = refract(-viewDir, normal, 1.0 / iorBlue);
    
    return vec3(
        texture(refractionMap, refractionRed.xy * 0.5 + 0.5).r,
        texture(refractionMap, refractionGreen.xy * 0.5 + 0.5).g,
        texture(refractionMap, refractionBlue.xy * 0.5 + 0.5).b
    );
}

// COMPLETE absorption calculation
vec3 calculateAbsorption(vec3 color, float distance, vec3 absorptionCoeff) {
    return color * exp(-absorptionCoeff * distance);
}

void main() {
    vec3 normal = normalize(vWorldNormal);
    vec3 viewDir = normalize(vViewDirection);
    
    // COMPLETE Fresnel calculation
    float fresnel = calculateFresnel(viewDir, normal, ior);
    
    // COMPLETE reflection
    vec3 reflectionColor = texture(environmentMap, vReflectionDirection.xy * 0.5 + 0.5).rgb;
    
    // COMPLETE refraction with chromatic dispersion
    vec3 refractionColor = calculateChromaticDispersion(viewDir, normal, ior);
    
    // COMPLETE absorption
    refractionColor = calculateAbsorption(refractionColor, thickness, absorption);
    
    // COMPLETE environmental effects
    float condensation = texture(condensationMap, vUv).r;
    float ice = texture(iceMap, vUv).r;
    
    // COMPLETE final color mixing
    vec3 finalColor = mix(refractionColor, reflectionColor, fresnel);
    
    // Apply environmental effects
    finalColor = mix(finalColor, vec3(0.8, 0.9, 1.0), condensation * 0.3);
    finalColor = mix(finalColor, vec3(0.9, 0.95, 1.0), ice * 0.5);
    
    fragColor = vec4(finalColor, 1.0 - fresnel * 0.1);
}
```

VALIDATION REQUIREMENTS:
CURSOR MUST verify after implementation:
✓ Multi-layer glass construction renders correctly
✓ Optical properties are physically accurate
✓ Environmental effects look realistic
✓ HUD glass system works properly
✓ Parallax correction functions correctly
✓ Performance remains above 45 FPS
✓ All glass shaders compile without errors
✓ Chromatic dispersion is visible and accurate

PERFORMANCE BENCHMARKS (MUST ACHIEVE):
✓ Glass rendering: <5ms per frame
✓ Environmental effects: <2ms per frame
✓ HUD system: <3ms per frame
✓ Parallax correction: <1ms per update
✓ Shader compilation: <200ms total
✓ Memory usage: <128MB for all glass systems
```

**GAP IDENTIFICATION FOR PHASE 3.2**:
```
CURSOR MUST CHECK FOR THESE CRITICAL GAPS:
❌ Inaccurate optical properties reducing realism
❌ Poor multi-layer construction breaking immersion
❌ Missing environmental effects on glass surfaces
❌ Inadequate HUD glass system functionality
❌ Poor parallax correction affecting usability
❌ Performance issues with complex glass rendering
❌ Missing chromatic dispersion effects
❌ Inadequate Fresnel calculations
❌ Poor environmental effect integration
❌ Missing thermal stress visualization
```

## Prompt 3.3: Mechanical Systems & Animation

**PREREQUISITE VALIDATION**:
```
CURSOR MUST VERIFY FROM PHASE 3.2:
✓ Canopy system renders with realistic glass properties
✓ Multi-layer glass construction is working correctly
✓ Environmental effects on glass are functional
✓ HUD glass system operates properly
✓ Performance benchmarks are met
✓ All glass shaders compile without errors
```

**CURSOR RULES FOR THIS PROMPT**:
1. MUST implement realistic mechanical physics for all moving parts
2. ALL animations must be based on real mechanical constraints
3. MUST support interactive control with proper feedback
4. Mechanical quality must match real aircraft systems

**DETAILED IMPLEMENTATION**:
```
Create realistic mechanical systems with proper physics simulation:

MANDATORY MECHANICAL SYSTEM COMPONENTS:

1. CONTROL STICK SYSTEM (COMPLETE IMPLEMENTATION):
   ControlStickSystem.js MUST implement:

   GIMBAL MECHANICS:
   - MUST implement proper gimbal mechanics with realistic pivot points
   - MUST create force feedback simulation with proper resistance curves
   - MUST build realistic control surface coupling and feedback
   - MUST implement proper friction and dampening characteristics
   - MUST create mechanical backlash and dead zone simulation
   - MUST add realistic wear patterns and lubrication effects

   PHYSICS SIMULATION:
   - MUST implement proper inertia calculations
   - MUST create realistic spring and damper systems
   - MUST build proper force transmission through linkages
   - MUST implement mechanical compliance and flexure
   - MUST create realistic control authority limits

2. SWITCH AND CONTROL MECHANISMS (COMPLETE IMPLEMENTATION):
   SwitchMechanisms.js MUST implement:

   SWITCH TYPES:
   - Toggle switches with proper spring mechanics
   - Rotary switches with detent positioning
   - Push buttons with tactile feedback
   - Slider controls with friction modeling
   - Key switches with proper actuation

   MECHANICAL PROPERTIES:
   - MUST implement proper switch actuation with realistic timing
   - MUST create mechanical relay clicking and electromagnetic effects
   - MUST build proper rotary control detent positioning
   - MUST implement realistic cable and linkage systems
   - MUST create proper mechanical compliance and flexure

3. SEAT AND ERGONOMIC SYSTEMS (COMPLETE IMPLEMENTATION):
   SeatSystem.js MUST implement:

   EJECTION SEAT MECHANICS:
   - MUST model proper ejection seat mechanics with realistic constraints
   - MUST implement adjustable seat positioning with proper kinematics
   - MUST create realistic cushioning compression and recovery
   - MUST build proper harness and restraint system simulation
   - MUST implement environmental controls with proper thermal modeling

COMPLETE IMPLEMENTATION REQUIREMENTS:

ControlStickSystem.js MUST implement:
```javascript
class ControlStickSystem {
    constructor(renderer, physicsEngine) {
        this.renderer = renderer;
        this.physics = physicsEngine;
        
        // COMPLETE mechanical components
        this.gimbalSystem = new GimbalSystem();
        this.forceSystem = new ForceSystem();
        this.dampingSystem = new DampingSystem();
        this.frictionSystem = new FrictionSystem();
        
        // COMPLETE control surfaces
        this.elevatorControl = new ElevatorControl();
        this.aileronControl = new AileronControl();
        this.rudderControl = new RudderControl();
        
        // COMPLETE feedback systems
        this.forceFeedback = new ForceFeedback();
        this.tactileFeedback = new TactileFeedback();
        
        this.initializeControlStick();
    }
    
    // MUST implement complete control stick physics
    updateControlStick(deltaTime, inputForces) {
        // COMPLETE force calculations
        const appliedForces = this.calculateAppliedForces(inputForces);
        const resistanceForces = this.calculateResistanceForces();
        const dampingForces = this.calculateDampingForces();
        const frictionForces = this.calculateFrictionForces();
        
        const totalForces = this.combineForces([
            appliedForces,
            resistanceForces,
            dampingForces,
            frictionForces
        ]);
        
        // COMPLETE motion calculation
        const acceleration = this.calculateAcceleration(totalForces);
        const velocity = this.updateVelocity(acceleration, deltaTime);
        const position = this.updatePosition(velocity, deltaTime);
        
        // COMPLETE constraint application
        const constrainedPosition = this.applyConstraints(position);
        const finalPosition = this.applyDeadZone(constrainedPosition);
        
        // COMPLETE control surface updates
        this.updateControlSurfaces(finalPosition);
        this.updateForceFeedback(totalForces);
        
        return finalPosition;
    }
    
    // MUST implement complete gimbal system
    calculateGimbalMotion(stickPosition) {
        const gimbalAngles = {
            pitch: this.calculatePitchAngle(stickPosition.y),
            roll: this.calculateRollAngle(stickPosition.x),
            yaw: this.calculateYawAngle(stickPosition.z)
        };
        
        // COMPLETE gimbal constraints
        gimbalAngles.pitch = this.constrainAngle(gimbalAngles.pitch, -15, 15); // degrees
        gimbalAngles.roll = this.constrainAngle(gimbalAngles.roll, -15, 15); // degrees
        gimbalAngles.yaw = this.constrainAngle(gimbalAngles.yaw, -5, 5); // degrees
        
        // COMPLETE mechanical coupling
        const coupledAngles = this.applyCoupling(gimbalAngles);
        
        return coupledAngles;
    }
    
    // MUST implement complete force feedback
    calculateForceFeedback(controlSurfaceLoads, airspeed) {
        const feedbackForces = {
            pitch: 0,
            roll: 0,
            yaw: 0
        };
        
        // COMPLETE aerodynamic feedback
        feedbackForces.pitch = this.calculatePitchFeedback(
            controlSurfaceLoads.elevator,
            airspeed
        );
        
        feedbackForces.roll = this.calculateRollFeedback(
            controlSurfaceLoads.ailerons,
            airspeed
        );
        
        feedbackForces.yaw = this.calculateYawFeedback(
            controlSurfaceLoads.rudder,
            airspeed
        );
        
        // COMPLETE force scaling
        const scaledForces = this.scaleForces(feedbackForces, this.forceScaling);
        
        return scaledForces;
    }
}

class SwitchMechanisms {
    constructor(physicsEngine) {
        this.physics = physicsEngine;
        
        // COMPLETE switch libraries
        this.toggleSwitches = new ToggleSwitchLibrary();
        this.rotarySwitches = new RotarySwitchLibrary();
        this.pushButtons = new PushButtonLibrary();
        this.sliders = new SliderLibrary();
        
        // COMPLETE mechanical properties
        this.springConstants = new SpringConstants();
        this.frictionCoefficients = new FrictionCoefficients();
        this.dampingFactors = new DampingFactors();
        
        this.initializeSwitchMechanisms();
    }
    
    // MUST implement complete toggle switch
    createToggleSwitch(spec) {
        const toggleSwitch = {
            // COMPLETE mechanical properties
            springConstant: spec.springConstant || 50.0, // N/m
            dampingFactor: spec.dampingFactor || 0.1,
            frictionCoefficient: spec.frictionCoefficient || 0.3,
            actuationForce: spec.actuationForce || 2.0, // N
            
            // COMPLETE switch positions
            positions: spec.positions || ['OFF', 'ON'],
            currentPosition: 0,
            targetPosition: 0,
            
            // COMPLETE mechanical state
            angle: 0,
            velocity: 0,
            acceleration: 0,
            
            // COMPLETE contact system
            contacts: this.createSwitchContacts(spec),
            
            // COMPLETE animation system
            animationCurve: this.createAnimationCurve(spec)
        };
        
        return toggleSwitch;
    }
    
    // MUST implement complete switch actuation
    actuateSwitch(switchObject, targetPosition, deltaTime) {
        // COMPLETE force calculation
        const springForce = this.calculateSpringForce(
            switchObject,
            targetPosition
        );
        
        const dampingForce = this.calculateDampingForce(
            switchObject.velocity,
            switchObject.dampingFactor
        );
        
        const frictionForce = this.calculateFrictionForce(
            switchObject.velocity,
            switchObject.frictionCoefficient
        );
        
        const totalForce = springForce - dampingForce - frictionForce;
        
        // COMPLETE motion integration
        switchObject.acceleration = totalForce / switchObject.mass;
        switchObject.velocity += switchObject.acceleration * deltaTime;
        switchObject.angle += switchObject.velocity * deltaTime;
        
        // COMPLETE position snapping
        if (this.isNearPosition(switchObject, targetPosition)) {
            switchObject.angle = this.getPositionAngle(targetPosition);
            switchObject.velocity = 0;
            switchObject.currentPosition = targetPosition;
        }
        
        // COMPLETE contact state update
        this.updateContactState(switchObject);
        
        return switchObject;
    }
    
    // MUST implement complete rotary switch
    createRotarySwitch(spec) {
        const rotarySwitch = {
            // COMPLETE mechanical properties
            detentTorque: spec.detentTorque || 0.05, // N⋅m
            frictionTorque: spec.frictionTorque || 0.01, // N⋅m
            inertia: spec.inertia || 1e-6, // kg⋅m²
            
            // COMPLETE detent system
            positions: spec.positions || 8,
            detentAngle: 360 / (spec.positions || 8), // degrees
            currentPosition: 0,
            
            // COMPLETE rotational state
            angle: 0,
            angularVelocity: 0,
            angularAcceleration: 0,
            
            // COMPLETE detent mechanism
            detentMechanism: this.createDetentMechanism(spec),
            
            // COMPLETE contact system
            contactRings: this.createContactRings(spec)
        };
        
        return rotarySwitch;
    }
}

class SeatSystem {
    constructor(physicsEngine) {
        this.physics = physicsEngine;
        
        // COMPLETE seat components
        this.seatFrame = new SeatFrame();
        this.cushionSystem = new CushionSystem();
        this.adjustmentMechanism = new AdjustmentMechanism();
        this.restraintSystem = new RestraintSystem();
        
        // COMPLETE ejection system
        this.ejectionMechanism = new EjectionMechanism();
        this.pyrotechnics = new PyrotechnicSystem();
        this.sequenceController = new SequenceController();
        
        this.initializeSeatSystem();
    }
    
    // MUST implement complete seat adjustment
    adjustSeat(adjustmentType, amount, deltaTime) {
        let adjustmentResult;
        
        switch (adjustmentType) {
            case 'height':
                adjustmentResult = this.adjustSeatHeight(amount, deltaTime);
                break;
            case 'fore_aft':
                adjustmentResult = this.adjustSeatPosition(amount, deltaTime);
                break;
            case 'back_angle':
                adjustmentResult = this.adjustBackAngle(amount, deltaTime);
                break;
            case 'lumbar':
                adjustmentResult = this.adjustLumbarSupport(amount, deltaTime);
                break;
            // COMPLETE implementation for all adjustment types
        }
        
        // COMPLETE constraint validation
        this.validateSeatPosition(adjustmentResult);
        
        // COMPLETE ergonomic validation
        this.validateErgonomics(adjustmentResult);
        
        return adjustmentResult;
    }
    
    // MUST implement complete cushion physics
    updateCushionSystem(pilotWeight, gForces, deltaTime) {
        const cushions = this.cushionSystem.getAllCushions();
        
        for (const cushion of cushions) {
            // COMPLETE load distribution
            const loadDistribution = this.calculateLoadDistribution(
                pilotWeight,
                gForces,
                cushion.position
            );
            
            // COMPLETE compression calculation
            const compression = this.calculateCompression(
                loadDistribution,
                cushion.stiffness,
                cushion.currentCompression
            );
            
            // COMPLETE viscoelastic response
            const viscoelasticResponse = this.calculateViscoelasticResponse(
                compression,
                cushion.dampingFactor,
                deltaTime
            );
            
            // COMPLETE cushion update
            cushion.currentCompression = compression;
            cushion.recoveryRate = viscoelasticResponse;
            
            // COMPLETE thermal effects
            this.updateCushionTemperature(cushion, pilotWeight, deltaTime);
        }
        
        return this.cushionSystem;
    }
    
    // MUST implement complete ejection sequence
    initiateEjectionSequence() {
        const sequence = [
            { action: 'canopy_jettison', delay: 0.0 },
            { action: 'seat_separation', delay: 0.1 },
            { action: 'rocket_ignition', delay: 0.15 },
            { action: 'drogue_deployment', delay: 0.5 },
            { action: 'main_chute_deployment', delay: 2.0 },
            { action: 'seat_separation', delay: 3.0 }
        ];
        
        // COMPLETE sequence execution
        for (const step of sequence) {
            this.scheduleEjectionStep(step.action, step.delay);
        }
        
        return sequence;
    }
}
```

ANIMATION SYSTEM:
MUST create complete animation controllers:

```javascript
class MechanicalAnimationController {
    constructor() {
        this.animationCurves = new AnimationCurves();
        this.interpolationEngine = new InterpolationEngine();
        this.constraintSolver = new ConstraintSolver();
    }
    
    // MUST implement complete mechanical animation
    animateMechanicalSystem(system, targetState, deltaTime) {
        // COMPLETE constraint solving
        const constrainedTarget = this.constraintSolver.solve(
            system.currentState,
            targetState,
            system.constraints
        );
        
        // COMPLETE interpolation
        const interpolatedState = this.interpolationEngine.interpolate(
            system.currentState,
            constrainedTarget,
            deltaTime,
            system.animationCurve
        );
        
        // COMPLETE physics integration
        const physicsState = this.integratePhysics(
            interpolatedState,
            system.physicsProperties,
            deltaTime
        );
        
        system.currentState = physicsState;
        
        return physicsState;
    }
}
```

VALIDATION REQUIREMENTS:
CURSOR MUST verify after implementation:
✓ All mechanical systems move realistically
✓ Control stick provides proper force feedback
✓ Switch mechanisms have realistic tactile response
✓ Seat adjustments work smoothly
✓ Physics simulation is stable and accurate
✓ Performance remains above 45 FPS
✓ All animations are smooth and natural
✓ Mechanical constraints are properly enforced

PERFORMANCE BENCHMARKS (MUST ACHIEVE):
✓ Mechanical physics: <3ms per frame
✓ Animation updates: <2ms per frame
✓ Constraint solving: <1ms per frame
✓ Force feedback: <0.5ms per update
✓ Switch actuation: <0.1ms per switch
✓ Seat adjustments: <1ms per adjustment
```

**GAP IDENTIFICATION FOR PHASE 3.3**:
```
CURSOR MUST CHECK FOR THESE CRITICAL GAPS:
❌ Unrealistic mechanical physics breaking immersion
❌ Poor force feedback reducing control realism
❌ Missing tactile response in switch operations
❌ Inadequate seat adjustment mechanisms
❌ Poor animation quality making movements look artificial
❌ Performance issues with complex physics simulation
❌ Missing mechanical constraints causing unrealistic behavior
❌ Inadequate wear and friction modeling
❌ Poor ejection sequence implementation
❌ Missing thermal effects on mechanical systems
```

## PHASE 3 COMPLETION CHECKLIST

### ✅ **VALIDATION REQUIREMENTS**
- [ ] Parametric cockpit geometry generates correctly
- [ ] Ergonomic calculations produce realistic results
- [ ] Display systems have pixel-level detail
- [ ] Multi-layer glass construction renders properly
- [ ] Environmental effects on glass are realistic
- [ ] HUD glass system functions correctly
- [ ] Mechanical systems move with realistic physics
- [ ] Control stick provides proper force feedback
- [ ] Switch mechanisms have tactile response
- [ ] Performance remains above 45 FPS

### ✅ **QUALITY GATES**
- [ ] All geometry renders without errors
- [ ] Optical properties are physically accurate
- [ ] Mechanical animations are smooth and natural
- [ ] Environmental effects enhance realism
- [ ] All systems integrate properly
- [ ] Memory usage is within acceptable limits
- [ ] All shaders compile without errors

### ✅ **PERFORMANCE BENCHMARKS**
- [ ] Geometry generation: <5s for complete cockpit
- [ ] Glass rendering: <5ms per frame
- [ ] Mechanical physics: <3ms per frame
- [ ] Environmental effects: <2ms per frame
- [ ] Animation updates: <2ms per frame
- [ ] Overall system: >45 FPS with all features

**PHASE 3 MUST BE 100% COMPLETE BEFORE PROCEEDING TO PHASE 4**
