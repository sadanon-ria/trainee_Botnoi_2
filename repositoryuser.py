from pymongo.collection import Collection
from model.models import UserModel
from typing import Dict, Any


class UserRepository:
    def __init__(self, db: Collection):
        self.collection: Collection = db["account"]

    def create_user(self, signup: UserModel) -> bool:
        try:
            user_data = signup.to_mongo().to_dict()
            self.collection.insert_one(user_data)
            return True
        except:
            return False

    def get_user(self):
        return self.collection.find()

    def get_user_by_username(self, username: str) -> UserModel:
        return self.collection.find_one({"username": username},{"_id":False,"email":True,"username":True,"password":True})
    

    def update_user(self, id: int, details: Dict[str, Any]) -> bool:
        try:
            self.collection.update_one({"id": id}, {"$set": details})
            return True
        except:
            return False

    def delete_user(self, id: int) -> bool:
        try:
            self.collection.delete_one({"id": id})
            return True
        except:
            return False
