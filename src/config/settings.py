"""
Carrega as variaveis de ambiente
"""

class NotFoundEnvroinError(Exception):
    pass


from pathlib import Path

import os
#Classe que Carrega as variaveis de ambiente
class LoadEnvroin:

    def __init__(self)-> None:

        self.BASE_DIR = Path(__file__).resolve().parent / ".env"
        self.envroins = []
        self._exists()
        self._load()
        self._read()


    #confere se o .env existe
    def _exists(self) -> None:

        if not os.path.exists(self.BASE_DIR):

            raise NotFoundEnvroinError("Exepted .env")

    #Carrega as variaveis
    def _load(self) -> None:

        from dotenv import load_dotenv
        load_dotenv(self.BASE_DIR)

    #le as variaveis
    def _read(self) -> None:

        envroins = ["redis_port", "redis_host", "url"]
    
        for name in envroins:

            env = os.getenv(name)

            if env is None:

                raise NotFoundEnvroinError(f"Exepted envroin {name}")

            self.envroins.append(env)


class Envroins(LoadEnvroin):

    def __init__(self):
        super().__init__()

        self.redis_port = self.envroins[0]
        self.redis_host = self.envroins[1]
        self.url = self.envroins[2]



        






    
        