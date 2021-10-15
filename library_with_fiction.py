class Book: 
    # Note: self represents the instance of the class 
    # e.g. used to access attributes and methods of a specific book
    def __init__(self, title, author):  
        self.title = title
        self.author = author
        self.borrower = None

    def describe(self):
        print("Book Details")
        print("============")
        print("\tThe book " + self.title + " is written by " + self.author)
        if self.borrower == None:
            print("\tIt is not currently on loan")
        else:
            self.borrower
            print("\tIt is on loan to " + self.borrower.getName())

    def loanTo(self, borrower):
        if self.borrower == None:
            print("Lending " + self.title + " to " + borrower.getName() + "\n")
            self.borrower = borrower
            return True
        else:
            print("Can't lend " + self.title + " to " + borrower.getName() + " - already loaned\n")
            return False

    def returned(self, borrower):
        print(borrower.getName() + " is returning " + self.title + "\n")
        self.borrower = None

class FictionBook(Book):
    # the class FictionBook inherits the behaviour and properies of its parent class: Book
    # we add the genre functionality which (in our world at least) only applies to fictional books
    def __init__(self, title, author, genre):
        Book.__init__(self, title, author) # execute the parent constructor
        self.genre = genre # and add the genre functionality

    def describe(self):
        super().describe() # do everything in the parent describe functionality
        print("\tGenre: " + self.genre) # then add the genre

class Member: 
    def __init__(self, name, membership_id):
        self.name = name
        self.membership_id = membership_id
        self.hasOnLoan = None

    def describe(self):
        print("Library Member")
        print("==============")
        print("\tName: " + self.name)
        print("\tMembership Number: ", self.membership_id)
        if self.hasOnLoan == None:
            print("\tThey have nothing on loan")
        else:
            print("\tThey have borrowed " + self.hasOnLoan)

    def borrowBook(self, book):
        if book.loanTo(self):
            self.hasOnLoan = book.title

    def returnBook(self, book):
        if self.hasOnLoan != None and self.hasOnLoan == book.title:
            book.returned(self)
            self.hasOnLoan = None
        else:
            print(self.name + " is unable to return " + book.title + " as they do not have that book")

    def getName(self):
        return self.name

# we've finished defining our classes
# let's use them by instantiating some instances

print("\n")
print("\n")
print("-----------------------------------------------------")
print("| Creating (instantiating) some object instances...")
print("-----------------------------------------------------")

# first some books
dune = FictionBook("Dune", "Frank Herbert", "SCiFi")
dune.describe()
print("\n")
hhgttg = Book("Hitch-Hikers Guide to the Galaxy", "Douglas Adams")
hhgttg.describe()
print("\n")

# then a library member so they can borrow the book
mary = Member("Mary Smith","49573")
mary.describe()
print("\n")
tony = Member("Tony Green","49572")
tony.describe()
print("\n")

# now let's do some borrowing

print("--------------------------------")
print("| Taking a book out on loan...")
print("--------------------------------")

mary.borrowBook(dune)
dune.describe()
print("\n")
mary.describe()
print("\n")

tony.borrowBook(dune)
dune.describe()
print("\n")
tony.describe()
print("\n")

print("Check: Can tony take back a book he doesn't have?")
tony.returnBook(dune)

print("Let's see if Mary can return the book so Tony can borrow it...")
print("\n")

mary.returnBook(dune)
dune.describe()
print("\n")
mary.borrowBook(hhgttg)
mary.describe()
print("\n")
hhgttg.describe()
print("\n")

tony.borrowBook(dune)
dune.describe()
print("\n")
tony.describe()
print("\n")