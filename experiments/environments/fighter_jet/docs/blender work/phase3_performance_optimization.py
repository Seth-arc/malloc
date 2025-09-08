# BLENDER PHASE 3.2: PERFORMANCE OPTIMIZATION AND LOD SYSTEM
# Complete implementation for Blender 4.4 Performance Optimization

import bpy
import bmesh
import mathutils
from mathutils import Vector
import os
import math

class PerformanceOptimizationSystem:
    """
    Comprehensive performance optimization system for web delivery
    Implements Phase 3.2 requirements from BLENDER_PHASE_03_Texturing_and_Optimization.md
    """
    
    def __init__(self):
        self.lod_configurations = {}
        self.optimization_metrics = {}
        self.export_settings = {}
        self.performance_targets = {
            'hero_triangles': 100000,
            'high_triangles': 75000,
            'medium_triangles': 50000,
            'low_triangles': 25000,
            'texture_memory_mb': 2048,
            'export_size_mb': 50
        }
        
    def create_complete_lod_system(self):
        """
        Create complete LOD system for all cockpit assets
        """
        print("=== PHASE 3.2: PERFORMANCE OPTIMIZATION AND LOD SYSTEM ===")
        print("Creating comprehensive LOD system...")
        
        # Get all hero assets
        hero_assets = [obj for obj in bpy.context.scene.objects 
                      if obj.type == 'MESH' and 'Hero' in obj.name]
        
        if not hero_assets:
            print("⚠️  No hero assets found for LOD generation")
            return {}
        
        for asset in hero_assets:
            self.create_asset_lod_chain(asset)
        
        # Validate LOD system performance
        self.validate_lod_system_performance()
        
        # Generate optimization report
        self.generate_optimization_report()
        
        print("LOD system creation completed")
        return self.lod_configurations
    
    def create_asset_lod_chain(self, hero_asset):
        """
        Create complete LOD chain for hero asset
        """
        print(f"Creating LOD chain for {hero_asset.name}")
        
        lod_chain = {
            'hero_asset': hero_asset,
            'lod_levels': {},
            'triangle_counts': {},
            'memory_usage': {},
            'quality_scores': {}
        }
        
        # Create each LOD level
        lod_levels = [
            ('LOD0', 1.0, 4096),    # Hero quality
            ('LOD1', 0.75, 2048),   # High quality  
            ('LOD2', 0.5, 1024),    # Medium quality
            ('LOD3', 0.25, 512)     # Low quality
        ]
        
        for lod_name, detail_ratio, texture_resolution in lod_levels:
            lod_object = self.create_lod_level(hero_asset, lod_name, detail_ratio, texture_resolution)
            lod_chain['lod_levels'][lod_name] = lod_object
            
            # Calculate metrics
            triangle_count = self.calculate_triangle_count(lod_object)
            memory_usage = self.calculate_memory_usage(lod_object, texture_resolution)
            quality_score = self.calculate_quality_score(lod_object, hero_asset)
            
            lod_chain['triangle_counts'][lod_name] = triangle_count
            lod_chain['memory_usage'][lod_name] = memory_usage
            lod_chain['quality_scores'][lod_name] = quality_score
            
            print(f"  {lod_name}: {triangle_count} triangles, {memory_usage:.1f}MB, Quality: {quality_score}/100")
        
        self.lod_configurations[hero_asset.name] = lod_chain
        return lod_chain
    
    def create_lod_level(self, hero_asset, lod_name, detail_ratio, texture_resolution):
        """
        Create specific LOD level from hero asset
        """
        # Duplicate hero asset
        lod_object = hero_asset.copy()
        lod_object.data = hero_asset.data.copy()
        lod_object.name = f"{hero_asset.name}_{lod_name}"
        
        # Link to scene
        bpy.context.collection.objects.link(lod_object)
        
        # Apply geometry optimization
        self.optimize_geometry_for_lod(lod_object, detail_ratio)
        
        # Optimize textures for LOD level
        self.optimize_textures_for_lod(lod_object, texture_resolution)
        
        # Optimize materials for LOD level
        self.optimize_materials_for_lod(lod_object, lod_name)
        
        return lod_object
    
    def optimize_geometry_for_lod(self, lod_object, detail_ratio):
        """
        Optimize geometry for specific LOD level
        """
        # Set active object
        bpy.context.view_layer.objects.active = lod_object
        
        # Add Decimate modifier for triangle reduction
        decimate = lod_object.modifiers.new(name="LOD_Decimate", type='DECIMATE')
        decimate.decimate_type = 'COLLAPSE'
        decimate.ratio = detail_ratio
        decimate.use_collapse_triangulate = True
        
        # Configure decimate settings based on detail ratio
        if detail_ratio >= 0.75:
            # High quality - preserve important details
            decimate.vertex_group_factor = 0.5
            decimate.use_symmetry = True
        elif detail_ratio >= 0.5:
            # Medium quality - balanced optimization
            decimate.vertex_group_factor = 1.0
            decimate.use_symmetry = True
        else:
            # Low quality - aggressive optimization
            decimate.vertex_group_factor = 2.0
            decimate.use_symmetry = False
        
        # Apply modifier
        bpy.ops.object.modifier_apply(modifier="LOD_Decimate")
        
        # Clean up geometry
        self.clean_lod_geometry(lod_object)
    
    def clean_lod_geometry(self, lod_object):
        """
        Clean up LOD geometry for optimal performance
        """
        # Enter Edit Mode
        bpy.context.view_layer.objects.active = lod_object
        bpy.ops.object.mode_set(mode='EDIT')
        
        # Select all geometry
        bpy.ops.mesh.select_all(action='SELECT')
        
        # Remove doubles
        bpy.ops.mesh.remove_doubles(threshold=0.001)
        
        # Recalculate normals
        bpy.ops.mesh.normals_make_consistent(inside=False)
        
        # Triangulate for consistent export
        bpy.ops.mesh.quads_convert_to_tris()
        
        # Return to Object Mode
        bpy.ops.object.mode_set(mode='OBJECT')
    
    def optimize_textures_for_lod(self, lod_object, target_resolution):
        """
        Optimize textures for LOD level
        """
        # Process all materials on the object
        for material in lod_object.data.materials:
            if material and material.use_nodes:
                self.optimize_material_textures(material, target_resolution)
    
    def optimize_material_textures(self, material, target_resolution):
        """
        Optimize textures in material for specific resolution
        """
        nodes = material.node_tree.nodes
        
        # Find all texture nodes
        texture_nodes = [node for node in nodes if node.type == 'TEX_IMAGE']
        
        for tex_node in texture_nodes:
            if tex_node.image:
                original_image = tex_node.image
                
                # Create optimized version if needed
                if original_image.size[0] > target_resolution:
                    optimized_image = self.create_optimized_texture(
                        original_image, 
                        target_resolution,
                        material.name
                    )
                    tex_node.image = optimized_image
    
    def create_optimized_texture(self, original_image, target_resolution, material_name):
        """
        Create optimized texture at target resolution
        """
        # Create new image at target resolution
        optimized_name = f"{original_image.name}_LOD_{target_resolution}"
        
        # Check if optimized version already exists
        if optimized_name in bpy.data.images:
            return bpy.data.images[optimized_name]
        
        optimized_image = bpy.data.images.new(
            name=optimized_name,
            width=target_resolution,
            height=target_resolution,
            alpha=original_image.alpha_mode != 'NONE',
            float_buffer=original_image.is_float
        )
        
        # Copy color space settings
        optimized_image.colorspace_settings.name = original_image.colorspace_settings.name
        
        # Scale down original image (simplified - in practice, use proper filtering)
        self.scale_image_data(original_image, optimized_image)
        
        return optimized_image
    
    def scale_image_data(self, source_image, target_image):
        """
        Scale image data from source to target resolution
        """
        # This is a simplified implementation
        # In practice, you'd use proper image filtering algorithms
        
        source_width, source_height = source_image.size
        target_width, target_height = target_image.size
        
        # Simple nearest-neighbor scaling
        scale_x = source_width / target_width
        scale_y = source_height / target_height
        
        target_pixels = []
        
        for y in range(target_height):
            for x in range(target_width):
                # Calculate source pixel coordinates
                src_x = int(x * scale_x)
                src_y = int(y * scale_y)
                
                # Clamp to source image bounds
                src_x = min(src_x, source_width - 1)
                src_y = min(src_y, source_height - 1)
                
                # Calculate pixel index in source image
                src_index = (src_y * source_width + src_x) * 4
                
                # Copy pixel data (RGBA)
                for channel in range(4):
                    if src_index + channel < len(source_image.pixels):
                        target_pixels.append(source_image.pixels[src_index + channel])
                    else:
                        target_pixels.append(0.0)
        
        # Apply scaled pixels to target image
        target_image.pixels = target_pixels
    
    def optimize_materials_for_lod(self, lod_object, lod_name):
        """
        Optimize materials for specific LOD level
        """
        for material in lod_object.data.materials:
            if material and material.use_nodes:
                # Simplify material for lower LOD levels
                if lod_name in ['LOD2', 'LOD3']:
                    self.simplify_material_for_low_lod(material)
    
    def simplify_material_for_low_lod(self, material):
        """
        Simplify material for low LOD levels
        """
        nodes = material.node_tree.nodes
        links = material.node_tree.links
        
        # Find Principled BSDF
        principled = None
        for node in nodes:
            if node.type == 'BSDF_PRINCIPLED':
                principled = node
                break
        
        if not principled:
            return
        
        # Remove complex nodes for performance
        nodes_to_remove = []
        for node in nodes:
            if node.type in ['TEX_NOISE', 'TEX_VORONOI', 'TEX_WAVE', 'MATH', 'VALTORGB']:
                # Keep essential connections, remove complex procedural nodes
                if not self.is_essential_node(node, principled):
                    nodes_to_remove.append(node)
        
        for node in nodes_to_remove:
            nodes.remove(node)
        
        # Simplify remaining connections
        self.simplify_material_connections(material, principled)
    
    def is_essential_node(self, node, principled):
        """
        Check if node is essential for material appearance
        """
        # Check if node directly connects to important Principled BSDF inputs
        essential_inputs = ['Base Color', 'Normal', 'Roughness', 'Metallic']
        
        for output in node.outputs:
            for link in output.links:
                if link.to_node == principled and link.to_socket.name in essential_inputs:
                    return True
        
        return False
    
    def simplify_material_connections(self, material, principled):
        """
        Simplify material connections for performance
        """
        # This would implement specific material simplification logic
        pass
    
    def calculate_triangle_count(self, obj):
        """
        Calculate triangle count for object
        """
        if obj.type != 'MESH':
            return 0
        
        # Ensure mesh data is up to date
        obj.data.calc_loop_triangles()
        return len(obj.data.loop_triangles)
    
    def calculate_memory_usage(self, obj, texture_resolution):
        """
        Calculate memory usage for object at specific texture resolution
        """
        memory_mb = 0
        
        # Calculate geometry memory
        if obj.type == 'MESH':
            vertex_count = len(obj.data.vertices)
            # Approximate: 32 bytes per vertex (position, normal, UV, etc.)
            geometry_memory = vertex_count * 32
            memory_mb += geometry_memory / (1024 * 1024)
        
        # Calculate texture memory
        for material in obj.data.materials:
            if material and material.use_nodes:
                texture_nodes = [node for node in material.node_tree.nodes 
                               if node.type == 'TEX_IMAGE' and node.image]
                
                for tex_node in texture_nodes:
                    # Assume 4 bytes per pixel (RGBA)
                    texture_memory = texture_resolution * texture_resolution * 4
                    memory_mb += texture_memory / (1024 * 1024)
        
        return memory_mb
    
    def calculate_quality_score(self, lod_object, hero_asset):
        """
        Calculate quality score compared to hero asset
        """
        # Simplified quality scoring based on triangle count ratio
        lod_triangles = self.calculate_triangle_count(lod_object)
        hero_triangles = self.calculate_triangle_count(hero_asset)
        
        if hero_triangles == 0:
            return 0
        
        triangle_ratio = lod_triangles / hero_triangles
        
        # Base score from triangle preservation
        quality_score = triangle_ratio * 100
        
        # Adjust for material complexity preservation
        lod_material_complexity = self.calculate_material_complexity(lod_object)
        hero_material_complexity = self.calculate_material_complexity(hero_asset)
        
        if hero_material_complexity > 0:
            material_ratio = lod_material_complexity / hero_material_complexity
            quality_score = (quality_score + material_ratio * 100) / 2
        
        return min(quality_score, 100)
    
    def calculate_material_complexity(self, obj):
        """
        Calculate material complexity score
        """
        complexity = 0
        
        for material in obj.data.materials:
            if material and material.use_nodes:
                # Count nodes as complexity measure
                complexity += len(material.node_tree.nodes)
        
        return complexity
    
    def validate_lod_system_performance(self):
        """
        Validate LOD system meets performance targets
        """
        print("\n=== LOD SYSTEM PERFORMANCE VALIDATION ===")
        
        validation_results = {
            'triangle_budget_compliance': True,
            'memory_budget_compliance': True,
            'quality_threshold_compliance': True,
            'total_memory_usage': 0,
            'performance_score': 100
        }
        
        total_memory = 0
        
        for asset_name, lod_chain in self.lod_configurations.items():
            for lod_name, triangle_count in lod_chain['triangle_counts'].items():
                # Check triangle budget compliance
                target_triangles = self.performance_targets.get(f"{lod_name.lower()}_triangles", 100000)
                if triangle_count > target_triangles:
                    validation_results['triangle_budget_compliance'] = False
                    print(f"⚠️  {asset_name} {lod_name} exceeds triangle budget: {triangle_count}/{target_triangles}")
                
                # Add to total memory
                memory_usage = lod_chain['memory_usage'][lod_name]
                total_memory += memory_usage
                
                # Check quality threshold
                quality_score = lod_chain['quality_scores'][lod_name]
                if quality_score < 60:  # Minimum acceptable quality
                    validation_results['quality_threshold_compliance'] = False
                    print(f"⚠️  {asset_name} {lod_name} quality below threshold: {quality_score}/100")
        
        validation_results['total_memory_usage'] = total_memory
        
        # Check total memory budget
        if total_memory > self.performance_targets['texture_memory_mb']:
            validation_results['memory_budget_compliance'] = False
            print(f"⚠️  Total memory usage exceeds budget: {total_memory:.1f}/{self.performance_targets['texture_memory_mb']}MB")
        
        # Calculate overall performance score
        performance_score = 100
        if not validation_results['triangle_budget_compliance']:
            performance_score -= 30
        if not validation_results['memory_budget_compliance']:
            performance_score -= 40
        if not validation_results['quality_threshold_compliance']:
            performance_score -= 30
        
        validation_results['performance_score'] = max(performance_score, 0)
        
        self.optimization_metrics['validation'] = validation_results
        
        print(f"LOD System Performance Score: {performance_score}/100")
        
        if performance_score >= 90:
            print("✅ Excellent optimization - ready for production")
        elif performance_score >= 70:
            print("✅ Good optimization - minor improvements recommended")
        else:
            print("⚠️  Significant optimization required before production")
        
        return validation_results
    
    def generate_optimization_report(self):
        """
        Generate comprehensive optimization report
        """
        report_path = bpy.path.abspath("//optimization_report.txt")
        
        with open(report_path, 'w') as f:
            f.write("PERFORMANCE OPTIMIZATION SYSTEM REPORT\n")
            f.write("=" * 60 + "\n\n")
            
            # Summary statistics
            total_assets = len(self.lod_configurations)
            total_lod_objects = sum(len(chain['lod_levels']) for chain in self.lod_configurations.values())
            
            f.write(f"SUMMARY:\n")
            f.write(f"Total Hero Assets: {total_assets}\n")
            f.write(f"Total LOD Objects: {total_lod_objects}\n")
            
            if 'validation' in self.optimization_metrics:
                validation = self.optimization_metrics['validation']
                f.write(f"Total Memory Usage: {validation['total_memory_usage']:.1f} MB\n")
                f.write(f"Performance Score: {validation['performance_score']}/100\n\n")
            
            # Detailed asset breakdown
            f.write("ASSET BREAKDOWN:\n")
            f.write("-" * 40 + "\n")
            
            for asset_name, lod_chain in self.lod_configurations.items():
                f.write(f"\n{asset_name}:\n")
                
                for lod_name in ['LOD0', 'LOD1', 'LOD2', 'LOD3']:
                    if lod_name in lod_chain['triangle_counts']:
                        triangles = lod_chain['triangle_counts'][lod_name]
                        memory = lod_chain['memory_usage'][lod_name]
                        quality = lod_chain['quality_scores'][lod_name]
                        
                        f.write(f"  {lod_name}: {triangles:,} triangles, {memory:.1f}MB, Quality: {quality:.1f}/100\n")
                        
                        # Performance warnings
                        target_triangles = self.performance_targets.get(f"{lod_name.lower()}_triangles", 100000)
                        if triangles > target_triangles:
                            f.write(f"    ⚠️  Exceeds triangle budget ({target_triangles:,})\n")
                        if quality < 60:
                            f.write(f"    ⚠️  Quality below acceptable threshold\n")
                        if memory > 100:  # 100MB per LOD level warning
                            f.write(f"    ⚠️  High memory usage\n")
            
            # Performance recommendations
            f.write(f"\nPERFORMANCE RECOMMENDATIONS:\n")
            f.write("-" * 40 + "\n")
            
            if 'validation' in self.optimization_metrics:
                validation = self.optimization_metrics['validation']
                
                if not validation['triangle_budget_compliance']:
                    f.write("• Reduce triangle counts on flagged LOD levels\n")
                if not validation['memory_budget_compliance']:
                    f.write("• Optimize texture resolutions or implement texture streaming\n")
                if not validation['quality_threshold_compliance']:
                    f.write("• Review LOD generation settings to maintain quality\n")
                
                if validation['performance_score'] >= 90:
                    f.write("• Optimization targets met - ready for production\n")
                elif validation['performance_score'] >= 70:
                    f.write("• Good optimization - minor improvements recommended\n")
                else:
                    f.write("• Significant optimization required before production\n")
        
        print(f"Optimization report saved to: {report_path}")
    
    def export_optimized_assets(self):
        """
        Export optimized assets for web delivery
        """
        print("\n=== EXPORTING OPTIMIZED ASSETS ===")
        
        export_path = bpy.path.abspath("//exports/")
        
        # Create export directories
        for lod_level in ['hero', 'high', 'medium', 'low']:
            lod_path = os.path.join(export_path, lod_level)
            os.makedirs(lod_path, exist_ok=True)
        
        # Export each LOD level
        lod_mapping = {
            'LOD0': 'hero',
            'LOD1': 'high', 
            'LOD2': 'medium',
            'LOD3': 'low'
        }
        
        for asset_name, lod_chain in self.lod_configurations.items():
            for lod_name, lod_object in lod_chain['lod_levels'].items():
                if lod_name in lod_mapping:
                    export_dir = lod_mapping[lod_name]
                    export_filename = f"{asset_name.lower()}_{export_dir}.glb"
                    export_filepath = os.path.join(export_path, export_dir, export_filename)
                    
                    # Select only this LOD object
                    bpy.ops.object.select_all(action='DESELECT')
                    lod_object.select_set(True)
                    bpy.context.view_layer.objects.active = lod_object
                    
                    # Export as glTF
                    bpy.ops.export_scene.gltf(
                        filepath=export_filepath,
                        use_selection=True,
                        export_format='GLB',
                        export_draco_mesh_compression_enable=True,
                        export_draco_mesh_compression_level=6,
                        export_texture_dir='',
                        export_keep_originals=False
                    )
                    
                    print(f"Exported {lod_name}: {export_filepath}")
        
        print("Asset export completed")


# Usage function
def create_performance_optimization_system():
    """
    Create complete performance optimization system
    """
    print("=== CREATING PERFORMANCE OPTIMIZATION SYSTEM ===")
    
    optimization_system = PerformanceOptimizationSystem()
    
    # Create LOD system
    lod_configurations = optimization_system.create_complete_lod_system()
    
    # Export optimized assets
    optimization_system.export_optimized_assets()
    
    print(f"Created LOD system for {len(lod_configurations)} hero assets")
    print("=== PERFORMANCE OPTIMIZATION SYSTEM COMPLETE ===")
    
    return optimization_system


# Execute optimization system creation
if __name__ == "__main__":
    optimization_system = create_performance_optimization_system()
