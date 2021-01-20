from src.views.payment_process.schema import PaymentRequest
from src.views.payment_process.interface import PaymentInterface
from src.services.payment_process.factories.gateway_interface import GatewayInterface
from src.services.payment_process.factories.cheap_gateway import CheapGateway
from src.services.payment_process.factories.expensive_gateway import ExpensiveGateway
from src.services.payment_process.factories.premium_gateway import PremiumGateway


class PaymentProvider(PaymentInterface):
    """
        Interface Provider
    """

    def get_gateway_service(self, amount: float) -> GatewayInterface:

        if amount<=20:
            return CheapGateway()
        elif 21<=amount<=500:
            return ExpensiveGateway()
        else:
            return PremiumGateway()

    def process_payment(self, request: PaymentRequest):
        return self.get_gateway_service(request.amount).initiate_payment(request)