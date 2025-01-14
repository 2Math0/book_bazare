# main.py

from mongodb.connection import MongoDBConnection
from mongodb.crud import MongoDBCRUD

# Configuration
MONGO_URI = "mongodb://localhost:27017/"
DATABASE_NAME = "example_db"
COLLECTION_NAME = "example_collection"

def main():
    # Initialize connection
    mongo_connection = MongoDBConnection(MONGO_URI, DATABASE_NAME)
    try:
        mongo_connection.connect()
        db = mongo_connection.db

        # Initialize CRUD operations
        crud = MongoDBCRUD(db, COLLECTION_NAME)

        # Example CRUD operations
        # Create
        new_document = {"name": "BookBazaar", "type": "Library Management"}
        doc_id = crud.create_document(new_document)
        print(f"Document inserted with ID: {doc_id}")

        # Read
        documents = crud.read_document()
        print("Documents:", documents)

        # Update
        update_result = crud.update_document({"name": "BookBazaar"}, {"type": "Management System"})
        print("Update Result:", update_result)

        # Delete
        delete_result = crud.delete_document({"name": "BookBazaar"})
        print("Delete Result:", delete_result)

    finally:
        mongo_connection.close()

if __name__ == "__main__":
    main()