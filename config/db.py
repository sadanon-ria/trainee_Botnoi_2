from pymongo import MongoClient
from typing import Optional

from pymongo import MongoClient
db_connection = MongoClient("mongodb+srv://boat:1234@cluster0.rmsa1et.mongodb.net/")
db = db_connection.myDB
collection_account = db["account"]

collection_line = db["account_Line"]

# MongoDB connection string
# db_connection = "mongodb+srv://boat:7pgLJxeKrYkMsMob@cluster0.rmsa1et.mongodb.net/"

# client = MongoClient(db_connection)
# db = client["myDB"]
# collection = db["account"]

# DATABASE_URL: Optional[str] = None
# SECRET_KEY: Optional[str] = "cairocoders"


# def get_db():
#     client = MongoClient(db_connection)
#     db = client["myDB"]
#     try:
#         yield db
#     finally:
#         client.close()
