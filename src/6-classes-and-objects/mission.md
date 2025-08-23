# Mission 6: Classes and Objects

## Learning Objectives
- Understand object-oriented programming (OOP) concepts
- Learn class definition and instantiation
- Master instance methods and attributes
- Practice encapsulation and data management
- Implement real-world object models

## Concepts Covered
- Class definition with `class` keyword
- Constructor method `__init__()`
- Instance attributes and methods
- String representation with `__str__()`
- Object state management
- Encapsulation and data hiding
- Real-world modeling with objects

## Mission Description
Object-oriented programming allows you to model real-world entities as objects with properties (attributes) and behaviors (methods). This mission implements three practical classes that demonstrate core OOP principles.

## What You'll Build
Three complete classes representing real-world entities:
1. `BankAccount` - Financial account management with transactions
2. `Car` - Vehicle with state management and operations
3. `Library` - Book management system with borrowing/returning

## Key Code Concepts

### Class Definition
```python
class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder  # Instance attribute
        self.balance = initial_balance
        self.transaction_history = []
```

### Instance Methods
```python
def deposit(self, amount):
    if amount <= 0:
        raise ValueError("Deposit amount must be positive")
    self.balance += amount
    self.transaction_history.append(f"Deposit: ${amount:.2f}")
```

### String Representation
```python
def __str__(self):
    return f"BankAccount({self.account_holder}, Balance: ${self.balance:.2f})"
```

### State Management
```python
def start(self):
    if not self.is_running:
        self.is_running = True
        return f"{self.make} {self.model} is now running"
    return f"{self.make} {self.model} is already running"
```

## Class Designs

### BankAccount Class
**Attributes:**
- `account_holder` (str) - Account owner's name
- `balance` (float) - Current account balance
- `transaction_history` (list) - Record of all transactions

**Methods:**
- `deposit(amount)` - Add money to account
- `withdraw(amount)` - Remove money (with validation)
- `get_balance()` - Return current balance
- `get_transaction_history()` - Return copy of transactions

### Car Class
**Attributes:**
- `make`, `model`, `year` (str/int) - Car identification
- `mileage` (float) - Current odometer reading
- `is_running` (bool) - Engine state

**Methods:**
- `start()` / `stop()` - Control engine state
- `drive(distance)` - Move car and update mileage
- `get_age(current_year)` - Calculate car's age

### Library Class
**Attributes:**
- `name` (str) - Library name
- `books` (dict) - ISBN -> book information
- `borrowed_books` (dict) - ISBN -> borrower mapping

**Methods:**
- `add_book(isbn, title, author)` - Add books to collection
- `borrow_book(isbn, borrower)` - Check out books
- `return_book(isbn)` - Return borrowed books
- `get_available_books()` / `get_borrowed_books()` - Query collections

## Tasks to Complete
1. ✅ Define classes with proper `__init__` methods
2. ✅ Implement instance methods that modify object state
3. ✅ Add validation and error handling in methods
4. ✅ Manage complex state transitions (car running/stopped)
5. ✅ Implement data relationships (library books and borrowers)
6. ✅ Create meaningful string representations

## Running Your Code
```bash
# Run the script directly
python main.py

# Run the tests
pytest tests.py -v
```

## Expected Output
When you run `main.py`, you should see:
```
BankAccount(Alice, Balance: $100.00)
Balance: 125.0
History: ['Initial deposit: $100.00', 'Deposit: $50.00', 'Withdrawal: $25.00']
2020 Toyota Camry (15000 miles, stopped)
Toyota Camry is now running
Drove 100 miles. Total mileage: 15100
2020 Toyota Camry (15100 miles, running)
Available books: [{'isbn': '123', 'title': 'Python Programming', 'author': 'John Doe'}, {'isbn': '456', 'title': 'Data Science', 'author': 'Jane Smith'}]
Borrowed books: [{'isbn': '123', 'title': 'Python Programming', 'author': 'John Doe', 'borrower': 'Bob'}]
```

## Test Requirements
Your classes must pass comprehensive tests covering:
- Object initialization with various parameters
- Method functionality and state changes
- Input validation and error handling
- Complex workflows (borrow → return cycles)
- Edge cases and boundary conditions

## OOP Principles Demonstrated

### Encapsulation
- Data (attributes) and behavior (methods) bundled together
- Internal state protected through method interfaces
- Validation logic contained within the class

### Abstraction
- Complex operations hidden behind simple method calls
- Users don't need to understand internal implementation
- Clear, intuitive interfaces for common operations

### Data Integrity
- Methods ensure object state remains valid
- Validation prevents impossible states
- Automatic calculations (like averages) stay synchronized

## Common Mistakes to Avoid
- ❌ Forgetting `self` parameter in method definitions
- ❌ Not initializing all attributes in `__init__`
- ❌ Modifying attributes directly instead of using methods
- ❌ Not validating inputs in methods
- ❌ Creating methods that don't use `self` (should be functions instead)

## Real-World Applications
These patterns are used everywhere:
- **BankAccount**: Financial software, payment systems, accounting
- **Car**: Vehicle management, fleet tracking, simulation games
- **Library**: Content management, inventory systems, resource booking

## Advanced OOP Concepts (Not Covered Here)
- Inheritance and subclasses
- Polymorphism and method overriding
- Class methods and static methods
- Properties and getters/setters
- Abstract base classes

## Next Steps
Congratulations! You've completed all six missions and learned Python fundamentals:
1. ✅ Functions and basic syntax
2. ✅ Variables and data types
3. ✅ Lists and control flow
4. ✅ Dictionaries and data structures
5. ✅ Advanced functions and modules
6. ✅ Object-oriented programming

You're now ready to tackle real-world Python projects!
