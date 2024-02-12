from http import HTTPStatus
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.tag_creator_controller import TagCreatorController

class TagCreatorView:
    def __init__(self):
        pass

    def validate_and_create(self, http_request: HttpRequest):
        tag_creator_controller = TagCreatorController()
        body = http_request.body
        product_code = body['product_code']
        data_to_response = tag_creator_controller.create(product_code)

        return HttpResponse(status_code=HTTPStatus.OK, body=data_to_response)
