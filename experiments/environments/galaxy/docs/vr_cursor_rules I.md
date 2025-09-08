# VR Photorealistic Development Project - Cursor Rules

## Project Context & Architecture

This project creates photorealistic VR experiences using a sophisticated AI-assisted workflow that maintains 90fps performance while achieving visual fidelity suitable for close examination in virtual reality environments.

### Primary Technology Stack
- **Blender 4.4** with EEVEE Next and enhanced Cycles rendering
- **Cursor MCP Integration** for AI-assisted 3D modeling
- **Three.js with WebXR** for VR deployment
- **glTF 2.0** as the universal 3D format standard
- **HTML, CSS, Vanilla JavaScript ONLY** (no additional frameworks or libraries)

### Performance Constraints (90fps = 11.1ms per frame budget)
- **Polygon Budget**: 100K-300K triangles total scene
- **Texture Memory**: 256MB-512MB total
- **Draw Calls**: Under 100 per eye
- **Shader Complexity**: Avoid complex procedural materials in final export

## Code Quality & Language Restrictions

### Absolute Language Restrictions
- Use ONLY HTML, CSS, and Vanilla JavaScript
- NO additional languages, libraries, or frameworks beyond Three.js
- NO preprocessors, transpilers, or build tools
- NO React, Vue, Angular, or any framework
- NO npm packages beyond Three.js and WebXR polyfills

### Completeness Requirements
- Provide COMPLETE, executable, and immediately runnable code
- Include ALL necessary HTML, CSS, and JavaScript
- NEVER use placeholders like "..." or "[rest of code]"
- Avoid partial implementations or pseudo-code
- Ensure all function signatures match their usage
- All variables must be properly defined
- Maintain complete error handling where present in original

### Structure Preservation Standards
Preserve ALL original elements:
- Class names and structures exactly as provided
- Function and method names
- Parameters and options
- Variable names and structure
- Comments and documentation style
- Loop structures and control flow
- Whitespace and indentation
- Line breaks and formatting

### Cross-File Alignment Protocol
- Maintain perfect alignment between all code files (HTML, CSS, JavaScript)
- Ensure class names, IDs, and selectors remain consistent across all files
- Preserve element relationships and hierarchies between HTML structure and CSS/JS selectors
- Any change to an identifier in one file must be consistently applied to all files
- Verify that DOM manipulation in JavaScript correctly targets HTML elements
- Maintain event handler relationships between HTML and JavaScript
- Keep CSS selector specificity and cascade order intact

## VR Performance Optimization Rules

### Asset Tier System Implementation
When creating or modifying assets, strictly adhere to:

#### Hero Assets (Close Examination Objects)
- Budget: 5K-15K triangles each
- Texture Resolution: Up to 2K per material channel
- PBR materials with full detail maps
- Implementation priority for LOD systems

#### Mid-Tier Assets (Interactive Background Elements)
- Budget: 1K-5K triangles each
- Texture Resolution: 1K per material channel
- Simplified PBR materials
- Distance-based optimization

#### Background Assets (Distant/Peripheral Objects)
- Budget: Under 1K triangles each
- Texture Resolution: 512px or lower
- Simplified materials with texture atlasing
- Aggressive optimization techniques

### VR-Specific Code Patterns
Always include in Three.js implementations:

```javascript
// VR performance monitoring
class VRPerformanceMonitor {
    constructor() {
        this.frameTime = 0;
        this.targetFrameTime = 11.1; // 90fps target
        this.warnings = [];
    }
    
    update(deltaTime) {
        this.frameTime = deltaTime;
        if (this.frameTime > this.targetFrameTime) {
            this.warnings.push(`Frame time exceeded: ${this.frameTime.toFixed(2)}ms`);
        }
    }
}

// Progressive asset loading
class VRAssetLoader {
    constructor() {
        this.loadQueue = [];
        this.memoryBudget = 512 * 1024 * 1024; // 512MB
        this.currentMemoryUsage = 0;
    }
    
    loadAsset(url, priority = 'normal') {
        return new Promise((resolve, reject) => {
            if (this.currentMemoryUsage >= this.memoryBudget) {
                this.unloadLowPriorityAssets();
            }
            // Progressive loading implementation
        });
    }
}

// LOD management systems
class VRLODManager {
    constructor(camera) {
        this.camera = camera;
        this.lodObjects = [];
        this.distances = [10, 50, 100]; // LOD distance thresholds
    }
    
    update() {
        this.lodObjects.forEach(obj => {
            const distance = this.camera.position.distanceTo(obj.position);
            obj.updateLOD(distance, this.distances);
        });
    }
}

// WebXR compatibility checks
function initializeVRCompatibility() {
    if ('xr' in navigator) {
        navigator.xr.isSessionSupported('immersive-vr').then(supported => {
            if (supported) {
                renderer.xr.enabled = true;
                document.body.appendChild(VRButton.createButton(renderer));
            }
        });
    }
}
```

## Blender 4.4 Integration Standards

### EEVEE Next Configuration
When providing Blender guidance, always reference:
- Enable Virtual Shadow Maps for accurate shadows without performance penalty
- Use Screen Space Reflections with VR-appropriate quality settings
- Configure Ambient Occlusion with GTAO method for VR-appropriate quality
- Set Volumetrics conservatively (VR is very sensitive to overdraw)

### PBR Material Workflow Requirements
- Always use Principled BSDF as primary shader node
- Connect texture maps correctly:
  - Base Color → Color input
  - Roughness → Roughness input (single channel)
  - Normal Map → Normal Map node → Normal input
  - Metallic → Metallic input (single channel)
- Configure for +Y Up export to match Three.js coordinate system
- Apply modifiers before glTF export

