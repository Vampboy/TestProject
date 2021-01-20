from flask import Blueprint
from flask_pydantic import validate

from src.views.payment_process.schema import PaymentRequest, ResponseModel
from src.services.payment_process.interface_provider import PaymentProvider


payment_api = Blueprint("payment_api",__name__)

@payment_api.route("/payment-gateway", methods=["POST"])
@validate()
def start_payment(body:PaymentRequest):
    try:
        return ResponseModel(
            code=200,
            message=PaymentProvider().process_payment(body)
        ), 200
    except Exception as e:
        return ResponseModel(
            code=500,
            message = "",
            error = "Internal Server Error",
            details=str(e)
        ), 500