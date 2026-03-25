"""C5 Auto-Cron: Automated Memory Decay Scheduling.

This module provides automated scheduling for C5 memory decay cleanup.
It supports multiple scheduling backends:
- APScheduler (recommended for production)
- schedule library (lightweight alternative)
- Manual cron script (for system cron)

Usage:
    # Start auto-cron scheduler
    from compositional_co_scientist.core.constraints.c5_auto_cron import start_c5_scheduler
    
    scheduler = start_c5_scheduler(run_interval_hours=24)
    
    # ... application runs ...
    
    # Stop scheduler on shutdown
    scheduler.shutdown()
"""
from typing import Optional, Callable, Dict, Any
from pathlib import Path
import logging
import os

logger = logging.getLogger(__name__)


def get_default_db_path() -> Path:
    """Get default memory database path."""
    data_dir = Path(os.environ.get(
        "CO_SCIENTIST_DATA",
        Path.home() / ".composable_co_scientist"
    ))
    return data_dir / "memory.db"


def run_c5_maintenance(
    db_path: Optional[Path] = None,
    utility_threshold: float = 0.3,
    decay_factor: float = 0.5
) -> Dict[str, Any]:
    """Run C5 maintenance routine.

    This function wraps the decay cleanup and health check functions
    for convenient scheduling.

    Args:
        db_path: Path to memory database. Uses default if None.
        utility_threshold: Utility score threshold for decay.
        decay_factor: Factor to multiply utility by when decaying.

    Returns:
        Dictionary containing maintenance results and health metrics.
    """
    from compositional_co_scientist.core.constraints.c5_memory_decay import (
        run_decay_cleanup,
        get_memory_stats,
        check_memory_health
    )

    db_path = db_path or get_default_db_path()

    logger.info(f"Starting C5 maintenance (db={db_path}, threshold={utility_threshold})")

    # Run decay cleanup
    cleanup_result = run_decay_cleanup(
        db_path=db_path,
        utility_threshold=utility_threshold,
        decay_factor=decay_factor
    )

    # Get statistics
    stats = get_memory_stats(db_path=db_path)

    # Check health (may raise ConstraintViolationError if unhealthy)
    try:
        health = check_memory_health(db_path=db_path)
        health_status = "healthy"
    except Exception as e:
        health = {"error": str(e)}
        health_status = "unhealthy"
        logger.warning(f"C5 health check failed: {e}")

    result = {
        **cleanup_result,
        "stats": stats,
        "health": health,
        "health_status": health_status
    }

    logger.info(
        f"C5 maintenance complete: "
        f"deleted={cleanup_result['expired_deleted']}, "
        f"decayed={cleanup_result['decayed_count']}, "
        f"status={health_status}"
    )

    return result


def create_apscheduler_callback(
    db_path: Optional[Path] = None,
    utility_threshold: float = 0.3,
    decay_factor: float = 0.5
) -> Callable:
    """Create APScheduler callback for C5 maintenance.

    Args:
        db_path: Path to memory database.
        utility_threshold: Utility score threshold.
        decay_factor: Decay factor.

    Returns:
        Callable function for APScheduler job.
    """
    def callback():
        try:
            result = run_c5_maintenance(
                db_path=db_path,
                utility_threshold=utility_threshold,
                decay_factor=decay_factor
            )
            logger.info(f"C5 maintenance completed: {result}")
            return result
        except Exception as e:
            logger.error(f"C5 maintenance failed: {e}", exc_info=True)
            raise

    return callback


def start_c5_scheduler(
    run_interval_hours: int = 24,
    db_path: Optional[Path] = None,
    utility_threshold: float = 0.3,
    decay_factor: float = 0.5,
    start_immediately: bool = True
) -> Optional[Any]:
    """Start APScheduler for automated C5 maintenance.

    This function sets up a background scheduler that runs C5 maintenance
    at the specified interval.

    Args:
        run_interval_hours: How often to run maintenance (default 24 hours).
        db_path: Path to memory database.
        utility_threshold: Utility score threshold.
        decay_factor: Decay factor.
        start_immediately: Whether to run maintenance immediately on startup.

    Returns:
        APScheduler instance (or None if APScheduler not installed).

    Example:
        scheduler = start_c5_scheduler(run_interval_hours=24)
        # ... application runs ...
        scheduler.shutdown()  # On shutdown
    """
    try:
        from apscheduler.schedulers.background import BackgroundScheduler
        from apscheduler.triggers.interval import IntervalTrigger
    except ImportError:
        logger.warning(
            "APScheduler not installed. Install with: pip install apscheduler\n"
            "C5 auto-cron will not run. Manual cleanup still available via "
            "compositional_co_scientist.core.constraints.c5_memory_decay.run_decay_cleanup()"
        )
        return None

    # Create scheduler
    scheduler = BackgroundScheduler(
        job_defaults={
            'coalesce': True,  # Combine multiple pending executions
            'max_instances': 1,  # Only one maintenance job at a time
            'misfire_grace_time': 3600  # 1 hour grace for missed executions
        }
    )

    # Create job callback
    callback = create_apscheduler_callback(
        db_path=db_path,
        utility_threshold=utility_threshold,
        decay_factor=decay_factor
    )

    # Add job with interval trigger
    scheduler.add_job(
        callback,
        trigger=IntervalTrigger(hours=run_interval_hours),
        id='c5_maintenance',
        name='C5 Memory Decay Maintenance',
        replace_existing=True
    )

    # Run immediately if requested
    if start_immediately:
        logger.info("Running initial C5 maintenance...")
        callback()

    # Start scheduler
    scheduler.start()
    logger.info(f"C5 scheduler started (interval={run_interval_hours}h)")

    return scheduler


