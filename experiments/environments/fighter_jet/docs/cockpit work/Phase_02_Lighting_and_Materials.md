# PHASE 2: SCIENTIFIC LIGHTING & ADVANCED MATERIALS

## PRE-PHASE 2 VALIDATION:
```
CURSOR MUST VERIFY FROM PHASE 1:
✓ Advanced renderer is fully functional
✓ Asset streaming system works correctly
✓ All performance benchmarks are met
✓ Memory usage is within acceptable limits
✓ Error handling prevents crashes
✓ Loading system provides smooth user experience
✓ All features have proper fallbacks for limited hardware
```

## Prompt 2.1: Physically Accurate Lighting System Implementation

**PREREQUISITE VALIDATION**:
```
CURSOR MUST VERIFY:
✓ Advanced renderer supports HDR pipeline
✓ Shadow system is working correctly
✓ Post-processing pipeline is functional
✓ Asset manager can load HDRI environments
✓ Performance monitoring shows acceptable frame rates
```

**CURSOR RULES FOR THIS PROMPT**:
1. MUST implement scientifically accurate lighting models only
2. ALL calculations must be based on real-world photometry
3. MUST provide fallbacks for each advanced feature
4. Performance MUST remain above 45 FPS on target hardware

**DETAILED IMPLEMENTATION**:
```
Implement scientifically accurate lighting system based on real-world photometry:

MANDATORY LIGHTING SYSTEM COMPONENTS:

1. PHYSICALLY ACCURATE SUN/SKY MODEL (COMPLETE IMPLEMENTATION):
   Create LightingManager.js with FULL implementation:

   SUN POSITION CALCULATION:
   - MUST implement accurate solar position algorithm
   - MUST support any geographic location and date/time
   - MUST calculate proper elevation and azimuth angles
   - MUST account for atmospheric refraction
   - MUST implement equation of time corrections

   SKY MODEL (Hosek-Wilkie Implementation):
   - MUST implement complete Hosek-Wilkie sky model
   - MUST support all 9 atmospheric parameters
   - MUST calculate proper luminance and chromaticity
   - MUST account for solar disk luminance and size
   - MUST implement proper horizon brightening effects

2. ATMOSPHERIC SCATTERING (COMPLETE PHYSICS IMPLEMENTATION):
   - Rayleigh Scattering (FULL implementation):
     * MUST use proper wavelength-dependent coefficients
     * MUST implement proper phase function
     * MUST account for molecular density variation with altitude
   - Mie Scattering (COMPLETE implementation):
     * MUST implement proper aerosol distribution
     * MUST support variable aerosol types and concentrations
     * MUST implement proper forward scattering enhancement
   - Ozone Absorption (FULL UV implementation):
     * MUST implement proper ozone absorption spectrum
     * MUST account for stratospheric ozone distribution

3. INTERIOR LIGHTING SYSTEM (PHOTOMETRICALLY ACCURATE):
   - Instrument Panel Lighting:
     * MUST calculate proper illumination in lux
     * MUST implement realistic LED/fluorescent characteristics
     * MUST support variable color temperature (2700K-6500K)
     * MUST implement proper light distribution patterns
   - Display Backlighting:
     * MUST implement edge-lit LED simulation
     * MUST account for light guide properties
     * MUST implement proper backlight uniformity
     * MUST support variable brightness (1-1000 nits)

COMPLETE IMPLEMENTATION REQUIREMENTS:

LightingManager.js MUST implement:
```javascript
class LightingManager {
    constructor(renderer, sceneManager) {
        this.renderer = renderer;
        this.scene = sceneManager.scene;
        
        // COMPLETE sun/sky system
        this.sunCalculator = new SolarPositionCalculator();
        this.skyModel = new HosekWilkieSky();
        this.atmosphereRenderer = new AtmosphericScattering();
        
        // COMPLETE interior lighting
        this.instrumentLights = new InstrumentLighting();
        this.displayLights = new DisplayLighting();
        this.ambientSystem = new AmbientLightingSystem();
        
        // COMPLETE IBL system
        this.iblManager = new IBLManager();
        this.lightProbes = new LightProbeSystem();
        
        this.initializeLighting();
    }
    
    // MUST implement complete sun position calculation
    updateSunPosition(latitude, longitude, date, time) {
        const solarData = this.sunCalculator.calculate(latitude, longitude, date, time);
        
        // COMPLETE implementation with:
        // - Accurate solar elevation and azimuth
        // - Atmospheric refraction corrections  
        // - Equation of time adjustments
        // - Solar disk size and position
        // - Proper coordinate system conversions
        
        this.updateSunLight(solarData);
        this.updateSkyModel(solarData);
        this.updateAtmosphere(solarData);
    }
    
    // MUST implement complete Hosek-Wilkie sky model
    updateSkyModel(solarData) {
        // COMPLETE implementation of all 9 parameters:
        // - Solar elevation dependent coefficients
        // - Turbidity factor calculations
        // - Ground albedo considerations
        // - Luminance and chromaticity distributions
        // - Proper normalization and scaling
    }
    
    // MUST implement complete atmospheric scattering
    updateAtmosphericScattering(solarData) {
        // COMPLETE Rayleigh + Mie scattering with:
        // - Proper wavelength dependencies
        // - Atmospheric density profiles
        // - Phase function calculations
        // - Multiple scattering approximation
        // - Proper integration through atmosphere
    }
    
