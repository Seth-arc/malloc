# BLENDER PHASE 1: FOUNDATION AND ASSET PIPELINE (BLENDER 4.4)

## PROJECT RULES & CONSTRAINTS

### MANDATORY DEVELOPMENT RULES FOR ALL BLENDER PHASES:

1. **BLENDER VERSION RESTRICTIONS**: 
   - Use ONLY Blender 4.4 LTS (Long Term Support)
   - NO other 3D software except for reference comparison
   - NO external plugins except officially approved add-ons
   - NO custom Python scripts unless fully documented and validated

2. **ASSET COMPLETENESS**: 
   - Provide COMPLETE, export-ready models for every prompt
   - NEVER use placeholders like "..." or "[model details here]"
   - All geometry must be fully modeled with proper topology
   - All materials must be completely set up with full node trees
   - All UV maps must be unwrapped and optimized

3. **BLENDER-THREE.JS CONSISTENCY**: 
   - Maintain perfect compatibility between Blender 4.4 and Three.js export
   - Ensure all materials translate correctly to glTF 2.0 format
   - Verify coordinate systems match (Y-up in Blender, compatible with Three.js)
   - Test all exports in Three.js environment before approval

4. **QUALITY GATES**: 
   - Each phase MUST pass Blender-specific validation before proceeding
   - Identify and fix ALL modeling gaps that could limit final quality
   - No phase advancement without successful Blender scene validation
   - All assets must meet photorealistic quality standards in Cycles rendering

5. **PERFORMANCE REQUIREMENTS**: 
   - Maintain <100K triangles per hero asset in Blender
   - Memory usage must not exceed 4GB during Blender operations
   - Export time must not exceed 30 seconds per major component
   - Real-time viewport performance must maintain >30 FPS in Material Preview

## PRE-PHASE 1 VALIDATION:
**CURSOR MUST CHECK:**
```
✓ Blender 4.4 LTS is installed and properly configured
✓ glTF 2.0 export add-on is enabled and functional
✓ Cycles render engine is set as default with GPU acceleration
✓ Asset Browser is configured for project organization
✓ No conflicting add-ons or custom configurations exist
```

## Prompt 1.1: Blender 4.4 Project Foundation Setup

**PREREQUISITE VALIDATION**: None (Initial setup)

**CURSOR RULES FOR THIS PROMPT**:
1. Create COMPLETE Blender project structure with all necessary collections
2. Implement FULL material library with PBR Principled BSDF setup
3. NO placeholder objects - everything must be production-ready
4. Must support both Cycles and Eevee rendering with identical results

