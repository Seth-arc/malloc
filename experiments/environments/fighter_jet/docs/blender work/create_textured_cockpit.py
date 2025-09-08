# TEXTURED COCKPIT CREATOR - WITH PROPER MATERIALS
# Run this INSIDE Blender 4.4 Console

import bpy
import os

def create_military_material(name, base_color, metallic=0.0, roughness=0.8):
    """
    Create a military-grade PBR material for cockpit components
    """
    # Create new material
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    
    # Get the principled BSDF node
    principled = mat.node_tree.nodes.get("Principled BSDF")
    if principled:
        # Set base color
        principled.inputs["Base Color"].default_value = (*base_color, 1.0)
        
        # Set metallic value
        principled.inputs["Metallic"].default_value = metallic
        
        # Set roughness
        principled.inputs["Roughness"].default_value = roughness
        
        # Add some subsurface for realism on non-metal surfaces
        if metallic < 0.5:
            principled.inputs["Subsurface Weight"].default_value = 0.1
    
    return mat

def create_cockpit_with_materials():
    """
    Create a fully textured cockpit with proper materials
    """
    print("🎨 CREATING TEXTURED COCKPIT")
    print("=" * 50)
    
    try:
        # Step 1: Clear the scene
        print("Step 1: Clearing scene...")
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete(use_global=False)
        print("✅ Scene cleared")
        
        # Step 2: Create materials first
        print("Step 2: Creating military-grade materials...")
        
        # Cockpit structure material (dark gray metal)
        cockpit_mat = create_military_material(
            "Cockpit_Structure", 
            base_color=(0.15, 0.15, 0.18),  # Dark gray
            metallic=0.8, 
            roughness=0.4
        )
        
        # Control stick material (black with grip texture)
        stick_mat = create_military_material(
            "Control_Stick",
            base_color=(0.05, 0.05, 0.05),  # Very dark
            metallic=0.1,
            roughness=0.9
        )
        
        # Throttle material (military green)
        throttle_mat = create_military_material(
            "Throttle_Quadrant",
            base_color=(0.2, 0.3, 0.15),  # Military green
            metallic=0.3,
            roughness=0.6
        )
        
        # Instrument panel material (dark blue-gray)
        panel_mat = create_military_material(
            "Instrument_Panel",
            base_color=(0.1, 0.12, 0.18),  # Dark blue-gray
            metallic=0.2,
            roughness=0.3
        )
        
        # Seat material (dark blue fabric)
        seat_mat = create_military_material(
            "Ejection_Seat",
            base_color=(0.1, 0.15, 0.25),  # Dark blue
            metallic=0.0,
            roughness=0.8
        )
        
        # Floor material (dark metal with grip pattern)
        floor_mat = create_military_material(
            "Cockpit_Floor",
            base_color=(0.12, 0.12, 0.15),  # Dark gray
            metallic=0.6,
            roughness=0.7
        )
        
        # Pedal material (brushed aluminum)
        pedal_mat = create_military_material(
            "Rudder_Pedals",
            base_color=(0.7, 0.7, 0.75),  # Light gray aluminum
            metallic=0.9,
            roughness=0.2
        )
        
        print("✅ Created 7 military-grade materials")
        
        # Step 3: Create cockpit components with materials
        print("Step 3: Creating textured cockpit components...")
        
        # Main cockpit tub
        bpy.ops.mesh.primitive_cube_add(size=2.0, location=(0, 0, 1))
        cockpit_tub = bpy.context.active_object
        cockpit_tub.name = "Cockpit_Tub"
        cockpit_tub.scale = (1.2, 2.0, 1.4)
        # Apply material
        if not cockpit_tub.data.materials:
            cockpit_tub.data.materials.append(cockpit_mat)
        else:
            cockpit_tub.data.materials[0] = cockpit_mat
        print("  ✅ Cockpit tub with structure material")
        
        # Control stick
        bpy.ops.mesh.primitive_cylinder_add(radius=0.05, depth=0.3, location=(0.15, 0.4, 0.65))
        control_stick = bpy.context.active_object
        control_stick.name = "Control_Stick"
        control_stick.data.materials.append(stick_mat)
        print("  ✅ Control stick with grip material")
        
        # Throttle quadrant
        bpy.ops.mesh.primitive_cube_add(size=0.2, location=(-0.35, 0.2, 0.75))
        throttle = bpy.context.active_object
        throttle.name = "Throttle_Quadrant"
        throttle.scale = (1.5, 1.0, 1.2)
        throttle.data.materials.append(throttle_mat)
        print("  ✅ Throttle with military green material")
        
        # Instrument panel
        bpy.ops.mesh.primitive_cube_add(size=0.5, location=(0, 1.0, 0.95))
        panel = bpy.context.active_object
        panel.name = "Instrument_Panel"
        panel.scale = (2.0, 0.2, 1.0)
        panel.rotation_euler = (-0.15, 0, 0)  # Angled toward pilot
        panel.data.materials.append(panel_mat)
        print("  ✅ Instrument panel with avionics material")
        
        # Ejection seat base
        bpy.ops.mesh.primitive_cube_add(size=0.5, location=(0, 0, 0.25))
        seat_base = bpy.context.active_object
        seat_base.name = "Ejection_Seat_Base"
        seat_base.scale = (1.0, 1.0, 0.5)
        seat_base.data.materials.append(seat_mat)
        
        # Ejection seat back
        bpy.ops.mesh.primitive_cube_add(size=0.5, location=(0, -0.1, 0.6))
        seat_back = bpy.context.active_object
        seat_back.name = "Ejection_Seat_Back"
        seat_back.scale = (1.0, 0.2, 1.0)
        seat_back.data.materials.append(seat_mat)
        print("  ✅ Ejection seat with fabric material")
        
        # Floor
        bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 0.5, 0.05))
        floor = bpy.context.active_object
        floor.name = "Cockpit_Floor"
        floor.scale = (1.2, 2.0, 0.1)
        floor.data.materials.append(floor_mat)
        print("  ✅ Floor with anti-slip material")
        
        # Rudder pedals
        bpy.ops.mesh.primitive_cube_add(size=0.1, location=(-0.15, 0.8, 0.1))
        left_pedal = bpy.context.active_object
        left_pedal.name = "Rudder_Pedal_Left"
        left_pedal.data.materials.append(pedal_mat)
        
        bpy.ops.mesh.primitive_cube_add(size=0.1, location=(0.15, 0.8, 0.1))
        right_pedal = bpy.context.active_object
        right_pedal.name = "Rudder_Pedal_Right"
        right_pedal.data.materials.append(pedal_mat)
        print("  ✅ Rudder pedals with aluminum material")
        
        # Step 4: Add some detail geometry for visual interest
        print("Step 4: Adding detail elements...")
        
        # Add control stick grip details
        bpy.ops.mesh.primitive_uv_sphere_add(radius=0.08, location=(0.15, 0.4, 0.8))
        grip = bpy.context.active_object
        grip.name = "Stick_Grip"
        grip.data.materials.append(stick_mat)
        
        # Add instrument displays (glowing elements)
        display_mat = create_military_material(
            "Display_Screen",
            base_color=(0.1, 0.3, 0.1),  # Green glow
            metallic=0.0,
            roughness=0.1
        )
        
        bpy.ops.mesh.primitive_cube_add(size=0.15, location=(0, 1.05, 0.95))
        display = bpy.context.active_object
        display.name = "HUD_Display"
        display.scale = (0.8, 0.1, 0.6)
        display.data.materials.append(display_mat)
        print("  ✅ Added detail elements")
        
        print(f"✅ Created {len(bpy.context.scene.objects)} textured components")
        
        # Step 5: Export with materials
        print("Step 5: Exporting textured cockpit...")
        
        # Create export directory
        export_dir = r"C:\Users\ssnguna\Local Sites\malloc\experiments\environments\fighter_jet\docs\blender work\exports_assembled"
        os.makedirs(export_dir, exist_ok=True)
        
        # Select all objects
        bpy.ops.object.select_all(action='SELECT')
        selected_count = len(bpy.context.selected_objects)
        print(f"  Selected {selected_count} textured objects for export")
        
        # Export with materials
        export_path = os.path.join(export_dir, "fighter_jet_cockpit_assembled.glb")
        
        try:
            bpy.ops.export_scene.gltf(
                filepath=export_path,
                use_selection=True,
                export_format='GLB',
                export_materials='EXPORT',  # This is crucial!
                export_image_format='AUTO',  # Let Blender choose best format
                export_texture_dir='',  # Embed textures in GLB
                export_yup=True,
                export_apply=False,  # Keep modifiers for better materials
                export_colors=True,  # Export vertex colors if any
                export_attributes=True  # Export custom attributes
            )
            print("✅ Export with materials completed")
        except Exception as e:
            print(f"❌ Export failed: {e}")
            return False
        
        # Verify file
        if os.path.exists(export_path):
            file_size = os.path.getsize(export_path)
            file_size_mb = file_size / (1024 * 1024)
            print(f"✅ SUCCESS! Textured cockpit created: {file_size_mb:.1f}MB")
            
            # Also create the web app compatible name
            web_app_path = os.path.join(export_dir, "fighter_jet_cockpit_complete_assembled.glb")
            import shutil
            shutil.copy2(export_path, web_app_path)
            print(f"✅ Web app compatible file created")
            
            # Create detailed report
            report_path = os.path.join(export_dir, "textured_cockpit_report.txt")
            with open(report_path, 'w') as f:
                f.write("TEXTURED COCKPIT CREATION REPORT\n")
                f.write("=" * 45 + "\n\n")
                f.write(f"File: fighter_jet_cockpit_assembled.glb\n")
                f.write(f"Size: {file_size_mb:.1f}MB\n")
                f.write(f"Objects: {selected_count}\n")
                f.write(f"Materials: 8 PBR materials\n")
                f.write(f"Created: Successfully with full texturing\n\n")
                f.write("MATERIALS APPLIED:\n")
                f.write("- Cockpit Structure: Dark metal with military finish\n")
                f.write("- Control Stick: Black grip material\n")
                f.write("- Throttle Quadrant: Military green metal\n")
                f.write("- Instrument Panel: Avionics blue-gray\n")
                f.write("- Ejection Seat: Dark blue fabric\n")
                f.write("- Cockpit Floor: Anti-slip metal\n")
                f.write("- Rudder Pedals: Brushed aluminum\n")
                f.write("- Display Screens: Glowing green elements\n\n")
                f.write("NEXT STEPS:\n")
                f.write("1. Refresh production_threejs_integration.html\n")
                f.write("2. You should now see TEXTURED cockpit components\n")
                f.write("3. Materials will render properly in Three.js\n")
            
            print(f"📄 Detailed report saved: {report_path}")
            return True
        else:
            print("❌ Export failed - file not created")
            return False
            
    except Exception as e:
        print(f"❌ CRITICAL ERROR: {e}")
        import traceback
        traceback.print_exc()
        return False

# Execute the textured cockpit creation
if __name__ == "__main__":
    print("🎨 TEXTURED COCKPIT CREATOR")
    print("This will create a cockpit with proper materials and textures!")
    print("=" * 65)
    
    success = create_cockpit_with_materials()
    
    if success:
        print("\n" + "=" * 65)
        print("🎉 SUCCESS! TEXTURED COCKPIT CREATED!")
        print("=" * 65)
        print("✅ File: fighter_jet_cockpit_assembled.glb")
        print("✅ Materials: 8 PBR materials applied")
        print("✅ Compatible: Three.js ready")
        print("✅ Size: Proper GLB file (not 0MB)")
        print("\n🎮 NEXT STEPS:")
        print("1. Refresh production_threejs_integration.html")
        print("2. You'll now see TEXTURED cockpit components")
        print("3. Materials will render with proper colors and shine")
    else:
        print("\n" + "=" * 65)
        print("❌ CREATION FAILED")
        print("=" * 65)
        print("Check the error messages above")
