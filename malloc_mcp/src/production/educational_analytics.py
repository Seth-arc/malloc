"""
Educational Data Analytics Platform for Malloc VR MCP Server

Educational Impact:
Provides comprehensive learning effectiveness tracking and insights to optimize
educational outcomes and validate adaptive learning algorithm performance.

Performance Requirements:
- Analytics processing: <200ms
- Real-time dashboard updates: <5 seconds
- Data retention: 30 days minimum
- Educational insight generation: <1 second

Author: Malloc VR Learning Team
Date: December 26, 2024
"""

import asyncio
import time
import logging
import json
import sqlite3
import aiosqlite
import statistics
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Tuple, Union
from dataclasses import dataclass, asdict
from enum import Enum
from collections import defaultdict, deque
import pandas as pd
from sklearn.metrics import accuracy_score, mean_absolute_error
import threading

from ..utils.learning_calculations import LearningCalculations
from ..learning.integration_engine import LearningIntegrationEngine


class LearningEventType(Enum):
    """Types of learning events tracked"""
    ONBOARDING = "onboarding"
    INTRODUCTION = "introduction"
    PRACTICE = "practice"
    APPLICATION = "application"
    MASTERY = "mastery"


class AnalyticsMetricType(Enum):
    """Types of analytics metrics"""
    EFFECTIVENESS = "effectiveness"
    ENGAGEMENT = "engagement"
    PERFORMANCE = "performance"
    ADAPTATION = "adaptation"
    OUTCOME = "outcome"


@dataclass
class LearningOutcome:
    """Individual learning outcome measurement"""
    learner_id: str
    event_type: LearningEventType
    timestamp: datetime
    competency_before: float
    competency_after: float
    engagement_score: float
    adaptation_applied: bool
    adaptation_effectiveness: float
    session_duration_minutes: float
    vr_interaction_quality: float
    educational_objective_met: bool


@dataclass
class EducationalInsight:
    """Educational effectiveness insight"""
    insight_type: str
    title: str
    description: str
    significance: str  # "low", "medium", "high", "critical"
    learning_impact: float  # 0.0-1.0
    recommendation: str
    supporting_data: Dict[str, Any]
    confidence_score: float  # 0.0-1.0
    generated_at: datetime


@dataclass
class AdaptationAnalysis:
    """Analysis of adaptation algorithm effectiveness"""
    adaptation_id: str
    learner_profile: Dict[str, Any]
    original_state: Dict[str, Any]
    adapted_state: Dict[str, Any]
    predicted_outcome: float
    actual_outcome: float
    accuracy_score: float
    adaptation_timestamp: datetime
    outcome_timestamp: datetime
    educational_context: str