def stop_c5_scheduler(scheduler: Any) -> None:
    """Stop APScheduler for C5 maintenance.

    Args:
        scheduler: APScheduler instance from start_c5_scheduler().
    """
    if scheduler is not None:
        scheduler.shutdown(wait=True)
        logger.info("C5 scheduler stopped")


def create_cron_script() -> str:
    """Create a cron script for C5 maintenance.

    This generates a standalone Python script that can be run
    from system cron.

    Returns:
        Python script content as string.

    Example cron entry (run daily at 2:00 AM):
        0 2 * * * /usr/bin/python3 /path/to/c5_cron.py >> /var/log/c5_maintenance.log 2>&1
    """
    script = '''#!/usr/bin/env python3
"""C5 Maintenance Cron Script.

This script is designed to be run from system cron for automated
C5 memory decay maintenance.

Example cron entry (daily at 2:00 AM):
    0 2 * * * /usr/bin/python3 c5_cron.py >> /var/log/c5_maintenance.log 2>&1
"""
import sys
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def main():
    """Run C5 maintenance."""
    try:
        from compositional_co_scientist.core.constraints.c5_auto_cron import (
            run_c5_maintenance
        )

        result = run_c5_maintenance()

        logger.info(f"C5 maintenance completed: {result}")

        # Exit with error if health check failed
        if result.get('health_status') == 'unhealthy':
            logger.warning("C5 health check failed")
            sys.exit(1)

        sys.exit(0)

    except Exception as e:
        logger.error(f"C5 maintenance failed: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
'''
    return script


def install_cron_job(
    script_path: Path,
    schedule: str = "0 2 * * *",
    log_path: Optional[Path] = None
) -> str:
    """Install C5 maintenance cron job.

    This function adds a cron entry to the user's crontab.

    Args:
        script_path: Path to the cron script (from create_cron_script()).
        schedule: Cron schedule string (default: daily at 2:00 AM).
        log_path: Path to log file (default: ~/.composable_co_scientist/c5_maintenance.log).

    Returns:
        The cron entry that was installed.

    Note:
        This function only works on Unix-like systems (Linux, macOS).
        For Windows, use Task Scheduler instead.
    """
    import subprocess
    import tempfile

    if log_path is None:
        log_path = Path.home() / ".composable_co_scientist" / "c5_maintenance.log"

    # Ensure log directory exists
    log_path.parent.mkdir(parents=True, exist_ok=True)

    # Create cron entry
    cron_entry = f"{schedule} /usr/bin/python3 {script_path} >> {log_path} 2>&1"

    # Get current crontab
    try:
        result = subprocess.run(
            ["crontab", "-l"],
            capture_output=True,
            text=True,
            check=False
        )
        current_crontab = result.stdout if result.returncode == 0 else ""
    except FileNotFoundError:
        logger.warning("crontab command not found. Cannot install cron job automatically.")
        return cron_entry

    # Check if entry already exists
    if cron_entry in current_crontab:
        logger.info("C5 cron job already installed")
        return cron_entry

    # Add new entry
    new_crontab = current_crontab + f"\n# C5 Memory Decay Maintenance\n{cron_entry}\n"

    # Install new crontab
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.crontab') as f:
        f.write(new_crontab)
        temp_path = f.name

    try:
        subprocess.run(
            ["crontab", temp_path],
            check=True
        )
        logger.info(f"C5 cron job installed: {cron_entry}")
    finally:
        Path(temp_path).unlink()

    return cron_entry


def create_windows_scheduled_task(
    script_path: Path,
    task_name: str = "ComposableCoScientist_C5_Maintenance",
    schedule: str = "DAILY",
    start_time: str = "02:00"
) -> Dict[str, Any]:
    """Create Windows Scheduled Task for C5 maintenance.

    Args:
        script_path: Path to the cron script.
        task_name: Name for the scheduled task.
        schedule: Schedule type (DAILY, WEEKLY, etc.).
        start_time: Start time in HH:MM format.

    Returns:
        Dictionary with task creation results.

    Note:
        Requires administrator privileges.
    """
    import subprocess

    python_exe = sys.executable
    script_path = Path(script_path).absolute()

    # Build schtasks command
    cmd = [
        "schtasks", "/Create",
        "/TN", task_name,
        "/TR", f'"{python_exe}" "{script_path}"',
        "/SC", schedule,
        "/ST", start_time,
        "/RL", "HIGHEST",  # Run with highest privileges
        "/F"  # Force creation (overwrite if exists)
    ]

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True
        )
        logger.info(f"Windows scheduled task created: {task_name}")
        return {
            "success": True,
            "task_name": task_name,
            "output": result.stdout
        }
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to create scheduled task: {e}")
        return {
            "success": False,
            "error": str(e),
            "stderr": e.stderr
        }
