# VR Photorealistic Development Project - Advanced Cursor Rules
*Integrating Vibe Coding Principles with VR Excellence*

## Project Mission & Core Philosophy

This project creates photorealistic VR experiences using an AI-assisted workflow that maintains 90fps performance while achieving visual fidelity suitable for close examination in virtual reality environments. Our approach integrates **Vibe Coding principles** with sophisticated technical constraints, recognizing that AI handles the "70%" of routine work while human expertise delivers the critical "30%" that separates software people tolerate from software people love.

### The 70/30 Principle for VR Development
- **AI Excellence (70%)**: Rapid prototyping, boilerplate generation, initial implementations, framework scaffolding
- **Human Mastery (30%)**: VR optimization, edge case handling, performance tuning, user comfort, accessibility, error message crafting, and the meticulous polish required for immersive experiences

## Technology Stack & Performance Constraints

### Primary Technology Stack
- **Blender 4.4** with EEVEE Next and enhanced Cycles rendering
- **Cursor MCP Integration** for AI-assisted 3D modeling
- **Three.js with WebXR** for VR deployment
- **glTF 2.0** as the universal 3D format standard
- **HTML, CSS, Vanilla JavaScript ONLY** (no additional frameworks or libraries)

### Critical VR Performance Budget (90fps = 11.1ms per frame)
- **Polygon Budget**: 100K-300K triangles total scene
- **Texture Memory**: 256MB-512MB total
- **Draw Calls**: Under 100 per eye
- **Shader Complexity**: Avoid complex procedural materials in final export

## The Golden Rules of VR Vibe Coding

### 1. Be Specific and Clear About VR Requirements
When interacting with AI, always include VR-specific context:
- "Create a VR-optimized..." instead of just "Create a..."
- Specify performance targets: "Maintain under 5K triangles for hero assets"
- Include platform constraints: "WebXR compatible for Quest 2"
- Reference our asset tier system explicitly

**Example of Specific VR Prompting:**
```
"Create a VR-optimized Three.js scene with a medieval castle hero asset (10K triangles max) 
that maintains 90fps on Quest 2. Include LOD system for distance-based optimization 
and ensure all materials use PBR workflow compatible with glTF export."
```

### 2. Always Validate AI Output Against VR Intent and Performance
AI-generated code must be validated for:
- **VR Performance**: Does it maintain 90fps? Check triangle counts, draw calls, and texture memory
- **User Comfort**: Does it prevent motion sickness? Are interactions intuitive in 3D space?
- **Technical Accuracy**: Does it export correctly through the Blender → glTF → Three.js pipeline?
- **Cross-Platform Compatibility**: Does it work on multiple VR headsets?

### 3. Treat AI as a Junior VR Developer (With Expert Supervision)
Provide oversight for VR-critical areas:
- Performance optimization decisions
- VR interaction design patterns
- Asset optimization strategies
- WebXR compatibility considerations
- User experience and comfort validation

### 4. Never Merge VR Code You Don't Understand
VR development has unique complexities:
- Frame timing and performance implications
- 3D coordinate systems and transformations
- VR-specific user interaction patterns
- WebXR API quirks and compatibility issues

If AI generates VR code that seems unclear, always ask for explanation and simplification.

### 5. Obsess Over VR Polish and Craft
This is where the critical 30% lives - areas AI cannot handle:
- **Error Messages**: VR users can't easily access traditional error displays
- **Edge Cases**: Hand tracking failures, headset disconnections, performance drops
- **Comfort**: Motion sickness prevention, proper locomotion, ergonomic interactions
- **Accessibility**: Seated vs standing play, different physical abilities
- **Performance**: Testing on slower hardware, optimizing for battery life

## Vibe Coding's Five Fundamental Skills for VR

### 1. Thinking (Strategic VR Problem Formulation)
Structure VR problems using multi-layered thinking:

**Logical Thinking**: What is the core VR experience?
```
"Create an immersive solar system where users can examine planets up close"
```

**Analytical Thinking**: How will users interact in VR?
```
"Users need hand tracking for grabbing, teleportation for movement, 
and detailed surface inspection for planetary surfaces"
```

**Computational Thinking**: How does this map to our technical architecture?
```
"Hero assets for planets (15K triangles), mid-tier for moons (5K triangles), 
background stars (particle system), LOD system for distance optimization"
```