**DETAILED IMPLEMENTATION**:
```
Create a professional Blender 4.4 project with the following COMPLETE structure:

BLENDER PROJECT STRUCTURE (create ALL collections and setup):
├── Scene Collection
│   ├── 01_COCKPIT_STRUCTURE/
│   │   ├── Cockpit_Tub_Hero (COMPLETE high-poly model)
│   │   ├── Canopy_Frame_Hero (FULL structural detail)
│   │   ├── Ejection_Seat_Rails (COMPLETE mounting system)
│   │   └── Reference_Empties (Pilot eye position, measurement guides)
│   ├── 02_FLIGHT_CONTROLS/
│   │   ├── Control_Stick_Assembly (FULL detail with all switches)
│   │   ├── Throttle_Quadrant (COMPLETE dual throttle system)
│   │   ├── Rudder_Pedals (FULL pedal assembly with mechanisms)
│   │   └── Control_Linkages (COMPLETE mechanical connections)
│   ├── 03_INSTRUMENT_PANELS/
│   │   ├── Central_Console_Hero (FULL switch and display layout)
│   │   ├── Left_Console_Primary (COMPLETE environmental controls)
│   │   ├── Right_Console_Primary (FULL weapon systems panel)
│   │   └── Individual_Components (ALL switches, buttons, displays)
│   ├── 04_DISPLAY_SYSTEMS/
│   │   ├── Primary_MFDs (COMPLETE bezel and screen assembly)
│   │   ├── HUD_Combiner (FULL optical glass and mounting)
│   │   ├── Warning_Lights (ALL indicator panels and LEDs)
│   │   └── Backlighting_System (COMPLETE illumination setup)
│   ├── 05_SEATING_SYSTEM/
│   │   ├── ACES_II_Seat_Hero (FULL ejection seat with all details)
│   │   ├── Harness_System (COMPLETE 5-point harness with hardware)
│   │   ├── Cushions_and_Padding (FULL fabric simulation setup)
│   │   └── Adjustment_Mechanisms (ALL functional seat adjustments)
│   ├── 06_ENVIRONMENTAL/
│   │   ├── Lighting_Fixtures (ALL interior lighting systems)
│   │   ├── Ventilation_Grilles (COMPLETE air circulation system)
│   │   ├── Wiring_Harnesses (FULL cable routing and management)
│   │   └── Access_Panels (ALL maintenance and service panels)
│   ├── 07_GLASS_ELEMENTS/
│   │   ├── Main_Canopy_Glass (COMPLETE optical glass with coatings)
│   │   ├── Instrument_Covers (ALL gauge and display glass)
│   │   ├── HUD_Glass (FULL combiner glass with optical properties)
│   │   └── Mirror_Systems (COMPLETE rearview and inspection mirrors)
│   └── 08_REFERENCE_MATERIALS/
│       ├── Reference_Images (Organized by component type)
│       ├── Technical_Drawings (CAD references and measurements)
│       ├── Color_Standards (Military specification color swatches)
│       └── Material_Samples (Physical reference materials)

MANDATORY BLENDER 4.4 SETUP REQUIREMENTS:

1. Scene Configuration MUST include:
   - Units set to Metric (meters) for real-world scale
   - Coordinate system: Y-up, Z-forward (Blender default)
   - Scene scale: 1 Blender unit = 1 meter
   - Render engine: Cycles with GPU acceleration enabled
   - Color management: ACES with sRGB display transform
   - Asset Browser library configured for project assets

2. Material Library MUST implement:
   - Complete PBR Principled BSDF setup for all material types
   - Aluminum_Anodized_Hero (Metallic=1.0, Roughness=0.3, proper anisotropy)
   - Steel_Polished_Primary (Metallic=1.0, Roughness=0.1, high reflectance)
   - Plastic_MilSpec_Black (Metallic=0.0, Roughness=0.8, anti-glare properties)
   - Fabric_Nomex_Cushion (Subsurface scattering, proper fabric shader)
   - Glass_Optical_Canopy (Transmission=1.0, IOR=1.52, anti-reflective coating)
   - Carbon_Fiber_Composite (Anisotropic weave pattern, resin coating)
   - Rubber_Grip_Textured (High roughness, tactile surface properties)

3. Lighting Setup MUST include:
   - HDRI world environment for realistic reflections
   - Sun lamp positioned for cockpit interior illumination
   - Area lights for instrument panel backlighting (minimum 8 lights)
   - Point lights for specific detail illumination (minimum 12 lights)
   - Proper light linking for hero asset presentation
   - Light temperature values matching real cockpit conditions

4. Camera System MUST implement:
   - Primary camera at pilot eye position (X=0, Y=1.2, Z=0.3)
   - Hero asset inspection cameras for close-up validation
   - Orthographic cameras for technical documentation
   - Animation-ready camera rigs for presentation sequences
   - Proper depth of field settings for realistic focus

VALIDATION CHECKPOINT:
After implementation, CURSOR MUST verify:
✓ All collections are created and properly organized
✓ Material library renders correctly in both Cycles and Eevee
✓ Lighting system provides even illumination without artifacts
✓ Camera system captures all required viewing angles
✓ Asset Browser is populated with reusable components
✓ Export pipeline produces clean glTF 2.0 files
✓ Memory usage remains under 2GB for base scene
✓ Viewport performance maintains >30 FPS in Material Preview

QUALITY GATE:
✓ Cycles rendering produces photorealistic results
✓ Material preview shows accurate PBR behavior
✓ All collections are logically organized and named
✓ Asset Browser enables efficient component reuse
✓ Export pipeline maintains material fidelity
✓ Scene file size remains under 500MB
```

**GAP IDENTIFICATION FOR PHASE 1.1**:
```
CURSOR MUST CHECK FOR THESE POTENTIAL GAPS:
❌ Missing material nodes causing incorrect PBR behavior
❌ Improper lighting setup limiting photorealistic quality
❌ Incorrect coordinate system causing Three.js export issues
❌ Missing Asset Browser organization preventing efficient workflow
❌ Inadequate camera setup limiting validation capabilities
❌ Poor collection organization causing workflow inefficiency
❌ Missing reference materials limiting accuracy validation
❌ Incorrect scene scale causing proportion issues
```

## Prompt 1.2: Advanced Blender 4.4 Asset Pipeline

**PREREQUISITE VALIDATION**:
```
CURSOR MUST VERIFY FROM PHASE 1.1:
✓ Blender project structure is complete and organized
✓ Material library renders correctly in Cycles
✓ Lighting system provides proper illumination
✓ Camera system captures all required angles
✓ Asset Browser is functional and organized
✓ Export pipeline produces valid glTF files
```

