



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

def main():
    books = [
        {'title':'Dune', 'author':'Frank Herbert'},
        {'title':'Hitch-Hickers Guide to the Galaxy', 'author':'Douglas Adams'},
    ]
    borrowers = [
        {'borrowerName':'Dave Smith','membershipNumber':'1246'},
        {'borrowerName':'Sarah Jones','membershipNumber':'1247'},
    ]

# Build the frame for data entry
from tkinter import *

#
# Define the event handlers
#

# create the event handler to clear the text
def evClear():
  lHistory['text'] = eBorrower.get()
  eBorrower.delete(0,END)

# create the event handler to add borrower
def evAddBorrower():
  lHistory['text'] = eBorrower.get()
  borrower = Member(eBorrower.get(),"123")
  eBorrower.delete(0,END)

# create the event handler to add borrower
def evDescribeBorrower():
    borrower.describe()

# create hotkey event handler to clear the text
def evHotKey(event):
    evClear()

#
# create the top level window/frame
#
top = Tk()
F = Frame(top)
F.pack(fill="both")

# Now the frame with text entry
fEntry = Frame(F, border=1)
eBorrower = Entry(fEntry)
eBorrower.pack(side="left")
eBorrower.bind("<Control-c>",evHotKey) # tie (bind) the CTRL-C key event to the event handler; nb: the key definition is case sensitive
lHistory = Label(fEntry, foreground="steelblue")
lHistory.pack(side="bottom", fill="x")
fEntry.pack(side="top")

# Finally the frame with the buttons. 
# We'll sink this one for emphasis
fButtons = Frame(F, relief="sunken", border=1)
bClear = Button(fButtons, text="Clear Text", command=evClear)
bClear.pack(side="left", padx=5, pady=2)
bAddBorrower = Button(fButtons, text="Add Borrower", command=evAddBorrower)
bAddBorrower.pack(side="left", padx=5, pady=2)
bDescribeBorrower = Button(fButtons, text="Describe Borrower", command=evDescribeBorrower)
bDescribeBorrower.pack(side="left", padx=5, pady=2)
bQuit = Button(fButtons, text="Quit", command=F.quit)
bQuit.pack(side="left", padx=5, pady=2)
fButtons.pack(side="top", fill="x")

# Now run the eventloop
F.mainloop()
