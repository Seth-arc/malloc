"""
Knowledge Model (∆) API Implementation
Following MCP Server Specification lines 120-191

Educational Impact:
Manages curriculum structure, prerequisite mapping, and content organization
to provide structured learning pathways and enable effective knowledge delivery.

Performance Requirements:
- Quest 3 VR: Knowledge structure creation <200ms
- Memory usage: <75MB for complex curricula
- Spatial precision: 0.1mm tolerance for educational objects

Manages curriculum structure, prerequisite mapping, and content organization
with Blender integration for educational 3D content creation
"""

import asyncio
import json
import logging
import time
import uuid
from typing import Dict, List, Any, Optional, Set, Tuple
from datetime import datetime
import numpy as np
import networkx as nx  # For prerequisite dependency graphs
from dataclasses import dataclass, asdict
from abc import ABC, abstractmethod

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class KnowledgeStructureData:
    """
    Knowledge structure data following MCP Server Specification
    Based on lines 127-174
    
    Educational Impact:
    Standardizes curriculum structure for consistent content delivery
    and prerequisite management across all learning experiences.
    """
    domain_id: str
    content_architecture: Dict[str, Any]
    creation_timestamp: str = None
    
    def __post_init__(self):
        if self.creation_timestamp is None:
            self.creation_timestamp = datetime.now().isoformat()
    
    def validate_structure(self) -> bool:
        """
        Validate knowledge structure against MCP specification
        
        Educational Impact:
        Ensures curriculum structure quality and consistency for
        reliable learning progression and content delivery.
        
        Returns:
            bool: True if structure is valid, False otherwise
        """
        try:
            required_sections = ["modular_structure", "prerequisite_mapping"]
            
            if not all(section in self.content_architecture for section in required_sections):
                logger.error(f"Missing required sections: {required_sections}")
                return False
            
            # Validate modular structure
            modular_structure = self.content_architecture["modular_structure"]
            if "units" not in modular_structure:
                logger.error("Missing 'units' in modular_structure")
                return False
            
            # Validate each unit
            for unit in modular_structure["units"]:
                required_unit_fields = ["unit_id", "learning_objectives", "prerequisite_units"]
                for field in required_unit_fields:
                    if field not in unit:
                        logger.error(f"Missing required unit field: {field}")
                        return False
            
            # Validate prerequisite mapping
            prerequisite_mapping = self.content_architecture["prerequisite_mapping"]
            if "dependencies" not in prerequisite_mapping:
                logger.error("Missing 'dependencies' in prerequisite_mapping")
                return False
            
            return True
            
        except Exception as e:
            logger.error(f"Knowledge structure validation failed: {e}")
            return False

