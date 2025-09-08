"""
Realistic Fighter Jet Cockpit Creation Script for Blender
This script creates a highly detailed and realistic F-16/F-18 style fighter jet cockpit
with proper geometry, materials, and textures.

Run this in Blender's Text Editor or Console.
"""

import bpy
import bmesh
import mathutils
import math
from mathutils import Vector

def clear_scene():
    """Clear all objects from the scene"""
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    
    # Clear materials
    for material in bpy.data.materials:
        bpy.data.materials.remove(material)

def create_realistic_materials():
    """Create realistic military-grade PBR materials"""
    materials = {}
    
    # 1. Aluminum Frame Material
    aluminum = bpy.data.materials.new(name="Military_Aluminum")
    aluminum.use_nodes = True
    aluminum.node_tree.clear()
    
    # Aluminum nodes
    bsdf = aluminum.node_tree.nodes.new(type='ShaderNodeBsdfPrincipled')
    output = aluminum.node_tree.nodes.new(type='ShaderNodeOutputMaterial')
    
    # Aluminum properties
    bsdf.inputs['Base Color'].default_value = (0.42, 0.45, 0.5, 1.0)  # Military gray
    bsdf.inputs['Metallic'].default_value = 0.95
    bsdf.inputs['Roughness'].default_value = 0.2
    bsdf.inputs['Specular'].default_value = 1.0
    
    aluminum.node_tree.links.new(bsdf.outputs['BSDF'], output.inputs['Surface'])
    materials['aluminum'] = aluminum
    
    # 2. Carbon Fiber Material
    carbon = bpy.data.materials.new(name="Carbon_Fiber")
    carbon.use_nodes = True
    carbon.node_tree.clear()
    
    bsdf = carbon.node_tree.nodes.new(type='ShaderNodeBsdfPrincipled')
    output = carbon.node_tree.nodes.new(type='ShaderNodeOutputMaterial')
    noise = carbon.node_tree.nodes.new(type='ShaderNodeTexNoise')
    
    # Carbon fiber properties
    bsdf.inputs['Base Color'].default_value = (0.05, 0.05, 0.05, 1.0)  # Dark carbon
    bsdf.inputs['Metallic'].default_value = 0.1
    bsdf.inputs['Roughness'].default_value = 0.3
    bsdf.inputs['Specular'].default_value = 0.8
    
    # Add noise for carbon weave
    noise.inputs['Scale'].default_value = 50.0
    carbon.node_tree.links.new(noise.outputs['Fac'], bsdf.inputs['Roughness'])
    carbon.node_tree.links.new(bsdf.outputs['BSDF'], output.inputs['Surface'])
    materials['carbon'] = carbon
    
    # 3. Leather Seat Material
    leather = bpy.data.materials.new(name="Military_Leather")
    leather.use_nodes = True
    leather.node_tree.clear()
    
    bsdf = leather.node_tree.nodes.new(type='ShaderNodeBsdfPrincipled')
    output = leather.node_tree.nodes.new(type='ShaderNodeOutputMaterial')
    
    # Leather properties
    bsdf.inputs['Base Color'].default_value = (0.15, 0.1, 0.08, 1.0)  # Dark brown
    bsdf.inputs['Metallic'].default_value = 0.0
    bsdf.inputs['Roughness'].default_value = 0.8
    bsdf.inputs['Specular'].default_value = 0.3
    
    leather.node_tree.links.new(bsdf.outputs['BSDF'], output.inputs['Surface'])
    materials['leather'] = leather
    
    # 4. Display Screen Material (Emissive)
    display = bpy.data.materials.new(name="Display_Screen")
    display.use_nodes = True
    display.node_tree.clear()
    
    bsdf = display.node_tree.nodes.new(type='ShaderNodeBsdfPrincipled')
    emission = display.node_tree.nodes.new(type='ShaderNodeEmission')
    output = display.node_tree.nodes.new(type='ShaderNodeOutputMaterial')
    mix = display.node_tree.nodes.new(type='ShaderNodeMixShader')
    
    # Display properties
    bsdf.inputs['Base Color'].default_value = (0.0, 0.0, 0.0, 1.0)  # Black base
    bsdf.inputs['Roughness'].default_value = 0.1
    emission.inputs['Color'].default_value = (0.0, 1.0, 0.2, 1.0)  # Green glow
    emission.inputs['Strength'].default_value = 2.0
    
    display.node_tree.links.new(bsdf.outputs['BSDF'], mix.inputs[1])
    display.node_tree.links.new(emission.outputs['Emission'], mix.inputs[2])
    mix.inputs['Fac'].default_value = 0.7
    display.node_tree.links.new(mix.outputs['Shader'], output.inputs['Surface'])
    materials['display'] = display
    
    # 5. Glass Canopy Material
    glass = bpy.data.materials.new(name="Canopy_Glass")
    glass.use_nodes = True
    glass.node_tree.clear()
    
    bsdf = glass.node_tree.nodes.new(type='ShaderNodeBsdfPrincipled')
    output = glass.node_tree.nodes.new(type='ShaderNodeOutputMaterial')
    
    # Glass properties
    bsdf.inputs['Base Color'].default_value = (0.95, 0.98, 1.0, 1.0)  # Slight blue tint
    bsdf.inputs['Metallic'].default_value = 0.0
    bsdf.inputs['Roughness'].default_value = 0.0
    bsdf.inputs['Transmission'].default_value = 0.95
    bsdf.inputs['IOR'].default_value = 1.45
    bsdf.inputs['Alpha'].default_value = 0.1
    
    glass.blend_method = 'BLEND'
    glass.node_tree.links.new(bsdf.outputs['BSDF'], output.inputs['Surface'])
    materials['glass'] = glass
    
    # 6. Rubber/Plastic Material
    rubber = bpy.data.materials.new(name="Rubber_Grip")
    rubber.use_nodes = True
    rubber.node_tree.clear()
    
    bsdf = rubber.node_tree.nodes.new(type='ShaderNodeBsdfPrincipled')
    output = rubber.node_tree.nodes.new(type='ShaderNodeOutputMaterial')
    
    # Rubber properties
    bsdf.inputs['Base Color'].default_value = (0.1, 0.1, 0.1, 1.0)  # Dark rubber
    bsdf.inputs['Metallic'].default_value = 0.0
    bsdf.inputs['Roughness'].default_value = 0.9
    bsdf.inputs['Specular'].default_value = 0.1
    
    rubber.node_tree.links.new(bsdf.outputs['BSDF'], output.inputs['Surface'])
    materials['rubber'] = rubber
    
    print("✅ Created 6 realistic PBR materials")
    return materials

