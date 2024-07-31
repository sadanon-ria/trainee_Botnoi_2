from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from route.routes_line import user
# from route.login_email import router
# from route.login_email import app_email as app_email_router

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.mount("", app_email_router)
app.include_router(user)