**Procedural Thinking**: What are the implementation details?
```
"Implement progressive loading, foveated rendering considerations, 
haptic feedback for interactions, and performance monitoring"
```

### 2. Framework (VR Architectural Awareness)
Guide AI toward VR-appropriate technologies:
- **Three.js**: Specify WebXR-compatible patterns and performance optimizations
- **Blender 4.4**: EEVEE Next for real-time preview, Cycles for final quality
- **glTF 2.0**: Ensure export compatibility and optimization settings
- **WebXR**: Platform-specific considerations and fallback handling

### 3. Checkpoints (Aggressive Version Control for VR)
VR development requires frequent checkpoints due to:
- Performance optimization experiments
- Asset iteration cycles
- Platform compatibility testing
- MCP-generated content validation

**Commit Strategy:**
```bash
git commit -m "feat: Add VR planet interaction system - untested"
git commit -m "perf: Optimize planet LOD system - 90fps maintained"
git commit -m "fix: Resolve WebXR controller tracking edge case"
```

### 4. Debugging (Collaborative VR Error Resolution)
VR debugging requires rich context for AI assistance:
- Performance profiling data
- VR-specific error logs
- Interaction pattern descriptions
- Device-specific behavior differences
- Screenshots/recordings from VR perspective

**Effective VR Debug Prompting:**
```
"VR interaction fails on Quest 2 but works on PC. Error shows 'Failed to get input source' 
in WebXR. Hand tracking works for grabbing but not for UI interactions. Here's the 
relevant code [snippet] and performance data [data]. Expected: smooth hand tracking. 
Actual: intermittent tracking loss."
```

### 5. Context (Comprehensive VR Information Provision)
Provide AI with rich VR context:
- Current VR hardware targets
- Performance budget constraints
- Asset optimization requirements
- User experience design patterns
- Integration with MCP workflow
- Blender export settings
- WebXR compatibility requirements

## Language & Code Quality Restrictions

### Absolute Language Constraints
```javascript
// ✅ ALLOWED: Pure Three.js VR patterns
renderer.xr.enabled = true;
const controller = renderer.xr.getController(0);

// ❌ FORBIDDEN: Framework additions
import React from 'react'; // NO
import Vue from 'vue';     // NO
npm install extra-lib;     // NO
```

### VR-Specific Code Completeness Standards
Every VR code response must include:

```javascript
// Required VR Performance Monitoring
class VRPerformanceValidator {
    constructor() {
        this.frameTime = 0;
        this.targetFrameTime = 11.1; // 90fps VR requirement
        this.triangleCount = 0;
        this.drawCalls = 0;
        this.memoryUsage = 0;
    }
    
    validateFrame(renderer) {
        const info = renderer.info;
        this.triangleCount = info.render.triangles;
        this.drawCalls = info.render.calls;
        
        // Critical VR performance thresholds
        if (this.triangleCount > 300000) {
            console.warn(`⚠️ VR: Triangle count exceeded: ${this.triangleCount}/300000`);
        }
        if (this.drawCalls > 100) {
            console.warn(`⚠️ VR: Draw calls exceeded: ${this.drawCalls}/100`);
        }
        if (this.frameTime > this.targetFrameTime) {
            console.error(`🚨 VR: Frame time critical: ${this.frameTime.toFixed(2)}ms`);
        }
    }
}

// Required VR Compatibility Checks
async function initializeVRExperience() {
    // WebXR availability check
    if (!('xr' in navigator)) {
        displayFallbackMessage('WebXR not supported');
        return false;
    }
    
    // VR session support validation
    const vrSupported = await navigator.xr.isSessionSupported('immersive-vr');
    if (!vrSupported) {
        displayFallbackMessage('VR headset not detected');
        return false;
    }
    
    return true;
}

// Required VR User Comfort Patterns
class VRComfortManager {
    constructor() {
        this.locomotionMode = 'teleport'; // Comfort-first default
        this.snapTurnEnabled = true;
        this.vignetteEnabled = true;
    }
    
    updateComfortSettings(userPreferences) {
        // Always provide comfort options for VR
        this.locomotionMode = userPreferences.comfort?.locomotion || 'teleport';
        this.enableComfortFeatures();
    }
}
```