**CURSOR RULES FOR THIS PROMPT**:
1. MUST implement ALL advanced Blender 4.4 features for asset creation
2. Each asset MUST have complete LOD system with smooth transitions
3. MUST validate each asset exports correctly to Three.js format
4. Performance optimization MUST be measured and documented

**DETAILED IMPLEMENTATION**:
```
Configure advanced Blender 4.4 asset pipeline for professional-quality output:

MANDATORY ADVANCED ASSET CREATION FEATURES:

1. GEOMETRY NODES PIPELINE (COMPLETE IMPLEMENTATION REQUIRED):
   - MUST implement procedural detail generation for repetitive elements:
     * Rivet placement using Array and Instance on Points nodes
     * Cable routing using Curve to Mesh and Resample Curve nodes
     * Panel line generation using Edge to Curve and Curve to Mesh
     * Wear pattern generation using Noise Texture and Displacement
   - MUST support parametric modeling for easy iteration:
     * Exposed parameters for rivet spacing, cable thickness, panel gaps
     * Driver-based controls for procedural detail density
     * Modifier stack organization for non-destructive workflow
   - MUST implement asset variation system:
     * Multiple wear states (new, used, heavily worn)
     * Component variations (different switch types, panel layouts)
     * Procedural damage and weathering effects

2. ADVANCED SCULPTING WORKFLOW (ALL TECHNIQUES REQUIRED):
   - High-frequency detail sculpting for hero assets:
     * MUST implement Multiresolution modifier workflow
     * MUST use Alpha brushes for surface texture creation
     * MUST implement proper retopology for game-ready assets
     * MUST bake high-poly details to normal maps using Cycles
   - Surface detail enhancement:
     * MUST sculpt wear patterns and contact points
     * MUST add manufacturing details (seams, joints, fasteners)
     * MUST implement realistic surface imperfections
     * MUST create variation masks for procedural texturing

3. ADVANCED UV MAPPING SYSTEM (COMPLETE IMPLEMENTATION):
   - MUST implement UDIM workflow for hero assets:
     * Multiple 4K texture tiles for maximum detail
     * Proper tile organization and naming convention
     * Seamless texture painting across UDIM boundaries
     * Efficient memory usage and streaming optimization
   - UV optimization requirements:
     * MUST achieve >95% UV space utilization
     * MUST implement proper seam placement for minimal distortion
     * MUST use angle-based unwrapping with manual seam control
     * MUST implement texture density consistency across all assets

4. MATERIAL AUTHORING PIPELINE (FULL IMPLEMENTATION):
   - Advanced Principled BSDF setup:
     * MUST implement proper metallic/roughness workflow
     * MUST use Fresnel-based mixing for realistic material blending
     * MUST implement anisotropic reflections for brushed metals
     * MUST use proper subsurface scattering for fabric materials
   - Procedural material enhancement:
     * MUST implement Geometry > Pointiness for automatic edge wear
     * MUST use Noise textures for surface variation
     * MUST implement ColorRamp nodes for precise control
     * MUST create reusable node groups for common material types

COMPLETE IMPLEMENTATION REQUIREMENTS:

Asset Creation Workflow MUST include:
```python
# Blender 4.4 Asset Creation Script Template
import bpy
import bmesh
import mathutils

def create_hero_cockpit_component(component_name, base_geometry_type):
    """
    Create a complete hero-quality cockpit component
    """
    # Create base mesh
    if base_geometry_type == 'panel':
        bpy.ops.mesh.primitive_cube_add(size=1.0)
    elif base_geometry_type == 'control':
        bpy.ops.mesh.primitive_cylinder_add(radius=0.05, depth=0.2)
    elif base_geometry_type == 'display':
        bpy.ops.mesh.primitive_cube_add(size=0.3)
    
    obj = bpy.context.active_object
    obj.name = component_name
    
    # Add Multiresolution modifier for sculpting
    multires = obj.modifiers.new(name="Multiresolution", type='MULTIRES')
    
    # Add Geometry Nodes for procedural details
    geo_nodes = obj.modifiers.new(name="Procedural_Details", type='NODES')
    
    # Create custom node group for component type
    node_group = create_component_node_group(component_name, base_geometry_type)
    geo_nodes.node_group = node_group
    
    # Setup material
    material = create_component_material(component_name, base_geometry_type)
    obj.data.materials.append(material)
    
    # Setup UV mapping
    setup_component_uvs(obj, base_geometry_type)
    
    # Add to appropriate collection
    collection_name = get_component_collection(base_geometry_type)
    collection = bpy.data.collections.get(collection_name)
    if collection:
        collection.objects.link(obj)
        bpy.context.scene.collection.objects.unlink(obj)
    
    return obj

