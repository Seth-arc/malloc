"""
COMPATIBLE - Realistic Fighter Jet Cockpit Creation Script for Blender
This script works with all Blender versions (2.8+) and creates a realistic cockpit.

Run this in Blender's Text Editor or Console.
"""

import bpy
import bmesh
import mathutils
import math
from mathutils import Vector

def clear_scene():
    """Clear all objects from the scene"""
    print("🧹 Clearing scene...")
    
    # Deselect all
    bpy.ops.object.select_all(action='DESELECT')
    
    # Select all objects
    for obj in bpy.context.scene.objects:
        if obj.type in ['MESH', 'LIGHT', 'CAMERA']:
            obj.select_set(True)
    
    # Delete selected objects
    bpy.ops.object.delete(use_global=False)
    
    # Clear materials (compatible way)
    for material in list(bpy.data.materials):
        if material.users == 0:
            bpy.data.materials.remove(material)
    
    print("✅ Scene cleared")

def clear_material_nodes(material):
    """Clear material nodes in a compatible way"""
    if material.use_nodes:
        # Remove all nodes except output
        nodes_to_remove = []
        for node in material.node_tree.nodes:
            if node.type != 'OUTPUT_MATERIAL':
                nodes_to_remove.append(node)
        
        for node in nodes_to_remove:
            material.node_tree.nodes.remove(node)

