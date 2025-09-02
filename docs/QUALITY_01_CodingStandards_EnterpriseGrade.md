# Elite VR Learning MCP: Code Style and Quality Assurance Documents

**Version:** 1.0  
**Date:** August 30, 2025  
**Purpose:** Enterprise-grade code quality standards and automated quality assurance  
**Target:** 99th percentile code quality with educational VR specialization

---

## Understanding the Quality Philosophy

Code quality in educational software carries responsibilities beyond typical software development. When your code manages learning experiences that shape how people understand concepts, spatial relationships, and complex ideas, every function, every variable name, and every architectural decision can impact learning effectiveness. The quality standards documented here reflect this responsibility.

Think of code quality in educational VR like designing a learning space in the physical world. Just as a well-designed classroom has clear sight lines, accessible materials, and organized learning stations that support different learning styles, your code must be structured to support maintainability, educational effectiveness, and the collaborative development process. Poor code quality in educational software doesn't just create bugs—it can disrupt learning experiences, compromise accessibility features, or degrade the performance optimizations that make Quest 3 VR comfortable for extended educational sessions.

The configurations below establish patterns that ensure your codebase remains comprehensible and maintainable as it grows to support sophisticated adaptive learning algorithms, real-time performance optimization, and the complex coordination between Blender, Unity, and your MCP server.

---

## TypeScript and JavaScript Code Style Configuration

### ESLint Configuration (.eslintrc.cjs)

