import json

import pytest
from starlette.status import HTTP_200_OK


@pytest.mark.parametrize(
    "test_input, expected",
    [
        #Correct Sample
        ({
            "creditCardNumber": "5388576018402626",
            "cardHolder": 1,
            "expirationDate": "2032-04-23T10:20:30.400",
            "securityCode": "123",
            "amount": "1.0"
        }, HTTP_200_OK),
        #Incorrect Credit card number
        ({
            "creditCardNumber": "7388576018402626",
            "cardHolder": 1,
            "expirationDate": "2032-04-23T10:20:30.400",
            "securityCode": "123",
            "amount": "1.0"
        }, 400),
        #Incorrect expiration date
        ({
            "creditCardNumber": "5388576018402626",
            "cardHolder": 1,
            "expirationDate": "2000-04-23T10:20:30.400",
            "securityCode": "123",
            "amount": "1.0"
        }, 400),
        #Incorrect Credit card number
        ({
            "creditCardNumber": "538857635434534018402626",
            "cardHolder": 1,
            "expirationDate": "2000-04-23T10:20:30.400",
            "securityCode": "123",
            "amount": "1.0"
        }, 400),
        #Incorrect Security number
        ({
            "creditCardNumber": "5388576018402626",
            "cardHolder": 1,
            "expirationDate": "2032-04-23T10:20:30.400",
            "securityCode": "1a3",
            "amount": "1.0"
        }, 400),
        #Incorrect Security number
        ({
            "creditCardNumber": "5388576018402626",
            "cardHolder": 1,
            "expirationDate": "2032-04-23T10:20:30.400",
            "securityCode": "1234",
            "amount": "1.0"
        }, 400),
        #Incorrect Amount number
        ({
            "creditCardNumber": "5388576018402626",
            "cardHolder": 1,
            "expirationDate": "2032-04-23T10:20:30.400",
            "securityCode": "123",
            "amount": "abc"
        }, 400),
    ],
)
def test_payment_api(client, test_input, expected):
    """A unit test for Payment request"""
    request_type = 'application/json'
    headers = {
        'Content-Type': request_type,
        'Accept': request_type
    }
    url = "/payment-gateway"

    response = client.post(url, data=json.dumps(test_input), headers=headers)
    assert response.status_code == expected
