# Mission 6: Classes and Objects

Welcome to Mission 6, the final mission in our Python tutorial series! This mission introduces you to object-oriented programming (OOP) concepts in Python, including classes, objects, inheritance, and encapsulation.

## Learning Objectives

By the end of this mission, you will understand:

1. **Class Definition and Instantiation**
   - Creating classes with `class` keyword
   - Defining `__init__` method for initialization
   - Creating objects (instances) from classes
   - Understanding the difference between classes and instances

2. **Attributes and Methods**
   - Instance attributes vs class attributes
   - Public vs protected attributes (naming conventions)
   - Instance methods, class methods, and static methods
   - Properties and property decorators

3. **Encapsulation and Data Validation**
   - Using protected attributes (leading underscore)
   - Property decorators for controlled access
   - Input validation in methods
   - Error handling within classes

4. **Special Methods (Dunder Methods)**
   - `__init__` for object initialization
   - `__str__` for user-friendly string representation
   - `__repr__` for developer-friendly representation

5. **Class Relationships and Composition**
   - Creating classes that contain other objects
   - Building complex systems from simple components
   - Managing collections of objects

## Classes Implemented

### 1. BankAccount Class

A complete banking system demonstrating core OOP concepts.

**Features:**
- Account creation with automatic account numbering
- Secure balance management (protected attribute)
- Transaction history tracking
- Deposit and withdrawal operations with validation
- Account statements and reporting
- Class-level tracking of total accounts

**Key Concepts Demonstrated:**
- Constructor with default parameters
- Protected attributes (`_balance`)
- Property decorator for read-only access
- Input validation and error handling
- Class attributes and class methods
- String representation methods

**Example Usage:**
```python
account = BankAccount("Alice Johnson", 1000.0)
account.deposit(500.0)
account.withdraw(200.0)
print(account.get_statement())
```

### 2. Car Class

A vehicle simulation demonstrating state management and method types.

**Features:**
- Engine start/stop functionality
- Fuel level management and consumption
- Mileage tracking
- Driving simulation with fuel consumption
- Refueling operations
- Car status reporting

**Key Concepts Demonstrated:**
- Boolean state management
- Method chaining and return values
- Complex state interactions
- Real-world modeling with classes
- Default parameter handling

**Example Usage:**
```python
car = Car("Toyota", "Camry", 2020, 15000)
car.start_engine()
car.drive(50)
car.refuel()
```

### 3. Book and Library System

A library management system demonstrating composition and collection management.

**Components:**
- **Book Class**: Simple book representation with borrowing status
- **Library Class**: Complete library management system

**Features:**
- Book collection management
- Member registration system
- Borrowing and returning books
- Book search functionality
- Library statistics and reporting
- Data validation and error handling

**Key Concepts Demonstrated:**
- Composition (Library contains Books)
- Collection management with lists and sets
- Search algorithms
- Complex business logic
- System integration

**Example Usage:**
```python
library = Library("City Library")
book = Book("Python Programming", "John Doe", "978-1234567890")
library.add_book(book)
library.register_member("Alice")
library.borrow_book("978-1234567890", "Alice")
```

## Object-Oriented Programming Concepts

### Encapsulation
- **Private Data**: Using protected attributes (`_balance`) to hide internal state
- **Controlled Access**: Properties provide read-only or validated access
- **Data Validation**: Methods validate inputs before modifying state

### Abstraction
- **Interface Design**: Classes provide clean, simple interfaces
- **Implementation Hiding**: Internal complexity hidden from users
- **Method Organization**: Related functionality grouped in classes

### Composition
- **Object Relationships**: Library contains Book objects
- **System Building**: Complex systems built from simple components
- **Dependency Management**: Clear relationships between objects

### Class vs Instance Concepts
- **Instance Attributes**: Unique to each object (`self.name`)
- **Class Attributes**: Shared by all instances (`BankAccount.bank_name`)
- **Instance Methods**: Operate on specific instances
- **Class Methods**: Operate on the class itself (`@classmethod`)

## Design Patterns Demonstrated

### Constructor Pattern
```python
def __init__(self, required_param, optional_param=default_value):
    # Initialize instance attributes
    self.attribute = value
```

### Property Pattern
```python
@property
def attribute(self):
    return self._protected_attribute
```

### Validation Pattern
```python
def method(self, value):
    if not self._is_valid(value):
        raise ValueError("Invalid input")
    # Process valid input
```

### Collection Management Pattern
```python
def add_item(self, item):
    if not isinstance(item, ExpectedType):
        raise TypeError("Wrong type")
    self.items.append(item)
```

## Error Handling in Classes

The classes demonstrate proper error handling:
- **Input Validation**: Check parameters before processing
- **Type Checking**: Ensure correct object types
- **State Validation**: Verify object state before operations
- **Clear Messages**: Provide helpful error descriptions

## Testing Strategy

The test suite demonstrates comprehensive testing approaches:
- **Unit Tests**: Test individual methods in isolation
- **Integration Tests**: Test class interactions
- **Edge Case Testing**: Test boundary conditions
- **Error Testing**: Verify proper exception handling

## Running the Code

To run the main demonstration:
```bash
python main.py
```

To run all tests:
```bash
pytest tests.py -v
```

To run specific test categories:
```bash
pytest tests.py::test_bank_account_creation -v
pytest tests.py -k "car" -v
pytest tests.py -k "library" -v
```

## Real-World Applications

These patterns are used in real software:
- **Banking Systems**: Account management, transaction processing
- **Vehicle Management**: Fleet tracking, maintenance systems
- **Library Systems**: Inventory management, user tracking
- **E-commerce**: Product catalogs, shopping carts
- **Gaming**: Player objects, game state management

## Best Practices Demonstrated

1. **Clear Naming**: Classes use PascalCase, methods use snake_case
2. **Docstrings**: All classes and methods documented
3. **Type Hints**: Clear parameter and return types in documentation
4. **Error Handling**: Proper exception raising with clear messages
5. **Encapsulation**: Protected attributes and controlled access
6. **Single Responsibility**: Each class has one clear purpose
7. **Composition over Inheritance**: Building systems by combining objects

## Advanced Concepts for Further Study

After mastering this mission, explore:
- **Inheritance**: Creating classes that extend other classes
- **Polymorphism**: Objects of different types with common interfaces
- **Abstract Base Classes**: Defining interfaces for other classes
- **Decorators**: Advanced method modification techniques
- **Context Managers**: Objects that work with `with` statements
- **Metaclasses**: Classes that create other classes

## Project Extensions

Try extending these classes:
1. **BankAccount**: Add interest calculation, account types, overdraft protection
2. **Car**: Add different vehicle types, maintenance tracking, GPS navigation
3. **Library**: Add book reservations, late fees, digital resources
4. **New Classes**: Create Student/Course system, Inventory/Product system

## Summary

This mission completes your foundation in Python programming by introducing object-oriented programming concepts. You now have the tools to:
- Design and implement classes for real-world problems
- Manage complex data and behavior relationships
- Build scalable and maintainable code systems
- Apply professional software development patterns

Congratulations on completing all six missions! You're now ready to tackle more advanced Python topics and real-world programming challenges.
