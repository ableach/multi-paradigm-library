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
            print("\tIt is not currently on loan" + "\n")
        else:
            self.borrower
            print("\tIt is on loan to " + self.borrower.name + "\n")

    def loanTo(self, borrower):
        if self.borrower == None:
            print("Lending " + self.title + " to " + borrower.name + "\n")
            self.borrower = borrower
            return True
        else:
            print("Can't lend " + self.title + " to " + borrower.name + " - already loaned\n")
            return False

    def returned(self, borrower):
        print(borrower.name + " is returning " + self.title + "\n")
        self.borrower = None

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
            print("\tThey have nothing on loan" + "\n")
        else:
            print("\tThey have borrowed " + self.hasOnLoan + "\n")

    def borrowBook(self, book):
        if book.loanTo(self):
            self.hasOnLoan = book.title

    def returnBook(self, book):
        if self.hasOnLoan != None and self.hasOnLoan == book.title:
            book.returned(self)
            self.hasOnLoan = None
        else:
            print(self.name + " is unable to return " + book.title + " as they do not have that book")

# we've finished defining our classes
# let's use them by instantiating some instances

print("\n")
print("\n")
print("-----------------------------------------------------")
print("| Creating (instantiating) some object instances...")
print("-----------------------------------------------------")

# first some books
dune = Book("Dune", "Frank Herbert")
dune.describe()
hhgttg = Book("Hitch-Hikers Guide to the Galaxy", "Douglas Adams")
hhgttg.describe()

# then a library member so they can borrow the book
mary = Member("Mary Smith","49573")
mary.describe()
tony = Member("Tony Green","49572")
tony.describe()

# now let's do some borrowing

print("--------------------------------")
print("| Taking a book out on loan...")
print("--------------------------------")

mary.borrowBook(dune)
dune.describe()
mary.describe()

tony.borrowBook(dune)
dune.describe()
tony.describe()

print("Check: Can tony take back a book he doesn't have?")
tony.returnBook(dune)

print("Let's see if Mary can return the book so Tony can borrow it...")
print("\n")

mary.returnBook(dune)
dune.describe()
mary.borrowBook(hhgttg)
mary.describe()
hhgttg.describe()

tony.borrowBook(dune)
dune.describe()
tony.describe()
