# BLENDER PHASE 2: ADVANCED MODELING AND MATERIALS (BLENDER 4.4)

## PHASE 2 PREREQUISITES VALIDATION

### MANDATORY PRE-PHASE 2 REQUIREMENTS:
**CURSOR MUST VERIFY FROM PHASE 1:**
```
✓ Complete Blender 4.4 project structure with all collections organized
✓ Material library renders photorealistically in Cycles with all PBR materials
✓ Advanced asset pipeline produces hero-quality components without errors
✓ Geometry Nodes systems enhance detail without performance impact
✓ UV mapping achieves >90% efficiency across all hero and primary assets
✓ Quality assurance system detects and reports all issues automatically
✓ Export pipeline produces valid glTF files compatible with Three.js
✓ Performance metrics meet all Phase 1 benchmarks consistently
✓ Asset Browser is fully populated and organized for efficient workflow
✓ Memory usage remains under 4GB for complete Phase 1 scene
```

### PHASE 2 ADVANCEMENT CRITERIA:
- **NO** advancement to Phase 2 without 100% completion of Phase 1 requirements
- **ALL** Phase 1 validation checkpoints must pass without exceptions
- **ALL** Phase 1 performance benchmarks must be consistently met
- **ALL** Phase 1 export compatibility must be verified in Three.js environment

---

## PROJECT RULES & CONSTRAINTS FOR PHASE 2

### MANDATORY DEVELOPMENT RULES FOR PHASE 2:

1. **ADVANCED MODELING RESTRICTIONS**: 
   - Use ONLY Blender 4.4 advanced modeling tools and workflows
   - NO external modeling software except for reference validation
   - NO custom Python scripts unless fully documented and performance-tested
   - ALL modeling must maintain real-world accuracy within 2% tolerance

2. **HERO ASSET COMPLETENESS**: 
   - Provide COMPLETE hero-quality models with every surface detail modeled
   - NEVER use placeholder geometry or "to be detailed later" annotations
   - All hero assets must withstand 0.1m viewing distance inspection
   - All mechanical details must be functionally accurate and properly animated

3. **MATERIAL SYSTEM CONSISTENCY**: 
   - Maintain perfect PBR compliance across all materials in all lighting conditions
   - Ensure all materials work identically in Cycles, Eevee, and Three.js export
   - Verify material behavior under all cockpit lighting scenarios
   - Test material performance impact and optimize without quality loss

4. **PHOTOREALISM QUALITY GATES**: 
   - Each component MUST be indistinguishable from real cockpit photography
   - Identify and eliminate ALL visual artifacts that break photorealism
   - No component advancement without expert validation against reference materials
   - All surfaces must exhibit correct physical properties under all lighting

5. **PERFORMANCE REQUIREMENTS**: 
   - Maintain <100K triangles per hero asset with full detail
   - Memory usage must not exceed 6GB during advanced modeling operations
   - Viewport performance must maintain >25 FPS in Material Preview with all assets
   - Export time must not exceed 60 seconds per hero component

---

## Prompt 2.1: Hero Asset Advanced Modeling Pipeline

**PREREQUISITE VALIDATION**:
```
CURSOR MUST VERIFY FROM PHASE 1:
✓ All Phase 1 foundation assets are complete and validated
✓ Geometry Nodes pipeline is functional and optimized
✓ Material library provides all base materials for hero assets
✓ Quality assurance system is operational and reporting accurately
✓ Export pipeline maintains material and geometry fidelity
✓ Performance benchmarks are consistently met across all operations
```

**CURSOR RULES FOR THIS PROMPT**:
1. Create COMPLETE hero-quality models with every detail fully realized
2. Implement FULL mechanical accuracy with proper working mechanisms
3. NO simplified geometry - every surface must be modeled to specification
4. Must achieve photorealistic quality indistinguishable from real cockpit photos

**DETAILED IMPLEMENTATION**:
```
Create advanced hero-quality cockpit components using Blender 4.4's most sophisticated modeling tools:

MANDATORY HERO ASSET MODELING PIPELINE:

1. CONTROL STICK ASSEMBLY HERO MODELING (COMPLETE IMPLEMENTATION REQUIRED):
   - MUST model every component to manufacturing specification:
     * Main grip with ergonomic contours sculpted to pilot hand measurements
     * All 23 individual switches and buttons with proper mechanical action
     * Trigger mechanism with realistic pivot points and spring tension
     * Hat switches with 4-way and 8-way directional controls
     * Paddle switches with proper finger ergonomics and tactile feedback
     * Internal wiring harnesses with proper routing and strain relief
     * Mounting hardware with accurate thread patterns and torque specifications
   
   - Advanced Blender 4.4 modeling techniques:
     * Use Subdivision Surface modeling for organic grip contours
     * Implement Boolean operations for precise mechanical cutouts
     * Apply Geometry Nodes for procedural cable routing and connector placement
     * Use Sculpting mode for fine surface textures and wear patterns
     * Implement Curve modifiers for complex cable paths and spring coils

2. THROTTLE QUADRANT HERO MODELING (ALL COMPONENTS REQUIRED):
   - MUST implement complete dual-throttle system:
     * Twin throttle levers with full travel range (0-100% + afterburner)
     * Afterburner detent mechanisms with proper spring-loaded gates
     * Throttle position sensors with realistic electronic components
     * Speed brake integration with mechanical linkage systems
     * Landing gear controls with proper switch mechanisms
     * Flap position controls with graduated detent positions
     * Engine start sequence controls with safety interlocks
     * Emergency throttle cutoff with protective covers and safety wires
   
   - Precision mechanical modeling:
     * All pivot points must have proper bearing surfaces and clearances
     * Mechanical linkages must follow real aircraft control system routing
     * Cable tensions and pulley systems must be accurately represented
     * Hydraulic actuators must show proper cylinder and piston details

3. INSTRUMENT PANEL HERO MODELING (COMPLETE IMPLEMENTATION):
   - MUST model every switch, button, and indicator to military specification:
     * Master caution/warning panel with all 48 individual warning lights
     * Engine monitoring displays with proper LCD screen construction
     * Fuel system controls with all valves, pumps, and quantity indicators
     * Electrical system panel with all circuit breakers and bus controls
     * Environmental controls with temperature, pressure, and flow indicators
     * Communication panel with all radio controls and frequency displays
     * Navigation controls with GPS, INS, and TACAN system interfaces
     * Weapon system controls with all armament selection and safety switches

COMPLETE BLENDER 4.4 IMPLEMENTATION REQUIREMENTS:

Hero Asset Modeling Workflow MUST include:
```python
# Blender 4.4 Hero Asset Modeling Pipeline
import bpy
import bmesh
import mathutils
from mathutils import Vector, Matrix
import math