```javascript
// Elite VR Learning MCP - ESLint Configuration
// Enforces enterprise-grade code quality with educational VR specialization

module.exports = {
  root: true,
  env: {
    node: true,
    es2022: true,
    jest: true
  },
  extends: [
    'eslint:recommended',
    '@typescript-eslint/recommended',
    '@typescript-eslint/recommended-requiring-type-checking',
    'prettier'
  ],
  parser: '@typescript-eslint/parser',
  parserOptions: {
    ecmaVersion: 2022,
    sourceType: 'module',
    project: './tsconfig.json',
    tsconfigRootDir: __dirname
  },
  plugins: [
    '@typescript-eslint',
    'import',
    'jest',
    'jsdoc',
    'prefer-arrow',
    'educational-vr' // Custom plugin for educational VR specific rules
  ],
  rules: {
    // === TypeScript Specific Rules ===
    '@typescript-eslint/no-unused-vars': ['error', { 
      argsIgnorePattern: '^_',
      varsIgnorePattern: '^_',
      caughtErrorsIgnorePattern: '^_'
    }],
    '@typescript-eslint/explicit-function-return-type': ['error', {
      allowExpressions: false,
      allowTypedFunctionExpressions: true,
      allowHigherOrderFunctions: true
    }],
    '@typescript-eslint/no-explicit-any': 'error',
    '@typescript-eslint/no-non-null-assertion': 'error',
    '@typescript-eslint/prefer-nullish-coalescing': 'error',
    '@typescript-eslint/prefer-optional-chain': 'error',
    '@typescript-eslint/strict-boolean-expressions': 'error',
    '@typescript-eslint/prefer-readonly': 'error',
    '@typescript-eslint/prefer-readonly-parameter-types': 'warn',
    
    // === Educational VR Specific Rules ===
    // These rules ensure educational context is maintained throughout the codebase
    'educational-vr/require-educational-context': 'error', // Functions handling learner data must include educational context
    'educational-vr/quest3-performance-annotation': 'warn', // Performance-critical functions should document Quest 3 impact
    'educational-vr/accessibility-compliance': 'error', // UI components must include accessibility considerations
    'educational-vr/learning-objective-mapping': 'warn', // Educational functions should reference learning objectives
    'educational-vr/spatial-precision-validation': 'error', // Spatial calculations must validate precision requirements
    
    // === Code Organization and Clarity ===
    'import/order': ['error', {
      groups: [
        'builtin',     // Node.js built-in modules
        'external',    // External libraries
        'internal',    // Internal modules
        'parent',      // Parent directories
        'sibling',     // Sibling files
        'index'        // Index files
      ],
      'newlines-between': 'always',
      alphabetize: {
        order: 'asc',
        caseInsensitive: true
      }
    }],
    
    // === Documentation Requirements ===
    // Educational software requires comprehensive documentation
    'jsdoc/require-jsdoc': ['error', {
      require: {
        FunctionDeclaration: true,
        MethodDefinition: true,
        ClassDeclaration: true,
        ArrowFunctionExpression: true,
        FunctionExpression: true
      },
      contexts: [
        'TSInterfaceDeclaration',
        'TSTypeAliasDeclaration',
        'TSEnumDeclaration'
      ]
    }],
    'jsdoc/require-param': 'error',
    'jsdoc/require-param-type': 'error',
    'jsdoc/require-returns': 'error',
    'jsdoc/require-returns-type': 'error',
    'jsdoc/require-description': 'error',
    'jsdoc/require-example': ['warn', {
      exemptedBy: ['private', 'internal']
    }],
    
    // === Error Handling Requirements ===
    // Educational VR applications must handle errors gracefully to avoid disrupting learning
    'prefer-promise-reject-errors': 'error',
    'no-throw-literal': 'error',
    '@typescript-eslint/only-throw-error': 'error',
    'no-console': ['warn', {
      allow: ['warn', 'error', 'info'] // Allow specific console methods for logging
    }],
    
    // === Performance and Memory Management ===
    // Critical for Quest 3 VR performance
    'no-await-in-loop': 'error',
    'prefer-const': 'error',
    'no-var': 'error',
    'prefer-arrow/prefer-arrow-functions': ['error', {
      disallowPrototype: true,
      singleReturnOnly: false,
      classPropertiesAllowed: false
    }],
    
    // === Code Complexity Management ===
    // Keep functions manageable for educational codebase maintenance
    complexity: ['error', 10], // Maximum cyclomatic complexity
    'max-lines-per-function': ['error', {
      max: 50,
      skipBlankLines: true,
      skipComments: true
    }],
    'max-params': ['error', 4], // Force object parameter patterns for complex functions
    'max-depth': ['error', 4], // Prevent excessive nesting
    
    // === Naming Conventions for Educational Context ===
    '@typescript-eslint/naming-convention': [
      'error',
      {
        selector: 'default',
        format: ['camelCase']
      },
      {
        selector: 'variable',
        format: ['camelCase', 'UPPER_CASE'],
        leadingUnderscore: 'allow'
      },
      {
        selector: 'typeLike',
        format: ['PascalCase']
      },
      {
        selector: 'interface',
        format: ['PascalCase'],
        prefix: ['I'] // Interfaces should be prefixed with 'I'
      },
      {
        selector: 'class',
        format: ['PascalCase'],
        suffix: ['Manager', 'Service', 'Handler', 'Controller', 'Tool', 'System'] // Educational system patterns
      },
      {
        selector: 'enumMember',
        format: ['PascalCase']
      },
      {
        selector: 'method',
        format: ['camelCase'],
        filter: {
          regex: '^(handle|process|execute|validate|optimize|analyze|track|measure).*',
          match: false
        },
        custom: {
          regex: '^(handle|process|execute|validate|optimize|analyze|track|measure).*',
          match: true
        }
      }
    ]
  },
  
  // Override rules for specific file patterns
  overrides: [
    // Test files have more relaxed rules
    {
      files: ['**/*.test.ts', '**/*.spec.ts', '**/__tests__/**/*.ts'],
      rules: {
        '@typescript-eslint/no-explicit-any': 'warn',
        '@typescript-eslint/no-non-null-assertion': 'warn',
        'jsdoc/require-jsdoc': 'off',
        'max-lines-per-function': 'off'
      }
    },
    
    // Configuration files
    {
      files: ['**/*.config.ts', '**/*.config.js'],
      rules: {
        '@typescript-eslint/no-var-requires': 'off',
        'import/no-default-export': 'off'
      }
    },
    
    // Educational content and templates have specific requirements
    {
      files: ['**/educational/**/*.ts', '**/templates/**/*.ts'],
      rules: {
        'educational-vr/learning-objective-mapping': 'error',
        'educational-vr/accessibility-compliance': 'error',
        'jsdoc/require-example': 'error'
      }
    }
  ],
  
  // Settings for specific plugins
  settings: {
    'educational-vr': {
      'quest3-performance-threshold': 72, // Minimum FPS for Quest 3
      'spatial-precision-tolerance': 0.0001, // 0.1mm precision requirement
      'educational-context-required': [
        'LearnerProfile',
        'EducationalContext', 
        'LearningObjective',
        'AssessmentData'
      ]
    }
  }
};
```

