# FILE CHECKER - See what files actually exist
import os

def check_project_files():
    """
    Check which files exist in the project
    """
    print("=" * 60)
    print("FIGHTER JET COCKPIT - FILE STATUS CHECK")
    print("=" * 60)
    
    base_path = r"C:\Users\ssnguna\Local Sites\malloc\experiments\environments\fighter_jet\docs\blender work"
    
    # Files the web app is looking for
    files_to_check = [
        ("exports_assembled/fighter_jet_cockpit_complete_assembled.glb", "Complete assembled cockpit"),
        ("exports_assembled/fighter_jet_cockpit_assembled.glb", "Basic assembled cockpit"),
        ("exports_assembled/basic_cockpit_fallback.glb", "Fallback cockpit"),
        ("exports/hero/fighter_cockpit_hero.glb", "Hero quality structure"),
        ("exports/hero/control_stick_hero_hero.glb", "Hero control stick"),
        ("exports/hero/throttle_quadrant_hero_hero.glb", "Hero throttle"),
        ("exports/hero/instrument_panel_hero_hero.glb", "Hero instrument panel"),
        ("production_threejs_integration.html", "Web application"),
        ("cockpit_assembly_system_fixed.py", "Assembly script"),
        ("diagnose_assembly_issues.py", "Diagnostic script")
    ]
    
    print("\nFILE STATUS:")
    print("-" * 40)
    
    existing_files = []
    missing_files = []
    
    for file_path, description in files_to_check:
        full_path = os.path.join(base_path, file_path)
        if os.path.exists(full_path):
            file_size = os.path.getsize(full_path)
            size_mb = file_size / (1024 * 1024)
            print(f"✅ {description}")
            print(f"   {file_path} ({size_mb:.1f}MB)")
            existing_files.append(file_path)
        else:
            print(f"❌ {description}")
            print(f"   {file_path} (MISSING)")
            missing_files.append(file_path)
        print()
    
    # Check directories
    print("DIRECTORY STATUS:")
    print("-" * 40)
    
    directories = [
        "exports_assembled",
        "exports/hero",
        "exports/high", 
        "exports/medium",
        "exports/low"
    ]
    
    for directory in directories:
        dir_path = os.path.join(base_path, directory)
        if os.path.exists(dir_path):
            files_in_dir = len([f for f in os.listdir(dir_path) if f.endswith('.glb')])
            print(f"✅ {directory}/ ({files_in_dir} .glb files)")
        else:
            print(f"❌ {directory}/ (MISSING)")
    
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    
    print(f"Existing files: {len(existing_files)}")
    print(f"Missing files: {len(missing_files)}")
    
    if "exports_assembled/fighter_jet_cockpit_assembled.glb" in missing_files:
        print("\n🔧 TO FIX WEB APP LOADING:")
        print("1. Open Blender 4.4")
        print("2. Run: exec(open('diagnose_assembly_issues.py').read())")
        print("3. This will create the missing assembled cockpit file")
        print("4. Refresh the web page")
    
    if len(existing_files) >= len(missing_files):
        print("\n✅ PROJECT STATUS: GOOD")
        print("Most files exist - minor fixes needed")
    else:
        print("\n⚠️ PROJECT STATUS: NEEDS WORK") 
        print("Many files missing - run assembly scripts")
    
    return existing_files, missing_files

if __name__ == "__main__":
    existing, missing = check_project_files()
    
    print(f"\n📁 EXISTING FILES ({len(existing)}):")
    for file in existing:
        print(f"  • {file}")
    
    if missing:
        print(f"\n❌ MISSING FILES ({len(missing)}):")
        for file in missing:
            print(f"  • {file}")
    
    print("\n🎯 NEXT STEPS:")
    print("1. Run this file checker to see current status")
    print("2. Run diagnostic script in Blender to create missing files")
    print("3. Test web app again")
