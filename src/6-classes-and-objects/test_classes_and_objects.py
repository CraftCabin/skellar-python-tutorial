import pytest
import sys
import os
sys.path.append(os.path.dirname(__file__))
from main import BankAccount, Car, Library


class TestBankAccount:
    """Tests for BankAccount class."""
    
    def test_init_default_balance(self):
        """Test account initialization with default balance."""
        account = BankAccount("John")
        assert account.account_holder == "John"
        assert account.balance == 0
        assert len(account.transaction_history) == 0
    
    def test_init_with_balance(self):
        """Test account initialization with initial balance."""
        account = BankAccount("Jane", 100)
        assert account.account_holder == "Jane"
        assert account.balance == 100
        assert len(account.transaction_history) == 1
        assert "Initial deposit: $100.00" in account.transaction_history[0]
    
    def test_deposit_valid(self):
        """Test valid deposit."""
        account = BankAccount("Alice")
        account.deposit(50)
        assert account.balance == 50
        assert "Deposit: $50.00" in account.transaction_history[0]
    
    def test_deposit_invalid(self):
        """Test invalid deposit amounts."""
        account = BankAccount("Bob")
        
        with pytest.raises(ValueError):
            account.deposit(0)
        
        with pytest.raises(ValueError):
            account.deposit(-10)
    
    def test_withdraw_valid(self):
        """Test valid withdrawal."""
        account = BankAccount("Charlie", 100)
        result = account.withdraw(30)
        assert result is True
        assert account.balance == 70
        assert "Withdrawal: $30.00" in account.transaction_history[-1]
    
    def test_withdraw_insufficient_funds(self):
        """Test withdrawal with insufficient funds."""
        account = BankAccount("David", 50)
        result = account.withdraw(100)
        assert result is False
        assert account.balance == 50  # Balance unchanged
    
    def test_withdraw_invalid(self):
        """Test invalid withdrawal amounts."""
        account = BankAccount("Eve", 100)
        
        with pytest.raises(ValueError):
            account.withdraw(0)
        
        with pytest.raises(ValueError):
            account.withdraw(-10)
    
    def test_get_balance(self):
        """Test getting account balance."""
        account = BankAccount("Frank", 75)
        assert account.get_balance() == 75
    
    def test_transaction_history(self):
        """Test transaction history."""
        account = BankAccount("Grace", 100)
        account.deposit(25)
        account.withdraw(10)
        
        history = account.get_transaction_history()
        assert len(history) == 3
        assert "Initial deposit" in history[0]
        assert "Deposit: $25.00" in history[1]
        assert "Withdrawal: $10.00" in history[2]


class TestCar:
    """Tests for Car class."""
    
    def test_init(self):
        """Test car initialization."""
        car = Car("Honda", "Civic", 2020, 5000)
        assert car.make == "Honda"
        assert car.model == "Civic"
        assert car.year == 2020
        assert car.mileage == 5000
        assert car.is_running is False
    
    def test_init_default_mileage(self):
        """Test car initialization with default mileage."""
        car = Car("Ford", "Focus", 2018)
        assert car.mileage == 0
    
    def test_start_stop(self):
        """Test starting and stopping the car."""
        car = Car("BMW", "X3", 2021)
        
        # Start the car
        result = car.start()
        assert car.is_running is True
        assert "BMW X3 is now running" in result
        
        # Try starting again
        result = car.start()
        assert "already running" in result
        
        # Stop the car
        result = car.stop()
        assert car.is_running is False
        assert "BMW X3 has stopped" in result
        
        # Try stopping again
        result = car.stop()
        assert "already stopped" in result
    
    def test_drive_valid(self):
        """Test driving the car."""
        car = Car("Audi", "A4", 2019, 10000)
        car.start()
        
        result = car.drive(100)
        assert car.mileage == 10100
        assert "Drove 100" in result
        assert "Total mileage: 10100" in result
    
    def test_drive_not_running(self):
        """Test driving when car is not running."""
        car = Car("Mercedes", "C300", 2020)
        result = car.drive(50)
        assert "Cannot drive - car is not running" in result
        assert car.mileage == 0
    
    def test_drive_negative_distance(self):
        """Test driving with negative distance."""
        car = Car("Lexus", "RX", 2021)
        car.start()
        
        with pytest.raises(ValueError):
            car.drive(-10)
    
    def test_get_age(self):
        """Test getting car age."""
        car = Car("Nissan", "Altima", 2020)
        age = car.get_age(2025)
        assert age == 5


class TestLibrary:
    """Tests for Library class."""
    
    def test_init(self):
        """Test library initialization."""
        library = Library("Central Library")
        assert library.name == "Central Library"
        assert len(library.books) == 0
        assert len(library.borrowed_books) == 0
    
    def test_add_book(self):
        """Test adding books to library."""
        library = Library("Public Library")
        library.add_book("123", "Python Guide", "Alice Author")
        
        assert "123" in library.books
        assert library.books["123"]["title"] == "Python Guide"
        assert library.books["123"]["author"] == "Alice Author"
        assert library.books["123"]["is_available"] is True
    
    def test_borrow_book_valid(self):
        """Test borrowing an available book."""
        library = Library("School Library")
        library.add_book("456", "Data Analysis", "Bob Writer")
        
        result = library.borrow_book("456", "Student John")
        assert result is True
        assert library.books["456"]["is_available"] is False
        assert library.borrowed_books["456"] == "Student John"
    
    def test_borrow_book_nonexistent(self):
        """Test borrowing a non-existent book."""
        library = Library("City Library")
        result = library.borrow_book("999", "Jane Doe")
        assert result is False
    
    def test_borrow_book_unavailable(self):
        """Test borrowing an already borrowed book."""
        library = Library("University Library")
        library.add_book("789", "Machine Learning", "Carol Expert")
        library.borrow_book("789", "First Borrower")
        
        result = library.borrow_book("789", "Second Borrower")
        assert result is False
    
    def test_return_book_valid(self):
        """Test returning a borrowed book."""
        library = Library("Community Library")
        library.add_book("101", "Web Development", "Dave Coder")
        library.borrow_book("101", "Borrower Name")
        
        result = library.return_book("101")
        assert result is True
        assert library.books["101"]["is_available"] is True
        assert "101" not in library.borrowed_books
    
    def test_return_book_not_borrowed(self):
        """Test returning a book that wasn't borrowed."""
        library = Library("Local Library")
        library.add_book("202", "Database Design", "Eve Engineer")
        
        result = library.return_book("202")
        assert result is False
    
    def test_get_available_books(self):
        """Test getting available books."""
        library = Library("Main Library")
        library.add_book("111", "Book One", "Author One")
        library.add_book("222", "Book Two", "Author Two")
        library.borrow_book("111", "Reader")
        
        available = library.get_available_books()
        assert len(available) == 1
        assert available[0]["isbn"] == "222"
        assert available[0]["title"] == "Book Two"
    
    def test_get_borrowed_books(self):
        """Test getting borrowed books."""
        library = Library("Branch Library")
        library.add_book("333", "Book Three", "Author Three")
        library.add_book("444", "Book Four", "Author Four")
        library.borrow_book("333", "Borrower One")
        library.borrow_book("444", "Borrower Two")
        
        borrowed = library.get_borrowed_books()
        assert len(borrowed) == 2
        
        isbn_to_borrower = {book["isbn"]: book["borrower"] for book in borrowed}
        assert isbn_to_borrower["333"] == "Borrower One"
        assert isbn_to_borrower["444"] == "Borrower Two"