class HeroAssetModeler:
    """
    Advanced hero asset modeling system for photorealistic cockpit components
    """
    
    def __init__(self):
        self.modeling_precision = 0.001  # 1mm precision
        self.reference_scale = 1.0  # 1:1 real-world scale
        self.quality_level = 'HERO'
        self.performance_budget = 100000  # Triangle limit per hero asset
        
    def create_control_stick_hero(self):
        """
        Create complete hero-quality control stick assembly
        """
        print("Creating hero control stick assembly...")
        
        # Create main collection for control stick
        stick_collection = bpy.data.collections.new("Control_Stick_Hero_Assembly")
        bpy.context.scene.collection.children.link(stick_collection)
        
        # Create main grip using subdivision surface modeling
        grip = self.create_ergonomic_grip()
        stick_collection.objects.link(grip)
        
        # Create all switches and buttons
        switches = self.create_all_switches()
        for switch in switches:
            stick_collection.objects.link(switch)
        
        # Create trigger mechanism
        trigger = self.create_trigger_mechanism()
        stick_collection.objects.link(trigger)
        
        # Create internal wiring
        wiring = self.create_internal_wiring()
        stick_collection.objects.link(wiring)
        
        # Create mounting hardware
        mounting = self.create_mounting_hardware()
        stick_collection.objects.link(mounting)
        
        # Apply hero-quality materials
        self.apply_hero_materials(stick_collection)
        
        # Validate hero asset quality
        self.validate_hero_quality(stick_collection)
        
        return stick_collection
    
    def create_ergonomic_grip(self):
        """
        Create ergonomic grip using advanced subdivision surface modeling
        """
        # Start with basic cylinder
        bpy.ops.mesh.primitive_cylinder_add(
            radius=0.025, 
            depth=0.15, 
            location=(0, 0, 0)
        )
        grip = bpy.context.active_object
        grip.name = "Control_Stick_Grip_Hero"
        
        # Enter Edit Mode for detailed shaping
        bpy.context.view_layer.objects.active = grip
        bpy.ops.object.mode_set(mode='EDIT')
        
        # Add edge loops for grip contours
        bpy.ops.mesh.subdivide(number_cuts=8)
        
        # Select grip area vertices for sculpting preparation
        bpy.ops.mesh.select_all(action='SELECT')
        
        # Return to Object Mode
        bpy.ops.object.mode_set(mode='OBJECT')
        
        # Add Subdivision Surface modifier
        subsurf = grip.modifiers.new(name="SubSurf", type='SUBSURF')
        subsurf.levels = 2
        subsurf.render_levels = 3
        
        # Add Multiresolution for sculpting
        multires = grip.modifiers.new(name="Multiresolution", type='MULTIRES')
        
        # Enter Sculpt Mode for ergonomic shaping
        bpy.ops.object.mode_set(mode='SCULPT')
        
        # Configure sculpting for grip texture
        bpy.context.scene.tool_settings.sculpt.use_symmetry_x = True
        
        # Return to Object Mode
        bpy.ops.object.mode_set(mode='OBJECT')
        
        return grip
    
    def create_all_switches(self):
        """
        Create all switches and buttons with proper mechanical detail
        """
        switches = []
        
        # Switch specifications based on real F-22/F-35 control stick
        switch_specs = [
            {'name': 'Weapon_Release', 'type': 'trigger', 'position': (0.02, 0.03, 0.05)},
            {'name': 'Sensor_Control', 'type': 'hat_4way', 'position': (0.0, 0.02, 0.08)},
            {'name': 'TMS_Switch', 'type': 'hat_4way', 'position': (-0.015, 0.025, 0.06)},
            {'name': 'DMS_Switch', 'type': 'hat_4way', 'position': (0.015, 0.025, 0.06)},
            {'name': 'CMS_Switch', 'type': 'hat_4way', 'position': (0.0, 0.035, 0.04)},
            {'name': 'Paddle_Switch_Left', 'type': 'paddle', 'position': (-0.03, 0.01, 0.02)},
            {'name': 'Paddle_Switch_Right', 'type': 'paddle', 'position': (0.03, 0.01, 0.02)},
            {'name': 'Pinky_Switch', 'type': 'toggle', 'position': (-0.02, -0.01, 0.01)}
        ]
        
        for spec in switch_specs:
            switch = self.create_switch_by_type(spec)
            switches.append(switch)
        
        return switches
    
    def create_switch_by_type(self, spec):
        """
        Create specific switch type with full mechanical detail
        """
        switch_type = spec['type']
        position = spec['position']
        name = spec['name']
        
        if switch_type == 'hat_4way':
            return self.create_hat_switch_4way(name, position)
        elif switch_type == 'paddle':
            return self.create_paddle_switch(name, position)
        elif switch_type == 'toggle':
            return self.create_toggle_switch(name, position)
        elif switch_type == 'trigger':
            return self.create_trigger_switch(name, position)
        
        return None
    
    def create_hat_switch_4way(self, name, position):
        """
        Create 4-way hat switch with full mechanical detail
        """
        # Create hat switch base
        bpy.ops.mesh.primitive_cylinder_add(
            radius=0.008, 
            depth=0.006, 
            location=position
        )
        hat_base = bpy.context.active_object
        hat_base.name = f"{name}_Base"
        
        # Create hat switch cap
        bpy.ops.mesh.primitive_uv_sphere_add(
            radius=0.006, 
            location=(position[0], position[1], position[2] + 0.004)
        )
        hat_cap = bpy.context.active_object
        hat_cap.name = f"{name}_Cap"
        
        # Create internal spring mechanism
        spring = self.create_switch_spring(position)
        spring.name = f"{name}_Spring"
        
        # Create electrical contacts
        contacts = self.create_switch_contacts(position)
        for i, contact in enumerate(contacts):
            contact.name = f"{name}_Contact_{i}"
        
        # Parent cap to base for animation
        hat_cap.parent = hat_base
        
        # Add constraint for 4-way movement
        constraint = hat_cap.constraints.new(type='LIMIT_LOCATION')
        constraint.use_min_x = constraint.use_max_x = True
        constraint.use_min_y = constraint.use_max_y = True
        constraint.min_x = constraint.max_x = 0
        constraint.min_y = constraint.max_y = 0
        constraint.owner_space = 'LOCAL'
        
        return hat_base
    
    def create_trigger_mechanism(self):
        """
        Create complete trigger mechanism with realistic mechanical action
        """
        # Create trigger body
        bpy.ops.mesh.primitive_cube_add(
            size=0.02, 
            location=(0.025, 0.04, -0.02)
        )
        trigger = bpy.context.active_object
        trigger.name = "Weapon_Trigger"
        
        # Enter Edit Mode for trigger shaping
        bpy.context.view_layer.objects.active = trigger
        bpy.ops.object.mode_set(mode='EDIT')
        
        # Shape trigger for finger ergonomics
        bpy.ops.mesh.subdivide(number_cuts=3)
        
        # Select front face for trigger curve
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.mesh.select_face_by_sides(number=4, type='EQUAL')
        
        # Extrude and shape trigger curve
        bpy.ops.mesh.extrude_region_move(
            TRANSFORM_OT_translate={"value": (0, 0.01, -0.005)}
        )
        
        bpy.ops.object.mode_set(mode='OBJECT')
        
        # Add Subdivision Surface for smooth trigger
        subsurf = trigger.modifiers.new(name="SubSurf", type='SUBSURF')
        subsurf.levels = 2
        
        # Create trigger pivot mechanism
        pivot = self.create_trigger_pivot()
        pivot.parent = trigger
        
        # Create trigger spring
        spring = self.create_trigger_spring()
        spring.parent = trigger
        
        # Add trigger animation constraints
        constraint = trigger.constraints.new(type='LIMIT_ROTATION')
        constraint.use_limit_x = True
        constraint.min_x = math.radians(-15)
        constraint.max_x = math.radians(0)
        constraint.owner_space = 'LOCAL'
        
        return trigger
    
    def create_internal_wiring(self):
        """
        Create realistic internal wiring harness
        """
        # Create main wire bundle using curves
        bpy.ops.curve.primitive_bezier_curve_add(location=(0, 0, -0.05))
        wire_curve = bpy.context.active_object
        wire_curve.name = "Internal_Wiring"
        
        # Configure curve for wire appearance
        wire_curve.data.bevel_depth = 0.002
        wire_curve.data.bevel_resolution = 4
        wire_curve.data.fill_mode = 'FULL'
        
        # Add multiple control points for realistic routing
        bpy.ops.object.mode_set(mode='EDIT')
        
        # Add control points for wire path
        bpy.ops.curve.subdivide(number_cuts=5)
        
        # Shape wire path through grip interior
        for i, point in enumerate(wire_curve.data.splines[0].bezier_points):
            if i == 1:
                point.co = Vector((0.005, 0.01, -0.03))
            elif i == 2:
                point.co = Vector((-0.005, 0.02, -0.02))
            elif i == 3:
                point.co = Vector((0.01, 0.03, -0.01))
        
        bpy.ops.object.mode_set(mode='OBJECT')
        
        # Convert curve to mesh for export
        bpy.ops.object.convert(target='MESH')
        
        return wire_curve
    
    def apply_hero_materials(self, collection):
        """
        Apply hero-quality materials to all components
        """
        for obj in collection.objects:
            if obj.type == 'MESH':
                # Determine material type based on component name
                if 'Grip' in obj.name:
                    material = self.get_material('Rubber_Grip_Textured_Hero')
                elif 'Switch' in obj.name or 'Button' in obj.name:
                    material = self.get_material('Aluminum_Switch_Hero')
                elif 'Trigger' in obj.name:
                    material = self.get_material('Steel_Trigger_Hero')
                elif 'Wiring' in obj.name:
                    material = self.get_material('Cable_Jacket_Hero')
                else:
                    material = self.get_material('Aluminum_Anodized_Hero')
                
                # Apply material
                if not obj.data.materials:
                    obj.data.materials.append(material)
                else:
                    obj.data.materials[0] = material
    
    def get_material(self, material_name):
        """
        Get or create hero-quality material
        """
        if material_name in bpy.data.materials:
            return bpy.data.materials[material_name]
        
        # Create new hero material if it doesn't exist
        return self.create_hero_material(material_name)
    
    def create_hero_material(self, material_name):
        """
        Create hero-quality PBR material
        """
        mat = bpy.data.materials.new(name=material_name)
        mat.use_nodes = True
        nodes = mat.node_tree.nodes
        links = mat.node_tree.links
        
        # Clear default nodes
        nodes.clear()
        
        # Add Principled BSDF
        principled = nodes.new(type='ShaderNodeBsdfPrincipled')
        principled.location = (0, 0)
        
        # Add Material Output
        output = nodes.new(type='ShaderNodeOutputMaterial')
        output.location = (300, 0)
        links.new(principled.outputs['BSDF'], output.inputs['Surface'])
        
        # Configure material based on type
        if 'Rubber' in material_name:
            principled.inputs['Base Color'].default_value = (0.1, 0.1, 0.1, 1.0)
            principled.inputs['Metallic'].default_value = 0.0
            principled.inputs['Roughness'].default_value = 0.9
            principled.inputs['Subsurface'].default_value = 0.1
        elif 'Aluminum' in material_name:
            principled.inputs['Base Color'].default_value = (0.7, 0.7, 0.75, 1.0)
            principled.inputs['Metallic'].default_value = 1.0
            principled.inputs['Roughness'].default_value = 0.3
            principled.inputs['Anisotropic'].default_value = 0.5
        elif 'Steel' in material_name:
            principled.inputs['Base Color'].default_value = (0.95, 0.95, 0.95, 1.0)
            principled.inputs['Metallic'].default_value = 1.0
            principled.inputs['Roughness'].default_value = 0.1
        
        # Mark as asset
        mat.asset_mark()
        mat.asset_data.description = f"Hero quality material for {material_name}"
        mat.asset_data.tags.new("hero")
        mat.asset_data.tags.new("cockpit")
        
        return mat
    
    def validate_hero_quality(self, collection):
        """
        Validate hero asset meets quality requirements
        """
        validation_results = {
            'triangle_count': 0,
            'material_compliance': True,
            'detail_level': 'HERO',
            'photorealism_score': 0
        }
        
        total_triangles = 0
        
        for obj in collection.objects:
            if obj.type == 'MESH':
                # Calculate triangle count
                obj.data.calc_loop_triangles()
                triangles = len(obj.data.loop_triangles)
                total_triangles += triangles
                
                # Validate materials
                if not obj.data.materials:
                    validation_results['material_compliance'] = False
                    print(f"⚠️  {obj.name} missing material")
                
                # Check detail level
                if triangles < 1000 and 'Hero' in obj.name:
                    print(f"⚠️  {obj.name} may need more detail for hero quality")
        
        validation_results['triangle_count'] = total_triangles
        
        # Check triangle budget
        if total_triangles > self.performance_budget:
            print(f"⚠️  Hero asset exceeds triangle budget: {total_triangles}/{self.performance_budget}")
        else:
            print(f"✓ Hero asset within triangle budget: {total_triangles}/{self.performance_budget}")
        
        # Calculate photorealism score (simplified)
        photorealism_score = 100
        if total_triangles < 50000:
            photorealism_score -= 20  # Insufficient detail
        if not validation_results['material_compliance']:
            photorealism_score -= 30  # Material issues
        
        validation_results['photorealism_score'] = photorealism_score
        
        print(f"Hero Asset Validation Results:")
        print(f"  Triangle Count: {total_triangles}")
        print(f"  Material Compliance: {validation_results['material_compliance']}")
        print(f"  Photorealism Score: {photorealism_score}/100")
        
        return validation_results

