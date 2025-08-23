import pytest
import sys
import os
sys.path.append(os.path.dirname(__file__))
from .main import BankAccount, Car, Book, Library


# BankAccount Tests
def test_bank_account_creation():
    """Test creating bank accounts."""
    account = BankAccount("John Doe", 100.0)
    
    assert account.account_holder == "John Doe"
    assert account.balance == 100.0
    assert account.account_number.startswith("ACC")
    assert len(account.transaction_history) == 1
    assert "Initial deposit: $100.00" in account.transaction_history[0]


def test_bank_account_creation_no_initial_balance():
    """Test creating account with no initial balance."""
    account = BankAccount("Jane Smith")
    
    assert account.account_holder == "Jane Smith"
    assert account.balance == 0.0
    assert len(account.transaction_history) == 0


def test_bank_account_negative_initial_balance():
    """Test that negative initial balance raises error."""
    with pytest.raises(ValueError):
        BankAccount("Test User", -100.0)


def test_bank_account_deposit():
    """Test depositing money."""
    account = BankAccount("Test User")
    result = account.deposit(50.0)
    
    assert result == 50.0
    assert account.balance == 50.0
    assert "Deposit: $50.00" in account.transaction_history[-1]


def test_bank_account_deposit_invalid():
    """Test depositing invalid amounts."""
    account = BankAccount("Test User")
    
    with pytest.raises(ValueError):
        account.deposit(0)
    
    with pytest.raises(ValueError):
        account.deposit(-10)


def test_bank_account_withdrawal():
    """Test withdrawing money."""
    account = BankAccount("Test User", 100.0)
    result = account.withdraw(30.0)
    
    assert result == 70.0
    assert account.balance == 70.0
    assert "Withdrawal: $30.00" in account.transaction_history[-1]


def test_bank_account_withdrawal_insufficient_funds():
    """Test withdrawing more than balance."""
    account = BankAccount("Test User", 50.0)
    
    with pytest.raises(ValueError):
        account.withdraw(100.0)


def test_bank_account_withdrawal_invalid():
    """Test withdrawing invalid amounts."""
    account = BankAccount("Test User", 100.0)
    
    with pytest.raises(ValueError):
        account.withdraw(0)
    
    with pytest.raises(ValueError):
        account.withdraw(-10)


def test_bank_account_statement():
    """Test getting account statement."""
    account = BankAccount("Test User", 100.0)
    account.deposit(50.0)
    account.withdraw(25.0)
    
    statement = account.get_statement()
    
    assert "Test User" in statement
    assert "$125.00" in statement  # Final balance
    assert "Initial deposit" in statement
    assert "Deposit: $50.00" in statement
    assert "Withdrawal: $25.00" in statement


def test_bank_account_class_methods():
    """Test class-level functionality."""
    initial_count = BankAccount.get_total_accounts()
    
    account1 = BankAccount("User 1")
    account2 = BankAccount("User 2")
    
    assert BankAccount.get_total_accounts() == initial_count + 2
    assert BankAccount.bank_name == "Python Tutorial Bank"


def test_bank_account_string_representation():
    """Test string representations."""
    account = BankAccount("Test User", 123.45)
    
    str_repr = str(account)
    repr_repr = repr(account)
    
    assert "Test User" in str_repr
    assert "123.45" in str_repr
    assert "'Test User'" in repr_repr
    assert "123.45" in repr_repr


# Car Tests
def test_car_creation():
    """Test creating a car."""
    car = Car("Honda", "Civic", 2020, 10000)
    
    assert car.make == "Honda"
    assert car.model == "Civic"
    assert car.year == 2020
    assert car.mileage == 10000
    assert car.is_running == False
    assert car.fuel_level == 100


def test_car_creation_default_mileage():
    """Test creating car with default mileage."""
    car = Car("Ford", "Focus", 2019)
    
    assert car.mileage == 0


def test_car_start_stop_engine():
    """Test starting and stopping engine."""
    car = Car("Toyota", "Camry", 2021)
    
    # Start engine
    result = car.start_engine()
    assert result == "Engine started successfully"
    assert car.is_running == True
    
    # Try to start again
    result = car.start_engine()
    assert result == "Engine is already running"
    
    # Stop engine
    result = car.stop_engine()
    assert result == "Engine stopped"
    assert car.is_running == False
    
    # Try to stop again
    result = car.stop_engine()
    assert result == "Engine is already stopped"


def test_car_start_no_fuel():
    """Test starting car with no fuel."""
    car = Car("Test", "Car", 2020)
    car.fuel_level = 0
    
    result = car.start_engine()
    assert result == "Cannot start - no fuel"
    assert car.is_running == False


