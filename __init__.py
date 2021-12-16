# import os
# from flask import Flask
# from buzz import generator

# app = Flask(__name__)

# @app.route("/")
# def generate_buzz():
#     page = '<html><body><h1>'
#     page += generator.generate_buzz()
#     page += '</h1></body></html>'
#     return page

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))


import logging
import azure.functions as func
from buzz import generator


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    return func.HttpResponse(generator.generate_buzz)
    # name = req.params.get('name')
    # if not name:
    #     try:
    #         req_body = req.get_json()
    #     except ValueError:
    #         pass
    #     else:
    #         name = req_body.get('name')

    # if name:
    #     return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    # else:
    #     return func.HttpResponse(
    #          "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
    #          status_code=200
    #     )