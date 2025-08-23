# Python Tutorial Missions

A collection of Python programming missions designed to teach fundamental concepts through hands-on practice. Each mission includes a complete implementation with pytest tests.

## Project Structure

```
src/
├── 1-hello-world/           # Basic Python output and functions
├── 2-variables-and-types/   # Working with different data types
├── 3-lists-and-loops/       # Lists, loops, and basic algorithms
├── 4-dictionaries/          # Dictionary manipulation and data structures
├── 5-functions-and-modules/ # Advanced functions, parameters, and modules
└── 6-classes-and-objects/   # Object-oriented programming basics
```

Each mission folder contains:
- `main.py` - Complete implementation with working examples
- `tests.py` - Comprehensive pytest test suite

## Mission Overview

### 1. Hello World
- Basic function creation and return values
- Simple string output
- Introduction to Python syntax

### 2. Variables and Types
- Working with strings, integers, floats, and booleans
- Variable assignment and manipulation
- String formatting and calculations

### 3. Lists and Loops
- Creating and manipulating lists
- Using for loops for iteration
- List operations (append, insert, sum)
- Filtering data with conditionals

### 4. Dictionaries
- Creating and updating dictionaries
- Nested data structures
- Data aggregation and analysis
- Working with key-value pairs

### 5. Functions and Modules
- Function parameters and return values
- Default parameters and *args/**kwargs
- Error handling with exceptions
- Mathematical operations and algorithms
- Module imports

### 6. Classes and Objects
- Class definition and initialization
- Instance methods and attributes
- Object state management
- Real-world class examples (BankAccount, Car, Library)

## Running the Missions

### Prerequisites
- Python 3.7+
- pytest (installed via requirements.txt)

### Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Or if using a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Running Individual Missions
```bash
# Run a specific mission
cd src/1-hello-world
python main.py

# Run tests for a specific mission
pytest tests.py -v
```

### Running All Tests
```bash
# From project root
python -m pytest src/*/tests.py -v
```

## Learning Path

1. **Start with Mission 1** - Get familiar with basic Python syntax
2. **Progress sequentially** - Each mission builds on previous concepts
3. **Read the code** - Study the implementations in `main.py`
4. **Run the tests** - Understand what each function should do
5. **Experiment** - Modify the code and see how tests react

## Test Coverage

Each mission includes comprehensive tests covering:
- ✅ Happy path scenarios
- ✅ Edge cases and boundary conditions  
- ✅ Error handling and validation
- ✅ Type checking and data validation

## Contributing

To add new missions:
1. Create a new numbered folder in `src/`
2. Add `main.py` with complete implementations
3. Add `tests.py` with comprehensive test coverage
4. Update this README with mission description

## License

This project is designed for educational purposes.
