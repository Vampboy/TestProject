from src.views.payment_process.schema import PaymentRequest
from src.common.singleton import Singleton

class PaymentInterface(metaclass=Singleton):

    def get_gateway(self, request:PaymentRequest):
        raise NotImplementedError
