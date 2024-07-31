import uvicorn
from fastapi import FastAPI, APIRouter
import pyrebase
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

from model.models import SingUpSchema, LoginSchema

app_email = FastAPI(
    title="firebase auth",
    docs_url="/"
)

router = APIRouter()

import firebase_admin
from firebase_admin import credentials, auth

if not firebase_admin._apps:
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred)

firebaseConfig = {
  "apiKey": "AIzaSyBcT36oEBQJzpjRTOASX0S12RIKDBjsJms",
  "authDomain": "botnoi-c646c.firebaseapp.com",
  "projectId": "botnoi-c646c",
  "storageBucket": "botnoi-c646c.appspot.com",
  "messagingSenderId": "431978984390",
  "appId": "1:431978984390:web:a50411adf199cd09d2f8c7",
  "measurementId": "G-FEWF0NN1FN",
  "databaseURL": ""
}

firebase = pyrebase.initialize_app(firebaseConfig)

@router.post("/singup")
async def create_an_account(user_data:SingUpSchema):
    email = user_data.email
    password = user_data.password

    try:
        user = auth.create_user(
            email = email,
            password = password
        )

        return JSONResponse(content={"message": f"User account create successfully for user {user.uid}"},
                            status_code=201)
    except auth.EmailAlreadyExistsError:
        raise HTTPException(
            status_code=400,
            detail= f"Account already created for the email {email}"
        )