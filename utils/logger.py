import logging
import os
from datetime import datetime


os.makedirs("logs", exist_ok=True)


log_filename = f"logs/execution_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"


logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)


logger = logging.getLogger()
