# mongodb/crud.py

class MongoDBCRUD:
    """
    Provides CRUD operations for a specific MongoDB collection.

    Attributes:
        collection (Collection): The MongoDB collection instance.
    """
    
    def __init__(self, db, collection_name: str):
        """
        Initialize CRUD operations for a collection.

        Args:
            db (Database): The connected MongoDB database instance.
            collection_name (str): The name of the collection to perform operations on.
        """
        self.collection = db[collection_name]

    def create_document(self, document: dict):
        """
        Insert a new document into the collection.

        Args:
            document (dict): The document to insert.

        Returns:
            ObjectId: The ID of the inserted document.
        """
        result = self.collection.insert_one(document)
        return result.inserted_id

    def read_document(self, filter_query: dict = None):
        """
        Retrieve documents from the collection.

        Args:
            filter_query (dict, optional): Query to filter documents. Defaults to None.

        Returns:
            list: List of documents that match the query.
        """
        return list(self.collection.find(filter_query or {}))

    def update_document(self, filter_query: dict, update_data: dict):
        """
        Update an existing document in the collection.

        Args:
            filter_query (dict): Query to match the document to update.
            update_data (dict): Data to update the document with.

        Returns:
            dict: The result of the update operation.
        """
        result = self.collection.update_one(filter_query, {"$set": update_data})
        return result.raw_result

    def delete_document(self, filter_query: dict):
        """
        Delete a document from the collection.

        Args:
            filter_query (dict): Query to match the document to delete.

        Returns:
            dict: The result of the delete operation.
        """
        result = self.collection.delete_one(filter_query)
        return result.raw_result