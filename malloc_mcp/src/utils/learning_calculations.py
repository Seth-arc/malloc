"""
Learning Calculations Utility Module
Educational mathematics and adaptive learning calculation utilities.

This module implements the core mathematical functions for the Malloc VR
learning equation and adaptive learning model calculations.

Mathematical Foundation:
Core Learning Equation: ∂(t+1) = ∂(t) + α · Δ(∩(t), ∆(t), E(t), A(t)) + β · ε(t)

Where:
- ∩(t) = Learner Model at time t
- ∆(t) = Knowledge Model at time t  
- E(t) = Engagement Model at time t
- A(t) = Assessment Model at time t
- α = Adaptation strength parameter [0.1-1.0]
- β = Environmental noise factor [0.0-0.5]
- ε(t) = Environmental factors at time t

Educational Impact:
These calculations enable real-time adaptive learning by processing learner
characteristics, engagement patterns, and assessment results to optimize
learning progression and personalization.

Performance Requirements:
- All calculations: <50ms processing time
- Memory usage: <5MB for typical learning sessions
- Mathematical precision: 6 decimal places for learning weights
- Real-time adaptation: <100ms total latency

Authors: Sethu Nguna
Version: 1.0.0
Last Updated: September 2025
License: Educational Use License
"""

import numpy as np
import logging
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime, timedelta
import math
import statistics


logger = logging.getLogger(__name__)


