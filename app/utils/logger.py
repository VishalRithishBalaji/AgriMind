from pathlib import Path
from loguru import logger

# Create logs folder automatically

Path("logs").mkdir(exist_ok=True)

logger.remove()

logger.add(
    "logs/system.log",
    rotation="10 MB",
    retention="10 days",
    level="INFO",
    enqueue=True
)

logger.add(
    lambda msg: print(msg, end=""),
    level="INFO"
)

logger.info("Logger Initialized")