This ESLint configuration demonstrates the sophisticated quality requirements for educational software development. The custom `educational-vr` plugin rules (which you would need to develop) ensure that educational considerations remain visible throughout your codebase. The complexity limits prevent functions from becoming unmaintainable, which is crucial when multiple developers are working on adaptive learning algorithms and spatial precision systems.

### Prettier Configuration (.prettierrc.json)

```json
{
  "semi": true,
  "trailingComma": "es5",
  "singleQuote": true,
  "printWidth": 100,
  "tabWidth": 2,
  "useTabs": false,
  "quoteProps": "as-needed",
  "bracketSpacing": true,
  "bracketSameLine": false,
  "arrowParens": "always",
  "endOfLine": "lf",
  "embeddedLanguageFormatting": "auto",
  "overrides": [
    {
      "files": "*.md",
      "options": {
        "printWidth": 80,
        "proseWrap": "always"
      }
    },
    {
      "files": "*.json",
      "options": {
        "printWidth": 120,
        "tabWidth": 2
      }
    },
    {
      "files": "*.yml",
      "options": {
        "tabWidth": 2,
        "singleQuote": false
      }
    }
  ]
}
```

The Prettier configuration balances readability with the space constraints that come from complex educational VR code. The 100-character line limit accommodates descriptive variable names like `spatialPrecisionValidationResult` while still maintaining readability.

---

## Unity C# Code Style Configuration

### .editorconfig for Unity Development

