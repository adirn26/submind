from pymongo import MongoClient


class AtlasClient:

    def __init__(self, altas_uri, dbname):
        self.mongodb_client = MongoClient(altas_uri)
        self.database = self.mongodb_client[dbname]

    # A quick way to test if we can connect to Atlas instance
    def ping(self):
        self.mongodb_client.admin.command("ping")

    # Get the MongoDB Atlas collection to connect to
    def get_collection(self, collection_name):
        collection = self.database[collection_name]
        return collection

    # Query a MongoDB collection
    def find(self, collection_name, filter={}, limit=0):
        collection = self.database[collection_name]
        items = list(collection.find(filter=filter, limit=limit))
        return items
    
    # Get list of all collections in the database
    def list_collections(self):
        """Returns a list of all collection names in the database.
        
        Returns:
            list: A list of collection names as strings.
        """
        return self.database.list_collection_names()
    
    def run_aggregate_pipeline(self, collection_name, pipeline):
        collection = self.database[collection_name]
        items = list(collection.aggregate(pipeline))
        return [dict(item) for item in items]
