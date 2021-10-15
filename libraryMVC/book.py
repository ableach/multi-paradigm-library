import mvc_exceptions as mvc_exc

def book():

    def __init__(self):
        self.bookStore = list()  

    def create_items(self, app_items):
        self.bookStore = app_items

    def create_item(self, title, author, genre):
        results = list(filter(lambda x: x['title'] == title, self.bookStore))
        if results:
            raise mvc_exc.ItemAlreadyStored('"{}" already stored!'.format(title))
        else:
            self.bookStore.append({'title': title, 'author': author, 'genre': genre})

    def read_item(self, title):
        self.myitems = list(filter(lambda x: x['title'] == title, self.bookStore))
        if self.myitems:
            return self.myitems[0]
        else:
            raise mvc_exc.ItemNotStored(
                'Item "{}" does not exist'.format(title))

    def read_items(self):
        return [item for item in self.bookStore]