```ini
# Elite VR Learning MCP - Unity C# Code Style Configuration
# EditorConfig file for consistent coding style across development team

root = true

# All files
[*]
charset = utf-8
insert_final_newline = true
trim_trailing_whitespace = true

# Code files
[*.{cs,csx,vb,vbx}]
indent_style = space
indent_size = 4
end_of_line = crlf

# Unity-specific files
[*.{unity,prefab,asset,mat,anim,controller,mixer,overrideController}]
indent_style = space
indent_size = 2

# Configuration files
[*.{json,yml,yaml}]
indent_style = space
indent_size = 2

# Markdown files
[*.md]
trim_trailing_whitespace = false

# C# Code Style Rules for Educational VR Development
[*.cs]

# Organize usings
dotnet_sort_system_directives_first = true
dotnet_separate_import_directive_groups = false

# Educational VR Naming Conventions
# These patterns reflect the sophisticated educational architecture

# Interfaces should be prefixed with I and use descriptive educational terms
dotnet_naming_rule.interfaces_should_be_prefixed_with_i.severity = error
dotnet_naming_rule.interfaces_should_be_prefixed_with_i.symbols = interface_symbols
dotnet_naming_rule.interfaces_should_be_prefixed_with_i.style = prefix_interface_with_i

# Classes should use PascalCase with educational descriptive suffixes
dotnet_naming_rule.classes_should_be_pascal_case.severity = error
dotnet_naming_rule.classes_should_be_pascal_case.symbols = class_symbols
dotnet_naming_rule.classes_should_be_pascal_case.style = pascal_case_style

# Educational component classes should have descriptive suffixes
dotnet_naming_rule.educational_components_should_have_suffixes.severity = warning
dotnet_naming_rule.educational_components_should_have_suffixes.symbols = educational_component_symbols
dotnet_naming_rule.educational_components_should_have_suffixes.style = educational_component_style

# Constants should be UPPER_CASE for educational configuration
dotnet_naming_rule.constants_should_be_upper_case.severity = error
dotnet_naming_rule.constants_should_be_upper_case.symbols = constant_symbols
dotnet_naming_rule.constants_should_be_upper_case.style = upper_case_style

# Private fields should be prefixed with underscore
dotnet_naming_rule.private_fields_should_be_prefixed.severity = error
dotnet_naming_rule.private_fields_should_be_prefixed.symbols = private_field_symbols
dotnet_naming_rule.private_fields_should_be_prefixed.style = prefix_underscore_style

# Symbol definitions
dotnet_naming_symbols.interface_symbols.applicable_kinds = interface
dotnet_naming_symbols.interface_symbols.applicable_accessibilities = public, internal, private, protected, protected_internal, private_protected

dotnet_naming_symbols.class_symbols.applicable_kinds = class
dotnet_naming_symbols.class_symbols.applicable_accessibilities = public, internal, private, protected, protected_internal, private_protected

dotnet_naming_symbols.educational_component_symbols.applicable_kinds = class
dotnet_naming_symbols.educational_component_symbols.applicable_accessibilities = public, internal
dotnet_naming_symbols.educational_component_symbols.required_suffixes = Manager, System, Controller, Handler, Tool, Component, Service, Engine, Analyzer, Tracker, Monitor, Validator, Optimizer

dotnet_naming_symbols.constant_symbols.applicable_kinds = field, local
dotnet_naming_symbols.constant_symbols.required_modifiers = const

dotnet_naming_symbols.private_field_symbols.applicable_kinds = field
dotnet_naming_symbols.private_field_symbols.applicable_accessibilities = private

# Style definitions
dotnet_naming_style.prefix_interface_with_i.required_prefix = I
dotnet_naming_style.prefix_interface_with_i.capitalization = pascal_case

dotnet_naming_style.pascal_case_style.capitalization = pascal_case

dotnet_naming_style.educational_component_style.capitalization = pascal_case
dotnet_naming_style.educational_component_style.required_suffix = Manager, System, Controller, Handler, Tool, Component, Service, Engine, Analyzer, Tracker, Monitor, Validator, Optimizer

dotnet_naming_style.upper_case_style.capitalization = all_upper
dotnet_naming_style.upper_case_style.word_separator = _

dotnet_naming_style.prefix_underscore_style.required_prefix = _
dotnet_naming_style.prefix_underscore_style.capitalization = camel_case

# Code Quality Rules for Educational VR
# These rules ensure Quest 3 performance and educational effectiveness

# Require explicit access modifiers for clarity in educational codebase
dotnet_style_require_accessibility_modifiers = always:error

# Prefer var when type is obvious (reduces visual clutter in complex educational algorithms)
csharp_style_var_for_built_in_types = false:suggestion
csharp_style_var_when_type_is_apparent = true:suggestion
csharp_style_var_elsewhere = false:suggestion

# Expression preferences for educational code readability
csharp_style_expression_bodied_methods = false:suggestion
csharp_style_expression_bodied_constructors = false:none
csharp_style_expression_bodied_operators = false:none
csharp_style_expression_bodied_properties = true:suggestion
csharp_style_expression_bodied_indexers = true:suggestion
csharp_style_expression_bodied_accessors = true:suggestion

# Pattern matching preferences (useful for educational state machines)
csharp_style_pattern_matching_over_is_with_cast_check = true:suggestion
csharp_style_pattern_matching_over_as_with_null_check = true:suggestion

# Null-checking preferences (critical for educational VR stability)
csharp_style_throw_expression = true:suggestion
csharp_style_conditional_delegate_call = true:suggestion

# Formatting Rules for Educational VR Development

# New line preferences
csharp_new_line_before_open_brace = all
csharp_new_line_before_else = true
csharp_new_line_before_catch = true
csharp_new_line_before_finally = true
csharp_new_line_before_members_in_object_initializers = true
csharp_new_line_before_members_in_anonymous_types = true

# Indentation preferences
csharp_indent_case_contents = true
csharp_indent_switch_labels = true
csharp_indent_labels = flush_left

# Space preferences for readable educational code
csharp_space_around_binary_operators = before_and_after
csharp_space_around_declaration_statements = false
csharp_space_before_open_square_brackets = false
csharp_space_between_empty_square_brackets = false
csharp_space_between_method_call_parameter_list_parentheses = false
csharp_space_between_method_declaration_parameter_list_parentheses = false
csharp_space_between_parentheses = false
csharp_space_between_square_brackets = false
```

