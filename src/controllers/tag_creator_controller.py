from typing import Dict
from src.external.barcode_handler import BarcodeHandler

class TagCreatorController:

    def create(self, product_code: str) -> Dict:
        path_from_tag = self.__create_tag(product_code)
        data_to_response = self.format_response(path_from_tag)
        return data_to_response

    def __create_tag(self, product_code: str) -> str:
        barcode_handler = BarcodeHandler()

        path_from_tag = barcode_handler.create_barcode(product_code)

        return path_from_tag

    def format_response(self, path_from_tag: str) -> Dict:
        return {
            'data' : {
                'type': 'Tag Image',
                'count': 1,
                'path': f'{path_from_tag}.png'
            }
        }