class LearningDataProcessor:
    """
    Processes and analyzes learning data for educational insights
    
    Educational Impact:
    Transforms raw learning interaction data into actionable educational
    insights for continuous improvement of learning effectiveness.
    
    Performance Requirements:
    - Data processing: <100ms per learning event
    - Batch analysis: <5 seconds for 1000 events
    - Memory usage: <200MB for analytics processing
    """
    
    def __init__(self, database_path: str = "data/educational_analytics.db"):
        self.database_path = database_path
        self.logger = logging.getLogger(__name__)
        self.processing_lock = threading.Lock()
        
        # Analytics caching
        self.recent_outcomes = deque(maxlen=1000)
        self.adaptation_history = deque(maxlen=500)
        self.insight_cache = {}
        
        # Performance tracking
        self.processing_stats = {
            "events_processed": 0,
            "insights_generated": 0,
            "adaptations_analyzed": 0,
            "processing_time_total": 0.0
        }
    
    async def initialize_database(self) -> None:
        """Initialize analytics database"""
        try:
            async with aiosqlite.connect(self.database_path) as db:
                # Learning outcomes table
                await db.execute("""
                    CREATE TABLE IF NOT EXISTS learning_outcomes (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        learner_id TEXT NOT NULL,
                        event_type TEXT NOT NULL,
                        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                        competency_before REAL,
                        competency_after REAL,
                        engagement_score REAL,
                        adaptation_applied BOOLEAN,
                        adaptation_effectiveness REAL,
                        session_duration_minutes REAL,
                        vr_interaction_quality REAL,
                        educational_objective_met BOOLEAN
                    )
                """)
                
                # Educational insights table
                await db.execute("""
                    CREATE TABLE IF NOT EXISTS educational_insights (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        insight_type TEXT NOT NULL,
                        title TEXT NOT NULL,
                        description TEXT,
                        significance TEXT,
                        learning_impact REAL,
                        recommendation TEXT,
                        supporting_data TEXT,
                        confidence_score REAL,
                        generated_at DATETIME DEFAULT CURRENT_TIMESTAMP
                    )
                """)
                
                # Adaptation analysis table
                await db.execute("""
                    CREATE TABLE IF NOT EXISTS adaptation_analysis (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        adaptation_id TEXT NOT NULL,
                        learner_profile TEXT,
                        original_state TEXT,
                        adapted_state TEXT,
                        predicted_outcome REAL,
                        actual_outcome REAL,
                        accuracy_score REAL,
                        adaptation_timestamp DATETIME,
                        outcome_timestamp DATETIME,
                        educational_context TEXT
                    )
                """)
                
                # Create indexes for performance
                await db.execute("CREATE INDEX IF NOT EXISTS idx_learner_timestamp ON learning_outcomes(learner_id, timestamp)")
                await db.execute("CREATE INDEX IF NOT EXISTS idx_event_type ON learning_outcomes(event_type)")
                await db.execute("CREATE INDEX IF NOT EXISTS idx_insight_type ON educational_insights(insight_type)")
                
                await db.commit()
                
        except Exception as e:
            self.logger.error(f"Failed to initialize analytics database: {e}")
    
    async def process_learning_event(self, outcome: LearningOutcome) -> None:
        """
        Process individual learning event for analytics
        
        Educational Impact:
        Captures and analyzes each learning interaction to build comprehensive
        understanding of educational effectiveness and learner progress.
        
        Args:
            outcome: Learning outcome data to process
        """
        start_time = time.time()
        
        try:
            with self.processing_lock:
                # Add to recent outcomes cache
                self.recent_outcomes.append(outcome)
                
                # Store in database
                await self._store_learning_outcome(outcome)
                
                # Update processing statistics
                self.processing_stats["events_processed"] += 1
                processing_time = time.time() - start_time
                self.processing_stats["processing_time_total"] += processing_time
                
                self.logger.debug(f"Processed learning event for {outcome.learner_id} in {processing_time*1000:.2f}ms")
                
        except Exception as e:
            self.logger.error(f"Failed to process learning event: {e}")
    
    async def _store_learning_outcome(self, outcome: LearningOutcome) -> None:
        """Store learning outcome in database"""
        try:
            async with aiosqlite.connect(self.database_path) as db:
                await db.execute("""
                    INSERT INTO learning_outcomes (
                        learner_id, event_type, timestamp, competency_before, competency_after,
                        engagement_score, adaptation_applied, adaptation_effectiveness,
                        session_duration_minutes, vr_interaction_quality, educational_objective_met
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    outcome.learner_id,
                    outcome.event_type.value,
                    outcome.timestamp,
                    outcome.competency_before,
                    outcome.competency_after,
                    outcome.engagement_score,
                    outcome.adaptation_applied,
                    outcome.adaptation_effectiveness,
                    outcome.session_duration_minutes,
                    outcome.vr_interaction_quality,
                    outcome.educational_objective_met
                ))
                await db.commit()
                
        except Exception as e:
            self.logger.error(f"Failed to store learning outcome: {e}")
    
    async def analyze_learning_effectiveness(self, time_period_hours: int = 24) -> Dict[str, Any]:
        """
        Analyze overall learning effectiveness over time period
        
        Educational Impact:
        Provides comprehensive assessment of learning algorithm effectiveness
        and identifies opportunities for educational improvement.
        
        Args:
            time_period_hours: Time period for analysis
        
        Returns:
            Comprehensive learning effectiveness analysis
        """
        try:
            cutoff_time = datetime.now() - timedelta(hours=time_period_hours)
            
            # Get recent learning outcomes
            async with aiosqlite.connect(self.database_path) as db:
                cursor = await db.execute("""
                    SELECT * FROM learning_outcomes 
                    WHERE timestamp > ? 
                    ORDER BY timestamp DESC
                """, (cutoff_time,))
                rows = await cursor.fetchall()
                columns = [description[0] for description in cursor.description]
            
            if not rows:
                return {"error": "No learning data available for analysis"}
            
            # Convert to structured data
            outcomes_data = [dict(zip(columns, row)) for row in rows]
            
            # Calculate effectiveness metrics
            total_sessions = len(outcomes_data)
            
            # Competency improvement
            competency_improvements = [
                (row["competency_after"] - row["competency_before"])
                for row in outcomes_data
                if row["competency_before"] is not None and row["competency_after"] is not None
            ]
            avg_competency_improvement = statistics.mean(competency_improvements) if competency_improvements else 0
            
            # Engagement analysis
            engagement_scores = [row["engagement_score"] for row in outcomes_data if row["engagement_score"] is not None]
            avg_engagement = statistics.mean(engagement_scores) if engagement_scores else 0
            
            # Success rate
            successful_sessions = sum(1 for row in outcomes_data if row["educational_objective_met"])
            success_rate = (successful_sessions / total_sessions) * 100 if total_sessions > 0 else 0
            
            # Adaptation effectiveness
            adapted_sessions = [row for row in outcomes_data if row["adaptation_applied"]]
            adaptation_effectiveness = []
            for session in adapted_sessions:
                if session["adaptation_effectiveness"] is not None:
                    adaptation_effectiveness.append(session["adaptation_effectiveness"])
            
            avg_adaptation_effectiveness = statistics.mean(adaptation_effectiveness) if adaptation_effectiveness else 0
            
            # VR interaction quality
            vr_quality_scores = [row["vr_interaction_quality"] for row in outcomes_data if row["vr_interaction_quality"] is not None]
            avg_vr_quality = statistics.mean(vr_quality_scores) if vr_quality_scores else 0
            
            # Learning event distribution
            event_distribution = defaultdict(int)
            for row in outcomes_data:
                event_distribution[row["event_type"]] += 1
            
            return {
                "analysis_period_hours": time_period_hours,
                "total_sessions": total_sessions,
                "metrics": {
                    "competency_improvement": {
                        "average": round(avg_competency_improvement, 3),
                        "count": len(competency_improvements)
                    },
                    "engagement": {
                        "average_score": round(avg_engagement, 3),
                        "count": len(engagement_scores)
                    },
                    "success_rate": round(success_rate, 2),
                    "adaptation_effectiveness": round(avg_adaptation_effectiveness, 3),
                    "vr_interaction_quality": round(avg_vr_quality, 3)
                },
                "learning_event_distribution": dict(event_distribution),
                "adaptation_statistics": {
                    "total_adaptations": len(adapted_sessions),
                    "adaptation_rate": round((len(adapted_sessions) / total_sessions) * 100, 2) if total_sessions > 0 else 0
                }
            }
            
        except Exception as e:
            self.logger.error(f"Failed to analyze learning effectiveness: {e}")
            return {"error": f"Analysis failed: {str(e)}"}
    
    async def generate_educational_insights(self) -> List[EducationalInsight]:
        """
        Generate actionable educational insights from learning data
        
        Educational Impact:
        Identifies patterns and opportunities in learning data to guide
        educational strategy improvements and learner support optimization.
        
        Returns:
            List of educational insights with recommendations
        """
        insights = []
        
        try:
            # Analyze recent learning effectiveness
            effectiveness_data = await self.analyze_learning_effectiveness(24)
            
            if "error" not in effectiveness_data:
                insights.extend(await self._analyze_effectiveness_insights(effectiveness_data))
                insights.extend(await self._analyze_engagement_insights(effectiveness_data))
                insights.extend(await self._analyze_adaptation_insights(effectiveness_data))
                insights.extend(await self._analyze_vr_insights(effectiveness_data))
            
            # Store insights in database
            for insight in insights:
                await self._store_educational_insight(insight)
            
            self.processing_stats["insights_generated"] += len(insights)
            
            return insights
            
        except Exception as e:
            self.logger.error(f"Failed to generate educational insights: {e}")
            return []
    
    async def _analyze_effectiveness_insights(self, data: Dict[str, Any]) -> List[EducationalInsight]:
        """Analyze learning effectiveness patterns"""
        insights = []
        
        success_rate = data["metrics"]["success_rate"]
        competency_improvement = data["metrics"]["competency_improvement"]["average"]
        
        # Success rate insights
        if success_rate < 70:
            insights.append(EducationalInsight(
                insight_type="effectiveness",
                title="Low Learning Success Rate",
                description=f"Current success rate of {success_rate:.1f}% is below optimal threshold of 85%",
                significance="high",
                learning_impact=0.8,
                recommendation="Review curriculum difficulty and provide additional scaffolding for struggling learners",
                supporting_data={"success_rate": success_rate, "threshold": 85},
                confidence_score=0.9,
                generated_at=datetime.now()
            ))
        elif success_rate > 95:
            insights.append(EducationalInsight(
                insight_type="effectiveness",
                title="High Learning Success Rate",
                description=f"Success rate of {success_rate:.1f}% indicates excellent learning effectiveness",
                significance="medium",
                learning_impact=0.6,
                recommendation="Consider increasing challenge level to optimize learning growth",
                supporting_data={"success_rate": success_rate},
                confidence_score=0.8,
                generated_at=datetime.now()
            ))
        
        # Competency improvement insights
        if competency_improvement < 0.1:
            insights.append(EducationalInsight(
                insight_type="effectiveness",
                title="Low Competency Growth",
                description=f"Average competency improvement of {competency_improvement:.3f} indicates slow learning progress",
                significance="high",
                learning_impact=0.9,
                recommendation="Implement more personalized learning paths and increase adaptation frequency",
                supporting_data={"competency_improvement": competency_improvement, "target": 0.2},
                confidence_score=0.85,
                generated_at=datetime.now()
            ))
        
        return insights
    
    async def _analyze_engagement_insights(self, data: Dict[str, Any]) -> List[EducationalInsight]:
        """Analyze engagement patterns"""
        insights = []
        
        engagement_score = data["metrics"]["engagement"]["average_score"]
        
        if engagement_score < 0.7:
            insights.append(EducationalInsight(
                insight_type="engagement",
                title="Low Learner Engagement",
                description=f"Average engagement score of {engagement_score:.2f} indicates attention challenges",
                significance="high",
                learning_impact=0.85,
                recommendation="Implement more interactive VR elements and gamification strategies",
                supporting_data={"engagement_score": engagement_score, "target": 0.8},
                confidence_score=0.9,
                generated_at=datetime.now()
            ))
        elif engagement_score > 0.9:
            insights.append(EducationalInsight(
                insight_type="engagement",
                title="Excellent Learner Engagement",
                description=f"High engagement score of {engagement_score:.2f} indicates optimal attention levels",
                significance="medium",
                learning_impact=0.7,
                recommendation="Maintain current engagement strategies and consider expanding to other learning areas",
                supporting_data={"engagement_score": engagement_score},
                confidence_score=0.8,
                generated_at=datetime.now()
            ))
        
        return insights
    
    async def _analyze_adaptation_insights(self, data: Dict[str, Any]) -> List[EducationalInsight]:
        """Analyze adaptation effectiveness"""
        insights = []
        
        adaptation_rate = data["adaptation_statistics"]["adaptation_rate"]
        adaptation_effectiveness = data["metrics"]["adaptation_effectiveness"]
        
        if adaptation_rate < 30:
            insights.append(EducationalInsight(
                insight_type="adaptation",
                title="Low Adaptation Frequency",
                description=f"Adaptation rate of {adaptation_rate:.1f}% may indicate missed personalization opportunities",
                significance="medium",
                learning_impact=0.6,
                recommendation="Lower adaptation thresholds to increase personalization frequency",
                supporting_data={"adaptation_rate": adaptation_rate, "target": 50},
                confidence_score=0.7,
                generated_at=datetime.now()
            ))
        
        if adaptation_effectiveness < 0.6:
            insights.append(EducationalInsight(
                insight_type="adaptation",
                title="Low Adaptation Effectiveness",
                description=f"Adaptation effectiveness of {adaptation_effectiveness:.2f} suggests suboptimal personalization",
                significance="high",
                learning_impact=0.8,
                recommendation="Review adaptation algorithm parameters and learning model weights",
                supporting_data={"adaptation_effectiveness": adaptation_effectiveness, "target": 0.8},
                confidence_score=0.85,
                generated_at=datetime.now()
            ))
        
        return insights
    
    async def _analyze_vr_insights(self, data: Dict[str, Any]) -> List[EducationalInsight]:
        """Analyze VR interaction quality"""
        insights = []
        
        vr_quality = data["metrics"]["vr_interaction_quality"]
        
        if vr_quality < 0.7:
            insights.append(EducationalInsight(
                insight_type="performance",
                title="VR Interaction Quality Issues",
                description=f"VR interaction quality of {vr_quality:.2f} indicates technical or usability challenges",
                significance="high",
                learning_impact=0.7,
                recommendation="Optimize VR interface design and ensure Quest 3 performance requirements are met",
                supporting_data={"vr_quality": vr_quality, "target": 0.85},
                confidence_score=0.8,
                generated_at=datetime.now()
            ))
        
        return insights
    
    async def _store_educational_insight(self, insight: EducationalInsight) -> None:
        """Store educational insight in database"""
        try:
            async with aiosqlite.connect(self.database_path) as db:
                await db.execute("""
                    INSERT INTO educational_insights (
                        insight_type, title, description, significance, learning_impact,
                        recommendation, supporting_data, confidence_score, generated_at
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    insight.insight_type,
                    insight.title,
                    insight.description,
                    insight.significance,
                    insight.learning_impact,
                    insight.recommendation,
                    json.dumps(insight.supporting_data),
                    insight.confidence_score,
                    insight.generated_at
                ))
                await db.commit()
                
        except Exception as e:
            self.logger.error(f"Failed to store educational insight: {e}")
    
    def get_processing_statistics(self) -> Dict[str, Any]:
        """Get analytics processing statistics"""
        total_time = self.processing_stats["processing_time_total"]
        events_processed = self.processing_stats["events_processed"]
        
        avg_processing_time = (total_time / events_processed * 1000) if events_processed > 0 else 0
        
        return {
            "events_processed": events_processed,
            "insights_generated": self.processing_stats["insights_generated"],
            "adaptations_analyzed": self.processing_stats["adaptations_analyzed"],
            "average_processing_time_ms": round(avg_processing_time, 2),
            "total_processing_time_seconds": round(total_time, 2),
            "cache_sizes": {
                "recent_outcomes": len(self.recent_outcomes),
                "adaptation_history": len(self.adaptation_history),
                "insight_cache": len(self.insight_cache)
            }
        }


