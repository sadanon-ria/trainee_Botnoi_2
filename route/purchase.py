import stripe
from fastapi import FastAPI, Request
import json
from starlette.middleware.sessions import SessionMiddleware
from fastapi.responses import RedirectResponse

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="dVu9jfC1PPVGRkq-X5nKaP_vDHC63CxQ2K4W0QVpFJo")

stripe.api_key = "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"

@app.post("/create-checkout-session")
async def create_checkout_session(request: Request):
    data = await request.json()

    google_id = request.session.get("google_id")
    # if google_id is None:
    #     # สร้างการตอบกลับว่าไม่ได้เข้าสู่ระบบหรือข้อผิดพลาดอื่น ๆ
    #     return {"error": "User is not logged in"}
    
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        mode="subscription",
        line_items=[{
            "price": data["priceId"],
            "quantity": 1
        }],
        client_reference_id=google_id,
        success_url='http://127.0.0.1:8000/success',
        cancel_url='http://127.0.0.1:8000/cancel',
    )
    # return RedirectResponse(checkout_session["url"])
    return {"sessionId": checkout_session["id"], 'message': checkout_session["url"]}

# @payment_app.post("/create_stripe_test", tags=["payments_service"])
# #def check_qrcode(user_id: str = Depends(oauth2_utils.require_user)):
# async def create_stripe_test(request : Request):
#     try:
#         payload = await request.body()
#         my_json = payload.decode('utf8').replace("'", '"')
#         data = json.loads(my_json)
#         stripe.api_key = ENV.STRIPE_KEY

#         #รับจาก body price คือ จำนวนที่ลูกค้าใส่เงินมา
#         price = data["price"]
#         user_id = data["user_id"]
#         name = "pack"+str(price)
#         unit_price = price * 100
#         print(ENV.STRIPE_REDIRECT)
#         a=stripe.checkout.Session.create(
#             payment_method_types=['card'],

#             # or you can take multiple payment methods with
#             # payment_method_types=['card', 'promptpay', ...]
#             line_items=[{
#                 'price_data': {
#                 'currency': 'thb',
#                 'product_data': {
#                     'name': name,
#                 },
#                 'unit_amount': unit_price,

#                 },

#                 'quantity': 1,
#             }],
#             mode='payment',
#             client_reference_id=user_id,
#             success_url=ENV.STRIPE_REDIRECT,
#             #after_completion={"type": "redirect", "redirect": {"url": ENV.STRIPE_REDIRECT}},
#             cancel_url='https://example.com/cancel',
#         )
#         return {"status" : 200 ,'message': a["url"]}
#     except Exception as e:
#         message = {"message" : str(e), "TypeError:" : type(e).name,"file_name" : file,  "line" : e.traceback.tb_lineno}
#         print("payment_check_qrcode error", message)

#         raise HTTPException(status_code=401, detail="Could not validate credentials", headers={"WWW-Authenticate": "Bearer"},)