# PHASE 5: ADVANCED SHADER PROGRAMMING & VISUAL EFFECTS

## PRE-PHASE 5 VALIDATION:
```
CURSOR MUST VERIFY FROM PHASE 4:
✓ All display systems render with photorealistic quality
✓ Avionics data provides realistic flight information
✓ HUD system functions with military-specification accuracy
✓ Text rendering is ultra-sharp and clear
✓ Performance benchmarks are met (>45 FPS)
✓ All display shaders compile without errors
✓ Memory usage is within acceptable limits
```

## Prompt 5.1: Custom Shader Library Development

**PREREQUISITE VALIDATION**:
```
CURSOR MUST VERIFY:
✓ Advanced renderer supports custom shader compilation
✓ Material system can integrate custom shaders
✓ Asset manager can load shader source files
✓ Performance monitoring shows acceptable baseline
✓ All previous shaders are working correctly
```

**CURSOR RULES FOR THIS PROMPT**:
1. MUST develop comprehensive library of custom shaders for photorealistic rendering
2. ALL shaders must be optimized for real-time performance
3. MUST support advanced BRDF models and lighting techniques
4. Shader quality must exceed standard PBR implementations

**DETAILED IMPLEMENTATION**:
```
Develop a comprehensive library of custom shaders for photorealistic rendering:

MANDATORY SHADER LIBRARY COMPONENTS:

1. ADVANCED MATERIAL SHADERS (COMPLETE IMPLEMENTATION):
   MaterialShaderLibrary.js MUST implement:

   PBR+ SHADER MODELS:
   - Cook-Torrance with multiple scattering compensation
   - Ashikhmin-Shirley anisotropic BRDF for brushed metals
   - Cloth shading with forward/backward scattering simulation
   - Subsurface scattering with proper light transport modeling
   - Clearcoat with proper multiple layer interaction physics
   - Iridescence with thin-film interference calculations

   SURFACE DETAIL SHADERS:
   - Parallax occlusion mapping with self-shadowing
   - Tessellation shaders for true surface displacement
   - Procedural surface noise generation at multiple scales
   - Dynamic surface weathering and aging simulation
   - Contact shadows for fine surface details
   - Micro-normal detail blending at multiple scales

2. ATMOSPHERIC AND ENVIRONMENTAL SHADERS (COMPLETE IMPLEMENTATION):
   EnvironmentalShaderLibrary.js MUST implement:

   ATMOSPHERIC EFFECTS:
   - Volumetric atmospheric scattering (Rayleigh + Mie)
   - Volumetric fog with proper light integration
   - God rays with proper light shaft calculation
   - Heat haze distortion with proper refraction physics
   - Atmospheric perspective with proper color shifts
   - Dynamic cloud rendering with proper light scattering

3. DISPLAY AND ELECTRONICS SHADERS (COMPLETE IMPLEMENTATION):
   ElectronicsShaderLibrary.js MUST implement:

   DISPLAY SIMULATION:
   - CRT phosphor simulation with proper persistence curves
   - LCD subpixel rendering with backlight simulation
   - OLED pixel perfect rendering with true black levels
   - LED and indicator light simulation with proper light distribution
   - Screen-space reflections for glass surfaces
   - Fresnel-based transparency with proper IOR handling

COMPLETE IMPLEMENTATION REQUIREMENTS:

MaterialShaderLibrary.js MUST implement:
```javascript
class MaterialShaderLibrary {
    constructor(renderer) {
        this.renderer = renderer;
        
        // COMPLETE shader categories
        this.pbrShaders = new PBRShaderCollection();
        this.surfaceDetailShaders = new SurfaceDetailShaderCollection();
        this.specialEffectShaders = new SpecialEffectShaderCollection();
        
        // COMPLETE shader management
        this.shaderCompiler = new ShaderCompiler();
        this.shaderCache = new ShaderCache();
        this.shaderValidator = new ShaderValidator();
        
        // COMPLETE shader optimization
        this.shaderOptimizer = new ShaderOptimizer();
        this.performanceProfiler = new ShaderPerformanceProfiler();
        
        this.initializeShaderLibrary();
    }
    
    // MUST implement complete shader compilation
    compileShader(shaderSource, shaderType, defines = {}) {
        // COMPLETE preprocessing
        const preprocessedSource = this.preprocessShader(shaderSource, defines);
        
        // COMPLETE validation
        this.validateShaderSource(preprocessedSource, shaderType);
        
        // COMPLETE optimization
        const optimizedSource = this.optimizeShader(preprocessedSource, shaderType);
        
        // COMPLETE compilation
        const compiledShader = this.shaderCompiler.compile(optimizedSource, shaderType);
        
        // COMPLETE caching
        this.cacheShader(compiledShader, shaderSource, defines);
        
        return compiledShader;
    }
    
    // MUST implement complete PBR+ shader
    createAdvancedPBRShader(materialType, features = {}) {
        const shaderDefines = this.generateShaderDefines(materialType, features);
        
        const vertexShader = this.generatePBRVertexShader(shaderDefines);
        const fragmentShader = this.generatePBRFragmentShader(shaderDefines);
        
        // COMPLETE shader program creation
        const shaderProgram = new THREE.ShaderMaterial({
            vertexShader: vertexShader,
            fragmentShader: fragmentShader,
            uniforms: this.generatePBRUniforms(materialType, features),
            defines: shaderDefines
        });
        
        return shaderProgram;
    }
    
    // MUST implement complete PBR fragment shader generation
    generatePBRFragmentShader(defines) {
        let fragmentShader = `
            #version 300 es
            precision highp float;
            
            // COMPLETE input variables
            in vec3 vWorldPosition;
            in vec3 vWorldNormal;
            in vec2 vUv;
            in vec3 vTangent;
            in vec3 vBitangent;
            in vec3 vViewPosition;
            
            // COMPLETE uniforms
            uniform vec3 cameraPosition;
            uniform vec3 albedo;
            uniform float metallic;
            uniform float roughness;
            uniform float ao;
            uniform vec3 emissive;
            
            // COMPLETE texture uniforms
            uniform sampler2D albedoMap;
            uniform sampler2D normalMap;
            uniform sampler2D roughnessMap;
            uniform sampler2D metallicMap;
            uniform sampler2D aoMap;
            uniform sampler2D emissiveMap;
            
            ${defines.USE_CLEARCOAT ? `
                uniform float clearcoat;
                uniform float clearcoatRoughness;
                uniform sampler2D clearcoatMap;
                uniform sampler2D clearcoatRoughnessMap;
                uniform sampler2D clearcoatNormalMap;
            ` : ''}
            
            ${defines.USE_ANISOTROPY ? `
                uniform float anisotropy;
                uniform float anisotropyRotation;
                uniform sampler2D anisotropyMap;
            ` : ''}
            
            ${defines.USE_IRIDESCENCE ? `
                uniform float iridescence;
                uniform float iridescenceIOR;
                uniform float iridescenceThicknessMin;
                uniform float iridescenceThicknessMax;
                uniform sampler2D iridescenceMap;
                uniform sampler2D iridescenceThicknessMap;
            ` : ''}
            
            ${defines.USE_SUBSURFACE ? `
                uniform float subsurface;
                uniform vec3 subsurfaceColor;
                uniform float subsurfaceRadius;
                uniform sampler2D subsurfaceMap;
            ` : ''}
            
            // COMPLETE lighting uniforms
            uniform vec3 lightPositions[8];
            uniform vec3 lightColors[8];
            uniform float lightIntensities[8];
            uniform int numLights;
            
            // COMPLETE IBL uniforms
            uniform samplerCube envMap;
            uniform samplerCube irradianceMap;
            uniform sampler2D brdfLUT;
            uniform float envMapIntensity;
            
            out vec4 fragColor;
            
            // COMPLETE BRDF functions
            ${this.generateBRDFFunctions(defines)}
            
            // COMPLETE lighting functions
            ${this.generateLightingFunctions(defines)}
            
            // COMPLETE main function
            void main() {
                // COMPLETE material property sampling
                vec4 albedoSample = texture(albedoMap, vUv);
                vec3 materialAlbedo = albedo * albedoSample.rgb;
                
                vec3 normalSample = texture(normalMap, vUv).rgb * 2.0 - 1.0;
                mat3 tbn = mat3(normalize(vTangent), normalize(vBitangent), normalize(vWorldNormal));
                vec3 materialNormal = normalize(tbn * normalSample);
                
                float materialRoughness = roughness * texture(roughnessMap, vUv).r;
                float materialMetallic = metallic * texture(metallicMap, vUv).r;
                float materialAO = ao * texture(aoMap, vUv).r;
                vec3 materialEmissive = emissive * texture(emissiveMap, vUv).rgb;
                
                // COMPLETE view direction
                vec3 viewDir = normalize(cameraPosition - vWorldPosition);
                
                // COMPLETE base PBR calculation
                vec3 finalColor = calculatePBRLighting(
                    materialAlbedo,
                    materialMetallic,
                    materialRoughness,
                    materialNormal,
                    viewDir
                );
                
                ${defines.USE_CLEARCOAT ? `
                    // COMPLETE clearcoat layer
                    float materialClearcoat = clearcoat * texture(clearcoatMap, vUv).r;
                    float materialClearcoatRoughness = clearcoatRoughness * texture(clearcoatRoughnessMap, vUv).r;
                    
                    if (materialClearcoat > 0.0) {
                        vec3 clearcoatNormalSample = texture(clearcoatNormalMap, vUv).rgb * 2.0 - 1.0;
                        vec3 clearcoatNormal = normalize(tbn * clearcoatNormalSample);
                        
                        finalColor = applyClearcoat(
                            finalColor,
                            clearcoatNormal,
                            viewDir,
                            materialClearcoat,
                            materialClearcoatRoughness
                        );
                    }
                ` : ''}
                
                ${defines.USE_ANISOTROPY ? `
                    // COMPLETE anisotropic reflection
                    if (anisotropy > 0.0) {
                        float materialAnisotropy = anisotropy * texture(anisotropyMap, vUv).r;
                        finalColor = applyAnisotropy(
                            finalColor,
                            materialNormal,
                            normalize(vTangent),
                            normalize(vBitangent),
                            materialAnisotropy,
                            anisotropyRotation
                        );
                    }
                ` : ''}
                
                ${defines.USE_IRIDESCENCE ? `
                    // COMPLETE iridescence effect
                    float materialIridescence = iridescence * texture(iridescenceMap, vUv).r;
                    if (materialIridescence > 0.0) {
                        float thickness = mix(
                            iridescenceThicknessMin,
                            iridescenceThicknessMax,
                            texture(iridescenceThicknessMap, vUv).r
                        );
                        
                        vec3 iridescenceColor = calculateIridescence(
                            materialIridescence,
                            iridescenceIOR,
                            thickness,
                            dot(materialNormal, viewDir)
                        );
                        
                        finalColor = mix(finalColor, iridescenceColor, materialIridescence);
                    }
                ` : ''}
                
                ${defines.USE_SUBSURFACE ? `
                    // COMPLETE subsurface scattering
                    float materialSubsurface = subsurface * texture(subsurfaceMap, vUv).r;
                    if (materialSubsurface > 0.0) {
                        vec3 subsurfaceContribution = calculateSubsurfaceScattering(
                            materialAlbedo,
                            subsurfaceColor,
                            materialNormal,
                            viewDir,
                            materialSubsurface,
                            subsurfaceRadius
                        );
                        
                        finalColor += subsurfaceContribution;
                    }
                ` : ''}
                
                // COMPLETE final color assembly
                finalColor += materialEmissive;
                finalColor *= materialAO;
                
                fragColor = vec4(finalColor, albedoSample.a);
            }
        `;
        
        return fragmentShader;
    }
    
