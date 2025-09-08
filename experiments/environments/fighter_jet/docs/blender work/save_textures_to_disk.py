# Save Phase 3 Textures to Disk
import bpy
import os

def save_all_phase3_textures():
    """
    Save all Phase 3 generated textures to disk
    """
    # Create textures directory
    textures_dir = bpy.path.abspath("//textures/")
    os.makedirs(textures_dir, exist_ok=True)
    
    saved_count = 0
    
    # Save all generated textures
    for img in bpy.data.images:
        # Check if it's a Phase 3 generated texture
        if any(asset in img.name for asset in ['Control_Stick_Hero', 'Throttle_Quadrant_Hero', 'Instrument_Panel_Hero']):
            # Set file path and format
            img.filepath_raw = os.path.join(textures_dir, f"{img.name}.png")
            img.file_format = 'PNG'
            
            # Save the image
            img.save()
            saved_count += 1
            print(f"Saved: {img.name}.png")
    
    print(f"\n✅ Saved {saved_count} textures to: {textures_dir}")

# Execute if run directly
if __name__ == "__main__":
    save_all_phase3_textures()
