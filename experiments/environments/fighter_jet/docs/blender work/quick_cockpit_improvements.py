"""
Quick Cockpit Improvements Script
This script enhances your existing basic cockpit with better materials and details.
Run this in Blender to immediately improve realism without starting from scratch.
"""

import bpy
import bmesh
import math

def improve_existing_cockpit():
    """Improve the existing cockpit with better materials and details"""
    print("🔧 Improving existing cockpit realism...")
    
    # Create better materials
    materials = create_improved_materials()
    
    # Find and improve existing objects
    improve_cockpit_frame(materials)
    improve_control_stick(materials)
    improve_throttle(materials)
    improve_instrument_panel(materials)
    improve_seat(materials)
    add_cockpit_details(materials)
    
    print("✅ Cockpit improvements completed!")

def create_improved_materials():
    """Create realistic PBR materials"""
    materials = {}
    
    # Military Aluminum
    aluminum = bpy.data.materials.new(name="Improved_Aluminum")
    aluminum.use_nodes = True
    bsdf = aluminum.node_tree.nodes["Principled BSDF"]
    bsdf.inputs['Base Color'].default_value = (0.4, 0.45, 0.5, 1.0)
    bsdf.inputs['Metallic'].default_value = 0.9
    bsdf.inputs['Roughness'].default_value = 0.2
    materials['aluminum'] = aluminum
    
    # Carbon Fiber
    carbon = bpy.data.materials.new(name="Improved_Carbon")
    carbon.use_nodes = True
    bsdf = carbon.node_tree.nodes["Principled BSDF"]
    bsdf.inputs['Base Color'].default_value = (0.05, 0.05, 0.05, 1.0)
    bsdf.inputs['Metallic'].default_value = 0.1
    bsdf.inputs['Roughness'].default_value = 0.3
    materials['carbon'] = carbon
    
    # Leather
    leather = bpy.data.materials.new(name="Improved_Leather")
    leather.use_nodes = True
    bsdf = leather.node_tree.nodes["Principled BSDF"]
    bsdf.inputs['Base Color'].default_value = (0.15, 0.1, 0.08, 1.0)
    bsdf.inputs['Metallic'].default_value = 0.0
    bsdf.inputs['Roughness'].default_value = 0.8
    materials['leather'] = leather
    
    # Glowing Display
    display = bpy.data.materials.new(name="Improved_Display")
    display.use_nodes = True
    bsdf = display.node_tree.nodes["Principled BSDF"]
    bsdf.inputs['Base Color'].default_value = (0.0, 1.0, 0.2, 1.0)
    bsdf.inputs['Emission'].default_value = (0.0, 1.0, 0.2, 1.0)
    bsdf.inputs['Emission Strength'].default_value = 2.0
    materials['display'] = display
    
    # Rubber Grip
    rubber = bpy.data.materials.new(name="Improved_Rubber")
    rubber.use_nodes = True
    bsdf = rubber.node_tree.nodes["Principled BSDF"]
    bsdf.inputs['Base Color'].default_value = (0.1, 0.1, 0.1, 1.0)
    bsdf.inputs['Metallic'].default_value = 0.0
    bsdf.inputs['Roughness'].default_value = 0.9
    materials['rubber'] = rubber
    
    print("✅ Created improved materials")
    return materials

def improve_cockpit_frame(materials):
    """Improve existing cockpit frame"""
    # Find frame objects
    frame_objects = [obj for obj in bpy.context.scene.objects if 'frame' in obj.name.lower() or 'cockpit' in obj.name.lower()]
    
    for obj in frame_objects:
        if obj.type == 'MESH':
            # Add bevel modifier for rounded edges
            if "Bevel" not in [mod.name for mod in obj.modifiers]:
                bevel_mod = obj.modifiers.new(name="Bevel", type='BEVEL')
                bevel_mod.width = 0.01
                bevel_mod.segments = 3
            
            # Apply aluminum material
            if obj.data.materials:
                obj.data.materials[0] = materials['aluminum']
            else:
                obj.data.materials.append(materials['aluminum'])
    
    print("✅ Improved cockpit frame")

