from http import HTTPStatus
from src.views.http_types.http_response import HttpResponse
from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntity

def errors_handler(error: Exception) -> HttpResponse:

    if isinstance(error, HttpUnprocessableEntity):
        return HttpResponse(
            status_code=error.status_code,
            body={
                'errors': [{
                    'title': error.name,
                    'detail': error.message
                }]
            }
        )

    return HttpResponse(
        status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
        body={
            'errors': [{
                'title': 'Internal Server Error',
                'detail': str(error)
            }]}
    )
