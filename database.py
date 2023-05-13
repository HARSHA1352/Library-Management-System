class Database:
    def __init__(self):
        self.ManagerData = set([("akhil", "akhil")])
        self.CustomerData = set([])
        self.Books = set()

    def _isvalid(self, user, passcode, type):
        # print(self.data)
        if type == 1:
            return (user, passcode) in self.ManagerData
        elif type == 2:
            return (user, passcode) in self.CustomerData

    def _AddNewBook(self):
        title = input("Enter title of book : ")
        author = input("Enter author of book : ")
        price = input("Enter price of book : ")
        self.Books.add((title, author, price))
        print("Book added **\n")

    def _isAvailable(self, title, author, price):
        return ((title, author, price)) in self.Books

    def _viewSpecificBook(self):
        title = input("Enter title of book : ")
        for i, j, k in self.Books:
            if i == title:
                print("Title: ", title)
                print("Author: ", j)
                print("Price : ", k)
                return
        print("Book isn't Available")

    def _viewAllBooks(self):
        print("*** Available Books *** \n")
        for i, j, k in self.Books:
            print("Title: ", i)
            print("Author: ", j)
            print("------------------")

    def _RemoveBooks(self):
        print("Enter Boooks Details")
        title = input("Enter title of book : ")
        author = input("Enter author of book : ")
        price = input("Enter price of book : ")
        if Database._isAvailable(self, title, author, price):
            self.Books.remove((title, author, price))
            print("Book Removed")
        else:
            print("Book dosen't Exist")

    def _UpdateBookDetails(self):
        print("Enter ** OLD ** Boooks Details")
        Database._RemoveBooks(self)
        print("Enter ** NEW ** Boooks Details")
        Database._AddNewBook(self)

    def _GenerateInvoice():
        pass

    def _RentBook():
        pass

    def _payBill():
        pass

    def _AcceptPayment():
        pass
