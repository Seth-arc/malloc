"""
ULTRA-COMPATIBLE - Simple Realistic Fighter Jet Cockpit for Blender
This script uses only the most basic Blender operations for maximum compatibility.

Run this in Blender's Text Editor or Console.
"""

import bpy
import math

def clear_scene():
    """Clear all objects from the scene"""
    print("🧹 Clearing scene...")
    
    # Deselect all
    bpy.ops.object.select_all(action='DESELECT')
    
    # Select all objects
    for obj in list(bpy.context.scene.objects):
        if obj.type in ['MESH', 'LIGHT', 'CAMERA']:
            bpy.context.view_layer.objects.active = obj
            obj.select_set(True)
    
    # Delete selected objects
    if bpy.context.selected_objects:
        bpy.ops.object.delete(use_global=False)
    
    print("✅ Scene cleared")

def create_simple_materials():
    """Create simple but realistic materials"""
    print("🎨 Creating simple realistic materials...")
    materials = {}
    
    # 1. Aluminum Material
    aluminum = bpy.data.materials.new(name="Aluminum")
    aluminum.use_nodes = True
    
    # Get the default principled BSDF
    bsdf = None
    for node in aluminum.node_tree.nodes:
        if node.type == 'BSDF_PRINCIPLED':
            bsdf = node
            break
    
    if bsdf:
        bsdf.inputs['Base Color'].default_value = (0.4, 0.4, 0.5, 1.0)  # Gray metal
        bsdf.inputs['Metallic'].default_value = 0.9
        bsdf.inputs['Roughness'].default_value = 0.3
    
    materials['aluminum'] = aluminum
    
    # 2. Carbon Fiber Material
    carbon = bpy.data.materials.new(name="Carbon")
    carbon.use_nodes = True
    
    bsdf = None
    for node in carbon.node_tree.nodes:
        if node.type == 'BSDF_PRINCIPLED':
            bsdf = node
            break
    
    if bsdf:
        bsdf.inputs['Base Color'].default_value = (0.05, 0.05, 0.05, 1.0)  # Dark
        bsdf.inputs['Metallic'].default_value = 0.1
        bsdf.inputs['Roughness'].default_value = 0.4
    
    materials['carbon'] = carbon
    
    # 3. Leather Material
    leather = bpy.data.materials.new(name="Leather")
    leather.use_nodes = True
    
    bsdf = None
    for node in leather.node_tree.nodes:
        if node.type == 'BSDF_PRINCIPLED':
            bsdf = node
            break
    
    if bsdf:
        bsdf.inputs['Base Color'].default_value = (0.2, 0.1, 0.05, 1.0)  # Brown
        bsdf.inputs['Metallic'].default_value = 0.0
        bsdf.inputs['Roughness'].default_value = 0.8
    
    materials['leather'] = leather
    
    # 4. Display Material (Glowing Green)
    display = bpy.data.materials.new(name="Display")
    display.use_nodes = True
    
    bsdf = None
    for node in display.node_tree.nodes:
        if node.type == 'BSDF_PRINCIPLED':
            bsdf = node
            break
    
    if bsdf:
        bsdf.inputs['Base Color'].default_value = (0.0, 1.0, 0.2, 1.0)  # Green
        # Try to add emission if available
        if 'Emission' in bsdf.inputs:
            bsdf.inputs['Emission'].default_value = (0.0, 0.8, 0.1, 1.0)
            if 'Emission Strength' in bsdf.inputs:
                bsdf.inputs['Emission Strength'].default_value = 1.5
    
    materials['display'] = display
    
    # 5. Rubber Material
    rubber = bpy.data.materials.new(name="Rubber")
    rubber.use_nodes = True
    
    bsdf = None
    for node in rubber.node_tree.nodes:
        if node.type == 'BSDF_PRINCIPLED':
            bsdf = node
            break
    
    if bsdf:
        bsdf.inputs['Base Color'].default_value = (0.1, 0.1, 0.1, 1.0)  # Dark rubber
        bsdf.inputs['Metallic'].default_value = 0.0
        bsdf.inputs['Roughness'].default_value = 0.9
    
    materials['rubber'] = rubber
    
    # 6. Glass Material
    glass = bpy.data.materials.new(name="Glass")
    glass.use_nodes = True
    
    bsdf = None
    for node in glass.node_tree.nodes:
        if node.type == 'BSDF_PRINCIPLED':
            bsdf = node
            break
    
    if bsdf:
        bsdf.inputs['Base Color'].default_value = (0.9, 0.95, 1.0, 1.0)  # Clear
        bsdf.inputs['Metallic'].default_value = 0.0
        bsdf.inputs['Roughness'].default_value = 0.0
        
        # Try to set transmission if available
        if 'Transmission' in bsdf.inputs:
            bsdf.inputs['Transmission'].default_value = 0.9
        
        if 'Alpha' in bsdf.inputs:
            bsdf.inputs['Alpha'].default_value = 0.2
            glass.blend_method = 'BLEND'
    
    materials['glass'] = glass
    
    print("✅ Created 6 simple realistic materials")
    return materials