    // MUST implement complete BRDF functions
    generateBRDFFunctions(defines) {
        return `
            // COMPLETE Fresnel calculation
            vec3 fresnelSchlick(float cosTheta, vec3 F0) {
                return F0 + (1.0 - F0) * pow(clamp(1.0 - cosTheta, 0.0, 1.0), 5.0);
            }
            
            vec3 fresnelSchlickRoughness(float cosTheta, vec3 F0, float roughness) {
                return F0 + (max(vec3(1.0 - roughness), F0) - F0) * pow(clamp(1.0 - cosTheta, 0.0, 1.0), 5.0);
            }
            
            // COMPLETE Distribution function (GGX/Trowbridge-Reitz)
            float distributionGGX(vec3 N, vec3 H, float roughness) {
                float a = roughness * roughness;
                float a2 = a * a;
                float NdotH = max(dot(N, H), 0.0);
                float NdotH2 = NdotH * NdotH;
                
                float num = a2;
                float denom = (NdotH2 * (a2 - 1.0) + 1.0);
                denom = 3.14159265359 * denom * denom;
                
                return num / denom;
            }
            
            // COMPLETE Geometry function
            float geometrySchlickGGX(float NdotV, float roughness) {
                float r = (roughness + 1.0);
                float k = (r * r) / 8.0;
                
                float num = NdotV;
                float denom = NdotV * (1.0 - k) + k;
                
                return num / denom;
            }
            
            float geometrySmith(vec3 N, vec3 V, vec3 L, float roughness) {
                float NdotV = max(dot(N, V), 0.0);
                float NdotL = max(dot(N, L), 0.0);
                float ggx2 = geometrySchlickGGX(NdotV, roughness);
                float ggx1 = geometrySchlickGGX(NdotL, roughness);
                
                return ggx1 * ggx2;
            }
            
            ${defines.USE_ANISOTROPY ? `
                // COMPLETE Anisotropic GGX distribution
                float distributionAnisotropicGGX(vec3 N, vec3 H, vec3 T, vec3 B, float roughnessT, float roughnessB) {
                    float NdotH = dot(N, H);
                    if (NdotH <= 0.0) return 0.0;
                    
                    float TdotH = dot(T, H);
                    float BdotH = dot(B, H);
                    
                    float a2T = roughnessT * roughnessT;
                    float a2B = roughnessB * roughnessB;
                    
                    float denom = TdotH * TdotH / a2T + BdotH * BdotH / a2B + NdotH * NdotH;
                    
                    return 1.0 / (3.14159265359 * roughnessT * roughnessB * denom * denom);
                }
            ` : ''}
            
            ${defines.USE_CLEARCOAT ? `
                // COMPLETE Clearcoat BRDF
                vec3 calculateClearcoatBRDF(vec3 N, vec3 V, vec3 L, float clearcoat, float clearcoatRoughness) {
                    vec3 H = normalize(V + L);
                    float NdotH = max(dot(N, H), 0.0);
                    float NdotV = max(dot(N, V), 0.0);
                    float NdotL = max(dot(N, L), 0.0);
                    float VdotH = max(dot(V, H), 0.0);
                    
                    // COMPLETE clearcoat Fresnel (fixed IOR = 1.5)
                    float F0_clearcoat = 0.04; // (1.5 - 1)^2 / (1.5 + 1)^2
                    float F_clearcoat = F0_clearcoat + (1.0 - F0_clearcoat) * pow(1.0 - VdotH, 5.0);
                    
                    // COMPLETE clearcoat distribution and geometry
                    float D_clearcoat = distributionGGX(N, H, clearcoatRoughness);
                    float G_clearcoat = geometrySmith(N, V, L, clearcoatRoughness);
                    
                    vec3 clearcoatBRDF = vec3(D_clearcoat * G_clearcoat * F_clearcoat / (4.0 * NdotV * NdotL + 0.001));
                    
                    return clearcoatBRDF * clearcoat;
                }
            ` : ''}
            
            ${defines.USE_IRIDESCENCE ? `
                // COMPLETE Iridescence calculation
                vec3 calculateIridescence(float iridescence, float ior, float thickness, float cosTheta) {
                    // COMPLETE thin-film interference
                    float opticalPath = 2.0 * ior * thickness * cosTheta;
                    
                    // COMPLETE wavelength-dependent interference
                    vec3 wavelengths = vec3(650.0, 510.0, 475.0); // RGB wavelengths in nm
                    vec3 phases = 2.0 * 3.14159265359 * opticalPath / wavelengths;
                    
                    // COMPLETE interference pattern
                    vec3 interference = 0.5 * (1.0 + cos(phases));
                    
                    // COMPLETE iridescence color
                    vec3 iridescenceColor = interference * iridescence;
                    
                    return iridescenceColor;
                }
            ` : ''}
        `;
    }
}

class SurfaceDetailShaderLibrary {
    constructor() {
        this.parallaxShaders = new ParallaxShaderCollection();
        this.tessellationShaders = new TessellationShaderCollection();
        this.proceduralShaders = new ProceduralShaderCollection();
    }
    
