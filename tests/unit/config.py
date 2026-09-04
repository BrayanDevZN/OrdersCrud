"""
testes de config
"""

from src.config.settings import Envroins, NotFoundEnvroinError


try:
    envroins = Envroins()

except NotFoundEnvroinError as e:

    raise e