def create_detailed_cockpit_frame(materials):
    """Create a detailed cockpit frame with proper geometry"""
    print("🏗️ Creating detailed cockpit frame...")
    
    # Create frame using curve and solidify for realistic thickness
    bpy.ops.curve.primitive_bezier_curve_add()
    frame_curve = bpy.context.active_object
    frame_curve.name = "Cockpit_Frame_Curve"
    
    # Edit the curve to create cockpit shape
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.curve.select_all(action='SELECT')
    bpy.ops.curve.delete(type='VERT')
    
    # Create cockpit frame outline points
    frame_points = [
        (-0.6, 0.0, 0.0),   # Left bottom
        (-0.6, 0.0, 1.2),   # Left top
        (-0.3, 0.0, 1.5),   # Left canopy
        (0.0, 0.0, 1.6),    # Top center
        (0.3, 0.0, 1.5),    # Right canopy
        (0.6, 0.0, 1.2),    # Right top
        (0.6, 0.0, 0.0),    # Right bottom
        (-0.6, 0.0, 0.0)    # Close loop
    ]
    
    # Add curve points
    for i, point in enumerate(frame_points):
        if i == 0:
            bpy.ops.curve.primitive_bezier_curve_add(location=point)
        else:
            bpy.ops.curve.extrude_move(CURVE_OT_extrude={"mode":'TRANSLATION'}, 
                                     TRANSFORM_OT_translate={"value": (point[0]-frame_points[i-1][0], 
                                                                     point[1]-frame_points[i-1][1], 
                                                                     point[2]-frame_points[i-1][2])})
    
    bpy.ops.object.mode_set(mode='OBJECT')
    
    # Convert to mesh and add solidify
    bpy.ops.object.convert(target='MESH')
    bpy.ops.object.modifier_add(type='SOLIDIFY')
    frame_curve.modifiers["Solidify"].thickness = 0.05
    
    # Apply material
    frame_curve.data.materials.append(materials['aluminum'])
    
    return frame_curve