# Additional helper methods would be fully implemented here...

def create_all_hero_assets():
    """
    Create all hero assets for Phase 2
    """
    modeler = HeroAssetModeler()
    
    # Create control stick hero
    control_stick = modeler.create_control_stick_hero()
    
    # Create throttle quadrant hero
    throttle_quadrant = modeler.create_throttle_quadrant_hero()
    
    # Create instrument panel hero
    instrument_panel = modeler.create_instrument_panel_hero()
    
    print("All hero assets created successfully")
    
    return [control_stick, throttle_quadrant, instrument_panel]

# Execute hero asset creation
if __name__ == "__main__":
    hero_assets = create_all_hero_assets()
```

VALIDATION REQUIREMENTS:
CURSOR MUST verify after implementation:
✓ All hero assets achieve photorealistic quality indistinguishable from references
✓ Mechanical details are functionally accurate and properly animated
✓ Triangle counts remain within performance budgets while maintaining detail
✓ Materials exhibit correct physical properties under all lighting conditions
✓ All components pass expert validation against real cockpit references
✓ Export pipeline maintains hero quality through Three.js conversion
✓ Performance impact allows smooth viewport operation with all assets
✓ Memory usage remains within acceptable limits during modeling operations

PERFORMANCE BENCHMARKS (MUST ACHIEVE):
✓ Hero asset modeling: <2 hours per major component
✓ Triangle optimization: Maintain <100K triangles per hero asset
✓ Material application: <5 minutes per component
✓ Quality validation: <30 seconds per hero asset
✓ Viewport performance: >25 FPS with all hero assets visible
✓ Memory usage: <6GB during advanced modeling operations
```

