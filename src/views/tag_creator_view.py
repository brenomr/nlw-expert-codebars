from http import HTTPStatus
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class TagCreatorView:
    def __init__(self):
        pass

    def validate_and_create(self, http_request: HttpRequest):
        body = http_request.body
        product_code = body['product_code']
        product_code = product_code + '' # simple test, silence linter on pre-commit
        print(product_code)

        return HttpResponse(status_code=HTTPStatus.OK, body={'message': 'simples test response.'})