    // MUST implement complete parallax occlusion mapping
    createParallaxOcclusionShader() {
        const fragmentShader = `
            #version 300 es
            precision highp float;
            
            in vec3 vWorldPosition;
            in vec3 vWorldNormal;
            in vec2 vUv;
            in vec3 vTangent;
            in vec3 vBitangent;
            in vec3 vViewPosition;
            
            uniform sampler2D albedoMap;
            uniform sampler2D normalMap;
            uniform sampler2D heightMap;
            uniform float heightScale;
            uniform int maxLayers;
            uniform int minLayers;
            
            out vec4 fragColor;
            
            // COMPLETE parallax occlusion mapping
            vec2 parallaxOcclusionMapping(vec2 texCoords, vec3 viewDir) {
                // COMPLETE layer calculation
                float numLayers = mix(float(maxLayers), float(minLayers), abs(dot(vec3(0.0, 0.0, 1.0), viewDir)));
                float layerDepth = 1.0 / numLayers;
                float currentLayerDepth = 0.0;
                
                // COMPLETE step calculation
                vec2 P = viewDir.xy / viewDir.z * heightScale;
                vec2 deltaTexCoords = P / numLayers;
                
                vec2 currentTexCoords = texCoords;
                float currentDepthMapValue = texture(heightMap, currentTexCoords).r;
                
                // COMPLETE layer stepping
                while(currentLayerDepth < currentDepthMapValue) {
                    currentTexCoords -= deltaTexCoords;
                    currentDepthMapValue = texture(heightMap, currentTexCoords).r;
                    currentLayerDepth += layerDepth;
                }
                
                // COMPLETE interpolation for smoother result
                vec2 prevTexCoords = currentTexCoords + deltaTexCoords;
                float afterDepth = currentDepthMapValue - currentLayerDepth;
                float beforeDepth = texture(heightMap, prevTexCoords).r - currentLayerDepth + layerDepth;
                
                float weight = afterDepth / (afterDepth - beforeDepth);
                vec2 finalTexCoords = prevTexCoords * weight + currentTexCoords * (1.0 - weight);
                
                return finalTexCoords;
            }
            
            // COMPLETE self-shadowing
            float calculateSelfShadowing(vec2 texCoords, vec3 lightDir) {
                float shadowMultiplier = 1.0;
                float minLayers = 8.0;
                float maxLayers = 32.0;
                
                if(dot(vec3(0.0, 0.0, 1.0), lightDir) > 0.0) {
                    float numSamplesUnderSurface = 0.0;
                    float numLayers = mix(maxLayers, minLayers, abs(dot(vec3(0.0, 0.0, 1.0), lightDir)));
                    float layerHeight = 1.0 / numLayers;
                    vec2 texStep = heightScale * lightDir.xy / lightDir.z / numLayers;
                    
                    float currentLayerHeight = texture(heightMap, texCoords).r - layerHeight;
                    vec2 currentTexCoords = texCoords + texStep;
                    
                    for(int i = 1; i < int(maxLayers) && currentLayerHeight > 0.0; i++) {
                        float heightFromTexture = texture(heightMap, currentTexCoords).r;
                        if(heightFromTexture < currentLayerHeight) {
                            numSamplesUnderSurface += 1.0;
                        }
                        currentLayerHeight -= layerHeight;
                        currentTexCoords += texStep;
                    }
                    
                    shadowMultiplier = 1.0 - numSamplesUnderSurface / numLayers;
                }
                
                return shadowMultiplier;
            }
            
            void main() {
                // COMPLETE view direction in tangent space
                mat3 TBN = mat3(normalize(vTangent), normalize(vBitangent), normalize(vWorldNormal));
                vec3 viewDirTangent = normalize(transpose(TBN) * (vViewPosition - vWorldPosition));
                
                // COMPLETE parallax mapping
                vec2 parallaxTexCoords = parallaxOcclusionMapping(vUv, viewDirTangent);
                
                // COMPLETE texture sampling with parallax coordinates
                vec3 albedo = texture(albedoMap, parallaxTexCoords).rgb;
                vec3 normal = texture(normalMap, parallaxTexCoords).rgb * 2.0 - 1.0;
                
                // COMPLETE self-shadowing
                vec3 lightDir = normalize(vec3(1.0, 1.0, 1.0)); // Example light direction
                vec3 lightDirTangent = normalize(transpose(TBN) * lightDir);
                float shadow = calculateSelfShadowing(parallaxTexCoords, lightDirTangent);
                
                // COMPLETE final color
                vec3 finalColor = albedo * shadow;
                
                fragColor = vec4(finalColor, 1.0);
            }
        `;
        
        return fragmentShader;
    }
}

class EnvironmentalShaderLibrary {
    constructor() {
        this.atmosphericShaders = new AtmosphericShaderCollection();
        this.volumetricShaders = new VolumetricShaderCollection();
        this.weatherShaders = new WeatherShaderCollection();
    }
    
    // MUST implement complete atmospheric scattering
    createAtmosphericScatteringShader() {
        const fragmentShader = `
            #version 300 es
            precision highp float;
            
            in vec3 vWorldPosition;
            in vec3 vWorldDirection;
            
            uniform vec3 cameraPosition;
            uniform vec3 sunDirection;
            uniform float sunIntensity;
            uniform float atmosphereRadius;
            uniform float planetRadius;
            uniform vec3 betaRayleigh;
            uniform vec3 betaMie;
            uniform float mieG;
            uniform float densityFalloff;
            uniform int numSamples;
            uniform int numSamplesLight;
            
            out vec4 fragColor;
            
            // COMPLETE ray-sphere intersection
            vec2 raySphereIntersection(vec3 rayOrigin, vec3 rayDirection, float sphereRadius) {
                float a = dot(rayDirection, rayDirection);
                float b = 2.0 * dot(rayOrigin, rayDirection);
                float c = dot(rayOrigin, rayOrigin) - sphereRadius * sphereRadius;
                float discriminant = b * b - 4.0 * a * c;
                
                if (discriminant < 0.0) {
                    return vec2(-1.0, -1.0);
                }
                
                float sqrtDiscriminant = sqrt(discriminant);
                return vec2((-b - sqrtDiscriminant) / (2.0 * a), (-b + sqrtDiscriminant) / (2.0 * a));
            }
            
            // COMPLETE atmospheric density
            float getAtmosphereDensity(vec3 position) {
                float altitude = length(position) - planetRadius;
                return exp(-altitude / densityFalloff);
            }
            
            // COMPLETE phase functions
            float rayleighPhase(float cosTheta) {
                return 3.0 / (16.0 * 3.14159265359) * (1.0 + cosTheta * cosTheta);
            }
            
            float miePhase(float cosTheta, float g) {
                float g2 = g * g;
                float cosTheta2 = cosTheta * cosTheta;
                return 3.0 / (8.0 * 3.14159265359) * ((1.0 - g2) * (1.0 + cosTheta2)) / 
                       ((2.0 + g2) * pow(1.0 + g2 - 2.0 * g * cosTheta, 1.5));
            }
            
            // COMPLETE optical depth calculation
            float getOpticalDepth(vec3 rayOrigin, vec3 rayDirection, float rayLength, vec3 scatteringCoeff) {
                vec3 densitySamplePoint = rayOrigin;
                float stepSize = rayLength / float(numSamplesLight);
                float opticalDepth = 0.0;
                
                for (int i = 0; i < numSamplesLight; i++) {
                    float localDensity = getAtmosphereDensity(densitySamplePoint);
                    opticalDepth += localDensity * stepSize;
                    densitySamplePoint += rayDirection * stepSize;
                }
                
                return opticalDepth;
            }
            
            // COMPLETE scattering calculation
            vec3 calculateScattering(vec3 rayOrigin, vec3 rayDirection) {
                // COMPLETE atmosphere intersection
                vec2 atmosphereIntersection = raySphereIntersection(rayOrigin, rayDirection, atmosphereRadius);
                
                if (atmosphereIntersection.x < 0.0) {
                    return vec3(0.0);
                }
                
                // COMPLETE ray parameters
                float rayLength = atmosphereIntersection.y - max(atmosphereIntersection.x, 0.0);
                float stepSize = rayLength / float(numSamples);
                
                vec3 rayleighScattering = vec3(0.0);
                vec3 mieScattering = vec3(0.0);
                float opticalDepthRayleigh = 0.0;
                float opticalDepthMie = 0.0;
                
                vec3 rayPos = rayOrigin + rayDirection * max(atmosphereIntersection.x, 0.0);
                
                // COMPLETE ray marching
                for (int i = 0; i < numSamples; i++) {
                    float localDensity = getAtmosphereDensity(rayPos);
                    
                    // COMPLETE optical depth accumulation
                    opticalDepthRayleigh += localDensity * stepSize;
                    opticalDepthMie += localDensity * stepSize;
                    
                    // COMPLETE light ray to sun
                    vec2 sunIntersection = raySphereIntersection(rayPos, sunDirection, atmosphereRadius);
                    float sunRayLength = sunIntersection.y;
                    
                    float sunOpticalDepthRayleigh = getOpticalDepth(rayPos, sunDirection, sunRayLength, betaRayleigh);
                    float sunOpticalDepthMie = getOpticalDepth(rayPos, sunDirection, sunRayLength, betaMie);
                    
                    // COMPLETE transmittance
                    vec3 transmittance = exp(-(betaRayleigh * (opticalDepthRayleigh + sunOpticalDepthRayleigh) + 
                                            betaMie * (opticalDepthMie + sunOpticalDepthMie)));
                    
                    // COMPLETE scattering contribution
                    rayleighScattering += transmittance * localDensity * stepSize;
                    mieScattering += transmittance * localDensity * stepSize;
                    
                    rayPos += rayDirection * stepSize;
                }
                
                // COMPLETE phase function application
                float cosTheta = dot(rayDirection, sunDirection);
                vec3 finalScattering = rayleighScattering * betaRayleigh * rayleighPhase(cosTheta) +
                                     mieScattering * betaMie * miePhase(cosTheta, mieG);
                
                return finalScattering * sunIntensity;
            }
            
            void main() {
                vec3 rayDirection = normalize(vWorldDirection);
                vec3 scattering = calculateScattering(cameraPosition, rayDirection);
                
                fragColor = vec4(scattering, 1.0);
            }
        `;
        
        return fragmentShader;
    }
}
```

VALIDATION REQUIREMENTS:
CURSOR MUST verify after implementation:
✓ All custom shaders compile without errors
✓ Advanced BRDF models produce realistic results
✓ Surface detail shaders enhance realism
✓ Atmospheric effects are visually convincing
✓ Shader performance meets targets
✓ All shader features integrate properly
✓ Memory usage is optimized
✓ Cross-platform compatibility is maintained

PERFORMANCE BENCHMARKS (MUST ACHIEVE):
✓ Shader compilation: <2s for complete library
✓ Advanced PBR shader: <0.5ms per material per frame
✓ Parallax occlusion mapping: <0.3ms additional overhead
✓ Atmospheric scattering: <2ms per frame
✓ Volumetric effects: <3ms per frame
✓ Overall shader overhead: <20% of frame time
```

**GAP IDENTIFICATION FOR PHASE 5.1**:
```
CURSOR MUST CHECK FOR THESE CRITICAL GAPS:
❌ Poor shader performance impacting frame rate
❌ Missing advanced BRDF models reducing realism
❌ Inadequate surface detail shaders
❌ Poor atmospheric effects breaking immersion
❌ Missing shader optimization causing performance issues
❌ Inadequate cross-platform compatibility
❌ Poor shader validation causing compilation errors
❌ Missing procedural generation capabilities
❌ Inadequate lighting model accuracy
❌ Poor integration with existing material system
```