**GAP IDENTIFICATION FOR PHASE 2.1**:
```
CURSOR MUST CHECK FOR THESE CRITICAL GAPS:
❌ Missing mechanical detail preventing functional accuracy
❌ Insufficient surface detail breaking photorealistic quality
❌ Poor material application causing unrealistic appearance
❌ Triangle budget exceeded without maintaining visual quality
❌ Missing animation constraints preventing proper interaction
❌ Inadequate reference validation allowing inaccurate modeling
❌ Export compatibility issues preventing Three.js integration
❌ Performance impact preventing smooth workflow operation
```

## Prompt 2.2: Advanced Material System Development

**PREREQUISITE VALIDATION**:
```
CURSOR MUST VERIFY FROM PHASE 2.1:
✓ All hero assets are complete with full mechanical detail
✓ Triangle counts are within budget while maintaining photorealistic quality
✓ Basic materials are applied and rendering correctly in Cycles
✓ Animation constraints are functional for all interactive components
✓ Export pipeline maintains hero asset quality through conversion
✓ Performance benchmarks are met with all hero assets in scene
```

**CURSOR RULES FOR THIS PROMPT**:
1. MUST implement complete advanced material system with all PBR features
2. Each material MUST be indistinguishable from real-world references
3. MUST validate material behavior under all cockpit lighting scenarios
4. Performance optimization MUST maintain photorealistic quality

