import logging
import os

def setup_logger():
    os.makedirs("logs", exist_ok=True)
    logger = logging.getLogger("TradingBot")
    logger.setLevel(logging.INFO)

    fh = logging.FileHandler("logs/bot.log")
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    fh.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(fh)

    return logger