def improve_control_stick(materials):
    """Improve existing control stick"""
    stick_objects = [obj for obj in bpy.context.scene.objects if 'stick' in obj.name.lower() or 'control' in obj.name.lower()]
    
    for obj in stick_objects:
        if obj.type == 'MESH':
            # Apply rubber material for grip
            if obj.data.materials:
                obj.data.materials[0] = materials['rubber']
            else:
                obj.data.materials.append(materials['rubber'])
            
            # Add some detail
            bpy.context.view_layer.objects.active = obj
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.subdivide(number_cuts=2)
            bpy.ops.object.mode_set(mode='OBJECT')
    
    print("✅ Improved control stick")

def improve_throttle(materials):
    """Improve existing throttle"""
    throttle_objects = [obj for obj in bpy.context.scene.objects if 'throttle' in obj.name.lower()]
    
    for obj in throttle_objects:
        if obj.type == 'MESH':
            # Apply aluminum material
            if obj.data.materials:
                obj.data.materials[0] = materials['aluminum']
            else:
                obj.data.materials.append(materials['aluminum'])
            
            # Add bevel
            if "Bevel" not in [mod.name for mod in obj.modifiers]:
                bevel_mod = obj.modifiers.new(name="Bevel", type='BEVEL')
                bevel_mod.width = 0.005
    
    print("✅ Improved throttle")

def improve_instrument_panel(materials):
    """Improve existing instrument panel"""
    panel_objects = [obj for obj in bpy.context.scene.objects if 'panel' in obj.name.lower() or 'instrument' in obj.name.lower()]
    
    for obj in panel_objects:
        if obj.type == 'MESH':
            # Apply carbon fiber material
            if obj.data.materials:
                obj.data.materials[0] = materials['carbon']
            else:
                obj.data.materials.append(materials['carbon'])
            
            # Add subdivision surface for smoothness
            if "Subdivision Surface" not in [mod.name for mod in obj.modifiers]:
                subsurf_mod = obj.modifiers.new(name="Subdivision Surface", type='SUBSURF')
                subsurf_mod.levels = 1
    
    print("✅ Improved instrument panel")

def improve_seat(materials):
    """Improve existing seat"""
    seat_objects = [obj for obj in bpy.context.scene.objects if 'seat' in obj.name.lower()]
    
    for obj in seat_objects:
        if obj.type == 'MESH':
            # Apply leather material
            if obj.data.materials:
                obj.data.materials[0] = materials['leather']
            else:
                obj.data.materials.append(materials['leather'])
            
            # Add bevel for comfort
            if "Bevel" not in [mod.name for mod in obj.modifiers]:
                bevel_mod = obj.modifiers.new(name="Bevel", type='BEVEL')
                bevel_mod.width = 0.02
                bevel_mod.segments = 3
    
    print("✅ Improved seat")

