# Dictionary to store books
catalog = {}

# List to store borrowed books
borrowed_books = []

# Set to store members
members = set()


# Add Book
def add_book(book_id, title, author, year):
    catalog[book_id] = (title, author, year)


# Borrow Book
def borrow_book(book_id):
    if book_id in catalog and book_id not in borrowed_books:
        borrowed_books.append(book_id)
        print("Book Borrowed")
    else:
        print("Book Not Available")


# Return Book
def return_book(book_id):
    if book_id in borrowed_books:
        borrowed_books.remove(book_id)
        print("Book Returned")
    else:
        print("Book Not Found")


# Register Member
def register_member(member_id):
    members.add(member_id)


# Show Available Books
def show_available():
    print("\nAvailable Books")
    for book_id in catalog:
        if book_id not in borrowed_books:
            print(book_id, catalog[book_id])


# Main Program

# Add 4 Books
add_book(101, "Python", "John", 2022)
add_book(102, "Java", "David", 2021)
add_book(103, "AI", "Alice", 2023)
add_book(104, "ML", "Bob", 2024)

# Register Members
register_member(1)
register_member(2)
register_member(3)
register_member(2)   # Duplicate

# Borrow Books
borrow_book(101)
borrow_book(103)

# Return One Book
return_book(101)

# Show Available Books
show_available()

print("\nBorrowed Books:", borrowed_books)
print("Members:", members)
