print("Hello again, moon.\nLong time no see.")
class book:
    def __init__(self,title,arthor, DeweyDecimalNumber = 0, isCheckedOut = False):
        self.title = title
        self.arthor = arthor
        self.isCheckedOut = isCheckedOut
        self.DDN = DeweyDecimalNumber
    def checking(self):
        print(self.title, "by", self.arthor)
        if self.isCheckedOut == True:
            print("It is checked out")
        else:
            print("It isn't checked out")
        print("It's Dewey Decimal Number is", self.DDN)
    def checkout(self):
        if self.isCheckedOut == False:
            print("Checking out", self.title)
            self.isCheckedOut = True
        else:
            print("You can't check out a book that's already been checked out.")
    def checkin(self):
        if self.isCheckedOut == True:
            print("Checking in", self.title)
            self.isCheckedOut = False
        else:
            print("You can't check in a book that's already been checked in.")
        
        
books = [book("dews and dnts", "Dominic Gomez", 453), book("Get free wifi anywhere you go", "Kiwiquest", 694), book("Nyan Cat vs The Corruption", "MarioXHK", 23), book("HOW TO BE A [BIG SHOT]", "Spamton", 197)]
quits = {"q", "Q", "quit", "Quit"}
views = {"v", "V", "view", "View"}
checo = {"co", "Co", "CO", "checkout" "check out", "Check out", "Check Out", "Checkout", "CheckOut"}
checn = {"ci", "Ci", "CI", "checkin" "check in", "Check in", "Check In", "Checkin", "CheckIn"}
bookstore = True
print("Welcome to the bookstore")
while bookstore == True:
    checkcount = 0
    for i in range(len(books)):
        if books[i].isCheckedOut == False:
            checkcount += 1
    print("We have", checkcount, "book(s) available")
    option = input()
    if option in quits:
        print("Goodbye, come back soon!")
        bookstore == False
    if option in views:
        print("These are the books we have:")
        for i in range(len(books)):
            books[i].checking()
    if option in checo:
        print("Which book would you like to check out?")
        nnn = input()
        isexist = False
        for i in range(len(books)):
            if books[i].title == nnn:
                isexist = True
                books[i].checkout()
        if isexist == False:
            print("We don't have a book titled", nnn+ ". Maybe you didn't type it in correctly")
    if option in checn:
        print("Which book would you like to check in?")
        nnn = input()
        isexist = False
        for i in range(len(books)):
            if books[i].title == nnn:
                isexist = True
                books[i].checkin()
        if isexist == False:
            print("We don't have a book titled", nnn+ ". Maybe you didn't type it in correctly")