    // MUST implement complete interior lighting
    updateInteriorLighting(ambientLevel, timeOfDay) {
        // COMPLETE implementation with:
        // - Photometrically accurate calculations
        // - Proper color temperature mixing
        // - Realistic light distribution
        // - Power consumption modeling
        // - Dimming curve accuracy
    }
}

class SolarPositionCalculator {
    // MUST implement COMPLETE solar position algorithm
    calculate(latitude, longitude, date, time) {
        // COMPLETE SPA (Solar Position Algorithm) implementation
        // Based on NREL's high-precision algorithm
        // Accuracy: ±0.0003° for years 2000-6000
    }
}

class HosekWilkieSky {
    // MUST implement COMPLETE Hosek-Wilkie sky model
    constructor() {
        this.coefficientsA = this.loadCoefficientsA(); // ALL coefficients
        this.coefficientsB = this.loadCoefficientsB(); // ALL coefficients
        this.coefficientsC = this.loadCoefficientsC(); // ALL coefficients
        // ... all other coefficient sets
    }
    
    calculateSkyLuminance(theta, gamma, solarElevation, turbidity) {
        // COMPLETE implementation of sky luminance calculation
    }
    
    calculateSkyChromaticity(theta, gamma, solarElevation, turbidity) {
        // COMPLETE implementation of sky chromaticity calculation
    }
}
```

SHADER REQUIREMENTS:
MUST create complete shaders for:

atmospheric_scattering.frag:
```glsl
// COMPLETE atmospheric scattering implementation
// MUST implement both Rayleigh and Mie scattering
// MUST support variable atmospheric conditions
// MUST be optimized for real-time rendering

precision highp float;

uniform vec3 cameraPos;
uniform vec3 sunDirection;
uniform float sunIntensity;
uniform float atmosphereRadius;
uniform float planetRadius;
uniform vec3 betaRayleigh;
uniform vec3 betaMie;
uniform float mieG;
uniform float densityFalloff;

// COMPLETE implementation required - no placeholders
vec3 calculateScattering(vec3 viewDir) {
    // COMPLETE ray-sphere intersection
    // COMPLETE numerical integration through atmosphere
    // COMPLETE phase function calculations
    // COMPLETE multiple scattering approximation
}
```

VALIDATION REQUIREMENTS:
CURSOR MUST verify after implementation:
✓ Sun position matches real-world solar calculators
✓ Sky colors match photographic references
✓ Atmospheric perspective is visually convincing
✓ Interior lighting levels are realistic
✓ Color temperature mixing is accurate
✓ Performance remains above 45 FPS
✓ All shaders compile without warnings
✓ Lighting changes smoothly with time/location

PERFORMANCE BENCHMARKS (MUST ACHIEVE):
✓ Sky rendering: <3ms per frame
✓ Atmospheric scattering: <2ms per frame  
✓ Interior lighting: <1ms per frame
✓ IBL updates: <5ms when changed
✓ Total lighting overhead: <15% of frame time
```

**GAP IDENTIFICATION FOR PHASE 2.1**:
```
CURSOR MUST CHECK FOR THESE CRITICAL GAPS:
❌ Inaccurate sun position calculations affecting realism
❌ Poor sky model implementation reducing visual quality
❌ Missing atmospheric scattering breaking depth perception
❌ Unrealistic interior lighting destroying immersion
❌ Poor color temperature handling causing unrealistic colors
❌ Missing IBL support limiting material appearance
❌ Performance issues preventing smooth operation
❌ Shader compilation errors on different hardware
❌ Missing fallbacks for unsupported features
❌ Inadequate dynamic range causing blown highlights/crushed shadows
```

## Prompt 2.2: Advanced PBR+ Material System

**PREREQUISITE VALIDATION**:
```
CURSOR MUST VERIFY FROM PHASE 2.1:
✓ Lighting system is working correctly
✓ Sun/sky model produces realistic lighting
✓ Atmospheric scattering is visually convincing
✓ Interior lighting provides proper illumination
✓ Performance benchmarks are met
✓ All shaders compile without errors
```

**CURSOR RULES FOR THIS PROMPT**:
1. MUST implement physically accurate material models only
2. ALL materials must be based on real-world measurements  
3. MUST support all required maps and properties
4. Material quality MUST be indistinguishable from reference photos

**DETAILED IMPLEMENTATION**:
```
Create next-generation material system that exceeds standard PBR:

MANDATORY MATERIAL SYSTEM COMPONENTS:

1. ADVANCED PBR+ MATERIAL MODEL (COMPLETE IMPLEMENTATION):
   MaterialSystem.js MUST implement:

   CORE PBR+ PROPERTIES (ALL REQUIRED):
   - Albedo/Diffuse with proper gamma handling
   - Normal maps with tangent-space reconstruction
   - Roughness with anisotropic support
   - Metallic with proper conductor/dielectric handling
   - Ambient Occlusion with multiple sampling methods
   - Height/Displacement with tessellation support
   - Subsurface scattering for translucent materials
   - Emission with HDR luminance values

   ADVANCED MATERIAL FEATURES (ALL REQUIRED):
   - Clearcoat layers for automotive-grade finishes
   - Anisotropic reflectance for brushed metals
   - Iridescence for thin-film interference
   - Cloth/fabric shading models
   - Transmission for glass materials
   - Wet surface simulation

2. MATERIAL AGING & WEATHERING SYSTEM (COMPLETE IMPLEMENTATION):
   - Dynamic wear patterns based on usage simulation
   - Corrosion progression with chemical accuracy
   - Dust accumulation with particle physics
   - UV damage with spectral accuracy
   - Thermal stress with material science
   - Battle damage with procedural generation

COMPLETE IMPLEMENTATION REQUIREMENTS:

MaterialSystem.js MUST implement:
```javascript
class MaterialSystem {
    constructor(renderer, assetManager) {
        this.renderer = renderer;
        this.assetManager = assetManager;
        
        // COMPLETE material libraries
        this.metalMaterials = new MetalMaterialLibrary();
        this.plasticMaterials = new PlasticMaterialLibrary();
        this.glassMaterials = new GlassMaterialLibrary();
        this.fabricMaterials = new FabricMaterialLibrary();
        this.compositeMaterials = new CompositeMaterialLibrary();
        
        // COMPLETE advanced features
        this.weatheringSystem = new MaterialWeatheringSystem();
        this.agingSystem = new MaterialAgingSystem();
        this.damageSystem = new MaterialDamageSystem();
        
        // COMPLETE shader management
        this.shaderLibrary = new MaterialShaderLibrary();
        this.shaderCache = new ShaderCache();
        
        this.initializeMaterials();
    }
    