def create_realistic_materials():
    """Create realistic military-grade PBR materials"""
    print("🎨 Creating realistic PBR materials...")
    materials = {}
    
    # 1. Military Aluminum Frame Material
    aluminum = bpy.data.materials.new(name="Military_Aluminum")
    aluminum.use_nodes = True
    clear_material_nodes(aluminum)
    
    # Aluminum nodes
    bsdf = aluminum.node_tree.nodes.new(type='ShaderNodeBsdfPrincipled')
    output = aluminum.node_tree.nodes.new(type='ShaderNodeOutputMaterial')
    
    # Position nodes
    bsdf.location = (0, 0)
    output.location = (300, 0)
    
    # Aluminum properties
    bsdf.inputs['Base Color'].default_value = (0.42, 0.45, 0.5, 1.0)  # Military gray
    bsdf.inputs['Metallic'].default_value = 0.95
    bsdf.inputs['Roughness'].default_value = 0.2
    
    # Check if Specular input exists (Blender version compatibility)
    if 'Specular' in bsdf.inputs:
        bsdf.inputs['Specular'].default_value = 1.0
    
    aluminum.node_tree.links.new(bsdf.outputs['BSDF'], output.inputs['Surface'])
    materials['aluminum'] = aluminum
    
    # 2. Carbon Fiber Material
    carbon = bpy.data.materials.new(name="Carbon_Fiber")
    carbon.use_nodes = True
    clear_material_nodes(carbon)
    
    bsdf = carbon.node_tree.nodes.new(type='ShaderNodeBsdfPrincipled')
    output = carbon.node_tree.nodes.new(type='ShaderNodeOutputMaterial')
    
    bsdf.location = (0, 0)
    output.location = (300, 0)
    
    # Carbon fiber properties
    bsdf.inputs['Base Color'].default_value = (0.05, 0.05, 0.05, 1.0)  # Dark carbon
    bsdf.inputs['Metallic'].default_value = 0.1
    bsdf.inputs['Roughness'].default_value = 0.3
    
    if 'Specular' in bsdf.inputs:
        bsdf.inputs['Specular'].default_value = 0.8
    
    carbon.node_tree.links.new(bsdf.outputs['BSDF'], output.inputs['Surface'])
    materials['carbon'] = carbon
    
    # 3. Leather Seat Material
    leather = bpy.data.materials.new(name="Military_Leather")
    leather.use_nodes = True
    clear_material_nodes(leather)
    
    bsdf = leather.node_tree.nodes.new(type='ShaderNodeBsdfPrincipled')
    output = leather.node_tree.nodes.new(type='ShaderNodeOutputMaterial')
    
    bsdf.location = (0, 0)
    output.location = (300, 0)
    
    # Leather properties
    bsdf.inputs['Base Color'].default_value = (0.15, 0.1, 0.08, 1.0)  # Dark brown
    bsdf.inputs['Metallic'].default_value = 0.0
    bsdf.inputs['Roughness'].default_value = 0.8
    
    if 'Specular' in bsdf.inputs:
        bsdf.inputs['Specular'].default_value = 0.3
    
    leather.node_tree.links.new(bsdf.outputs['BSDF'], output.inputs['Surface'])
    materials['leather'] = leather
    
    # 4. Display Screen Material (Emissive)
    display = bpy.data.materials.new(name="Display_Screen")
    display.use_nodes = True
    clear_material_nodes(display)
    
    bsdf = display.node_tree.nodes.new(type='ShaderNodeBsdfPrincipled')
    output = display.node_tree.nodes.new(type='ShaderNodeOutputMaterial')
    
    bsdf.location = (0, 0)
    output.location = (300, 0)
    
    # Display properties
    bsdf.inputs['Base Color'].default_value = (0.0, 1.0, 0.2, 1.0)  # Green
    
    # Check for Emission input (version compatibility)
    if 'Emission' in bsdf.inputs:
        bsdf.inputs['Emission'].default_value = (0.0, 1.0, 0.2, 1.0)
        if 'Emission Strength' in bsdf.inputs:
            bsdf.inputs['Emission Strength'].default_value = 2.0
    
    bsdf.inputs['Roughness'].default_value = 0.1
    
    display.node_tree.links.new(bsdf.outputs['BSDF'], output.inputs['Surface'])
    materials['display'] = display
    
    # 5. Glass Canopy Material
    glass = bpy.data.materials.new(name="Canopy_Glass")
    glass.use_nodes = True
    clear_material_nodes(glass)
    
    bsdf = glass.node_tree.nodes.new(type='ShaderNodeBsdfPrincipled')
    output = glass.node_tree.nodes.new(type='ShaderNodeOutputMaterial')
    
    bsdf.location = (0, 0)
    output.location = (300, 0)
    
    # Glass properties
    bsdf.inputs['Base Color'].default_value = (0.95, 0.98, 1.0, 1.0)  # Slight blue tint
    bsdf.inputs['Metallic'].default_value = 0.0
    bsdf.inputs['Roughness'].default_value = 0.0
    
    # Check for Transmission input (version compatibility)
    if 'Transmission' in bsdf.inputs:
        bsdf.inputs['Transmission'].default_value = 0.95
    
    if 'IOR' in bsdf.inputs:
        bsdf.inputs['IOR'].default_value = 1.45
    
    if 'Alpha' in bsdf.inputs:
        bsdf.inputs['Alpha'].default_value = 0.1
        glass.blend_method = 'BLEND'
    
    glass.node_tree.links.new(bsdf.outputs['BSDF'], output.inputs['Surface'])
    materials['glass'] = glass
    
    # 6. Rubber/Plastic Material
    rubber = bpy.data.materials.new(name="Rubber_Grip")
    rubber.use_nodes = True
    clear_material_nodes(rubber)
    
    bsdf = rubber.node_tree.nodes.new(type='ShaderNodeBsdfPrincipled')
    output = rubber.node_tree.nodes.new(type='ShaderNodeOutputMaterial')
    
    bsdf.location = (0, 0)
    output.location = (300, 0)
    
    # Rubber properties
    bsdf.inputs['Base Color'].default_value = (0.1, 0.1, 0.1, 1.0)  # Dark rubber
    bsdf.inputs['Metallic'].default_value = 0.0
    bsdf.inputs['Roughness'].default_value = 0.9
    
    if 'Specular' in bsdf.inputs:
        bsdf.inputs['Specular'].default_value = 0.1
    
    rubber.node_tree.links.new(bsdf.outputs['BSDF'], output.inputs['Surface'])
    materials['rubber'] = rubber
    
    print("✅ Created 6 realistic PBR materials")
    return materials

def create_cockpit_frame(materials):
    """Create a detailed cockpit frame"""
    print("🏗️ Creating cockpit frame...")
    
    # Main cockpit frame - create as separate pieces for hollow effect
    frame_pieces = []
    
    # Bottom frame
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0.5, 0.3))
    bottom_frame = bpy.context.active_object
    bottom_frame.name = "Cockpit_Frame_Bottom"
    bottom_frame.scale = (1.2, 2.0, 0.05)
    bottom_frame.data.materials.append(materials['aluminum'])
    frame_pieces.append(bottom_frame)
    
    # Left frame
    bpy.ops.mesh.primitive_cube_add(size=1, location=(-0.6, 0.5, 0.8))
    left_frame = bpy.context.active_object
    left_frame.name = "Cockpit_Frame_Left"
    left_frame.scale = (0.05, 2.0, 1.0)
    left_frame.data.materials.append(materials['aluminum'])
    frame_pieces.append(left_frame)
    
    # Right frame
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0.6, 0.5, 0.8))
    right_frame = bpy.context.active_object
    right_frame.name = "Cockpit_Frame_Right"
    right_frame.scale = (0.05, 2.0, 1.0)
    right_frame.data.materials.append(materials['aluminum'])
    frame_pieces.append(right_frame)
    
    # Add bevel modifiers to all frame pieces
    for piece in frame_pieces:
        bevel_mod = piece.modifiers.new(name="Bevel", type='BEVEL')
        bevel_mod.width = 0.01
        bevel_mod.segments = 2
    
    return frame_pieces[0]  # Return main piece

