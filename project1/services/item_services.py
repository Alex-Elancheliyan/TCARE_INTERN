from typing import List
from project1.models.item import Item
from project1.schemas.item_schema import ItemCreate, ItemUpdate

class ItemService:
    def __init__(self):
        self.items = []

    def get_all_items(self) -> List[Item]:
        return self.items

    def get_item_by_id(self, item_id: int) -> Item:
        for item in self.items:
            if item.id == item_id:
                return item
        return None

    def create_item(self, item_data: ItemCreate) -> Item:
        new_item = Item(**item_data.dict(), id=len(self.items) + 1)
        self.items.append(new_item)
        return new_item

    def update_item(self, item_id: int, item_data: ItemUpdate) -> Item:
        item = self.get_item_by_id(item_id)
        if item:
            item.name = item_data.name
            item.description = item_data.description
            return item
        return None

    def delete_item(self, item_id: int) -> bool:
        item = self.get_item_by_id(item_id)
        if item:
            self.items.remove(item)
            return True
        return False