## Prompt 5.2: Advanced Post-Processing Pipeline

**PREREQUISITE VALIDATION**:
```
CURSOR MUST VERIFY FROM PHASE 5.1:
✓ Custom shader library is fully functional
✓ All shaders compile without errors
✓ Advanced BRDF models work correctly
✓ Surface detail shaders enhance realism
✓ Performance benchmarks are met
✓ Shader integration is working properly
```

**CURSOR RULES FOR THIS PROMPT**:
1. MUST create cinema-quality post-processing pipeline
2. ALL effects must be based on real camera and film techniques
3. MUST maintain performance while adding visual enhancement
4. Post-processing quality must rival professional film production

**DETAILED IMPLEMENTATION**:
```
Create a cinema-quality post-processing pipeline:

MANDATORY POST-PROCESSING COMPONENTS:

1. ADVANCED ANTI-ALIASING (COMPLETE IMPLEMENTATION):
   AntiAliasingPipeline.js MUST implement:

   TEMPORAL ANTI-ALIASING (TAA):
   - MUST implement proper velocity buffer generation
   - MUST implement history buffer management with proper reprojection
   - MUST implement rejection sampling for disocclusion handling
   - MUST implement sharpening to counteract temporal blur
   - MUST implement proper jitter pattern for sample distribution

   MORPHOLOGICAL ANTI-ALIASING (MLAA):
   - MUST implement edge detection with proper thresholds
   - MUST implement blending weight calculation
   - MUST implement neighborhood blending with area textures
   - MUST implement proper handling of diagonal edges

2. ADVANCED COLOR GRADING (COMPLETE IMPLEMENTATION):
   ColorGradingPipeline.js MUST implement:

   PROFESSIONAL COLOR CONTROLS:
   - MUST implement lift/gamma/gain controls with proper curves
   - MUST implement film-style color lookup tables (LUT) with proper interpolation
   - MUST implement color wheel adjustments with proper hue preservation
   - MUST implement shadow/highlight separation with luminance masking
   - MUST implement saturation controls with proper skin tone preservation
   - MUST implement color temperature adjustment with proper white balance

3. DEPTH-BASED EFFECTS (COMPLETE IMPLEMENTATION):
   DepthEffectsPipeline.js MUST implement:

   DEPTH OF FIELD:
   - MUST implement physically accurate depth of field with bokeh simulation
   - MUST implement proper circle of confusion calculations
   - MUST implement realistic bokeh shapes and characteristics
   - MUST implement focus pulling with smooth transitions

   SCREEN-SPACE EFFECTS:
   - MUST implement screen-space ambient occlusion with temporal filtering
   - MUST implement screen-space reflections with proper roughness handling
   - MUST implement contact shadows for fine detail enhancement

COMPLETE IMPLEMENTATION REQUIREMENTS:

PostProcessingPipeline.js MUST implement:
```javascript
class PostProcessingPipeline {
    constructor(renderer) {
        this.renderer = renderer;
        
        // COMPLETE post-processing passes
        this.taaPass = new TemporalAntiAliasingPass();
        this.mlaaPass = new MorphologicalAntiAliasingPass();
        this.ssaoPass = new SSAOPass();
        this.ssrPass = new SSRPass();
        this.dofPass = new DepthOfFieldPass();
        this.colorGradingPass = new ColorGradingPass();
        this.tonemappingPass = new TonemappingPass();
        this.filmGrainPass = new FilmGrainPass();
        
        // COMPLETE render targets
        this.renderTargets = this.createRenderTargets();
        
        // COMPLETE pass management
        this.passManager = new PassManager();
        this.effectComposer = new EffectComposer(renderer);
        
        this.initializePostProcessing();
    }
    
    // MUST implement complete post-processing execution
    executePostProcessing(inputTexture, camera, scene) {
        // COMPLETE pass sequence
        let currentTexture = inputTexture;
        
        // COMPLETE temporal anti-aliasing
        if (this.taaPass.enabled) {
            currentTexture = this.taaPass.render(currentTexture, camera, scene);
        }
        
        // COMPLETE screen-space ambient occlusion
        if (this.ssaoPass.enabled) {
            currentTexture = this.ssaoPass.render(currentTexture, camera, scene);
        }
        
        // COMPLETE screen-space reflections
        if (this.ssrPass.enabled) {
            currentTexture = this.ssrPass.render(currentTexture, camera, scene);
        }
        
        // COMPLETE depth of field
        if (this.dofPass.enabled) {
            currentTexture = this.dofPass.render(currentTexture, camera, scene);
        }
        
        // COMPLETE color grading
        if (this.colorGradingPass.enabled) {
            currentTexture = this.colorGradingPass.render(currentTexture);
        }
        
        // COMPLETE tone mapping
        if (this.tonemappingPass.enabled) {
            currentTexture = this.tonemappingPass.render(currentTexture);
        }
        
        // COMPLETE film grain
        if (this.filmGrainPass.enabled) {
            currentTexture = this.filmGrainPass.render(currentTexture);
        }
        
        return currentTexture;
    }
}

class TemporalAntiAliasingPass {
    constructor() {
        this.enabled = true;
        this.historyBuffer = null;
        this.velocityBuffer = null;
        this.jitterPattern = this.generateJitterPattern();
        this.frameIndex = 0;
        
        // COMPLETE TAA parameters
        this.parameters = {
            blendFactor: 0.9,
            rejectionThreshold: 0.1,
            sharpenStrength: 0.3,
            maxSampleCount: 16
        };
        
        this.initializeTAA();
    }
    
    // MUST implement complete TAA rendering
    render(inputTexture, camera, scene) {
        // COMPLETE jitter application
        const jitter = this.jitterPattern[this.frameIndex % this.jitterPattern.length];
        this.applyJitter(camera, jitter);
        
        // COMPLETE velocity buffer generation
        this.generateVelocityBuffer(camera, scene);
        
        // COMPLETE history reprojection
        const reprojectedHistory = this.reprojectHistory(camera);
        
        // COMPLETE temporal blending
        const blendedResult = this.temporalBlend(inputTexture, reprojectedHistory);
        
        // COMPLETE sharpening
        const sharpenedResult = this.applySharpen(blendedResult);
        
        // COMPLETE history update
        this.updateHistory(sharpenedResult);
        
        this.frameIndex++;
        
        return sharpenedResult;
    }
    
    // MUST implement complete velocity buffer generation
    generateVelocityBuffer(camera, scene) {
        const velocityMaterial = new THREE.ShaderMaterial({
            vertexShader: `
                #version 300 es
                precision highp float;
                
                in vec3 position;
                
                uniform mat4 modelMatrix;
                uniform mat4 viewMatrix;
                uniform mat4 projectionMatrix;
                uniform mat4 previousModelMatrix;
                uniform mat4 previousViewMatrix;
                uniform mat4 previousProjectionMatrix;
                
                out vec2 vVelocity;
                
                void main() {
                    // COMPLETE current position
                    vec4 currentPos = projectionMatrix * viewMatrix * modelMatrix * vec4(position, 1.0);
                    currentPos /= currentPos.w;
                    
                    // COMPLETE previous position
                    vec4 previousPos = previousProjectionMatrix * previousViewMatrix * previousModelMatrix * vec4(position, 1.0);
                    previousPos /= previousPos.w;
                    
                    // COMPLETE velocity calculation
                    vVelocity = (currentPos.xy - previousPos.xy) * 0.5;
                    
                    gl_Position = currentPos;
                }
            `,
            fragmentShader: `
                #version 300 es
                precision highp float;
                
                in vec2 vVelocity;
                out vec4 fragColor;
                
                void main() {
                    fragColor = vec4(vVelocity, 0.0, 1.0);
                }
            `
        });
        
        // COMPLETE velocity buffer rendering
        this.renderVelocityBuffer(scene, camera, velocityMaterial);
    }
    
