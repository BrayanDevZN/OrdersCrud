import logging
import sys

"""Configuração global de logs"""
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        # Terminal
        logging.StreamHandler(sys.stdout),

        # Arquivo
        logging.FileHandler(
            "src/logs/app.log",
            encoding="utf-8"
        ),
    ],
)

logger = logging.getLogger(__name__)