def create_component_node_group(component_name, geometry_type):
    """
    Create Geometry Nodes setup for component type
    """
    # Create new node group
    node_group = bpy.data.node_groups.new(
        name=f"{component_name}_Procedural", 
        type='GeometryNodeTree'
    )
    
    # Add input and output nodes
    input_node = node_group.nodes.new('NodeGroupInput')
    output_node = node_group.nodes.new('NodeGroupOutput')
    
    # Create geometry input/output sockets
    node_group.interface.new_socket('Geometry', in_out='INPUT', socket_type='NodeSocketGeometry')
    node_group.interface.new_socket('Geometry', in_out='OUTPUT', socket_type='NodeSocketGeometry')
    
    # Add component-specific procedural details
    if geometry_type == 'panel':
        add_panel_procedural_details(node_group, input_node, output_node)
    elif geometry_type == 'control':
        add_control_procedural_details(node_group, input_node, output_node)
    elif geometry_type == 'display':
        add_display_procedural_details(node_group, input_node, output_node)
    
    return node_group

def create_component_material(component_name, geometry_type):
    """
    Create complete PBR material for component
    """
    mat = bpy.data.materials.new(name=f"{component_name}_Material")
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
    
    # Setup material properties based on component type
    if geometry_type == 'panel':
        setup_panel_material(nodes, links, principled)
    elif geometry_type == 'control':
        setup_control_material(nodes, links, principled)
    elif geometry_type == 'display':
        setup_display_material(nodes, links, principled)
    
    # Mark as asset for Asset Browser
    mat.asset_mark()
    mat.asset_data.description = f"PBR material for {component_name}"
    mat.asset_data.tags.new("cockpit")
    mat.asset_data.tags.new(geometry_type)
    
    return mat

def setup_component_uvs(obj, geometry_type):
    """
    Setup optimized UV mapping for component
    """
    # Enter Edit Mode
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.mode_set(mode='EDIT')
    
    # Select all geometry
    bpy.ops.mesh.select_all(action='SELECT')
    
    # Smart UV Project with optimized settings
    bpy.ops.uv.smart_project(
        angle_limit=66.0,
        island_margin=0.02,
        area_weight=0.0,
        correct_aspect=True,
        scale_to_bounds=False
    )
    
    # Return to Object Mode
    bpy.ops.object.mode_set(mode='OBJECT')
    
    # Validate UV efficiency
    uv_efficiency = calculate_uv_efficiency(obj)
    if uv_efficiency < 0.90:
        print(f"Warning: UV efficiency for {obj.name} is {uv_efficiency:.2%}")

# Additional helper functions would be fully implemented here...
```

VALIDATION REQUIREMENTS:
CURSOR MUST verify after implementation:
✓ All Geometry Nodes setups work without errors
✓ Sculpting workflow produces high-quality details
✓ UV mapping achieves >90% efficiency
✓ Materials render correctly in Cycles and Eevee
✓ Export pipeline maintains all asset details
✓ Performance remains within acceptable limits
✓ Asset Browser organization enables efficient reuse
✓ LOD system provides smooth quality transitions

PERFORMANCE BENCHMARKS (MUST ACHIEVE):
✓ Geometry Nodes evaluation: <100ms per component
✓ Sculpting responsiveness: >20 FPS in Sculpt Mode
✓ UV unwrapping: <30 seconds per hero asset
✓ Material compilation: <10 seconds per material
✓ Export time: <60 seconds per complete assembly
✓ Memory usage: <4GB for full scene with all assets
```

**GAP IDENTIFICATION FOR PHASE 1.2**:
```
CURSOR MUST CHECK FOR THESE CRITICAL GAPS:
❌ Missing Geometry Nodes causing lack of procedural detail
❌ Incomplete sculpting workflow limiting surface quality
❌ Poor UV mapping reducing texture quality and efficiency
❌ Inadequate material setup preventing photorealistic results
❌ Missing LOD system causing performance issues
❌ Incomplete Asset Browser organization reducing workflow efficiency
❌ Export pipeline issues causing Three.js compatibility problems
❌ Performance bottlenecks preventing smooth workflow
```

## Prompt 1.3: Blender 4.4 Quality Assurance & Export Pipeline