    // MUST implement complete material creation
    createMaterial(type, properties) {
        const material = new THREE.Material();
        
        // COMPLETE PBR+ property assignment
        this.assignAlbedoProperties(material, properties.albedo);
        this.assignNormalProperties(material, properties.normal);
        this.assignRoughnessProperties(material, properties.roughness);
        this.assignMetallicProperties(material, properties.metallic);
        this.assignAOProperties(material, properties.ao);
        this.assignDisplacementProperties(material, properties.displacement);
        this.assignSubsurfaceProperties(material, properties.subsurface);
        this.assignEmissionProperties(material, properties.emission);
        
        // COMPLETE advanced features
        this.assignClearcoatProperties(material, properties.clearcoat);
        this.assignAnisotropyProperties(material, properties.anisotropy);
        this.assignIridescenceProperties(material, properties.iridescence);
        this.assignTransmissionProperties(material, properties.transmission);
        
        this.validateMaterial(material);
        return material;
    }
    
    // MUST implement complete cockpit materials
    createCockpitMaterials() {
        return {
            // Aluminum materials with accurate optical properties
            brushedAluminum: this.createBrushedAluminumMaterial(),
            anodizedAluminum: this.createAnodizedAluminumMaterial(),
            
            // Steel materials with proper aging
            paintedSteel: this.createPaintedSteelMaterial(),
            stainlessSteel: this.createStainlessSteelMaterial(),
            
            // Plastic materials with realistic surface properties
            matteBlackPlastic: this.createMatteBlackPlasticMaterial(),
            glossyPlastic: this.createGlossyPlasticMaterial(),
            
            // Glass materials with multi-layer construction
            canopyGlass: this.createCanopyGlassMaterial(),
            instrumentGlass: this.createInstrumentGlassMaterial(),
            hudGlass: this.createHUDGlassMaterial(),
            
            // Composite materials
            carbonFiber: this.createCarbonFiberMaterial(),
            fiberglass: this.createFiberglassMaterial(),
            
            // Fabric materials
            seatFabric: this.createSeatFabricMaterial(),
            canvasStrap: this.createCanvasStrapMaterial(),
            
            // Electronic materials
            pcbMaterial: this.createPCBMaterial(),
            ledMaterial: this.createLEDMaterial()
        };
    }
    
    // MUST implement each material type completely
    createBrushedAluminumMaterial() {
        return this.createMaterial('metal', {
            albedo: {
                baseColor: new THREE.Color(0.913, 0.921, 0.925),
                texture: 'brushed_aluminum_albedo_4k.jpg',
                gamma: 2.2
            },
            normal: {
                texture: 'brushed_aluminum_normal_4k.jpg',
                strength: 0.8,
                flipY: false
            },
            roughness: {
                value: 0.3,
                texture: 'brushed_aluminum_roughness_4k.jpg',
                anisotropy: 0.9, // High anisotropy for brushed surface
                anisotropyRotation: 0.0 // Vertical brush marks
            },
            metallic: {
                value: 1.0 // Pure metal
            },
            // COMPLETE implementation for all properties...
        });
    }
}

class MaterialWeatheringSystem {
    constructor() {
        this.corrosionModels = new CorrosionModels();
        this.wearSimulation = new WearSimulation();
        this.uvDamageModel = new UVDamageModel();
        this.dustAccumulation = new DustAccumulationModel();
    }
    
    // MUST implement complete weathering simulation
    applyWeathering(material, conditions, timeElapsed) {
        // COMPLETE weathering implementation:
        // - Chemical corrosion based on material properties
        // - Mechanical wear from usage patterns
        // - UV degradation with spectral accuracy
        // - Dust accumulation with electrostatic forces
        // - Temperature cycling effects
        // - Humidity exposure effects
    }
}
```

SHADER REQUIREMENTS:
MUST create complete PBR+ shaders:

pbr_plus_vertex.glsl:
```glsl
// COMPLETE PBR+ vertex shader
#version 300 es
precision highp float;

// ALL required attributes
in vec3 position;
in vec3 normal;
in vec2 uv;
in vec4 tangent;
in vec3 color;

// ALL required uniforms
uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;
uniform mat3 normalMatrix;

// ALL required outputs
out vec3 vWorldPosition;
out vec3 vWorldNormal;
out vec2 vUv;
out vec3 vTangent;
out vec3 vBitangent;
out vec3 vColor;

