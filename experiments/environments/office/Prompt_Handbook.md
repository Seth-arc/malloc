# **Cursor Agent Prompt Handbook: Ultra-Photorealistic 3D WebGL Office**
## **World-Class Visual Fidelity Standards (99th Percentile)**

---

## **PRIMARY DIRECTIVE: INDISTINGUISHABLE FROM REALITY**
Create a 3D office environment that achieves **architectural visualization studio quality**. The final render must pass the **"photograph test"** - viewers should be unable to distinguish it from a professional architectural photograph without close inspection.

---

## **ADVANCED TECHNICAL ARCHITECTURE**

### **WebGL 2.0 Maximum Quality Context**
```javascript
const gl = canvas.getContext('webgl2', {
    antialias: true,
    alpha: false,
    depth: true,
    stencil: true,
    premultipliedAlpha: false,
    preserveDrawingBuffer: false,
    powerPreference: 'high-performance',
    failIfMajorPerformanceCaveat: false
});

// Force maximum precision
gl.getExtension('EXT_color_buffer_half_float');
gl.getExtension('OES_texture_half_float_linear');
gl.getExtension('WEBGL_color_buffer_float');
```

### **Advanced Rendering Pipeline (Hollywood-Grade)**

#### **1. Spectral PBR with Advanced BRDF**
- **Multi-lobe BRDF** combining Cook-Torrance with clearcoat
- **Spectral rendering** (wavelength-based calculations)
- **Anisotropic reflections** with tangent-space calculations
- **Advanced Fresnel** with dispersion for glass materials
- **Energy conservation** with inter-reflection calculations

#### **2. Advanced Lighting Model**
```glsl
// Implement Disney BRDF with full feature set
vec3 DisneyBRDF(MaterialProperties mat, vec3 L, vec3 V, vec3 N) {
    // Base layer (diffuse + subsurface)
    // Metallic layer with anisotropy
    // Clearcoat layer with separate roughness
    // Sheen layer for fabric materials
    // Transmission for glass/thin materials
}
```

#### **3. Cascaded Shadow Maps with PCF+**
- **4-cascade shadow maps** (4096x4096 each)
- **Percentage Closer Soft Shadows (PCSS)**
- **Contact hardening shadows** (realistic penumbra)
- **Temporal shadow filtering** for noise reduction

---

## **SCENE DESIGN: ARCHITECTURAL EXCELLENCE**

### **Space Planning (Professional Interior Design)**

#### **Office Layout: Premium Corporate Environment**
- **Dimensions**: 15m x 12m x 3.2m (luxury office proportions)
- **Golden ratio proportions** in furniture placement
- **Biophilic design elements** throughout
- **Feng shui principles** in desk orientation

#### **Zoned Functionality**
1. **Executive workspace** (corner office feel)
2. **Collaborative meeting area** (8-person conference setup)
3. **Informal breakout space** (lounge seating)
4. **Technology wall** (video conferencing setup)
5. **Storage and filing zone** (built-in millwork)
6. **Plant/green wall feature** (living wall system)

### **Material Palette (Luxury Commercial Grade)**

#### **Primary Materials**
- **Walnut veneer** with book-matched grain patterns
- **Carrara marble** with realistic veining
- **Brushed aluminum** with directional anisotropy  
- **Charcoal wool carpet** with subtle texture variation
- **Low-iron glass** with anti-reflective coating
- **Painted drywall** with orange peel texture

#### **Accent Materials**
- **Leather upholstery** with natural grain and wear
- **Brass fixtures** with patina variation
- **Concrete accent wall** with board-form texture
- **Natural linen** window treatments
- **Cork flooring** in breakout areas

---

## **LIGHTING DESIGN: CINEMATIC QUALITY**

### **Natural Lighting System**
#### **Sun + Sky Model**
```javascript
// Hosek-Wilkie sky model implementation
const skyModel = {
    turbidity: 2.0,      // Clear day
    sunElevation: 45,    // Mid-morning angle
    azimuth: 135,        // Southeast exposure
    intensity: 100000,   // Lux values
    colorTemperature: 5500 // Kelvin
};
```