def test_car_drive():
    """Test driving the car."""
    car = Car("Test", "Car", 2020)
    car.start_engine()
    
    result = car.drive(20.0)
    
    assert "Drove 20.0 miles" in result
    assert car.mileage == 20.0
    assert car.fuel_level == 98.0  # Lost 2% fuel (20 miles / 10)


def test_car_drive_engine_off():
    """Test driving with engine off."""
    car = Car("Test", "Car", 2020)
    
    result = car.drive(10.0)
    assert result == "Cannot drive - engine is not running"


def test_car_drive_invalid_distance():
    """Test driving invalid distances."""
    car = Car("Test", "Car", 2020)
    car.start_engine()
    
    result = car.drive(0)
    assert result == "Distance must be positive"
    
    result = car.drive(-10)
    assert result == "Distance must be positive"


def test_car_drive_insufficient_fuel():
    """Test driving without enough fuel."""
    car = Car("Test", "Car", 2020)
    car.start_engine()
    car.fuel_level = 5.0  # Only 5% fuel
    
    result = car.drive(100.0)  # Would need 10% fuel
    assert result == "Not enough fuel for this trip"


def test_car_refuel():
    """Test refueling the car."""
    car = Car("Test", "Car", 2020)
    car.fuel_level = 50.0
    
    # Partial refuel
    result = car.refuel(20.0)
    assert result == "Added 20.0% fuel. Current level: 70.0%"
    assert car.fuel_level == 70.0
    
    # Full tank refuel
    result = car.refuel()
    assert result == "Tank filled to 100%"
    assert car.fuel_level == 100.0


def test_car_refuel_invalid():
    """Test refueling with invalid amounts."""
    car = Car("Test", "Car", 2020)
    
    result = car.refuel(0)
    assert result == "Fuel amount must be positive"
    
    result = car.refuel(-10)
    assert result == "Fuel amount must be positive"


def test_car_refuel_overflow():
    """Test refueling beyond tank capacity."""
    car = Car("Test", "Car", 2020)
    car.fuel_level = 90.0
    
    result = car.refuel(20.0)
    assert car.fuel_level == 100.0  # Capped at 100%


def test_car_get_info():
    """Test getting car information."""
    car = Car("BMW", "X5", 2022, 5000)
    
    info = car.get_info()
    
    assert "2022 BMW X5" in info
    assert "5,000 miles" in info
    assert "100%" in info
    assert "Stopped" in info


def test_car_string_representation():
    """Test car string representation."""
    car = Car("Mercedes", "C-Class", 2023)
    
    str_repr = str(car)
    assert str_repr == "2023 Mercedes C-Class"


# Book Tests
def test_book_creation():
    """Test creating a book."""
    book = Book("Test Title", "Test Author", "123-456-789")
    
    assert book.title == "Test Title"
    assert book.author == "Test Author"
    assert book.isbn == "123-456-789"
    assert book.is_borrowed == False
    assert book.borrower is None


def test_book_string_representation():
    """Test book string representations."""
    book = Book("Python Guide", "John Smith", "978-123-456")
    
    str_repr = str(book)
    repr_repr = repr(book)
    
    assert str_repr == "Python Guide by John Smith"
    assert "'Python Guide'" in repr_repr
    assert "'John Smith'" in repr_repr
    assert "'978-123-456'" in repr_repr


# Library Tests
def test_library_creation():
    """Test creating a library."""
    library = Library("Test Library")
    
    assert library.name == "Test Library"
    assert len(library.books) == 0
    assert len(library.members) == 0


def test_library_add_book():
    """Test adding books to library."""
    library = Library("Test Library")
    book = Book("Test Book", "Test Author", "123-456")
    
    result = library.add_book(book)
    
    assert result == "Added 'Test Book' to the library"
    assert len(library.books) == 1
    assert library.books[0] == book


def test_library_add_duplicate_book():
    """Test adding duplicate books."""
    library = Library("Test Library")
    book1 = Book("Test Book", "Author 1", "123-456")
    book2 = Book("Different Title", "Author 2", "123-456")  # Same ISBN
    
    library.add_book(book1)
    result = library.add_book(book2)
    
    assert "already exists" in result
    assert len(library.books) == 1


def test_library_add_invalid_book():
    """Test adding non-book object."""
    library = Library("Test Library")
    
    with pytest.raises(TypeError):
        library.add_book("not a book")


def test_library_register_member():
    """Test registering library members."""
    library = Library("Test Library")
    
    result = library.register_member("Alice")
    assert result == "Registered Alice as a library member"
    assert "Alice" in library.members
    
    # Try to register again
    result = library.register_member("Alice")
    assert "already a member" in result