def create_ejection_seat(materials):
    """Create a detailed ejection seat"""
    print("🪑 Creating detailed ejection seat...")
    
    # Seat base
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0.3, 0.4))
    seat_base = bpy.context.active_object
    seat_base.name = "Ejection_Seat_Base"
    seat_base.scale = (0.5, 0.6, 0.1)
    
    # Add bevel for rounded edges
    bpy.ops.object.modifier_add(type='BEVEL')
    seat_base.modifiers["Bevel"].width = 0.02
    seat_base.modifiers["Bevel"].segments = 3
    
    # Seat back
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0.0, 0.7))
    seat_back = bpy.context.active_object
    seat_back.name = "Ejection_Seat_Back"
    seat_back.scale = (0.5, 0.1, 0.4)
    seat_back.rotation_euler = (math.radians(-10), 0, 0)
    
    # Add bevel
    bpy.ops.object.modifier_add(type='BEVEL')
    seat_back.modifiers["Bevel"].width = 0.02
    seat_back.modifiers["Bevel"].segments = 3
    
    # Headrest
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, -0.05, 1.0))
    headrest = bpy.context.active_object
    headrest.name = "Ejection_Seat_Headrest"
    headrest.scale = (0.3, 0.1, 0.15)
    
    # Seat frame (aluminum)
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0.3, 0.35))
    seat_frame = bpy.context.active_object
    seat_frame.name = "Ejection_Seat_Frame"
    seat_frame.scale = (0.52, 0.62, 0.05)
    seat_frame.data.materials.append(materials['aluminum'])
    
    # Apply leather to seat parts
    seat_base.data.materials.append(materials['leather'])
    seat_back.data.materials.append(materials['leather'])
    headrest.data.materials.append(materials['leather'])
    
    # Join seat parts
    bpy.ops.object.select_all(action='DESELECT')
    seat_base.select_set(True)
    seat_back.select_set(True)
    headrest.select_set(True)
    bpy.context.view_layer.objects.active = seat_base
    bpy.ops.object.join()
    
    return seat_base

def create_control_stick(materials):
    """Create a detailed control stick with realistic grip"""
    print("🕹️ Creating detailed control stick...")
    
    # Main shaft
    bpy.ops.mesh.primitive_cylinder_add(radius=0.02, depth=0.4, location=(0.15, 0.45, 0.65))
    stick_shaft = bpy.context.active_object
    stick_shaft.name = "Control_Stick_Shaft"
    stick_shaft.data.materials.append(materials['aluminum'])
    
    # Grip handle
    bpy.ops.mesh.primitive_cylinder_add(radius=0.03, depth=0.12, location=(0.15, 0.45, 0.85))
    grip = bpy.context.active_object
    grip.name = "Control_Stick_Grip"
    
    # Add grip texture with displacement
    bpy.ops.object.modifier_add(type='SUBSURF')
    grip.modifiers["Subdivision Surface"].levels = 2
    
    # Create grip material with noise
    grip_material = bpy.data.materials.new(name="Grip_Material")
    grip_material.use_nodes = True
    grip_material.node_tree.clear()
    
    bsdf = grip_material.node_tree.nodes.new(type='ShaderNodeBsdfPrincipled')
    output = grip_material.node_tree.nodes.new(type='ShaderNodeOutputMaterial')
    noise = grip_material.node_tree.nodes.new(type='ShaderNodeTexNoise')
    displacement = grip_material.node_tree.nodes.new(type='ShaderNodeDisplacement')
    
    # Grip texture properties
    bsdf.inputs['Base Color'].default_value = (0.2, 0.2, 0.2, 1.0)
    bsdf.inputs['Roughness'].default_value = 0.8
    noise.inputs['Scale'].default_value = 20.0
    displacement.inputs['Scale'].default_value = 0.002
    
    grip_material.node_tree.links.new(noise.outputs['Fac'], displacement.inputs['Height'])
    grip_material.node_tree.links.new(bsdf.outputs['BSDF'], output.inputs['Surface'])
    grip_material.node_tree.links.new(displacement.outputs['Displacement'], output.inputs['Displacement'])
    
    grip.data.materials.append(grip_material)
    
    # Trigger button
    bpy.ops.mesh.primitive_cube_add(size=0.02, location=(0.17, 0.45, 0.82))
    trigger = bpy.context.active_object
    trigger.name = "Control_Stick_Trigger"
    trigger.data.materials.append(materials['rubber'])
    
    # Hat switch (4-way)
    bpy.ops.mesh.primitive_cylinder_add(radius=0.015, depth=0.01, location=(0.15, 0.45, 0.9))
    hat_switch = bpy.context.active_object
    hat_switch.name = "Hat_Switch"
    hat_switch.data.materials.append(materials['rubber'])
    
    # Join stick parts
    bpy.ops.object.select_all(action='DESELECT')
    stick_shaft.select_set(True)
    grip.select_set(True)
    trigger.select_set(True)
    hat_switch.select_set(True)
    bpy.context.view_layer.objects.active = stick_shaft
    bpy.ops.object.join()
    
    return stick_shaft