// COMPLETE implementation - no placeholders
void main() {
    // COMPLETE vertex transformation
    vec4 worldPosition = modelMatrix * vec4(position, 1.0);
    vWorldPosition = worldPosition.xyz;
    
    // COMPLETE normal transformation
    vWorldNormal = normalize(normalMatrix * normal);
    
    // COMPLETE tangent space calculation
    vTangent = normalize(normalMatrix * tangent.xyz);
    vBitangent = normalize(cross(vWorldNormal, vTangent) * tangent.w);
    
    // COMPLETE UV and color pass-through
    vUv = uv;
    vColor = color;
    
    gl_Position = projectionMatrix * viewMatrix * worldPosition;
}
```

pbr_plus_fragment.glsl:
```glsl
// COMPLETE PBR+ fragment shader
#version 300 es
precision highp float;

// ALL required inputs
in vec3 vWorldPosition;
in vec3 vWorldNormal;
in vec2 vUv;
in vec3 vTangent;
in vec3 vBitangent;
in vec3 vColor;

// ALL required uniforms
uniform vec3 cameraPosition;
uniform vec3 albedo;
uniform float metallic;
uniform float roughness;
uniform float ao;
uniform vec3 emissive;

// ALL texture uniforms
uniform sampler2D albedoMap;
uniform sampler2D normalMap;
uniform sampler2D roughnessMap;
uniform sampler2D metallicMap;
uniform sampler2D aoMap;
uniform sampler2D heightMap;
uniform sampler2D emissiveMap;

// ADVANCED feature uniforms
uniform float clearcoat;
uniform float clearcoatRoughness;
uniform sampler2D clearcoatMap;
uniform sampler2D clearcoatRoughnessMap;
uniform sampler2D clearcoatNormalMap;

uniform float anisotropy;
uniform float anisotropyRotation;

uniform float iridescence;
uniform float iridescenceIOR;
uniform float iridescenceThicknessMin;
uniform float iridescenceThicknessMax;
uniform sampler2D iridescenceMap;
uniform sampler2D iridescenceThicknessMap;

// LIGHTING uniforms
uniform vec3 lightPositions[8];
uniform vec3 lightColors[8];
uniform float lightIntensities[8];
uniform int numLights;

// IBL uniforms
uniform samplerCube envMap;
uniform samplerCube irradianceMap;
uniform sampler2D brdfLUT;

out vec4 fragColor;

// COMPLETE BRDF implementations
vec3 calculateFresnelSchlick(float cosTheta, vec3 F0) {
    // COMPLETE Fresnel calculation
}

float calculateDistributionGGX(vec3 N, vec3 H, float roughness) {
    // COMPLETE GGX distribution function
}

float calculateGeometrySchlickGGX(float NdotV, float roughness) {
    // COMPLETE Schlick-GGX geometry function
}

vec3 calculatePBRLighting(vec3 albedo, float metallic, float roughness, vec3 normal, vec3 viewDir) {
    // COMPLETE PBR lighting calculation with:
    // - Cook-Torrance BRDF
    // - Multiple light support  
    // - Image-based lighting
    // - Energy conservation
    // - Proper Fresnel handling
}

vec3 calculateClearcoat(vec3 baseColor, vec3 normal, vec3 viewDir, float clearcoat, float clearcoatRoughness) {
    // COMPLETE clearcoat implementation
}

vec3 calculateAnisotropy(vec3 normal, vec3 tangent, vec3 bitangent, float anisotropy, float anisotropyRotation) {
    // COMPLETE anisotropic reflection calculation
}

vec3 calculateIridescence(float iridescence, float iridescenceIOR, float thickness, float NdotV) {
    // COMPLETE thin-film interference calculation
}

void main() {
    // COMPLETE material property sampling
    vec4 albedoSample = texture(albedoMap, vUv);
    vec3 materialAlbedo = albedo * albedoSample.rgb * vColor;
    
    vec3 normalSample = texture(normalMap, vUv).rgb * 2.0 - 1.0;
    vec3 materialNormal = normalize(vTangent * normalSample.x + vBitangent * normalSample.y + vWorldNormal * normalSample.z);
    
    float materialRoughness = roughness * texture(roughnessMap, vUv).r;
    float materialMetallic = metallic * texture(metallicMap, vUv).r;
    float materialAO = ao * texture(aoMap, vUv).r;
    vec3 materialEmissive = emissive * texture(emissiveMap, vUv).rgb;
    
    // COMPLETE advanced feature sampling
    float materialClearcoat = clearcoat * texture(clearcoatMap, vUv).r;
    float materialClearcoatRoughness = clearcoatRoughness * texture(clearcoatRoughnessMap, vUv).r;
    
    float materialIridescence = iridescence * texture(iridescenceMap, vUv).r;
    float iridescenceThickness = mix(iridescenceThicknessMin, iridescenceThicknessMax, texture(iridescenceThicknessMap, vUv).r);
    
    // COMPLETE lighting calculation
    vec3 viewDir = normalize(cameraPosition - vWorldPosition);
    vec3 finalColor = calculatePBRLighting(materialAlbedo, materialMetallic, materialRoughness, materialNormal, viewDir);
    
    // COMPLETE advanced feature application
    if (materialClearcoat > 0.0) {
        finalColor = calculateClearcoat(finalColor, materialNormal, viewDir, materialClearcoat, materialClearcoatRoughness);
    }
    
    if (anisotropy > 0.0) {
        finalColor = calculateAnisotropy(materialNormal, normalize(vTangent), normalize(vBitangent), anisotropy, anisotropyRotation);
    }
    
    if (materialIridescence > 0.0) {
        vec3 iridescenceColor = calculateIridescence(materialIridescence, iridescenceIOR, iridescenceThickness, dot(materialNormal, viewDir));
        finalColor = mix(finalColor, iridescenceColor, materialIridescence);
    }
    
    // COMPLETE final color assembly
    finalColor += materialEmissive;
    finalColor *= materialAO;
    
    fragColor = vec4(finalColor, albedoSample.a);
}
```

VALIDATION REQUIREMENTS:
CURSOR MUST verify after implementation:
✓ All materials render without errors
✓ PBR calculations are energy-conserving
✓ Material properties match reference images
✓ Advanced features work correctly
✓ Weathering system produces realistic results
✓ Performance remains above target FPS
✓ All shaders compile on target hardware
✓ Material switching works smoothly

PERFORMANCE BENCHMARKS (MUST ACHIEVE):
✓ Material shader compilation: <500ms total
✓ Per-material rendering overhead: <0.1ms
✓ Texture memory usage: <512MB for all materials
✓ Material switching: <1ms delay
✓ Weathering calculations: <1ms per material per frame
```