## Asset Tier Implementation with Vibe Coding

### Hero Assets (Close Examination) - The Critical 30%
These require human expertise for the polish that defines VR quality:

```javascript
class HeroAssetManager {
    constructor() {
        this.maxTriangles = 15000;
        this.textureResolution = 2048;
        this.detailMaps = ['diffuse', 'normal', 'roughness', 'metallic'];
    }
    
    validateHeroAsset(asset) {
        // Human validation required for:
        // - Surface detail accuracy for close inspection
        // - Material authenticity under VR lighting
        // - Edge case handling for interaction boundaries
        // - Performance impact during intensive examination
        return this.performHumanQualityReview(asset);
    }
}
```

### Mid-Tier Assets (Interactive Background) - AI + Human Optimization
```javascript
class MidTierAssetPipeline {
    optimizeForVR(asset) {
        // AI can handle: Basic optimization patterns
        // Human must handle: Interaction design, visual hierarchy
        return {
            geometry: this.aiOptimizeGeometry(asset.geometry),
            materials: this.humanOptimizeMaterials(asset.materials), // Requires expertise
            interactions: this.humanDesignInteractions(asset) // Critical 30%
        };
    }
}
```

## MCP Integration with Vibe Coding Principles

### Collaborative Creation Workflow
```json
{
    "vibePrompts": {
        "aiGeneration": "Create base planetary surface with realistic terrain features",
        "humanRefinement": "Optimize for VR viewing distances and hand interaction",
        "iterativeImprovement": "Adjust based on user testing feedback in VR"
    },
    "mcpConfiguration": {
        "blenderIntegration": "AI-assisted creation + manual VR optimization",
        "qualityGates": "Human validation at each pipeline stage"
    }
}
```

### Strategic Problem Formulation for MCP
When prompting MCP systems, structure requests using VR-aware thinking:

```python
# Vibe Coding prompt structure for MCP
mcp_prompt = f"""
Create {asset_type} for VR experience:

Context: {vr_context}
Performance: {performance_requirements}
Interaction: {user_interaction_patterns}
Quality: {visual_fidelity_targets}
Platform: {target_vr_hardware}

Generate base implementation, then iterate based on VR testing feedback.
"""
```

## The Art of VR Polish - The Critical 30%

### Error Handling That Preserves VR Immersion
```javascript
class VRErrorManager {
    handleError(error, context) {
        // AI cannot design this - requires empathy and VR UX expertise
        switch (error.type) {
            case 'TRACKING_LOST':
                this.showSpatialErrorMessage(error.message);
                this.provideFallbackInteraction();
                break;
            case 'PERFORMANCE_DROP':
                this.gracefullyReduceQuality();
                this.maintainUserComfort();
                break;
            case 'CONTROLLER_DISCONNECT':
                this.enableAlternativeInputMethods();
                this.preserveUserProgress();
                break;
        }
    }
    
    showSpatialErrorMessage(message) {
        // Design spatial UI that doesn't break immersion
        // Position in user's field of view appropriately
        // Use 3D typography that's readable in VR
        // Provide clear recovery instructions
    }
}
```

### Performance Optimization - Where Human Expertise Shines
```javascript
class VRPerformanceOptimizer {
    optimizeForRealUsers() {
        // AI handles routine optimizations
        // Humans handle the nuanced decisions that matter for VR:
        
        this.profileOnActualHardware(); // Test on Quest 2, not just dev machines
        this.optimizeForBatteryLife();  // VR sessions are power-intensive
        this.handleNetworkVariability(); // VR apps often need cloud assets
        this.accommodatePhysicalLimitations(); // Room scale vs seated play
        this.preventMotionSickness(); // Requires understanding of human perception
    }
}
```

## Quality Validation Framework

### The Human-AI Collaboration Checklist
Before accepting any AI-generated VR code:

**AI Validation (Automated):**
- [ ] Code compiles and runs
- [ ] Basic Three.js patterns implemented
- [ ] WebXR compatibility maintained
- [ ] Performance thresholds not exceeded

**Human Validation (Critical 30%):**
- [ ] VR user experience feels natural and comfortable
- [ ] Edge cases handled gracefully (controller battery dies, tracking lost)
- [ ] Error messages preserve immersion
- [ ] Interactions work for users of different physical abilities
- [ ] Performance remains stable during extended sessions
- [ ] Visual quality meets photorealistic standards at VR viewing distances