def create_instrument_panel(materials):
    """Create detailed instrument panel with displays"""
    print("📱 Creating detailed instrument panel...")
    
    # Main panel base
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 1.0, 0.95))
    panel_base = bpy.context.active_object
    panel_base.name = "Instrument_Panel_Base"
    panel_base.scale = (1.0, 0.15, 0.4)
    panel_base.rotation_euler = (math.radians(-15), 0, 0)
    
    # Add bevel and subsurf for smooth edges
    bpy.ops.object.modifier_add(type='BEVEL')
    panel_base.modifiers["Bevel"].width = 0.01
    bpy.ops.object.modifier_add(type='SUBSURF')
    panel_base.modifiers["Subdivision Surface"].levels = 1
    
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
    
    # Central warning panel
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 1.08, 1.05))
    warning_panel = bpy.context.active_object
    warning_panel.name = "Warning_Panel"
    warning_panel.scale = (0.4, 0.02, 0.1)
    warning_panel.rotation_euler = (math.radians(-15), 0, 0)
    warning_panel.data.materials.append(materials['display'])
    
    # Add switch bezels around displays
    for i, pos in enumerate([(-0.3, 1.08, 0.98), (0.3, 1.08, 0.98)]):
        bpy.ops.mesh.primitive_cube_add(size=1, location=pos)
        bezel = bpy.context.active_object
        bezel.name = f"Display_Bezel_{i}"
        bezel.scale = (0.27, 0.03, 0.22)
        bezel.rotation_euler = (math.radians(-15), 0, 0)
        bezel.data.materials.append(materials['aluminum'])
    
    return panel_base

def create_throttle_quadrant(materials):
    """Create detailed throttle quadrant"""
    print("🎚️ Creating detailed throttle quadrant...")
    
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
    
    # Afterburner detent
    bpy.ops.mesh.primitive_cylinder_add(radius=0.02, depth=0.05, location=(-0.4, 0.25, 0.65))
    detent = bpy.context.active_object
    detent.name = "Afterburner_Detent"
    detent.rotation_euler = (math.radians(90), 0, 0)
    detent.data.materials.append(materials['aluminum'])
    
    return throttle_base

def create_switch_panels(materials):
    """Create detailed switch panels"""
    print("🔘 Creating detailed switch panels...")
    
    switch_group = bpy.data.collections.new("Switch_Panels")
    bpy.context.scene.collection.children.link(switch_group)
    
    # Left console switches
    for row in range(6):
        for col in range(4):
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
            
            # Create colored switch material
            switch_color = (1.0, 0.0, 0.0, 1.0) if row % 2 == 0 else (0.0, 1.0, 0.0, 1.0)
            switch_mat = bpy.data.materials.new(name=f"Switch_Material_{row}_{col}")
            switch_mat.use_nodes = True
            bsdf = switch_mat.node_tree.nodes["Principled BSDF"]
            bsdf.inputs['Base Color'].default_value = switch_color
            bsdf.inputs['Emission'].default_value = switch_color
            bsdf.inputs['Emission Strength'].default_value = 0.5
            
            switch_cap.data.materials.append(switch_mat)
            
            # Move to collection
            switch_group.objects.link(switch_base)
            switch_group.objects.link(switch_cap)
            bpy.context.scene.collection.objects.unlink(switch_base)
            bpy.context.scene.collection.objects.unlink(switch_cap)

