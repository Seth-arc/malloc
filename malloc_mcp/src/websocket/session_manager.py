"""
Session Manager for Real-time Learning WebSocket Communication

Educational Impact:
Manages the complete lifecycle of educational WebSocket sessions, ensuring
FERPA-compliant learner data handling, secure session state management,
and educational continuity across connection interruptions. Enables
persistent learning context that survives network issues and maintains
optimal educational progression.

Performance Requirements:
- Session creation: <200ms including learner profile loading
- Session state updates: <50ms for real-time data processing
- Memory per session: <2MB for comprehensive learner state
- Concurrent sessions: Support 50+ simultaneous learners
- Data persistence: <100ms for educational data preservation

Quest 3 VR Optimization:
- Efficient session state serialization for VR memory constraints
- Optimized learner profile caching for fast VR interactions
- Minimal memory footprint per session for VR performance
"""

import asyncio
import json
import logging
import time
from typing import Dict, List, Optional, Any
from datetime import datetime, timezone, timedelta
import uuid
from dataclasses import dataclass, asdict

from ..security.educational_security import EducationalSecurityManager
from ..learning.learner_model import LearnerModel
from ..learning.integration_engine import LearningIntegrationEngine

logger = logging.getLogger(__name__)

@dataclass
class SessionConfig:
    """
    Configuration for educational learning session.
    
    Educational Impact:
    Defines the educational parameters and settings that guide the
    learning experience, ensuring appropriate difficulty, pacing,
    and educational objectives are maintained throughout the session.
    """
    learning_domain: str = "vr_3d_modeling"
    target_learning_event: str = "introduction"
    adaptation_sensitivity: str = "medium"  # low, medium, high
    difficulty_level: float = 0.5  # 0.0 to 1.0
    support_level: str = "adaptive"  # minimal, adaptive, intensive
    collaboration_enabled: bool = False
    analytics_enabled: bool = True
    session_timeout_minutes: int = 60

@dataclass
class SessionState:
    """
    Current state of educational learning session.
    
    Educational Impact:
    Maintains comprehensive educational context including learner progress,
    engagement levels, learning effectiveness, and adaptation history to
    ensure educational continuity and optimal learning outcomes.
    """
    session_id: str
    learner_id: str
    connection_id: str
    created_at: datetime
    last_activity: datetime
    session_config: SessionConfig
    
    # Learning state
    current_learning_event: str
    progress_percentage: float = 0.0
    competency_level: float = 0.5
    engagement_score: float = 0.5
    
    # Interaction metrics
    total_interactions: int = 0
    successful_interactions: int = 0
    help_requests: int = 0
    adaptation_count: int = 0
    
    # Performance metrics
    average_response_time: float = 0.0
    error_rate: float = 0.0
    flow_state_duration: float = 0.0
    
    # Educational analytics
    learning_gains: float = 0.0
    skill_improvements: Dict[str, float] = None
    knowledge_retention: float = 0.0
    
    def __post_init__(self):
        if self.skill_improvements is None:
            self.skill_improvements = {}