def add_cockpit_details(materials):
    """Add missing details to cockpit"""
    
    # Add instrument displays if they don't exist
    if not any('display' in obj.name.lower() for obj in bpy.context.scene.objects):
        # Left MFD
        bpy.ops.mesh.primitive_cube_add(size=1, location=(-0.3, 1.0, 0.95))
        left_mfd = bpy.context.active_object
        left_mfd.name = "Left_MFD"
        left_mfd.scale = (0.25, 0.02, 0.2)
        left_mfd.rotation_euler = (math.radians(-15), 0, 0)
        left_mfd.data.materials.append(materials['display'])
        
        # Right MFD
        bpy.ops.mesh.primitive_cube_add(size=1, location=(0.3, 1.0, 0.95))
        right_mfd = bpy.context.active_object
        right_mfd.name = "Right_MFD"
        right_mfd.scale = (0.25, 0.02, 0.2)
        right_mfd.rotation_euler = (math.radians(-15), 0, 0)
        right_mfd.data.materials.append(materials['display'])
    
    # Add some switches
    switch_positions = [
        (-0.4, 0.85, 0.8), (-0.36, 0.85, 0.8), (-0.32, 0.85, 0.8),
        (-0.4, 0.85, 0.85), (-0.36, 0.85, 0.85), (-0.32, 0.85, 0.85)
    ]
    
    for i, pos in enumerate(switch_positions):
        bpy.ops.mesh.primitive_cylinder_add(radius=0.01, depth=0.02, location=pos)
        switch = bpy.context.active_object
        switch.name = f"Switch_{i}"
        switch.rotation_euler = (math.radians(90), 0, 0)
        switch.data.materials.append(materials['aluminum'])
        
        # Switch cap
        bpy.ops.mesh.primitive_sphere_add(radius=0.008, location=(pos[0], pos[1]+0.015, pos[2]))
        cap = bpy.context.active_object
        cap.name = f"Switch_Cap_{i}"
        
        # Colored switch material
        switch_mat = bpy.data.materials.new(name=f"Switch_Mat_{i}")
        switch_mat.use_nodes = True
        bsdf = switch_mat.node_tree.nodes["Principled BSDF"]
        color = (1.0, 0.0, 0.0, 1.0) if i % 2 == 0 else (0.0, 1.0, 0.0, 1.0)
        bsdf.inputs['Base Color'].default_value = color
        bsdf.inputs['Emission'].default_value = color
        bsdf.inputs['Emission Strength'].default_value = 0.5
        cap.data.materials.append(switch_mat)
    
    print("✅ Added cockpit details")

def add_realistic_lighting():
    """Add realistic lighting to the scene"""
    
    # Remove default light if it exists
    if "Light" in bpy.data.objects:
        bpy.data.objects.remove(bpy.data.objects["Light"], do_unlink=True)
    
    # Sun light (external)
    bpy.ops.object.light_add(type='SUN', location=(5, 5, 10))
    sun = bpy.context.active_object
    sun.name = "Sun_Light"
    sun.data.energy = 3.0
    sun.data.color = (1.0, 0.95, 0.8)
    sun.rotation_euler = (math.radians(45), math.radians(45), 0)
    
    # Instrument panel light (red)
    bpy.ops.object.light_add(type='POINT', location=(0, 0.8, 1.0))
    panel_light = bpy.context.active_object
    panel_light.name = "Panel_Light"
    panel_light.data.energy = 20.0
    panel_light.data.color = (1.0, 0.2, 0.2)
    
    # Console lights (blue)
    bpy.ops.object.light_add(type='POINT', location=(-0.4, 0.6, 0.8))
    left_light = bpy.context.active_object
    left_light.name = "Left_Console_Light"
    left_light.data.energy = 10.0
    left_light.data.color = (0.2, 0.4, 1.0)
    
    bpy.ops.object.light_add(type='POINT', location=(0.4, 0.6, 0.8))
    right_light = bpy.context.active_object
    right_light.name = "Right_Console_Light"
    right_light.data.energy = 10.0
    right_light.data.color = (0.2, 0.4, 1.0)
    
    print("✅ Added realistic lighting")

def setup_better_render():
    """Setup better render settings"""
    
    # Use Cycles for better materials
    bpy.context.scene.render.engine = 'CYCLES'
    bpy.context.scene.cycles.samples = 64  # Good quality/speed balance
    bpy.context.scene.cycles.use_denoising = True
    
    # Better color management
    bpy.context.scene.view_settings.view_transform = 'Filmic'
    bpy.context.scene.view_settings.look = 'Medium High Contrast'
    
    print("✅ Improved render settings")

def main():
    """Main improvement function"""
    print("🚀 Starting quick cockpit improvements...")
    
    # Improve existing cockpit
    improve_existing_cockpit()
    
    # Add lighting
    add_realistic_lighting()
    
    # Setup render
    setup_better_render()
    
    print("✅ Quick cockpit improvements completed!")
    print("🎬 Your cockpit now has:")
    print("   • Realistic PBR materials")
    print("   • Smooth beveled edges") 
    print("   • Glowing displays")
    print("   • Military-style lighting")
    print("   • Improved surface details")
    print("")
    print("🎮 Switch to Material Preview or Rendered viewport shading to see the improvements!")

if __name__ == "__main__":
    main()
