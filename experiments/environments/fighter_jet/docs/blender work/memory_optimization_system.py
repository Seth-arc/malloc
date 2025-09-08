# MEMORY OPTIMIZATION AND TEXTURE COMPRESSION SYSTEM
# Critical fix for 19GB -> 2GB memory budget compliance

import bpy
import bmesh
import os
import json
import time
from mathutils import Vector
import shutil

class MemoryOptimizationSystem:
    """
    Comprehensive memory optimization system to fix critical memory budget issues
    Target: Reduce from 19GB to under 2GB total memory usage
    """
    
    def __init__(self):
        self.memory_budget = {
            'total_limit_mb': 2048,  # 2GB total limit
            'texture_limit_mb': 1536,  # 1.5GB for textures
            'geometry_limit_mb': 512   # 512MB for geometry
        }
        
        self.compression_settings = {
            'hero_lod': {'max_texture_size': 1024, 'quality': 0.85},
            'high_lod': {'max_texture_size': 512, 'quality': 0.75},
            'medium_lod': {'max_texture_size': 256, 'quality': 0.65},
            'low_lod': {'max_texture_size': 128, 'quality': 0.55}
        }
        
        self.optimization_results = {}
        
    def run_complete_memory_optimization(self):
        """
        Run complete memory optimization pipeline
        """
        print("=" * 60)
        print("CRITICAL MEMORY OPTIMIZATION - FIXING 19GB BUDGET ISSUE")
        print("=" * 60)
        
        # Step 1: Analyze current memory usage
        current_usage = self.analyze_current_memory_usage()
        print(f"Current memory usage: {current_usage['total_mb']:.1f}MB")
        
        if current_usage['total_mb'] <= self.memory_budget['total_limit_mb']:
            print("✅ Memory budget already compliant")
            return True
            
        # Step 2: Aggressive texture optimization
        texture_savings = self.optimize_all_textures()
        
        # Step 3: Geometry optimization
        geometry_savings = self.optimize_geometry_memory()
        
        # Step 4: Remove unused assets
        cleanup_savings = self.cleanup_unused_assets()
        
        # Step 5: Implement texture streaming
        self.implement_texture_streaming()
        
        # Step 6: Final validation
        final_usage = self.analyze_current_memory_usage()
        
        total_savings = current_usage['total_mb'] - final_usage['total_mb']
        
        print(f"\n🎯 OPTIMIZATION RESULTS:")
        print(f"Initial Memory: {current_usage['total_mb']:.1f}MB")
        print(f"Final Memory: {final_usage['total_mb']:.1f}MB")
        print(f"Total Savings: {total_savings:.1f}MB ({(total_savings/current_usage['total_mb'])*100:.1f}%)")
        
        if final_usage['total_mb'] <= self.memory_budget['total_limit_mb']:
            print("✅ MEMORY BUDGET COMPLIANCE ACHIEVED!")
            return True
        else:
            print("❌ Still over budget - implementing emergency optimization")
            return self.emergency_optimization()
    
    def analyze_current_memory_usage(self):
        """
        Analyze current memory usage across all assets
        """
        usage = {
            'textures_mb': 0,
            'geometry_mb': 0,
            'total_mb': 0,
            'texture_breakdown': {},
            'geometry_breakdown': {}
        }
        
        # Analyze texture memory
        for image in bpy.data.images:
            if image.size[0] > 0 and image.size[1] > 0:
                # Calculate memory: width * height * 4 bytes (RGBA) / 1024^2
                texture_mb = (image.size[0] * image.size[1] * 4) / (1024 * 1024)
                usage['textures_mb'] += texture_mb
                usage['texture_breakdown'][image.name] = texture_mb
        
        # Analyze geometry memory
        for obj in bpy.data.objects:
            if obj.type == 'MESH' and obj.data:
                # Estimate geometry memory
                mesh_data = obj.data
                vertex_count = len(mesh_data.vertices)
                face_count = len(mesh_data.polygons)
                
                # Approximate memory: vertices * 32 bytes + faces * 16 bytes
                geometry_mb = ((vertex_count * 32) + (face_count * 16)) / (1024 * 1024)
                usage['geometry_mb'] += geometry_mb
                usage['geometry_breakdown'][obj.name] = geometry_mb
        
        usage['total_mb'] = usage['textures_mb'] + usage['geometry_mb']
        
        return usage
    
    def optimize_all_textures(self):
        """
        Aggressively optimize all textures to meet memory budget
        """
        print("\n🔧 Optimizing textures for memory compliance...")
        
        total_savings = 0
        processed_textures = 0
        
        # Create optimized texture directory
        optimized_dir = bpy.path.abspath("//textures_optimized/")
        os.makedirs(optimized_dir, exist_ok=True)
        
        for image in bpy.data.images:
            if image.size[0] > 0 and image.size[1] > 0:
                original_mb = (image.size[0] * image.size[1] * 4) / (1024 * 1024)
                
                # Determine optimization level based on usage
                optimization_level = self.determine_texture_optimization_level(image)
                
                # Apply optimization
                savings = self.optimize_individual_texture(image, optimization_level, optimized_dir)
                total_savings += savings
                processed_textures += 1
                
                print(f"  Optimized {image.name}: {savings:.1f}MB saved")
        
        print(f"✅ Texture optimization complete: {total_savings:.1f}MB saved from {processed_textures} textures")
        return total_savings
    
    def determine_texture_optimization_level(self, image):
        """
        Determine appropriate optimization level for texture
        """
        # Check which objects use this texture
        usage_priority = 'low'  # Default to aggressive optimization
        
        for material in bpy.data.materials:
            if material.use_nodes:
                for node in material.node_tree.nodes:
                    if node.type == 'TEX_IMAGE' and node.image == image:
                        # Check material usage on objects
                        for obj in bpy.data.objects:
                            if obj.type == 'MESH' and obj.data and obj.data.materials:
                                if material in obj.data.materials:
                                    # Determine priority based on object name
                                    if 'hero' in obj.name.lower():
                                        usage_priority = 'hero_lod'
                                    elif 'high' in obj.name.lower():
                                        usage_priority = 'high_lod'
                                    elif 'medium' in obj.name.lower():
                                        usage_priority = 'medium_lod'
                                    else:
                                        usage_priority = 'low_lod'
                                    break
        
        return usage_priority
    
    def optimize_individual_texture(self, image, optimization_level, output_dir):
        """
        Optimize individual texture based on level
        """
        settings = self.compression_settings[optimization_level]
        original_mb = (image.size[0] * image.size[1] * 4) / (1024 * 1024)
        
        # Calculate target size
        current_size = max(image.size[0], image.size[1])
        target_size = min(current_size, settings['max_texture_size'])
        
        if target_size < current_size:
            # Resize texture
            scale_factor = target_size / current_size
            new_width = int(image.size[0] * scale_factor)
            new_height = int(image.size[1] * scale_factor)
            
            # Create new optimized image
            image.scale(new_width, new_height)
            
            # Save optimized version
            optimized_path = os.path.join(output_dir, f"{image.name}_optimized.png")
            image.save_render(optimized_path)
            
            new_mb = (new_width * new_height * 4) / (1024 * 1024)
            savings = original_mb - new_mb
            
            print(f"    Resized {image.name}: {image.size[0]}x{image.size[1]} -> {new_width}x{new_height}")
            
            return savings
        
        return 0
    
    def optimize_geometry_memory(self):
        """
        Optimize geometry memory usage
        """
        print("\n🔧 Optimizing geometry memory...")
        
        total_savings = 0
        
        for obj in bpy.data.objects:
            if obj.type == 'MESH' and obj.data:
                original_vertices = len(obj.data.vertices)
                original_faces = len(obj.data.polygons)
                
                # Apply optimization based on object priority
                if self.is_low_priority_object(obj):
                    savings = self.apply_geometry_optimization(obj)
                    total_savings += savings
        
        print(f"✅ Geometry optimization complete: {total_savings:.1f}MB saved")
        return total_savings
    
    def is_low_priority_object(self, obj):
        """
        Determine if object can be aggressively optimized
        """
        low_priority_keywords = ['low', 'medium', 'background', 'detail', 'secondary']
        
        for keyword in low_priority_keywords:
            if keyword in obj.name.lower():
                return True
        
        return False
    
    def apply_geometry_optimization(self, obj):
        """
        Apply geometry optimization to object
        """
        original_memory = self.calculate_mesh_memory(obj.data)
        
        # Set active object
        bpy.context.view_layer.objects.active = obj
        
        # Enter Edit Mode
        bpy.ops.object.mode_set(mode='EDIT')
        
        # Select all
        bpy.ops.mesh.select_all(action='SELECT')
        
        # Limited dissolve to reduce geometry
        bpy.ops.mesh.dissolve_limited(angle_limit=0.1)
        
        # Remove doubles
        bpy.ops.mesh.remove_doubles(threshold=0.001)
        
        # Return to Object Mode
        bpy.ops.object.mode_set(mode='OBJECT')
        
        new_memory = self.calculate_mesh_memory(obj.data)
        savings = original_memory - new_memory
        
        return savings
    
    def calculate_mesh_memory(self, mesh_data):
        """
        Calculate approximate mesh memory usage
        """
        vertex_count = len(mesh_data.vertices)
        face_count = len(mesh_data.polygons)
        
        # Approximate memory calculation
        memory_mb = ((vertex_count * 32) + (face_count * 16)) / (1024 * 1024)
        return memory_mb
    
    def cleanup_unused_assets(self):
        """
        Remove unused assets to free memory
        """
        print("\n🔧 Cleaning up unused assets...")
        
        initial_count = {
            'images': len(bpy.data.images),
            'materials': len(bpy.data.materials),
            'meshes': len(bpy.data.meshes)
        }
        
        # Remove unused data blocks
        bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)
        
        final_count = {
            'images': len(bpy.data.images),
            'materials': len(bpy.data.materials),
            'meshes': len(bpy.data.meshes)
        }
        
        cleaned_images = initial_count['images'] - final_count['images']
        cleaned_materials = initial_count['materials'] - final_count['materials']
        cleaned_meshes = initial_count['meshes'] - final_count['meshes']
        
        print(f"✅ Cleanup complete:")
        print(f"  Removed {cleaned_images} unused images")
        print(f"  Removed {cleaned_materials} unused materials")
        print(f"  Removed {cleaned_meshes} unused meshes")
        
        # Estimate savings (approximate)
        estimated_savings = (cleaned_images * 5) + (cleaned_materials * 0.1) + (cleaned_meshes * 2)
        return estimated_savings
    
    def implement_texture_streaming(self):
        """
        Implement texture streaming system for memory efficiency
        """
        print("\n🔧 Implementing texture streaming system...")
        
        # Create texture streaming configuration
        streaming_config = {
            'enable_streaming': True,
            'max_loaded_textures': 10,
            'texture_cache_mb': 256,
            'lod_switching_distance': [2, 5, 15, 50],
            'streaming_manifest': []
        }
        
        # Generate streaming manifest
        for image in bpy.data.images:
            if image.size[0] > 0:
                texture_info = {
                    'name': image.name,
                    'size_mb': (image.size[0] * image.size[1] * 4) / (1024 * 1024),
                    'dimensions': [image.size[0], image.size[1]],
                    'priority': self.determine_texture_priority(image)
                }
                streaming_config['streaming_manifest'].append(texture_info)
        
        # Sort by priority for streaming order
        streaming_config['streaming_manifest'].sort(key=lambda x: x['priority'], reverse=True)
        
        # Save streaming configuration
        config_path = bpy.path.abspath("//texture_streaming_config.json")
        with open(config_path, 'w') as f:
            json.dump(streaming_config, f, indent=2)
        
        print(f"✅ Texture streaming configuration saved: {config_path}")
        
    def determine_texture_priority(self, image):
        """
        Determine texture loading priority
        """
        priority_score = 1.0
        
        # Hero assets get highest priority
        if 'hero' in image.name.lower():
            priority_score = 10.0
        elif 'high' in image.name.lower():
            priority_score = 7.0
        elif 'medium' in image.name.lower():
            priority_score = 4.0
        elif 'low' in image.name.lower():
            priority_score = 1.0
        
        return priority_score
    
    def emergency_optimization(self):
        """
        Emergency optimization if still over budget
        """
        print("\n🚨 EMERGENCY OPTIMIZATION - AGGRESSIVE MEMORY REDUCTION")
        
        # Further reduce texture sizes
        for image in bpy.data.images:
            if image.size[0] > 256 or image.size[1] > 256:
                new_size = min(256, max(image.size[0], image.size[1]))
                scale_factor = new_size / max(image.size[0], image.size[1])
                new_width = max(64, int(image.size[0] * scale_factor))
                new_height = max(64, int(image.size[1] * scale_factor))
                
                image.scale(new_width, new_height)
                print(f"  Emergency resize: {image.name} -> {new_width}x{new_height}")
        
        # Apply more aggressive geometry optimization
        for obj in bpy.data.objects:
            if obj.type == 'MESH' and len(obj.data.vertices) > 1000:
                # Apply decimate modifier
                decimate = obj.modifiers.new(name="EmergencyDecimate", type='DECIMATE')
                decimate.ratio = 0.5
                decimate.use_collapse_triangulate = True
                
                bpy.context.view_layer.objects.active = obj
                bpy.ops.object.modifier_apply(modifier=decimate.name)
                
                print(f"  Emergency decimation: {obj.name}")
        
        # Final check
        final_usage = self.analyze_current_memory_usage()
        
        if final_usage['total_mb'] <= self.memory_budget['total_limit_mb']:
            print("✅ EMERGENCY OPTIMIZATION SUCCESSFUL!")
            return True
        else:
            print("❌ Unable to meet memory budget - manual intervention required")
            return False
    
    def generate_optimization_report(self):
        """
        Generate optimization report
        """
        report_path = bpy.path.abspath("//memory_optimization_report.txt")
        
        with open(report_path, 'w') as f:
            f.write("MEMORY OPTIMIZATION REPORT\n")
            f.write("=" * 50 + "\n\n")
            
            usage = self.analyze_current_memory_usage()
            
            f.write(f"Current Memory Usage: {usage['total_mb']:.1f}MB\n")
            f.write(f"Budget Compliance: {'✅ PASS' if usage['total_mb'] <= self.memory_budget['total_limit_mb'] else '❌ FAIL'}\n")
            f.write(f"Budget Limit: {self.memory_budget['total_limit_mb']}MB\n\n")
            
            f.write("TEXTURE BREAKDOWN:\n")
            f.write("-" * 30 + "\n")
            for name, size in usage['texture_breakdown'].items():
                f.write(f"{name}: {size:.1f}MB\n")
            
            f.write(f"\nTotal Texture Memory: {usage['textures_mb']:.1f}MB\n")
            f.write(f"Total Geometry Memory: {usage['geometry_mb']:.1f}MB\n")
        
        print(f"📄 Optimization report saved: {report_path}")

# Usage function
def fix_memory_budget():
    """
    Fix critical memory budget issue
    """
    optimizer = MemoryOptimizationSystem()
    success = optimizer.run_complete_memory_optimization()
    optimizer.generate_optimization_report()
    
    return success

if __name__ == "__main__":
    success = fix_memory_budget()
    if success:
        print("🎉 MEMORY BUDGET COMPLIANCE ACHIEVED!")
    else:
        print("⚠️ Manual intervention required for memory optimization")
