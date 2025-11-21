"""Datenbank verknüpfung

In dieser Datei wird die Datenbank verknüpft und verschiedene Funktionen bereitgestellt.

"""

from configs.config import mongo_uri
from pymongo import MongoClient

class Database:
    def __init__(self):
        self.db = mongo_uri