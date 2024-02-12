from http import HTTPStatus
from src.views.http_types.http_response import HttpResponse

def errors_handler(error: Exception) -> HttpResponse:
    return HttpResponse(
        status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
        body={
            'errors': [{
                'title': 'Internal Server Error',
                'detail': str(error)
            }]}
    )
