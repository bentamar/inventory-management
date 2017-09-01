from abc import ABCMeta, abstractmethod


class ItemController(object):
    """
    A base class for an item controller, which provides methods for item manipulation 
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_item(self, item_id):
        pass

    @abstractmethod
    def list_items(self, **kwargs):
        pass

    @abstractmethod
    def delete_item(self, item_id):
        pass

    @abstractmethod
    def update_item(self, item_id, metadata):
        pass