def create_cockpit_frame(materials):
    """Create cockpit frame using only cubes"""
    print("🏗️ Creating cockpit frame...")
    
    # Bottom frame
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0.5, 0.3))
    bottom = bpy.context.active_object
    bottom.name = "Frame_Bottom"
    bottom.scale = (1.2, 2.0, 0.05)
    bottom.data.materials.append(materials['aluminum'])
    
    # Left frame
    bpy.ops.mesh.primitive_cube_add(size=1, location=(-0.6, 0.5, 0.8))
    left = bpy.context.active_object
    left.name = "Frame_Left"
    left.scale = (0.05, 2.0, 1.0)
    left.data.materials.append(materials['aluminum'])
    
    # Right frame
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0.6, 0.5, 0.8))
    right = bpy.context.active_object
    right.name = "Frame_Right"
    right.scale = (0.05, 2.0, 1.0)
    right.data.materials.append(materials['aluminum'])
    
    # Front frame
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 1.4, 0.8))
    front = bpy.context.active_object
    front.name = "Frame_Front"
    front.scale = (1.2, 0.05, 1.0)
    front.data.materials.append(materials['aluminum'])
    
    print("✅ Cockpit frame created")
    return bottom

def create_ejection_seat(materials):
    """Create ejection seat"""
    print("🪑 Creating ejection seat...")
    
    # Seat base
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0.3, 0.4))
    seat_base = bpy.context.active_object
    seat_base.name = "Seat_Base"
    seat_base.scale = (0.5, 0.6, 0.1)
    seat_base.data.materials.append(materials['leather'])
    
    # Seat back
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0.0, 0.7))
    seat_back = bpy.context.active_object
    seat_back.name = "Seat_Back"
    seat_back.scale = (0.5, 0.1, 0.4)
    seat_back.rotation_euler = (math.radians(-10), 0, 0)
    seat_back.data.materials.append(materials['leather'])
    
    # Headrest
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, -0.05, 1.0))
    headrest = bpy.context.active_object
    headrest.name = "Headrest"
    headrest.scale = (0.3, 0.1, 0.15)
    headrest.data.materials.append(materials['leather'])
    
    print("✅ Ejection seat created")
    return seat_base

def create_control_stick(materials):
    """Create control stick"""
    print("🕹️ Creating control stick...")
    
    # Main shaft
    bpy.ops.mesh.primitive_cylinder_add(radius=0.02, depth=0.4, location=(0.15, 0.45, 0.65))
    shaft = bpy.context.active_object
    shaft.name = "Stick_Shaft"
    shaft.data.materials.append(materials['aluminum'])
    
    # Grip handle
    bpy.ops.mesh.primitive_cylinder_add(radius=0.03, depth=0.12, location=(0.15, 0.45, 0.85))
    grip = bpy.context.active_object
    grip.name = "Stick_Grip"
    grip.data.materials.append(materials['rubber'])
    
    # Trigger button
    bpy.ops.mesh.primitive_cube_add(size=0.02, location=(0.17, 0.45, 0.82))
    trigger = bpy.context.active_object
    trigger.name = "Trigger"
    trigger.data.materials.append(materials['rubber'])
    
    print("✅ Control stick created")
    return shaft

def create_instrument_panel(materials):
    """Create instrument panel"""
    print("📱 Creating instrument panel...")
    
    # Main panel base
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 1.0, 0.95))
    panel = bpy.context.active_object
    panel.name = "Instrument_Panel"
    panel.scale = (1.0, 0.15, 0.4)
    panel.rotation_euler = (math.radians(-15), 0, 0)
    panel.data.materials.append(materials['carbon'])
    
    # Left MFD Display
    bpy.ops.mesh.primitive_cube_add(size=1, location=(-0.3, 1.08, 0.98))
    mfd_left = bpy.context.active_object
    mfd_left.name = "MFD_Left"
    mfd_left.scale = (0.25, 0.02, 0.2)
    mfd_left.rotation_euler = (math.radians(-15), 0, 0)
    mfd_left.data.materials.append(materials['display'])
    
    # Right MFD Display
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0.3, 1.08, 0.98))
    mfd_right = bpy.context.active_object
    mfd_right.name = "MFD_Right"
    mfd_right.scale = (0.25, 0.02, 0.2)
    mfd_right.rotation_euler = (math.radians(-15), 0, 0)
    mfd_right.data.materials.append(materials['display'])
    
    # Warning panel (center)
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 1.08, 1.05))
    warning = bpy.context.active_object
    warning.name = "Warning_Panel"
    warning.scale = (0.4, 0.02, 0.1)
    warning.rotation_euler = (math.radians(-15), 0, 0)
    warning.data.materials.append(materials['display'])
    
    print("✅ Instrument panel created")
    return panel