### Export Pipeline Standards
```python
# Blender export script template
import bpy

def export_for_vr(filepath):
    # Apply all modifiers
    for obj in bpy.context.selected_objects:
        if obj.type == 'MESH':
            for modifier in obj.modifiers:
                bpy.context.view_layer.objects.active = obj
                bpy.ops.object.modifier_apply(modifier=modifier.name)
    
    # Configure export settings
    bpy.ops.export_scene.gltf(
        filepath=filepath,
        export_format='GLB',
        ui_tab='GENERAL',
        export_copyright='',
        export_image_format='JPEG',
        export_texture_dir='',
        export_keep_originals=False,
        export_texcoords=True,
        export_normals=True,
        export_draco_mesh_compression_enable=True,
        export_draco_mesh_compression_level=6,
        export_draco_position_quantization=14,
        export_draco_normal_quantization=10,
        export_draco_texcoord_quantization=12,
        export_draco_color_quantization=10,
        export_draco_generic_quantization=12
    )
```

## MCP Integration Protocols

### Cursor MCP Configuration Requirements
When setting up or troubleshooting MCP integration:

```json
{
    "mcpServers": {
        "blender": {
            "command": "uvx",
            "args": ["blender-mcp"],
            "env": {
                "BLENDER_EXECUTABLE_PATH": "/path/to/blender",
                "ASTRONOMICAL_DATA_PATH": "./data/astronomical"
            }
        }
    }
}
```

### AI-Assisted Workflow Integration
- Phase 1-2: Environment setup and project planning
- Phase 3: AI-assisted creation via MCP + manual refinement
- Phase 4: VR-specific optimization techniques
- Phase 5: Export workflow (Blender → glTF → Three.js)
- Phase 6-8: Testing, deployment, and continuous optimization

## UI and Visual Element Standards

### Icon and Visual Element Requirements
- DO NOT use emojis as icons or visual elements
- Use proper HTML elements, CSS, or SVG solutions instead
- Maintain the original visual approach for icons and UI elements
- If icons are needed, suggest proper alternatives like SVG paths or icon fonts

### HTML Structure Requirements
```html
<!-- VR-optimized HTML structure -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VR Photorealistic Experience</title>
    <style>
        body { margin: 0; overflow: hidden; background: #000; }
        canvas { display: block; }
        .vr-ui { position: absolute; top: 10px; left: 10px; z-index: 100; }
        .performance-monitor { position: absolute; top: 10px; right: 10px; color: #fff; font-family: monospace; }
    </style>
</head>
<body>
    <div class="vr-ui">
        <button id="vr-button">Enter VR</button>
    </div>
    <div class="performance-monitor" id="performance-display"></div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
        // VR application implementation
    </script>
</body>
</html>
```

## Change Management Protocols

### Minimal Change Implementation
- Implement ONLY exactly what was requested
- NO additional improvements without explicit request
- Make minimal changes necessary to fulfill the request
- For any modification, show the ENTIRE code with changes clearly indicated
- Carefully verify each update for precision
- Only add new parameters if explicitly required

### Verification Checklist
Before delivering any code:
- [ ] Ensure all class names remain unchanged
- [ ] Verify all function signatures remain intact unless explicitly modified
- [ ] Confirm code maintains its original structure and organization
- [ ] Check that all changes integrate seamlessly with existing code
- [ ] Validate that no extraneous modifications were made
- [ ] Confirm only HTML, CSS, and Vanilla JavaScript are used
- [ ] Verify cross-file references remain valid and aligned
- [ ] Check that no emojis are used as icons or UI elements
- [ ] Ensure VR performance considerations are maintained
- [ ] Validate 90fps performance budget compliance

## Documentation and Workflow Phase Awareness

### Phase-Appropriate Responses
- **Phase 0-1**: Focus on spatial standards and environment setup
- **Phase 2-3**: Emphasize asset strategy and photorealistic creation
- **Phase 4-5**: Prioritize optimization and export workflows
- **Phase 6-8**: Concentrate on testing, deployment, and iteration

### Documentation Framework Integration
Reference appropriate documentation when providing solutions:
- Spatial Design Standards for dimensional decisions
- Performance Budget Specifications for optimization choices
- Asset Creation Strategy for workflow guidance
- Quality Assurance Protocols for validation requirements

## Quality Validation Standards

Every code response must consider:
- Does this maintain VR presence and comfort?
- Will this solution scale across the asset tier system?
- Is this compatible with the Blender → glTF → Three.js pipeline?
- Does this align with the established performance budgets?
- Can this be validated using the quality assurance protocols?
- Does this follow the vibe coding principles for AI-assisted development?

## Troubleshooting and Diagnostics

### Common Issue Resolution Patterns
When addressing problems:

1. **MCP Connection Issues**:
   ```bash
   # Health check sequence
   uv --version
   python --version
   uvx blender-mcp --check-connection
   ```

2. **Performance Bottlenecks**:
   ```javascript
   // Performance profiling
   function profileVRPerformance() {
       const stats = renderer.info;
       console.log(`Triangles: ${stats.render.triangles}`);
       console.log(`Draw calls: ${stats.render.calls}`);
       console.log(`Memory: ${stats.memory.geometries}MB`);
   }
   ```

3. **Export Pipeline Failures**:
   - Verify all modifiers are applied
   - Check material node connections
   - Validate texture paths and formats
   - Confirm coordinate system alignment (+Y Up)

### Team Coordination Standards
- Use standardized branch naming: `feature/vr-*`, `hotfix/performance-*`, `release/v*`
- Implement CI/CD validation for Blender files and VR performance
- Maintain consistent development environment configurations
- Document all performance optimization decisions

This comprehensive ruleset ensures all code and guidance provided maintains the highest standards for VR photorealistic development while strictly adhering to the project's technical constraints and performance requirements.