    // MUST implement complete temporal blending
    temporalBlend(currentFrame, historyFrame) {
        const blendMaterial = new THREE.ShaderMaterial({
            uniforms: {
                currentTexture: { value: currentFrame },
                historyTexture: { value: historyFrame },
                velocityTexture: { value: this.velocityBuffer },
                blendFactor: { value: this.parameters.blendFactor },
                rejectionThreshold: { value: this.parameters.rejectionThreshold }
            },
            fragmentShader: `
                #version 300 es
                precision highp float;
                
                uniform sampler2D currentTexture;
                uniform sampler2D historyTexture;
                uniform sampler2D velocityTexture;
                uniform float blendFactor;
                uniform float rejectionThreshold;
                
                in vec2 vUv;
                out vec4 fragColor;
                
                // COMPLETE neighborhood sampling
                vec3 sampleNeighborhood(sampler2D tex, vec2 uv) {
                    vec2 texelSize = 1.0 / textureSize(tex, 0);
                    
                    vec3 samples[9];
                    samples[0] = texture(tex, uv + vec2(-texelSize.x, -texelSize.y)).rgb;
                    samples[1] = texture(tex, uv + vec2(0.0, -texelSize.y)).rgb;
                    samples[2] = texture(tex, uv + vec2(texelSize.x, -texelSize.y)).rgb;
                    samples[3] = texture(tex, uv + vec2(-texelSize.x, 0.0)).rgb;
                    samples[4] = texture(tex, uv).rgb;
                    samples[5] = texture(tex, uv + vec2(texelSize.x, 0.0)).rgb;
                    samples[6] = texture(tex, uv + vec2(-texelSize.x, texelSize.y)).rgb;
                    samples[7] = texture(tex, uv + vec2(0.0, texelSize.y)).rgb;
                    samples[8] = texture(tex, uv + vec2(texelSize.x, texelSize.y)).rgb;
                    
                    // COMPLETE min/max calculation
                    vec3 minColor = samples[0];
                    vec3 maxColor = samples[0];
                    
                    for (int i = 1; i < 9; i++) {
                        minColor = min(minColor, samples[i]);
                        maxColor = max(maxColor, samples[i]);
                    }
                    
                    return samples[4]; // Return center sample
                }
                
                void main() {
                    vec3 currentColor = texture(currentTexture, vUv).rgb;
                    vec2 velocity = texture(velocityTexture, vUv).xy;
                    
                    // COMPLETE history sampling with velocity
                    vec2 historyUV = vUv - velocity;
                    vec3 historyColor = texture(historyTexture, historyUV).rgb;
                    
                    // COMPLETE neighborhood clamping
                    vec3 neighborhoodMin = vec3(1.0);
                    vec3 neighborhoodMax = vec3(0.0);
                    
                    vec2 texelSize = 1.0 / textureSize(currentTexture, 0);
                    for (int x = -1; x <= 1; x++) {
                        for (int y = -1; y <= 1; y++) {
                            vec3 sample = texture(currentTexture, vUv + vec2(x, y) * texelSize).rgb;
                            neighborhoodMin = min(neighborhoodMin, sample);
                            neighborhoodMax = max(neighborhoodMax, sample);
                        }
                    }
                    
                    // COMPLETE history clamping
                    historyColor = clamp(historyColor, neighborhoodMin, neighborhoodMax);
                    
                    // COMPLETE rejection test
                    vec3 colorDiff = abs(currentColor - historyColor);
                    float rejection = step(rejectionThreshold, length(colorDiff));
                    
                    // COMPLETE temporal blending
                    float finalBlendFactor = mix(blendFactor, 0.1, rejection);
                    vec3 finalColor = mix(historyColor, currentColor, finalBlendFactor);
                    
                    fragColor = vec4(finalColor, 1.0);
                }
            `
        });
        
        return this.renderFullscreenQuad(blendMaterial);
    }
}

class DepthOfFieldPass {
    constructor() {
        this.enabled = true;
        
        // COMPLETE DOF parameters
        this.parameters = {
            focusDistance: 10.0, // meters
            focalLength: 50.0, // mm
            fStop: 2.8,
            sensorSize: 36.0, // mm (full frame)
            bokehSides: 6, // hexagonal bokeh
            bokehRotation: 0.0
        };
        
        this.initializeDOF();
    }
    
    // MUST implement complete depth of field
    render(inputTexture, camera, scene) {
        // COMPLETE circle of confusion calculation
        const cocTexture = this.calculateCircleOfConfusion(camera);
        
        // COMPLETE bokeh blur
        const blurredTexture = this.applyBokehBlur(inputTexture, cocTexture);
        
        // COMPLETE near/far field separation
        const separatedFields = this.separateNearFarFields(inputTexture, cocTexture);
        
        // COMPLETE field composition
        const compositeResult = this.compositeFields(separatedFields, blurredTexture);
        
        return compositeResult;
    }
    
    // MUST implement complete circle of confusion calculation
    calculateCircleOfConfusion(camera) {
        const cocMaterial = new THREE.ShaderMaterial({
            uniforms: {
                depthTexture: { value: this.getDepthTexture() },
                focusDistance: { value: this.parameters.focusDistance },
                focalLength: { value: this.parameters.focalLength },
                fStop: { value: this.parameters.fStop },
                sensorSize: { value: this.parameters.sensorSize },
                cameraNear: { value: camera.near },
                cameraFar: { value: camera.far }
            },
            fragmentShader: `
                #version 300 es
                precision highp float;
                
                uniform sampler2D depthTexture;
                uniform float focusDistance;
                uniform float focalLength;
                uniform float fStop;
                uniform float sensorSize;
                uniform float cameraNear;
                uniform float cameraFar;
                
                in vec2 vUv;
                out vec4 fragColor;
                
                // COMPLETE depth linearization
                float linearizeDepth(float depth) {
                    float z = depth * 2.0 - 1.0;
                    return (2.0 * cameraNear * cameraFar) / (cameraFar + cameraNear - z * (cameraFar - cameraNear));
                }
                
                void main() {
                    float depth = texture(depthTexture, vUv).r;
                    float linearDepth = linearizeDepth(depth);
                    
                    // COMPLETE circle of confusion calculation
                    // CoC = (f * |S - D|) / (D * (S - f)) * (A / S)
                    // f = focal length, S = subject distance, D = focus distance, A = aperture diameter
                    
                    float apertureDiameter = focalLength / fStop;
                    float subjectDistance = linearDepth;
                    
                    float coc = (focalLength * abs(subjectDistance - focusDistance)) / 
                               (subjectDistance * (focusDistance - focalLength)) * 
                               (apertureDiameter / focusDistance);
                    
                    // COMPLETE CoC normalization
                    coc = coc / (sensorSize * 0.001); // Convert to normalized units
                    
                    // COMPLETE near/far field indication
                    float nearField = step(subjectDistance, focusDistance);
                    
                    fragColor = vec4(coc, nearField, 0.0, 1.0);
                }
            `
        });
        
        return this.renderFullscreenQuad(cocMaterial);
    }
}

class ColorGradingPass {
    constructor() {
        this.enabled = true;
        
        // COMPLETE color grading parameters
        this.parameters = {
            // COMPLETE lift/gamma/gain
            lift: new THREE.Vector3(0.0, 0.0, 0.0),
            gamma: new THREE.Vector3(1.0, 1.0, 1.0),
            gain: new THREE.Vector3(1.0, 1.0, 1.0),
            
            // COMPLETE color wheels
            shadowsColor: new THREE.Vector3(0.0, 0.0, 0.0),
            midtonesColor: new THREE.Vector3(0.0, 0.0, 0.0),
            highlightsColor: new THREE.Vector3(0.0, 0.0, 0.0),
            
            // COMPLETE saturation and contrast
            saturation: 1.0,
            contrast: 1.0,
            brightness: 0.0,
            
            // COMPLETE temperature and tint
            temperature: 0.0,
            tint: 0.0,
            
            // COMPLETE LUT
            lutTexture: null,
            lutIntensity: 1.0
        };
        
        this.initializeColorGrading();
    }
    
