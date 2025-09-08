"""
Adaptation Processor for Real-time Learning Adjustments

Educational Impact:
Processes real-time learner interaction data to generate immediate educational
adaptations, enabling dynamic learning optimization based on engagement,
performance, and competency indicators. Ensures learners receive optimal
support and challenge levels for maximum educational effectiveness.

Performance Requirements:
- Adaptation processing: <10ms for real-time response generation
- Decision accuracy: >95% appropriate educational recommendations
- Memory efficiency: <5MB for processing state
- Concurrent processing: Support 50+ simultaneous learner adaptations

Quest 3 VR Optimization:
- Minimal processing overhead to maintain VR frame rates
- Efficient adaptation command generation for VR environments
- Optimized memory usage for VR system constraints
"""

import asyncio
import logging
import time
from typing import Dict, List, Optional, Any, Tuple
from datetime import datetime, timezone
from dataclasses import dataclass
import numpy as np

from ..learning.integration_engine import LearningIntegrationEngine
from ..learning.learner_model import LearnerModel
from ..learning.knowledge_model import KnowledgeModel
from ..learning.engagement_model import EngagementModel
from ..learning.assessment_model import AssessmentModel

logger = logging.getLogger(__name__)

@dataclass
class AdaptationCommand:
    """
    Educational adaptation command for VR learning environment.
    
    Educational Impact:
    Represents a specific educational intervention or adjustment that
    optimizes the learning experience based on real-time learner data,
    ensuring appropriate challenge, support, and engagement levels.
    """
    command_type: str  # difficulty_adjustment, support_intervention, content_modification, etc.
    command_action: str  # increase, decrease, provide, remove, etc.
    target_value: float  # 0.0 to 1.0 scale for adjustments
    reasoning: str  # Educational rationale for the adaptation
    priority: int  # 1 (urgent) to 5 (low priority)
    educational_context: str  # Educational objective or focus area
    implementation_hint: str  # Guidance for VR environment implementation
    duration_estimate: float  # Estimated implementation time in seconds

@dataclass
class AdaptationResult:
    """
    Result of adaptation processing with educational context.
    
    Educational Impact:
    Comprehensive adaptation outcome including specific commands,
    educational rationale, and performance metrics to guide
    real-time learning optimization and educational effectiveness.
    """
    adaptation_commands: List[AdaptationCommand]
    educational_effectiveness: float  # 0.0 to 1.0 effectiveness score
    processing_time: float  # Processing time in milliseconds
    confidence_score: float  # 0.0 to 1.0 confidence in recommendations
    learning_state_update: Dict[str, Any]  # Updated learning state
    performance_metrics: Dict[str, float]  # Processing performance data