**PREREQUISITE VALIDATION**:
```
CURSOR MUST VERIFY FROM PHASES 1.1-1.2:
✓ Complete project structure with all collections organized
✓ Advanced asset pipeline producing high-quality components
✓ Geometry Nodes systems working without errors
✓ Material library rendering correctly in all engines
✓ UV mapping achieving efficiency targets
✓ Sculpting workflow producing detailed surfaces
✓ Asset Browser enabling efficient component reuse
```

**CURSOR RULES FOR THIS PROMPT**:
1. MUST implement complete quality validation system for all assets
2. ALL export formats must be tested and validated for Three.js compatibility
3. MUST implement automated quality checking and reporting
4. Performance optimization MUST be measured and documented at every step

**DETAILED IMPLEMENTATION**:
```
Implement comprehensive quality assurance and export pipeline for Three.js integration:

MANDATORY QUALITY ASSURANCE FEATURES:

1. AUTOMATED QUALITY VALIDATION SYSTEM (COMPLETE IMPLEMENTATION):
   - MUST implement comprehensive geometry validation:
     * Non-manifold geometry detection and automatic repair
     * Triangle count validation against performance budgets
     * UV mapping efficiency measurement and reporting
     * Normal vector validation and automatic correction
     * Scale validation against real-world measurements
   - MUST implement material validation:
     * PBR compliance checking for all materials
     * Texture resolution validation and optimization
     * Node tree validation for export compatibility
     * Color space validation for accurate reproduction
     * Performance impact measurement for each material

2. EXPORT PIPELINE OPTIMIZATION (ALL FORMATS REQUIRED):
   - glTF 2.0 export with full validation:
     * MUST implement automatic material conversion to glTF standard
     * MUST validate all textures are properly packed and optimized
     * MUST ensure coordinate system compatibility with Three.js
     * MUST implement LOD export for performance optimization
     * MUST validate animation data if present
   - Quality preservation during export:
     * MUST maintain material fidelity through export process
     * MUST preserve UV mapping and texture coordinates
     * MUST maintain proper normal vector orientation
     * MUST ensure proper scaling and proportions

3. PERFORMANCE OPTIMIZATION PIPELINE (FULL IMPLEMENTATION):
   - Automatic LOD generation:
     * MUST implement 4-level LOD system (Hero, High, Medium, Low)
     * MUST use Decimate modifier with intelligent settings
     * MUST maintain silhouette quality at all LOD levels
     * MUST implement smooth LOD transitions in Three.js
   - Texture optimization:
     * MUST implement automatic texture resizing for LOD levels
     * MUST use appropriate compression for each texture type
     * MUST implement texture atlasing for small components
     * MUST validate texture quality after compression

COMPLETE IMPLEMENTATION REQUIREMENTS:

Quality Assurance System MUST include:
```python
# Blender 4.4 Quality Assurance Script
import bpy
import bmesh
import mathutils
from mathutils import Vector
import os