**DETAILED IMPLEMENTATION**:
```
Develop advanced material system using Blender 4.4's most sophisticated PBR capabilities:

MANDATORY ADVANCED MATERIAL FEATURES:

1. PHYSICALLY ACCURATE MATERIAL LIBRARY (COMPLETE IMPLEMENTATION REQUIRED):
   - MUST implement all military-specification materials:
     * Aluminum 6061-T6 with proper anodizing (Type II, Class 1)
     * Stainless Steel 316L with various surface finishes
     * Titanium Ti-6Al-4V with heat treatment coloration
     * Carbon Fiber Composite with realistic weave patterns
     * Nomex fabric with proper subsurface scattering
     * Optical glass with accurate IOR and transmission
     * Military specification plastics with anti-glare properties
     * Rubber compounds with proper tactile surface properties

2. ADVANCED SHADER DEVELOPMENT (ALL TECHNIQUES REQUIRED):
   - Anisotropic reflection systems:
     * MUST implement brushed metal with directional reflections
     * MUST create carbon fiber with proper weave anisotropy
     * MUST develop fabric materials with fiber-level anisotropy
   - Subsurface scattering implementation:
     * MUST create realistic fabric translucency
     * MUST implement proper skin-like materials for grip surfaces
     * MUST develop realistic plastic translucency effects
   - Advanced layering systems:
     * MUST implement clearcoat over base materials
     * MUST create wear layers with proper edge detection
     * MUST develop dirt and grime accumulation systems

3. PROCEDURAL WEATHERING SYSTEM (FULL IMPLEMENTATION):
   - Automatic wear pattern generation:
     * MUST use Geometry > Pointiness for automatic edge wear
     * MUST implement contact-based wear using vertex colors
     * MUST create procedural dirt accumulation in recesses
     * MUST develop UV-based fading for sun-exposed areas
   - Environmental aging effects:
     * MUST implement oxidation patterns on metal surfaces
     * MUST create realistic fabric fading and wear
     * MUST develop plastic degradation and discoloration
     * MUST implement realistic scratching and scuffing

COMPLETE BLENDER 4.4 MATERIAL IMPLEMENTATION:

Advanced Material System MUST include:
```python
# Blender 4.4 Advanced Material System
import bpy
import mathutils
from mathutils import Vector, Color
import math

