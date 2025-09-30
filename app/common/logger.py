import logging
import os
from datetime import datetime

LOGS_DIR = "logs"
os.makedirs(LOGS_DIR,exist_ok=True)

LOG_FILE = os.path.join(LOGS_DIR, f"log_{datetime.now().strftime('%Y-%m-%d')}.log")

logging.basicConfig(
    filename=LOG_FILE,
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger

# DEBUG → detailed diagnostic info (for developers)

# INFO → general runtime events (things are working as expected)

# WARNING → something unexpected, but not breaking

# ERROR → something failed, but program continues

# CRITICAL → serious error, program may crash