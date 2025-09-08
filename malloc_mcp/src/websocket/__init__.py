"""
WebSocket Communication Protocol Package

Educational Impact:
This package provides real-time WebSocket communication for continuous learning
adaptation, enabling immediate response to learner interactions and maintaining
optimal learning flow without interruption.

Performance Requirements:
- WebSocket latency: <25ms for real-time adaptation
- Concurrent connections: Support 50+ simultaneous learners
- Message processing: <10ms for adaptation command generation
- Data streaming: 5-second intervals for continuous learning data

The WebSocket protocol enables the mathematical learning equation to operate
in real-time, providing immediate adaptation based on learner state changes,
engagement metrics, and performance indicators.
"""

from .websocket_server import WebSocketServer
from .session_manager import SessionManager
from .adaptation_processor import AdaptationProcessor
from .streaming_handler import StreamingHandler

__all__ = [
    'WebSocketServer',
    'SessionManager', 
    'AdaptationProcessor',
    'StreamingHandler'
]