class AdvancedMaterialSystem:
    """
    Comprehensive advanced material system for photorealistic cockpit materials
    """
    
    def __init__(self):
        self.material_library = {}
        self.weathering_presets = {}
        self.validation_standards = {}
        self.performance_metrics = {}
        
    def create_complete_material_library(self):
        """
        Create complete library of military-specification materials
        """
        print("Creating advanced material library...")
        
        # Create all required materials
        materials = [
            ('Aluminum_6061_T6_Anodized', 'metal'),
            ('Stainless_Steel_316L_Brushed', 'metal'),
            ('Titanium_Ti6Al4V_Heat_Treated', 'metal'),
            ('Carbon_Fiber_Composite_2x2_Twill', 'composite'),
            ('Nomex_Fabric_Olive_Drab', 'fabric'),
            ('Optical_Glass_Anti_Reflective', 'glass'),
            ('Plastic_ABS_Matte_Black', 'plastic'),
            ('Rubber_EPDM_Textured_Grip', 'rubber'),
            ('Kevlar_Webbing_Tan_499', 'fabric'),
            ('Polycarbonate_Clear_UV_Resistant', 'plastic')
        ]
        
        for material_name, material_type in materials:
            material = self.create_advanced_material(material_name, material_type)
            self.material_library[material_name] = material
            
        print(f"Created {len(materials)} advanced materials")
        return self.material_library
    
    def create_advanced_material(self, name, material_type):
        """
        Create advanced PBR material with full node setup
        """
        mat = bpy.data.materials.new(name=name)
        mat.use_nodes = True
        nodes = mat.node_tree.nodes
        links = mat.node_tree.links
        
        # Clear default nodes
        nodes.clear()
        
        # Create node layout based on material type
        if material_type == 'metal':
            return self.create_advanced_metal_material(mat, name)
        elif material_type == 'composite':
            return self.create_carbon_fiber_material(mat, name)
        elif material_type == 'fabric':
            return self.create_fabric_material(mat, name)
        elif material_type == 'glass':
            return self.create_optical_glass_material(mat, name)
        elif material_type == 'plastic':
            return self.create_advanced_plastic_material(mat, name)
        elif material_type == 'rubber':
            return self.create_rubber_material(mat, name)
        
        return mat
    
    def create_advanced_metal_material(self, mat, name):
        """
        Create advanced metal material with anisotropic reflections
        """
        nodes = mat.node_tree.nodes
        links = mat.node_tree.links
        
        # Principled BSDF
        principled = nodes.new(type='ShaderNodeBsdfPrincipled')
        principled.location = (0, 0)
        principled.inputs['Metallic'].default_value = 1.0
        
        # Material Output
        output = nodes.new(type='ShaderNodeOutputMaterial')
        output.location = (400, 0)
        links.new(principled.outputs['BSDF'], output.inputs['Surface'])
        
        # Texture Coordinate
        tex_coord = nodes.new(type='ShaderNodeTexCoord')
        tex_coord.location = (-800, 0)
        
        # Mapping for texture control
        mapping = nodes.new(type='ShaderNodeMapping')
        mapping.location = (-600, 0)
        links.new(tex_coord.outputs['UV'], mapping.inputs['Vector'])
        
        # Configure based on specific metal type
        if 'Aluminum' in name:
            self.setup_aluminum_material(nodes, links, principled, mapping)
        elif 'Stainless' in name:
            self.setup_stainless_steel_material(nodes, links, principled, mapping)
        elif 'Titanium' in name:
            self.setup_titanium_material(nodes, links, principled, mapping)
        
        # Add weathering system
        self.add_weathering_system(nodes, links, principled, name)
        
        # Mark as asset
        mat.asset_mark()
        mat.asset_data.description = f"Advanced {name} material with weathering"
        mat.asset_data.tags.new("advanced")
        mat.asset_data.tags.new("metal")
        mat.asset_data.tags.new("cockpit")
        
        return mat
    
    def setup_aluminum_material(self, nodes, links, principled, mapping):
        """
        Setup aluminum 6061-T6 with anodizing
        """
        # Base color for anodized aluminum
        principled.inputs['Base Color'].default_value = (0.7, 0.7, 0.75, 1.0)
        principled.inputs['Roughness'].default_value = 0.3
        principled.inputs['Anisotropic'].default_value = 0.5
        
        # Create brushed texture using noise
        noise = nodes.new(type='ShaderNodeTexNoise')
        noise.location = (-400, 200)
        noise.inputs['Scale'].default_value = 100.0
        noise.inputs['Detail'].default_value = 0.0
        noise.inputs['Roughness'].default_value = 0.0
        
        # ColorRamp for brushed pattern
        colorramp = nodes.new(type='ShaderNodeValToRGB')
        colorramp.location = (-200, 200)
        colorramp.color_ramp.elements[0].position = 0.45
        colorramp.color_ramp.elements[1].position = 0.55
        
        # Connect brushed texture to roughness
        links.new(mapping.outputs['Vector'], noise.inputs['Vector'])
        links.new(noise.outputs['Fac'], colorramp.inputs['Fac'])
        links.new(colorramp.outputs['Color'], principled.inputs['Roughness'])
        
        # Add anisotropic rotation control
        separate_xyz = nodes.new(type='ShaderNodeSeparateXYZ')
        separate_xyz.location = (-400, 0)
        links.new(tex_coord.outputs['UV'], separate_xyz.inputs['Vector'])
        
        # Use U coordinate for anisotropic rotation
        math_multiply = nodes.new(type='ShaderNodeMath')
        math_multiply.location = (-200, 0)
        math_multiply.operation = 'MULTIPLY'
        math_multiply.inputs[1].default_value = 0.5
        
        links.new(separate_xyz.outputs['X'], math_multiply.inputs[0])
        links.new(math_multiply.outputs['Value'], principled.inputs['Anisotropic Rotation'])
    
    def setup_stainless_steel_material(self, nodes, links, principled, mapping):
        """
        Setup stainless steel 316L with brushed finish
        """
        # Base color for stainless steel
        principled.inputs['Base Color'].default_value = (0.95, 0.95, 0.95, 1.0)
        principled.inputs['Roughness'].default_value = 0.1
        principled.inputs['Anisotropic'].default_value = 0.8
        
        # Create fine brushed texture
        wave = nodes.new(type='ShaderNodeTexWave')
        wave.location = (-400, 200)
        wave.wave_type = 'BANDS'
        wave.inputs['Scale'].default_value = 200.0
        wave.inputs['Distortion'].default_value = 0.0
        
        # ColorRamp for fine brushing
        colorramp = nodes.new(type='ShaderNodeValToRGB')
        colorramp.location = (-200, 200)
        colorramp.color_ramp.elements[0].position = 0.48
        colorramp.color_ramp.elements[1].position = 0.52
        
        # Connect to roughness
        links.new(mapping.outputs['Vector'], wave.inputs['Vector'])
        links.new(wave.outputs['Color'], colorramp.inputs['Fac'])
        links.new(colorramp.outputs['Color'], principled.inputs['Roughness'])
    
    def create_carbon_fiber_material(self, mat, name):
        """
        Create carbon fiber composite with realistic weave pattern
        """
        nodes = mat.node_tree.nodes
        links = mat.node_tree.links
        
        # Principled BSDF
        principled = nodes.new(type='ShaderNodeBsdfPrincipled')
        principled.location = (0, 0)
        principled.inputs['Base Color'].default_value = (0.02, 0.02, 0.02, 1.0)
        principled.inputs['Metallic'].default_value = 0.0
        principled.inputs['Roughness'].default_value = 0.2
        principled.inputs['Anisotropic'].default_value = 0.9
        
        # Material Output
        output = nodes.new(type='ShaderNodeOutputMaterial')
        output.location = (400, 0)
        links.new(principled.outputs['BSDF'], output.inputs['Surface'])
        
        # Create carbon fiber weave pattern
        tex_coord = nodes.new(type='ShaderNodeTexCoord')
        tex_coord.location = (-800, 0)
        
        mapping = nodes.new(type='ShaderNodeMapping')
        mapping.location = (-600, 0)
        mapping.inputs['Scale'].default_value = (50, 50, 1)
        links.new(tex_coord.outputs['UV'], mapping.inputs['Vector'])
        
        # Create weave pattern using wave textures
        wave_u = nodes.new(type='ShaderNodeTexWave')
        wave_u.location = (-400, 200)
        wave_u.wave_type = 'BANDS'
        wave_u.inputs['Scale'].default_value = 10.0
        
        wave_v = nodes.new(type='ShaderNodeTexWave')
        wave_v.location = (-400, 0)
        wave_v.wave_type = 'BANDS'
        wave_v.inputs['Scale'].default_value = 10.0
        wave_v.inputs['Wave Profile'].default_value = 1.0  # Sawtooth
        
        # Rotate V wave by 90 degrees
        mapping_v = nodes.new(type='ShaderNodeMapping')
        mapping_v.location = (-600, -200)
        mapping_v.inputs['Rotation'].default_value = (0, 0, math.radians(90))
        
        links.new(mapping.outputs['Vector'], wave_u.inputs['Vector'])
        links.new(mapping.outputs['Vector'], mapping_v.inputs['Vector'])
        links.new(mapping_v.outputs['Vector'], wave_v.inputs['Vector'])
        
        # Combine weave patterns
        mix_weave = nodes.new(type='ShaderNodeMix')
        mix_weave.location = (-200, 100)
        mix_weave.data_type = 'RGBA'
        mix_weave.blend_type = 'MULTIPLY'
        
        links.new(wave_u.outputs['Color'], mix_weave.inputs['Color1'])
        links.new(wave_v.outputs['Color'], mix_weave.inputs['Color2'])
        
        # Apply weave to normal and roughness
        links.new(mix_weave.outputs['Color'], principled.inputs['Roughness'])
        
        # Create normal map from weave
        normal_map = nodes.new(type='ShaderNodeNormalMap')
        normal_map.location = (-200, -100)
        links.new(mix_weave.outputs['Color'], normal_map.inputs['Color'])
        links.new(normal_map.outputs['Normal'], principled.inputs['Normal'])
        
        return mat
    
    def create_fabric_material(self, mat, name):
        """
        Create fabric material with subsurface scattering
        """
        nodes = mat.node_tree.nodes
        links = mat.node_tree.links
        
        # Principled BSDF
        principled = nodes.new(type='ShaderNodeBsdfPrincipled')
        principled.location = (0, 0)
        principled.inputs['Metallic'].default_value = 0.0
        principled.inputs['Roughness'].default_value = 0.9
        principled.inputs['Subsurface'].default_value = 0.1
        
        # Configure based on fabric type
        if 'Nomex' in name:
            principled.inputs['Base Color'].default_value = (0.2, 0.3, 0.1, 1.0)  # Olive drab
            principled.inputs['Subsurface Color'].default_value = (0.3, 0.4, 0.2, 1.0)
        elif 'Kevlar' in name:
            principled.inputs['Base Color'].default_value = (0.8, 0.7, 0.5, 1.0)  # Tan
            principled.inputs['Subsurface Color'].default_value = (0.9, 0.8, 0.6, 1.0)
        
        # Material Output
        output = nodes.new(type='ShaderNodeOutputMaterial')
        output.location = (400, 0)
        links.new(principled.outputs['BSDF'], output.inputs['Surface'])
        
        # Create fabric weave texture
        tex_coord = nodes.new(type='ShaderNodeTexCoord')
        tex_coord.location = (-800, 0)
        
        mapping = nodes.new(type='ShaderNodeMapping')
        mapping.location = (-600, 0)
        mapping.inputs['Scale'].default_value = (200, 200, 1)
        links.new(tex_coord.outputs['UV'], mapping.inputs['Vector'])
        
        # Fabric weave using Voronoi texture
        voronoi = nodes.new(type='ShaderNodeTexVoronoi')
        voronoi.location = (-400, 0)
        voronoi.feature = 'F1'
        voronoi.inputs['Scale'].default_value = 100.0
        
        links.new(mapping.outputs['Vector'], voronoi.inputs['Vector'])
        
        # Apply to normal and roughness
        normal_map = nodes.new(type='ShaderNodeNormalMap')
        normal_map.location = (-200, -100)
        normal_map.inputs['Strength'].default_value = 0.5
        
        links.new(voronoi.outputs['Distance'], normal_map.inputs['Color'])
        links.new(normal_map.outputs['Normal'], principled.inputs['Normal'])
        
        return mat
    
    def add_weathering_system(self, nodes, links, principled, material_name):
        """
        Add procedural weathering system to material
        """
        # Get geometry pointiness for edge wear
        geometry = nodes.new(type='ShaderNodeNewGeometry')
        geometry.location = (-800, -400)
        
        # ColorRamp for edge wear control
        edge_wear_ramp = nodes.new(type='ShaderNodeValToRGB')
        edge_wear_ramp.location = (-600, -400)
        edge_wear_ramp.color_ramp.elements[0].position = 0.7
        edge_wear_ramp.color_ramp.elements[1].position = 1.0
        
        links.new(geometry.outputs['Pointiness'], edge_wear_ramp.inputs['Fac'])
        
        # Mix worn and clean materials
        mix_wear = nodes.new(type='ShaderNodeMix')
        mix_wear.location = (-200, -300)
        mix_wear.data_type = 'RGBA'
        
        # Get current roughness connection
        current_roughness = principled.inputs['Roughness']
        if current_roughness.is_linked:
            # Store current connection
            current_node = current_roughness.links[0].from_node
            current_output = current_roughness.links[0].from_socket
            
            # Disconnect current
            links.remove(current_roughness.links[0])
            
            # Connect through wear mixer
            links.new(current_output, mix_wear.inputs['Color1'])
            mix_wear.inputs['Color2'].default_value = (0.8, 0.8, 0.8, 1.0)  # Worn roughness
            links.new(edge_wear_ramp.outputs['Color'], mix_wear.inputs['Fac'])
            links.new(mix_wear.outputs['Color'], principled.inputs['Roughness'])
        
        # Add dirt accumulation in recesses
        dirt_noise = nodes.new(type='ShaderNodeTexNoise')
        dirt_noise.location = (-600, -600)
        dirt_noise.inputs['Scale'].default_value = 50.0
        
        # Invert pointiness for recesses
        invert_pointiness = nodes.new(type='ShaderNodeInvert')
        invert_pointiness.location = (-400, -500)
        links.new(geometry.outputs['Pointiness'], invert_pointiness.inputs['Color'])
        
        # Mix dirt with base color
        mix_dirt = nodes.new(type='ShaderNodeMix')
        mix_dirt.location = (-200, -500)
        mix_dirt.data_type = 'RGBA'
        mix_dirt.inputs['Color2'].default_value = (0.1, 0.08, 0.06, 1.0)  # Dirt color
        
        # Get current base color
        current_base_color = principled.inputs['Base Color'].default_value
        mix_dirt.inputs['Color1'].default_value = current_base_color
        
        links.new(invert_pointiness.outputs['Color'], mix_dirt.inputs['Fac'])
        links.new(mix_dirt.outputs['Color'], principled.inputs['Base Color'])
    
    def validate_material_quality(self, material):
        """
        Validate material meets photorealistic standards
        """
        validation_results = {
            'name': material.name,
            'pbr_compliant': False,
            'node_count': 0,
            'texture_count': 0,
            'performance_score': 100,
            'photorealism_score': 0
        }
        
        if not material.use_nodes:
            validation_results['pbr_compliant'] = False
            return validation_results
        
        nodes = material.node_tree.nodes
        validation_results['node_count'] = len(nodes)
        
        # Check for Principled BSDF
        principled_nodes = [n for n in nodes if n.type == 'BSDF_PRINCIPLED']
        validation_results['pbr_compliant'] = len(principled_nodes) > 0
        
        # Count texture nodes
        texture_nodes = [n for n in nodes if n.type == 'TEX_IMAGE']
        validation_results['texture_count'] = len(texture_nodes)
        
        # Calculate performance score
        performance_score = 100
        performance_score -= len(nodes) * 2  # Node complexity penalty
        performance_score -= len(texture_nodes) * 10  # Texture penalty
        validation_results['performance_score'] = max(performance_score, 0)
        
        # Calculate photorealism score
        photorealism_score = 0
        if validation_results['pbr_compliant']:
            photorealism_score += 40
        if len(texture_nodes) > 0:
            photorealism_score += 20
        if len(nodes) > 10:  # Complex shader
            photorealism_score += 20
        if 'weathering' in material.name.lower():
            photorealism_score += 20
        
        validation_results['photorealism_score'] = photorealism_score
        
        return validation_results
    
    def generate_material_report(self):
        """
        Generate comprehensive material validation report
        """
        report_path = bpy.path.abspath("//material_validation_report.txt")
        
        with open(report_path, 'w') as f:
            f.write("ADVANCED MATERIAL SYSTEM VALIDATION REPORT\n")
            f.write("=" * 60 + "\n\n")
            
            total_materials = len(self.material_library)
            f.write(f"Total Materials: {total_materials}\n\n")
            
            for material_name, material in self.material_library.items():
                validation = self.validate_material_quality(material)
                
                f.write(f"{material_name}:\n")
                f.write(f"  PBR Compliant: {validation['pbr_compliant']}\n")
                f.write(f"  Node Count: {validation['node_count']}\n")
                f.write(f"  Texture Count: {validation['texture_count']}\n")
                f.write(f"  Performance Score: {validation['performance_score']}/100\n")
                f.write(f"  Photorealism Score: {validation['photorealism_score']}/100\n")
                
                if validation['photorealism_score'] < 60:
                    f.write("  ⚠️  Low photorealism score - needs improvement\n")
                if validation['performance_score'] < 50:
                    f.write("  ⚠️  Performance concerns - optimize node tree\n")
                
                f.write("\n")
        
        print(f"Material validation report saved to: {report_path}")