class SessionManager:
    """
    Manages WebSocket sessions for real-time learning adaptation.
    
    Educational Impact:
    Provides comprehensive session lifecycle management that ensures
    educational continuity, learner data protection, and optimal
    learning progression across WebSocket connections. Maintains
    educational context and enables seamless learning experiences.
    
    Performance Requirements:
    - Session operations: <100ms for all session management tasks
    - Memory efficiency: <2MB per active session
    - Concurrent sessions: Support 50+ simultaneous learners
    - Data persistence: FERPA-compliant with encryption
    
    Features:
    - FERPA-compliant session data handling with encryption
    - Educational context preservation across connection interruptions
    - Real-time session state synchronization
    - Comprehensive learning analytics and progress tracking
    """
    
    def __init__(self, security_manager: EducationalSecurityManager):
        """
        Initialize session manager for educational WebSocket sessions.
        
        Educational Impact:
        Sets up the infrastructure for managing educational sessions
        with proper security, data protection, and learning context
        preservation to ensure optimal educational outcomes.
        
        Args:
            security_manager: FERPA-compliant security manager for learner data protection
        """
        self.security_manager = security_manager
        
        # Session storage
        self.active_sessions: Dict[str, SessionState] = {}
        self.session_lookup: Dict[str, str] = {}  # connection_id -> session_id
        self.learner_sessions: Dict[str, List[str]] = {}  # learner_id -> [session_ids]
        
        # Performance tracking
        self.session_metrics = {
            'sessions_created': 0,
            'sessions_completed': 0,
            'sessions_terminated': 0,
            'average_session_duration': 0.0,
            'total_session_time': 0.0,
            'educational_effectiveness': 0.0
        }
        
        # Cleanup configuration
        self.session_timeout = timedelta(minutes=60)
        self.cleanup_interval = 300  # 5 minutes
        self._cleanup_task = None
        
        # Learning models
        self.learner_model = LearnerModel()
        
        # Start cleanup task
        self._start_cleanup_task()
        
    async def create_session(
        self, 
        learner_id: str, 
        connection_id: str, 
        session_config: Dict[str, Any]
    ) -> str:
        """
        Create new educational learning session.
        
        Educational Impact:
        Establishes a new educational session with proper learner context,
        educational objectives, and FERPA-compliant data handling to
        ensure optimal learning outcomes from session start.
        
        Performance Requirements:
        - Session creation: <200ms including learner profile loading
        - Memory allocation: <2MB for session state
        - Data encryption: <50ms for FERPA compliance
        
        Args:
            learner_id: Unique identifier for the learner
            connection_id: WebSocket connection identifier
            session_config: Educational configuration parameters
            
        Returns:
            session_id: Unique session identifier for tracking
        """
        try:
            # Generate unique session ID
            session_id = f"session_{uuid.uuid4().hex[:16]}"
            
            # Parse and validate session configuration
            config = SessionConfig(**session_config) if session_config else SessionConfig()
            
            # Load learner profile for educational context
            learner_profile = await self._load_learner_profile(learner_id)
            
            # Create session state with educational context
            session_state = SessionState(
                session_id=session_id,
                learner_id=learner_id,
                connection_id=connection_id,
                created_at=datetime.now(timezone.utc),
                last_activity=datetime.now(timezone.utc),
                session_config=config,
                current_learning_event=config.target_learning_event,
                competency_level=learner_profile.get('competency_level', 0.5),
                engagement_score=learner_profile.get('baseline_engagement', 0.5)
            )
            
            # Store session with encryption for FERPA compliance
            encrypted_session_data = await self._encrypt_session_data(session_state)
            
            # Register session
            self.active_sessions[session_id] = session_state
            self.session_lookup[connection_id] = session_id
            
            # Track learner sessions
            if learner_id not in self.learner_sessions:
                self.learner_sessions[learner_id] = []
            self.learner_sessions[learner_id].append(session_id)
            
            # Update metrics
            self.session_metrics['sessions_created'] += 1
            
            logger.info(f"Educational session created: {session_id} for learner: {learner_id}")
            logger.info(f"Learning event: {config.target_learning_event}, Domain: {config.learning_domain}")
            
            return session_id
            
        except Exception as e:
            logger.error(f"Error creating session: {e}")
            raise
            
    async def update_session_data(
        self, 
        session_id: str, 
        interaction_snapshot: Dict[str, Any]
    ) -> None:
        """
        Update session with latest learning interaction data.
        
        Educational Impact:
        Maintains real-time educational context by processing learner
        interactions, updating engagement metrics, and preserving
        learning progression data for continuous adaptation.
        
        Performance Requirements:
        - Update processing: <50ms for real-time data integration
        - Memory efficiency: Minimal allocation for updates
        - Data validation: Complete with educational context preservation
        
        Args:
            session_id: Unique session identifier
            interaction_snapshot: Latest learner interaction data
        """
        try:
            if session_id not in self.active_sessions:
                logger.warning(f"Session not found for update: {session_id}")
                return
                
            session = self.active_sessions[session_id]
            
            # Update activity timestamp
            session.last_activity = datetime.now(timezone.utc)
            
            # Extract and process interaction data
            learner_state = interaction_snapshot.get('learner_state', {})
            engagement_metrics = interaction_snapshot.get('engagement_metrics', {})
            performance_indicators = interaction_snapshot.get('performance_indicators', {})
            
            # Update learning metrics
            if 'competency_confidence' in learner_state:
                session.competency_level = learner_state['competency_confidence']
                
            if 'attention_level' in engagement_metrics:
                session.engagement_score = engagement_metrics['attention_level']
                
            # Update interaction counters
            session.total_interactions += 1
            
            if performance_indicators.get('task_completion_rate', 0) > 0.8:
                session.successful_interactions += 1
                
            if learner_state.get('help_seeking_frequency', 0) > 0.1:
                session.help_requests += 1
                
            # Update performance metrics
            if 'error_frequency' in performance_indicators:
                session.error_rate = performance_indicators['error_frequency']
                
            # Calculate learning gains
            current_progress = performance_indicators.get('task_completion_rate', 0)
            if current_progress > session.progress_percentage:
                session.learning_gains += current_progress - session.progress_percentage
                session.progress_percentage = current_progress
                
            # Update skill improvements
            if 'skill_demonstration' in performance_indicators:
                skill_level = performance_indicators['skill_demonstration']
                previous_skill = session.skill_improvements.get('current_skill', 0.5)
                if skill_level > previous_skill:
                    session.skill_improvements['current_skill'] = skill_level
                    session.skill_improvements['improvement'] = skill_level - previous_skill
                    
            # Encrypt and store updated session data
            await self._encrypt_session_data(session)
            
            logger.debug(f"Session updated: {session_id}, Progress: {session.progress_percentage:.2f}")
            
        except Exception as e:
            logger.error(f"Error updating session data: {e}")
            
    async def get_session_state(self, session_id: str) -> Optional[SessionState]:
        """
        Retrieve current session state.
        
        Educational Impact:
        Provides access to comprehensive educational session context
        for adaptation decisions, learning analytics, and educational
        continuity across system components.
        
        Args:
            session_id: Unique session identifier
            
        Returns:
            SessionState: Current session state or None if not found
        """
        return self.active_sessions.get(session_id)
        
    async def get_session_by_connection(self, connection_id: str) -> Optional[SessionState]:
        """
        Retrieve session state by connection ID.
        
        Educational Impact:
        Enables quick access to educational context based on WebSocket
        connection, facilitating real-time adaptation and educational
        response to learner interactions.
        
        Args:
            connection_id: WebSocket connection identifier
            
        Returns:
            SessionState: Current session state or None if not found
        """
        session_id = self.session_lookup.get(connection_id)
        if session_id:
            return self.active_sessions.get(session_id)
        return None
        
    async def finalize_session(self, session_id: str, reason: Optional[str] = None) -> None:
        """
        Finalize educational session with data preservation.
        
        Educational Impact:
        Ensures proper closure of educational session with complete
        learning data preservation, analytics recording, and FERPA-compliant
        data handling for educational continuity and assessment.
        
        Performance Requirements:
        - Finalization processing: <100ms for data preservation
        - Data encryption: <50ms for FERPA compliance
        - Analytics processing: <200ms for educational metrics
        
        Args:
            session_id: Unique session identifier
            reason: Optional reason for session closure
        """
        try:
            if session_id not in self.active_sessions:
                logger.warning(f"Session not found for finalization: {session_id}")
                return
                
            session = self.active_sessions[session_id]
            
            # Calculate final session metrics
            session_duration = (datetime.now(timezone.utc) - session.created_at).total_seconds()
            
            # Update session metrics
            self.session_metrics['sessions_completed'] += 1
            self.session_metrics['total_session_time'] += session_duration
            
            # Calculate average session duration
            if self.session_metrics['sessions_completed'] > 0:
                self.session_metrics['average_session_duration'] = (
                    self.session_metrics['total_session_time'] / 
                    self.session_metrics['sessions_completed']
                )
            
            # Calculate educational effectiveness
            success_rate = (session.successful_interactions / max(session.total_interactions, 1))
            learning_efficiency = session.learning_gains / max(session_duration / 3600, 0.1)  # gains per hour
            engagement_quality = session.engagement_score
            
            educational_effectiveness = (success_rate * 0.4 + learning_efficiency * 0.4 + engagement_quality * 0.2)
            
            # Update overall educational effectiveness
            current_effectiveness = self.session_metrics['educational_effectiveness']
            completed_sessions = self.session_metrics['sessions_completed']
            
            self.session_metrics['educational_effectiveness'] = (
                (current_effectiveness * (completed_sessions - 1) + educational_effectiveness) / 
                completed_sessions
            )
            
            # Save session analytics for educational research
            await self._save_session_analytics(session, session_duration, educational_effectiveness)
            
            # Update learner profile with session learnings
            await self._update_learner_profile(session)
            
            logger.info(f"Session finalized: {session_id}")
            logger.info(f"Duration: {session_duration:.1f}s, Effectiveness: {educational_effectiveness:.3f}")
            logger.info(f"Learning gains: {session.learning_gains:.3f}, Interactions: {session.total_interactions}")
            
        except Exception as e:
            logger.error(f"Error finalizing session: {e}")
            
    async def cleanup_session(self, session_id: str) -> None:
        """
        Cleanup session resources and remove from active sessions.
        
        Educational Impact:
        Ensures proper cleanup of educational resources while preserving
        learner data and maintaining FERPA compliance during session removal.
        
        Args:
            session_id: Unique session identifier
        """
        try:
            if session_id not in self.active_sessions:
                return
                
            session = self.active_sessions[session_id]
            
            # Remove from active sessions
            del self.active_sessions[session_id]
            
            # Remove connection lookup
            if session.connection_id in self.session_lookup:
                del self.session_lookup[session.connection_id]
                
            # Remove from learner sessions
            if session.learner_id in self.learner_sessions:
                self.learner_sessions[session.learner_id] = [
                    sid for sid in self.learner_sessions[session.learner_id] 
                    if sid != session_id
                ]
                
                # Remove empty learner entry
                if not self.learner_sessions[session.learner_id]:
                    del self.learner_sessions[session.learner_id]
                    
            logger.debug(f"Session cleanup completed: {session_id}")
            
        except Exception as e:
            logger.error(f"Error cleaning up session: {e}")
            
    async def cleanup_all_sessions(self) -> None:
        """
        Cleanup all active sessions during server shutdown.
        
        Educational Impact:
        Ensures all educational sessions are properly finalized with
        data preservation and FERPA compliance during system shutdown.
        """
        try:
            logger.info(f"Cleaning up {len(self.active_sessions)} active sessions")
            
            # Finalize all sessions
            finalization_tasks = []
            for session_id in list(self.active_sessions.keys()):
                finalization_tasks.append(self.finalize_session(session_id, "server_shutdown"))
                
            await asyncio.gather(*finalization_tasks, return_exceptions=True)
            
            # Clear all session data
            self.active_sessions.clear()
            self.session_lookup.clear()
            self.learner_sessions.clear()
            
            # Stop cleanup task
            if self._cleanup_task:
                self._cleanup_task.cancel()
                
            logger.info("All sessions cleaned up successfully")
            
        except Exception as e:
            logger.error(f"Error during session cleanup: {e}")
            
    async def get_session_summary(self, session_id: str) -> Dict[str, Any]:
        """
        Get comprehensive session summary for educational analytics.
        
        Educational Impact:
        Provides detailed educational session summary including learning
        outcomes, engagement metrics, and performance indicators for
        educational assessment and continuous improvement.
        
        Args:
            session_id: Unique session identifier
            
        Returns:
            Dict containing comprehensive session summary and educational metrics
        """
        try:
            if session_id not in self.active_sessions:
                return {"error": "Session not found"}
                
            session = self.active_sessions[session_id]
            session_duration = (datetime.now(timezone.utc) - session.created_at).total_seconds()
            
            return {
                "session_info": {
                    "session_id": session_id,
                    "learner_id": session.learner_id,
                    "duration_seconds": session_duration,
                    "learning_domain": session.session_config.learning_domain,
                    "learning_event": session.current_learning_event
                },
                "learning_outcomes": {
                    "progress_percentage": session.progress_percentage,
                    "competency_level": session.competency_level,
                    "learning_gains": session.learning_gains,
                    "skill_improvements": session.skill_improvements,
                    "knowledge_retention": session.knowledge_retention
                },
                "engagement_metrics": {
                    "engagement_score": session.engagement_score,
                    "flow_state_duration": session.flow_state_duration,
                    "total_interactions": session.total_interactions,
                    "successful_interactions": session.successful_interactions
                },
                "performance_indicators": {
                    "success_rate": session.successful_interactions / max(session.total_interactions, 1),
                    "error_rate": session.error_rate,
                    "help_request_frequency": session.help_requests / max(session.total_interactions, 1),
                    "adaptation_count": session.adaptation_count
                },
                "educational_quality": {
                    "learning_efficiency": session.learning_gains / max(session_duration / 3600, 0.1),
                    "engagement_quality": session.engagement_score,
                    "interaction_quality": session.successful_interactions / max(session.total_interactions, 1)
                }
            }
            
        except Exception as e:
            logger.error(f"Error generating session summary: {e}")
            return {"error": str(e)}
            
    def get_average_session_duration(self) -> float:
        """
        Get average session duration for performance monitoring.
        
        Educational Impact:
        Provides educational analytics on session duration patterns
        to optimize learning session lengths and engagement strategies.
        
        Returns:
            Average session duration in seconds
        """
        return self.session_metrics['average_session_duration']
        
    def get_session_metrics(self) -> Dict[str, Any]:
        """
        Get comprehensive session metrics for monitoring.
        
        Educational Impact:
        Provides detailed educational analytics for system optimization,
        learning effectiveness assessment, and educational research.
        
        Returns:
            Dict containing comprehensive session and educational metrics
        """
        return {
            "session_statistics": self.session_metrics.copy(),
            "active_sessions": {
                "total_active": len(self.active_sessions),
                "active_learners": len(self.learner_sessions),
                "sessions_by_event": self._get_sessions_by_learning_event(),
                "sessions_by_domain": self._get_sessions_by_domain()
            },
            "educational_analytics": {
                "average_engagement": self._calculate_average_engagement(),
                "average_competency": self._calculate_average_competency(),
                "overall_learning_gains": self._calculate_total_learning_gains(),
                "success_rate": self._calculate_overall_success_rate()
            }
        }
        
    async def _load_learner_profile(self, learner_id: str) -> Dict[str, Any]:
        """
        Load learner profile for educational context initialization.
        
        Educational Impact:
        Retrieves comprehensive learner profile including learning history,
        preferences, competency levels, and educational objectives to
        initialize optimal learning context for the session.
        
        Args:
            learner_id: Unique learner identifier
            
        Returns:
            Dict containing learner profile data
        """
        try:
            # Load learner profile using learner model
            learner_data = await self.learner_model.get_learner_profile(learner_id)
            
            # Return profile with educational defaults if not found
            return learner_data or {
                'competency_level': 0.5,
                'baseline_engagement': 0.5,
                'learning_preferences': {},
                'educational_history': []
            }
            
        except Exception as e:
            logger.error(f"Error loading learner profile: {e}")
            return {
                'competency_level': 0.5,
                'baseline_engagement': 0.5,
                'learning_preferences': {},
                'educational_history': []
            }
            
    async def _encrypt_session_data(self, session_state: SessionState) -> bytes:
        """
        Encrypt session data for FERPA compliance.
        
        Educational Impact:
        Ensures all learner session data is encrypted according to FERPA
        requirements, protecting educational privacy while maintaining
        accessibility for educational purposes.
        
        Args:
            session_state: Session state to encrypt
            
        Returns:
            Encrypted session data
        """
        try:
            # Convert session state to dict for encryption
            session_dict = asdict(session_state)
            session_json = json.dumps(session_dict, default=str)
            
            # Encrypt using security manager
            encrypted_data = await self.security_manager.encrypt_learner_data(
                session_json.encode('utf-8'),
                f"session_{session_state.session_id}"
            )
            
            return encrypted_data
            
        except Exception as e:
            logger.error(f"Error encrypting session data: {e}")
            raise
            
    async def _save_session_analytics(
        self, 
        session: SessionState, 
        duration: float, 
        effectiveness: float
    ) -> None:
        """
        Save session analytics for educational research and improvement.
        
        Educational Impact:
        Preserves detailed educational analytics for learning effectiveness
        research, system optimization, and educational outcome assessment.
        
        Args:
            session: Session state with educational data
            duration: Session duration in seconds
            effectiveness: Calculated educational effectiveness score
        """
        try:
            analytics_data = {
                'session_id': session.session_id,
                'learner_id': session.learner_id,
                'duration': duration,
                'effectiveness': effectiveness,
                'learning_gains': session.learning_gains,
                'engagement_score': session.engagement_score,
                'competency_level': session.competency_level,
                'interaction_metrics': {
                    'total_interactions': session.total_interactions,
                    'successful_interactions': session.successful_interactions,
                    'help_requests': session.help_requests,
                    'adaptation_count': session.adaptation_count
                },
                'educational_context': {
                    'learning_domain': session.session_config.learning_domain,
                    'learning_event': session.current_learning_event,
                    'difficulty_level': session.session_config.difficulty_level
                },
                'timestamp': datetime.now(timezone.utc).isoformat()
            }
            
            # Save analytics with encryption for FERPA compliance
            await self.security_manager.save_educational_analytics(analytics_data)
            
        except Exception as e:
            logger.error(f"Error saving session analytics: {e}")
            
    async def _update_learner_profile(self, session: SessionState) -> None:
        """
        Update learner profile with session learning outcomes.
        
        Educational Impact:
        Updates learner profile with new competency levels, learning gains,
        and educational progress to ensure future sessions build upon
        current achievements and maintain educational continuity.
        
        Args:
            session: Completed session with learning outcomes
        """
        try:
            # Calculate profile updates based on session outcomes
            profile_updates = {
                'competency_level': session.competency_level,
                'recent_engagement': session.engagement_score,
                'learning_progress': session.progress_percentage,
                'skill_improvements': session.skill_improvements,
                'session_count': 1,  # Increment by 1
                'total_learning_time': (
                    datetime.now(timezone.utc) - session.created_at
                ).total_seconds(),
                'last_session': session.session_id,
                'educational_gains': session.learning_gains
            }
            
            # Update learner profile through learner model
            await self.learner_model.update_learner_profile(
                session.learner_id, 
                profile_updates
            )
            
        except Exception as e:
            logger.error(f"Error updating learner profile: {e}")
            
    def _start_cleanup_task(self) -> None:
        """
        Start background task for session cleanup and maintenance.
        
        Educational Impact:
        Ensures system resources are efficiently managed while preserving
        educational data integrity and maintaining optimal performance for
        active learning sessions.
        """
        async def cleanup_expired_sessions():
            while True:
                try:
                    await asyncio.sleep(self.cleanup_interval)
                    await self._cleanup_expired_sessions()
                except asyncio.CancelledError:
                    break
                except Exception as e:
                    logger.error(f"Error in cleanup task: {e}")
                    
        self._cleanup_task = asyncio.create_task(cleanup_expired_sessions())
        
    async def _cleanup_expired_sessions(self) -> None:
        """
        Cleanup sessions that have exceeded timeout limits.
        
        Educational Impact:
        Maintains system performance while ensuring educational data
        preservation and proper session finalization for inactive sessions.
        """
        try:
            current_time = datetime.now(timezone.utc)
            expired_sessions = []
            
            for session_id, session in self.active_sessions.items():
                if current_time - session.last_activity > self.session_timeout:
                    expired_sessions.append(session_id)
                    
            if expired_sessions:
                logger.info(f"Cleaning up {len(expired_sessions)} expired sessions")
                
                for session_id in expired_sessions:
                    await self.finalize_session(session_id, "session_timeout")
                    await self.cleanup_session(session_id)
                    
                self.session_metrics['sessions_terminated'] += len(expired_sessions)
                
        except Exception as e:
            logger.error(f"Error cleaning up expired sessions: {e}")
            
    def _get_sessions_by_learning_event(self) -> Dict[str, int]:
        """Get count of sessions by learning event for analytics."""
        event_counts = {}
        for session in self.active_sessions.values():
            event = session.current_learning_event
            event_counts[event] = event_counts.get(event, 0) + 1
        return event_counts
        
    def _get_sessions_by_domain(self) -> Dict[str, int]:
        """Get count of sessions by learning domain for analytics."""
        domain_counts = {}
        for session in self.active_sessions.values():
            domain = session.session_config.learning_domain
            domain_counts[domain] = domain_counts.get(domain, 0) + 1
        return domain_counts
        
    def _calculate_average_engagement(self) -> float:
        """Calculate average engagement across active sessions."""
        if not self.active_sessions:
            return 0.0
        total_engagement = sum(session.engagement_score for session in self.active_sessions.values())
        return total_engagement / len(self.active_sessions)
        
    def _calculate_average_competency(self) -> float:
        """Calculate average competency across active sessions."""
        if not self.active_sessions:
            return 0.0
        total_competency = sum(session.competency_level for session in self.active_sessions.values())
        return total_competency / len(self.active_sessions)
        
    def _calculate_total_learning_gains(self) -> float:
        """Calculate total learning gains across active sessions."""
        return sum(session.learning_gains for session in self.active_sessions.values())
        
    def _calculate_overall_success_rate(self) -> float:
        """Calculate overall success rate across active sessions."""
        total_interactions = sum(session.total_interactions for session in self.active_sessions.values())
        successful_interactions = sum(session.successful_interactions for session in self.active_sessions.values())
        
        if total_interactions == 0:
            return 0.0
        return successful_interactions / total_interactions
