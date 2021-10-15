import book

class ModelBasic(object):
    def __init__(self, application_items):
        self._item_type = 'product'
        self.create_books(application_items)

    @property
    def item_type(self):
        return self._item_type

    @item_type.setter
    def item_type(self, new_item_type):
        self._item_type = new_item_type

    def create_book(self, title, author, genre):
        book.create_item(title, author, genre)

    def create_books(self, items):
        book.create_items(items)

    def describe_book(self, title):
        return book.read_item(title)

    def list_books(self):
        return book.read_items()