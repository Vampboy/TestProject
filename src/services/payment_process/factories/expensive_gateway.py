from src.views.payment_process.schema import PaymentRequest
from src.services.payment_process.factories.gateway_interface import GatewayInterface
from src.services.payment_process.factories.cheap_gateway import CheapGateway

class ExpensiveGateway(GatewayInterface):
    """
        Interface Provider
    """

    def payment_response(self, request: PaymentRequest):
        return "Sucess"

    def retry_process(self, request: PaymentRequest):
        return CheapGateway().initiate_payment(request)

    def initiate_payment(self, request: PaymentRequest):
        print("Done Expensive payment")
        response = self.payment_response(request)
        if response!="Sucess":
            return self.retry_process(request)
        return response