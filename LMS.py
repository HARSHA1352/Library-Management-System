from collections import defaultdict

from database import Database


db = Database()


class LibraryManagementSystem:
    def __init__(self, username, password, type):
        self.username = username
        self.password = password
        self.type = type
        if LibraryManagementSystem._authenticate(self):
            if type == 1:
                print("Logged in successfully as MANAGER ****\n")
            elif type == 2:
                print("Logged in successfully as CUSTOMER ****\n")
        else:
            print("Login Failed try again ****\n")
            return
        # print("hii")
        while(1):
            print(" 1. view Menu")
            print(" 2. Logout")
            dd = int(input("=>"))
            if dd == 1:
                LibraryManagementSystem._printMenu(self)
            elif dd == 2:
                return
            else:
                print("Invalid Option")

    def _authenticate(self):
        return db._isvalid(self.username, self.password, self.type)

    def _printMenu(self):
        if type == 1:
            print("Manager Menu\n")
            print(" 1. Add New Book")
            print(" 2. Update Book Details")
            print(" 3. Remove Book")
            print(" 4. View All Books")
            print(" 5. View Specific Book")
            print(" 6. Accept Payment")
            print(" 7. Generate Invoice")
            print(" 8. Exit")
            option = int(input("=> "))

            if option == 8:
                print("Menu Exitted")
                return

            if option > 7 or option < 1:
                print("Invalid Option \n")
                return

            if option == 1:
                db._AddNewBook()
            elif option == 2:
                db._UpdateBookDetails()
            elif option == 3:
                db._RemoveBooks()
            elif option == 4:
                db._viewAllBooks()
            elif option == 5:
                db._viewSpecificBook()
            elif option == 6:
                db._AcceptPayment()
            elif option == 7:
                db._GenerateInvoice()

        elif type == 2:
            print("Customer Menu\n")
            print(" 1. View All Books")
            print(" 2. View Specific Book")
            print(" 3. Rent a Book")
            print(" 4. Paybill")
            option = int(input("=> "))

            if option == 1:
                db._viewAllBooks()
            elif option == 2:
                db._viewSpecificBook()
            elif option == 3:
                db._RentBook()
            elif option == 4:
                db._payBill()
            else:
                print("Invalid Option")


while(1):
    LoginType = int(input(" 1. Login \n 2. SignUp \n 3.Exit \n =>"))

    if LoginType == 1:
        type = int(
            input("Select Login Type *** 1 for 'Manager' | 2 for 'Customer': "))
        if type not in (1, 2):
            print("Selected invalid option\n")
        else:
            username = str(input("Enter User Name : "))
            password = str(input("Enter Password : "))
            obj = LibraryManagementSystem(username, password, type)

    elif LoginType == 2:
        print("SignUp *** \n")
    else:
        if(LoginType not in (1, 2, 3)):
            print("Invalid Option")
        print(".....Exited")
        break