class BlenderQualityAssurance:
    """
    Comprehensive quality assurance system for Blender assets
    """
    
    def __init__(self):
        self.validation_results = {}
        self.performance_metrics = {}
        self.export_validation = {}
        
    def run_complete_validation(self):
        """
        Run all validation checks on current scene
        """
        print("Starting comprehensive quality validation...")
        
        # Validate all objects in scene
        for obj in bpy.context.scene.objects:
            if obj.type == 'MESH':
                self.validate_mesh_object(obj)
        
        # Validate materials
        for material in bpy.data.materials:
            self.validate_material(material)
        
        # Validate scene setup
        self.validate_scene_setup()
        
        # Generate validation report
        self.generate_validation_report()
        
        return self.validation_results
    
    def validate_mesh_object(self, obj):
        """
        Comprehensive mesh validation
        """
        validation_data = {
            'name': obj.name,
            'triangle_count': 0,
            'uv_efficiency': 0.0,
            'has_non_manifold': False,
            'scale_validation': True,
            'normal_issues': False,
            'material_count': 0
        }
        
        # Get mesh data
        mesh = obj.data
        
        # Calculate triangle count
        mesh.calc_loop_triangles()
        validation_data['triangle_count'] = len(mesh.loop_triangles)
        
        # Check triangle count against budget
        if 'Hero' in obj.name and validation_data['triangle_count'] > 100000:
            validation_data['triangle_budget_exceeded'] = True
        elif 'Primary' in obj.name and validation_data['triangle_count'] > 50000:
            validation_data['triangle_budget_exceeded'] = True
        elif 'Secondary' in obj.name and validation_data['triangle_count'] > 25000:
            validation_data['triangle_budget_exceeded'] = True
        
        # Validate UV mapping
        if mesh.uv_layers:
            validation_data['uv_efficiency'] = self.calculate_uv_efficiency(mesh)
            if validation_data['uv_efficiency'] < 0.90:
                validation_data['uv_efficiency_low'] = True
        
        # Check for non-manifold geometry
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.mesh.select_non_manifold()
        
        # Count selected vertices (non-manifold)
        bm = bmesh.from_edit_mesh(mesh)
        non_manifold_count = len([v for v in bm.verts if v.select])
        validation_data['has_non_manifold'] = non_manifold_count > 0
        validation_data['non_manifold_count'] = non_manifold_count
        
        bpy.ops.object.mode_set(mode='OBJECT')
        
        # Validate scale
        scale = obj.scale
        if not (0.9 <= scale.x <= 1.1 and 0.9 <= scale.y <= 1.1 and 0.9 <= scale.z <= 1.1):
            validation_data['scale_validation'] = False
        
        # Validate normals
        validation_data['normal_issues'] = self.check_normal_issues(mesh)
        
        # Count materials
        validation_data['material_count'] = len(obj.data.materials)
        
        self.validation_results[obj.name] = validation_data
    
    def validate_material(self, material):
        """
        Comprehensive material validation
        """
        if not material.use_nodes:
            self.validation_results[f"Material_{material.name}"] = {
                'error': 'Material does not use nodes - not PBR compatible'
            }
            return
        
        material_data = {
            'name': material.name,
            'has_principled_bsdf': False,
            'texture_count': 0,
            'texture_resolutions': [],
            'export_compatible': True,
            'performance_score': 0
        }
        
        nodes = material.node_tree.nodes
        
        # Check for Principled BSDF
        principled_nodes = [n for n in nodes if n.type == 'BSDF_PRINCIPLED']
        material_data['has_principled_bsdf'] = len(principled_nodes) > 0
        
        # Count and validate textures
        texture_nodes = [n for n in nodes if n.type == 'TEX_IMAGE']
        material_data['texture_count'] = len(texture_nodes)
        
        for tex_node in texture_nodes:
            if tex_node.image:
                resolution = tex_node.image.size
                material_data['texture_resolutions'].append(resolution)
                
                # Check for oversized textures
                if resolution[0] > 4096 or resolution[1] > 4096:
                    material_data['oversized_textures'] = True
        
        # Calculate performance score
        material_data['performance_score'] = self.calculate_material_performance(material)
        
        self.validation_results[f"Material_{material.name}"] = material_data
    
    def validate_scene_setup(self):
        """
        Validate overall scene configuration
        """
        scene_data = {
            'units_metric': bpy.context.scene.unit_settings.system == 'METRIC',
            'render_engine': bpy.context.scene.render.engine,
            'color_management': bpy.context.scene.view_settings.view_transform,
            'collection_count': len(bpy.data.collections),
            'object_count': len(bpy.context.scene.objects),
            'material_count': len(bpy.data.materials),
            'texture_count': len(bpy.data.images)
        }
        
        # Validate coordinate system
        scene_data['coordinate_system_valid'] = True  # Y-up is Blender default
        
        # Check render settings
        if scene_data['render_engine'] != 'CYCLES':
            scene_data['render_engine_warning'] = 'Cycles recommended for PBR workflow'
        
        # Check color management
        if scene_data['color_management'] != 'sRGB':
            scene_data['color_management_warning'] = 'sRGB recommended for game assets'
        
        self.validation_results['Scene_Setup'] = scene_data
    
    def calculate_uv_efficiency(self, mesh):
        """
        Calculate UV space utilization efficiency
        """
        if not mesh.uv_layers:
            return 0.0
        
        uv_layer = mesh.uv_layers.active.data
        
        # Calculate used UV space (simplified calculation)
        min_u, max_u = float('inf'), float('-inf')
        min_v, max_v = float('inf'), float('-inf')
        
        for uv in uv_layer:
            min_u = min(min_u, uv.uv[0])
            max_u = max(max_u, uv.uv[0])
            min_v = min(min_v, uv.uv[1])
            max_v = max(max_v, uv.uv[1])
        
        used_area = (max_u - min_u) * (max_v - min_v)
        return min(used_area, 1.0)  # Cap at 100%
    
    def check_normal_issues(self, mesh):
        """
        Check for normal vector issues
        """
        # Simplified normal validation
        mesh.calc_normals_split()
        
        # Check for zero-length normals
        for loop in mesh.loops:
            normal = mesh.loops[loop.index].normal
            if normal.length < 0.1:
                return True
        
        return False
    
    def calculate_material_performance(self, material):
        """
        Calculate material performance score
        """
        score = 100
        nodes = material.node_tree.nodes
        
        # Deduct points for complex node setups
        score -= len(nodes) * 2
        
        # Deduct points for multiple texture nodes
        texture_count = len([n for n in nodes if n.type == 'TEX_IMAGE'])
        score -= texture_count * 10
        
        # Deduct points for complex math operations
        math_nodes = len([n for n in nodes if 'MATH' in n.type])
        score -= math_nodes * 5
        
        return max(score, 0)
    
    def generate_validation_report(self):
        """
        Generate comprehensive validation report
        """
        report_path = bpy.path.abspath("//validation_report.txt")
        
        with open(report_path, 'w') as f:
            f.write("BLENDER QUALITY ASSURANCE REPORT\n")
            f.write("=" * 50 + "\n\n")
            
            # Scene summary
            f.write("SCENE SUMMARY:\n")
            if 'Scene_Setup' in self.validation_results:
                scene_data = self.validation_results['Scene_Setup']
                f.write(f"Objects: {scene_data['object_count']}\n")
                f.write(f"Materials: {scene_data['material_count']}\n")
                f.write(f"Textures: {scene_data['texture_count']}\n")
                f.write(f"Render Engine: {scene_data['render_engine']}\n\n")
            
            # Object validation results
            f.write("OBJECT VALIDATION:\n")
            for obj_name, data in self.validation_results.items():
                if obj_name.startswith('Material_') or obj_name == 'Scene_Setup':
                    continue
                
                f.write(f"\n{obj_name}:\n")
                f.write(f"  Triangle Count: {data.get('triangle_count', 'N/A')}\n")
                f.write(f"  UV Efficiency: {data.get('uv_efficiency', 0):.1%}\n")
                f.write(f"  Non-manifold Issues: {data.get('has_non_manifold', False)}\n")
                f.write(f"  Scale Valid: {data.get('scale_validation', True)}\n")
                
                # Highlight issues
                if data.get('triangle_budget_exceeded'):
                    f.write("  ⚠️  Triangle budget exceeded!\n")
                if data.get('uv_efficiency_low'):
                    f.write("  ⚠️  UV efficiency below 90%!\n")
                if data.get('has_non_manifold'):
                    f.write("  ⚠️  Non-manifold geometry detected!\n")
            
            # Material validation results
            f.write("\n\nMATERIAL VALIDATION:\n")
            for mat_name, data in self.validation_results.items():
                if not mat_name.startswith('Material_'):
                    continue
                
                f.write(f"\n{data['name']}:\n")
                f.write(f"  Has Principled BSDF: {data.get('has_principled_bsdf', False)}\n")
                f.write(f"  Texture Count: {data.get('texture_count', 0)}\n")
                f.write(f"  Performance Score: {data.get('performance_score', 0)}\n")
                
                if data.get('oversized_textures'):
                    f.write("  ⚠️  Oversized textures detected!\n")
        
        print(f"Validation report saved to: {report_path}")

