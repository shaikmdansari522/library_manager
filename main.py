
from models import LibraryItem, Book, Magazine, DVD, Member


def main():

    print("===== LIBRARY MANAGEMENT SYSTEM =====")

    # Step 1: Create two members
    member1 = Member("Rahul", 101)
    member2 = Member("Priya", 102)

    # Step 2: Create one object of each item type
    book = Book("Python 101", 1, "A. Rao")
    magazine = Magazine("Tech Monthly", 2, 25)
    dvd = DVD("Python Tutorial", 3, 120)

    # Additional item to test borrowing limit
    extra_book = Book("Advanced Python", 4, "John Smith")

    # Step 3: Display item descriptions
    print("\n===== ITEM DETAILS =====")

    items = [book, magazine, dvd]

    for item in items:
        print(item.describe())

    # Step 4: Demonstrate polymorphism
    print("\n===== LATE FEES FOR 3 DAYS =====")

    for item in items:
        print(f"{item.title}: Rs {item.late_fee(3)}")

    # Step 5: Borrow items
    print("\n===== BORROW ITEMS =====")

    for item in items:
        try:
            member1.borrow(item)
        except ValueError as e:
            print(f"Error: {e}")

    # Step 6: Test borrowing the same item twice
    print("\n===== TEST DUPLICATE BORROWING =====")

    try:
        member2.borrow(book)
    except ValueError as e:
        print(f"Error: {e}")

    # Step 7: Test maximum borrowing limit
    print("\n===== TEST BORROWING LIMIT =====")

    try:
        member1.borrow(extra_book)
    except ValueError as e:
        print(f"Error: {e}")

    # Step 8: Display borrowed items
    print("\n===== BORROWED ITEMS =====")

    print(f"{member1.name}: {member1.borrowed_titles()}")
    print(f"{member2.name}: {member2.borrowed_titles()}")

    # Step 9: Return items and calculate late fees
    print("\n===== RETURN ITEMS =====")

    try:
        fee = member1.return_item(book, 3)
        print(f"Returned {book.title}. Late fee: Rs {fee}")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        fee = member1.return_item(magazine, 3)
        print(f"Returned {magazine.title}. Late fee: Rs {fee}")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        fee = member1.return_item(dvd, 3)
        print(f"Returned {dvd.title}. Late fee: Rs {fee}")
    except ValueError as e:
        print(f"Error: {e}")

    # Step 10: Demonstrate encapsulation
    print("\n===== ENCAPSULATION =====")

    try:
        print(book.__available)
    except AttributeError as e:
        print("Private attribute cannot be accessed directly.")
        print(type(e).__name__)

    print(f"Book availability: {book.is_available()}")

    # Step 11: Display total items
    print("\n===== TOTAL LIBRARY ITEMS =====")

    print(f"Total items created: {LibraryItem.total_items}")


if __name__ == "__main__":
    main()