def create_ejection_seat(materials):
    """Create a detailed ejection seat"""
    print("🪑 Creating ejection seat...")
    
    # Seat base
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0.3, 0.4))
    seat_base = bpy.context.active_object
    seat_base.name = "Ejection_Seat_Base"
    seat_base.scale = (0.5, 0.6, 0.1)
    
    # Add bevel for rounded edges
    bevel_mod = seat_base.modifiers.new(name="Bevel", type='BEVEL')
    bevel_mod.width = 0.02
    bevel_mod.segments = 2
    
    # Seat back
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0.0, 0.7))
    seat_back = bpy.context.active_object
    seat_back.name = "Ejection_Seat_Back"
    seat_back.scale = (0.5, 0.1, 0.4)
    seat_back.rotation_euler = (math.radians(-10), 0, 0)
    
    # Add bevel
    bevel_mod = seat_back.modifiers.new(name="Bevel", type='BEVEL')
    bevel_mod.width = 0.02
    bevel_mod.segments = 2
    
    # Headrest
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, -0.05, 1.0))
    headrest = bpy.context.active_object
    headrest.name = "Ejection_Seat_Headrest"
    headrest.scale = (0.3, 0.1, 0.15)
    
    # Apply leather to seat parts
    seat_base.data.materials.append(materials['leather'])
    seat_back.data.materials.append(materials['leather'])
    headrest.data.materials.append(materials['leather'])
    
    return seat_base

def create_control_stick(materials):
    """Create a detailed control stick"""
    print("🕹️ Creating control stick...")
    
    # Main shaft
    bpy.ops.mesh.primitive_cylinder_add(radius=0.02, depth=0.4, location=(0.15, 0.45, 0.65))
    stick_shaft = bpy.context.active_object
    stick_shaft.name = "Control_Stick_Shaft"
    stick_shaft.data.materials.append(materials['aluminum'])
    
    # Grip handle
    bpy.ops.mesh.primitive_cylinder_add(radius=0.03, depth=0.12, location=(0.15, 0.45, 0.85))
    grip = bpy.context.active_object
    grip.name = "Control_Stick_Grip"
    grip.data.materials.append(materials['rubber'])
    
    # Trigger button
    bpy.ops.mesh.primitive_cube_add(size=0.02, location=(0.17, 0.45, 0.82))
    trigger = bpy.context.active_object
    trigger.name = "Control_Stick_Trigger"
    trigger.data.materials.append(materials['rubber'])
    
    return stick_shaft

def create_instrument_panel(materials):
    """Create detailed instrument panel"""
    print("📱 Creating instrument panel...")
    
    # Main panel base
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 1.0, 0.95))
    panel_base = bpy.context.active_object
    panel_base.name = "Instrument_Panel_Base"
    panel_base.scale = (1.0, 0.15, 0.4)
    panel_base.rotation_euler = (math.radians(-15), 0, 0)
    
    # Add bevel for smooth edges
    bevel_mod = panel_base.modifiers.new(name="Bevel", type='BEVEL')
    bevel_mod.width = 0.01
    bevel_mod.segments = 2
    
    panel_base.data.materials.append(materials['carbon'])
    
    # MFD (Multi Function Display) - Left
    bpy.ops.mesh.primitive_cube_add(size=1, location=(-0.3, 1.08, 0.98))
    mfd_left = bpy.context.active_object
    mfd_left.name = "MFD_Left"
    mfd_left.scale = (0.25, 0.02, 0.2)
    mfd_left.rotation_euler = (math.radians(-15), 0, 0)
    mfd_left.data.materials.append(materials['display'])
    
    # MFD (Multi Function Display) - Right
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0.3, 1.08, 0.98))
    mfd_right = bpy.context.active_object
    mfd_right.name = "MFD_Right"
    mfd_right.scale = (0.25, 0.02, 0.2)
    mfd_right.rotation_euler = (math.radians(-15), 0, 0)
    mfd_right.data.materials.append(materials['display'])
    
    return panel_base

