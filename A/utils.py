from kavenegar import *

def send_otp_code(phone_number, code):
    try:
        api = KavenegarAPI('326C314553496A4C6E6E55505A6B6D4D51446C586B4969305067512F6642363479533273365644646C32773D')
        params = {
            'sender': '',  # optional
            'receptor': phone_number,  # multiple mobile number, split by comma
            'message' : f'کد تایید{code}'
            }
        response = api.verify_lookup(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)

