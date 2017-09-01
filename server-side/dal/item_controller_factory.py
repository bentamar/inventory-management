from dal.excel_item_controller import ExcelItemController

ITEM_CONTROLLER_NAME_TO_CLASS = {"excel": ExcelItemController}


def get_item_controller(name, **kwargs):
    return ITEM_CONTROLLER_NAME_TO_CLASS[name](**kwargs)