def create_throttle_quadrant(materials):
    """Create detailed throttle quadrant"""
    print("🎚️ Creating throttle quadrant...")
    
    # Throttle base
    bpy.ops.mesh.primitive_cube_add(size=1, location=(-0.4, 0.3, 0.6))
    throttle_base = bpy.context.active_object
    throttle_base.name = "Throttle_Base"
    throttle_base.scale = (0.15, 0.3, 0.25)
    throttle_base.data.materials.append(materials['carbon'])
    
    # Main throttle lever
    bpy.ops.mesh.primitive_cube_add(size=1, location=(-0.4, 0.45, 0.75))
    throttle_lever = bpy.context.active_object
    throttle_lever.name = "Throttle_Lever"
    throttle_lever.scale = (0.04, 0.15, 0.02)
    throttle_lever.rotation_euler = (math.radians(-20), 0, 0)
    throttle_lever.data.materials.append(materials['aluminum'])
    
    # Throttle grip
    bpy.ops.mesh.primitive_cube_add(size=1, location=(-0.4, 0.52, 0.8))
    throttle_grip = bpy.context.active_object
    throttle_grip.name = "Throttle_Grip"
    throttle_grip.scale = (0.06, 0.08, 0.04)
    throttle_grip.rotation_euler = (math.radians(-20), 0, 0)
    throttle_grip.data.materials.append(materials['rubber'])
    
    return throttle_base

def create_switch_panels(materials):
    """Create detailed switch panels"""
    print("🔘 Creating switch panels...")
    
    # Left console switches (simplified for compatibility)
    for row in range(3):
        for col in range(3):
            x = -0.5 + col * 0.04
            y = 0.85
            z = 0.8 + row * 0.05
            
            # Switch base
            bpy.ops.mesh.primitive_cylinder_add(radius=0.012, depth=0.02, location=(x, y, z))
            switch_base = bpy.context.active_object
            switch_base.name = f"Switch_Base_{row}_{col}"
            switch_base.rotation_euler = (math.radians(90), 0, 0)
            switch_base.data.materials.append(materials['aluminum'])
            
            # Switch cap (colored)
            bpy.ops.mesh.primitive_sphere_add(radius=0.008, location=(x, y + 0.015, z))
            switch_cap = bpy.context.active_object
            switch_cap.name = f"Switch_Cap_{row}_{col}"
            
            # Create simple colored material for switch cap
            switch_mat = bpy.data.materials.new(name=f"Switch_Material_{row}_{col}")
            switch_mat.use_nodes = True
            
            # Get the default principled BSDF (should exist by default)
            if switch_mat.node_tree.nodes:
                bsdf = None
                for node in switch_mat.node_tree.nodes:
                    if node.type == 'BSDF_PRINCIPLED':
                        bsdf = node
                        break
                
                if bsdf:
                    switch_color = (1.0, 0.0, 0.0, 1.0) if row % 2 == 0 else (0.0, 1.0, 0.0, 1.0)
                    bsdf.inputs['Base Color'].default_value = switch_color
                    
                    # Try to set emission if available
                    if 'Emission' in bsdf.inputs:
                        bsdf.inputs['Emission'].default_value = switch_color
                        if 'Emission Strength' in bsdf.inputs:
                            bsdf.inputs['Emission Strength'].default_value = 0.5
            
            switch_cap.data.materials.append(switch_mat)

def create_canopy_glass(materials):
    """Create realistic canopy glass"""
    print("🪟 Creating canopy glass...")
    
    # Main canopy - simplified for compatibility
    bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=(0, 0.5, 1.2))
    canopy = bpy.context.active_object
    canopy.name = "Canopy_Glass"
    canopy.scale = (0.8, 1.2, 0.6)
    
    # Edit to create proper canopy shape
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.bisect(plane_co=(0, 0, 1), plane_no=(0, 0, -1), clear_inner=True)
    bpy.ops.object.mode_set(mode='OBJECT')
    
    canopy.data.materials.append(materials['glass'])
    
    return canopy