**GAP IDENTIFICATION FOR PHASE 2.2**:
```
CURSOR MUST CHECK FOR THESE CRITICAL GAPS:
❌ Inaccurate PBR implementation reducing visual realism
❌ Missing advanced material features limiting quality
❌ Poor shader performance impacting frame rate
❌ Incorrect material properties making surfaces look fake
❌ Missing weathering effects reducing authenticity
❌ Inadequate texture resolution causing visible pixelation
❌ Poor normal mapping reducing surface detail
❌ Missing anisotropy making metals look unrealistic
❌ Incorrect Fresnel calculations affecting reflections
❌ Poor clearcoat implementation reducing paint quality
```

## Prompt 2.3: Surface Micro-Detail & Procedural Systems

**PREREQUISITE VALIDATION**:
```
CURSOR MUST VERIFY FROM PHASE 2.2:
✓ Material system is working correctly
✓ All PBR+ features are functional
✓ Advanced material properties are rendering properly
✓ Weathering system produces realistic results
✓ Performance benchmarks are met
✓ All shaders compile without errors
✓ Material quality matches reference standards
```

**CURSOR RULES FOR THIS PROMPT**:
1. MUST implement multi-scale detail systems for extreme close-up viewing
2. ALL procedural systems must be deterministic and reproducible
3. MUST maintain performance while adding microscopic detail
4. Detail quality must be indistinguishable from reality at all viewing distances

**DETAILED IMPLEMENTATION**:
```
Implement microscopic surface detail for extreme close-up realism:

MANDATORY MICRO-DETAIL SYSTEMS:

1. MULTI-SCALE SURFACE DETAIL (COMPLETE IMPLEMENTATION):
   SurfaceDetailSystem.js MUST implement:

   MACRO DETAIL (visible at arm's length - 0.5-2m):
   - Panel lines and manufacturing seams
   - Rivet and fastener details with proper shadowing
   - Surface imperfections and manufacturing variations
   - Wear patterns from repeated use
   - Installation marks and assembly residue

   MICRO DETAIL (visible at close inspection - 0.1-0.5m):
   - Surface texture variations (orange peel, brush marks)
   - Microscopic scratches and scuff marks
   - Dust and particle accumulation in crevices
   - Fingerprint oils and skin contact residue
   - Static electricity dust attraction patterns
   - Manufacturing tool marks and surface finishing

   NANO DETAIL (shader-level - <0.1m):
   - Fresnel effects with proper IOR values
   - Surface roughness variation at sub-pixel level
   - Anisotropic reflection direction variation
   - Subsurface scattering depth variation
   - Clearcoat thickness variation
   - Environmental reflection distortion

2. PROCEDURAL DETAIL GENERATION (COMPLETE IMPLEMENTATION):
   - Noise-based surface generation at multiple octaves
   - Usage-pattern simulation for realistic wear
   - Environmental factor influence (humidity, temperature)
   - Contact-based detail accumulation
   - Time-based aging and degradation

COMPLETE IMPLEMENTATION REQUIREMENTS:

SurfaceDetailSystem.js MUST implement:
```javascript
class SurfaceDetailSystem {
    constructor(renderer, materialSystem) {
        this.renderer = renderer;
        this.materialSystem = materialSystem;
        
        // COMPLETE detail generators
        this.macroDetailGenerator = new MacroDetailGenerator();
        this.microDetailGenerator = new MicroDetailGenerator();
        this.nanoDetailGenerator = new NanoDetailGenerator();
        
        // COMPLETE procedural systems
        this.noiseGenerator = new MultiOctaveNoiseGenerator();
        this.wearSimulator = new WearPatternSimulator();
        this.dustAccumulator = new DustAccumulationSystem();
        this.fingerprintGenerator = new FingerprintGenerator();
        
        // COMPLETE detail management
        this.lodManager = new DetailLODManager();
        this.detailCache = new DetailCache();
        
        this.initializeDetailSystems();
    }
    
    // MUST implement complete macro detail generation
    generateMacroDetails(geometry, materialType, usageLevel) {
        const details = {
            panelLines: this.generatePanelLines(geometry),
            rivets: this.generateRivets(geometry, materialType),
            seams: this.generateManufacturingSeams(geometry),
            wearPatterns: this.generateWearPatterns(geometry, usageLevel),
            imperfections: this.generateManufacturingImperfections(geometry)
        };
        
        // COMPLETE detail integration with geometry
        this.integrateDetailsWithGeometry(geometry, details);
        return details;
    }
    
