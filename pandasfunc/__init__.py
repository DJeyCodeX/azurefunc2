import logging
import pandas as pd
import json

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        req_body = req.get_json() 
        logging.info(req_body)
    except Exception as e:
        func.HttpResponse(str(e), status_code=400)

    try:
        if req_body['name'] == "databricksflow":
            lst = ['Java', 'Python', 'C', 'C++', 'JavaScript', 'Swift', 'Go']  
            dframe = pd.DataFrame(lst)  
            logging.info(dframe)
        return func.HttpResponse("Process Complated")
    except Exception as e:
        return func.HttpResponse(str(e), status_code=400)
