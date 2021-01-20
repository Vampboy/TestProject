from src.views.payment_process.schema import PaymentRequest
from src.common.singleton import Singleton

class GatewayInterface(metaclass=Singleton):

    def payment_response(self, request: PaymentRequest):
        raise NotImplementedError


    def retry_process(self, request: PaymentRequest):
        raise NotImplementedError

    def initiate_payment(self, request:PaymentRequest):
        raise NotImplementedError