# Usage
def create_advanced_material_system():
    """
    Create complete advanced material system
    """
    material_system = AdvancedMaterialSystem()
    
    # Create all materials
    materials = material_system.create_complete_material_library()
    
    # Validate all materials
    for material in materials.values():
        validation = material_system.validate_material_quality(material)
        print(f"Material {material.name}: Photorealism {validation['photorealism_score']}/100")
    
    # Generate report
    material_system.generate_material_report()
    
    return material_system

# Execute material system creation
if __name__ == "__main__":
    advanced_materials = create_advanced_material_system()
```

VALIDATION REQUIREMENTS:
CURSOR MUST verify after implementation:
✓ All materials exhibit physically correct behavior under all lighting conditions
✓ Anisotropic reflections accurately represent real-world material properties
✓ Subsurface scattering creates realistic translucency effects
✓ Weathering systems add authentic aging without breaking material realism
✓ Performance impact allows smooth viewport operation with all materials
✓ Export pipeline maintains material fidelity through Three.js conversion
✓ Color accuracy matches military specification standards
✓ All materials pass expert validation against real-world references

PERFORMANCE BENCHMARKS (MUST ACHIEVE):
✓ Material compilation: <30 seconds for complete library
✓ Shader performance: <0.5ms per material per frame
✓ Memory usage: <1GB for all materials and textures
✓ Export conversion: 100% material fidelity preservation
✓ Viewport responsiveness: >25 FPS with all materials applied
✓ Quality validation: <60 seconds for complete material library
```

