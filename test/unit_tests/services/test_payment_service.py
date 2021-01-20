import json

import pytest

from src.views.payment_process.schema import PaymentRequest
from src.services.payment_process.factories.cheap_gateway import CheapGateway
from src.services.payment_process.factories.expensive_gateway import ExpensiveGateway
from src.services.payment_process.factories.premium_gateway import PremiumGateway
from src.services.payment_process.interface_provider import PaymentProvider

@pytest.mark.parametrize(
    "test_input, expected",
    [
        #Cheap Transaction
        ({
            "creditCardNumber": "5388576018402626",
            "cardHolder": 1,
            "expirationDate": "2032-04-23T10:20:30.400",
            "securityCode": "123",
            "amount": "10"
        }, CheapGateway()),
        #expensive Transaction
        ({
            "creditCardNumber": "5388576018402626",
            "cardHolder": 1,
            "expirationDate": "2032-04-23T10:20:30.400",
            "securityCode": "123",
            "amount": "250"
        }, ExpensiveGateway()),
        #premium Transaction
        ({
            "creditCardNumber": "5388576018402626",
            "cardHolder": 1,
            "expirationDate": "2032-04-23T10:20:30.400",
            "securityCode": "123",
            "amount": "1000"
        }, PremiumGateway())
    ],
)
def test_gateway_api(test_input, expected):
    """A unit test for Payment gateway selection"""
    print(PaymentRequest(**test_input).amount)
    response = PaymentProvider().get_gateway_service(PaymentRequest(**test_input).amount)
    assert response == expected