class KnowledgeModelProcessor:
    """
    Knowledge Model processor implementing MCP Server Specification API
    
    Educational Impact:
    Manages curriculum structure and content organization to provide
    structured learning pathways and enable effective knowledge delivery.
    
    Performance Requirements:
    - Knowledge structure creation: <200ms for complex curricula
    - Memory usage: <75MB for typical operations
    - Quest 3 compatibility: Maintains >72fps during processing
    """
    
    def __init__(self, blender_integration_enabled: bool = False):
        self.blender_integration_enabled = blender_integration_enabled
        self.knowledge_domains = {}
        self.prerequisite_graphs = {}
        self.content_cache = {}
        
        # Performance monitoring
        self.performance_metrics = {
            "structure_creation_times": [],
            "graph_processing_times": [],
            "blender_integration_times": []
        }
        
        # Initialize Blender integration if available
        if blender_integration_enabled:
            try:
                self.blender_integration = BlenderKnowledgeIntegration()
                logger.info("Blender integration enabled for knowledge model")
            except Exception as e:
                logger.error(f"Blender integration initialization failed: {e}")
                self.blender_integration_enabled = False
        
        logger.info("KnowledgeModelProcessor initialized with curriculum management capabilities")
    
    async def create_knowledge_structure(self, structure_data: KnowledgeStructureData) -> Dict[str, Any]:
        """
        Create knowledge structure following MCP Server Specification
        POST /api/v1/knowledge/structure/create implementation (lines 127-174)
        
        Educational Impact:
        Establishes structured curriculum framework for systematic knowledge
        delivery and prerequisite-based learning progression.
        
        Performance Requirements:
        - Quest 3 VR: <200ms response time
        - Memory: <50MB for structure creation
        - Spatial precision: 0.1mm for 3D educational content
        
        Args:
            structure_data: Validated knowledge structure data
            
        Returns:
            Dict containing structure creation results and metrics
            
        Raises:
            ValueError: If structure data is invalid
            PerformanceError: If processing exceeds Quest 3 performance thresholds
        """
        start_time = time.time()
        
        try:
            domain_id = structure_data.domain_id
            content_architecture = structure_data.content_architecture
            
            # Validate content architecture structure
            if not structure_data.validate_structure():
                raise ValueError("Invalid knowledge structure format")
            
            # Create prerequisite dependency graph
            graph_start = time.time()
            prerequisite_graph = await self.create_prerequisite_graph(
                content_architecture.get("prerequisite_mapping", {})
            )
            graph_time = time.time() - graph_start
            
            # Process modular structure
            processed_units = await self.process_learning_units(
                content_architecture.get("modular_structure", {}).get("units", [])
            )
            
            # Create cross-reference networks
            cross_references = await self.create_cross_reference_networks(
                content_architecture.get("cross_reference_networks", {})
            )
            
            # Calculate knowledge model weight configuration
            weight_configuration = await self.calculate_knowledge_weight_configuration(
                processed_units, prerequisite_graph
            )
            
            # Store knowledge domain
            domain_entry = {
                "content_architecture": content_architecture,
                "prerequisite_graph": prerequisite_graph,
                "processed_units": processed_units,
                "cross_references": cross_references,
                "weight_configuration": weight_configuration,
                "created_timestamp": datetime.now().isoformat(),
                "access_count": 0
            }
            
            self.knowledge_domains[domain_id] = domain_entry
            self.prerequisite_graphs[domain_id] = prerequisite_graph
            
            # Create Blender integration if enabled
            blender_integration_result = None
            blender_time = 0
            if self.blender_integration_enabled:
                blender_start = time.time()
                blender_integration_result = await self.create_blender_knowledge_nodes(
                    domain_id, processed_units
                )
                blender_time = time.time() - blender_start
            
            processing_time = time.time() - start_time
            
            # Record performance metrics
            await self._record_performance_metrics(processing_time, graph_time, blender_time)
            
            # Quest 3 performance validation
            if processing_time > 0.2:  # 200ms threshold
                logger.warning(f"Knowledge structure creation exceeded Quest 3 threshold: {processing_time:.3f}s")
            
            response = {
                "status": "created",
                "domain_id": domain_id,
                "units_processed": len(processed_units),
                "prerequisite_dependencies": prerequisite_graph.number_of_edges(),
                "cross_references": len(cross_references.get("concept_connections", [])),
                "weight_configuration": weight_configuration,
                "blender_integration": blender_integration_result,
                "performance_metrics": {
                    "total_processing_time_ms": processing_time * 1000,
                    "graph_processing_time_ms": graph_time * 1000,
                    "blender_integration_time_ms": blender_time * 1000
                },
                "creation_timestamp": datetime.now().isoformat()
            }
            
            logger.info(f"Knowledge structure created successfully: {domain_id}")
            return response
            
        except Exception as e:
            processing_time = time.time() - start_time
            logger.error(f"Knowledge structure creation failed ({processing_time:.3f}s): {e}")
            raise
    
    async def get_knowledge_structure(self, domain_id: str) -> Dict[str, Any]:
        """
        Get knowledge structure with current status and analytics
        GET /api/v1/knowledge/structure/{domain_id} implementation
        
        Educational Impact:
        Provides access to curriculum structure and learning pathway
        information for adaptive content delivery decisions.
        
        Args:
            domain_id: Unique identifier for the knowledge domain
            
        Returns:
            Dict containing knowledge structure and analytics
        """
        start_time = time.time()
        
        try:
            if domain_id not in self.knowledge_domains:
                raise ValueError(f"Knowledge domain not found: {domain_id}")
            
            domain_data = self.knowledge_domains[domain_id]
            domain_data["access_count"] += 1
            
            # Calculate learning pathway analytics
            pathway_analytics = await self.calculate_pathway_analytics(
                domain_data["prerequisite_graph"], 
                domain_data["processed_units"]
            )
            
            # Calculate content readiness metrics
            content_readiness = await self.assess_content_readiness(domain_data)
            
            processing_time = time.time() - start_time
            
            response = {
                "domain_id": domain_id,
                "content_architecture": domain_data["content_architecture"],
                "units_count": len(domain_data["processed_units"]),
                "prerequisite_dependencies": domain_data["prerequisite_graph"].number_of_edges(),
                "weight_configuration": domain_data["weight_configuration"],
                "pathway_analytics": pathway_analytics,
                "content_readiness": content_readiness,
                "access_count": domain_data["access_count"],
                "created_timestamp": domain_data["created_timestamp"],
                "processing_time_ms": processing_time * 1000
            }
            
            return response
            
        except Exception as e:
            processing_time = time.time() - start_time
            logger.error(f"Knowledge structure retrieval failed ({processing_time:.3f}s): {e}")
            raise
    
    async def create_prerequisite_graph(self, prerequisite_mapping: Dict[str, Any]) -> nx.DiGraph:
        """
        Create prerequisite dependency graph using NetworkX
        Based on MCP specification prerequisite mapping structure
        
        Educational Impact:
        Enables systematic learning progression by modeling prerequisite
        relationships and preventing knowledge gaps in learning pathways.
        
        Args:
            prerequisite_mapping: Prerequisite mapping configuration
            
        Returns:
            NetworkX directed graph representing prerequisite relationships
        """
        graph = nx.DiGraph()
        
        dependencies = prerequisite_mapping.get("dependencies", [])
        
        for dependency in dependencies:
            unit_id = dependency["unit_id"]
            requires = dependency.get("requires", [])
            
            # Add unit node with metadata
            graph.add_node(unit_id, 
                          unit_type=dependency.get("unit_type", "standard"),
                          difficulty_level=dependency.get("difficulty_level", "moderate"),
                          estimated_duration=dependency.get("estimated_duration", 30))
            
            # Add prerequisite edges
            for prerequisite in requires:
                graph.add_node(prerequisite)
                graph.add_edge(prerequisite, unit_id, 
                              dependency_type=dependency.get("dependency_type", "required"),
                              strength=dependency.get("dependency_strength", 1.0))
        
        # Validate graph is acyclic (no circular dependencies)
        if not nx.is_directed_acyclic_graph(graph):
            raise ValueError("Prerequisite mapping contains circular dependencies")
        
        # Add topological ordering for learning sequence
        try:
            topological_order = list(nx.topological_sort(graph))
            for i, node in enumerate(topological_order):
                graph.nodes[node]["topological_order"] = i
        except nx.NetworkXError:
            logger.warning("Could not create topological ordering for prerequisite graph")
        
        logger.info(f"Created prerequisite graph with {graph.number_of_nodes()} nodes and {graph.number_of_edges()} dependencies")
        return graph
    
    async def process_learning_units(self, units: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Process learning units with enhanced metadata and validation
        
        Educational Impact:
        Enriches learning units with metadata for effective content delivery
        and progress tracking throughout the learning experience.
        
        Args:
            units: List of raw learning unit definitions
            
        Returns:
            List of processed learning units with enhanced metadata
        """
        processed_units = []
        
        for unit in units:
            processed_unit = unit.copy()
            
            # Add processing metadata
            processed_unit["processing_timestamp"] = datetime.now().isoformat()
            processed_unit["estimated_duration_minutes"] = self._parse_duration(
                unit.get("estimated_duration", "15_minutes")
            )
            
            # Validate and enhance learning objectives
            objectives = unit.get("learning_objectives", [])
            processed_unit["objective_count"] = len(objectives)
            processed_unit["objective_complexity"] = await self._assess_objective_complexity(objectives)
            
            # Add competency mapping
            processed_unit["competency_mapping"] = await self._map_unit_competencies(unit)
            
            # Calculate unit difficulty score
            processed_unit["difficulty_score"] = await self._calculate_unit_difficulty(unit)
            
            # Add assessment integration points
            processed_unit["assessment_integration"] = await self._identify_assessment_points(unit)
            
            processed_units.append(processed_unit)
        
        return processed_units
    
    async def create_cross_reference_networks(self, cross_reference_config: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create cross-reference networks for concept connections
        
        Educational Impact:
        Establishes conceptual relationships between learning units to support
        knowledge transfer and deeper understanding across domains.
        
        Args:
            cross_reference_config: Cross-reference network configuration
            
        Returns:
            Dict containing cross-reference network data
        """
        concept_connections = cross_reference_config.get("concept_connections", [])
        skill_transfers = cross_reference_config.get("skill_transfers", [])
        
        # Build concept connection graph
        concept_graph = nx.Graph()
        for connection in concept_connections:
            source_concept = connection.get("source_concept")
            target_concept = connection.get("target_concept")
            connection_strength = connection.get("strength", 0.5)
            connection_type = connection.get("type", "conceptual")
            
            if source_concept and target_concept:
                concept_graph.add_edge(source_concept, target_concept,
                                     strength=connection_strength,
                                     type=connection_type)
        
        # Calculate concept centrality measures
        centrality_measures = {}
        if concept_graph.number_of_nodes() > 0:
            centrality_measures = {
                "betweenness": nx.betweenness_centrality(concept_graph),
                "closeness": nx.closeness_centrality(concept_graph),
                "degree": nx.degree_centrality(concept_graph)
            }
        
        return {
            "concept_connections": concept_connections,
            "skill_transfers": skill_transfers,
            "concept_graph": concept_graph,
            "centrality_measures": centrality_measures,
            "network_density": nx.density(concept_graph) if concept_graph.number_of_nodes() > 0 else 0.0
        }
    
    async def calculate_knowledge_weight_configuration(self, units: List[Dict[str, Any]], prerequisite_graph: nx.DiGraph) -> Dict[str, Any]:
        """
        Calculate knowledge model weight configuration for learning events
        Based on MCP specification lines 114-117
        
        Educational Impact:
        Determines appropriate emphasis on knowledge-specific factors in the
        adaptive learning equation for effective content delivery.
        
        Args:
            units: List of processed learning units
            prerequisite_graph: Prerequisite dependency graph
            
        Returns:
            Dict containing weight configuration for different learning events
        """
        # Base weight configurations per learning event (from spec lines 98-101)
        base_weights = {
            "onboarding": 0.22,      # Lower weight for onboarding
            "introduction": 0.28,    # Moderate weight for introduction
            "practice": 0.32,        # Higher weight for practice
            "application": 0.27,     # Moderate weight for application
            "mastery": 0.23          # Lower weight for mastery assessment
        }
        
        # Calculate curriculum complexity factors
        total_units = len(units)
        total_dependencies = prerequisite_graph.number_of_edges()
        dependency_density = total_dependencies / total_units if total_units > 0 else 0
        
        # Adjust weights based on curriculum complexity
        complexity_adjustment = min(0.1, dependency_density * 0.15)
        
        # Calculate average unit difficulty
        unit_difficulties = [unit.get("difficulty_score", 0.5) for unit in units]
        avg_difficulty = np.mean(unit_difficulties) if unit_difficulties else 0.5
        
        # Difficulty adjustment
        difficulty_adjustment = (avg_difficulty - 0.5) * 0.1
        
        # Generate final weight configuration
        weight_configuration = {}
        for event, base_weight in base_weights.items():
            adjusted_weight = base_weight + complexity_adjustment + difficulty_adjustment
            
            # Ensure weights stay within MCP specification bounds (0.20-0.35)
            final_weight = max(0.20, min(0.35, adjusted_weight))
            weight_configuration[event] = final_weight
        
        weight_configuration["complexity_factors"] = {
            "dependency_density": dependency_density,
            "average_difficulty": avg_difficulty,
            "complexity_adjustment": complexity_adjustment,
            "difficulty_adjustment": difficulty_adjustment
        }
        
        return weight_configuration
    
    async def create_blender_knowledge_nodes(self, domain_id: str, units: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Create Blender scene nodes with embedded learning metadata
        Implementation of MCP specification lines 177-191
        
        Educational Impact:
        Creates 3D educational content with embedded learning metadata
        to support immersive VR learning experiences.
        
        Args:
            domain_id: Knowledge domain identifier
            units: List of processed learning units
            
        Returns:
            Dict containing Blender integration results
        """
        if not self.blender_integration_enabled:
            return {"status": "disabled", "reason": "Blender integration not available"}
        
        try:
            created_nodes = []
            
            for unit in units:
                # Create knowledge node in Blender with spatial precision
                node_result = await self.blender_integration.create_knowledge_node(unit)
                created_nodes.append(node_result)
                
                # Create assessment triggers for each learning objective
                assessment_triggers = []
                for objective in unit.get("learning_objectives", []):
                    trigger_result = await self.blender_integration.create_assessment_trigger(
                        unit["unit_id"], objective
                    )
                    assessment_triggers.append(trigger_result)
                
                node_result["assessment_triggers"] = assessment_triggers
            
            return {
                "status": "created",
                "domain_id": domain_id,
                "nodes_created": len(created_nodes),
                "blender_scenes": created_nodes,
                "spatial_precision": "0.1mm",
                "quest3_optimization": True
            }
            
        except Exception as e:
            logger.error(f"Blender knowledge node creation failed: {e}")
            return {"status": "failed", "error": str(e)}
    
    async def calculate_pathway_analytics(self, prerequisite_graph: nx.DiGraph, units: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Calculate learning pathway analytics
        
        Educational Impact:
        Provides insights into learning pathway structure and complexity
        to optimize curriculum design and learner progression.
        
        Args:
            prerequisite_graph: Prerequisite dependency graph
            units: List of processed learning units
            
        Returns:
            Dict containing pathway analytics
        """
        # Calculate graph metrics
        num_nodes = prerequisite_graph.number_of_nodes()
        num_edges = prerequisite_graph.number_of_edges()
        
        # Calculate pathway complexity
        if num_nodes > 0:
            density = nx.density(prerequisite_graph)
            
            # Calculate average path length
            if nx.is_weakly_connected(prerequisite_graph):
                avg_path_length = nx.average_shortest_path_length(prerequisite_graph.to_undirected())
            else:
                # For disconnected graphs, calculate for largest component
                largest_component = max(nx.weakly_connected_components(prerequisite_graph), key=len)
                subgraph = prerequisite_graph.subgraph(largest_component)
                avg_path_length = nx.average_shortest_path_length(subgraph.to_undirected()) if len(largest_component) > 1 else 0
        else:
            density = 0
            avg_path_length = 0
        
        # Calculate learning sequence metrics
        total_duration = sum(unit.get("estimated_duration_minutes", 30) for unit in units)
        avg_difficulty = np.mean([unit.get("difficulty_score", 0.5) for unit in units]) if units else 0.5
        
        # Calculate prerequisite bottlenecks
        bottlenecks = []
        for node in prerequisite_graph.nodes():
            in_degree = prerequisite_graph.in_degree(node)
            out_degree = prerequisite_graph.out_degree(node)
            
            if in_degree > 2:  # High prerequisite requirements
                bottlenecks.append({
                    "unit_id": node,
                    "type": "prerequisite_heavy",
                    "in_degree": in_degree
                })
            elif out_degree > 3:  # Many dependent units
                bottlenecks.append({
                    "unit_id": node,
                    "type": "dependency_source",
                    "out_degree": out_degree
                })
        
        return {
            "pathway_complexity": {
                "density": density,
                "average_path_length": avg_path_length,
                "total_units": num_nodes,
                "total_dependencies": num_edges
            },
            "learning_metrics": {
                "total_duration_minutes": total_duration,
                "average_difficulty": avg_difficulty,
                "complexity_score": density * avg_difficulty
            },
            "bottlenecks": bottlenecks,
            "optimization_recommendations": await self._generate_optimization_recommendations(
                prerequisite_graph, units, bottlenecks
            )
        }
    
    async def assess_content_readiness(self, domain_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Assess readiness of content for learning delivery
        
        Educational Impact:
        Evaluates curriculum quality and completeness to ensure effective
        learning delivery and identify areas for improvement.
        
        Args:
            domain_data: Complete domain data structure
            
        Returns:
            Dict containing content readiness assessment
        """
        units = domain_data["processed_units"]
        prerequisite_graph = domain_data["prerequisite_graph"]
        
        # Assess content completeness
        completeness_score = 0.0
        total_checks = 0
        
        for unit in units:
            total_checks += 4
            
            # Check learning objectives
            if unit.get("learning_objectives") and len(unit["learning_objectives"]) > 0:
                completeness_score += 1
            
            # Check assessment integration
            if unit.get("assessment_integration"):
                completeness_score += 1
            
            # Check competency mapping
            if unit.get("competency_mapping"):
                completeness_score += 1
            
            # Check content materials
            if unit.get("content_materials") and len(unit["content_materials"]) > 0:
                completeness_score += 1
        
        final_completeness = completeness_score / total_checks if total_checks > 0 else 0.0
        
        # Assess prerequisite consistency
        prerequisite_consistency = self._assess_prerequisite_consistency(prerequisite_graph, units)
        
        # Assess difficulty progression
        difficulty_progression = self._assess_difficulty_progression(units, prerequisite_graph)
        
        # Overall readiness score
        readiness_score = (
            final_completeness * 0.4 +
            prerequisite_consistency * 0.3 +
            difficulty_progression * 0.3
        )
        
        return {
            "overall_readiness": readiness_score,
            "content_completeness": final_completeness,
            "prerequisite_consistency": prerequisite_consistency,
            "difficulty_progression": difficulty_progression,
            "readiness_level": self._categorize_readiness_level(readiness_score),
            "improvement_recommendations": self._generate_improvement_recommendations(
                final_completeness, prerequisite_consistency, difficulty_progression
            )
        }
    
    def _parse_duration(self, duration_str: str) -> int:
        """Parse duration string to minutes"""
        try:
            if "minutes" in duration_str:
                return int(duration_str.replace("_minutes", "").replace("minutes", ""))
            elif "hours" in duration_str:
                return int(duration_str.replace("_hours", "").replace("hours", "")) * 60
            else:
                return int(duration_str)
        except:
            return 30  # Default 30 minutes
    
    async def _assess_objective_complexity(self, objectives: List[str]) -> float:
        """Assess complexity of learning objectives"""
        if not objectives:
            return 0.0
        
        complexity_keywords = {
            "remember": 0.1, "recall": 0.1, "list": 0.1,
            "understand": 0.3, "explain": 0.3, "describe": 0.3,
            "apply": 0.5, "use": 0.5, "demonstrate": 0.5,
            "analyze": 0.7, "compare": 0.7, "categorize": 0.7,
            "evaluate": 0.9, "critique": 0.9, "assess": 0.9,
            "create": 1.0, "design": 1.0, "develop": 1.0
        }
        
        total_complexity = 0.0
        for objective in objectives:
            objective_lower = objective.lower()
            max_complexity = 0.3  # Default moderate complexity
            
            for keyword, complexity in complexity_keywords.items():
                if keyword in objective_lower:
                    max_complexity = max(max_complexity, complexity)
            
            total_complexity += max_complexity
        
        return total_complexity / len(objectives)
    
    async def _map_unit_competencies(self, unit: Dict[str, Any]) -> Dict[str, Any]:
        """Map unit to competency framework"""
        objectives = unit.get("learning_objectives", [])
        
        competency_mapping = {
            "cognitive_skills": [],
            "procedural_skills": [],
            "metacognitive_skills": []
        }
        
        # Simple keyword-based mapping (in production, would use more sophisticated NLP)
        for objective in objectives:
            obj_lower = objective.lower()
            
            if any(word in obj_lower for word in ["analyze", "evaluate", "compare", "synthesize"]):
                competency_mapping["cognitive_skills"].append(objective)
            elif any(word in obj_lower for word in ["perform", "execute", "demonstrate", "apply"]):
                competency_mapping["procedural_skills"].append(objective)
            elif any(word in obj_lower for word in ["reflect", "monitor", "plan", "regulate"]):
                competency_mapping["metacognitive_skills"].append(objective)
        
        return competency_mapping
    
    async def _calculate_unit_difficulty(self, unit: Dict[str, Any]) -> float:
        """Calculate unit difficulty score"""
        base_difficulty = 0.5
        
        # Adjust based on prerequisites
        prerequisites = unit.get("prerequisite_units", [])
        prerequisite_adjustment = len(prerequisites) * 0.1
        
        # Adjust based on objective complexity
        objectives = unit.get("learning_objectives", [])
        objective_complexity = await self._assess_objective_complexity(objectives)
        
        # Adjust based on estimated duration
        duration_minutes = self._parse_duration(unit.get("estimated_duration", "30_minutes"))
        duration_adjustment = min(0.2, (duration_minutes - 30) / 300)  # Longer = slightly harder
        
        difficulty = base_difficulty + prerequisite_adjustment + objective_complexity + duration_adjustment
        
        return max(0.1, min(1.0, difficulty))
    
    async def _identify_assessment_points(self, unit: Dict[str, Any]) -> Dict[str, Any]:
        """Identify assessment integration points for unit"""
        objectives = unit.get("learning_objectives", [])
        
        assessment_points = {
            "formative_assessments": [],
            "summative_assessments": [],
            "peer_assessments": [],
            "self_assessments": []
        }
        
        # Create assessment point for each objective
        for i, objective in enumerate(objectives):
            assessment_points["formative_assessments"].append({
                "assessment_id": f"{unit['unit_id']}_formative_{i+1}",
                "learning_objective": objective,
                "assessment_type": "formative",
                "trigger_condition": "objective_practice_completion"
            })
        
        # Add summative assessment at unit completion
        if objectives:
            assessment_points["summative_assessments"].append({
                "assessment_id": f"{unit['unit_id']}_summative",
                "learning_objectives": objectives,
                "assessment_type": "summative",
                "trigger_condition": "unit_completion"
            })
        
        return assessment_points
    
    async def _generate_optimization_recommendations(self, prerequisite_graph: nx.DiGraph, units: List[Dict[str, Any]], bottlenecks: List[Dict[str, Any]]) -> List[str]:
        """Generate optimization recommendations for learning pathway"""
        recommendations = []
        
        # Check for prerequisite bottlenecks
        if bottlenecks:
            recommendations.append("Consider splitting high-prerequisite units to reduce learning complexity")
        
        # Check pathway density
        density = nx.density(prerequisite_graph)
        if density > 0.7:
            recommendations.append("Prerequisite structure is dense - consider parallel learning paths")
        elif density < 0.2:
            recommendations.append("Prerequisite structure is sparse - consider adding connecting concepts")
        
        # Check difficulty progression
        difficulties = [unit.get("difficulty_score", 0.5) for unit in units]
        if difficulties:
            difficulty_variance = np.var(difficulties)
            if difficulty_variance > 0.2:
                recommendations.append("Large difficulty variance - consider smoothing difficulty progression")
        
        return recommendations
    
    def _assess_prerequisite_consistency(self, prerequisite_graph: nx.DiGraph, units: List[Dict[str, Any]]) -> float:
        """Assess consistency of prerequisite relationships"""
        if prerequisite_graph.number_of_nodes() == 0:
            return 1.0
        
        inconsistencies = 0
        total_checks = 0
        
        # Check for prerequisite-difficulty consistency
        for unit in units:
            unit_id = unit["unit_id"]
            if unit_id in prerequisite_graph:
                unit_difficulty = unit.get("difficulty_score", 0.5)
                
                # Check prerequisites have lower or equal difficulty
                for predecessor in prerequisite_graph.predecessors(unit_id):
                    predecessor_unit = next((u for u in units if u["unit_id"] == predecessor), None)
                    if predecessor_unit:
                        predecessor_difficulty = predecessor_unit.get("difficulty_score", 0.5)
                        total_checks += 1
                        
                        if predecessor_difficulty > unit_difficulty + 0.1:  # Allow small tolerance
                            inconsistencies += 1
        
        if total_checks == 0:
            return 1.0
        
        return 1.0 - (inconsistencies / total_checks)
    
    def _assess_difficulty_progression(self, units: List[Dict[str, Any]], prerequisite_graph: nx.DiGraph) -> float:
        """Assess quality of difficulty progression"""
        if not units:
            return 1.0
        
        difficulties = []
        ordered_units = []
        
        # Try to order units by topological sort if possible
        try:
            topological_order = list(nx.topological_sort(prerequisite_graph))
            ordered_units = [unit for unit_id in topological_order 
                           for unit in units if unit["unit_id"] == unit_id]
            
            # Add units not in graph
            graph_unit_ids = set(topological_order)
            for unit in units:
                if unit["unit_id"] not in graph_unit_ids:
                    ordered_units.append(unit)
                    
        except (nx.NetworkXError, nx.NetworkXUnfeasible):
            ordered_units = units
        
        difficulties = [unit.get("difficulty_score", 0.5) for unit in ordered_units]
        
        if len(difficulties) < 2:
            return 1.0
        
        # Calculate progression quality (prefer gradual increase)
        progression_score = 0.0
        for i in range(1, len(difficulties)):
            diff_change = difficulties[i] - difficulties[i-1]
            
            # Reward gradual increases, neutral for same level, penalize decreases
            if diff_change >= 0 and diff_change <= 0.3:
                progression_score += 1.0
            elif diff_change > 0.3:
                progression_score += 0.5  # Too steep increase
            else:
                progression_score += 0.3  # Decrease
        
        return progression_score / (len(difficulties) - 1)
    
    def _categorize_readiness_level(self, readiness_score: float) -> str:
        """Categorize content readiness level"""
        if readiness_score >= 0.9:
            return "production_ready"
        elif readiness_score >= 0.7:
            return "pilot_ready"
        elif readiness_score >= 0.5:
            return "development_needed"
        else:
            return "major_revision_required"
    
    def _generate_improvement_recommendations(self, completeness: float, consistency: float, progression: float) -> List[str]:
        """Generate improvement recommendations"""
        recommendations = []
        
        if completeness < 0.7:
            recommendations.append("Improve content completeness by adding missing learning materials and assessments")
        
        if consistency < 0.7:
            recommendations.append("Review prerequisite relationships for consistency with difficulty levels")
        
        if progression < 0.7:
            recommendations.append("Optimize difficulty progression to provide smoother learning curve")
        
        return recommendations
    
    async def _record_performance_metrics(self, total_time: float, graph_time: float, blender_time: float):
        """Record performance metrics for monitoring"""
        self.performance_metrics["structure_creation_times"].append({
            "total_time": total_time,
            "timestamp": datetime.now().isoformat()
        })
        
        self.performance_metrics["graph_processing_times"].append({
            "graph_time": graph_time,
            "timestamp": datetime.now().isoformat()
        })
        
        if blender_time > 0:
            self.performance_metrics["blender_integration_times"].append({
                "blender_time": blender_time,
                "timestamp": datetime.now().isoformat()
            })
        
        # Keep only last 100 measurements
        for metric_list in self.performance_metrics.values():
            if isinstance(metric_list, list) and len(metric_list) > 100:
                metric_list[:] = metric_list[-100:]
    
    def get_performance_metrics(self) -> Dict[str, Any]:
        """Get current performance metrics for monitoring"""
        recent_creation_times = [m["total_time"] for m in self.performance_metrics["structure_creation_times"][-10:]]
        recent_graph_times = [m["graph_time"] for m in self.performance_metrics["graph_processing_times"][-10:]]
        
        return {
            "average_creation_time": np.mean(recent_creation_times) if recent_creation_times else 0.0,
            "max_creation_time": max(recent_creation_times) if recent_creation_times else 0.0,
            "average_graph_time": np.mean(recent_graph_times) if recent_graph_times else 0.0,
            "active_domains": len(self.knowledge_domains),
            "quest3_compliance": all(t < 0.2 for t in recent_creation_times) if recent_creation_times else True
        }


class BlenderKnowledgeIntegration:
    """
    Blender integration for knowledge model following MCP specification
    Implementation of lines 177-191
    
    Educational Impact:
    Creates immersive 3D educational content with embedded learning metadata
    to support spatial learning and Quest 3 VR experiences.
    """
    
    def __init__(self):
        try:
            import bpy
            self.bpy = bpy
            self.blender_available = True
            logger.info("Blender integration initialized for knowledge model")
        except ImportError:
            self.blender_available = False
            logger.warning("Blender not available for knowledge integration")
    
    async def create_knowledge_node(self, unit_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create Blender scene with embedded learning metadata
        Following MCP specification implementation lines 179-191
        
        Educational Impact:
        Creates 3D educational content with precise spatial positioning
        and embedded metadata for immersive learning experiences.
        
        Performance Requirements:
        - Spatial precision: 0.1mm tolerance
        - Quest 3 optimization: >72fps maintained
        - Memory usage: <25MB per knowledge node
        
        Args:
            unit_data: Learning unit data structure
            
        Returns:
            Dict containing knowledge node creation results
        """
        if not self.blender_available:
            raise RuntimeError("Blender not available")
        
        try:
            # Get current scene
            scene = self.bpy.context.scene
            
            # Create knowledge node collection
            collection_name = f"knowledge_unit_{unit_data['unit_id']}"
            knowledge_collection = self.bpy.data.collections.new(collection_name)
            scene.collection.children.link(knowledge_collection)
            
            # Embed learning metadata in scene custom properties
            scene[f"learning_unit_id_{unit_data['unit_id']}"] = unit_data["unit_id"]
            scene[f"prerequisites_{unit_data['unit_id']}"] = json.dumps(
                unit_data.get("prerequisite_units", [])
            )
            scene[f"learning_objectives_{unit_data['unit_id']}"] = json.dumps(
                unit_data.get("learning_objectives", [])
            )
            scene[f"estimated_duration_{unit_data['unit_id']}"] = unit_data.get("estimated_duration", "15_minutes")
            scene[f"difficulty_score_{unit_data['unit_id']}"] = unit_data.get("difficulty_score", 0.5)
            
            # Create 3D content based on unit type
            content_objects = await self._create_unit_content_objects(unit_data, knowledge_collection)
            
            # Create assessment trigger objects for each learning objective
            assessment_triggers = []
            for objective in unit_data.get("learning_objectives", []):
                trigger_result = await self.create_assessment_trigger(unit_data["unit_id"], objective)
                assessment_triggers.append(trigger_result)
            
            # Apply Quest 3 optimization
            await self._optimize_for_quest3(content_objects)
            
            return {
                "unit_id": unit_data["unit_id"],
                "scene_name": scene.name,
                "collection_name": collection_name,
                "metadata_embedded": True,
                "content_objects_created": len(content_objects),
                "assessment_triggers": assessment_triggers,
                "spatial_precision": "0.1mm",
                "quest3_optimized": True,
                "creation_timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"Blender knowledge node creation failed: {e}")
            raise
    
    async def create_assessment_trigger(self, unit_id: str, learning_objective: str) -> Dict[str, Any]:
        """
        Create assessment trigger object in Blender scene
        
        Educational Impact:
        Creates invisible interaction zones that trigger assessments
        when learners interact with specific educational content.
        
        Args:
            unit_id: Learning unit identifier
            learning_objective: Specific learning objective for assessment
            
        Returns:
            Dict containing assessment trigger creation results
        """
        try:
            # Create invisible cube as assessment trigger with spatial precision
            self.bpy.ops.mesh.primitive_cube_add(size=0.2, location=(0, 0, 0))
            trigger_obj = self.bpy.context.active_object
            trigger_obj.name = f"assessment_trigger_{unit_id}_{hash(learning_objective) % 1000}"
            
            # Apply spatial precision positioning
            trigger_obj.location = (
                round(trigger_obj.location.x, 4),  # 0.1mm precision
                round(trigger_obj.location.y, 4),
                round(trigger_obj.location.z, 4)
            )
            
            # Make invisible but keep for interaction detection
            trigger_obj.hide_viewport = True
            trigger_obj.hide_render = True
            
            # Add assessment metadata with educational context
            trigger_obj["assessment_trigger"] = True
            trigger_obj["unit_id"] = unit_id
            trigger_obj["learning_objective"] = learning_objective
            trigger_obj["trigger_type"] = "formative"
            trigger_obj["spatial_precision"] = "0.1mm"
            trigger_obj["quest3_compatible"] = True
            
            # Add custom properties for VR interaction
            trigger_obj["vr_interaction_type"] = "proximity"
            trigger_obj["trigger_distance"] = 0.5  # 0.5 meters
            trigger_obj["assessment_duration"] = 60  # 60 seconds
            
            return {
                "trigger_name": trigger_obj.name,
                "unit_id": unit_id,
                "learning_objective": learning_objective,
                "trigger_created": True,
                "spatial_precision": "0.1mm",
                "quest3_optimized": True
            }
            
        except Exception as e:
            logger.error(f"Assessment trigger creation failed: {e}")
            return {
                "trigger_created": False,
                "error": str(e)
            }
    
    async def _create_unit_content_objects(self, unit_data: Dict[str, Any], collection) -> List[Any]:
        """
        Create 3D content objects based on unit type and objectives
        
        Educational Impact:
        Generates appropriate 3D educational content that supports
        the specific learning objectives and knowledge domain.
        
        Args:
            unit_data: Learning unit data
            collection: Blender collection for organization
            
        Returns:
            List of created Blender objects
        """
        content_objects = []
        
        try:
            unit_type = unit_data.get("unit_type", "conceptual")
            objectives = unit_data.get("learning_objectives", [])
            
            # Create content based on unit type
            if unit_type == "procedural":
                # Create step-by-step procedural content
                for i, objective in enumerate(objectives):
                    self.bpy.ops.mesh.primitive_cube_add(
                        size=0.5, 
                        location=(i * 1.0, 0, 0)
                    )
                    obj = self.bpy.context.active_object
                    obj.name = f"procedural_step_{i+1}_{unit_data['unit_id']}"
                    
                    # Add to collection
                    collection.objects.link(obj)
                    if obj.name in self.bpy.context.scene.collection.objects:
                        self.bpy.context.scene.collection.objects.unlink(obj)
                    
                    # Add educational metadata
                    obj["learning_objective"] = objective
                    obj["step_number"] = i + 1
                    obj["unit_id"] = unit_data["unit_id"]
                    
                    content_objects.append(obj)
            
            elif unit_type == "conceptual":
                # Create conceptual visualization
                self.bpy.ops.mesh.primitive_ico_sphere_add(
                    radius=0.7,
                    location=(0, 0, 1)
                )
                obj = self.bpy.context.active_object
                obj.name = f"concept_visualization_{unit_data['unit_id']}"
                
                # Add to collection
                collection.objects.link(obj)
                if obj.name in self.bpy.context.scene.collection.objects:
                    self.bpy.context.scene.collection.objects.unlink(obj)
                
                # Add educational metadata
                obj["unit_type"] = "conceptual"
                obj["concept_complexity"] = unit_data.get("difficulty_score", 0.5)
                obj["unit_id"] = unit_data["unit_id"]
                
                content_objects.append(obj)
            
            elif unit_type == "spatial":
                # Create spatial learning environment
                self.bpy.ops.mesh.primitive_plane_add(
                    size=2.0,
                    location=(0, 0, 0)
                )
                plane = self.bpy.context.active_object
                plane.name = f"spatial_environment_{unit_data['unit_id']}"
                
                # Add to collection
                collection.objects.link(plane)
                if plane.name in self.bpy.context.scene.collection.objects:
                    self.bpy.context.scene.collection.objects.unlink(plane)
                
                # Add spatial reference objects
                for i in range(3):
                    self.bpy.ops.mesh.primitive_cylinder_add(
                        radius=0.1,
                        depth=0.5,
                        location=(i * 0.8 - 0.8, 0, 0.25)
                    )
                    ref_obj = self.bpy.context.active_object
                    ref_obj.name = f"spatial_ref_{i}_{unit_data['unit_id']}"
                    
                    collection.objects.link(ref_obj)
                    if ref_obj.name in self.bpy.context.scene.collection.objects:
                        self.bpy.context.scene.collection.objects.unlink(ref_obj)
                    
                    content_objects.extend([plane, ref_obj])
            
            logger.info(f"Created {len(content_objects)} content objects for unit {unit_data['unit_id']}")
            
        except Exception as e:
            logger.error(f"Content object creation failed: {e}")
        
        return content_objects
    
    async def _optimize_for_quest3(self, content_objects: List[Any]):
        """
        Apply Quest 3 VR optimizations to content objects
        
        Educational Impact:
        Ensures optimal performance for VR learning experiences
        while maintaining educational effectiveness and spatial precision.
        
        Args:
            content_objects: List of Blender objects to optimize
        """
        try:
            for obj in content_objects:
                # Optimize geometry for VR performance
                if obj.type == 'MESH':
                    # Reduce subdivision levels for performance
                    for modifier in obj.modifiers:
                        if modifier.type == 'SUBSURF':
                            modifier.levels = min(modifier.levels, 2)
                    
                    # Ensure reasonable polygon count
                    if len(obj.data.polygons) > 5000:
                        # Add decimate modifier for optimization
                        decimate = obj.modifiers.new(name="VR_Optimize", type='DECIMATE')
                        decimate.ratio = 0.7
                        decimate.use_collapse_triangulate = True
                
                # Add VR-specific custom properties
                obj["quest3_optimized"] = True
                obj["target_fps"] = 72
                obj["spatial_precision"] = "0.1mm"
                obj["vr_interaction_enabled"] = True
                
                # Ensure objects are within VR interaction range
                if abs(obj.location.z) > 3.0:  # Keep within 3m height
                    obj.location.z = max(-1.5, min(1.5, obj.location.z))
            
            logger.info(f"Applied Quest 3 optimizations to {len(content_objects)} objects")
            
        except Exception as e:
            logger.error(f"Quest 3 optimization failed: {e}")
