class BankAccount:
    """A simple bank account class."""
    
    def __init__(self, account_holder, initial_balance=0):
        """
        Initialize a bank account.
        
        Args:
            account_holder (str): Name of the account holder
            initial_balance (float): Starting balance (default: 0)
        """
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transaction_history = []
        
        if initial_balance > 0:
            self.transaction_history.append(f"Initial deposit: ${initial_balance:.2f}")
    
    def deposit(self, amount):
        """
        Deposit money into the account.
        
        Args:
            amount (float): Amount to deposit
            
        Raises:
            ValueError: If amount is negative or zero
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        
        self.balance += amount
        self.transaction_history.append(f"Deposit: ${amount:.2f}")
    
    def withdraw(self, amount):
        """
        Withdraw money from the account.
        
        Args:
            amount (float): Amount to withdraw
            
        Returns:
            bool: True if withdrawal successful, False if insufficient funds
            
        Raises:
            ValueError: If amount is negative or zero
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        
        if amount > self.balance:
            return False
        
        self.balance -= amount
        self.transaction_history.append(f"Withdrawal: ${amount:.2f}")
        return True
    
    def get_balance(self):
        """Get current account balance."""
        return self.balance
    
    def get_transaction_history(self):
        """Get list of all transactions."""
        return self.transaction_history.copy()
    
    def __str__(self):
        """String representation of the account."""
        return f"BankAccount({self.account_holder}, Balance: ${self.balance:.2f})"


class Car:
    """A simple car class."""
    
    def __init__(self, make, model, year, mileage=0):
        """
        Initialize a car.
        
        Args:
            make (str): Car manufacturer
            model (str): Car model
            year (int): Year of manufacture
            mileage (float): Current mileage (default: 0)
        """
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.is_running = False
    
    def start(self):
        """Start the car."""
        if not self.is_running:
            self.is_running = True
            return f"{self.make} {self.model} is now running"
        return f"{self.make} {self.model} is already running"
    
    def stop(self):
        """Stop the car."""
        if self.is_running:
            self.is_running = False
            return f"{self.make} {self.model} has stopped"
        return f"{self.make} {self.model} is already stopped"
    
    def drive(self, distance):
        """
        Drive the car for a given distance.
        
        Args:
            distance (float): Distance to drive
            
        Returns:
            str: Status message
            
        Raises:
            ValueError: If distance is negative
        """
        if distance < 0:
            raise ValueError("Distance cannot be negative")
        
        if not self.is_running:
            return "Cannot drive - car is not running"
        
        self.mileage += distance
        return f"Drove {distance} miles. Total mileage: {self.mileage}"
    
    def get_age(self, current_year=2025):
        """Get the age of the car."""
        return current_year - self.year
    
    def __str__(self):
        """String representation of the car."""
        status = "running" if self.is_running else "stopped"
        return f"{self.year} {self.make} {self.model} ({self.mileage} miles, {status})"


class Library:
    """A simple library management class."""
    
    def __init__(self, name):
        """
        Initialize a library.
        
        Args:
            name (str): Name of the library
        """
        self.name = name
        self.books = {}  # ISBN -> {title, author, is_available}
        self.borrowed_books = {}  # ISBN -> borrower_name
    
    def add_book(self, isbn, title, author):
        """
        Add a book to the library.
        
        Args:
            isbn (str): Book ISBN
            title (str): Book title
            author (str): Book author
        """
        self.books[isbn] = {
            'title': title,
            'author': author,
            'is_available': True
        }
    
    def borrow_book(self, isbn, borrower_name):
        """
        Borrow a book from the library.
        
        Args:
            isbn (str): Book ISBN
            borrower_name (str): Name of borrower
            
        Returns:
            bool: True if successful, False otherwise
        """
        if isbn not in self.books:
            return False
        
        if not self.books[isbn]['is_available']:
            return False
        
        self.books[isbn]['is_available'] = False
        self.borrowed_books[isbn] = borrower_name
        return True
    
    def return_book(self, isbn):
        """
        Return a book to the library.
        
        Args:
            isbn (str): Book ISBN
            
        Returns:
            bool: True if successful, False otherwise
        """
        if isbn not in self.books or self.books[isbn]['is_available']:
            return False
        
        self.books[isbn]['is_available'] = True
        del self.borrowed_books[isbn]
        return True
    
    def get_available_books(self):
        """Get list of available books."""
        available = []
        for isbn, book in self.books.items():
            if book['is_available']:
                available.append({
                    'isbn': isbn,
                    'title': book['title'],
                    'author': book['author']
                })
        return available
    
    def get_borrowed_books(self):
        """Get list of borrowed books with borrower names."""
        borrowed = []
        for isbn, borrower in self.borrowed_books.items():
            book = self.books[isbn]
            borrowed.append({
                'isbn': isbn,
                'title': book['title'],
                'author': book['author'],
                'borrower': borrower
            })
        return borrowed


if __name__ == "__main__":
    # Test BankAccount
    account = BankAccount("Alice", 100)
    print(account)
    account.deposit(50)
    account.withdraw(25)
    print(f"Balance: {account.get_balance()}")
    print("History:", account.get_transaction_history())
    
    # Test Car
    car = Car("Toyota", "Camry", 2020, 15000)
    print(car)
    print(car.start())
    print(car.drive(100))
    print(car)
    
    # Test Library
    library = Library("City Library")
    library.add_book("123", "Python Programming", "John Doe")
    library.add_book("456", "Data Science", "Jane Smith")
    print("Available books:", library.get_available_books())
    library.borrow_book("123", "Bob")
    print("Borrowed books:", library.get_borrowed_books())