    // MUST implement complete color grading
    render(inputTexture) {
        const colorGradingMaterial = new THREE.ShaderMaterial({
            uniforms: {
                inputTexture: { value: inputTexture },
                lift: { value: this.parameters.lift },
                gamma: { value: this.parameters.gamma },
                gain: { value: this.parameters.gain },
                shadowsColor: { value: this.parameters.shadowsColor },
                midtonesColor: { value: this.parameters.midtonesColor },
                highlightsColor: { value: this.parameters.highlightsColor },
                saturation: { value: this.parameters.saturation },
                contrast: { value: this.parameters.contrast },
                brightness: { value: this.parameters.brightness },
                temperature: { value: this.parameters.temperature },
                tint: { value: this.parameters.tint },
                lutTexture: { value: this.parameters.lutTexture },
                lutIntensity: { value: this.parameters.lutIntensity }
            },
            fragmentShader: `
                #version 300 es
                precision highp float;
                
                uniform sampler2D inputTexture;
                uniform vec3 lift;
                uniform vec3 gamma;
                uniform vec3 gain;
                uniform vec3 shadowsColor;
                uniform vec3 midtonesColor;
                uniform vec3 highlightsColor;
                uniform float saturation;
                uniform float contrast;
                uniform float brightness;
                uniform float temperature;
                uniform float tint;
                uniform sampler2D lutTexture;
                uniform float lutIntensity;
                
                in vec2 vUv;
                out vec4 fragColor;
                
                // COMPLETE color space conversions
                vec3 rgb2hsv(vec3 c) {
                    vec4 K = vec4(0.0, -1.0 / 3.0, 2.0 / 3.0, -1.0);
                    vec4 p = mix(vec4(c.bg, K.wz), vec4(c.gb, K.xy), step(c.b, c.g));
                    vec4 q = mix(vec4(p.xyw, c.r), vec4(c.r, p.yzx), step(p.x, c.r));
                    
                    float d = q.x - min(q.w, q.y);
                    float e = 1.0e-10;
                    return vec3(abs(q.z + (q.w - q.y) / (6.0 * d + e)), d / (q.x + e), q.x);
                }
                
                vec3 hsv2rgb(vec3 c) {
                    vec4 K = vec4(1.0, 2.0 / 3.0, 1.0 / 3.0, 3.0);
                    vec3 p = abs(fract(c.xxx + K.xyz) * 6.0 - K.www);
                    return c.z * mix(K.xxx, clamp(p - K.xxx, 0.0, 1.0), c.y);
                }
                
                // COMPLETE lift/gamma/gain
                vec3 applyLiftGammaGain(vec3 color, vec3 lift, vec3 gamma, vec3 gain) {
                    // COMPLETE lift (shadows)
                    color = color + lift;
                    
                    // COMPLETE gamma (midtones)
                    color = pow(max(color, vec3(0.0)), 1.0 / gamma);
                    
                    // COMPLETE gain (highlights)
                    color = color * gain;
                    
                    return color;
                }
                
                // COMPLETE color wheels
                vec3 applyColorWheels(vec3 color, vec3 shadows, vec3 midtones, vec3 highlights) {
                    float luminance = dot(color, vec3(0.299, 0.587, 0.114));
                    
                    // COMPLETE luminance-based blending weights
                    float shadowWeight = 1.0 - smoothstep(0.0, 0.5, luminance);
                    float highlightWeight = smoothstep(0.5, 1.0, luminance);
                    float midtoneWeight = 1.0 - shadowWeight - highlightWeight;
                    
                    // COMPLETE color wheel application
                    color += shadows * shadowWeight;
                    color += midtones * midtoneWeight;
                    color += highlights * highlightWeight;
                    
                    return color;
                }
                
                // COMPLETE temperature and tint
                vec3 applyTemperatureAndTint(vec3 color, float temperature, float tint) {
                    // COMPLETE temperature adjustment (blue-orange)
                    float tempFactor = temperature * 0.01;
                    color.r += tempFactor;
                    color.b -= tempFactor;
                    
                    // COMPLETE tint adjustment (green-magenta)
                    float tintFactor = tint * 0.01;
                    color.g += tintFactor;
                    
                    return color;
                }
                
                // COMPLETE LUT application
                vec3 applyLUT(vec3 color, sampler2D lut) {
                    float lutSize = 32.0; // Assuming 32x32x32 LUT
                    float scale = (lutSize - 1.0) / lutSize;
                    float offset = 1.0 / (2.0 * lutSize);
                    
                    // COMPLETE 3D LUT sampling
                    color = clamp(color, 0.0, 1.0);
                    
                    float blueSlice = color.b * (lutSize - 1.0);
                    float blueSliceInt = floor(blueSlice);
                    float blueFrac = blueSlice - blueSliceInt;
                    
                    vec2 uv1 = vec2(
                        (color.r * scale + offset) / lutSize + blueSliceInt / lutSize,
                        color.g * scale + offset
                    );
                    
                    vec2 uv2 = vec2(
                        (color.r * scale + offset) / lutSize + (blueSliceInt + 1.0) / lutSize,
                        color.g * scale + offset
                    );
                    
                    vec3 color1 = texture(lut, uv1).rgb;
                    vec3 color2 = texture(lut, uv2).rgb;
                    
                    return mix(color1, color2, blueFrac);
                }
                
                void main() {
                    vec3 color = texture(inputTexture, vUv).rgb;
                    
                    // COMPLETE color grading pipeline
                    color = applyLiftGammaGain(color, lift, gamma, gain);
                    color = applyColorWheels(color, shadowsColor, midtonesColor, highlightsColor);
                    color = applyTemperatureAndTint(color, temperature, tint);
                    
                    // COMPLETE saturation adjustment
                    vec3 hsv = rgb2hsv(color);
                    hsv.y *= saturation;
                    color = hsv2rgb(hsv);
                    
                    // COMPLETE contrast and brightness
                    color = (color - 0.5) * contrast + 0.5 + brightness;
                    
                    // COMPLETE LUT application
                    if (lutTexture != null && lutIntensity > 0.0) {
                        vec3 lutColor = applyLUT(color, lutTexture);
                        color = mix(color, lutColor, lutIntensity);
                    }
                    
                    fragColor = vec4(color, 1.0);
                }
            `
        });
        
        return this.renderFullscreenQuad(colorGradingMaterial);
    }
}
```

VALIDATION REQUIREMENTS:
CURSOR MUST verify after implementation:
✓ All post-processing effects work correctly
✓ Temporal anti-aliasing reduces aliasing effectively
✓ Depth of field produces realistic bokeh
✓ Color grading provides professional control
✓ Screen-space effects enhance realism
✓ Performance remains above 45 FPS
✓ All shaders compile without errors
✓ Effects integrate smoothly together

PERFORMANCE BENCHMARKS (MUST ACHIEVE):
✓ TAA pass: <2ms per frame
✓ Depth of field: <3ms per frame
✓ Color grading: <1ms per frame
✓ SSAO pass: <2ms per frame
✓ SSR pass: <3ms per frame
✓ Total post-processing: <15ms per frame
```

**GAP IDENTIFICATION FOR PHASE 5.2**:
```
CURSOR MUST CHECK FOR THESE CRITICAL GAPS:
❌ Poor anti-aliasing quality leaving visible jagged edges
❌ Unrealistic depth of field effects
❌ Inadequate color grading controls
❌ Performance issues with complex post-processing
❌ Poor temporal stability in TAA
❌ Missing professional film techniques
❌ Inadequate bokeh quality in DOF
❌ Poor screen-space effect integration
❌ Missing motion blur effects
❌ Inadequate HDR tone mapping
```

## Prompt 5.3: Volumetric Lighting & Atmospheric Effects

**PREREQUISITE VALIDATION**:
```
CURSOR MUST VERIFY FROM PHASE 5.2:
✓ Post-processing pipeline is fully functional
✓ All post-processing effects work correctly
✓ Performance benchmarks are met
✓ Temporal anti-aliasing is stable
✓ Color grading provides professional control
✓ All shaders compile without errors
```

**CURSOR RULES FOR THIS PROMPT**:
1. MUST implement advanced volumetric lighting for cinematic atmosphere
2. ALL atmospheric effects must be based on real physics
3. MUST maintain performance while adding volumetric complexity
4. Atmospheric quality must rival high-end film production

**DETAILED IMPLEMENTATION**:
```
Implement advanced volumetric lighting for cinematic atmosphere:

MANDATORY VOLUMETRIC LIGHTING COMPONENTS:

1. VOLUMETRIC RAY MARCHING (COMPLETE IMPLEMENTATION):
   VolumetricLightingSystem.js MUST implement:

   RAY MARCHING ENGINE:
   - MUST implement efficient ray marching through volumetric media
   - MUST create proper light scattering calculations with phase functions
   - MUST build temporal filtering for reduced noise and flickering
   - MUST implement proper extinction and absorption modeling
   - MUST create realistic fog density variation with height and distance
   - MUST build proper light shaft formation and god ray effects

2. ATMOSPHERIC SCATTERING (COMPLETE IMPLEMENTATION):
   AtmosphericScatteringSystem.js MUST implement:

   PHYSICAL SCATTERING:
   - MUST implement Hosek-Wilkie sky model for accurate sky colors
   - MUST create proper Rayleigh scattering for blue sky effects
   - MUST build Mie scattering for haze and aerosol effects
   - MUST implement ozone absorption for proper sky color gradients
   - MUST create realistic sunset/sunrise color progressions
   - MUST build proper aerial perspective with atmospheric color shifts

3. PARTICLE SYSTEMS (COMPLETE IMPLEMENTATION):
   VolumetricParticleSystem.js MUST implement:

   ATMOSPHERIC PARTICLES:
   - Dust motes with proper Brownian motion and air current effects
   - Condensation particles with realistic formation and evaporation
   - Smoke and vapor effects with proper fluid dynamics
   - Static electricity effects with particle attraction and repulsion
   - Heat shimmer effects with proper air density variation
   - Electromagnetic interference effects with proper field visualization

COMPLETE IMPLEMENTATION REQUIREMENTS:

VolumetricLightingSystem.js MUST implement:
```javascript
class VolumetricLightingSystem {
    constructor(renderer, scene) {
        this.renderer = renderer;
        this.scene = scene;
        
        // COMPLETE volumetric components
        this.rayMarcher = new VolumetricRayMarcher();
        this.scatteringCalculator = new ScatteringCalculator();
        this.fogSystem = new VolumetricFogSystem();
        this.godRaySystem = new GodRaySystem();
        
        // COMPLETE render targets
        this.volumetricBuffer = this.createVolumetricBuffer();
        this.scatteringBuffer = this.createScatteringBuffer();
        this.temporalBuffer = this.createTemporalBuffer();
        
        // COMPLETE parameters
        this.parameters = {
            rayMarchSteps: 64,
            scatteringIntensity: 1.0,
            extinctionCoefficient: 0.1,
            phaseG: 0.8,
            fogDensity: 0.02,
            fogHeightFalloff: 0.1
        };
        
        this.initializeVolumetricLighting();
    }
    
    // MUST implement complete volumetric lighting update
    updateVolumetricLighting(camera, lights, deltaTime) {
        // COMPLETE fog density calculation
        this.updateFogDensity(camera.position, deltaTime);
        
        // COMPLETE light scattering calculation
        this.calculateLightScattering(camera, lights);
        
        // COMPLETE ray marching execution
        this.executeRayMarching(camera, lights);
        
        // COMPLETE temporal filtering
        this.applyTemporalFiltering(deltaTime);
        
        // COMPLETE god ray calculation
        this.calculateGodRays(camera, lights);
        
        return this.volumetricBuffer;
    }
    