    // MUST implement complete panel line generation
    generatePanelLines(geometry) {
        // COMPLETE implementation with:
        // - Realistic panel sizes based on manufacturing constraints
        // - Proper depth and width for different materials
        // - Consistent spacing and alignment
        // - Material-appropriate sealing compounds
        // - Weathering effects on panel lines
        
        const panelLines = [];
        const faces = geometry.faces;
        
        for (let i = 0; i < faces.length; i += 50) { // Every 50th face gets a panel line
            const face = faces[i];
            const edge = this.calculatePanelLineEdge(face);
            const depth = this.calculatePanelLineDepth(face.materialIndex);
            const width = this.calculatePanelLineWidth(face.materialIndex);
            
            panelLines.push({
                edge: edge,
                depth: depth,
                width: width,
                sealant: this.generateSealantProperties(face.materialIndex),
                weathering: this.calculateWeathering(face.normal, face.centroid)
            });
        }
        
        return panelLines;
    }
    
    // MUST implement complete rivet generation
    generateRivets(geometry, materialType) {
        // COMPLETE implementation with:
        // - Proper rivet spacing based on structural requirements
        // - Material-appropriate rivet types and sizes
        // - Realistic head shapes and profiles
        // - Installation marks and deformation
        // - Corrosion patterns around rivets
        
        const rivets = [];
        const rivetSpacing = this.calculateRivetSpacing(materialType);
        const rivetType = this.selectRivetType(materialType);
        
        // Generate rivets along panel edges and structural lines
        const structuralLines = this.identifyStructuralLines(geometry);
        
        for (const line of structuralLines) {
            const rivetPositions = this.distributeRivetsAlongLine(line, rivetSpacing);
            
            for (const position of rivetPositions) {
                rivets.push({
                    position: position,
                    type: rivetType,
                    diameter: this.calculateRivetDiameter(materialType),
                    headProfile: this.generateRivetHeadProfile(rivetType),
                    installationMarks: this.generateInstallationMarks(),
                    corrosion: this.generateRivetCorrosion(position, materialType)
                });
            }
        }
        
        return rivets;
    }
    
    // MUST implement complete micro detail generation
    generateMicroDetails(surface, viewingDistance, lightingConditions) {
        if (viewingDistance > 0.5) return null; // LOD optimization
        
        const microDetails = {
            surfaceTexture: this.generateSurfaceTexture(surface),
            scratches: this.generateMicroscratches(surface),
            dust: this.generateDustAccumulation(surface, lightingConditions),
            fingerprints: this.generateFingerprints(surface),
            staticDust: this.generateStaticElectricityEffects(surface)
        };
        
        return this.combineMicroDetails(microDetails);
    }
    
    // MUST implement complete surface texture generation
    generateSurfaceTexture(surface) {
        const materialType = surface.materialType;
        let texture;
        
        switch (materialType) {
            case 'brushed_aluminum':
                texture = this.generateBrushedAluminumTexture(surface);
                break;
            case 'painted_steel':
                texture = this.generatePaintedSteelTexture(surface);
                break;
            case 'matte_plastic':
                texture = this.generateMattePlasticTexture(surface);
                break;
            // COMPLETE implementation for all material types
        }
        
        return texture;
    }
    
    // MUST implement complete brushed aluminum texture
    generateBrushedAluminumTexture(surface) {
        // COMPLETE implementation with:
        // - Proper brush mark direction and spacing
        // - Realistic brush mark depth and width
        // - Anisotropic reflection properties
        // - Manufacturing tool mark variations
        // - Oxidation patterns in brush valleys
        
        const brushDirection = surface.brushDirection || new THREE.Vector3(0, 1, 0);
        const brushSpacing = 0.05; // 50 microns
        const brushDepth = 0.002; // 2 microns
        
        const textureData = new Uint8Array(1024 * 1024 * 4);
        
        for (let y = 0; y < 1024; y++) {
            for (let x = 0; x < 1024; x++) {
                const brushValue = this.calculateBrushMarkValue(x, y, brushDirection, brushSpacing, brushDepth);
                const oxidationValue = this.calculateOxidationValue(x, y, brushValue);
                
                const index = (y * 1024 + x) * 4;
                textureData[index] = brushValue; // Height
                textureData[index + 1] = oxidationValue; // Oxidation
                textureData[index + 2] = this.calculateAnisotropyValue(brushValue); // Anisotropy
                textureData[index + 3] = 255; // Alpha
            }
        }
        
        return new THREE.DataTexture(textureData, 1024, 1024, THREE.RGBAFormat);
    }
}

class WearPatternSimulator {
    constructor() {
        this.contactAreas = new Map();
        this.wearRates = new Map();
        this.materialHardness = new Map();
    }
    
    // MUST implement complete wear simulation
    simulateWear(surface, usageHistory, timeElapsed) {
        // COMPLETE wear simulation with:
        // - Contact pressure distribution
        // - Material hardness considerations
        // - Friction coefficient calculations
        // - Abrasive particle effects
        // - Chemical wear processes
        // - Fatigue and stress concentration
        
        const wearPattern = new WearPattern();
        
        for (const contact of usageHistory.contacts) {
            const localWear = this.calculateLocalWear(
                surface,
                contact.position,
                contact.pressure,
                contact.duration,
                contact.frictionCoefficient,
                timeElapsed
            );
            
            wearPattern.addLocalWear(contact.position, localWear);
        }
        
        return wearPattern;
    }
    
