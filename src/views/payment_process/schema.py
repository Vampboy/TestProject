
from pydantic import BaseModel, validator
from datetime import datetime, timedelta
from typing import Optional



class PaymentRequest(BaseModel):
    
    creditCardNumber : str
    cardHolder: str
    expirationDate: datetime
    securityCode: Optional[str]
    amount: float

    @validator('creditCardNumber')
    def creditCardNumber_validation(cls, value):
        print(13<=len(value)<=16 and ((int(value[0]) in [4,5,6]) or int(value[:1])==37))
        if (13<=len(value)<=16) and ((int(value[0]) in [4,5,6]) or int(value[:1])==37):
            return value
        else:
            raise ValueError('Not a Valid Credit Card number: ')
    
    @validator('expirationDate')
    def expirationDate_validation(cls, value):
        past = datetime.now() - timedelta(days=1)
        if value > past:
            return value
        else:
            raise ValueError('DateTime should not be past: ')

    @validator('securityCode')
    def securityCode_validation(cls, value):
        if value is not None:
            if len(value)==3 and value.isdigit():
                return value
            else:
                raise ValueError('SecurityCode should be 3 digit: ')
        return value
    
    @validator('amount')
    def amount_validation(cls, value):
        if value>0:
            return value
        else:
            raise ValueError('Amount should be always Positive: ')  

    
class ResponseModel(BaseModel):
    code : int
    message : Optional[str] = None
    error : Optional[str] = None
    details : Optional[str] = None