### Continuous Learning and Iteration
```javascript
class VRDevelopmentLearning {
    captureUserFeedback() {
        // Areas AI cannot optimize without human insight:
        return {
            comfortRating: this.measureMotionSickness(),
            usabilityIssues: this.identifyUIProblems(),
            performancePerception: this.assessFrameRateExperience(),
            immersionBreakers: this.catalogueJarringExperiences()
        };
    }
    
    iterateBasedOnRealUsers(feedback) {
        // This requires human empathy and design judgment
        // AI can suggest technical solutions
        // Humans must decide on experience priorities
    }
}
```

## Documentation and Knowledge Sharing

### Effective Prompt Documentation
Maintain a repository of proven VR prompts:

```markdown
## High-Quality VR Prompts

### Asset Creation
**Prompt**: "Create a VR-optimized medieval stone texture with PBR workflow..."
**Result Quality**: ⭐⭐⭐⭐⭐
**Performance Impact**: Low
**Human Refinement Needed**: Material authenticity validation

### Interaction Systems  
**Prompt**: "Implement hand tracking for object manipulation in Three.js WebXR..."
**Result Quality**: ⭐⭐⭐
**Performance Impact**: Medium
**Human Refinement Needed**: Edge case handling, comfort optimization
```

### Architecture Decision Records (ADRs) for VR
Document the reasoning behind VR-specific decisions:

```markdown
# ADR-001: VR Locomotion System Choice

**Decision**: Teleportation-first with smooth locomotion option
**Context**: Comfort vs immersion trade-offs
**Human Reasoning**: Motion sickness prevention takes priority
**AI Cannot Decide**: Requires understanding of human physiology
```

## Advanced Troubleshooting Patterns

### Collaborative VR Error Resolution
When providing error context to AI:

```javascript
// Rich context for AI debugging assistance
const vrDebugContext = {
    error: "Hand tracking intermittent on Quest 2",
    hardwareInfo: navigator.xr.systemInfo,
    performanceData: renderer.info,
    userBehavior: "Occurs during rapid hand movements",
    expectedBehavior: "Smooth continuous tracking",
    vrSpecificFactors: {
        roomLighting: "Dim lighting conditions",
        handPosition: "Often occurs at edge of tracking volume",
        batteryLevel: "Controller at 30% battery"
    },
    codeSnippet: `
        controller.addEventListener('connected', (event) => {
            // Relevant tracking code
        });
    `,
    previousAttempts: [
        "Increased tracking confidence threshold - no improvement",
        "Added prediction smoothing - helped but not resolved"
    ]
};
```

## Future-Proofing and Evolution

### Balancing AI Assistance with Human Mastery
As AI capabilities evolve, maintain focus on irreplaceable human contributions:

- **System Architecture**: High-level VR experience design
- **User Empathy**: Understanding diverse VR user needs
- **Quality Craft**: The polish that creates love, not just tolerance
- **Domain Expertise**: Deep knowledge of VR perception and comfort
- **Creative Problem-Solving**: Novel solutions to unique VR challenges

### Preparing for Advanced VR Technologies
```javascript
class FutureVRCapabilities {
    // Areas where human oversight will remain critical:
    designForFoveatedRendering() {
        // Requires understanding of human visual perception
    }
    
    optimizeForEyeTracking() {
        // Needs empathy for different visual abilities
    }
    
    createHapticExperiences() {
        // Demands understanding of human touch perception
    }
    
    handleSocialVRInteractions() {
        // Requires social and emotional intelligence
    }
}
```

## Conclusion: Excellence Through Human-AI Symbiosis

This ruleset recognizes that exceptional VR experiences emerge from the synergy between AI's efficiency and human expertise. AI accelerates the 70% of development that follows established patterns, while human mastery delivers the 30% that creates truly compelling, comfortable, and delightful VR experiences.

The goal is not to replace human judgment but to amplify it, allowing developers to focus on the creative, empathetic, and craft-focused work that separates good software from great experiences. In VR, where user comfort and immersion are paramount, this balance becomes even more critical.

**Remember**: AI is your junior developer for the routine work. You are the senior engineer responsible for the experience, the craft, and the human elements that make VR magical.