def create_canopy_glass(materials):
    """Create realistic canopy glass"""
    print("🪟 Creating realistic canopy glass...")
    
    # Main canopy
    bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=(0, 0.5, 1.2))
    canopy = bpy.context.active_object
    canopy.name = "Canopy_Glass"
    canopy.scale = (0.8, 1.2, 0.6)
    
    # Edit to create proper canopy shape
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.bisect(plane_co=(0, 0, 1), plane_no=(0, 0, -1), clear_inner=True)
    bpy.ops.mesh.bisect(plane_co=(0, 0, 0.8), plane_no=(0, 0, -1), clear_inner=True)
    bpy.ops.object.mode_set(mode='OBJECT')
    
    # Add subsurf for smooth surface
    bpy.ops.object.modifier_add(type='SUBSURF')
    canopy.modifiers["Subdivision Surface"].levels = 2
    
    canopy.data.materials.append(materials['glass'])
    
    # Side windows
    bpy.ops.mesh.primitive_cube_add(size=1, location=(-0.6, 0.5, 1.0))
    left_window = bpy.context.active_object
    left_window.name = "Left_Window"
    left_window.scale = (0.05, 0.8, 0.4)
    left_window.rotation_euler = (0, math.radians(15), 0)
    left_window.data.materials.append(materials['glass'])
    
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0.6, 0.5, 1.0))
    right_window = bpy.context.active_object
    right_window.name = "Right_Window"
    right_window.scale = (0.05, 0.8, 0.4)
    right_window.rotation_euler = (0, math.radians(-15), 0)
    right_window.data.materials.append(materials['glass'])
    
    return canopy

def create_hud_system(materials):
    """Create HUD (Heads Up Display) system"""
    print("👁️ Creating HUD system...")
    
    # HUD glass
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 1.2, 1.3))
    hud_glass = bpy.context.active_object
    hud_glass.name = "HUD_Glass"
    hud_glass.scale = (0.3, 0.02, 0.25)
    hud_glass.rotation_euler = (math.radians(-30), 0, 0)
    
    # Create HUD material (semi-transparent with green glow)
    hud_material = bpy.data.materials.new(name="HUD_Material")
    hud_material.use_nodes = True
    hud_material.node_tree.clear()
    
    bsdf = hud_material.node_tree.nodes.new(type='ShaderNodeBsdfPrincipled')
    emission = hud_material.node_tree.nodes.new(type='ShaderNodeEmission')
    output = hud_material.node_tree.nodes.new(type='ShaderNodeOutputMaterial')
    mix = hud_material.node_tree.nodes.new(type='ShaderNodeMixShader')
    
    # HUD properties
    bsdf.inputs['Base Color'].default_value = (0.0, 1.0, 0.3, 1.0)
    bsdf.inputs['Transmission'].default_value = 0.9
    bsdf.inputs['Alpha'].default_value = 0.3
    emission.inputs['Color'].default_value = (0.0, 1.0, 0.3, 1.0)
    emission.inputs['Strength'].default_value = 1.0
    
    hud_material.blend_method = 'BLEND'
    hud_material.node_tree.links.new(bsdf.outputs['BSDF'], mix.inputs[1])
    hud_material.node_tree.links.new(emission.outputs['Emission'], mix.inputs[2])
    mix.inputs['Fac'].default_value = 0.3
    hud_material.node_tree.links.new(mix.outputs['Shader'], output.inputs['Surface'])
    
    hud_glass.data.materials.append(hud_material)
    
    return hud_glass

def setup_lighting():
    """Setup realistic cockpit lighting"""
    print("💡 Setting up realistic lighting...")
    
    # Remove default light
    if "Light" in bpy.data.objects:
        bpy.data.objects.remove(bpy.data.objects["Light"], do_unlink=True)
    
    # HDRI environment lighting
    world = bpy.context.scene.world
    world.use_nodes = True
    world.node_tree.clear()
    
    # World shader setup
    output = world.node_tree.nodes.new('ShaderNodeOutputWorld')
    background = world.node_tree.nodes.new('ShaderNodeBackground')
    environment = world.node_tree.nodes.new('ShaderNodeTexEnvironment')
    mapping = world.node_tree.nodes.new('ShaderNodeMapping')
    coord = world.node_tree.nodes.new('ShaderNodeTexCoord')
    
    # Sky color
    background.inputs['Color'].default_value = (0.5, 0.7, 1.0, 1.0)  # Sky blue
    background.inputs['Strength'].default_value = 1.0
    
    world.node_tree.links.new(coord.outputs['Generated'], mapping.inputs['Vector'])
    world.node_tree.links.new(mapping.outputs['Vector'], environment.inputs['Vector'])
    world.node_tree.links.new(background.outputs['Background'], output.inputs['Surface'])
    
    # Key light (sun)
    bpy.ops.object.light_add(type='SUN', location=(5, 5, 10))
    sun = bpy.context.active_object
    sun.name = "Sun_Light"
    sun.data.energy = 3.0
    sun.data.color = (1.0, 0.95, 0.8)
    sun.rotation_euler = (math.radians(45), math.radians(45), 0)
    
    # Cockpit interior lighting
    bpy.ops.object.light_add(type='POINT', location=(0, 0.8, 1.0))
    panel_light = bpy.context.active_object
    panel_light.name = "Panel_Light"
    panel_light.data.energy = 20.0
    panel_light.data.color = (1.0, 0.2, 0.2)  # Red instrument lighting
    
    # Side console lights
    bpy.ops.object.light_add(type='POINT', location=(-0.4, 0.6, 0.8))
    left_light = bpy.context.active_object
    left_light.name = "Left_Console_Light"
    left_light.data.energy = 10.0
    left_light.data.color = (0.2, 0.4, 1.0)  # Blue console lighting
    
    bpy.ops.object.light_add(type='POINT', location=(0.4, 0.6, 0.8))
    right_light = bpy.context.active_object
    right_light.name = "Right_Console_Light"
    right_light.data.energy = 10.0
    right_light.data.color = (0.2, 0.4, 1.0)  # Blue console lighting

