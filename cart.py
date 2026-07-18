# cart.py

class ShoppingCart:
    def __init__(self):
        self.items = []

    def remove_item(self, item_name):
        # Bug: mutating list while iterating over it
        for item in self.items:
            if item == item_name:
                self.items.remove(item)

    def get_item(self, index):
        # Bug: no bounds check
        return self.items[index]


def load_cart_file(filename):
    # Bug: file never closed, no error handling
    file = open(filename, "r")
    data = file.read()
    return data