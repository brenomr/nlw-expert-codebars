from src.validators.tag_creator_validator import tag_creator_validator
from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntity

class Mockrequest:
    def __init__(self, json) -> None:
        self.json = json

def test_tag_creator_validator():
    request = Mockrequest(json={'product_code': '123.456.789-0'})
    tag_creator_validator(request)

    # Assert to check the return of the function
    # result = tag_creator_validator(req)
    # assert result is None

def test_tag_creator_validator_with_error():
    request = Mockrequest(json={'product_code': 12234})

    try:
        tag_creator_validator(request)
        assert False
    except Exception as ex:
        assert isinstance(ex, HttpUnprocessableEntity)
