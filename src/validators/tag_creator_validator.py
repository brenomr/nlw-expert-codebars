from cerberus import Validator
from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntity

def tag_creator_validator(request) -> None:
    tag_creator_schema = Validator({
        'product_code': {
            'type': 'string',
            'required': True,
            'empty': False,
        }
    })

    result = tag_creator_schema.validate(request.json)

    if not result:
        raise HttpUnprocessableEntity(tag_creator_schema.errors)
