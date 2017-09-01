from openpyxl import Workbook
from filelock import FileLock

import config
from dal.item_controller import ItemController


def lock_file(func):
    def wrapped_method(excel_item_controller_instance, *args, **kwargs):
        lock = excel_item_controller_instance
    return wrapped_method

class ExcelItemController(ItemController):
    def __init__(self, excel_file_name=config.EXCEL_FILE_PATH):
        self._workbook = Workbook()
        self._file_name = excel_file_name

    @property
    def file_name(self):
        return self._file_name

    def list_items(self, **kwargs):
        pass

    def get_item(self, item_id):
        pass

    def update_item(self, item_id, metadata):
        pass

    def delete_item(self, item_id):
        pass