This EditorConfig file establishes Unity C# coding standards that reflect the educational nature of your platform. The naming conventions help developers immediately understand the role and scope of different classes and components, which is crucial when working with complex systems like adaptive learning algorithms and spatial precision managers.

---

## Git Workflow and Commit Standards

### Git Workflow Configuration (.gitflow.config)

```ini
# Elite VR Learning MCP - Git Flow Configuration
# Defines branching strategy for educational VR development

[gitflow "branch"]
    # Main development branches
    master = main
    develop = develop

[gitflow "prefix"]
    # Feature development branches
    feature = feature/
    release = release/
    hotfix = hotfix/
    support = support/
    bugfix = bugfix/
    
    # Educational VR specific branch types
    educational = educational/
    quest3-optimization = quest3/
    accessibility = accessibility/
    analytics = analytics/
    spatial-precision = spatial/

[gitflow "version"]
    # Version tagging for educational releases
    tag = v
```

### Commit Message Convention (.gitmessage)

```
# Elite VR Learning MCP - Commit Message Template
# 
# Format: <type>(<scope>): <description>
#
# Types:
#   feat      - New feature for educational VR system
#   fix       - Bug fix that affects learning effectiveness
#   docs      - Documentation changes
#   style     - Code style changes (formatting, semicolons, etc.)
#   refactor  - Code changes that neither fix bugs nor add features
#   test      - Adding or modifying tests
#   chore     - Build process or auxiliary tool changes
#   educational - Changes specifically to educational effectiveness
#   quest3    - Quest 3 performance optimizations
#   spatial   - Spatial precision improvements
#   analytics - Learning analytics enhancements
#   accessibility - Accessibility feature improvements
#
# Scopes:
#   mcp-server     - MCP protocol server
#   blender        - Blender integration
#   unity          - Unity VR development
#   analytics      - Learning analytics system
#   spatial        - Spatial precision system  
#   quest3         - Quest 3 optimization
#   educational    - Educational framework
#   accessibility  - Accessibility features
#   docs           - Documentation
#   tests          - Testing infrastructure
#
# Examples:
#   feat(mcp-server): add adaptive learning path generation
#   fix(quest3): resolve frame rate degradation in complex scenes
#   educational(analytics): improve learning objective tracking accuracy
#   spatial(precision): implement sub-millimeter connection validation
#   accessibility(ui): add screen reader support for VR menus
#
# Body: Explain WHAT changed and WHY (not HOW)
# Include educational impact when relevant
#
# Footer: Reference issues, breaking changes, educational validation
# Example: Closes #123, Educational-Impact: Improves spatial learning by 15%
#
# Remember: Each commit should represent a complete, working change that
# maintains or improves educational effectiveness
```

