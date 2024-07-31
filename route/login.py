# from fastapi import FastAPI, Request, APIRouter, Depends, Form, HTTPException, Response
# from starlette.templating import Jinja2Templates
# from fastapi.staticfiles import StaticFiles
# from pymongo import MongoClient
# from typing import Any

# from fastapi.encoders import jsonable_encoder
# from bson import ObjectId

# from config.db import get_db, collection
# from auth.scurity import get_password_hash, verify_password, create_access_token, verify_token, COOKIE_NAME

# from starlette.responses import RedirectResponse

# # Repository
# from repositoryuser import UserRepository

# # Model
# from model.models import UserModel


# Router = APIRouter()

# templates = Jinja2Templates(directory="templates")

# app = FastAPI()


# @Router.post("/signupuser")
# def signup_user(
#     db: Any = Depends(get_db),
#     username: str = Form(),
#     email: str = Form(),
#     password: str = Form()
# ):
#     userRepository = UserRepository(db)
#     db_user = userRepository.get_user_by_username(username)
#     if db_user:
#         return "username is not valid"

#     signup = UserModel(email=email, username=username, password=get_password_hash(password))
#     success = userRepository.create_user(signup)
#     # token = create_access_token(signup)
#     # SendEmailVerify.sendVerify(token) # ต้องแก้ไขให้เรียกใช้วิธีส่งอีเมลที่ถูกต้อง
#     if success:
#         return "create user successfully"
#     else:
#         raise HTTPException(
#             status_code=401, detail="Credentials not correct"
#         )

# @Router.post("/signinuser")
# def signin_user(
#     response: Response,
#     db: Any = Depends(get_db),
#     username: str = Form(),
#     password: str = Form()
# ):
#     userRepository = UserRepository(db)
#     db_user = userRepository.get_user_by_username(username)
#     print(db_user)
#     if not db_user:
#         return "username or password is not valid"
    
#     db_user = UserModel(**db_user)  # Convert to UserModel object
#     if verify_password(password, db_user.password):
#         token = create_access_token(db_user)
#         response.set_cookie(
#             key=COOKIE_NAME,
#             value=token,
#             httponly=True,
#             expires=1800
#         )
#         databUser = {"username":username,"email":db_user.email}
#         # return {"data":databUser}
#         return {COOKIE_NAME: token, "token_type": "cairocoders","data":databUser}
    
    
# # @Router.get('/user/verify/{token}')
# # def verify_user(token, db: Any = Depends(get_db)):
# #     userRepository = UserRepository(db)
# #     payload = verify_token(token)
# #     username = payload.get("username")
# #     db_user = userRepository.get_user_by_username(username)

# #     if not username:
# #         raise HTTPException(
# #             status_code=401, detail="Credentials not correct"
# #         )
# #     if db_user.is_active:
# #         return "your account has already been activated"

# #     db_user.is_active = True
# #     db_user.commit()
# #     response = RedirectResponse(url="/user/signin")
# #     return response