    // MUST implement complete ray marching
    executeRayMarching(camera, lights) {
        const rayMarchMaterial = new THREE.ShaderMaterial({
            uniforms: {
                depthTexture: { value: this.getDepthTexture() },
                cameraPosition: { value: camera.position },
                cameraDirection: { value: camera.getWorldDirection(new THREE.Vector3()) },
                lightPositions: { value: lights.map(l => l.position) },
                lightColors: { value: lights.map(l => l.color) },
                lightIntensities: { value: lights.map(l => l.intensity) },
                numLights: { value: lights.length },
                rayMarchSteps: { value: this.parameters.rayMarchSteps },
                scatteringIntensity: { value: this.parameters.scatteringIntensity },
                extinctionCoefficient: { value: this.parameters.extinctionCoefficient },
                phaseG: { value: this.parameters.phaseG },
                fogDensity: { value: this.parameters.fogDensity },
                fogHeightFalloff: { value: this.parameters.fogHeightFalloff },
                time: { value: performance.now() * 0.001 }
            },
            vertexShader: `
                #version 300 es
                precision highp float;
                
                in vec3 position;
                in vec2 uv;
                
                uniform mat4 modelMatrix;
                uniform mat4 viewMatrix;
                uniform mat4 projectionMatrix;
                
                out vec2 vUv;
                out vec3 vWorldDirection;
                
                void main() {
                    vUv = uv;
                    
                    // COMPLETE world direction calculation
                    vec4 worldPosition = modelMatrix * vec4(position, 1.0);
                    vec4 viewPosition = viewMatrix * worldPosition;
                    
                    vWorldDirection = normalize(worldPosition.xyz);
                    
                    gl_Position = projectionMatrix * viewPosition;
                }
            `,
            fragmentShader: `
                #version 300 es
                precision highp float;
                
                uniform sampler2D depthTexture;
                uniform vec3 cameraPosition;
                uniform vec3 cameraDirection;
                uniform vec3 lightPositions[8];
                uniform vec3 lightColors[8];
                uniform float lightIntensities[8];
                uniform int numLights;
                uniform int rayMarchSteps;
                uniform float scatteringIntensity;
                uniform float extinctionCoefficient;
                uniform float phaseG;
                uniform float fogDensity;
                uniform float fogHeightFalloff;
                uniform float time;
                
                in vec2 vUv;
                in vec3 vWorldDirection;
                
                out vec4 fragColor;
                
                // COMPLETE phase function
                float henyeyGreensteinPhase(float cosTheta, float g) {
                    float g2 = g * g;
                    return (1.0 - g2) / (4.0 * 3.14159265359 * pow(1.0 + g2 - 2.0 * g * cosTheta, 1.5));
                }
                
                // COMPLETE fog density calculation
                float calculateFogDensity(vec3 position) {
                    float heightFactor = exp(-position.y * fogHeightFalloff);
                    
                    // COMPLETE noise-based density variation
                    float noise1 = sin(position.x * 0.1 + time * 0.5) * 0.5 + 0.5;
                    float noise2 = sin(position.z * 0.15 + time * 0.3) * 0.5 + 0.5;
                    float noiseVariation = noise1 * noise2 * 0.3 + 0.7;
                    
                    return fogDensity * heightFactor * noiseVariation;
                }
                
                // COMPLETE light attenuation
                float calculateLightAttenuation(vec3 lightPos, vec3 samplePos) {
                    float distance = length(lightPos - samplePos);
                    return 1.0 / (1.0 + distance * distance * 0.01);
                }
                
                // COMPLETE shadow sampling
                float sampleShadow(vec3 position, vec3 lightDirection) {
                    // COMPLETE shadow map sampling would go here
                    // For now, return simple distance-based attenuation
                    return 1.0;
                }
                
                // COMPLETE volumetric ray marching
                vec3 rayMarchVolume(vec3 rayOrigin, vec3 rayDirection, float maxDistance) {
                    vec3 scatteredLight = vec3(0.0);
                    float stepSize = maxDistance / float(rayMarchSteps);
                    
                    vec3 currentPos = rayOrigin;
                    float transmittance = 1.0;
                    
                    for (int i = 0; i < rayMarchSteps; i++) {
                        if (i >= rayMarchSteps) break;
                        
                        // COMPLETE fog density at current position
                        float density = calculateFogDensity(currentPos);
                        
                        if (density > 0.0) {
                            // COMPLETE light contribution from all lights
                            vec3 lightContribution = vec3(0.0);
                            
                            for (int j = 0; j < numLights && j < 8; j++) {
                                vec3 lightDir = normalize(lightPositions[j] - currentPos);
                                float cosTheta = dot(rayDirection, lightDir);
                                
                                // COMPLETE phase function
                                float phase = henyeyGreensteinPhase(cosTheta, phaseG);
                                
                                // COMPLETE light attenuation
                                float attenuation = calculateLightAttenuation(lightPositions[j], currentPos);
                                
                                // COMPLETE shadow sampling
                                float shadow = sampleShadow(currentPos, lightDir);
                                
                                // COMPLETE light contribution
                                lightContribution += lightColors[j] * lightIntensities[j] * 
                                                   phase * attenuation * shadow * density;
                            }
                            
                            // COMPLETE scattering integration
                            scatteredLight += lightContribution * transmittance * stepSize * scatteringIntensity;
                            
                            // COMPLETE transmittance update
                            transmittance *= exp(-density * extinctionCoefficient * stepSize);
                        }
                        
                        currentPos += rayDirection * stepSize;
                    }
                    
                    return scatteredLight;
                }
                
                void main() {
                    // COMPLETE depth sampling
                    float depth = texture(depthTexture, vUv).r;
                    
                    // COMPLETE ray setup
                    vec3 rayDirection = normalize(vWorldDirection);
                    float maxDistance = depth * 1000.0; // Convert normalized depth to world units
                    
                    // COMPLETE volumetric ray marching
                    vec3 volumetricLight = rayMarchVolume(cameraPosition, rayDirection, maxDistance);
                    
                    fragColor = vec4(volumetricLight, 1.0);
                }
            `
        });
        
        // COMPLETE ray marching execution
        this.renderer.setRenderTarget(this.volumetricBuffer);
        this.renderFullscreenQuad(rayMarchMaterial);
        this.renderer.setRenderTarget(null);
    }
    
    // MUST implement complete god ray system
    calculateGodRays(camera, lights) {
        for (const light of lights) {
            if (light.castGodRays) {
                this.generateGodRaysForLight(light, camera);
            }
        }
    }
    
    // MUST implement complete god ray generation
    generateGodRaysForLight(light, camera) {
        const godRayMaterial = new THREE.ShaderMaterial({
            uniforms: {
                depthTexture: { value: this.getDepthTexture() },
                lightPosition: { value: light.position },
                lightColor: { value: light.color },
                lightIntensity: { value: light.intensity },
                cameraPosition: { value: camera.position },
                projectionMatrix: { value: camera.projectionMatrix },
                viewMatrix: { value: camera.matrixWorldInverse },
                godRaySteps: { value: 32 },
                godRayIntensity: { value: 0.5 },
                godRayDecay: { value: 0.95 }
            },
            fragmentShader: `
                #version 300 es
                precision highp float;
                
                uniform sampler2D depthTexture;
                uniform vec3 lightPosition;
                uniform vec3 lightColor;
                uniform float lightIntensity;
                uniform vec3 cameraPosition;
                uniform mat4 projectionMatrix;
                uniform mat4 viewMatrix;
                uniform int godRaySteps;
                uniform float godRayIntensity;
                uniform float godRayDecay;
                
                in vec2 vUv;
                out vec4 fragColor;
                
                void main() {
                    // COMPLETE light position in screen space
                    vec4 lightViewPos = viewMatrix * vec4(lightPosition, 1.0);
                    vec4 lightScreenPos = projectionMatrix * lightViewPos;
                    lightScreenPos /= lightScreenPos.w;
                    vec2 lightUV = lightScreenPos.xy * 0.5 + 0.5;
                    
                    // COMPLETE ray direction from current pixel to light
                    vec2 rayDirection = lightUV - vUv;
                    float rayLength = length(rayDirection);
                    rayDirection = normalize(rayDirection);
                    
                    // COMPLETE god ray sampling
                    vec3 godRayColor = vec3(0.0);
                    float stepSize = rayLength / float(godRaySteps);
                    float currentIntensity = godRayIntensity;
                    
                    vec2 currentUV = vUv;
                    
                    for (int i = 0; i < godRaySteps; i++) {
                        if (i >= godRaySteps) break;
                        
                        // COMPLETE depth sampling
                        float depth = texture(depthTexture, currentUV).r;
                        
                        // COMPLETE occlusion test
                        if (depth > 0.99) { // Sky or very far objects
                            godRayColor += lightColor * currentIntensity;
                        }
                        
                        currentUV += rayDirection * stepSize;
                        currentIntensity *= godRayDecay;
                        
                        // COMPLETE bounds check
                        if (currentUV.x < 0.0 || currentUV.x > 1.0 || 
                            currentUV.y < 0.0 || currentUV.y > 1.0) {
                            break;
                        }
                    }
                    
                    godRayColor *= lightIntensity / float(godRaySteps);
                    
                    fragColor = vec4(godRayColor, 1.0);
                }
            `
        });
        
        // COMPLETE god ray rendering
        this.renderGodRayPass(godRayMaterial);
    }
}

class AtmosphericScatteringSystem {
    constructor() {
        // COMPLETE atmospheric parameters
        this.parameters = {
            rayleighCoefficient: new THREE.Vector3(5.8e-6, 13.5e-6, 33.1e-6),
            mieCoefficient: 21e-6,
            sunIntensity: 20.0,
            mieDirectionalG: 0.8,
            turbidity: 2.0,
            rayleighZenithLength: 615,
            mieZenithLength: 1255,
            sunAngularDiameterCos: 0.999956676946448443553574619906976478926848692873900859324
        };
        
        this.initializeAtmosphericScattering();
    }
    