def setup_camera():
    """Setup camera for pilot's view"""
    print("📸 Setting up pilot's view camera...")
    
    # Remove default camera
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
    
    # Render engine
    bpy.context.scene.render.engine = 'CYCLES'
    bpy.context.scene.cycles.samples = 128
    bpy.context.scene.cycles.use_denoising = True
    
    # Resolution
    bpy.context.scene.render.resolution_x = 1920
    bpy.context.scene.render.resolution_y = 1080
    bpy.context.scene.render.resolution_percentage = 100
    
    # Color management
    bpy.context.scene.view_settings.view_transform = 'Filmic'
    bpy.context.scene.view_settings.look = 'Medium High Contrast'

def main():
    """Main function to create the realistic cockpit"""
    print("🚀 Starting realistic fighter jet cockpit creation...")
    
    # Clear scene
    clear_scene()
    
    # Create materials
    materials = create_realistic_materials()
    
    # Create cockpit components
    create_detailed_cockpit_frame(materials)
    create_ejection_seat(materials)
    create_control_stick(materials)
    create_instrument_panel(materials)
    create_throttle_quadrant(materials)
    create_switch_panels(materials)
    create_canopy_glass(materials)
    create_hud_system(materials)
    
    # Setup scene
    setup_lighting()
    setup_camera()
    setup_render_settings()
    
    # Create main cockpit collection
    cockpit_collection = bpy.data.collections.new("Realistic_Fighter_Cockpit")
    bpy.context.scene.collection.children.link(cockpit_collection)
    
    # Move all cockpit objects to collection
    for obj in bpy.context.scene.objects:
        if obj.type == 'MESH' and "Cockpit" in obj.name or "Ejection" in obj.name or "Control" in obj.name or "Instrument" in obj.name or "Throttle" in obj.name or "Canopy" in obj.name or "HUD" in obj.name:
            cockpit_collection.objects.link(obj)
            bpy.context.scene.collection.objects.unlink(obj)
    
    print("✅ Realistic fighter jet cockpit creation completed!")
    print("🎮 Switch to Camera view (Numpad 0) to see pilot's perspective")
    print("🎬 Press F12 to render the final image")
    
    # Export as GLB
    export_path = "C:/Users/ssnguna/Local Sites/malloc/experiments/environments/fighter_jet/docs/blender work/exports_assembled/realistic_fighter_cockpit.glb"
    
    try:
        # Select all cockpit objects
        bpy.ops.object.select_all(action='DESELECT')
        for obj in cockpit_collection.objects:
            obj.select_set(True)
        
        # Export as GLB
        bpy.ops.export_scene.gltf(
            filepath=export_path,
            use_selection=True,
            export_format='GLB',
            export_materials='EXPORT',
            export_image_format='AUTO',
            export_apply=False,
            export_attributes=True,
            export_draco_mesh_compression_enable=True,
            export_draco_mesh_compression_level=6,
            export_lights=True
        )
        print(f"✅ Exported realistic cockpit to: {export_path}")
        
    except Exception as e:
        print(f"❌ Export failed: {str(e)}")

if __name__ == "__main__":
    main()