class LearningEquationCalculator:
    """
    Core learning equation calculator for adaptive VR learning.
    
    Implements the mathematical foundation for real-time learning adaptation
    based on the integration of learner, knowledge, engagement, and assessment models.
    
    Educational Impact:
    The learning equation enables personalized learning experiences by
    dynamically adjusting to individual learner needs and progress patterns.
    
    Mathematical Precision:
    - Weight calculations: 6 decimal places
    - Learning progression: 4 decimal places  
    - Confidence intervals: 95% statistical confidence
    - Convergence criteria: 0.001 tolerance
    
    Example:
        calculator = LearningEquationCalculator()
        
        result = await calculator.calculate_transition(
            current_state={"transition_value": 0.5},
            learner_weight=0.35,
            knowledge_weight=0.25,
            engagement_weight=0.20,
            assessment_weight=0.20,
            alpha=0.7,
            beta=0.3
        )
    """
    
    def __init__(self):
        """Initialize learning equation calculator with default parameters."""
        self.precision_digits = 6
        self.convergence_tolerance = 0.001
        self.max_iterations = 100
        
    async def calculate_learning_equation(
        self,
        current_state: Dict[str, Any],
        learner_model: Dict[str, Any],
        knowledge_model: Dict[str, Any], 
        engagement_model: Dict[str, Any],
        assessment_model: Dict[str, Any],
        alpha: float = 0.7,
        beta: float = 0.3
    ) -> Dict[str, Any]:
        """
        Calculate the core learning equation for transition decisions.
        
        Implements: ∂(t+1) = ∂(t) + α · Δ(∩(t), ∆(t), E(t), A(t)) + β · ε(t)
        
        Educational Impact:
        This calculation determines optimal learning progression by integrating
        all learning model outputs into a single transition decision.
        
        Args:
            current_state: Current learning state with transition value
            learner_model: Learner model output with weight and characteristics
            knowledge_model: Knowledge model output with curriculum structure
            engagement_model: Engagement model output with interaction metrics
            assessment_model: Assessment model output with competency scores
            alpha: Adaptation strength parameter [0.1-1.0]
            beta: Environmental noise factor [0.0-0.5]
            
        Returns:
            Dict[str, Any]: Learning equation result with transition value
            
        Example:
            result = await calculate_learning_equation(
                current_state={"transition_value": 0.5, "progress": 0.3},
                learner_model={"weight": 0.35, "adaptation_params": {...}},
                knowledge_model={"weight": 0.25, "complexity": 0.6},
                engagement_model={"weight": 0.20, "score": 0.8},
                assessment_model={"weight": 0.20, "competency": 0.7},
                alpha=0.7,
                beta=0.3
            )
        """
        try:
            # Extract current transition value ∂(t)
            current_transition = current_state.get("transition_value", 0.0)
            
            # Extract model weights and outputs
            learner_weight = learner_model.get("weight", 0.35)
            knowledge_weight = knowledge_model.get("weight", 0.25)
            engagement_weight = engagement_model.get("weight", 0.20)
            assessment_weight = assessment_model.get("weight", 0.20)
            
            # Validate weight normalization
            total_weight = learner_weight + knowledge_weight + engagement_weight + assessment_weight
            if abs(total_weight - 1.0) > 0.01:
                logger.warning(f"Model weights not normalized: {total_weight}, normalizing...")
                # Normalize weights
                learner_weight /= total_weight
                knowledge_weight /= total_weight
                engagement_weight /= total_weight
                assessment_weight /= total_weight
            
            # Calculate model integration Δ(∩(t), ∆(t), E(t), A(t))
            model_integration = await self._calculate_model_integration(
                learner_model, knowledge_model, engagement_model, assessment_model,
                learner_weight, knowledge_weight, engagement_weight, assessment_weight
            )
            
            # Calculate environmental factors ε(t)
            environmental_factors = await self._calculate_environmental_factors(
                current_state, learner_model, engagement_model
            )
            
            # Apply learning equation: ∂(t+1) = ∂(t) + α · Δ + β · ε
            adaptation_term = alpha * model_integration
            noise_term = beta * environmental_factors
            
            new_transition_value = current_transition + adaptation_term + noise_term
            
            # Ensure transition value stays within valid bounds [0.0, 1.0]
            new_transition_value = max(0.0, min(1.0, new_transition_value))
            
            # Calculate confidence and stability metrics
            confidence = await self._calculate_transition_confidence(
                model_integration, environmental_factors, alpha, beta
            )
            
            stability = await self._calculate_stability_metric(
                current_transition, new_transition_value, adaptation_term
            )
            
            return {
                "transition_value": round(new_transition_value, 4),
                "previous_transition": current_transition,
                "model_integration": round(model_integration, 6),
                "environmental_factors": round(environmental_factors, 6),
                "adaptation_term": round(adaptation_term, 6),
                "noise_term": round(noise_term, 6),
                "alpha_used": alpha,
                "beta_used": beta,
                "model_weights": {
                    "learner": round(learner_weight, 6),
                    "knowledge": round(knowledge_weight, 6),
                    "engagement": round(engagement_weight, 6),
                    "assessment": round(assessment_weight, 6)
                },
                "confidence": round(confidence, 4),
                "stability": round(stability, 4),
                "calculation_timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"Learning equation calculation failed: {e}")
            raise
    
    async def _calculate_model_integration(
        self,
        learner_model: Dict[str, Any],
        knowledge_model: Dict[str, Any],
        engagement_model: Dict[str, Any],
        assessment_model: Dict[str, Any],
        learner_weight: float,
        knowledge_weight: float,
        engagement_weight: float,
        assessment_weight: float
    ) -> float:
        """
        Calculate the model integration term Δ(∩(t), ∆(t), E(t), A(t)).
        
        Educational Impact:
        Model integration combines all learning dimensions into a unified
        adaptation signal that guides learning progression decisions.
        
        Args:
            learner_model: Learner model output
            knowledge_model: Knowledge model output
            engagement_model: Engagement model output
            assessment_model: Assessment model output
            learner_weight: Weight for learner model
            knowledge_weight: Weight for knowledge model
            engagement_weight: Weight for engagement model
            assessment_weight: Weight for assessment model
            
        Returns:
            float: Integrated model value [-1.0, 1.0]
        """
        try:
            # Extract model-specific adaptation signals
            learner_signal = await self._extract_learner_signal(learner_model)
            knowledge_signal = await self._extract_knowledge_signal(knowledge_model)
            engagement_signal = await self._extract_engagement_signal(engagement_model)
            assessment_signal = await self._extract_assessment_signal(assessment_model)
            
            # Calculate weighted integration
            integration = (
                learner_weight * learner_signal +
                knowledge_weight * knowledge_signal +
                engagement_weight * engagement_signal +
                assessment_weight * assessment_signal
            )
            
            # Ensure integration stays within bounds [-1.0, 1.0]
            return max(-1.0, min(1.0, integration))
            
        except Exception as e:
            logger.error(f"Model integration calculation failed: {e}")
            return 0.0
    
    async def _extract_learner_signal(self, learner_model: Dict[str, Any]) -> float:
        """
        Extract adaptation signal from learner model.
        
        Educational Impact:
        Learner signal indicates how well the current learning approach
        matches the individual learner's characteristics and preferences.
        
        Args:
            learner_model: Learner model output with adaptation parameters
            
        Returns:
            float: Learner adaptation signal [-1.0, 1.0]
        """
        try:
            # Extract key learner characteristics
            adaptation_params = learner_model.get("adaptation_parameters", {})
            learning_preferences = learner_model.get("learning_preferences_score", 0.5)
            behavioral_analysis = learner_model.get("behavioral_analysis", {})
            
            # Calculate learner readiness for progression
            readiness_score = adaptation_params.get("readiness_score", 0.5)
            confidence_level = adaptation_params.get("confidence_level", 0.5)
            
            # Analyze behavioral patterns
            engagement_trend = behavioral_analysis.get("engagement_trend", 0.0)
            learning_pace = behavioral_analysis.get("learning_pace", 0.0)
            
            # Combine factors into adaptation signal
            signal = (
                0.4 * (readiness_score - 0.5) * 2 +  # Convert to [-1, 1]
                0.3 * (learning_preferences - 0.5) * 2 +
                0.2 * engagement_trend +
                0.1 * learning_pace
            )
            
            return max(-1.0, min(1.0, signal))
            
        except Exception as e:
            logger.error(f"Learner signal extraction failed: {e}")
            return 0.0
    
    async def _extract_knowledge_signal(self, knowledge_model: Dict[str, Any]) -> float:
        """
        Extract adaptation signal from knowledge model.
        
        Educational Impact:
        Knowledge signal indicates whether the learner is ready to progress
        based on curriculum structure and prerequisite completion.
        
        Args:
            knowledge_model: Knowledge model output with curriculum data
            
        Returns:
            float: Knowledge adaptation signal [-1.0, 1.0]
        """
        try:
            # Extract curriculum progression metrics
            path_complexity = knowledge_model.get("path_complexity", 0.5)
            prerequisite_completion = knowledge_model.get("prerequisite_completion", 0.5)
            competency_gaps = knowledge_model.get("competency_gaps", [])
            
            # Calculate knowledge readiness
            complexity_factor = 1.0 - path_complexity  # Lower complexity = higher readiness
            prerequisite_factor = prerequisite_completion
            gap_penalty = len(competency_gaps) * 0.1
            
            # Combine into knowledge signal
            signal = (
                0.5 * (prerequisite_factor - 0.5) * 2 +
                0.3 * (complexity_factor - 0.5) * 2 -
                0.2 * gap_penalty
            )
            
            return max(-1.0, min(1.0, signal))
            
        except Exception as e:
            logger.error(f"Knowledge signal extraction failed: {e}")
            return 0.0
    
    async def _extract_engagement_signal(self, engagement_model: Dict[str, Any]) -> float:
        """
        Extract adaptation signal from engagement model.
        
        Educational Impact:
        Engagement signal indicates learner motivation and attention levels
        to determine optimal pacing and challenge adjustments.
        
        Args:
            engagement_model: Engagement model output with interaction data
            
        Returns:
            float: Engagement adaptation signal [-1.0, 1.0]
        """
        try:
            # Extract engagement metrics
            engagement_score = engagement_model.get("engagement_score", 0.5)
            attention_analysis = engagement_model.get("attention_analysis", {})
            motivation_evaluation = engagement_model.get("motivation_evaluation", {})
            
            # Analyze attention patterns
            attention_level = attention_analysis.get("attention_level", 0.5)
            focus_stability = attention_analysis.get("focus_stability", 0.5)
            
            # Analyze motivation indicators
            intrinsic_motivation = motivation_evaluation.get("intrinsic_motivation", 0.5)
            task_persistence = motivation_evaluation.get("task_persistence", 0.5)
            
            # Combine into engagement signal
            signal = (
                0.4 * (engagement_score - 0.5) * 2 +
                0.3 * (attention_level - 0.5) * 2 +
                0.2 * (intrinsic_motivation - 0.5) * 2 +
                0.1 * (task_persistence - 0.5) * 2
            )
            
            return max(-1.0, min(1.0, signal))
            
        except Exception as e:
            logger.error(f"Engagement signal extraction failed: {e}")
            return 0.0
    
    async def _extract_assessment_signal(self, assessment_model: Dict[str, Any]) -> float:
        """
        Extract adaptation signal from assessment model.
        
        Educational Impact:
        Assessment signal indicates mastery level and competency development
        to guide progression and remediation decisions.
        
        Args:
            assessment_model: Assessment model output with competency data
            
        Returns:
            float: Assessment adaptation signal [-1.0, 1.0]
        """
        try:
            # Extract assessment metrics
            competency_level = assessment_model.get("competency_level", 0.5)
            skill_scores = assessment_model.get("skill_scores", {})
            accuracy_evaluation = assessment_model.get("accuracy_evaluation", {})
            
            # Calculate skill proficiency
            if skill_scores:
                avg_skill_score = statistics.mean(skill_scores.values())
            else:
                avg_skill_score = 0.5
            
            # Extract accuracy metrics
            overall_accuracy = accuracy_evaluation.get("overall_accuracy", 0.5)
            consistency = accuracy_evaluation.get("consistency", 0.5)
            
            # Combine into assessment signal
            signal = (
                0.4 * (competency_level - 0.5) * 2 +
                0.3 * (avg_skill_score - 0.5) * 2 +
                0.2 * (overall_accuracy - 0.5) * 2 +
                0.1 * (consistency - 0.5) * 2
            )
            
            return max(-1.0, min(1.0, signal))
            
        except Exception as e:
            logger.error(f"Assessment signal extraction failed: {e}")
            return 0.0
    
    async def _calculate_environmental_factors(
        self,
        current_state: Dict[str, Any],
        learner_model: Dict[str, Any],
        engagement_model: Dict[str, Any]
    ) -> float:
        """
        Calculate environmental factors ε(t) for the learning equation.
        
        Educational Impact:
        Environmental factors account for external influences on learning
        such as session context, time factors, and external distractions.
        
        Args:
            current_state: Current learning state and context
            learner_model: Learner model with individual characteristics
            engagement_model: Engagement model with interaction patterns
            
        Returns:
            float: Environmental factor value [-0.5, 0.5]
        """
        try:
            # Extract contextual factors
            session_duration = current_state.get("session_duration", 0)
            time_of_day = current_state.get("time_of_day", 12)  # 24-hour format
            learning_environment = current_state.get("environment", "standard")
            
            # Calculate fatigue factor based on session duration
            fatigue_factor = self._calculate_fatigue_factor(session_duration)
            
            # Calculate time-of-day influence
            time_factor = self._calculate_time_factor(time_of_day)
            
            # Calculate environment stability
            environment_factor = self._calculate_environment_factor(learning_environment)
            
            # Extract learner-specific environmental sensitivity
            environmental_sensitivity = learner_model.get("environmental_sensitivity", 0.5)
            
            # Combine environmental factors
            base_environmental = (
                0.4 * fatigue_factor +
                0.3 * time_factor +
                0.3 * environment_factor
            )
            
            # Apply learner sensitivity
            environmental_noise = base_environmental * environmental_sensitivity
            
            # Ensure environmental factors stay within bounds [-0.5, 0.5]
            return max(-0.5, min(0.5, environmental_noise))
            
        except Exception as e:
            logger.error(f"Environmental factors calculation failed: {e}")
            return 0.0
    
    def _calculate_fatigue_factor(self, session_duration: float) -> float:
        """
        Calculate fatigue factor based on session duration.
        
        Args:
            session_duration: Session duration in minutes
            
        Returns:
            float: Fatigue factor [-0.5, 0.5]
        """
        # Optimal session duration: 20-30 minutes
        optimal_duration = 25.0
        
        if session_duration <= optimal_duration:
            # Early session, slight positive boost
            return 0.1 * (session_duration / optimal_duration - 0.5)
        else:
            # Fatigue increases after optimal duration
            excess_duration = session_duration - optimal_duration
            fatigue = -0.02 * excess_duration  # 2% fatigue per minute over optimal
            return max(-0.5, fatigue)
    
    def _calculate_time_factor(self, time_of_day: int) -> float:
        """
        Calculate time-of-day learning effectiveness factor.
        
        Args:
            time_of_day: Hour of day (0-23)
            
        Returns:
            float: Time factor [-0.3, 0.3]
        """
        # Peak learning hours: 9-11 AM and 2-4 PM
        peak_hours = [9, 10, 11, 14, 15, 16]
        low_hours = [0, 1, 2, 3, 4, 5, 22, 23]
        
        if time_of_day in peak_hours:
            return 0.2
        elif time_of_day in low_hours:
            return -0.2
        else:
            return 0.0
    
    def _calculate_environment_factor(self, environment: str) -> float:
        """
        Calculate learning environment stability factor.
        
        Args:
            environment: Learning environment type
            
        Returns:
            float: Environment factor [-0.3, 0.3]
        """
        environment_scores = {
            "optimal": 0.3,
            "standard": 0.0,
            "noisy": -0.2,
            "distracted": -0.3,
            "mobile": -0.1
        }
        
        return environment_scores.get(environment, 0.0)
    
    async def _calculate_transition_confidence(
        self,
        model_integration: float,
        environmental_factors: float,
        alpha: float,
        beta: float
    ) -> float:
        """
        Calculate confidence in the transition decision.
        
        Educational Impact:
        Transition confidence helps determine whether to proceed with
        the calculated transition or maintain current learning state.
        
        Args:
            model_integration: Integrated model value
            environmental_factors: Environmental noise value
            alpha: Adaptation strength parameter
            beta: Environmental noise factor
            
        Returns:
            float: Confidence value [0.0, 1.0]
        """
        try:
            # Higher model integration values indicate clearer direction
            signal_strength = abs(model_integration)
            
            # Lower environmental noise increases confidence
            noise_level = abs(environmental_factors)
            
            # Strong adaptation parameters increase confidence
            adaptation_confidence = alpha
            
            # Calculate base confidence
            base_confidence = (
                0.5 * signal_strength +
                0.3 * (1.0 - noise_level) +
                0.2 * adaptation_confidence
            )
            
            # Boost confidence when all models agree (high signal strength)
            if signal_strength > 0.7:
                base_confidence += 0.1
            
            # Reduce confidence with high environmental noise
            if noise_level > 0.3:
                base_confidence -= 0.1
            
            return max(0.0, min(1.0, base_confidence))
            
        except Exception as e:
            logger.error(f"Transition confidence calculation failed: {e}")
            return 0.5
    
    async def _calculate_stability_metric(
        self,
        previous_transition: float,
        new_transition: float,
        adaptation_term: float
    ) -> float:
        """
        Calculate stability metric for transition changes.
        
        Educational Impact:
        Stability metrics help prevent rapid oscillations in learning
        progression that could confuse or frustrate learners.
        
        Args:
            previous_transition: Previous transition value
            new_transition: New calculated transition value
            adaptation_term: Adaptation term from learning equation
            
        Returns:
            float: Stability metric [0.0, 1.0]
        """
        try:
            # Calculate transition change magnitude
            transition_change = abs(new_transition - previous_transition)
            
            # Small changes indicate stability
            if transition_change < 0.1:
                stability = 1.0
            elif transition_change < 0.3:
                stability = 0.8
            elif transition_change < 0.5:
                stability = 0.6
            else:
                stability = 0.4
            
            # Adjust for adaptation term strength
            adaptation_strength = abs(adaptation_term)
            if adaptation_strength > 0.5:
                # Strong adaptation reduces stability but may be necessary
                stability *= 0.8
            
            return max(0.0, min(1.0, stability))
            
        except Exception as e:
            logger.error(f"Stability metric calculation failed: {e}")
            return 0.5


# Utility functions for common learning calculations
async def calculate_learner_model_weight(
    static_profile: Dict[str, Any],
    dynamic_profile: Dict[str, Any]
) -> float:
    """
    Calculate learner model weight for integration equation.
    
    Educational Impact:
    Learner model weight determines how much influence individual
    learner characteristics have on learning progression decisions.
    
    Args:
        static_profile: Static learner characteristics
        dynamic_profile: Dynamic behavioral data
        
    Returns:
        float: Learner model weight [0.25, 0.40]
    """
    try:
        # Extract key factors
        demographic = static_profile.get("demographic", {})
        learning_preferences = static_profile.get("learning_preferences", {})
        
        knowledge_level = demographic.get("current_knowledge_level", "beginner")
        guidance_preference = learning_preferences.get("guidance_level", "moderate")
        interaction_style = learning_preferences.get("interaction_style", "guided")
        
        # Map knowledge level to base weight
        knowledge_weights = {
            "novice": 0.40,      # High learner influence for beginners
            "beginner": 0.35,
            "intermediate": 0.30,
            "advanced": 0.25,    # Low learner influence for experts
            "expert": 0.25
        }
        
        base_weight = knowledge_weights.get(knowledge_level, 0.35)
        
        # Adjust based on guidance preference
        guidance_adjustments = {
            "high": 0.05,        # Need more personalization
            "moderate": 0.0,
            "low": -0.03,        # Less personalization needed
            "adaptive": 0.02     # Slight boost for adaptive learners
        }
        
        guidance_adjustment = guidance_adjustments.get(guidance_preference, 0.0)
        
        # Adjust based on interaction style
        style_adjustments = {
            "guided": 0.02,      # Guided learners need more personalization
            "independent": -0.02, # Independent learners need less
            "collaborative": 0.01 # Collaborative learners moderate adjustment
        }
        
        style_adjustment = style_adjustments.get(interaction_style, 0.0)
        
        # Calculate final weight
        final_weight = base_weight + guidance_adjustment + style_adjustment
        
        # Ensure weight stays within valid range [0.25, 0.40]
        return max(0.25, min(0.40, final_weight))
        
    except Exception as e:
        logger.error(f"Learner model weight calculation failed: {e}")
        return 0.35  # Default weight


async def calculate_engagement_score(interaction_data: Dict[str, Any]) -> float:
    """
    Calculate overall engagement score from interaction data.
    
    Educational Impact:
    Engagement score provides a unified metric for learner motivation
    and attention that guides real-time learning adaptations.
    
    Args:
        interaction_data: VR interaction and engagement metrics
        
    Returns:
        float: Engagement score [0.0, 1.0]
    """
    try:
        # Extract interaction metrics
        duration_minutes = interaction_data.get("duration_minutes", 0)
        interaction_count = interaction_data.get("interaction_count", 0)
        
        # Extract attention metrics
        attention_metrics = interaction_data.get("attention_metrics", {})
        focus_duration = attention_metrics.get("focus_duration", 0)
        distraction_events = attention_metrics.get("distraction_events", 0)
        
        # Extract motivation indicators
        motivation_indicators = interaction_data.get("motivation_indicators", {})
        task_completion_rate = motivation_indicators.get("task_completion_rate", 0.0)
        retry_attempts = motivation_indicators.get("retry_attempts", 0)
        help_seeking = motivation_indicators.get("help_seeking_frequency", 0)
        
        # Calculate engagement components
        duration_score = min(1.0, duration_minutes / 30.0)  # Normalize to 30 min
        interaction_score = min(1.0, interaction_count / 50.0)  # Normalize to 50 interactions
        
        # Calculate attention score
        if duration_minutes > 0:
            attention_score = focus_duration / duration_minutes
            distraction_penalty = min(0.3, distraction_events * 0.05)
            attention_score = max(0.0, attention_score - distraction_penalty)
        else:
            attention_score = 0.0
        
        # Calculate motivation score
        motivation_score = task_completion_rate
        if retry_attempts > 0:
            motivation_score += min(0.1, retry_attempts * 0.02)  # Slight boost for persistence
        if help_seeking > 5:
            motivation_score -= min(0.1, (help_seeking - 5) * 0.01)  # Penalty for excessive help
        
        # Combine engagement components
        engagement_score = (
            0.3 * duration_score +
            0.25 * interaction_score +
            0.25 * attention_score +
            0.2 * motivation_score
        )
        
        return max(0.0, min(1.0, engagement_score))
        
    except Exception as e:
        logger.error(f"Engagement score calculation failed: {e}")
        return 0.5  # Default moderate engagement