#### **Window System**
- **Floor-to-ceiling windows** (2.8m height)
- **Automated blinds** at varying positions
- **Window mullions** casting geometric shadows
- **Fresnel reflections** on glass surfaces
- **Caustic patterns** from window frames

### **Artificial Lighting (Professional Grade)**
#### **Primary Sources**
- **Linear LED strips** (4000K, CRI 95+) recessed in ceiling
- **Task lighting** (2700K warm white) at each workstation
- **Accent lighting** (3000K) highlighting artwork
- **Emergency lighting** with realistic fixture details

#### **Advanced Light Behaviors**
- **IES photometric profiles** for each fixture
- **Light temperature variation** throughout day cycle
- **Dimming curves** with realistic ballast behavior
- **Color mixing** for tunable LED sources

---

## **ADVANCED MATERIAL SCIENCE**

### **Subsurface Scattering Implementation**
```glsl
// For marble, skin-like materials, thin plastics
float subsurfaceScattering(vec3 lightDir, vec3 normal, vec3 viewDir, float thickness) {
    vec3 scatterDir = lightDir + normal * 0.25;
    float scatter = pow(saturate(dot(viewDir, -scatterDir)), 12.0) * thickness;
    return scatter;
}
```

### **Advanced Material Properties**

#### **Wood (Walnut Veneer)**
- **Anisotropic reflectance** following grain direction
- **Subsurface scattering** for thin veneer translucency
- **Micro-normal variation** for surface imperfections
- **Seasonal wood movement** simulation
- **French polish finish** with multiple coat simulation

#### **Glass (Architectural)**
- **Dispersion** (chromatic aberration) at edges
- **Internal reflections** between glass layers
- **Fingerprint smudges** and cleaning streaks
- **Thickness variation** affecting distortion
- **Low-E coating** spectral properties

#### **Fabric (Upholstery)**
- **Dual-lobe BRDF** for fabric + sheen
- **Anisotropic behavior** along weave direction
- **Wear patterns** at contact points
- **Pilling texture** in micro-detail
- **Static electricity** dust accumulation

### **Weathering and Wear Simulation**
- **Edge wear** on high-contact surfaces
- **UV fading** near windows
- **Coffee stains** and water marks
- **Keyboard shine** from finger oils
- **Chair arm wear** patterns
- **Dust accumulation** in corners and crevices

---

## **ENVIRONMENTAL STORYTELLING**

### **Lived-In Details (Hyperrealistic)**
#### **Desktop Ecosystems**
- **Organized chaos** - believable paper stacks
- **Personal items** - family photos, coffee mugs with logos
- **Technology clutter** - charging cables, adapters
- **Stationery arrangement** - pens in holders, sticky notes
- **Document authenticity** - realistic text, letterheads

#### **Ambient Details**
- **Dust motes** floating in sunbeams
- **Condensation** on cold drink glasses
- **Screen reflections** showing room environment
- **Plant leaves** with realistic imperfections
- **Book spines** with readable (but legal) titles
- **Clock synchronization** across multiple timepieces

### **Seasonal Environmental Cues**
- **Autumn leaves** visible through windows
- **Seasonal decorations** appropriate to time of year
- **Clothing** hanging on chairs (blazers, scarves)
- **Beverage choices** (hot coffee vs. iced drinks)
- **Plant conditions** reflecting seasonal care

---

## **ADVANCED POST-PROCESSING CHAIN**

### **Color Science (Professional Grade)**
#### **ACES Color Pipeline**
```glsl
// Academy Color Encoding System implementation
vec3 ACES_tonemap(vec3 color) {
    const float A = 2.51;
    const float B = 0.03;
    const float C = 2.43;
    const float D = 0.59;
    const float E = 0.14;
    return saturate((color * (A * color + B)) / (color * (C * color + D) + E));
}
```

#### **Advanced Effects Stack**
1. **Temporal Anti-Aliasing (TAA)** with motion vectors
2. **Screen-Space Reflections** with ray marching
3. **Screen-Space Ambient Occlusion** with temporal filtering
4. **Volumetric lighting** for dust and atmosphere
5. **Chromatic aberration** for lens simulation
6. **Film grain** for subtle organic feel
7. **Vignetting** for natural lens falloff
8. **Lens flares** for bright light sources