def create_throttle_quadrant(materials):
    """Create throttle quadrant"""
    print("🎚️ Creating throttle quadrant...")
    
    # Throttle base
    bpy.ops.mesh.primitive_cube_add(size=1, location=(-0.4, 0.3, 0.6))
    base = bpy.context.active_object
    base.name = "Throttle_Base"
    base.scale = (0.15, 0.3, 0.25)
    base.data.materials.append(materials['carbon'])
    
    # Throttle lever
    bpy.ops.mesh.primitive_cube_add(size=1, location=(-0.4, 0.45, 0.75))
    lever = bpy.context.active_object
    lever.name = "Throttle_Lever"
    lever.scale = (0.04, 0.15, 0.02)
    lever.rotation_euler = (math.radians(-20), 0, 0)
    lever.data.materials.append(materials['aluminum'])
    
    # Throttle grip
    bpy.ops.mesh.primitive_cube_add(size=1, location=(-0.4, 0.52, 0.8))
    grip = bpy.context.active_object
    grip.name = "Throttle_Grip"
    grip.scale = (0.06, 0.08, 0.04)
    grip.rotation_euler = (math.radians(-20), 0, 0)
    grip.data.materials.append(materials['rubber'])
    
    print("✅ Throttle quadrant created")
    return base

def create_simple_switches(materials):
    """Create simple switch panel using only cubes"""
    print("🔘 Creating simple switches...")
    
    # Switch panel base
    bpy.ops.mesh.primitive_cube_add(size=1, location=(-0.45, 0.85, 0.9))
    switch_panel = bpy.context.active_object
    switch_panel.name = "Switch_Panel"
    switch_panel.scale = (0.2, 0.05, 0.3)
    switch_panel.data.materials.append(materials['carbon'])
    
    # Create simple switches (cubes only)
    switch_positions = [
        (-0.5, 0.87, 0.8), (-0.46, 0.87, 0.8), (-0.42, 0.87, 0.8),
        (-0.5, 0.87, 0.85), (-0.46, 0.87, 0.85), (-0.42, 0.87, 0.85),
        (-0.5, 0.87, 0.9), (-0.46, 0.87, 0.9), (-0.42, 0.87, 0.9),
        (-0.5, 0.87, 0.95), (-0.46, 0.87, 0.95), (-0.42, 0.87, 0.95)
    ]
    
    for i, pos in enumerate(switch_positions):
        # Switch base
        bpy.ops.mesh.primitive_cube_add(size=0.015, location=pos)
        switch = bpy.context.active_object
        switch.name = f"Switch_{i}"
        switch.data.materials.append(materials['aluminum'])
        
        # Switch indicator (small cube on top)
        bpy.ops.mesh.primitive_cube_add(size=0.008, location=(pos[0], pos[1]+0.01, pos[2]))
        indicator = bpy.context.active_object
        indicator.name = f"Switch_Indicator_{i}"
        
        # Create simple colored material
        color_mat = bpy.data.materials.new(name=f"Switch_Color_{i}")
        color_mat.use_nodes = True
        
        # Get BSDF node
        bsdf = None
        for node in color_mat.node_tree.nodes:
            if node.type == 'BSDF_PRINCIPLED':
                bsdf = node
                break
        
        if bsdf:
            # Alternate colors
            if i % 3 == 0:
                color = (1.0, 0.0, 0.0, 1.0)  # Red
            elif i % 3 == 1:
                color = (0.0, 1.0, 0.0, 1.0)  # Green
            else:
                color = (1.0, 0.8, 0.0, 1.0)  # Amber
            
            bsdf.inputs['Base Color'].default_value = color
            
            # Add emission if available
            if 'Emission' in bsdf.inputs:
                bsdf.inputs['Emission'].default_value = color
                if 'Emission Strength' in bsdf.inputs:
                    bsdf.inputs['Emission Strength'].default_value = 0.5
        
        indicator.data.materials.append(color_mat)
    
    print("✅ Simple switches created")
    return switch_panel

