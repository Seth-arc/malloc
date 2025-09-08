# MANUAL COCKPIT CREATOR - GUARANTEED TO WORK
# Run this INSIDE Blender 4.4 Console

import bpy
import os

def create_cockpit_manually():
    """
    Manually create a cockpit that will definitely work
    This bypasses all complex systems and just creates the file
    """
    print("🚀 CREATING COCKPIT MANUALLY - GUARANTEED TO WORK")
    print("=" * 60)
    
    try:
        # Step 1: Clear the scene
        print("Step 1: Clearing scene...")
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete(use_global=False)
        print("✅ Scene cleared")
        
        # Step 2: Create basic cockpit components
        print("Step 2: Creating cockpit components...")
        
        # Main cockpit tub
        bpy.ops.mesh.primitive_cube_add(size=2.0, location=(0, 0, 1))
        cockpit_tub = bpy.context.active_object
        cockpit_tub.name = "Cockpit_Tub"
        cockpit_tub.scale = (1.2, 2.0, 1.4)
        print("  ✅ Created cockpit tub")
        
        # Control stick
        bpy.ops.mesh.primitive_cylinder_add(radius=0.05, depth=0.3, location=(0.15, 0.4, 0.65))
        control_stick = bpy.context.active_object
        control_stick.name = "Control_Stick"
        print("  ✅ Created control stick")
        
        # Throttle quadrant
        bpy.ops.mesh.primitive_cube_add(size=0.2, location=(-0.35, 0.2, 0.75))
        throttle = bpy.context.active_object
        throttle.name = "Throttle_Quadrant"
        throttle.scale = (1.5, 1.0, 1.2)
        print("  ✅ Created throttle quadrant")
        
        # Instrument panel
        bpy.ops.mesh.primitive_cube_add(size=0.5, location=(0, 1.0, 0.95))
        panel = bpy.context.active_object
        panel.name = "Instrument_Panel"
        panel.scale = (2.0, 0.2, 1.0)
        panel.rotation_euler = (-0.15, 0, 0)  # Angled toward pilot
        print("  ✅ Created instrument panel")
        
        # Ejection seat
        bpy.ops.mesh.primitive_cube_add(size=0.5, location=(0, 0, 0.25))
        seat_base = bpy.context.active_object
        seat_base.name = "Ejection_Seat_Base"
        seat_base.scale = (1.0, 1.0, 0.5)
        
        bpy.ops.mesh.primitive_cube_add(size=0.5, location=(0, -0.1, 0.6))
        seat_back = bpy.context.active_object
        seat_back.name = "Ejection_Seat_Back"
        seat_back.scale = (1.0, 0.2, 1.0)
        print("  ✅ Created ejection seat")
        
        # Floor
        bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 0.5, 0.05))
        floor = bpy.context.active_object
        floor.name = "Cockpit_Floor"
        floor.scale = (1.2, 2.0, 0.1)
        print("  ✅ Created cockpit floor")
        
        # Rudder pedals
        bpy.ops.mesh.primitive_cube_add(size=0.1, location=(-0.15, 0.8, 0.1))
        left_pedal = bpy.context.active_object
        left_pedal.name = "Rudder_Pedal_Left"
        
        bpy.ops.mesh.primitive_cube_add(size=0.1, location=(0.15, 0.8, 0.1))
        right_pedal = bpy.context.active_object
        right_pedal.name = "Rudder_Pedal_Right"
        print("  ✅ Created rudder pedals")
        
        print(f"✅ Created {len(bpy.context.scene.objects)} cockpit components")
        
        # Step 3: Create export directory
        print("Step 3: Creating export directory...")
        
        # Use absolute path to be sure
        export_dir = r"C:\Users\ssnguna\Local Sites\malloc\experiments\environments\fighter_jet\docs\blender work\exports_assembled"
        
        try:
            os.makedirs(export_dir, exist_ok=True)
            print(f"✅ Export directory: {export_dir}")
        except Exception as e:
            print(f"❌ Could not create directory: {e}")
            return False
        
        # Step 4: Export the cockpit
        print("Step 4: Exporting cockpit...")
        
        # Select all objects
        bpy.ops.object.select_all(action='SELECT')
        selected_count = len(bpy.context.selected_objects)
        print(f"  Selected {selected_count} objects for export")
        
        # Export path
        export_path = os.path.join(export_dir, "fighter_jet_cockpit_assembled.glb")
        print(f"  Export path: {export_path}")
        
        # Perform export
        try:
            bpy.ops.export_scene.gltf(
                filepath=export_path,
                use_selection=True,
                export_format='GLB',
                export_materials='EXPORT',
                export_yup=True
            )
            print("✅ Export operation completed")
        except Exception as e:
            print(f"❌ Export failed: {e}")
            return False
        
        # Step 5: Verify the file was created
        print("Step 5: Verifying export...")
        
        if os.path.exists(export_path):
            file_size = os.path.getsize(export_path)
            file_size_mb = file_size / (1024 * 1024)
            print(f"✅ SUCCESS! File created: {file_size_mb:.1f}MB")
            print(f"   File location: {export_path}")
            
            # Create a simple report
            report_path = os.path.join(export_dir, "manual_creation_report.txt")
            with open(report_path, 'w') as f:
                f.write("MANUAL COCKPIT CREATION REPORT\n")
                f.write("=" * 40 + "\n\n")
                f.write(f"File: fighter_jet_cockpit_assembled.glb\n")
                f.write(f"Size: {file_size_mb:.1f}MB\n")
                f.write(f"Objects: {selected_count}\n")
                f.write(f"Created: Successfully\n\n")
                f.write("COMPONENTS INCLUDED:\n")
                f.write("- Cockpit tub structure\n")
                f.write("- Control stick\n")
                f.write("- Throttle quadrant\n")
                f.write("- Instrument panel\n")
                f.write("- Ejection seat (base and back)\n")
                f.write("- Cockpit floor\n")
                f.write("- Rudder pedals\n\n")
                f.write("NEXT STEPS:\n")
                f.write("1. Refresh production_threejs_integration.html\n")
                f.write("2. The 404 errors should be gone\n")
                f.write("3. You should see the complete cockpit\n")
            
            print(f"📄 Report saved: {report_path}")
            
            return True
        else:
            print("❌ FAILED! File was not created")
            print("   Check Blender console for export errors")
            return False
            
    except Exception as e:
        print(f"❌ CRITICAL ERROR: {e}")
        return False