class AdaptationEffectivenessAnalyzer:
    """
    Analyzes the effectiveness of learning adaptations
    
    Educational Impact:
    Validates and improves the learning adaptation algorithm by measuring
    prediction accuracy and educational outcome correlation.
    
    Performance Requirements:
    - Analysis completion: <500ms
    - Prediction accuracy tracking: >90%
    - Memory usage: <50MB
    """
    
    def __init__(self, data_processor: LearningDataProcessor):
        self.data_processor = data_processor
        self.logger = logging.getLogger(__name__)
        
        # Analysis tracking
        self.adaptation_predictions = deque(maxlen=1000)
        self.accuracy_history = deque(maxlen=100)
        
    async def analyze_adaptation(self, analysis: AdaptationAnalysis) -> Dict[str, Any]:
        """
        Analyze individual adaptation effectiveness
        
        Educational Impact:
        Measures how well the adaptation algorithm predicts and improves
        learning outcomes for continuous algorithm improvement.
        
        Args:
            analysis: Adaptation analysis data
        
        Returns:
            Comprehensive adaptation effectiveness assessment
        """
        try:
            # Store adaptation analysis
            await self._store_adaptation_analysis(analysis)
            
            # Add to tracking
            self.adaptation_predictions.append({
                "predicted": analysis.predicted_outcome,
                "actual": analysis.actual_outcome,
                "timestamp": analysis.outcome_timestamp
            })
            
            # Calculate accuracy
            accuracy = 1.0 - abs(analysis.predicted_outcome - analysis.actual_outcome)
            self.accuracy_history.append(accuracy)
            
            # Calculate recent accuracy trend
            recent_accuracy = statistics.mean(list(self.accuracy_history)[-10:]) if self.accuracy_history else 0
            
            # Determine effectiveness level
            effectiveness_level = self._determine_effectiveness_level(accuracy, recent_accuracy)
            
            result = {
                "adaptation_id": analysis.adaptation_id,
                "individual_accuracy": round(accuracy, 3),
                "recent_average_accuracy": round(recent_accuracy, 3),
                "effectiveness_level": effectiveness_level,
                "prediction_error": abs(analysis.predicted_outcome - analysis.actual_outcome),
                "educational_context": analysis.educational_context,
                "analysis_timestamp": datetime.now().isoformat()
            }
            
            self.data_processor.processing_stats["adaptations_analyzed"] += 1
            return result
            
        except Exception as e:
            self.logger.error(f"Failed to analyze adaptation effectiveness: {e}")
            return {"error": f"Analysis failed: {str(e)}"}
    
    async def _store_adaptation_analysis(self, analysis: AdaptationAnalysis) -> None:
        """Store adaptation analysis in database"""
        try:
            async with aiosqlite.connect(self.data_processor.database_path) as db:
                await db.execute("""
                    INSERT INTO adaptation_analysis (
                        adaptation_id, learner_profile, original_state, adapted_state,
                        predicted_outcome, actual_outcome, accuracy_score,
                        adaptation_timestamp, outcome_timestamp, educational_context
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    analysis.adaptation_id,
                    json.dumps(analysis.learner_profile),
                    json.dumps(analysis.original_state),
                    json.dumps(analysis.adapted_state),
                    analysis.predicted_outcome,
                    analysis.actual_outcome,
                    analysis.accuracy_score,
                    analysis.adaptation_timestamp,
                    analysis.outcome_timestamp,
                    analysis.educational_context
                ))
                await db.commit()
                
        except Exception as e:
            self.logger.error(f"Failed to store adaptation analysis: {e}")
    
    def _determine_effectiveness_level(self, accuracy: float, recent_accuracy: float) -> str:
        """Determine adaptation effectiveness level"""
        if accuracy > 0.9 and recent_accuracy > 0.85:
            return "excellent"
        elif accuracy > 0.8 and recent_accuracy > 0.75:
            return "good"
        elif accuracy > 0.7 and recent_accuracy > 0.65:
            return "acceptable"
        else:
            return "needs_improvement"
    
    async def get_adaptation_summary(self, hours: int = 24) -> Dict[str, Any]:
        """Get comprehensive adaptation effectiveness summary"""
        try:
            cutoff_time = datetime.now() - timedelta(hours=hours)
            
            # Get recent adaptations
            recent_predictions = [
                p for p in self.adaptation_predictions
                if p["timestamp"] > cutoff_time
            ]
            
            if not recent_predictions:
                return {"error": "No recent adaptation data available"}
            
            # Calculate metrics
            predictions = [p["predicted"] for p in recent_predictions]
            actuals = [p["actual"] for p in recent_predictions]
            
            mae = mean_absolute_error(actuals, predictions)
            
            # Accuracy distribution
            accuracies = [1.0 - abs(p["predicted"] - p["actual"]) for p in recent_predictions]
            
            return {
                "analysis_period_hours": hours,
                "total_adaptations": len(recent_predictions),
                "metrics": {
                    "mean_absolute_error": round(mae, 4),
                    "average_accuracy": round(statistics.mean(accuracies), 3),
                    "accuracy_std": round(statistics.stdev(accuracies), 3) if len(accuracies) > 1 else 0,
                    "min_accuracy": round(min(accuracies), 3),
                    "max_accuracy": round(max(accuracies), 3)
                },
                "recent_trend": {
                    "last_10_average": round(statistics.mean(list(self.accuracy_history)[-10:]), 3) if self.accuracy_history else 0,
                    "trend_direction": self._calculate_trend_direction()
                }
            }
            
        except Exception as e:
            self.logger.error(f"Failed to get adaptation summary: {e}")
            return {"error": f"Summary generation failed: {str(e)}"}
    
    def _calculate_trend_direction(self) -> str:
        """Calculate recent accuracy trend direction"""
        if len(self.accuracy_history) < 5:
            return "insufficient_data"
        
        recent_5 = list(self.accuracy_history)[-5:]
        first_half = statistics.mean(recent_5[:2])
        second_half = statistics.mean(recent_5[-2:])
        
        if second_half > first_half + 0.05:
            return "improving"
        elif second_half < first_half - 0.05:
            return "declining"
        else:
            return "stable"


class EducationalAnalyticsPlatform:
    """
    Main educational analytics platform for comprehensive learning analysis
    
    Educational Impact:
    Provides complete educational effectiveness monitoring and optimization
    recommendations to ensure maximum learning outcomes and adaptive algorithm performance.
    
    Performance Requirements:
    - Real-time dashboard updates: <5 seconds
    - Comprehensive analysis: <10 seconds
    - Memory usage: <300MB total
    - Educational insight generation: <2 seconds
    """
    
    def __init__(self, database_path: str = "data/educational_analytics.db"):
        self.data_processor = LearningDataProcessor(database_path)
        self.adaptation_analyzer = AdaptationEffectivenessAnalyzer(self.data_processor)
        self.logger = logging.getLogger(__name__)
        
        # Platform statistics
        self.platform_start_time = datetime.now()
        self.dashboard_updates = 0
        self.analysis_requests = 0
        
    async def initialize(self) -> None:
        """Initialize educational analytics platform"""
        await self.data_processor.initialize_database()
        self.logger.info("Educational Analytics Platform initialized")
    
    async def process_learning_session(self, outcome: LearningOutcome) -> None:
        """
        Process complete learning session for analytics
        
        Educational Impact:
        Captures comprehensive learning session data for continuous
        educational effectiveness monitoring and improvement.
        
        Args:
            outcome: Complete learning session outcome
        """
        await self.data_processor.process_learning_event(outcome)
    
    async def analyze_adaptation_effectiveness(self, analysis: AdaptationAnalysis) -> Dict[str, Any]:
        """
        Analyze learning adaptation effectiveness
        
        Educational Impact:
        Validates adaptation algorithm performance to ensure optimal
        personalized learning experiences.
        
        Args:
            analysis: Adaptation effectiveness analysis data
        
        Returns:
            Comprehensive adaptation effectiveness assessment
        """
        return await self.adaptation_analyzer.analyze_adaptation(analysis)
    
    async def get_comprehensive_analytics_dashboard(self) -> Dict[str, Any]:
        """
        Get complete analytics dashboard data
        
        Educational Impact:
        Provides real-time visibility into educational effectiveness
        for data-driven learning optimization decisions.
        
        Returns:
            Comprehensive educational analytics dashboard
        """
        try:
            self.analysis_requests += 1
            
            # Get learning effectiveness analysis
            effectiveness_24h = await self.data_processor.analyze_learning_effectiveness(24)
            effectiveness_7d = await self.data_processor.analyze_learning_effectiveness(168)
            
            # Get educational insights
            insights = await self.data_processor.generate_educational_insights()
            
            # Get adaptation analysis
            adaptation_summary = await self.adaptation_analyzer.get_adaptation_summary(24)
            
            # Get processing statistics
            processing_stats = self.data_processor.get_processing_statistics()
            
            # Platform statistics
            uptime_hours = (datetime.now() - self.platform_start_time).total_seconds() / 3600
            
            dashboard = {
                "dashboard_generated_at": datetime.now().isoformat(),
                "platform_statistics": {
                    "uptime_hours": round(uptime_hours, 2),
                    "analysis_requests": self.analysis_requests,
                    "dashboard_updates": self.dashboard_updates
                },
                "learning_effectiveness": {
                    "last_24_hours": effectiveness_24h,
                    "last_7_days": effectiveness_7d
                },
                "educational_insights": [
                    {
                        "type": insight.insight_type,
                        "title": insight.title,
                        "description": insight.description,
                        "significance": insight.significance,
                        "learning_impact": insight.learning_impact,
                        "recommendation": insight.recommendation,
                        "confidence": insight.confidence_score
                    }
                    for insight in insights[-10:]  # Last 10 insights
                ],
                "adaptation_effectiveness": adaptation_summary,
                "processing_performance": processing_stats
            }
            
            self.dashboard_updates += 1
            return dashboard
            
        except Exception as e:
            self.logger.error(f"Failed to generate analytics dashboard: {e}")
            return {"error": f"Dashboard generation failed: {str(e)}"}
    
    async def get_learner_specific_analytics(self, learner_id: str, days: int = 7) -> Dict[str, Any]:
        """
        Get analytics specific to individual learner
        
        Educational Impact:
        Provides personalized learning analytics to support individual
        learner progress tracking and optimization.
        
        Args:
            learner_id: Unique learner identifier
            days: Number of days to analyze
        
        Returns:
            Comprehensive learner-specific analytics
        """
        try:
            cutoff_time = datetime.now() - timedelta(days=days)
            
            # Get learner outcomes
            async with aiosqlite.connect(self.data_processor.database_path) as db:
                cursor = await db.execute("""
                    SELECT * FROM learning_outcomes 
                    WHERE learner_id = ? AND timestamp > ?
                    ORDER BY timestamp DESC
                """, (learner_id, cutoff_time))
                rows = await cursor.fetchall()
                columns = [description[0] for description in cursor.description]
            
            if not rows:
                return {"error": f"No data found for learner {learner_id}"}
            
            outcomes_data = [dict(zip(columns, row)) for row in rows]
            
            # Analyze learner progress
            sessions = len(outcomes_data)
            competency_progression = []
            engagement_trend = []
            
            for outcome in reversed(outcomes_data):  # Chronological order
                if outcome["competency_after"] is not None:
                    competency_progression.append(outcome["competency_after"])
                if outcome["engagement_score"] is not None:
                    engagement_trend.append(outcome["engagement_score"])
            
            # Calculate learner-specific metrics
            total_study_time = sum(
                outcome["session_duration_minutes"] 
                for outcome in outcomes_data 
                if outcome["session_duration_minutes"] is not None
            )
            
            success_rate = (
                sum(1 for outcome in outcomes_data if outcome["educational_objective_met"]) 
                / sessions * 100
            ) if sessions > 0 else 0
            
            # Learning event distribution
            event_counts = defaultdict(int)
            for outcome in outcomes_data:
                event_counts[outcome["event_type"]] += 1
            
            return {
                "learner_id": learner_id,
                "analysis_period_days": days,
                "summary": {
                    "total_sessions": sessions,
                    "total_study_time_minutes": round(total_study_time, 1),
                    "success_rate": round(success_rate, 2),
                    "average_session_duration": round(total_study_time / sessions, 1) if sessions > 0 else 0
                },
                "progress": {
                    "competency_progression": competency_progression,
                    "engagement_trend": engagement_trend,
                    "current_competency": competency_progression[-1] if competency_progression else None,
                    "competency_improvement": (
                        competency_progression[-1] - competency_progression[0]
                        if len(competency_progression) > 1 else 0
                    )
                },
                "learning_events": dict(event_counts),
                "recommendations": self._generate_learner_recommendations(outcomes_data)
            }
            
        except Exception as e:
            self.logger.error(f"Failed to generate learner analytics for {learner_id}: {e}")
            return {"error": f"Learner analytics failed: {str(e)}"}
    
    def _generate_learner_recommendations(self, outcomes_data: List[Dict[str, Any]]) -> List[str]:
        """Generate personalized recommendations for learner"""
        recommendations = []
        
        if not outcomes_data:
            return recommendations
        
        # Analyze recent performance
        recent_outcomes = outcomes_data[:5]  # Last 5 sessions
        
        # Success rate analysis
        recent_success_rate = (
            sum(1 for outcome in recent_outcomes if outcome["educational_objective_met"]) 
            / len(recent_outcomes) * 100
        )
        
        if recent_success_rate < 60:
            recommendations.append("Consider reviewing foundational concepts before advancing to new topics")
        elif recent_success_rate > 90:
            recommendations.append("Ready for more challenging learning objectives")
        
        # Engagement analysis
        recent_engagement = [
            outcome["engagement_score"] 
            for outcome in recent_outcomes 
            if outcome["engagement_score"] is not None
        ]
        
        if recent_engagement and statistics.mean(recent_engagement) < 0.7:
            recommendations.append("Try different VR interaction modes to improve engagement")
        
        # Session duration analysis
        recent_durations = [
            outcome["session_duration_minutes"] 
            for outcome in recent_outcomes 
            if outcome["session_duration_minutes"] is not None
        ]
        
        if recent_durations and statistics.mean(recent_durations) < 10:
            recommendations.append("Consider longer learning sessions for better retention")
        elif recent_durations and statistics.mean(recent_durations) > 45:
            recommendations.append("Break learning into shorter sessions to maintain focus")
        
        return recommendations


# Utility functions for educational analytics integration

async def create_educational_analytics_platform(
    database_path: str = "data/educational_analytics.db"
) -> EducationalAnalyticsPlatform:
    """
    Create and initialize educational analytics platform
    
    Educational Impact:
    Establishes comprehensive educational data analysis capabilities
    for continuous learning effectiveness optimization.
    
    Args:
        database_path: Path to analytics database
    
    Returns:
        Initialized educational analytics platform
    """
    platform = EducationalAnalyticsPlatform(database_path)
    await platform.initialize()
    return platform


def setup_analytics_logging() -> None:
    """Set up specialized logging for educational analytics"""
    # Create analytics specific logger
    analytics_logger = logging.getLogger("malloc_vr.educational_analytics")
    analytics_logger.setLevel(logging.INFO)
    
    # Create file handler for analytics logs
    try:
        handler = logging.FileHandler("logs/educational_analytics.log")
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        analytics_logger.addHandler(handler)
    except Exception as e:
        print(f"Warning: Could not set up educational analytics log file: {e}")


# Sample data generators for testing and demonstration

async def generate_sample_learning_outcome(
    learner_id: str = "test_learner",
    event_type: LearningEventType = LearningEventType.PRACTICE
) -> LearningOutcome:
    """Generate sample learning outcome for testing"""
    import random
    
    competency_before = random.uniform(0.3, 0.8)
    improvement = random.uniform(0.05, 0.25)
    competency_after = min(1.0, competency_before + improvement)
    
    return LearningOutcome(
        learner_id=learner_id,
        event_type=event_type,
        timestamp=datetime.now(),
        competency_before=competency_before,
        competency_after=competency_after,
        engagement_score=random.uniform(0.6, 0.95),
        adaptation_applied=random.choice([True, False]),
        adaptation_effectiveness=random.uniform(0.7, 0.95),
        session_duration_minutes=random.uniform(15, 35),
        vr_interaction_quality=random.uniform(0.75, 0.95),
        educational_objective_met=competency_after > competency_before + 0.1
    )


async def generate_sample_adaptation_analysis(
    adaptation_id: str = "test_adaptation"
) -> AdaptationAnalysis:
    """Generate sample adaptation analysis for testing"""
    import random
    
    predicted = random.uniform(0.6, 0.9)
    actual = predicted + random.uniform(-0.15, 0.15)  # Some prediction error
    actual = max(0.0, min(1.0, actual))  # Clamp to valid range
    
    return AdaptationAnalysis(
        adaptation_id=adaptation_id,
        learner_profile={"learning_rate": 0.7, "preferred_difficulty": 0.6},
        original_state={"competency": 0.5, "engagement": 0.7},
        adapted_state={"competency": 0.6, "engagement": 0.8},
        predicted_outcome=predicted,
        actual_outcome=actual,
        accuracy_score=1.0 - abs(predicted - actual),
        adaptation_timestamp=datetime.now() - timedelta(minutes=30),
        outcome_timestamp=datetime.now(),
        educational_context="VR spatial reasoning practice"
    )
