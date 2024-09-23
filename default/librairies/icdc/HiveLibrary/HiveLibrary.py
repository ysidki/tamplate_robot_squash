from pyhive import hive
import pandas as pd


class HiveLibrary:
    # def __init__(self) -> None:
    #     self.conection = None

    def connect_to_hive(self, host, port, username, database, query):
        """
        Press a single key.
        :param key: The key to be pressed (e.g., 'a', 'b', 'enter', 'tab').
        """
        try:
            connection = hive.Connection(host, port, username, database)
            print("Connexion réussie à Hive")
        except Exception as e:
            print(f"Erreur lors de la connexion à Hive : {e}")

        try:
            df = pd.read_sql(query,connection)
            print("Requête exécutée avec succès")
            return df
        except Exception as e:
            print(f"Erreur lors de l'exécution de la requête : {e}")

        

    # you add methods that will become keywords in Robot
    
   