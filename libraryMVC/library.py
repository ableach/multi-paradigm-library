import mvc_exceptions as mvc_exc

class BookStore:

    def __init__(self, bookStore):
        self.bookStore = bookStore  

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

class Model:
    def __init__(self, entity):
        self._item_type = 'Item'
        self.entity = entity

    @property
    def item_type(self):
        return self._item_type

    @item_type.setter
    def item_type(self, new_item_type):
        self._item_type = new_item_type

    def create_item(self):
        pass

    def describe_item(self):
        pass

    def list_items(self):
        return self.entity.read_items()

class BookModel(Model):
    def __init__(self, entity):
        self._item_type = 'Book'
        self.entity = entity
    
    def create_item(self, title, author, genre):
        self.entity.create_item(title, author, genre)

    def describe_item(self, title):
        return self.entity.read_item(title)

class View:

    @staticmethod
    def show_bullet_point_list(item_type, items):
        print('--- {} LIST ---'.format(item_type.upper()))
        for item in items:
            print('* {}'.format(item))

    @staticmethod
    def show_number_point_list(item_type, items):
        print('--- {} LIST ---'.format(item_type.upper()))
        for i, item in enumerate(items):
            print('{}. {}'.format(i+1, item))

    @staticmethod
    def show_item(item_type, item, item_info):
        print('//////////////////////////////////////////////////////////////')
        print('Good news, we have the item {}!'.format(item.upper()))
        print('{} INFO: {}'.format(item_type.upper(), item_info))
        print('//////////////////////////////////////////////////////////////')

    @staticmethod
    def display_missing_item_error(item, err):
        print('**************************************************************')
        print('We are sorry, we have no {}!'.format(item.upper()))
        print('{}'.format(err.args[0]))
        print('**************************************************************')

    @staticmethod
    def display_item_already_stored_error(item, item_type, err):
        print('**************************************************************')
        print('Hey! We already have {} in our {} list!'
              .format(item.upper(), item_type))
        print('{}'.format(err.args[0]))
        print('**************************************************************')

    @staticmethod
    def display_item_not_yet_stored_error(item, item_type, err):
        print('**************************************************************')
        print('We don\'t have {} in our {} list. Please insert it first!'
              .format(item.upper(), item_type))
        print('{}'.format(err.args[0]))
        print('**************************************************************')

    @staticmethod
    def display_item_stored(item, item_type):
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('Hooray! We have just added {} to our {} list!'
              .format(item.upper(), item_type))
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')     

    @staticmethod
    def display_change_item_type(older, newer):
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')
        print('Change item type from "{}" to "{}"'.format(older, newer))
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')

    @staticmethod
    def display_item_updated(item, o_price, o_quantity, n_price, n_quantity):
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')
        print('Change {} price: {} --> {}'
              .format(item, o_price, n_price))
        print('Change {} quantity: {} --> {}'
              .format(item, o_quantity, n_quantity))
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')

    @staticmethod
    def display_item_deletion(name):
        print('--------------------------------------------------------------')
        print('We have just removed {} from our list'.format(name))
        print('--------------------------------------------------------------')

class BookController:

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def show_items(self, bullet_points=False):
        items = self.model.list_items()
        item_type = self.model.item_type
        if bullet_points:
            self.view.show_bullet_point_list(item_type, items)
        else:
            self.view.show_number_point_list(item_type, items)

    def show_item(self, item_name):
        try:
            item = self.model.describe_item(item_name)
            item_type = self.model.item_type
            self.view.show_item(item_type, item_name, item)
        except mvc_exc.ItemNotStored as e:
            self.view.display_missing_item_error(item_name, e)

    def insert_item(self, title, author, genre):
        item_type = self.model.item_type
        try:
            self.model.create_item(title, author, genre)
            self.view.display_item_stored(title, item_type)
        except mvc_exc.ItemAlreadyStored as e:
            self.view.display_item_already_stored_error(title, item_type, e)


books = [
    {'title':'Dune', 'author':'Frank Herbert', 'genre': 'Sci-Fi'},
    {'title':'Hitch-Hickers Guide to the Galaxy', 'author':'Douglas Adams'},
]

bookStore = BookStore(books)
c = BookController(BookModel(bookStore), View())

# Build the frame for data entry
from tkinter import *

#
# Define the event handlers
#

# create the event handler to clear the text
def evClearFields():
  eTitle.delete(0,END)
  eAuthor.delete(0,END)
  eGenre.delete(0,END)

# create the event handler to add book
def evAddBook():
  c.insert_item(eTitle.get(),eAuthor.get(),eGenre.get())
  evClearFields()

# create the event handler to describe book
def evDescribeBook():
    c.show_item(eTitle.get())

# create the event handler to list books
def evListBooks():
    c.show_items()

# create hotkey event handler to clear the text
def evHotKey(event):
    evClearFields()

#
# create the top level window/frame
#
top = Tk()
F = Frame(top)
F.pack(fill="both")

# Now the frame with title entry
fTitle = Frame(F, border=1)
lTitle = Label(fTitle,text='Title',padx=10, justify = LEFT)
lTitle.grid(row = 0, column = 0, pady=5, sticky='w')
eTitle = Entry(fTitle)
eTitle.grid(row = 0, column = 4, pady=5)
eTitle.bind("<Control-c>",evHotKey) # tie (bind) the CTRL-C key event to the event handler; nb: the key definition is case sensitive
fTitle.pack(side="top")

# Now the frame with author entry
fAuthor = Frame(F, border=1)
lAuthor = Label(fAuthor,text='Author',padx=10, justify = LEFT)
lAuthor.grid(row = 1, column = 0, pady=5, sticky='w')
eAuthor = Entry(fAuthor)
eAuthor.grid(row = 1, column = 4, pady=5)
eAuthor.bind("<Control-c>",evHotKey) # tie (bind) the CTRL-C key event to the event handler; nb: the key definition is case sensitive
fAuthor.pack(side="top")

# Now the frame with genre entry
fGenre = Frame(F, border=1)
lGenre = Label(fGenre,text='Genre',padx=10, justify = LEFT)
lGenre.grid(row = 2, column = 0, pady=5, sticky='w')
eGenre = Entry(fGenre)
eGenre.grid(row = 2, column = 4, pady=5)
eGenre.bind("<Control-c>",evHotKey) # tie (bind) the CTRL-C key event to the event handler; nb: the key definition is case sensitive
fGenre.pack(side="top")

# Finally the frame with the buttons. 
# We'll sink this one for emphasis
fButtons = Frame(F, relief="sunken", border=1)
bClear = Button(fButtons, text="Clear Fields", command=evClearFields)
bClear.pack(side="left", padx=5, pady=2)
bAddBook = Button(fButtons, text="Add Book", command=evAddBook)
bAddBook.pack(side="left", padx=5, pady=2)
bDescribeBook = Button(fButtons, text="Describe Book", command=evDescribeBook)
bDescribeBook.pack(side="left", padx=5, pady=2)
bListBooks = Button(fButtons, text="List Books", command=evListBooks)
bListBooks.pack(side="left", padx=5, pady=2)
bQuit = Button(fButtons, text="Quit", command=F.quit)
bQuit.pack(side="left", padx=5, pady=2)
fButtons.pack(side="top", fill="x")

# Now run the eventloop
F.mainloop()