**GAP IDENTIFICATION FOR PHASE 2.2**:
```
CURSOR MUST CHECK FOR THESE CRITICAL GAPS:
❌ Missing PBR compliance preventing realistic material behavior
❌ Inadequate anisotropic setup reducing material authenticity
❌ Poor subsurface scattering breaking fabric and plastic realism
❌ Missing weathering effects preventing authentic aging appearance
❌ Performance issues causing viewport lag with complex materials
❌ Export compatibility problems preventing Three.js material fidelity
❌ Color inaccuracy failing military specification standards
❌ Missing validation allowing unrealistic material behavior
```

## PHASE 2 COMPLETION CHECKLIST

### ✅ **BLENDER 4.4 HERO ASSET VALIDATION**
- [ ] All hero assets achieve photorealistic quality indistinguishable from real cockpit photos
- [ ] Mechanical details are functionally accurate with proper animation constraints
- [ ] Triangle counts remain within performance budgets while maintaining maximum detail
- [ ] All interactive components have realistic mechanical behavior and feedback
- [ ] Surface details withstand close inspection at 0.1m viewing distance
- [ ] Expert validation confirms accuracy against real F-22/F-35 references
- [ ] Export pipeline maintains hero quality through Three.js conversion
- [ ] Performance allows smooth operation with all hero assets in scene

### ✅ **ADVANCED MATERIAL SYSTEM VALIDATION**
- [ ] All materials exhibit physically correct behavior under all lighting scenarios
- [ ] Anisotropic reflections accurately represent brushed metals and carbon fiber
- [ ] Subsurface scattering creates realistic fabric and plastic translucency
- [ ] Weathering systems add authentic aging without breaking material realism
- [ ] Color accuracy matches military specification standards within 2% tolerance
- [ ] Performance impact maintains smooth viewport operation >25 FPS
- [ ] Export compatibility preserves 100% material fidelity in Three.js
- [ ] All materials pass expert validation against real-world material samples

### ✅ **PERFORMANCE BENCHMARKS**
- [ ] Hero asset modeling: <2 hours per major component with full detail
- [ ] Triangle optimization: <100K triangles per hero asset maintained
- [ ] Material compilation: <30 seconds for complete advanced library
- [ ] Quality validation: <60 seconds for all assets and materials
- [ ] Viewport performance: >25 FPS with all hero assets and materials
- [ ] Memory usage: <6GB during advanced modeling and material operations
- [ ] Export process: <120 seconds per hero assembly with materials

**PHASE 2 MUST BE 100% COMPLETE BEFORE PROCEEDING TO PHASE 3**

---

*This document serves as the definitive guide for Blender Phase 2 development in the Fighter Jet Cockpit project. All advanced modeling and material work must follow these processes and meet these standards to achieve the target photorealistic quality and maintain Three.js compatibility.*