def test_library_borrow_book():
    """Test borrowing books."""
    library = Library("Test Library")
    book = Book("Test Book", "Test Author", "123-456")
    library.add_book(book)
    library.register_member("Alice")
    
    result = library.borrow_book("123-456", "Alice")
    
    assert result == "Alice borrowed 'Test Book'"
    assert book.is_borrowed == True
    assert book.borrower == "Alice"


def test_library_borrow_book_non_member():
    """Test borrowing by non-member."""
    library = Library("Test Library")
    book = Book("Test Book", "Test Author", "123-456")
    library.add_book(book)
    
    result = library.borrow_book("123-456", "Bob")
    assert "not a registered member" in result


def test_library_borrow_nonexistent_book():
    """Test borrowing non-existent book."""
    library = Library("Test Library")
    library.register_member("Alice")
    
    result = library.borrow_book("999-999", "Alice")
    assert "not found" in result


def test_library_borrow_already_borrowed():
    """Test borrowing already borrowed book."""
    library = Library("Test Library")
    book = Book("Test Book", "Test Author", "123-456")
    library.add_book(book)
    library.register_member("Alice")
    library.register_member("Bob")
    
    library.borrow_book("123-456", "Alice")
    result = library.borrow_book("123-456", "Bob")
    
    assert "already borrowed by Alice" in result


def test_library_return_book():
    """Test returning books."""
    library = Library("Test Library")
    book = Book("Test Book", "Test Author", "123-456")
    library.add_book(book)
    library.register_member("Alice")
    
    library.borrow_book("123-456", "Alice")
    result = library.return_book("123-456")
    
    assert result == "'Test Book' returned by Alice"
    assert book.is_borrowed == False
    assert book.borrower is None


def test_library_return_not_borrowed():
    """Test returning book that wasn't borrowed."""
    library = Library("Test Library")
    book = Book("Test Book", "Test Author", "123-456")
    library.add_book(book)
    
    result = library.return_book("123-456")
    assert "was not borrowed" in result


def test_library_return_nonexistent():
    """Test returning non-existent book."""
    library = Library("Test Library")
    
    result = library.return_book("999-999")
    assert "not found" in result


def test_library_search_books():
    """Test searching for books."""
    library = Library("Test Library")
    book1 = Book("Python Programming", "John Doe", "123-456")
    book2 = Book("Java Guide", "Jane Smith", "789-012")
    book3 = Book("Web Development", "John Doe", "345-678")
    
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    
    # Search by title
    results = library.search_books("Python")
    assert len(results) == 1
    assert results[0] == book1
    
    # Search by author
    results = library.search_books("John Doe")
    assert len(results) == 2
    assert book1 in results
    assert book3 in results
    
    # Case insensitive search
    results = library.search_books("python")
    assert len(results) == 1


def test_library_get_available_borrowed_books():
    """Test getting available and borrowed books."""
    library = Library("Test Library")
    book1 = Book("Book 1", "Author 1", "123")
    book2 = Book("Book 2", "Author 2", "456")
    
    library.add_book(book1)
    library.add_book(book2)
    library.register_member("Alice")
    
    # Initially all available
    available = library.get_available_books()
    borrowed = library.get_borrowed_books()
    
    assert len(available) == 2
    assert len(borrowed) == 0
    
    # Borrow one book
    library.borrow_book("123", "Alice")
    available = library.get_available_books()
    borrowed = library.get_borrowed_books()
    
    assert len(available) == 1
    assert len(borrowed) == 1
    assert available[0] == book2
    assert borrowed[0] == book1


def test_library_get_stats():
    """Test getting library statistics."""
    library = Library("Test Library")
    book1 = Book("Book 1", "Author 1", "123")
    book2 = Book("Book 2", "Author 2", "456")
    
    library.add_book(book1)
    library.add_book(book2)
    library.register_member("Alice")
    library.register_member("Bob")
    library.borrow_book("123", "Alice")
    
    stats = library.get_library_stats()
    
    assert stats['library_name'] == "Test Library"
    assert stats['total_books'] == 2
    assert stats['available_books'] == 1
    assert stats['borrowed_books'] == 1
    assert stats['total_members'] == 2


def test_library_string_representation():
    """Test library string representation."""
    library = Library("City Library")
    book = Book("Test", "Author", "123")
    library.add_book(book)
    library.register_member("Alice")
    
    str_repr = str(library)
    assert "City Library" in str_repr
    assert "1 books" in str_repr
    assert "1 members" in str_repr