class AdaptationProcessor:
    """
    Processes real-time learning data to generate educational adaptations.
    
    Educational Impact:
    Provides the core intelligence for real-time learning optimization,
    analyzing learner interactions, engagement patterns, and performance
    indicators to generate immediate educational adaptations that maximize
    learning outcomes and maintain optimal challenge levels.
    
    Performance Requirements:
    - Processing latency: <10ms for adaptation command generation
    - Decision accuracy: >95% appropriate educational recommendations
    - Memory efficiency: <5MB per concurrent learner processing
    - Educational effectiveness: >90% positive learning outcomes
    
    Features:
    - Real-time mathematical learning equation processing
    - Multi-dimensional learner state analysis
    - Educational psychology-based adaptation strategies
    - VR-optimized adaptation command generation
    """
    
    def __init__(self, integration_engine: LearningIntegrationEngine):
        """
        Initialize adaptation processor for real-time learning optimization.
        
        Educational Impact:
        Sets up the core adaptation intelligence that enables immediate
        educational response to learner needs, ensuring optimal learning
        progression and engagement in real-time VR environments.
        
        Args:
            integration_engine: Learning integration engine for mathematical processing
        """
        self.integration_engine = integration_engine
        
        # Learning model components
        self.learner_model = LearnerModel()
        self.knowledge_model = KnowledgeModel()
        self.engagement_model = EngagementModel()
        self.assessment_model = AssessmentModel()
        
        # Adaptation strategies
        self.adaptation_strategies = {
            'difficulty_management': self._process_difficulty_adaptation,
            'support_optimization': self._process_support_adaptation,
            'engagement_enhancement': self._process_engagement_adaptation,
            'content_personalization': self._process_content_adaptation,
            'pacing_optimization': self._process_pacing_adaptation
        }
        
        # Performance tracking
        self.processing_metrics = {
            'total_adaptations': 0,
            'successful_adaptations': 0,
            'average_processing_time': 0.0,
            'average_effectiveness': 0.0,
            'adaptation_accuracy': 0.0
        }
        
        # Educational effectiveness tracking
        self.effectiveness_metrics = {
            'learning_improvements': 0,
            'engagement_improvements': 0,
            'performance_improvements': 0,
            'total_recommendations': 0
        }
        
        # Adaptation thresholds
        self.adaptation_thresholds = {
            'stress_level_high': 0.7,
            'engagement_low': 0.4,
            'performance_struggling': 0.3,
            'competency_ready_advance': 0.8,
            'help_seeking_frequent': 0.2,
            'error_rate_concerning': 0.4
        }
        
    async def process_learning_data(
        self, 
        session_id: str, 
        interaction_snapshot: Dict[str, Any], 
        timestamp: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Process real-time learning data to generate educational adaptations.
        
        Educational Impact:
        Analyzes comprehensive learner interaction data to generate immediate
        educational adaptations, ensuring optimal learning progression,
        appropriate challenge levels, and maximum educational effectiveness.
        
        Performance Requirements:
        - Processing time: <10ms for real-time adaptation generation
        - Decision accuracy: >95% appropriate educational recommendations
        - Memory allocation: <1MB for processing state
        
        Args:
            session_id: Unique session identifier for context
            interaction_snapshot: Real-time learner interaction data
            timestamp: Optional timestamp for temporal analysis
            
        Returns:
            Dict containing adaptation commands and educational analysis
        """
        start_time = time.time()
        
        try:
            # Extract interaction components
            learner_state = interaction_snapshot.get('learner_state', {})
            engagement_metrics = interaction_snapshot.get('engagement_metrics', {})
            performance_indicators = interaction_snapshot.get('performance_indicators', {})
            
            # Process through integration engine for mathematical analysis
            integration_result = await self.integration_engine.process_real_time_adaptation(
                session_id=session_id,
                learner_state=learner_state,
                engagement_metrics=engagement_metrics,
                performance_indicators=performance_indicators,
                timestamp=timestamp
            )
            
            # Generate adaptation strategies based on integration result
            adaptation_commands = await self._generate_adaptation_strategies(
                session_id=session_id,
                integration_result=integration_result,
                interaction_snapshot=interaction_snapshot
            )
            
            # Calculate educational effectiveness
            effectiveness_score = await self._calculate_adaptation_effectiveness(
                adaptation_commands,
                integration_result
            )
            
            # Update learning state based on adaptations
            learning_state_update = await self._generate_learning_state_update(
                integration_result,
                adaptation_commands
            )
            
            # Calculate processing performance
            processing_time = (time.time() - start_time) * 1000  # Convert to milliseconds
            
            # Create adaptation result
            result = AdaptationResult(
                adaptation_commands=adaptation_commands,
                educational_effectiveness=effectiveness_score,
                processing_time=processing_time,
                confidence_score=integration_result.get('confidence_score', 0.8),
                learning_state_update=learning_state_update,
                performance_metrics={
                    'processing_time_ms': processing_time,
                    'commands_generated': len(adaptation_commands),
                    'effectiveness_score': effectiveness_score
                }
            )
            
            # Update performance metrics
            await self._update_processing_metrics(result)
            
            # Format response for WebSocket communication
            return {
                'adaptation_commands': [self._format_adaptation_command(cmd) for cmd in adaptation_commands],
                'updated_learning_state': learning_state_update,
                'performance_metrics': result.performance_metrics,
                'educational_analysis': {
                    'effectiveness_score': effectiveness_score,
                    'confidence_score': result.confidence_score,
                    'processing_time_ms': processing_time,
                    'recommendation_count': len(adaptation_commands)
                }
            }
            
        except Exception as e:
            logger.error(f"Error processing learning data: {e}")
            return {
                'adaptation_commands': [],
                'error': str(e),
                'processing_time_ms': (time.time() - start_time) * 1000
            }
            
    async def process_adaptation_request(
        self, 
        session_id: str, 
        request_type: str, 
        parameters: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Process explicit adaptation request from VR learning environment.
        
        Educational Impact:
        Responds to specific adaptation requests, enabling targeted educational
        interventions and customized learning adjustments based on explicit
        learner or system needs for optimal educational outcomes.
        
        Args:
            session_id: Unique session identifier
            request_type: Type of adaptation requested
            parameters: Request-specific parameters
            
        Returns:
            Dict containing adaptation response and educational guidance
        """
        start_time = time.time()
        
        try:
            adaptation_result = None
            
            if request_type == 'difficulty_adjustment':
                adaptation_result = await self._handle_difficulty_request(session_id, parameters)
            elif request_type == 'support_request':
                adaptation_result = await self._handle_support_request(session_id, parameters)
            elif request_type == 'content_modification':
                adaptation_result = await self._handle_content_request(session_id, parameters)
            elif request_type == 'pacing_adjustment':
                adaptation_result = await self._handle_pacing_request(session_id, parameters)
            else:
                adaptation_result = {
                    'success': False,
                    'error': f'Unknown adaptation request type: {request_type}'
                }
            
            processing_time = (time.time() - start_time) * 1000
            adaptation_result['processing_time_ms'] = processing_time
            
            return adaptation_result
            
        except Exception as e:
            logger.error(f"Error processing adaptation request: {e}")
            return {
                'success': False,
                'error': str(e),
                'processing_time_ms': (time.time() - start_time) * 1000
            }
            
    async def _generate_adaptation_strategies(
        self, 
        session_id: str, 
        integration_result: Dict[str, Any], 
        interaction_snapshot: Dict[str, Any]
    ) -> List[AdaptationCommand]:
        """
        Generate comprehensive adaptation strategies based on learning analysis.
        
        Educational Impact:
        Creates targeted educational strategies that address specific learner
        needs, optimize challenge levels, and enhance engagement based on
        real-time analysis of learning effectiveness and learner state.
        
        Args:
            session_id: Session context for adaptation
            integration_result: Mathematical learning equation analysis
            interaction_snapshot: Current learner interaction data
            
        Returns:
            List of prioritized adaptation commands
        """
        adaptation_commands = []
        
        # Extract key metrics for adaptation analysis
        learner_state = interaction_snapshot.get('learner_state', {})
        engagement_metrics = interaction_snapshot.get('engagement_metrics', {})
        performance_indicators = interaction_snapshot.get('performance_indicators', {})
        
        # Get transition decision and learning weights
        transition_decision = integration_result.get('transition_decision', {})
        learning_weights = integration_result.get('current_weights', {})
        
        # Process each adaptation strategy
        for strategy_name, strategy_processor in self.adaptation_strategies.items():
            try:
                strategy_commands = await strategy_processor(
                    session_id=session_id,
                    learner_state=learner_state,
                    engagement_metrics=engagement_metrics,
                    performance_indicators=performance_indicators,
                    transition_decision=transition_decision,
                    learning_weights=learning_weights
                )
                adaptation_commands.extend(strategy_commands)
            except Exception as e:
                logger.error(f"Error in adaptation strategy {strategy_name}: {e}")
                
        # Sort by priority (urgent first)
        adaptation_commands.sort(key=lambda cmd: cmd.priority)
        
        # Limit to top 5 commands to avoid overwhelming VR environment
        return adaptation_commands[:5]
        
    async def _process_difficulty_adaptation(
        self, 
        session_id: str, 
        learner_state: Dict[str, Any], 
        engagement_metrics: Dict[str, Any], 
        performance_indicators: Dict[str, Any], 
        transition_decision: Dict[str, Any], 
        learning_weights: Dict[str, Any]
    ) -> List[AdaptationCommand]:
        """
        Process difficulty level adaptations based on learner performance.
        
        Educational Impact:
        Optimizes challenge levels to maintain learner in optimal learning zone,
        preventing frustration from excessive difficulty or boredom from
        insufficient challenge, maximizing learning effectiveness.
        """
        commands = []
        
        # Analyze stress and competency indicators
        stress_level = learner_state.get('stress_indicators', 0.0)
        competency_confidence = learner_state.get('competency_confidence', 0.5)
        task_completion_rate = performance_indicators.get('task_completion_rate', 0.0)
        error_frequency = performance_indicators.get('error_frequency', 0.0)
        
        # High stress or low performance - reduce difficulty
        if stress_level > self.adaptation_thresholds['stress_level_high'] or \
           task_completion_rate < self.adaptation_thresholds['performance_struggling']:
            
            difficulty_reduction = min(0.3, stress_level * 0.5)
            commands.append(AdaptationCommand(
                command_type="difficulty_adjustment",
                command_action="decrease",
                target_value=1.0 - difficulty_reduction,
                reasoning=f"High stress ({stress_level:.2f}) or low completion rate ({task_completion_rate:.2f})",
                priority=2,
                educational_context="Maintaining optimal challenge level for learning progression",
                implementation_hint="Reduce task complexity, provide additional scaffolding",
                duration_estimate=5.0
            ))
            
        # High competency and low errors - increase difficulty
        elif competency_confidence > self.adaptation_thresholds['competency_ready_advance'] and \
             error_frequency < 0.1:
            
            difficulty_increase = min(0.2, competency_confidence * 0.3)
            commands.append(AdaptationCommand(
                command_type="difficulty_adjustment",
                command_action="increase",
                target_value=1.0 + difficulty_increase,
                reasoning=f"High competency ({competency_confidence:.2f}) and low errors ({error_frequency:.2f})",
                priority=3,
                educational_context="Advancing learner to appropriate challenge level",
                implementation_hint="Introduce advanced features, reduce guidance",
                duration_estimate=3.0
            ))
            
        return commands
        
    async def _process_support_adaptation(
        self, 
        session_id: str, 
        learner_state: Dict[str, Any], 
        engagement_metrics: Dict[str, Any], 
        performance_indicators: Dict[str, Any], 
        transition_decision: Dict[str, Any], 
        learning_weights: Dict[str, Any]
    ) -> List[AdaptationCommand]:
        """
        Process support level adaptations for optimal learning assistance.
        
        Educational Impact:
        Provides appropriate educational support that helps learners overcome
        challenges without creating dependency, fostering independent learning
        while ensuring educational progress and confidence building.
        """
        commands = []
        
        help_seeking_frequency = learner_state.get('help_seeking_frequency', 0.0)
        error_frequency = performance_indicators.get('error_frequency', 0.0)
        competency_confidence = learner_state.get('competency_confidence', 0.5)
        
        # High help seeking or errors - provide additional support
        if help_seeking_frequency > self.adaptation_thresholds['help_seeking_frequent'] or \
           error_frequency > self.adaptation_thresholds['error_rate_concerning']:
            
            if error_frequency > 0.3:
                # Provide contextual hints
                commands.append(AdaptationCommand(
                    command_type="support_intervention",
                    command_action="provide",
                    target_value=0.8,
                    reasoning=f"High error rate ({error_frequency:.2f}) indicates need for guidance",
                    priority=1,
                    educational_context="Providing scaffolding to support learning progression",
                    implementation_hint="Show contextual hints, highlight important UI elements",
                    duration_estimate=2.0
                ))
                
            if help_seeking_frequency > 0.15:
                # Provide tutorial reinforcement
                commands.append(AdaptationCommand(
                    command_type="support_intervention",
                    command_action="provide",
                    target_value=0.6,
                    reasoning=f"Frequent help seeking ({help_seeking_frequency:.2f}) suggests conceptual gaps",
                    priority=2,
                    educational_context="Reinforcing foundational concepts for solid understanding",
                    implementation_hint="Offer mini-tutorial or concept review",
                    duration_estimate=10.0
                ))
                
        # Low help seeking and high competency - reduce support
        elif help_seeking_frequency < 0.05 and competency_confidence > 0.7:
            commands.append(AdaptationCommand(
                command_type="support_intervention",
                command_action="reduce",
                target_value=0.3,
                reasoning=f"Low help seeking ({help_seeking_frequency:.2f}) and high competency ({competency_confidence:.2f})",
                priority=4,
                educational_context="Encouraging independent learning and self-efficacy",
                implementation_hint="Reduce automatic hints, encourage exploration",
                duration_estimate=1.0
            ))
            
        return commands
        
    async def _process_engagement_adaptation(
        self, 
        session_id: str, 
        learner_state: Dict[str, Any], 
        engagement_metrics: Dict[str, Any], 
        performance_indicators: Dict[str, Any], 
        transition_decision: Dict[str, Any], 
        learning_weights: Dict[str, Any]
    ) -> List[AdaptationCommand]:
        """
        Process engagement level adaptations for optimal learner motivation.
        
        Educational Impact:
        Maintains optimal engagement levels that promote active learning,
        flow state achievement, and sustained educational motivation,
        preventing disengagement while maintaining educational focus.
        """
        commands = []
        
        attention_level = engagement_metrics.get('attention_level', 0.5)
        interaction_quality = engagement_metrics.get('interaction_quality', 0.5)
        flow_state_indicators = engagement_metrics.get('flow_state_indicators', 0.5)
        
        # Low engagement - enhance engagement strategies
        if attention_level < self.adaptation_thresholds['engagement_low']:
            
            # Add interactive elements
            commands.append(AdaptationCommand(
                command_type="engagement_enhancement",
                command_action="increase_interactivity",
                target_value=0.8,
                reasoning=f"Low attention level ({attention_level:.2f}) requires engagement boost",
                priority=2,
                educational_context="Enhancing engagement to maintain active learning",
                implementation_hint="Add interactive elements, gamification features",
                duration_estimate=5.0
            ))
            
            # Provide variety
            if interaction_quality < 0.4:
                commands.append(AdaptationCommand(
                    command_type="engagement_enhancement",
                    command_action="add_variety",
                    target_value=0.7,
                    reasoning=f"Low interaction quality ({interaction_quality:.2f}) suggests need for variety",
                    priority=3,
                    educational_context="Adding variety to maintain educational interest",
                    implementation_hint="Introduce new interaction methods, change visual elements",
                    duration_estimate=3.0
                ))
                
        # High engagement - maintain flow state
        elif flow_state_indicators > 0.8:
            commands.append(AdaptationCommand(
                command_type="engagement_enhancement",
                command_action="maintain_flow",
                target_value=0.9,
                reasoning=f"High flow state ({flow_state_indicators:.2f}) should be preserved",
                priority=1,
                educational_context="Maintaining optimal flow state for deep learning",
                implementation_hint="Avoid interruptions, maintain current pacing",
                duration_estimate=0.5
            ))
            
        return commands
        
    async def _process_content_adaptation(
        self, 
        session_id: str, 
        learner_state: Dict[str, Any], 
        engagement_metrics: Dict[str, Any], 
        performance_indicators: Dict[str, Any], 
        transition_decision: Dict[str, Any], 
        learning_weights: Dict[str, Any]
    ) -> List[AdaptationCommand]:
        """
        Process content personalization adaptations for individual learning needs.
        
        Educational Impact:
        Personalizes educational content presentation and sequencing to match
        individual learning preferences, cognitive load capacity, and
        educational objectives for optimal knowledge acquisition.
        """
        commands = []
        
        # Analyze learning progression and content needs
        task_completion_rate = performance_indicators.get('task_completion_rate', 0.0)
        skill_demonstration = performance_indicators.get('skill_demonstration', 0.5)
        competency_confidence = learner_state.get('competency_confidence', 0.5)
        
        # Low skill demonstration - provide alternative content approach
        if skill_demonstration < 0.4:
            commands.append(AdaptationCommand(
                command_type="content_modification",
                command_action="alternative_approach",
                target_value=0.7,
                reasoning=f"Low skill demonstration ({skill_demonstration:.2f}) suggests need for different approach",
                priority=2,
                educational_context="Providing alternative learning pathway for concept mastery",
                implementation_hint="Present concept using different modality or metaphor",
                duration_estimate=8.0
            ))
            
        # High competency - provide advanced content
        elif competency_confidence > 0.8 and task_completion_rate > 0.8:
            commands.append(AdaptationCommand(
                command_type="content_modification",
                command_action="advance_content",
                target_value=1.0,
                reasoning=f"High competency ({competency_confidence:.2f}) and completion ({task_completion_rate:.2f})",
                priority=3,
                educational_context="Advancing to higher-level concepts for continued growth",
                implementation_hint="Introduce advanced features or concepts",
                duration_estimate=5.0
            ))
            
        return commands
        
    async def _process_pacing_adaptation(
        self, 
        session_id: str, 
        learner_state: Dict[str, Any], 
        engagement_metrics: Dict[str, Any], 
        performance_indicators: Dict[str, Any], 
        transition_decision: Dict[str, Any], 
        learning_weights: Dict[str, Any]
    ) -> List[AdaptationCommand]:
        """
        Process learning pacing adaptations for optimal temporal progression.
        
        Educational Impact:
        Optimizes learning pacing to match individual processing speeds,
        attention spans, and cognitive load capacity, ensuring adequate
        time for concept mastery while maintaining educational momentum.
        """
        commands = []
        
        stress_level = learner_state.get('stress_indicators', 0.0)
        attention_level = engagement_metrics.get('attention_level', 0.5)
        error_frequency = performance_indicators.get('error_frequency', 0.0)
        
        # High stress or errors - slow down pacing
        if stress_level > 0.6 or error_frequency > 0.3:
            commands.append(AdaptationCommand(
                command_type="pacing_adjustment",
                command_action="slow_down",
                target_value=0.7,
                reasoning=f"High stress ({stress_level:.2f}) or errors ({error_frequency:.2f}) require slower pacing",
                priority=2,
                educational_context="Allowing more time for concept processing and mastery",
                implementation_hint="Extend time limits, add processing breaks",
                duration_estimate=2.0
            ))
            
        # High attention and low errors - can increase pace
        elif attention_level > 0.8 and error_frequency < 0.1:
            commands.append(AdaptationCommand(
                command_type="pacing_adjustment",
                command_action="speed_up",
                target_value=1.2,
                reasoning=f"High attention ({attention_level:.2f}) and low errors ({error_frequency:.2f})",
                priority=4,
                educational_context="Maintaining engagement through appropriate pacing challenge",
                implementation_hint="Reduce wait times, provide faster progression options",
                duration_estimate=1.0
            ))
            
        return commands
        
    async def _calculate_adaptation_effectiveness(
        self, 
        adaptation_commands: List[AdaptationCommand], 
        integration_result: Dict[str, Any]
    ) -> float:
        """
        Calculate educational effectiveness score for adaptation recommendations.
        
        Educational Impact:
        Evaluates the potential educational impact of adaptation commands
        to ensure recommendations support learning objectives and maintain
        appropriate challenge levels for optimal educational outcomes.
        
        Returns:
            Effectiveness score from 0.0 to 1.0
        """
        if not adaptation_commands:
            return 0.5  # Neutral effectiveness for no adaptations
            
        # Weight effectiveness factors
        priority_score = sum(1.0 / cmd.priority for cmd in adaptation_commands) / len(adaptation_commands)
        coverage_score = min(1.0, len(adaptation_commands) / 3.0)  # Optimal 3 adaptations
        confidence_score = integration_result.get('confidence_score', 0.8)
        
        # Calculate composite effectiveness
        effectiveness = (priority_score * 0.4 + coverage_score * 0.3 + confidence_score * 0.3)
        
        return min(1.0, effectiveness)
        
    async def _generate_learning_state_update(
        self, 
        integration_result: Dict[str, Any], 
        adaptation_commands: List[AdaptationCommand]
    ) -> Dict[str, Any]:
        """
        Generate updated learning state based on adaptation processing.
        
        Educational Impact:
        Updates comprehensive learning state to reflect current educational
        context, adaptation outcomes, and projected learning progression
        for continued educational optimization.
        
        Returns:
            Dict containing updated learning state information
        """
        transition_decision = integration_result.get('transition_decision', {})
        
        return {
            'current_learning_event': transition_decision.get('recommended_event', 'introduction'),
            'progress_percentage': min(100, transition_decision.get('progress_percentage', 0) * 100),
            'competency_level': transition_decision.get('competency_assessment', 0.5),
            'adaptation_count': len(adaptation_commands),
            'last_adaptation_time': datetime.now(timezone.utc).isoformat(),
            'educational_focus': self._determine_educational_focus(adaptation_commands),
            'estimated_completion_time': self._estimate_completion_time(
                transition_decision, adaptation_commands
            )
        }
        
    async def _update_processing_metrics(self, result: AdaptationResult) -> None:
        """
        Update performance and effectiveness metrics for monitoring.
        
        Educational Impact:
        Tracks adaptation processing effectiveness and performance to
        ensure optimal educational outcomes and system performance
        for continuous improvement of learning adaptations.
        """
        # Update processing metrics
        self.processing_metrics['total_adaptations'] += 1
        
        if result.educational_effectiveness > 0.7:
            self.processing_metrics['successful_adaptations'] += 1
            
        # Update average processing time
        current_avg = self.processing_metrics['average_processing_time']
        total_adaptations = self.processing_metrics['total_adaptations']
        
        self.processing_metrics['average_processing_time'] = (
            (current_avg * (total_adaptations - 1) + result.processing_time) / total_adaptations
        )
        
        # Update average effectiveness
        current_effectiveness = self.processing_metrics['average_effectiveness']
        self.processing_metrics['average_effectiveness'] = (
            (current_effectiveness * (total_adaptations - 1) + result.educational_effectiveness) / 
            total_adaptations
        )
        
        # Update accuracy
        self.processing_metrics['adaptation_accuracy'] = (
            self.processing_metrics['successful_adaptations'] / 
            max(self.processing_metrics['total_adaptations'], 1)
        )
        
    def _format_adaptation_command(self, command: AdaptationCommand) -> Dict[str, Any]:
        """
        Format adaptation command for WebSocket transmission.
        
        Educational Impact:
        Provides clear, actionable adaptation commands for VR learning
        environment implementation, ensuring educational intent is
        preserved and implementation guidance is comprehensive.
        """
        return {
            'type': command.command_type,
            'action': command.command_action,
            'value': command.target_value,
            'reason': command.reasoning,
            'priority': command.priority,
            'educational_context': command.educational_context,
            'implementation_hint': command.implementation_hint,
            'duration_estimate': command.duration_estimate
        }
        
    def _determine_educational_focus(self, adaptation_commands: List[AdaptationCommand]) -> str:
        """
        Determine primary educational focus based on adaptation commands.
        
        Educational Impact:
        Identifies the main educational area requiring attention to
        guide VR environment focus and educational priority setting
        for optimal learning outcomes.
        """
        if not adaptation_commands:
            return "general_learning"
            
        focus_counts = {}
        for cmd in adaptation_commands:
            if cmd.command_type in focus_counts:
                focus_counts[cmd.command_type] += 1
            else:
                focus_counts[cmd.command_type] = 1
                
        primary_focus = max(focus_counts, key=focus_counts.get)
        
        focus_mapping = {
            'difficulty_adjustment': 'challenge_optimization',
            'support_intervention': 'learning_support',
            'engagement_enhancement': 'engagement_optimization',
            'content_modification': 'content_personalization',
            'pacing_adjustment': 'temporal_optimization'
        }
        
        return focus_mapping.get(primary_focus, 'general_learning')
        
    def _estimate_completion_time(
        self, 
        transition_decision: Dict[str, Any], 
        adaptation_commands: List[AdaptationCommand]
    ) -> str:
        """
        Estimate completion time based on learning state and adaptations.
        
        Educational Impact:
        Provides learners with realistic expectations for learning
        completion, supporting motivation and time management for
        optimal educational planning and engagement.
        """
        base_time = 15  # Base completion time in minutes
        progress = transition_decision.get('progress_percentage', 0.0)
        
        # Adjust based on progress
        remaining_progress = 1.0 - progress
        estimated_minutes = base_time * remaining_progress
        
        # Adjust based on adaptations
        for cmd in adaptation_commands:
            if cmd.command_type == 'difficulty_adjustment':
                if cmd.command_action == 'increase':
                    estimated_minutes *= 1.2
                elif cmd.command_action == 'decrease':
                    estimated_minutes *= 0.8
            elif cmd.command_type == 'support_intervention':
                estimated_minutes += cmd.duration_estimate / 60  # Convert seconds to minutes
                
        # Format as readable time estimate
        if estimated_minutes < 1:
            return "less than 1 minute"
        elif estimated_minutes < 60:
            return f"{int(estimated_minutes)} minutes"
        else:
            hours = int(estimated_minutes // 60)
            minutes = int(estimated_minutes % 60)
            return f"{hours}h {minutes}m"
            
    # Request handlers for explicit adaptation requests
    
    async def _handle_difficulty_request(self, session_id: str, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """Handle explicit difficulty adjustment request."""
        target_difficulty = parameters.get('target_difficulty', 0.5)
        reason = parameters.get('reason', 'explicit_request')
        
        return {
            'success': True,
            'adaptation_type': 'difficulty_adjustment',
            'target_value': target_difficulty,
            'educational_guidance': f"Adjusting difficulty to {target_difficulty:.1f} level",
            'implementation_time': '3-5 seconds'
        }
        
    async def _handle_support_request(self, session_id: str, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """Handle explicit support level request."""
        support_type = parameters.get('support_type', 'general')
        urgency = parameters.get('urgency', 'normal')
        
        return {
            'success': True,
            'adaptation_type': 'support_intervention',
            'support_type': support_type,
            'educational_guidance': f"Providing {support_type} support with {urgency} priority",
            'implementation_time': '1-2 seconds'
        }
        
    async def _handle_content_request(self, session_id: str, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """Handle explicit content modification request."""
        content_type = parameters.get('content_type', 'alternative')
        target_area = parameters.get('target_area', 'current')
        
        return {
            'success': True,
            'adaptation_type': 'content_modification',
            'content_type': content_type,
            'educational_guidance': f"Modifying {target_area} content with {content_type} approach",
            'implementation_time': '5-10 seconds'
        }
        
    async def _handle_pacing_request(self, session_id: str, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """Handle explicit pacing adjustment request."""
        pacing_direction = parameters.get('direction', 'maintain')
        intensity = parameters.get('intensity', 0.5)
        
        return {
            'success': True,
            'adaptation_type': 'pacing_adjustment',
            'pacing_direction': pacing_direction,
            'educational_guidance': f"Adjusting pacing {pacing_direction} with {intensity:.1f} intensity",
            'implementation_time': '1-3 seconds'
        }
        
    # Public metrics methods
    
    def get_adaptation_success_rate(self) -> float:
        """Get current adaptation success rate for monitoring."""
        return self.processing_metrics.get('adaptation_accuracy', 0.0)
        
    def get_learning_effectiveness_score(self) -> float:
        """Get current learning effectiveness score for monitoring."""
        return self.processing_metrics.get('average_effectiveness', 0.0)
        
    def get_processing_metrics(self) -> Dict[str, Any]:
        """Get comprehensive processing metrics for monitoring."""
        return {
            'processing_performance': self.processing_metrics.copy(),
            'educational_effectiveness': self.effectiveness_metrics.copy(),
            'adaptation_thresholds': self.adaptation_thresholds.copy()
        }
