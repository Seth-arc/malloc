"""
Performance Optimization System for Malloc VR MCP Server

Educational Impact:
Provides real-time performance tuning to maintain optimal learning effectiveness
and Quest 3 VR performance requirements for continuous educational delivery.

Performance Requirements:
- Optimization response: <50ms
- Memory overhead: <10MB
- Quest 3 VR: >72fps maintained
- Latency optimization: <100ms for learning updates

Author: Malloc VR Learning Team
Date: December 26, 2024
"""

import asyncio
import time
import logging
import gc
import threading
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Tuple, Callable
from dataclasses import dataclass, asdict
from enum import Enum
import statistics
import psutil
import weakref
from collections import deque, defaultdict
from concurrent.futures import ThreadPoolExecutor
import json

from ..utils.learning_calculations import LearningCalculations


class OptimizationLevel(Enum):
    """Performance optimization levels"""
    CONSERVATIVE = "conservative"
    BALANCED = "balanced"
    AGGRESSIVE = "aggressive"
    EMERGENCY = "emergency"


@dataclass
class PerformanceMetrics:
    """Real-time performance metrics"""
    timestamp: datetime
    cpu_usage: float
    memory_usage: float
    response_time_ms: float
    quest3_fps: float
    concurrent_learners: int
    cache_hit_rate: float
    gc_count: int
    optimization_level: OptimizationLevel


@dataclass
class OptimizationAction:
    """Performance optimization action"""
    name: str
    description: str
    impact_level: str  # "low", "medium", "high"
    educational_risk: str  # "none", "low", "medium", "high"
    performance_gain: float  # Expected improvement (0.0-1.0)
    executed_at: Optional[datetime] = None
    result: Optional[str] = None


class LearningDataCache:
    """
    Optimized caching system for learning data
    
    Educational Impact:
    Provides high-speed access to frequently used educational data,
    reducing response times and improving learning adaptation speed.
    
    Performance Requirements:
    - Cache access: <5ms
    - Memory efficiency: <100MB total
    - Hit rate: >85%
    """
    
    def __init__(self, max_memory_mb: int = 100, ttl_seconds: int = 300):
        self.max_memory_bytes = max_memory_mb * 1024 * 1024
        self.ttl_seconds = ttl_seconds
        self.cache_data = {}
        self.access_times = {}
        self.access_counts = defaultdict(int)
        self.memory_usage = 0
        self.lock = threading.RLock()
        self.logger = logging.getLogger(__name__)
        
        # Performance tracking
        self.hits = 0
        self.misses = 0
        self.evictions = 0
        
    async def get_learner_cache(self, learner_id: str) -> Optional[Dict[str, Any]]:
        """
        Get cached learner data
        
        Educational Impact:
        Enables immediate access to learner profiles for real-time adaptation
        without database queries, maintaining learning continuity.
        
        Args:
            learner_id: Unique learner identifier
        
        Returns:
            Cached learner data or None if not found/expired
        """
        with self.lock:
            cache_key = f"learner_{learner_id}"
            
            if cache_key not in self.cache_data:
                self.misses += 1
                return None
            
            # Check TTL
            if self._is_expired(cache_key):
                self._remove_item(cache_key)
                self.misses += 1
                return None
            
            # Update access tracking
            self.access_times[cache_key] = time.time()
            self.access_counts[cache_key] += 1
            self.hits += 1
            
            return self.cache_data[cache_key].copy()
    
    async def update_learner_cache(self, learner_id: str, data: Dict[str, Any]) -> None:
        """
        Update cached learner data
        
        Educational Impact:
        Ensures learner profiles are immediately available for subsequent
        learning adaptations, maintaining educational effectiveness.
        
        Args:
            learner_id: Unique learner identifier
            data: Updated learner data to cache
        """
        with self.lock:
            cache_key = f"learner_{learner_id}"
            
            # Calculate memory usage
            data_size = len(json.dumps(data, default=str).encode('utf-8'))
            
            # Evict if necessary
            while (self.memory_usage + data_size > self.max_memory_bytes and 
                   len(self.cache_data) > 0):
                self._evict_lru_item()
            
            # Store data
            if cache_key in self.cache_data:
                # Update existing
                old_size = len(json.dumps(self.cache_data[cache_key], default=str).encode('utf-8'))
                self.memory_usage = self.memory_usage - old_size + data_size
            else:
                # New entry
                self.memory_usage += data_size
            
            self.cache_data[cache_key] = data.copy()
            self.access_times[cache_key] = time.time()
            self.access_counts[cache_key] += 1
    
    def _is_expired(self, cache_key: str) -> bool:
        """Check if cache item is expired"""
        if cache_key not in self.access_times:
            return True
        
        return time.time() - self.access_times[cache_key] > self.ttl_seconds
    
    def _remove_item(self, cache_key: str) -> None:
        """Remove item from cache"""
        if cache_key in self.cache_data:
            data_size = len(json.dumps(self.cache_data[cache_key], default=str).encode('utf-8'))
            self.memory_usage -= data_size
            del self.cache_data[cache_key]
        
        if cache_key in self.access_times:
            del self.access_times[cache_key]
        
        if cache_key in self.access_counts:
            del self.access_counts[cache_key]
    
    def _evict_lru_item(self) -> None:
        """Evict least recently used item"""
        if not self.access_times:
            return
        
        # Find LRU item
        lru_key = min(self.access_times.keys(), key=lambda k: self.access_times[k])
        self._remove_item(lru_key)
        self.evictions += 1
    
    def get_cache_statistics(self) -> Dict[str, Any]:
        """Get cache performance statistics"""
        total_requests = self.hits + self.misses
        hit_rate = (self.hits / total_requests * 100) if total_requests > 0 else 0
        
        return {
            "hits": self.hits,
            "misses": self.misses,
            "hit_rate": hit_rate,
            "evictions": self.evictions,
            "memory_usage_mb": self.memory_usage / (1024 * 1024),
            "cache_size": len(self.cache_data),
            "total_requests": total_requests
        }
    
    async def cleanup_expired(self) -> int:
        """Clean up expired cache entries"""
        with self.lock:
            expired_keys = [
                key for key in self.access_times.keys()
                if self._is_expired(key)
            ]
            
            for key in expired_keys:
                self._remove_item(key)
            
            return len(expired_keys)


