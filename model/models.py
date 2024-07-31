from pydantic import BaseModel
# class Roles(Enum):
#     # กำหนดสิทธิ์ที่คุณต้องการให้มีใน MongoDB
#     USER = "user"
#     ADMIN = "admin"


class User(BaseModel):
    userId: str
    displayName: str

class SingUpSchema(BaseModel):
    email: str
    password: str

    class Config:
        json_schema_extra ={
            "example":{
                "email": "sadanon@gmail.com",
                "password": "123456789"
            }
        }

class LoginSchema(BaseModel):
    email: str
    password: str

    class Config:
        json_schema_extra ={
            "example":{
                "email": "sadanon@gmail.com",
                "password": "123456789"
            }
        }
        
# class UserModel(Document):
#     meta = {"collection": "account"}
    
#     _id = StringField(required=True)
#     id = StringField()
#     email = StringField()
#     username = StringField()
#     password = StringField()
#     is_active = BooleanField()



    # id = StringField(primary_key=True)
    # email = StringField(unique=True)
    # username = StringField(unique=True)
    # password = StringField(unique=False)
    # is_active = BooleanField(default=False)
    # role = EnumField(Roles, default=Roles.USER)
