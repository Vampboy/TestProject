from src.views.payment_process.schema import PaymentRequest
from src.services.payment_process.factories.gateway_interface import GatewayInterface

class PremiumGateway(GatewayInterface):
    """
        Interface Provider
    """

    def payment_response(self, request: PaymentRequest):
        return "Sucess"

    def retry_process(self, request: PaymentRequest, retry_count=3):
        while(retry_count):
            retry_count-=1
            response = self.payment_response(request)
            if response=="Sucess":
                return response
        return response
        

    def initiate_payment(self, request: PaymentRequest):
        print("Done Premiume payment")
        response = self.payment_response(request)
        if response!="Sucess":
            return self.retry_process(request)
        return response