This commit message template ensures that every change to your codebase includes context about its educational impact. This is crucial for maintaining the pedagogical focus of your development process and for creating clear documentation of how technical changes affect learning outcomes.

---

## Testing Standards and Configuration

### Jest Testing Configuration (jest.config.js)

```javascript
// Elite VR Learning MCP - Jest Testing Configuration
// Comprehensive testing setup for educational VR system

/** @type {import('jest').Config} */
module.exports = {
  // Basic configuration
  preset: 'ts-jest',
  testEnvironment: 'node',
  clearMocks: true,
  collectCoverage: true,
  
  // Test file patterns
  testMatch: [
    '**/__tests__/**/*.(test|spec).ts',
    '**/?(*.)+(test|spec).ts'
  ],
  
  // Coverage configuration for educational software quality standards
  collectCoverageFrom: [
    'src/**/*.ts',
    '!src/**/*.d.ts',
    '!src/**/__tests__/**/*',
    '!src/**/__mocks__/**/*',
    '!src/**/index.ts' // Usually just exports
  ],
  
  // Coverage thresholds for educational software
  coverageThreshold: {
    global: {
      branches: 85,     // Educational logic must be thoroughly tested
      functions: 90,    // High function coverage for reliability
      lines: 90,        // Comprehensive line coverage
      statements: 90    // Complete statement coverage
    },
    
    // Higher standards for critical educational components
    'src/educational/**/*.ts': {
      branches: 95,
      functions: 95,
      lines: 95,
      statements: 95
    },
    
    // Spatial precision requires near-perfect testing
    'src/spatial-precision/**/*.ts': {
      branches: 98,
      functions: 98,
      lines: 98,
      statements: 98
    },
    
    // Quest 3 optimization critical for performance
    'src/quest3-optimization/**/*.ts': {
      branches: 95,
      functions: 95,
      lines: 95,
      statements: 95
    }
  },
  
  // Test setup and teardown
  setupFilesAfterEnv: [
    '<rootDir>/src/__tests__/setup/jest.setup.ts',
    '<rootDir>/src/__tests__/setup/educational-test-setup.ts'
  ],
  
  // Module mapping for educational VR development
  moduleNameMapping: {
    '^@/(.*)$': '<rootDir>/src/$1',
    '^@educational/(.*)$': '<rootDir>/src/educational/$1',
    '^@quest3/(.*)$': '<rootDir>/src/quest3-optimization/$1',
    '^@spatial/(.*)$': '<rootDir>/src/spatial-precision/$1',
    '^@analytics/(.*)$': '<rootDir>/src/analytics/$1',
    '^@testing/(.*)$': '<rootDir>/src/__tests__/utilities/$1'
  },
  
  // Transform configuration
  transform: {
    '^.+\\.ts$': 'ts-jest'
  },
  
  // Global test configuration for educational VR testing
  globals: {
    'ts-jest': {
      tsconfig: {
        // Relaxed type checking for test files
        compilerOptions: {
          types: ['jest', 'node']
        }
      }
    },
    
    // Educational VR test configuration
    EDUCATIONAL_TEST_CONFIG: {
      mockLearnerProfiles: true,
      mockQuest3Hardware: true,
      mockBlenderIntegration: true,
      enablePerformanceTesting: true,
      spatialPrecisionTesting: true
    }
  },
  
  // Test timeout for VR performance tests
  testTimeout: 30000, // 30 seconds for complex VR tests
  
  // Verbose output for educational development debugging
  verbose: true,
  
  // Test reporters for educational development workflow
  reporters: [
    'default',
    ['jest-junit', {
      outputDirectory: 'reports/junit',
      outputName: 'test-results.xml',
      classNameTemplate: '{classname}',
      titleTemplate: '{title}',
      ancestorSeparator: ' > ',
      usePathForSuiteName: true
    }],
    ['jest-html-reporter', {
      pageTitle: 'Elite VR Learning MCP Test Results',
      outputPath: 'reports/html/test-report.html',
      includeFailureMsg: true,
      includeSuiteFailure: true
    }]
  ]
};
```

