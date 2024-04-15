import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")

#Create or select a DB
mydb = client["lexicondb"]

books_collection = mydb["Book_Store"]

def add_Book():
    title = input("Enter book title: ")
    book_isavail = books_collection.find_one({"title": title})
    if not book_isavail:
        author = input("Enter author: ")
        price = float(input("Enter price: "))
        stock = int(input("Enter stock quantity: "))
        book = {"title": title, "author": author, "price": price, "stock": stock}
        books_collection.insert_one(book)
        print("Book added successfully!!")
    else:
        print(f"{title} is already available in book store, choose update option")

def view_Books():
    print("Book store collection: ")
    for book in books_collection.find():
        print(book)

def search_Book():
    title = input("Enter the title of the book to search: ")
    regex_pattern = {'$regex': title, '$options': 'i'}
    book_isavail = books_collection.find_one({"title": regex_pattern})
    if book_isavail:
        for book in books_collection.find({"title": regex_pattern}):
            print(book)
    else:
        print("No book found with that title.")
   

def update_Book_Price():
    book_title = input("Enter book title to update price: ")
    book_isavail = books_collection.find_one({"title": book_title})
    if book_isavail:
        new_price = float(input("Enter new price: "))
        myquery = { "title": book_title }
        newvalues = { "$set": { "price": new_price } }
        books_collection.update_one(myquery, newvalues)
        print(f"Price updated successfully for {book_title}!")
    else:
        print("No book found with that title.")


def delete_Book():
    del_book = input("Enter a book title to delete: ")
    book_isavail = books_collection.find_one({"title": del_book})
    if book_isavail:
        deleteQuery = { "title": del_book }
        books_collection.delete_one(deleteQuery)
        print(f"{del_book} is deleted!")
    else:
        print("No book found with that title.")


def sortBy_Author():
    author = input("Enter author's name: ")
    book_isavail = books_collection.find_one({"author": author})
    if book_isavail:
        for book in books_collection.find({"title": author}):
            print(book)
    else:
        print("No book found with that author.")


def booksIn_Stock():
    for book in books_collection.find({"stock": {"$gt": 0}}):
        print(book)


def main_menu():
    while True:
        print("\n--- Hello and welcome to the awesome Lexicon bookstore! ---")
        print("1. Add a book")
        print("2. View all books")
        print("3. Search a book by title")
        print("4. Update a book price")
        print("5. Delete a book")
        print("6. View books by author")
        print("7. View books in Stock")
        print("9. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            add_Book()
        elif choice == '2':
            view_Books()
        elif choice == '3':
            search_Book()
        elif choice == '4':
            update_Book_Price()
        elif choice == '5':
            delete_Book()
        elif choice == '6':
            sortBy_Author()
        elif choice == '7':
            booksIn_Stock()
        elif choice == '8':
            print("Goodbye!! See you again :)")
            break
        else:
            print("Invalid option, please choose again.")

if __name__ == "__main__":
    main_menu()
