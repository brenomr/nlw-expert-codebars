from unittest.mock import patch
from src.controllers.tag_creator_controller import TagCreatorController
from src.external.barcode_handler import BarcodeHandler

@patch.object(BarcodeHandler, 'create_barcode')
def test_create(mock_create_barcode):
    mocked_value = 'image_path'
    mock_create_barcode.return_value = mocked_value
    tag_creator_controller = TagCreatorController()

    result = tag_creator_controller.create(mocked_value)

    assert isinstance(result, dict)
    assert 'data' in result
    assert 'type' in result['data']
    assert 'count' in result['data']
    assert 'path' in result['data']

    assert result['data']['type'] == 'Tag Image'
    assert result['data']['count'] == 1
    assert result['data']['path'] == f'{mocked_value}.png'
