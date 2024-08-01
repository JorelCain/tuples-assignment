# Python Data Structure Challenge

# Library System Enhancement: You are maintaining a library system where each book is stored as a tuple within a list. Your task is to update this system by adding new books and ensuring no duplicates.

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def add_book(library, new_book):
    if new_book in library:
        print(f"The book '{new_book[0]}' by {new_book[1]} is already in the library.")
    else:
        library.append(new_book)
        print(f"The book '{new_book[0]}' by {new_book[1]} has been added to the library.")

new_book = ("War and Peace", "Leo Tolstoy")
new_book_2 = ("1984", "George Orwell")

add_book(library, new_book)
add_book(library, new_book_2)

print(library)