def create_canopy(materials):
    """Create simple canopy"""
    print("🪟 Creating canopy...")
    
    # Front windscreen
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 1.2, 1.3))
    windscreen = bpy.context.active_object
    windscreen.name = "Windscreen"
    windscreen.scale = (0.8, 0.05, 0.6)
    windscreen.rotation_euler = (math.radians(-30), 0, 0)
    windscreen.data.materials.append(materials['glass'])
    
    # Left window
    bpy.ops.mesh.primitive_cube_add(size=1, location=(-0.6, 0.5, 1.2))
    left_window = bpy.context.active_object
    left_window.name = "Left_Window"
    left_window.scale = (0.05, 1.0, 0.5)
    left_window.rotation_euler = (0, math.radians(10), 0)
    left_window.data.materials.append(materials['glass'])
    
    # Right window
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0.6, 0.5, 1.2))
    right_window = bpy.context.active_object
    right_window.name = "Right_Window"
    right_window.scale = (0.05, 1.0, 0.5)
    right_window.rotation_euler = (0, math.radians(-10), 0)
    right_window.data.materials.append(materials['glass'])
    
    # Top canopy
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0.5, 1.5))
    top_canopy = bpy.context.active_object
    top_canopy.name = "Top_Canopy"
    top_canopy.scale = (0.8, 1.2, 0.05)
    top_canopy.data.materials.append(materials['glass'])
    
    print("✅ Canopy created")
    return windscreen

def setup_simple_lighting():
    """Setup simple but effective lighting"""
    print("💡 Setting up lighting...")
    
    # Remove default light if exists
    if "Light" in bpy.data.objects:
        bpy.data.objects.remove(bpy.data.objects["Light"], do_unlink=True)
    
    # Sun light
    bpy.ops.object.light_add(type='SUN', location=(5, 5, 10))
    sun = bpy.context.active_object
    sun.name = "Sun"
    sun.data.energy = 5.0
    sun.data.color = (1.0, 0.95, 0.8)
    
    # Panel light (red)
    bpy.ops.object.light_add(type='POINT', location=(0, 0.8, 1.0))
    panel_light = bpy.context.active_object
    panel_light.name = "Panel_Light"
    panel_light.data.energy = 100.0
    panel_light.data.color = (1.0, 0.2, 0.2)
    
    # Console lights (blue)
    bpy.ops.object.light_add(type='POINT', location=(-0.4, 0.6, 0.8))
    left_light = bpy.context.active_object
    left_light.name = "Left_Light"
    left_light.data.energy = 50.0
    left_light.data.color = (0.2, 0.4, 1.0)
    
    bpy.ops.object.light_add(type='POINT', location=(0.4, 0.6, 0.8))
    right_light = bpy.context.active_object
    right_light.name = "Right_Light"
    right_light.data.energy = 50.0
    right_light.data.color = (0.2, 0.4, 1.0)
    
    print("✅ Lighting setup complete")

def setup_camera():
    """Setup pilot camera"""
    print("📸 Setting up camera...")
    
    # Remove default camera
    if "Camera" in bpy.data.objects:
        bpy.data.objects.remove(bpy.data.objects["Camera"], do_unlink=True)
    
    # Add camera at pilot position
    bpy.ops.object.camera_add(location=(0, 0.3, 0.9))
    camera = bpy.context.active_object
    camera.name = "Pilot_Camera"
    camera.rotation_euler = (math.radians(90), 0, math.radians(180))
    
    # Set as active camera
    bpy.context.scene.camera = camera
    
    # Camera settings
    camera.data.lens = 35
    camera.data.clip_start = 0.01
    camera.data.clip_end = 1000
    
    print("✅ Camera setup complete")

def main():
    """Main function"""
    print("🚀 Creating simple realistic fighter jet cockpit...")
    
    # Clear scene
    clear_scene()
    
    # Create materials
    materials = create_simple_materials()
    
    # Create cockpit components
    create_cockpit_frame(materials)
    create_ejection_seat(materials)
    create_control_stick(materials)
    create_instrument_panel(materials)
    create_throttle_quadrant(materials)
    create_simple_switches(materials)
    create_canopy(materials)
    
    # Setup scene
    setup_simple_lighting()
    setup_camera()
    
    print("✅ Simple realistic cockpit completed!")
    print("🎮 Press Numpad 0 for pilot view")
    print("🎨 Switch to Material Preview or Rendered viewport")
    print("🎬 Press F12 to render")
    
    # Try GLB export
    try:
        export_path = "C:/Users/ssnguna/Local Sites/malloc/experiments/environments/fighter_jet/docs/blender work/exports_assembled/simple_cockpit.glb"
        
        bpy.ops.object.select_all(action='DESELECT')
        for obj in bpy.context.scene.objects:
            if obj.type == 'MESH':
                obj.select_set(True)
        
        if hasattr(bpy.ops.export_scene, 'gltf'):
            bpy.ops.export_scene.gltf(
                filepath=export_path,
                use_selection=True,
                export_format='GLB'
            )
            print(f"✅ Exported to: {export_path}")
        else:
            print("💡 Manual export: File → Export → glTF 2.0")
            
    except Exception as e:
        print(f"⚠️ Export note: {str(e)}")
        print("💡 Manual export: File → Export → glTF 2.0")

if __name__ == "__main__":
    main()