    calculateLocalWear(surface, position, pressure, duration, friction, timeElapsed) {
        const materialHardness = this.getMaterialHardness(surface.materialType);
        const wearCoefficient = this.getWearCoefficient(surface.materialType);
        
        // Archard's wear equation: V = K * W * s / H
        // V = wear volume, K = wear coefficient, W = applied load
        // s = sliding distance, H = hardness
        
        const appliedLoad = pressure * surface.getContactArea(position);
        const slidingDistance = friction * duration * surface.getSurfaceVelocity(position);
        
        const wearVolume = (wearCoefficient * appliedLoad * slidingDistance) / materialHardness;
        
        return {
            volume: wearVolume,
            depth: wearVolume / surface.getContactArea(position),
            pattern: this.calculateWearPattern(friction, pressure),
            colorChange: this.calculateColorChange(wearVolume, surface.materialType)
        };
    }
}
```

SHADER REQUIREMENTS:
MUST create complete detail shaders:

surface_detail_vertex.glsl:
```glsl
#version 300 es
precision highp float;

in vec3 position;
in vec3 normal;
in vec2 uv;
in vec4 tangent;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;
uniform mat3 normalMatrix;
uniform float time;

// Detail uniforms
uniform float detailScale1;
uniform float detailScale2;
uniform float detailScale3;

out vec3 vWorldPosition;
out vec3 vWorldNormal;
out vec2 vUv;
out vec2 vDetailUv1;
out vec2 vDetailUv2;
out vec2 vDetailUv3;
out vec3 vTangent;
out vec3 vBitangent;
out float vViewDistance;

void main() {
    vec4 worldPosition = modelMatrix * vec4(position, 1.0);
    vWorldPosition = worldPosition.xyz;
    vWorldNormal = normalize(normalMatrix * normal);
    
    // Calculate view distance for LOD
    vec3 viewPosition = (viewMatrix * worldPosition).xyz;
    vViewDistance = length(viewPosition);
    
    // Multi-scale UV coordinates
    vUv = uv;
    vDetailUv1 = uv * detailScale1;
    vDetailUv2 = uv * detailScale2;
    vDetailUv3 = uv * detailScale3;
    
    // Tangent space
    vTangent = normalize(normalMatrix * tangent.xyz);
    vBitangent = normalize(cross(vWorldNormal, vTangent) * tangent.w);
    
    gl_Position = projectionMatrix * viewMatrix * worldPosition;
}
```

surface_detail_fragment.glsl:
```glsl
#version 300 es
precision highp float;

in vec3 vWorldPosition;
in vec3 vWorldNormal;
in vec2 vUv;
in vec2 vDetailUv1;
in vec2 vDetailUv2;
in vec2 vDetailUv3;
in vec3 vTangent;
in vec3 vBitangent;
in float vViewDistance;

// Base material textures
uniform sampler2D albedoMap;
uniform sampler2D normalMap;
uniform sampler2D roughnessMap;

// Detail textures
uniform sampler2D macroDetailMap;
uniform sampler2D microDetailMap;
uniform sampler2D nanoDetailMap;

// Detail parameters
uniform float macroDetailStrength;
uniform float microDetailStrength;
uniform float nanoDetailStrength;
uniform float detailFadeStart;
uniform float detailFadeEnd;

out vec4 fragColor;

// COMPLETE noise functions for procedural detail
float random(vec2 st) {
    return fract(sin(dot(st.xy, vec2(12.9898, 78.233))) * 43758.5453123);
}

float noise(vec2 st) {
    vec2 i = floor(st);
    vec2 f = fract(st);
    
    float a = random(i);
    float b = random(i + vec2(1.0, 0.0));
    float c = random(i + vec2(0.0, 1.0));
    float d = random(i + vec2(1.0, 1.0));
    
    vec2 u = f * f * (3.0 - 2.0 * f);
    
    return mix(a, b, u.x) + (c - a) * u.y * (1.0 - u.x) + (d - b) * u.x * u.y;
}

float fbm(vec2 st) {
    float value = 0.0;
    float amplitude = 0.5;
    
    for (int i = 0; i < 8; i++) {
        value += amplitude * noise(st);
        st *= 2.0;
        amplitude *= 0.5;
    }
    
    return value;
}

// COMPLETE surface detail calculation
vec3 calculateSurfaceDetails(vec2 uv, vec3 normal, vec3 tangent, vec3 bitangent) {
    // Calculate LOD based on view distance
    float detailLOD = smoothstep(detailFadeStart, detailFadeEnd, vViewDistance);
    
    // Sample detail textures
    vec3 macroDetail = texture(macroDetailMap, vDetailUv1).rgb;
    vec3 microDetail = texture(microDetailMap, vDetailUv2).rgb;
    vec3 nanoDetail = texture(nanoDetailMap, vDetailUv3).rgb;
    
    // Procedural detail generation
    float proceduralNoise = fbm(uv * 100.0);
    float surfaceVariation = fbm(uv * 500.0);
    
    // Combine details based on view distance
    vec3 combinedDetail = vec3(0.0);
    
    // Macro details (always visible)
    combinedDetail += macroDetail * macroDetailStrength;
    
    // Micro details (fade out with distance)
    combinedDetail += microDetail * microDetailStrength * (1.0 - smoothstep(0.5, 2.0, vViewDistance));
    
    // Nano details (only visible up close)
    combinedDetail += nanoDetail * nanoDetailStrength * (1.0 - smoothstep(0.1, 0.5, vViewDistance));
    
    // Procedural details
    combinedDetail += vec3(proceduralNoise) * 0.1 * (1.0 - detailLOD);
    combinedDetail += vec3(surfaceVariation) * 0.05 * (1.0 - smoothstep(0.05, 0.2, vViewDistance));
    
    // Convert height variation to normal perturbation
    vec3 detailNormal = normalize(normal + 
        tangent * combinedDetail.x * 0.1 + 
        bitangent * combinedDetail.y * 0.1);
    
    return detailNormal;
}

