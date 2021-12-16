import logging

import azure.functions as func

from buzz import generator


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    buzzwords = generator.generate_buzz()
    return func.HttpResponse(f"Greetings from corstuur \n{buzzwords}")