# Export Pipeline Implementation
class BlenderExportPipeline:
    """
    Comprehensive export pipeline for Three.js integration
    """
    
    def __init__(self):
        self.export_settings = {
            'gltf': {
                'export_format': 'GLB',
                'export_texcoords': True,
                'export_normals': True,
                'export_materials': 'EXPORT',
                'export_colors': True,
                'export_yup': True
            }
        }
    
    def export_for_threejs(self, export_path, lod_level='hero'):
        """
        Export optimized assets for Three.js
        """
        # Prepare scene for export
        self.prepare_scene_for_export(lod_level)
        
        # Export glTF
        gltf_path = os.path.join(export_path, f"cockpit_{lod_level}.glb")
        bpy.ops.export_scene.gltf(**self.export_settings['gltf'], filepath=gltf_path)
        
        # Validate export
        self.validate_export(gltf_path)
        
        return gltf_path
    
    def prepare_scene_for_export(self, lod_level):
        """
        Prepare scene for specific LOD export
        """
        # Hide objects not needed for this LOD level
        for obj in bpy.context.scene.objects:
            if lod_level == 'low' and 'Hero' in obj.name:
                obj.hide_set(True)
            elif lod_level == 'medium' and ('Hero' in obj.name or 'Detail' in obj.name):
                obj.hide_set(True)
        
        # Apply modifiers for export
        for obj in bpy.context.scene.objects:
            if obj.type == 'MESH' and not obj.hide_get():
                bpy.context.view_layer.objects.active = obj
                for modifier in obj.modifiers:
                    if modifier.type in ['SUBSURF', 'MULTIRES']:
                        # Reduce subdivision for lower LOD
                        if lod_level == 'low':
                            modifier.levels = 0
                        elif lod_level == 'medium':
                            modifier.levels = 1
    
    def validate_export(self, export_path):
        """
        Validate exported file
        """
        if os.path.exists(export_path):
            file_size = os.path.getsize(export_path) / (1024 * 1024)  # MB
            print(f"Export successful: {export_path}")
            print(f"File size: {file_size:.2f} MB")
            
            # Check file size limits
            if file_size > 100:  # 100MB limit
                print("⚠️  Warning: Export file size exceeds 100MB")
        else:
            print(f"❌ Export failed: {export_path}")