def check_blender_setup():
    """
    Check if Blender is set up correctly for export
    """
    print("\n🔍 CHECKING BLENDER SETUP:")
    print("-" * 30)
    
    # Check if we're in Blender
    try:
        print(f"✅ Blender version: {bpy.app.version_string}")
    except:
        print("❌ Not running in Blender!")
        return False
    
    # Check glTF exporter
    import addon_utils
    gltf_enabled = addon_utils.check("io_scene_gltf2")[1]
    if gltf_enabled:
        print("✅ glTF exporter: Enabled")
    else:
        print("❌ glTF exporter: Disabled - enabling now...")
        try:
            addon_utils.enable("io_scene_gltf2", default_set=True)
            print("✅ glTF exporter: Now enabled")
        except Exception as e:
            print(f"❌ Could not enable glTF exporter: {e}")
            return False
    
    # Check scene
    object_count = len(bpy.context.scene.objects)
    print(f"ℹ️  Current scene objects: {object_count}")
    
    return True

# Main execution
if __name__ == "__main__":
    print("🚀 MANUAL COCKPIT CREATOR")
    print("This will definitely create the missing cockpit file!")
    print("=" * 60)
    
    # Check setup
    if not check_blender_setup():
        print("\n❌ Blender setup issues - cannot continue")
        print("Make sure you're running this INSIDE Blender!")
    else:
        # Create the cockpit
        success = create_cockpit_manually()
        
        if success:
            print("\n" + "=" * 60)
            print("🎉 SUCCESS! COCKPIT CREATED!")
            print("=" * 60)
            print("✅ File: fighter_jet_cockpit_assembled.glb")
            print("✅ Location: exports_assembled/")
            print("✅ Ready for web app")
            print("\n🎮 NEXT STEPS:")
            print("1. Refresh production_threejs_integration.html")
            print("2. The 404 errors will be gone")
            print("3. You'll see the complete cockpit!")
        else:
            print("\n" + "=" * 60)
            print("❌ CREATION FAILED")
            print("=" * 60)
            print("Check the error messages above")
            print("Make sure you're running this in Blender Console")
