from fastapi.responses import JSONResponse
from fastapi import Request

class PincodeNotFoundError(Exception):
    def __init__(self,pincode:str):
        self.pincode=pincode

class InvalidPincodeError(Exception):
    def __init__(self,pincode:str,reason:str="Invalid Format"):
        self.pincode=pincode
        self.reason=reason



#custom handlers
async def pincode_not_found_handler(request: Request, exc:PincodeNotFoundError):
    return JSONResponse(
        status_code=404,
        content={
            "error":"Pincode not found",
            "message":f"No location for pincode:{exc.pincode}",
            "Pincode":exc.pincode
        }
    ) 
async def invalid_pincode_not_found_handler(request: Request, exc:PincodeNotFoundError):
    return JSONResponse(
        status_code=400,
        content={
            "error":"Invalid pincode",
            "message":f"Pincode '{exc.pincode}'is invalid:{exc.reason}",
            "Pincode":exc.pincode
        }
    ) 

       
            