def setup_lighting():
    """Setup realistic cockpit lighting"""
    print("💡 Setting up realistic lighting...")
    
    # Remove default light if it exists
    if "Light" in bpy.data.objects:
        bpy.data.objects.remove(bpy.data.objects["Light"], do_unlink=True)
    
    # Sun light (external)
    bpy.ops.object.light_add(type='SUN', location=(5, 5, 10))
    sun = bpy.context.active_object
    sun.name = "Sun_Light"
    sun.data.energy = 5.0
    sun.data.color = (1.0, 0.95, 0.8)
    sun.rotation_euler = (math.radians(45), math.radians(45), 0)
    
    # Cockpit interior lighting
    bpy.ops.object.light_add(type='POINT', location=(0, 0.8, 1.0))
    panel_light = bpy.context.active_object
    panel_light.name = "Panel_Light"
    panel_light.data.energy = 50.0
    panel_light.data.color = (1.0, 0.2, 0.2)  # Red instrument lighting
    
    # Side console lights
    bpy.ops.object.light_add(type='POINT', location=(-0.4, 0.6, 0.8))
    left_light = bpy.context.active_object
    left_light.name = "Left_Console_Light"
    left_light.data.energy = 25.0
    left_light.data.color = (0.2, 0.4, 1.0)  # Blue console lighting
    
    bpy.ops.object.light_add(type='POINT', location=(0.4, 0.6, 0.8))
    right_light = bpy.context.active_object
    right_light.name = "Right_Console_Light"
    right_light.data.energy = 25.0
    right_light.data.color = (0.2, 0.4, 1.0)  # Blue console lighting

def setup_camera():
    """Setup camera for pilot's view"""
    print("📸 Setting up pilot's view camera...")
    
    # Remove default camera if it exists
    if "Camera" in bpy.data.objects:
        bpy.data.objects.remove(bpy.data.objects["Camera"], do_unlink=True)
    
    # Add camera at pilot's eye level
    bpy.ops.object.camera_add(location=(0, 0.3, 0.9))
    camera = bpy.context.active_object
    camera.name = "Pilot_Camera"
    camera.rotation_euler = (math.radians(90), 0, math.radians(180))
    
    # Set camera as active
    bpy.context.scene.camera = camera
    
    # Camera settings
    camera.data.lens = 35  # Wide angle for cockpit view
    camera.data.clip_start = 0.01
    camera.data.clip_end = 1000

def setup_render_settings():
    """Setup render settings for best quality"""
    print("🎬 Setting up render settings...")
    
    # Use Cycles if available, otherwise Eevee
    if 'CYCLES' in [engine[0] for engine in bpy.types.RenderEngine.bl_rna.properties['bl_idname'].enum_items]:
        bpy.context.scene.render.engine = 'CYCLES'
        if hasattr(bpy.context.scene, 'cycles'):
            bpy.context.scene.cycles.samples = 64
            if hasattr(bpy.context.scene.cycles, 'use_denoising'):
                bpy.context.scene.cycles.use_denoising = True
    else:
        bpy.context.scene.render.engine = 'BLENDER_EEVEE'
    
    # Resolution
    bpy.context.scene.render.resolution_x = 1920
    bpy.context.scene.render.resolution_y = 1080
    bpy.context.scene.render.resolution_percentage = 100

def main():
    """Main function to create the realistic cockpit"""
    print("🚀 Starting realistic fighter jet cockpit creation...")
    
    # Clear scene
    clear_scene()
    
    # Create materials
    materials = create_realistic_materials()
    
    # Create cockpit components
    create_cockpit_frame(materials)
    create_ejection_seat(materials)
    create_control_stick(materials)
    create_instrument_panel(materials)
    create_throttle_quadrant(materials)
    create_switch_panels(materials)
    create_canopy_glass(materials)
    
    # Setup scene
    setup_lighting()
    setup_camera()
    setup_render_settings()
    
    print("✅ Realistic fighter jet cockpit creation completed!")
    print("🎮 Switch to Camera view (Numpad 0) to see pilot's perspective")
    print("🎨 Switch viewport to 'Material Preview' or 'Rendered' to see materials")
    print("🎬 Press F12 to render the final image")
    
    # Try to export as GLB
    export_path = "C:/Users/ssnguna/Local Sites/malloc/experiments/environments/fighter_jet/docs/blender work/exports_assembled/realistic_fighter_cockpit.glb"
    
    try:
        # Select all mesh objects for export
        bpy.ops.object.select_all(action='DESELECT')
        for obj in bpy.context.scene.objects:
            if obj.type == 'MESH':
                obj.select_set(True)
        
        # Export as GLB (with error handling for different Blender versions)
        if hasattr(bpy.ops.export_scene, 'gltf'):
            bpy.ops.export_scene.gltf(
                filepath=export_path,
                use_selection=True,
                export_format='GLB',
                export_materials='EXPORT',
                export_apply=False
            )
            print(f"✅ Exported realistic cockpit to: {export_path}")
        else:
            print("⚠️ GLB export not available in this Blender version")
            print("💡 You can manually export: File → Export → glTF 2.0")
        
    except Exception as e:
        print(f"⚠️ Export issue: {str(e)}")
        print("💡 You can manually export: File → Export → glTF 2.0")

if __name__ == "__main__":
    main()