// COMPLETE wear pattern calculation
vec3 calculateWearEffects(vec2 uv, vec3 baseColor, float roughness) {
    // Simulate wear based on surface accessibility and friction
    float wearFactor = smoothstep(0.3, 0.7, random(uv * 50.0));
    
    // Areas of high wear show underlying material
    vec3 wornColor = mix(baseColor, vec3(0.8, 0.8, 0.9), wearFactor * 0.3);
    
    // Worn areas are smoother
    float wornRoughness = mix(roughness, roughness * 0.5, wearFactor);
    
    return wornColor;
}

// COMPLETE dust accumulation calculation
float calculateDustAccumulation(vec2 uv, vec3 normal) {
    // Dust accumulates in horizontal surfaces and crevices
    float horizontalFactor = 1.0 - abs(dot(normal, vec3(0.0, 1.0, 0.0)));
    
    // Add random dust particles
    float dustNoise = fbm(uv * 200.0);
    float dustAccumulation = horizontalFactor * dustNoise * 0.2;
    
    // Dust in corners and crevices
    float cornerFactor = smoothstep(0.8, 1.0, random(uv * 100.0));
    dustAccumulation += cornerFactor * 0.1;
    
    return clamp(dustAccumulation, 0.0, 1.0);
}

void main() {
    // Sample base material properties
    vec4 albedoSample = texture(albedoMap, vUv);
    vec3 normalSample = texture(normalMap, vUv).rgb * 2.0 - 1.0;
    float roughnessSample = texture(roughnessMap, vUv).r;
    
    // Calculate detailed surface normal
    vec3 detailedNormal = calculateSurfaceDetails(vUv, vWorldNormal, vTangent, vBitangent);
    
    // Apply wear effects
    vec3 albedoWithWear = calculateWearEffects(vUv, albedoSample.rgb, roughnessSample);
    
    // Apply dust accumulation
    float dustLevel = calculateDustAccumulation(vUv, detailedNormal);
    vec3 finalAlbedo = mix(albedoWithWear, vec3(0.4, 0.4, 0.35), dustLevel * 0.3);
    
    // Output final surface properties
    fragColor = vec4(finalAlbedo, albedoSample.a);
}
```

VALIDATION REQUIREMENTS:
CURSOR MUST verify after implementation:
✓ Multi-scale details are visible at appropriate distances
✓ Procedural systems generate consistent, realistic patterns
✓ Performance remains acceptable with all detail levels
✓ Detail fading works smoothly with view distance
✓ Wear patterns look realistic and material-appropriate
✓ Dust accumulation follows physical principles
✓ All detail shaders compile without errors
✓ Detail quality enhances realism without overwhelming

PERFORMANCE BENCHMARKS (MUST ACHIEVE):
✓ Detail generation: <10ms per surface
✓ Detail rendering overhead: <20% additional cost
✓ Memory usage for details: <256MB additional
✓ Detail LOD transitions: Imperceptible to user
✓ Procedural calculations: <5ms per frame
✓ Overall frame rate: >45 FPS with all details active
```

**GAP IDENTIFICATION FOR PHASE 2.3**:
```
CURSOR MUST CHECK FOR THESE CRITICAL GAPS:
❌ Missing multi-scale detail causing unrealistic appearance at close viewing
❌ Poor procedural generation creating repetitive or artificial patterns
❌ Inadequate LOD system causing performance issues
❌ Missing wear simulation reducing authenticity
❌ Poor dust accumulation breaking immersion
❌ Inadequate surface variation making materials look uniform
❌ Missing microscopic detail reducing close-up realism
❌ Poor noise functions creating obvious patterns
❌ Performance impact too high preventing smooth operation
❌ Detail transitions causing visual popping or discontinuities
```

## PHASE 2 COMPLETION CHECKLIST

### ✅ **VALIDATION REQUIREMENTS**
- [ ] Lighting system produces realistic illumination
- [ ] Sun/sky model matches real-world references
- [ ] Atmospheric scattering is visually convincing
- [ ] Interior lighting provides proper illumination levels
- [ ] All materials render with photorealistic quality
- [ ] PBR+ features work correctly (clearcoat, anisotropy, etc.)
- [ ] Weathering system produces authentic aging effects
- [ ] Multi-scale surface details enhance realism
- [ ] Performance remains above 45 FPS

### ✅ **QUALITY GATES**
- [ ] Sun position matches solar calculators
- [ ] Sky colors match photographic references
- [ ] Material properties match reference images
- [ ] Advanced material features functional
- [ ] Detail systems work at all viewing distances
- [ ] All shaders compile without errors
- [ ] Smooth performance with all features active

### ✅ **PERFORMANCE BENCHMARKS**
- [ ] Sky rendering: <3ms per frame
- [ ] Atmospheric scattering: <2ms per frame
- [ ] Interior lighting: <1ms per frame
- [ ] Material shader compilation: <500ms total
- [ ] Per-material rendering: <0.1ms overhead
- [ ] Detail generation: <10ms per surface
- [ ] Overall lighting overhead: <15% of frame time

**PHASE 2 MUST BE 100% COMPLETE BEFORE PROCEEDING TO PHASE 3**
