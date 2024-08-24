# Library dictionary structure: 
# {
#   'Title1': {'author': 'Author1', 'genre': 'Genre1', 'copies': 5},
#   'Title2': {'author': 'Author2', 'genre': 'Genre2', 'copies': 3},
#   ...
# }

library = {}

# Function to add a new book
def add_book(title, author, genre, copies):
    if title in library:
        print(f"The book '{title}' is already in the library.")
    else:
        library[title] = {'author': author, 'genre': genre, 'copies': copies}
        print(f"Book '{title}' added to the library.")

# Function to update the number of copies
def update_copies(title, copies):
    if title in library:
        library[title]['copies'] = copies
        print(f"Updated the number of copies for '{title}' to {copies}.")
    else:
        print(f"The book '{title}' is not in the library.")

# Function to list books by a specific author or genre
def list_books_by(criteria, value):
    print(f"Books by {criteria} '{value}':")
    for title, details in library.items():
        if details[criteria] == value:
            print(f" - {title} ({details['copies']} copies available)")

# Function to borrow a book
def borrow_book(title):
    if title in library and library[title]['copies'] > 0:
        library[title]['copies'] -= 1
        print(f"You borrowed '{title}'. {library[title]['copies']} copies left.")
    elif title in library:
        print(f"Sorry, '{title}' is out of stock.")
    else:
        print(f"The book '{title}' is not available in the library.")

# Function to return a book
def return_book(title):
    if title in library:
        library[title]['copies'] += 1
        print(f"You returned '{title}'. {library[title]['copies']} copies now available.")
    else:
        print(f"The book '{title}' does not belong to our library.")

# Function to list all books in the library
def list_all_books():
    print("Books available in the library:")
    for title, details in library.items():
        print(f" - {title} by {details['author']} ({details['copies']} copies, Genre: {details['genre']})")

# Testing the program
add_book("The Hobbit", "J.R.R. Tolkien", "Fantasy", 5)
add_book("1984", "George Orwell", "Dystopian", 3)
add_book("To Kill a Mockingbird", "Harper Lee", "Classic", 4)

list_all_books()

borrow_book("1984")
borrow_book("1984")
borrow_book("1984")
borrow_book("1984")  # Should indicate it's out of stock

return_book("1984")
list_books_by("author", "George Orwell")
list_books_by("genre", "Fantasy")

update_copies("The Hobbit", 10)
list_all_books()