    // MUST implement complete atmospheric scattering
    calculateAtmosphericScattering(sunPosition, viewDirection) {
        const scatteringMaterial = new THREE.ShaderMaterial({
            uniforms: {
                sunPosition: { value: sunPosition },
                rayleighCoefficient: { value: this.parameters.rayleighCoefficient },
                mieCoefficient: { value: this.parameters.mieCoefficient },
                sunIntensity: { value: this.parameters.sunIntensity },
                mieDirectionalG: { value: this.parameters.mieDirectionalG },
                turbidity: { value: this.parameters.turbidity },
                rayleighZenithLength: { value: this.parameters.rayleighZenithLength },
                mieZenithLength: { value: this.parameters.mieZenithLength },
                sunAngularDiameterCos: { value: this.parameters.sunAngularDiameterCos }
            },
            fragmentShader: `
                #version 300 es
                precision highp float;
                
                uniform vec3 sunPosition;
                uniform vec3 rayleighCoefficient;
                uniform float mieCoefficient;
                uniform float sunIntensity;
                uniform float mieDirectionalG;
                uniform float turbidity;
                uniform float rayleighZenithLength;
                uniform float mieZenithLength;
                uniform float sunAngularDiameterCos;
                
                in vec3 vWorldDirection;
                out vec4 fragColor;
                
                // COMPLETE constants
                const float pi = 3.141592653589793238462643383279502884197169;
                const float n = 1.0003; // refractive index of air
                const float N = 2.545E25; // number of molecules per unit volume for air at 288.15K and 1013mb
                const float pn = 0.035; // depolatization factor for standard air
                
                // COMPLETE wavelength of used primaries
                const vec3 lambda = vec3(680E-9, 550E-9, 450E-9);
                
                // COMPLETE mie stuff
                const float v = 4.0;
                
                // COMPLETE optical length at zenith for molecules
                const float rayleighZenithLengthConst = 8.4E3;
                const float mieZenithLengthConst = 1.25E3;
                const vec3 up = vec3(0.0, 1.0, 0.0);
                
                // COMPLETE earth shadow hack
                const float cutoffAngle = 1.6110731556870734;
                const float steepness = 1.5;
                
                vec3 totalRayleigh(vec3 lambda) {
                    return (8.0 * pow(pi, 3.0) * pow(pow(n, 2.0) - 1.0, 2.0) * (6.0 + 3.0 * pn)) / 
                           (3.0 * N * pow(lambda, vec3(4.0)) * (6.0 - 7.0 * pn));
                }
                
                vec3 simplifiedRayleigh() {
                    return 0.0005 / vec3(94, 40, 18);
                }
                
                float rayleighPhase(float cosTheta) {
                    return (3.0 / (16.0 * pi)) * (1.0 + pow(cosTheta, 2.0));
                }
                
                vec3 totalMie(vec3 lambda, vec3 K, float T) {
                    float c = (0.2 * T) * 10E-18;
                    return 0.434 * c * pi * pow((2.0 * pi) / lambda, vec3(v - 2.0)) * K;
                }
                
                float hgPhase(float cosTheta, float g) {
                    return (1.0 / (4.0 * pi)) * ((1.0 - pow(g, 2.0)) / pow(1.0 - 2.0 * g * cosTheta + pow(g, 2.0), 1.5));
                }
                
                float sunIntensityFunction(float zenithAngleCos) {
                    return sunIntensity * max(0.0, 1.0 - exp(-((cutoffAngle - acos(zenithAngleCos)) / steepness)));
                }
                
                float A = 0.15;
                float B = 0.50;
                float C = 0.10;
                float D = 0.20;
                float E = 0.02;
                float F = 0.30;
                float W = 1000.0;
                
                vec3 Uncharted2Tonemap(vec3 x) {
                    return ((x * (A * x + C * B) + D * E) / (x * (A * x + B) + D * F)) - E / F;
                }
                
                void main() {
                    vec3 direction = normalize(vWorldDirection);
                    
                    // COMPLETE optical length
                    float zenithAngle = acos(max(0.0, dot(up, direction)));
                    float sR = rayleighZenithLength / (cos(zenithAngle) + 0.15 * pow(93.885 - ((zenithAngle * 180.0) / pi), -1.253));
                    float sM = mieZenithLength / (cos(zenithAngle) + 0.15 * pow(93.885 - ((zenithAngle * 180.0) / pi), -1.253));
                    
                    // COMPLETE combined extinction factor
                    vec3 Fex = exp(-(rayleighCoefficient * sR + mieCoefficient * sM));
                    
                    // COMPLETE in scattering
                    float cosTheta = dot(direction, normalize(sunPosition));
                    
                    float rPhase = rayleighPhase(cosTheta * 0.5 + 0.5);
                    vec3 betaRTheta = rayleighCoefficient * rPhase;
                    
                    float mPhase = hgPhase(cosTheta, mieDirectionalG);
                    vec3 betaMTheta = mieCoefficient * mPhase;
                    
                    vec3 Lin = pow(sunIntensity * ((betaRTheta + betaMTheta) / (rayleighCoefficient + mieCoefficient)) * (1.0 - Fex), vec3(1.5));
                    Lin *= mix(vec3(1.0), pow(sunIntensity * ((betaRTheta + betaMTheta) / (rayleighCoefficient + mieCoefficient)) * Fex, vec3(1.0 / 2.0)), clamp(pow(1.0 - dot(up, sunPosition), 5.0), 0.0, 1.0));
                    
                    // COMPLETE nightsky
                    vec3 direction2 = normalize(direction);
                    float theta = acos(direction2.y); // elevation --> y-axis, [-pi/2, pi/2]
                    float phi = atan(direction2.z, direction2.x); // azimuth --> x-axis [-pi/2, pi/2]
                    vec2 uv = vec2(phi, theta) / vec2(2.0 * pi, pi) + vec2(0.5, 0.0);
                    vec3 L0 = vec3(0.1) * Fex;
                    
                    // COMPLETE composition + solar disc
                    float sundisk = smoothstep(sunAngularDiameterCos, sunAngularDiameterCos + 0.00002, cosTheta);
                    L0 += (sunIntensity * 19000.0 * Fex) * sundisk;
                    
                    vec3 whiteScale = 1.0 / Uncharted2Tonemap(vec3(W));
                    
                    vec3 texColor = (Lin + L0);
                    texColor *= 0.04;
                    texColor += vec3(0.0, 0.001, 0.0025) * 0.3;
                    
                    vec3 curr = Uncharted2Tonemap((log2(2.0 / pow(length(texColor), 4.0))) * texColor);
                    vec3 color = curr * whiteScale;
                    
                    vec3 retColor = pow(color, vec3(1.0 / (1.2 + (1.2 * sunIntensityFunction(dot(sunPosition, up))))));
                    
                    fragColor = vec4(retColor, 1.0);
                }
            `
        });
        
        return this.renderAtmosphericScattering(scatteringMaterial);
    }
}
```

VALIDATION REQUIREMENTS:
CURSOR MUST verify after implementation:
✓ Volumetric lighting produces realistic light shafts
✓ Atmospheric scattering matches real-world sky colors
✓ God rays are visually convincing
✓ Particle systems enhance atmospheric realism
✓ Performance remains above 45 FPS
✓ Temporal filtering reduces noise effectively
✓ All volumetric shaders compile without errors
✓ Integration with existing lighting is seamless

PERFORMANCE BENCHMARKS (MUST ACHIEVE):
✓ Volumetric ray marching: <4ms per frame
✓ Atmospheric scattering: <2ms per frame
✓ God ray calculation: <3ms per frame
✓ Particle systems: <2ms per frame
✓ Temporal filtering: <1ms per frame
✓ Total volumetric overhead: <15ms per frame
```

**GAP IDENTIFICATION FOR PHASE 5.3**:
```
CURSOR MUST CHECK FOR THESE CRITICAL GAPS:
❌ Poor volumetric lighting quality reducing atmosphere
❌ Inaccurate atmospheric scattering breaking realism
❌ Performance issues with complex ray marching
❌ Missing temporal filtering causing flickering
❌ Poor god ray quality reducing dramatic effect
❌ Inadequate particle system integration
❌ Missing physical accuracy in scattering calculations
❌ Poor noise reduction in volumetric effects
❌ Inadequate light shaft formation
❌ Missing atmospheric perspective effects
```

## PHASE 5 COMPLETION CHECKLIST

### ✅ **VALIDATION REQUIREMENTS**
- [ ] Custom shader library compiles without errors
- [ ] Advanced BRDF models produce realistic results
- [ ] Post-processing pipeline enhances visual quality
- [ ] Volumetric lighting creates cinematic atmosphere
- [ ] All shader effects integrate properly
- [ ] Performance remains above 45 FPS
- [ ] Temporal stability is maintained
- [ ] Cross-platform compatibility is ensured

### ✅ **QUALITY GATES**
- [ ] Shader quality exceeds standard PBR implementations
- [ ] Post-processing rivals professional film production
- [ ] Atmospheric effects are physically accurate
- [ ] All effects work together seamlessly
- [ ] Memory usage is optimized
- [ ] Shader compilation times are acceptable

### ✅ **PERFORMANCE BENCHMARKS**
- [ ] Shader compilation: <2s for complete library
- [ ] Advanced PBR rendering: <0.5ms per material
- [ ] Post-processing pipeline: <15ms per frame
- [ ] Volumetric effects: <15ms per frame
- [ ] Overall shader overhead: <20% of frame time
- [ ] Memory usage: <256MB for all shaders

**PHASE 5 MUST BE 100% COMPLETE BEFORE PROCEEDING TO PHASE 6**