The Jest configuration demonstrates the rigorous testing standards required for educational software. The coverage thresholds are higher than typical software projects because educational applications must be exceptionally reliable—learning disruptions caused by bugs can negatively impact educational outcomes and learner confidence.

### Educational Testing Utilities

```typescript
/**
 * Educational VR Testing Utilities
 * Specialized testing helpers for educational VR development
 */

import { LearnerProfile, EducationalContext, LearningObjective } from '@/types/educational';
import { Quest3PerformanceMetrics } from '@/types/quest3';
import { SpatialPrecisionResult } from '@/types/spatial';

/**
 * Creates a comprehensive mock learner profile for testing educational algorithms
 * @param overrides - Specific profile attributes to override
 * @returns Complete mock learner profile with realistic educational data
 */
export const createMockLearnerProfile = (overrides: Partial<LearnerProfile> = {}): LearnerProfile => {
  const defaultProfile: LearnerProfile = {
    userId: 'test-learner-001',
    demographicInfo: {
      ageGroup: '13-17',
      educationalLevel: 'high-school',
      priorVRExperience: 'beginner'
    },
    learningPreferences: {
      modalityPreferences: ['visual', 'kinesthetic'],
      embodimentPreference: 3, // High embodiment preference
      cognitiveLoadTolerance: 0.7,
      pacePreference: 'moderate'
    },
    vrPhysiologicalProfile: {
      motionSicknessLevel: 'low',
      vrComfortDuration: 45, // minutes
      spatialAwareness: 0.8,
      handTrackingAccuracy: 0.9
    },
    accessibilityNeeds: [],
    performanceHistory: {
      averageEngagement: 0.85,
      learningEffectiveness: 0.78,
      completionRate: 0.92,
      collaborationQuality: 0.75
    }
  };
  
  return { ...defaultProfile, ...overrides };
};

/**
 * Creates mock Quest 3 performance metrics for testing optimization algorithms
 * @param scenario - Performance scenario to simulate
 * @returns Realistic Quest 3 performance data
 */
export const createMockQuest3Metrics = (
  scenario: 'optimal' | 'degraded' | 'critical' = 'optimal'
): Quest3PerformanceMetrics => {
  const scenarios = {
    optimal: {
      averageFPS: 89.5,
      minimumFPS: 87.2,
      frameTimeVariability: 0.8,
      interactionLatency: 16.2,
      memoryUsage: 5.2, // GB
      thermalStatus: 'normal' as const,
      spatialTrackingQuality: 0.98
    },
    degraded: {
      averageFPS: 76.3,
      minimumFPS: 71.8,
      frameTimeVariability: 2.1,
      interactionLatency: 23.7,
      memoryUsage: 7.1, // GB
      thermalStatus: 'warm' as const,
      spatialTrackingQuality: 0.94
    },
    critical: {
      averageFPS: 68.1,
      minimumFPS: 65.2,
      frameTimeVariability: 4.2,
      interactionLatency: 31.5,
      memoryUsage: 8.3, // GB
      thermalStatus: 'hot' as const,
      spatialTrackingQuality: 0.89
    }
  };
  
  return scenarios[scenario];
};

/**
 * Validates educational effectiveness of test results
 * @param testResult - Result from educational algorithm testing
 * @param expectedEffectiveness - Minimum expected effectiveness score
 * @returns Validation result with detailed feedback
 */
export const validateEducationalEffectiveness = (
  testResult: any,
  expectedEffectiveness: number = 0.8
): EducationalValidationResult => {
  const effectiveness = testResult.educationalEffectiveness || 0;
  const engagement = testResult.engagementLevel || 0;
  const learningOutcomes = testResult.learningOutcomes || [];
  
  const isEffective = effectiveness >= expectedEffectiveness;
  const hasGoodEngagement = engagement >= 0.7;
  const achievedObjectives = learningOutcomes.filter((outcome: any) => outcome.achieved).length;
  const totalObjectives = learningOutcomes.length;
  const objectiveAchievementRate = totalObjectives > 0 ? achievedObjectives / totalObjectives : 0;
  
  return {
    isValid: isEffective && hasGoodEngagement && objectiveAchievementRate >= 0.8,
    effectiveness,
    engagement,
    objectiveAchievementRate,
    recommendations: [
      ...(effectiveness < expectedEffectiveness ? ['Improve educational algorithm effectiveness'] : []),
      ...(engagement < 0.7 ? ['Enhance learner engagement mechanisms'] : []),
      ...(objectiveAchievementRate < 0.8 ? ['Review learning objective alignment'] : [])
    ]
  };
};

/**
 * Asserts that spatial precision meets educational requirements
 * @param spatialResult - Result from spatial precision testing
 * @param tolerance - Maximum acceptable tolerance (default: 0.1mm)
 */
export const assertSpatialPrecision = (
  spatialResult: SpatialPrecisionResult,
  tolerance: number = 0.0001 // 0.1mm default
): void => {
  expect(spatialResult.positionError).toBeLessThanOrEqual(tolerance);
  expect(spatialResult.rotationError).toBeLessThanOrEqual(0.01); // 0.01 degrees
  expect(spatialResult.precisionScore).toBeGreaterThanOrEqual(0.999);
  
  if (spatialResult.educationalImpact) {
    expect(spatialResult.educationalImpact.preservesLearningEffectiveness).toBe(true);
  }
};

/**
 * Creates a test suite for educational VR components
 * @param componentName - Name of the component being tested
 * @param testSuite - Test suite function
 */
export const createEducationalTestSuite = (
  componentName: string,
  testSuite: () => void
): void => {
  describe(`Educational VR Component: ${componentName}`, () => {
    beforeEach(() => {
      // Reset educational test state
      jest.clearAllMocks();
      
      // Initialize educational testing environment
      global.EDUCATIONAL_TEST_ENV = {
        mockLearnerProfile: createMockLearnerProfile(),
        mockQuest3Metrics: createMockQuest3Metrics(),
        testStartTime: Date.now()
      };
    });
    
    afterEach(() => {
      // Validate educational compliance after each test
      const testDuration = Date.now() - global.EDUCATIONAL_TEST_ENV.testStartTime;
      
      // Ensure tests don't run too long (simulate VR comfort limits)
      expect(testDuration).toBeLessThan(30000); // 30 seconds max per test
      
      // Clean up educational test environment
      delete global.EDUCATIONAL_TEST_ENV;
    });
    
    testSuite();
  });
};

interface EducationalValidationResult {
  isValid: boolean;
  effectiveness: number;
  engagement: number;
  objectiveAchievementRate: number;
  recommendations: string[];
}
```

These testing utilities demonstrate how quality assurance in educational software extends beyond traditional software testing. The utilities include specialized assertions for educational effectiveness, spatial precision validation, and Quest 3 performance requirements that reflect the unique demands of your educational VR platform.

The comprehensive quality assurance framework I've outlined here ensures that your sophisticated educational VR system maintains the high standards necessary for effective learning. The ESLint rules prevent common coding mistakes while enforcing patterns that support educational effectiveness. The Unity C# standards ensure your VR components follow consistent patterns that make the codebase maintainable as it grows to support complex adaptive learning algorithms. The Git workflow standards ensure that every change to your system is properly documented and contextualized within its educational impact.

The testing configuration establishes the rigorous validation standards necessary for educational software, where bugs don't just affect user experience—they can disrupt learning processes and potentially impact educational outcomes. The specialized testing utilities provide the tools needed to validate not just that your code works, but that it effectively supports the sophisticated educational goals you've established for your system.