### **Camera Simulation (Professional Photography)**
#### **Physical Camera Properties**
- **f/2.8 aperture** simulation for depth of field
- **35mm equivalent focal length** for natural perspective
- **Sensor noise** at high ISO simulation
- **Rolling shutter** effects during movement
- **Auto-exposure** adaptation with realistic curves

---

## **MICRO-DETAIL REQUIREMENTS**

### **Surface Imperfections (Believability Layer)**
#### **Every Surface Must Include**:
- **Fingerprints** on glass and metal
- **Dust accumulation** patterns
- **Microscopic scratches** from daily use
- **Thermal expansion** gaps in materials
- **Installation imperfections** (slightly uneven mounting)
- **Color variation** within material batches

### **Manufacturing Details**
- **Screw holes** and fastener details
- **Mold lines** on plastic components
- **Weld seams** on metal structures
- **Grain direction** consistency in wood
- **Joint lines** in upholstery seams
- **Tolerance variations** between components

---

## **QUALITY BENCHMARKS (AAA Standards)**

### **Visual Quality Metrics**
- **Texture resolution**: 4K minimum for hero surfaces, 8K for close inspection areas
- **Normal map detail**: 16-bit depth minimum
- **Color depth**: HDR throughout pipeline (16-bit per channel)
- **Shadow resolution**: 4096x4096 cascaded maps
- **Reflection resolution**: 1024x1024 cubemaps per major surface

### **Realism Verification Checklist**
- [ ] **Photogrammetry reference** matching for all materials
- [ ] **Color calibration** against real-world samples
- [ ] **Lighting measurement** matches IES profiles
- [ ] **Physics accuracy** in all reflections and refractions
- [ ] **Scale verification** using human reference measurements
- [ ] **Atmospheric perspective** correctly implemented
- [ ] **Contact shadows** present at all surface intersections

---

## **IMPLEMENTATION PHASES (Professional Workflow)**

### **Phase 1: Foundation (Week 1)**
- Advanced WebGL setup with all extensions
- PBR shader architecture with Disney BRDF
- HDR pipeline with ACES tone mapping
- Basic room geometry with proper proportions

### **Phase 2: Lighting (Week 2)**  
- Hosek-Wilkie sky model implementation
- Cascaded shadow mapping with PCSS
- IES profile integration for all fixtures
- Volumetric lighting for atmosphere

### **Phase 3: Materials (Week 3)**
- Advanced material system with subsurface scattering
- Anisotropic reflection implementation  
- Weathering and wear detail addition
- Texture optimization and streaming

### **Phase 4: Environment (Week 4)**
- Furniture placement with golden ratio proportions
- Environmental storytelling details
- Dust, fingerprints, and imperfection passes
- Seasonal environmental cues

### **Phase 5: Polish (Week 5)**
- Temporal anti-aliasing implementation
- Screen-space effects (SSR, SSAO)
- Camera simulation with DoF
- Performance optimization without quality loss

---

## **SUCCESS CRITERIA: MUSEUM QUALITY**

### **The "Architectural Photography Test"**
The final implementation must:
1. **Fool professional photographers** for 30+ seconds of inspection
2. **Pass pixel-peeping** under magnification
3. **Demonstrate material authenticity** matching physical samples  
4. **Show convincing wear patterns** that tell a story
5. **Exhibit atmospheric effects** indistinguishable from reality
6. **Respond to lighting** exactly as photographed reference materials

### **Industry Benchmark Comparison**
Quality must match or exceed:
- **Unreal Engine 5 Lumen** architectural visualizations
- **V-Ray/Corona** high-end architectural renders  
- **Pixar/ILM** environment art standards
- **Apple product photography** material fidelity
- **High-end real estate** virtual staging quality

**Execute with the precision of a Swiss watchmaker and the artistic vision of a master cinematographer. Every pixel must serve the illusion of reality.**