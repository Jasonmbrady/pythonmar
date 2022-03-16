class Cart:
    def __init__(self):
        self.total = 0
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        self.total += item.price
        return self

    def remove_item(self, item_name):
        for idx in range(len(self.items)):
            if self.items[idx].name == item_name:
                self.total -= self.items[idx].price
                self.items.pop(idx)
        return self

