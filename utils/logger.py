import logging
import os

def get_logger(name="TestLogger"):
    os.makedirs("reports/logs", exist_ok=True)
    log_file = os.path.join("reports/logs", "execution.log")

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        # File handler
        fh = logging.FileHandler(log_file, mode='w')
        fh.setLevel(logging.INFO)
        # Console handler
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # Formato
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # Añadir handlers
        logger.addHandler(fh)
        logger.addHandler(ch)

    return logger
