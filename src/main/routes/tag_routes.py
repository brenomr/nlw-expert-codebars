from flask import Blueprint, request, jsonify
from src.views.http_types.http_request import HttpRequest
from src.views.tag_creator_view import TagCreatorView
from src.errors.errors_handler import errors_handler
from src.validators.tag_creator_validator import tag_creator_validator

tag_routes_bp = Blueprint('tag_routes', __name__)

@tag_routes_bp.route('/create_tag', methods=['POST'])
def create_tag():
    response = None

    try:
        tag_creator_validator(request)

        tag_creator_view = TagCreatorView()

        http_request = HttpRequest(body=request.json,)

        response = tag_creator_view.validate_and_create(http_request=http_request)

    except Exception as error:
        response = errors_handler(error)

    return jsonify(response.body), response.status_code
