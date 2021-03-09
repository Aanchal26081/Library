class Library:
    def __init__(self,listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books present in this library are: ")
        for book in self.books:
            print("\t" + book)

    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please keep it safe and return it within 30 days.")
            self.books.remove(bookName)
            return True

        else:
            print("Sorry, This book has already been issued to someone else. Please wait until the book is returned")
            return False

    def returnBook(self,bookName):
        self.books.append(bookName)
        print("Thanks for returning this book!")


class Student:
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book
        
    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book


if __name__ == "__main__":
    centralLibrary = Library(["Algorithm","Danjo","Python","C++","C","DSA"])
    student = Student()
    centralLibrary.displayAvailableBooks()
    while(True):
        WelcomeMsg = '''Welcome to the Central library
        Please choose an option:
        1. Listing all the book
        2. Request a book
        3. Return a book
        4. Exit the library
        '''
        print(WelcomeMsg)
        a = int(input("Enter a choice: "))
        if a == 1:
            centralLibrary.displayAvailableBooks()
        elif a == 2:
            centralLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centralLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for using central library! Have a great day ahead")
            exit()
        else:
            print("Invalid Choice!")
