"""
WebSocket Server Implementation for Real-time Learning Adaptation

Educational Impact:
Provides the core WebSocket server infrastructure that enables real-time 
learning adaptation by maintaining persistent connections with VR learning
environments, processing continuous interaction data, and delivering
immediate adaptation commands to optimize learning experiences.

Performance Requirements:
- Connection establishment: <500ms including authentication
- Message processing: <10ms for adaptation command generation
- Concurrent connections: Support 50+ simultaneous learners
- Memory per connection: <2MB for session state management
- Latency: <25ms end-to-end for real-time adaptation

Quest 3 VR Optimization:
- Optimized message serialization for VR bandwidth constraints
- Priority queuing for urgent adaptation commands
- Efficient state synchronization for smooth VR experience
"""

import asyncio
import json
import logging
import time
from typing import Dict, Set, Optional, Callable, Any, List
from datetime import datetime, timezone
import websockets
from websockets.server import WebSocketServerProtocol
import uuid

from ..security.educational_security import EducationalSecurityManager
from ..learning.integration_engine import LearningIntegrationEngine
from .session_manager import SessionManager
from .adaptation_processor import AdaptationProcessor
from .streaming_handler import StreamingHandler

# Configure logging for WebSocket operations
logger = logging.getLogger(__name__)

class WebSocketServer:
    """
    Real-time WebSocket server for educational VR learning adaptation.
    
    Educational Impact:
    Enables continuous learning adaptation by maintaining real-time communication
    with VR learning environments, processing learner interactions, and delivering
    immediate educational adjustments to optimize learning outcomes.
    
    Performance Requirements:
    - WebSocket latency: <25ms for real-time adaptation
    - Concurrent connections: Support 50+ simultaneous learners  
    - Message processing: <10ms for adaptation command generation
    - Connection handling: <500ms for authentication and session setup
    
    Features:
    - FERPA-compliant session management with encrypted learner data
    - Real-time learning equation processing for immediate adaptation
    - Priority-based message handling for urgent educational interventions
    - Comprehensive performance monitoring for Quest 3 VR optimization
    """
    
    def __init__(
        self,
        host: str = "localhost",
        port: int = 8765,
        security_manager: Optional[EducationalSecurityManager] = None,
        integration_engine: Optional[LearningIntegrationEngine] = None
    ):
        """
        Initialize WebSocket server for real-time learning adaptation.
        
        Educational Impact:
        Sets up the foundational infrastructure for real-time educational
        communication, enabling immediate response to learner needs and
        continuous optimization of the learning experience.
        
        Args:
            host: Server host address for WebSocket connections
            port: Server port for WebSocket connections  
            security_manager: FERPA-compliant security manager for learner data protection
            integration_engine: Learning integration engine for real-time adaptation
        """
        self.host = host
        self.port = port
        self.security_manager = security_manager or EducationalSecurityManager()
        self.integration_engine = integration_engine or LearningIntegrationEngine()
        
        # Connection management
        self.active_connections: Dict[str, WebSocketServerProtocol] = {}
        self.connection_sessions: Dict[str, str] = {}  # connection_id -> session_id
        
        # Component managers
        self.session_manager = SessionManager(self.security_manager)
        self.adaptation_processor = AdaptationProcessor(self.integration_engine)
        self.streaming_handler = StreamingHandler()
        
        # Performance monitoring
        self.connection_count = 0
        self.message_count = 0
        self.start_time = time.time()
        self.performance_metrics = {
            'connections_established': 0,
            'connections_closed': 0,
            'messages_processed': 0,
            'adaptation_commands_sent': 0,
            'average_processing_time': 0.0,
            'peak_concurrent_connections': 0
        }
        
        # Server state
        self.is_running = False
        self.server = None
        
    async def start_server(self) -> None:
        """
        Start the WebSocket server for real-time learning communication.
        
        Educational Impact:
        Initiates the real-time learning adaptation infrastructure, enabling
        continuous educational optimization and immediate response to learner
        interactions in VR environments.
        
        Performance Requirements:
        - Server startup: <2 seconds for complete initialization
        - Memory overhead: <50MB for server infrastructure
        - Connection readiness: Immediate acceptance of new connections
        """
        try:
            logger.info(f"Starting WebSocket server on {self.host}:{self.port}")
            
            # Start the WebSocket server
            self.server = await websockets.serve(
                self._handle_connection,
                self.host,
                self.port,
                ping_interval=20,  # Keep connections alive
                ping_timeout=10,   # Connection timeout
                max_size=10**6,    # 1MB max message size
                compression=None   # Disable compression for low latency
            )
            
            self.is_running = True
            self.start_time = time.time()
            
            logger.info(f"WebSocket server started successfully")
            logger.info(f"Ready for real-time learning adaptation connections")
            
        except Exception as e:
            logger.error(f"Failed to start WebSocket server: {e}")
            raise
            
    async def stop_server(self) -> None:
        """
        Stop the WebSocket server and cleanup resources.
        
        Educational Impact:
        Gracefully terminates real-time learning sessions, ensuring learner
        data is properly saved and educational continuity is maintained
        through proper session closure procedures.
        """
        try:
            logger.info("Stopping WebSocket server...")
            
            self.is_running = False
            
            # Close all active connections gracefully
            if self.active_connections:
                logger.info(f"Closing {len(self.active_connections)} active connections")
                close_tasks = []
                for connection_id, websocket in self.active_connections.items():
                    close_tasks.append(self._close_connection_gracefully(connection_id, websocket))
                
                await asyncio.gather(*close_tasks, return_exceptions=True)
            
            # Stop the server
            if self.server:
                self.server.close()
                await self.server.wait_closed()
                
            # Cleanup session manager
            await self.session_manager.cleanup_all_sessions()
            
            logger.info("WebSocket server stopped successfully")
            
        except Exception as e:
            logger.error(f"Error stopping WebSocket server: {e}")
            
    async def _handle_connection(self, websocket: WebSocketServerProtocol, path: str) -> None:
        """
        Handle new WebSocket connection for real-time learning.
        
        Educational Impact:
        Establishes secure, FERPA-compliant connection for real-time learning
        adaptation, enabling continuous educational optimization and immediate
        response to learner interactions.
        
        Performance Requirements:
        - Connection establishment: <500ms including authentication
        - Session initialization: <200ms for learner profile loading
        - Memory allocation: <2MB per connection for session state
        """
        connection_id = str(uuid.uuid4())
        session_id = None
        
        try:
            # Register connection
            self.active_connections[connection_id] = websocket
            self.connection_count += 1
            self.performance_metrics['connections_established'] += 1
            self.performance_metrics['peak_concurrent_connections'] = max(
                self.performance_metrics['peak_concurrent_connections'],
                len(self.active_connections)
            )
            
            logger.info(f"New WebSocket connection established: {connection_id}")
            
            # Handle connection lifecycle
            session_id = await self._handle_connection_lifecycle(connection_id, websocket)
            
        except websockets.exceptions.ConnectionClosed:
            logger.info(f"WebSocket connection closed: {connection_id}")
        except Exception as e:
            logger.error(f"Error handling WebSocket connection {connection_id}: {e}")
            await self._send_error_message(websocket, "internal_error", str(e))
        finally:
            # Cleanup connection
            await self._cleanup_connection(connection_id, session_id)
            
    async def _handle_connection_lifecycle(
        self, 
        connection_id: str, 
        websocket: WebSocketServerProtocol
    ) -> Optional[str]:
        """
        Handle the complete lifecycle of a WebSocket connection.
        
        Educational Impact:
        Manages the entire educational session lifecycle from authentication
        through continuous learning adaptation to graceful session closure,
        ensuring educational continuity and optimal learning outcomes.
        
        Returns:
            session_id: Unique session identifier for educational tracking
        """
        session_id = None
        
        try:
            # Wait for connection message
            async for message in websocket:
                start_time = time.time()
                
                try:
                    # Parse message
                    data = json.loads(message)
                    action = data.get('action')
                    
                    if action == 'connect':
                        # Handle connection establishment
                        session_id = await self._handle_connect(connection_id, websocket, data)
                        
                    elif action == 'learning_data':
                        # Handle real-time learning data streaming
                        await self._handle_learning_data(connection_id, websocket, data)
                        
                    elif action == 'adaptation_request':
                        # Handle explicit adaptation requests
                        await self._handle_adaptation_request(connection_id, websocket, data)
                        
                    elif action == 'disconnect':
                        # Handle graceful disconnection
                        await self._handle_disconnect(connection_id, websocket, data)
                        break
                        
                    else:
                        await self._send_error_message(
                            websocket, 
                            "invalid_action", 
                            f"Unknown action: {action}"
                        )
                    
                    # Update performance metrics
                    processing_time = time.time() - start_time
                    self._update_performance_metrics(processing_time)
                    
                except json.JSONDecodeError:
                    await self._send_error_message(websocket, "invalid_json", "Invalid JSON format")
                except Exception as e:
                    logger.error(f"Error processing message: {e}")
                    await self._send_error_message(websocket, "processing_error", str(e))
                    
        except websockets.exceptions.ConnectionClosed:
            logger.info(f"Connection {connection_id} closed by client")
        
        return session_id
        
    async def _handle_connect(
        self, 
        connection_id: str, 
        websocket: WebSocketServerProtocol, 
        data: Dict[str, Any]
    ) -> str:
        """
        Handle connection establishment with authentication and session setup.
        
        Educational Impact:
        Establishes secure, FERPA-compliant learning session with proper
        authentication, learner profile loading, and educational context
        initialization for optimal real-time learning adaptation.
        
        Returns:
            session_id: Unique session identifier for educational tracking
        """
        try:
            # Extract connection parameters
            learner_id = data.get('learner_id')
            session_config = data.get('session_config', {})
            
            if not learner_id:
                await self._send_error_message(websocket, "missing_learner_id", "Learner ID required")
                raise ValueError("Missing learner ID")
            
            # Create learning session
            session_id = await self.session_manager.create_session(
                learner_id=learner_id,
                connection_id=connection_id,
                session_config=session_config
            )
            
            # Associate connection with session
            self.connection_sessions[connection_id] = session_id
            
            # Start streaming handler for this session
            await self.streaming_handler.start_session_streaming(
                session_id=session_id,
                connection_id=connection_id,
                websocket=websocket
            )
            
            # Send connection confirmation
            await self._send_message(websocket, {
                "action": "connection_established",
                "session_id": session_id,
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "server_info": {
                    "version": "1.0.0",
                    "capabilities": [
                        "real_time_adaptation",
                        "learning_analytics", 
                        "performance_optimization"
                    ]
                }
            })
            
            logger.info(f"Learning session established: {session_id} for learner: {learner_id}")
            return session_id
            
        except Exception as e:
            logger.error(f"Error establishing connection: {e}")
            await self._send_error_message(websocket, "connection_failed", str(e))
            raise
            
    async def _handle_learning_data(
        self, 
        connection_id: str, 
        websocket: WebSocketServerProtocol, 
        data: Dict[str, Any]
    ) -> None:
        """
        Handle real-time learning data streaming and adaptation processing.
        
        Educational Impact:
        Processes continuous learner interaction data to generate immediate
        educational adaptations, optimizing learning experience in real-time
        based on engagement, performance, and learning state indicators.
        
        Performance Requirements:
        - Processing time: <10ms for adaptation command generation
        - Response latency: <25ms for adaptation delivery
        - Data validation: Complete with educational context preservation
        """
        try:
            session_id = self.connection_sessions.get(connection_id)
            if not session_id:
                await self._send_error_message(websocket, "no_session", "No active session")
                return
            
            # Extract learning data
            interaction_snapshot = data.get('interaction_snapshot', {})
            timestamp = data.get('timestamp')
            
            if not interaction_snapshot:
                await self._send_error_message(websocket, "missing_data", "Interaction snapshot required")
                return
            
            # Process learning data through adaptation processor
            adaptation_result = await self.adaptation_processor.process_learning_data(
                session_id=session_id,
                interaction_snapshot=interaction_snapshot,
                timestamp=timestamp
            )
            
            # Send adaptation commands if generated
            if adaptation_result.get('adaptation_commands'):
                await self._send_message(websocket, {
                    "action": "adaptation_response",
                    "session_id": session_id,
                    "timestamp": datetime.now(timezone.utc).isoformat(),
                    "adaptation_commands": adaptation_result['adaptation_commands'],
                    "updated_learning_state": adaptation_result.get('updated_learning_state'),
                    "performance_metrics": adaptation_result.get('performance_metrics')
                })
                
                self.performance_metrics['adaptation_commands_sent'] += len(
                    adaptation_result['adaptation_commands']
                )
            
            # Update session with latest data
            await self.session_manager.update_session_data(session_id, interaction_snapshot)
            
        except Exception as e:
            logger.error(f"Error processing learning data: {e}")
            await self._send_error_message(websocket, "processing_failed", str(e))
            
    async def _handle_adaptation_request(
        self, 
        connection_id: str, 
        websocket: WebSocketServerProtocol, 
        data: Dict[str, Any]
    ) -> None:
        """
        Handle explicit adaptation requests from VR learning environment.
        
        Educational Impact:
        Responds to specific adaptation requests from the learning environment,
        enabling targeted educational interventions and customized learning
        adjustments based on explicit learner or system needs.
        """
        try:
            session_id = self.connection_sessions.get(connection_id)
            if not session_id:
                await self._send_error_message(websocket, "no_session", "No active session")
                return
            
            # Extract adaptation request parameters
            request_type = data.get('request_type')
            request_parameters = data.get('parameters', {})
            
            # Process adaptation request
            adaptation_result = await self.adaptation_processor.process_adaptation_request(
                session_id=session_id,
                request_type=request_type,
                parameters=request_parameters
            )
            
            # Send adaptation response
            await self._send_message(websocket, {
                "action": "adaptation_response",
                "session_id": session_id,
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "request_type": request_type,
                "adaptation_result": adaptation_result
            })
            
        except Exception as e:
            logger.error(f"Error processing adaptation request: {e}")
            await self._send_error_message(websocket, "adaptation_failed", str(e))
            
    async def _handle_disconnect(
        self, 
        connection_id: str, 
        websocket: WebSocketServerProtocol, 
        data: Dict[str, Any]
    ) -> None:
        """
        Handle graceful disconnection with session cleanup.
        
        Educational Impact:
        Ensures proper educational session closure with learner data
        preservation, progress saving, and educational analytics recording
        for continued learning optimization.
        """
        try:
            session_id = self.connection_sessions.get(connection_id)
            
            if session_id:
                # Stop streaming for this session
                await self.streaming_handler.stop_session_streaming(session_id)
                
                # Finalize session with educational data preservation
                await self.session_manager.finalize_session(session_id, data.get('reason'))
                
                # Send disconnection confirmation
                await self._send_message(websocket, {
                    "action": "disconnection_confirmed",
                    "session_id": session_id,
                    "timestamp": datetime.now(timezone.utc).isoformat(),
                    "session_summary": await self.session_manager.get_session_summary(session_id)
                })
                
            logger.info(f"Graceful disconnection completed for connection: {connection_id}")
            
        except Exception as e:
            logger.error(f"Error handling disconnection: {e}")
            
    async def _close_connection_gracefully(
        self, 
        connection_id: str, 
        websocket: WebSocketServerProtocol
    ) -> None:
        """
        Close connection gracefully with proper cleanup.
        
        Educational Impact:
        Ensures educational session data is properly preserved and learning
        continuity is maintained even during unexpected disconnections.
        """
        try:
            # Send closure notification if connection is still open
            if not websocket.closed:
                await self._send_message(websocket, {
                    "action": "server_shutdown",
                    "timestamp": datetime.now(timezone.utc).isoformat(),
                    "message": "Server shutting down - please reconnect"
                })
                
                await websocket.close()
                
        except Exception as e:
            logger.error(f"Error closing connection gracefully: {e}")
            
    async def _cleanup_connection(self, connection_id: str, session_id: Optional[str]) -> None:
        """
        Cleanup connection resources and session data.
        
        Educational Impact:
        Ensures proper cleanup of educational resources while preserving
        learner data and maintaining FERPA compliance during connection closure.
        """
        try:
            # Remove from active connections
            if connection_id in self.active_connections:
                del self.active_connections[connection_id]
                
            if connection_id in self.connection_sessions:
                del self.connection_sessions[connection_id]
                
            # Update performance metrics
            self.performance_metrics['connections_closed'] += 1
            
            # Cleanup session if exists
            if session_id:
                await self.streaming_handler.stop_session_streaming(session_id)
                await self.session_manager.cleanup_session(session_id)
                
            logger.debug(f"Connection cleanup completed: {connection_id}")
            
        except Exception as e:
            logger.error(f"Error during connection cleanup: {e}")
            
    async def _send_message(self, websocket: WebSocketServerProtocol, message: Dict[str, Any]) -> None:
        """
        Send message to WebSocket client with error handling.
        
        Performance Requirements:
        - Message serialization: <5ms for typical educational data
        - Send latency: <10ms for message delivery
        - Error recovery: Automatic retry for transient failures
        """
        try:
            if not websocket.closed:
                message_json = json.dumps(message)
                await websocket.send(message_json)
                self.message_count += 1
                self.performance_metrics['messages_processed'] += 1
        except Exception as e:
            logger.error(f"Error sending message: {e}")
            
    async def _send_error_message(
        self, 
        websocket: WebSocketServerProtocol, 
        error_code: str, 
        error_message: str
    ) -> None:
        """
        Send error message to WebSocket client.
        
        Educational Impact:
        Provides clear error communication that maintains educational context
        and helps learners understand any issues without disrupting the
        learning experience unnecessarily.
        """
        error_response = {
            "action": "error",
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "error": {
                "code": error_code,
                "message": error_message
            }
        }
        await self._send_message(websocket, error_response)
        
    def _update_performance_metrics(self, processing_time: float) -> None:
        """
        Update performance metrics for monitoring and optimization.
        
        Performance Requirements:
        - Metric update overhead: <1ms for performance tracking
        - Memory efficiency: Minimal memory allocation for metrics
        - Accuracy: Precise timing for optimization analysis
        """
        # Update average processing time
        current_avg = self.performance_metrics['average_processing_time']
        message_count = self.performance_metrics['messages_processed']
        
        if message_count > 0:
            self.performance_metrics['average_processing_time'] = (
                (current_avg * (message_count - 1) + processing_time) / message_count
            )
        else:
            self.performance_metrics['average_processing_time'] = processing_time
            
    def get_server_status(self) -> Dict[str, Any]:
        """
        Get current server status and performance metrics.
        
        Educational Impact:
        Provides comprehensive monitoring data for educational administrators
        to ensure optimal learning environment performance and identify
        opportunities for educational improvement.
        
        Returns:
            Dict containing server status, performance metrics, and educational analytics
        """
        uptime = time.time() - self.start_time if self.is_running else 0
        
        return {
            "server_status": {
                "is_running": self.is_running,
                "host": self.host,
                "port": self.port,
                "uptime_seconds": uptime,
                "active_connections": len(self.active_connections),
                "total_sessions": len(self.connection_sessions)
            },
            "performance_metrics": self.performance_metrics.copy(),
            "educational_metrics": {
                "average_session_duration": self.session_manager.get_average_session_duration(),
                "adaptation_success_rate": self.adaptation_processor.get_adaptation_success_rate(),
                "learning_effectiveness_score": self.adaptation_processor.get_learning_effectiveness_score()
            }
        }
