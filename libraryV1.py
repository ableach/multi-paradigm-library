class Book: 
    def __init__(self, title, author):  # self represents the instance of the class e.g. used to access attributes and methods of a specific book
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
            print("\tIt is on loan to " + self.borrower.name + "\n")

    def loanTo(self, borrower):
        print("Lending " + self.title + " to " + borrower.name + "\n")
        self.borrower = borrower

class Member: 
    def __init__(self, name, membership_id):
        self.name = name
        self.membership_id = membership_id

    def describe(self):
        print("Library Member")
        print("==============")
        print("\tName: " + self.name)
        print("\tMembership Number: ", self.membership_id)
        
    def borrowBook(self, book):
        book.loanTo(self)
        
# we've finished defining our classes
# let's use them by instantiating some instances

print("\n")
print("\n")
print("-----------------------------------------------------")
print("| Creating (instantiating) some object instances...")
print("-----------------------------------------------------")


# first a book
dune = Book("Dune", "Frank Herbert")
dune.describe()

# then a library member so they can borrow the book
mary = Member("Mary Smith","49573")
mary.describe()

# now let's do some borrowing

print("--------------------------------")
print("| Taking a book out on loan...")
print("--------------------------------")

mary.borrowBook(dune)
dune.describe()
mary.describe()

