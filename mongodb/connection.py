# mongodb/connection.py

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ConfigurationError

class MongoDBConnection:
    """
    Manages connection to a MongoDB instance.

    Attributes:
        client (MongoClient): The MongoDB client instance.
        db (Database): The connected database instance.
    """
    
    def __init__(self, uri: str, db_name: str):
        """
        Initialize the connection to MongoDB.

        Args:
            uri (str): The connection URI for MongoDB.
            db_name (str): The name of the database to connect to.
        """
        self.client = None
        self.db = None
        self.uri = uri
        self.db_name = db_name

    def connect(self):
        """
        Establish connection to MongoDB and select the database.

        Raises:
            ConnectionFailure: If MongoDB is not reachable.
            ConfigurationError: If URI or configuration is invalid.
        """
        try:
            self.client = MongoClient(self.uri)
            self.db = self.client[self.db_name]
            # Validate connection
            self.client.admin.command('ping')
            print(f"Connected to MongoDB: {self.db_name}")
        except ConnectionFailure as e:
            raise ConnectionFailure("Could not connect to MongoDB: ", e)
        except ConfigurationError as e:
            raise ConfigurationError("Invalid MongoDB URI or configuration: ", e)

    def close(self):
        """
        Close the connection to MongoDB.
        """
        if self.client:
            self.client.close()
            print("MongoDB connection closed.")