# Usage example
def run_quality_assurance():
    """
    Run complete quality assurance pipeline
    """
    qa = BlenderQualityAssurance()
    results = qa.run_complete_validation()
    
    exporter = BlenderExportPipeline()
    export_path = bpy.path.abspath("//exports/")
    
    # Export all LOD levels
    for lod in ['hero', 'high', 'medium', 'low']:
        exporter.export_for_threejs(export_path, lod)
    
    return results

# Execute quality assurance
if __name__ == "__main__":
    run_quality_assurance()
```

VALIDATION REQUIREMENTS:
CURSOR MUST verify after implementation:
✓ Quality assurance system detects all common issues
✓ Export pipeline produces valid glTF files for all LOD levels
✓ Material fidelity is maintained through export process
✓ Performance metrics are within acceptable ranges
✓ Automated reporting provides actionable feedback
✓ Three.js compatibility is verified for all exports
✓ File sizes are optimized for web delivery
✓ All validation errors are automatically flagged

PERFORMANCE BENCHMARKS (MUST ACHIEVE):
✓ Quality validation: <60 seconds for complete scene
✓ Export process: <120 seconds per LOD level
✓ File size optimization: <50MB for hero assets
✓ Material conversion: 100% fidelity preservation
✓ UV mapping validation: >95% efficiency detection
✓ Geometry validation: 100% non-manifold detection
```

**GAP IDENTIFICATION FOR PHASE 1.3**:
```
CURSOR MUST CHECK FOR THESE CRITICAL GAPS:
❌ Missing quality validation causing undetected issues
❌ Incomplete export pipeline preventing Three.js integration
❌ Poor performance optimization limiting real-time usage
❌ Missing automated reporting reducing workflow efficiency
❌ Inadequate LOD system causing performance problems
❌ Export compatibility issues preventing proper Three.js loading
❌ Missing file size optimization causing slow loading times
❌ Incomplete material validation allowing PBR compliance issues
```

## PHASE 1 COMPLETION CHECKLIST

### ✅ **BLENDER 4.4 VALIDATION REQUIREMENTS**
- [ ] Complete project structure with all collections organized
- [ ] Material library renders photorealistically in Cycles
- [ ] Advanced asset pipeline produces hero-quality components
- [ ] Geometry Nodes systems enhance detail without performance impact
- [ ] UV mapping achieves >90% efficiency across all assets
- [ ] Quality assurance system detects and reports all issues
- [ ] Export pipeline produces valid glTF files for Three.js
- [ ] Performance metrics meet all specified benchmarks

### ✅ **QUALITY GATES**
- [ ] Cycles rendering produces photorealistic results indistinguishable from references
- [ ] Material preview shows accurate PBR behavior in all lighting conditions
- [ ] Asset Browser enables efficient component reuse and organization
- [ ] Geometry validation passes with zero critical issues
- [ ] Export compatibility verified in Three.js environment
- [ ] Performance optimization maintains smooth workflow
- [ ] Automated reporting provides comprehensive quality feedback

### ✅ **PERFORMANCE BENCHMARKS**
- [ ] Viewport performance: >30 FPS in Material Preview mode
- [ ] Geometry Nodes evaluation: <100ms per component
- [ ] Quality validation: <60 seconds for complete scene
- [ ] Export process: <120 seconds per LOD level
- [ ] Memory usage: <4GB for complete scene with all assets
- [ ] File size optimization: <50MB for hero assets
- [ ] UV mapping efficiency: >90% for all components

**PHASE 1 MUST BE 100% COMPLETE BEFORE PROCEEDING TO PHASE 2**

---

*This document serves as the definitive guide for Blender Phase 1 development in the Fighter Jet Cockpit project. All Blender work must follow these processes and meet these standards to achieve the target photorealistic quality and Three.js compatibility.*
