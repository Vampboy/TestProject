from src.views.payment_process.schema import PaymentRequest
from src.services.payment_process.factories.gateway_interface import GatewayInterface

class CheapGateway(GatewayInterface):
    """
        Interface Provider
    """

    def payment_response(self, request: PaymentRequest):
        return "Sucess"

    def retry_process(self, request: PaymentRequest):
        raise NotImplementedError   

    def initiate_payment(self, request: PaymentRequest):
        response = self.payment_response(request)
        return response