class PerformanceOptimizer:
    """
    Real-time performance optimization system
    
    Educational Impact:
    Maintains optimal system performance for educational effectiveness,
    ensuring Quest 3 VR requirements and sub-100ms learning adaptation response.
    
    Performance Requirements:
    - Optimization decisions: <10ms
    - Memory monitoring: Continuous
    - Quest 3 fps: >72fps maintained
    - Educational impact: Minimal during optimization
    """
    
    def __init__(self, target_fps: float = 72.0, max_response_time_ms: float = 100.0):
        self.target_fps = target_fps
        self.max_response_time_ms = max_response_time_ms
        self.cache_manager = LearningDataCache()
        self.computation_pool = ThreadPoolExecutor(max_workers=4)
        self.logger = logging.getLogger(__name__)
        
        # Performance monitoring
        self.metrics_history = deque(maxlen=1000)
        self.optimization_actions = []
        self.current_optimization_level = OptimizationLevel.BALANCED
        
        # Optimization thresholds
        self.thresholds = {
            "cpu_critical": 85.0,
            "cpu_warning": 70.0,
            "memory_critical": 90.0,
            "memory_warning": 75.0,
            "response_time_critical": 150.0,
            "response_time_warning": 100.0,
            "fps_critical": 60.0,
            "fps_warning": 70.0
        }
        
        # Optimization strategies
        self.optimization_strategies = {
            OptimizationLevel.CONSERVATIVE: self._conservative_optimizations,
            OptimizationLevel.BALANCED: self._balanced_optimizations,
            OptimizationLevel.AGGRESSIVE: self._aggressive_optimizations,
            OptimizationLevel.EMERGENCY: self._emergency_optimizations
        }
        
        # Background tasks
        self.optimization_task = None
        self.monitoring_active = False
        
    async def initialize(self) -> None:
        """Initialize performance optimizer"""
        self.logger.info("Performance Optimizer initialized")
        await self.start_monitoring()
    
    async def start_monitoring(self) -> None:
        """Start performance monitoring and optimization"""
        if self.monitoring_active:
            return
        
        self.monitoring_active = True
        self.optimization_task = asyncio.create_task(self._optimization_loop())
        self.logger.info("Performance monitoring and optimization started")
    
    async def stop_monitoring(self) -> None:
        """Stop performance monitoring"""
        if not self.monitoring_active:
            return
        
        self.monitoring_active = False
        if self.optimization_task:
            self.optimization_task.cancel()
            try:
                await self.optimization_task
            except asyncio.CancelledError:
                pass
        
        self.logger.info("Performance monitoring stopped")
    
    async def _optimization_loop(self) -> None:
        """Main optimization monitoring loop"""
        while self.monitoring_active:
            try:
                # Collect current metrics
                metrics = await self._collect_performance_metrics()
                self.metrics_history.append(metrics)
                
                # Determine required optimization level
                required_level = self._analyze_optimization_needs(metrics)
                
                # Apply optimizations if needed
                if required_level != self.current_optimization_level:
                    await self._apply_optimization_level(required_level)
                    self.current_optimization_level = required_level
                
                # Periodic optimizations
                await self._apply_periodic_optimizations()
                
                # Wait before next optimization cycle
                await asyncio.sleep(5)  # 5-second optimization cycle
                
            except asyncio.CancelledError:
                break
            except Exception as e:
                self.logger.error(f"Optimization loop error: {e}")
                await asyncio.sleep(5)
    
    async def _collect_performance_metrics(self) -> PerformanceMetrics:
        """Collect current system performance metrics"""
        try:
            # System metrics
            cpu_usage = psutil.cpu_percent(interval=0.1)
            memory = psutil.virtual_memory()
            memory_usage = memory.percent
            
            # Simulated Quest 3 FPS (in real implementation, this would come from VR system)
            quest3_fps = self._estimate_quest3_fps(cpu_usage, memory_usage)
            
            # Response time (measured from recent operations)
            response_time_ms = await self._measure_response_time()
            
            # Cache performance
            cache_stats = self.cache_manager.get_cache_statistics()
            cache_hit_rate = cache_stats["hit_rate"]
            
            # GC metrics
            gc_count = len(gc.get_objects())
            
            # Simulated concurrent learners
            concurrent_learners = min(50, max(1, int(100 - cpu_usage)))  # Simplified simulation
            
            return PerformanceMetrics(
                timestamp=datetime.now(),
                cpu_usage=cpu_usage,
                memory_usage=memory_usage,
                response_time_ms=response_time_ms,
                quest3_fps=quest3_fps,
                concurrent_learners=concurrent_learners,
                cache_hit_rate=cache_hit_rate,
                gc_count=gc_count,
                optimization_level=self.current_optimization_level
            )
            
        except Exception as e:
            self.logger.error(f"Failed to collect performance metrics: {e}")
            return PerformanceMetrics(
                timestamp=datetime.now(),
                cpu_usage=0.0,
                memory_usage=0.0,
                response_time_ms=1000.0,  # High fallback
                quest3_fps=60.0,  # Low fallback
                concurrent_learners=1,
                cache_hit_rate=0.0,
                gc_count=0,
                optimization_level=self.current_optimization_level
            )
    
    def _estimate_quest3_fps(self, cpu_usage: float, memory_usage: float) -> float:
        """Estimate Quest 3 VR fps based on system performance"""
        # Simplified estimation model
        base_fps = 90.0  # Quest 3 target fps
        
        # CPU impact
        if cpu_usage > 80:
            base_fps -= (cpu_usage - 80) * 2.0
        elif cpu_usage > 60:
            base_fps -= (cpu_usage - 60) * 0.5
        
        # Memory impact
        if memory_usage > 85:
            base_fps -= (memory_usage - 85) * 1.5
        elif memory_usage > 70:
            base_fps -= (memory_usage - 70) * 0.3
        
        return max(30.0, min(90.0, base_fps))
    
    async def _measure_response_time(self) -> float:
        """Measure current system response time"""
        start_time = time.time()
        
        try:
            # Simulate a typical learning operation
            await asyncio.sleep(0.001)  # 1ms base operation
            
            # Add cache lookup simulation
            test_data = await self.cache_manager.get_learner_cache("test_user")
            
            # Simple computation
            result = sum(range(100))
            
        except Exception:
            pass  # Don't fail on test operation
        
        end_time = time.time()
        return (end_time - start_time) * 1000  # Convert to milliseconds
    
    def _analyze_optimization_needs(self, metrics: PerformanceMetrics) -> OptimizationLevel:
        """Analyze current metrics to determine optimization needs"""
        # Check for emergency conditions
        if (metrics.cpu_usage > self.thresholds["cpu_critical"] or
            metrics.memory_usage > self.thresholds["memory_critical"] or
            metrics.response_time_ms > self.thresholds["response_time_critical"] or
            metrics.quest3_fps < self.thresholds["fps_critical"]):
            return OptimizationLevel.EMERGENCY
        
        # Check for aggressive optimization needs
        critical_count = 0
        if metrics.cpu_usage > self.thresholds["cpu_warning"]:
            critical_count += 1
        if metrics.memory_usage > self.thresholds["memory_warning"]:
            critical_count += 1
        if metrics.response_time_ms > self.thresholds["response_time_warning"]:
            critical_count += 1
        if metrics.quest3_fps < self.thresholds["fps_warning"]:
            critical_count += 1
        
        if critical_count >= 3:
            return OptimizationLevel.AGGRESSIVE
        elif critical_count >= 1:
            return OptimizationLevel.BALANCED
        else:
            return OptimizationLevel.CONSERVATIVE
    
    async def _apply_optimization_level(self, level: OptimizationLevel) -> None:
        """Apply optimizations for the specified level"""
        self.logger.info(f"Applying {level.value} optimization level")
        
        strategy = self.optimization_strategies.get(level)
        if strategy:
            actions = await strategy()
            self.optimization_actions.extend(actions)
            
            # Log actions taken
            for action in actions:
                self.logger.info(f"Optimization applied: {action.name} - {action.description}")
    
    async def _conservative_optimizations(self) -> List[OptimizationAction]:
        """Conservative optimization strategies"""
        actions = []
        
        # Light cache cleanup
        expired_count = await self.cache_manager.cleanup_expired()
        if expired_count > 0:
            actions.append(OptimizationAction(
                name="cache_cleanup",
                description=f"Cleaned up {expired_count} expired cache entries",
                impact_level="low",
                educational_risk="none",
                performance_gain=0.05,
                executed_at=datetime.now(),
                result="success"
            ))
        
        # Gentle garbage collection
        if len(gc.get_objects()) > 10000:
            gc.collect()
            actions.append(OptimizationAction(
                name="garbage_collection",
                description="Performed gentle garbage collection",
                impact_level="low",
                educational_risk="none",
                performance_gain=0.03,
                executed_at=datetime.now(),
                result="success"
            ))
        
        return actions
    
    async def _balanced_optimizations(self) -> List[OptimizationAction]:
        """Balanced optimization strategies"""
        actions = await self._conservative_optimizations()
        
        # More aggressive cache management
        cache_stats = self.cache_manager.get_cache_statistics()
        if cache_stats["memory_usage_mb"] > 80:
            # Force cache cleanup
            with self.cache_manager.lock:
                items_to_remove = len(self.cache_manager.cache_data) // 4
                lru_keys = sorted(
                    self.cache_manager.access_times.keys(),
                    key=lambda k: self.cache_manager.access_times[k]
                )[:items_to_remove]
                
                for key in lru_keys:
                    self.cache_manager._remove_item(key)
            
            actions.append(OptimizationAction(
                name="cache_reduction",
                description=f"Reduced cache size by {items_to_remove} items",
                impact_level="medium",
                educational_risk="low",
                performance_gain=0.15,
                executed_at=datetime.now(),
                result="success"
            ))
        
        # Thread pool optimization
        if hasattr(self.computation_pool, '_threads'):
            current_workers = len(self.computation_pool._threads)
            if current_workers > 2:
                # Reduce thread pool size
                self.computation_pool._max_workers = max(2, current_workers - 1)
                actions.append(OptimizationAction(
                    name="thread_reduction",
                    description=f"Reduced thread pool to {self.computation_pool._max_workers} workers",
                    impact_level="medium",
                    educational_risk="low",
                    performance_gain=0.10,
                    executed_at=datetime.now(),
                    result="success"
                ))
        
        return actions
    
    async def _aggressive_optimizations(self) -> List[OptimizationAction]:
        """Aggressive optimization strategies"""
        actions = await self._balanced_optimizations()
        
        # Aggressive memory cleanup
        gc.collect()
        gc.collect()  # Double collection
        actions.append(OptimizationAction(
            name="aggressive_gc",
            description="Performed aggressive garbage collection",
            impact_level="high",
            educational_risk="medium",
            performance_gain=0.25,
            executed_at=datetime.now(),
            result="success"
        ))
        
        # Cache size reduction
        with self.cache_manager.lock:
            # Keep only most frequently accessed items
            if len(self.cache_manager.cache_data) > 10:
                top_keys = sorted(
                    self.cache_manager.access_counts.keys(),
                    key=lambda k: self.cache_manager.access_counts[k],
                    reverse=True
                )[:10]
                
                keys_to_remove = [
                    key for key in self.cache_manager.cache_data.keys()
                    if key not in top_keys
                ]
                
                for key in keys_to_remove:
                    self.cache_manager._remove_item(key)
                
                actions.append(OptimizationAction(
                    name="cache_aggressive_reduction",
                    description=f"Reduced cache to top 10 items (removed {len(keys_to_remove)})",
                    impact_level="high",
                    educational_risk="medium",
                    performance_gain=0.30,
                    executed_at=datetime.now(),
                    result="success"
                ))
        
        return actions
    
    async def _emergency_optimizations(self) -> List[OptimizationAction]:
        """Emergency optimization strategies"""
        actions = await self._aggressive_optimizations()
        
        # Emergency cache clear
        with self.cache_manager.lock:
            cache_size = len(self.cache_manager.cache_data)
            self.cache_manager.cache_data.clear()
            self.cache_manager.access_times.clear()
            self.cache_manager.access_counts.clear()
            self.cache_manager.memory_usage = 0
        
        actions.append(OptimizationAction(
            name="emergency_cache_clear",
            description=f"Emergency cache clear (removed {cache_size} items)",
            impact_level="critical",
            educational_risk="high",
            performance_gain=0.50,
            executed_at=datetime.now(),
            result="success"
        ))
        
        # Force garbage collection
        import gc
        gc.disable()
        gc.collect()
        gc.enable()
        
        actions.append(OptimizationAction(
            name="emergency_gc",
            description="Emergency garbage collection with temporary disable",
            impact_level="critical",
            educational_risk="high",
            performance_gain=0.40,
            executed_at=datetime.now(),
            result="success"
        ))
        
        # Log emergency condition
        self.logger.critical("Emergency optimization procedures executed")
        
        return actions
    
    async def _apply_periodic_optimizations(self) -> None:
        """Apply periodic maintenance optimizations"""
        try:
            # Periodic cache cleanup (every 5 minutes)
            if len(self.metrics_history) % 60 == 0:  # 5 minutes at 5-second intervals
                await self.cache_manager.cleanup_expired()
            
            # Periodic garbage collection (every 10 minutes)
            if len(self.metrics_history) % 120 == 0:  # 10 minutes at 5-second intervals
                gc.collect()
                
        except Exception as e:
            self.logger.error(f"Periodic optimization error: {e}")
    
    async def optimize_learning_computation(self, learner_id: str) -> Any:
        """
        Optimize computation of learning adaptation equation
        
        Educational Impact:
        Ensures learning adaptations are computed within 100ms requirements
        while maintaining educational accuracy and effectiveness.
        
        Args:
            learner_id: Unique learner identifier
        
        Returns:
            Optimized learning computation result
        """
        try:
            # Check cache first
            cached_data = await self.cache_manager.get_learner_cache(learner_id)
            
            if cached_data and not self.needs_recomputation(cached_data):
                return cached_data.get("last_computation")
            
            # Async computation for non-blocking operation
            future = self.computation_pool.submit(
                self.compute_learning_adaptation, learner_id
            )
            
            result = await asyncio.wrap_future(future)
            
            # Update cache
            cache_data = cached_data.copy() if cached_data else {}
            cache_data["last_computation"] = result
            cache_data["last_update"] = time.time()
            await self.cache_manager.update_learner_cache(learner_id, cache_data)
            
            return result
            
        except Exception as e:
            self.logger.error(f"Learning computation optimization failed for {learner_id}: {e}")
            # Fallback to basic computation
            return self.compute_learning_adaptation(learner_id)
    
    def needs_recomputation(self, cached_data: Dict[str, Any]) -> bool:
        """Check if cached computation needs refresh"""
        if not cached_data or "last_update" not in cached_data:
            return True
        
        # Recompute if cache is older than 30 seconds
        return time.time() - cached_data["last_update"] > 30
    
    def compute_learning_adaptation(self, learner_id: str) -> Dict[str, Any]:
        """
        Compute learning adaptation (placeholder implementation)
        
        Educational Impact:
        Provides core learning adaptation computation while maintaining
        performance requirements for real-time educational response.
        """
        # Simplified computation for demonstration
        # In real implementation, this would use LearningCalculations
        calc = LearningCalculations()
        
        # Simulate computation
        result = {
            "adaptation_strength": 0.75,
            "difficulty_adjustment": 0.1,
            "engagement_factor": 0.85,
            "computed_at": time.time(),
            "learner_id": learner_id
        }
        
        return result
    
    def get_performance_summary(self) -> Dict[str, Any]:
        """Get comprehensive performance summary"""
        if not self.metrics_history:
            return {}
        
        recent_metrics = list(self.metrics_history)[-10:]  # Last 10 metrics
        
        # Calculate averages
        avg_cpu = statistics.mean([m.cpu_usage for m in recent_metrics])
        avg_memory = statistics.mean([m.memory_usage for m in recent_metrics])
        avg_response_time = statistics.mean([m.response_time_ms for m in recent_metrics])
        avg_fps = statistics.mean([m.quest3_fps for m in recent_metrics])
        avg_cache_hit_rate = statistics.mean([m.cache_hit_rate for m in recent_metrics])
        
        # Cache statistics
        cache_stats = self.cache_manager.get_cache_statistics()
        
        # Recent optimizations
        recent_optimizations = [
            action for action in self.optimization_actions[-10:]
        ]
        
        return {
            "current_optimization_level": self.current_optimization_level.value,
            "performance_averages": {
                "cpu_usage": round(avg_cpu, 2),
                "memory_usage": round(avg_memory, 2),
                "response_time_ms": round(avg_response_time, 2),
                "quest3_fps": round(avg_fps, 2),
                "cache_hit_rate": round(avg_cache_hit_rate, 2)
            },
            "cache_statistics": cache_stats,
            "recent_optimizations": [
                {
                    "name": action.name,
                    "description": action.description,
                    "impact_level": action.impact_level,
                    "performance_gain": action.performance_gain,
                    "executed_at": action.executed_at.isoformat() if action.executed_at else None
                }
                for action in recent_optimizations
            ],
            "metrics_collected": len(self.metrics_history),
            "total_optimizations": len(self.optimization_actions)
        }
    
    def is_performance_acceptable(self) -> Tuple[bool, List[str]]:
        """Check if current performance meets requirements"""
        if not self.metrics_history:
            return False, ["No performance data available"]
        
        latest = self.metrics_history[-1]
        issues = []
        
        if latest.cpu_usage > self.thresholds["cpu_warning"]:
            issues.append(f"High CPU usage: {latest.cpu_usage:.1f}%")
        
        if latest.memory_usage > self.thresholds["memory_warning"]:
            issues.append(f"High memory usage: {latest.memory_usage:.1f}%")
        
        if latest.response_time_ms > self.thresholds["response_time_warning"]:
            issues.append(f"High response time: {latest.response_time_ms:.1f}ms")
        
        if latest.quest3_fps < self.thresholds["fps_warning"]:
            issues.append(f"Low Quest 3 FPS: {latest.quest3_fps:.1f}")
        
        if latest.cache_hit_rate < 80:
            issues.append(f"Low cache hit rate: {latest.cache_hit_rate:.1f}%")
        
        return len(issues) == 0, issues


# Utility functions for performance optimization integration

async def create_performance_optimizer(
    target_fps: float = 72.0,
    max_response_time_ms: float = 100.0
) -> PerformanceOptimizer:
    """
    Create and initialize performance optimizer
    
    Educational Impact:
    Establishes real-time performance optimization to ensure consistent
    educational effectiveness and Quest 3 VR performance requirements.
    
    Args:
        target_fps: Target VR fps to maintain
        max_response_time_ms: Maximum acceptable response time
    
    Returns:
        Initialized performance optimizer
    """
    optimizer = PerformanceOptimizer(target_fps, max_response_time_ms)
    await optimizer.initialize()
    return optimizer


def setup_performance_logging() -> None:
    """Set up specialized logging for performance optimization"""
    # Create performance specific logger
    perf_logger = logging.getLogger("malloc_vr.performance")
    perf_logger.setLevel(logging.INFO)
    
    # Create file handler for performance logs
    try:
        handler = logging.FileHandler("logs/performance_optimization.log")
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        perf_logger.addHandler(handler)
    except Exception as e:
        print(f"Warning: Could not set up performance optimization log file: {e}")
