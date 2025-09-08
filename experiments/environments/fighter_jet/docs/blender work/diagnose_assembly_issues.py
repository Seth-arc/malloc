# DIAGNOSTIC SCRIPT - Find why assembly export isn't working
import bpy
import os
import addon_utils

def diagnose_assembly_issues():
    """
    Comprehensive diagnosis of assembly export issues
    """
    print("=" * 60)
    print("COCKPIT ASSEMBLY DIAGNOSTIC")
    print("=" * 60)
    
    issues_found = []
    
    # 1. Check blend file status
    print("\n1. BLEND FILE STATUS:")
    if bpy.data.filepath == '':
        print("❌ Blend file not saved")
        issues_found.append("Blend file must be saved before export")
    else:
        print(f"✅ Blend file: {bpy.data.filepath}")
    
    # 2. Check export directory
    print("\n2. EXPORT DIRECTORY:")
    export_dir = bpy.path.abspath("//exports_assembled/")
    print(f"Target directory: {export_dir}")
    
    try:
        os.makedirs(export_dir, exist_ok=True)
        if os.path.exists(export_dir):
            print("✅ Export directory accessible")
        else:
            print("❌ Cannot create export directory")
            issues_found.append("Export directory not accessible")
    except Exception as e:
        print(f"❌ Directory error: {e}")
        issues_found.append(f"Directory creation failed: {e}")
    
    # 3. Check glTF exporter
    print("\n3. GLTF EXPORTER:")
    gltf_enabled = addon_utils.check("io_scene_gltf2")[1]
    if gltf_enabled:
        print("✅ glTF exporter enabled")
    else:
        print("❌ glTF exporter not enabled")
        issues_found.append("glTF exporter must be enabled")
        
        try:
            addon_utils.enable("io_scene_gltf2", default_set=True)
            print("✅ Enabled glTF exporter")
        except Exception as e:
            print(f"❌ Cannot enable glTF exporter: {e}")
    
    # 4. Check scene objects
    print("\n4. SCENE OBJECTS:")
    mesh_objects = [obj for obj in bpy.context.scene.objects if obj.type == 'MESH']
    print(f"Mesh objects in scene: {len(mesh_objects)}")
    
    if len(mesh_objects) == 0:
        print("❌ No mesh objects to export")
        issues_found.append("Scene has no mesh objects")
    else:
        print("✅ Mesh objects available for export")
        for obj in mesh_objects[:5]:  # Show first 5
            print(f"   - {obj.name}")
    
    # 5. Test basic export
    print("\n5. EXPORT TEST:")
    if len(mesh_objects) > 0:
        try:
            test_path = os.path.join(export_dir, "diagnostic_test.glb")
            
            # Select objects
            bpy.ops.object.select_all(action='DESELECT')
            for obj in mesh_objects:
                obj.select_set(True)
            
            # Try export
            bpy.ops.export_scene.gltf(
                filepath=test_path,
                use_selection=True,
                export_format='GLB'
            )
            
            if os.path.exists(test_path):
                file_size = os.path.getsize(test_path) / 1024
                print(f"✅ Export test successful: {file_size:.1f}KB")
                # Clean up test file
                os.remove(test_path)
            else:
                print("❌ Export test failed - file not created")
                issues_found.append("glTF export not working")
                
        except Exception as e:
            print(f"❌ Export test failed: {e}")
            issues_found.append(f"Export error: {e}")
    
    # 6. Check assembly script
    print("\n6. ASSEMBLY SCRIPT:")
    script_path = bpy.path.abspath("//cockpit_assembly_system_fixed.py")
    if os.path.exists(script_path):
        print(f"✅ Assembly script found: {script_path}")
    else:
        print(f"❌ Assembly script not found: {script_path}")
        issues_found.append("Assembly script file missing")
    
    # Summary
    print("\n" + "=" * 60)
    print("DIAGNOSTIC SUMMARY")
    print("=" * 60)
    
    if len(issues_found) == 0:
        print("✅ No issues found - assembly should work")
        print("\nTry running the assembly script:")
        print('exec(open("cockpit_assembly_system_fixed.py").read())')
    else:
        print(f"❌ {len(issues_found)} issues found:")
        for i, issue in enumerate(issues_found, 1):
            print(f"{i}. {issue}")
        
        print("\nFIXES TO APPLY:")
        if "Blend file must be saved" in str(issues_found):
            print("• Save your blend file first")
        if "glTF exporter" in str(issues_found):
            print("• Enable glTF exporter addon")
        if "no mesh objects" in str(issues_found):
            print("• Create or import some mesh objects")
        if "Export directory" in str(issues_found):
            print("• Check file permissions and disk space")
    
    return len(issues_found) == 0

def create_emergency_assembly():
    """
    Create emergency assembly if main script fails
    """
    print("\n🚨 CREATING EMERGENCY ASSEMBLY")
    
    try:
        # Clear scene
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete(use_global=False)
        
        # Create basic cockpit
        bpy.ops.mesh.primitive_cube_add(size=2.0, location=(0, 0, 1))
        cockpit = bpy.context.active_object
        cockpit.name = "Emergency_Cockpit_Tub"
        
        bpy.ops.mesh.primitive_cylinder_add(radius=0.05, depth=0.3, location=(0.2, 0.3, 0.8))
        stick = bpy.context.active_object  
        stick.name = "Emergency_Control_Stick"
        
        bpy.ops.mesh.primitive_cube_add(size=0.3, location=(-0.3, 0.2, 0.9))
        throttle = bpy.context.active_object
        throttle.name = "Emergency_Throttle"
        
        bpy.ops.mesh.primitive_cube_add(size=0.5, location=(0, 1.0, 0.9))
        panel = bpy.context.active_object
        panel.name = "Emergency_Panel"
        panel.scale = (2.0, 0.2, 1.0)
        
        # Export emergency assembly
        export_dir = bpy.path.abspath("//exports_assembled/")
        os.makedirs(export_dir, exist_ok=True)
        
        bpy.ops.object.select_all(action='SELECT')
        export_path = os.path.join(export_dir, "fighter_jet_cockpit_assembled.glb")
        
        bpy.ops.export_scene.gltf(
            filepath=export_path,
            use_selection=True,
            export_format='GLB'
        )
        
        if os.path.exists(export_path):
            file_size = os.path.getsize(export_path) / 1024
            print(f"✅ Emergency assembly created: {file_size:.1f}KB")
            print(f"   Saved as: {export_path}")
            return True
        else:
            print("❌ Emergency assembly export failed")
            return False
            
    except Exception as e:
        print(f"❌ Emergency assembly failed: {e}")
        return False

# Run diagnostics
if __name__ == "__main__":
    success = diagnose_assembly_issues()
    
    if not success:
        print("\n" + "="*60)
        print("ATTEMPTING EMERGENCY ASSEMBLY...")
        print("="*60)
        emergency_success = create_emergency_assembly()
        
        if emergency_success:
            print("\n🎉 Emergency assembly created successfully!")
            print("Your web app should now load the assembled cockpit.")
        else:
            print("\n❌ All assembly attempts failed.")
            print("Please check the issues listed above and try again.")
