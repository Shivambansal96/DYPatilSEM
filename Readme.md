<div align="center">

# 🐍🚀 Python Basics – D Y Patil SEM

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active%20Learning-success?style=for-the-badge)
![Students](https://img.shields.io/badge/DYPatil%20SEM%20Students-Learning-blue?style=for-the-badge)
![Progress](https://img.shields.io/badge/Day%202-Ongoing-brightgreen?style=for-the-badge)
![Duration](https://img.shields.io/badge/Duration-2%20Days-orange?style=for-the-badge)

### 🚀 *Master Python Fundamentals in 2 Days!*

**Welcome to your comprehensive 2-day Python learning journey!**  
Everything you need to build a strong foundation in Python programming.

[📚 Start Learning](#-topics-covered---day-1) • [💻 Practice Questions](#-practice-questions---day-1) • [🎯 What's Next](#-whats-next)

---

</div>

## 🎯 Quick Navigation

<table>
<tr>
<td width="50%" align="center">

### 📖 **Day 1: Fundamentals**
Variables, DataTypes & Functions

[Jump to Day 1 →](#-topics-covered---day-1)

</td>
<td width="50%" align="center">

### 🎨 **Day 2: OOPs**
Encapsulation & Inheritance

[Jump to Day 2 →](#-topics-covered---day-2)

</td>
</tr>
</table>

---

## 📊 Learning Progress

```
Day 1 - Python Fundamentals & Functions:
████████████████████████████████ 100%

✅ Python Installation and Setup
✅ DataTypes - Integers, Floats, Strings, Booleans, Lists, Tuples
✅ Rules for Identifiers - Naming conventions and best practices
✅ Variables - Declaration and Assignment
✅ Operators - Arithmetic, Relational, Assignment, Logical
✅ Comments - Single-line and Multi-line comments
✅ Taking Inputs - input() function and user interaction
✅ Type Conversion & Casting - int(), float(), str(), bool()
✅ Conditional Statements - if, else, elif
✅ Strings - Creation, indexing, slicing, in-built methods
✅ Lists - Creation, indexing, slicing, in-built methods
✅ Tuples - Immutable sequences and operations
✅ Loops - for and while loops with break and continue
✅ Functions - Definition, parameters, return values
✅ 20+ Practice Questions Solved

Day 2 - Object-Oriented Programming (In Progress):
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 0%

⏳ Classes and Objects (In Progress)
⏳ Constructor and Methods
⏳ Encapsulation - Data hiding and access control
⏳ Inheritance - Code reusability and hierarchy
⏳ Access Modifiers - Public, Protected, Private
```

---

## 📚 Topics Covered - Day 1

### ✅ Python Installation and Setup
- **What is Python?** - Interpreted, high-level programming language
- **Installation** - Download from python.org, installation steps
- **IDE/Editors** - VS Code, PyCharm, Thonny, Jupyter Notebook
- **Running Python** - Interactive mode vs Script mode
- **First Program** - `print("Hello, World!")`

### ✅ DataTypes - Foundation of Programming
- **Integer (int)** - Whole numbers: 5, -10, 0, 1000
  - `x = 42` (positive integer)
  - `y = -15` (negative integer)
  
- **Float** - Decimal numbers: 3.14, -2.5, 0.001
  - `price = 99.99` (price with decimal)
  - `temperature = 36.5` (temperature reading)
  
- **String (str)** - Text data: "Hello", 'Python', "123"
  - Single quotes: `'Hello'`
  - Double quotes: `"World"`
  - Multi-line: `"""Multi\nline string"""`
  
- **Boolean (bool)** - True or False values
  - `is_active = True`
  - `is_logged_in = False`
  - Result of comparison: `5 > 3` returns `True`
  
- **List** - Ordered, mutable collection: [1, 2, 3]
  - `fruits = ['apple', 'banana', 'orange']`
  - Mixed types: `[1, 'hello', 3.14, True]`
  
- **Tuple** - Ordered, immutable collection: (1, 2, 3)
  - `coordinates = (10, 20)`
  - Single element: `single = (5,)` (note the comma)

- **Type Checking** - Using `type()` function
  - `type(42)` returns `<class 'int'>`
  - `type("Hello")` returns `<class 'str'>`

### ✅ Rules for Identifiers (Variable Naming)
- **What are Identifiers?** - Names for variables, functions, classes
- **Valid Rules:**
  - Must start with letter (a-z, A-Z) or underscore (_)
  - Can contain letters, digits, and underscores
  - Case-sensitive: `name` ≠ `Name` ≠ `NAME`
  - No spaces allowed
  - No special characters (@, #, $, %, etc.)
  
- **Valid Examples:**
  - `student_name` ✅
  - `_private_var` ✅
  - `age123` ✅
  - `MyClass` ✅
  
- **Invalid Examples:**
  - `123student` ❌ (starts with digit)
  - `student-name` ❌ (contains hyphen)
  - `student name` ❌ (contains space)
  - `student@name` ❌ (contains special character)

- **Python Keywords** - Reserved words (cannot use as identifiers)
  - `if`, `else`, `for`, `while`, `def`, `class`, `import`, `return`, `True`, `False`, `None`, etc.

- **Naming Conventions:**
  - `snake_case` for variables and functions: `user_name`, `calculate_area()`
  - `CamelCase` for classes: `StudentClass`, `MyClass`
  - `CONSTANT` for constants: `MAX_SIZE`, `PI_VALUE`

### ✅ Variables - Storage and Assignment
- **What are Variables?** - Named storage containers for data
- **Variable Declaration** - Creating and assigning values
  - `name = "Alice"` (string assignment)
  - `age = 20` (integer assignment)
  - `height = 5.8` (float assignment)
  
- **Multiple Assignment:**
  - `a = b = c = 10` (assigning same value to multiple variables)
  - `x, y, z = 1, 2, 3` (unpacking values)
  
- **Variable Reassignment** - Changing values
  - `count = 5`
  - `count = 10` (value changes, same variable)
  
- **Type Changing** - Variables can hold different types
  - `data = 42` (initially integer)
  - `data = "forty-two"` (changed to string)

### ✅ Operators - Performing Operations
#### **Arithmetic Operators** ( `+` , `-` , `*` , `/` , `%` , `**` , `//` )
- **Addition (+)** - `5 + 3 = 8`
- **Subtraction (-)** - `10 - 4 = 6`
- **Multiplication (*)** - `6 * 7 = 42`
- **Division (/)** - `15 / 3 = 5.0` (always returns float)
- **Floor Division (//)** - `15 // 4 = 3` (returns integer, rounds down)
- **Modulus (%)** - `15 % 4 = 3` (remainder after division)
- **Exponentiation (**)** - `2 ** 3 = 8` (power operation)

#### **Relational / Comparison Operators** ( `==` , `!=` , `>` , `<` , `>=` , `<=` )
- **Equal to (==)** - `5 == 5` returns `True`
- **Not equal to (!=)** - `5 != 3` returns `True`
- **Greater than (>)** - `10 > 5` returns `True`
- **Less than (<)** - `3 < 7` returns `True`
- **Greater than or equal (>=)** - `10 >= 10` returns `True`
- **Less than or equal (<=)** - `5 <= 8` returns `True`

#### **Assignment Operators** ( `=` , `+=` , `-=` , `*=` , `/=` , `%=` , `**=` )
- **Simple assignment (=)** - `x = 10`
- **Add and assign (+=)** - `x += 5` is same as `x = x + 5`
- **Subtract and assign (-=)** - `x -= 3` is same as `x = x - 3`
- **Multiply and assign (*=)** - `x *= 2` is same as `x = x * 2`
- **Divide and assign (/=)** - `x /= 2` is same as `x = x / 2`
- **Modulus and assign (%=)** - `x %= 3` is same as `x = x % 3`
- **Exponent and assign (**=)** - `x **= 2` is same as `x = x ** 2`

#### **Logical Operators** ( `and` , `or` , `not` )
- **and** - Both conditions must be True
  - `(5 > 3) and (10 > 5)` returns `True`
  - `(5 > 10) and (3 > 1)` returns `False`
  
- **or** - At least one condition must be True
  - `(5 > 10) or (3 > 1)` returns `True`
  - `(5 > 10) or (3 > 10)` returns `False`
  
- **not** - Inverts the boolean value
  - `not True` returns `False`
  - `not (5 > 10)` returns `True`

### ✅ Comments - Documenting Code
- **Single-line Comments** - Using `#`
  ```python
  # This is a single-line comment
  x = 10  # This is an inline comment
  ```

- **Multi-line Comments** - Using triple quotes
  ```python
  """
  This is a multi-line comment.
  It can span multiple lines.
  Often used for docstrings.
  """
  ```

- **Best Practices:**
  - Explain WHY, not WHAT
  - Keep comments updated with code
  - Avoid obvious comments
  - Use meaningful comment text

### ✅ Taking Inputs - User Interaction
- **input() Function** - Getting user input
  - Syntax: `variable = input("prompt message")`
  - Always returns a string
  - Example: `name = input("Enter your name: ")`
  
- **Taking Multiple Inputs:**
  - Separate statements:
    ```python
    name = input("Enter name: ")
    age = input("Enter age: ")
    city = input("Enter city: ")
    ```
  
- **Input and Display:**
  ```python
  student_name = input("What is your name? ")
  print(f"Hello, {student_name}!")
  ```

### ✅ Type Conversion & Casting
- **What is Type Conversion?** - Converting one data type to another
- **Automatic Type Conversion** - Python converts implicitly
  - `result = 5 + 3.5` (int + float = float)
  - `result` is `8.5` (converted to float)
  
- **Manual Type Casting** - Explicit conversion
  - **int()** - Convert to integer
    - `int("42")` returns `42`
    - `int(3.14)` returns `3`
    - `int("42.5")` causes error
    
  - **float()** - Convert to float
    - `float("3.14")` returns `3.14`
    - `float(42)` returns `42.0`
    
  - **str()** - Convert to string
    - `str(42)` returns `"42"`
    - `str(3.14)` returns `"3.14"`
    
  - **bool()** - Convert to boolean
    - `bool(1)` returns `True`
    - `bool(0)` returns `False`
    - `bool("")` returns `False` (empty string)
    - `bool("hello")` returns `True` (non-empty string)

- **Practical Example:**
  ```python
  age_str = input("Enter your age: ")  # Gets "25" as string
  age_int = int(age_str)  # Converts to integer 25
  next_year_age = age_int + 1  # Can now perform math
  print(f"Next year you'll be {next_year_age}")
  ```

### ✅ Conditional Statements - Decision Making
- **if Statement** - Execute code if condition is true
  ```python
  if age >= 18:
      print("You are an adult")
  ```

- **else Statement** - Execute if condition is false
  ```python
  if age >= 18:
      print("You are an adult")
  else:
      print("You are a minor")
  ```

- **elif Statement** - Multiple conditions
  ```python
  if score >= 90:
      grade = 'A'
  elif score >= 80:
      grade = 'B'
  elif score >= 70:
      grade = 'C'
  else:
      grade = 'F'
  ```

- **Nested if Statements** - Conditions within conditions
  ```python
  if age >= 18:
      if score >= 80:
          print("You are eligible for scholarship")
  ```

### ✅ Strings - Text Processing
- **String Creation** - Creating string data
  - Single quotes: `name = 'Alice'`
  - Double quotes: `city = "Mumbai"`
  - Triple quotes: `bio = """Multi\nline text"""`

- **String Indexing** - Accessing individual characters
  - `text = "PYTHON"`
  - `text[0]` = 'P' (first character)
  - `text[5]` = 'N' (sixth character)
  - `text[-1]` = 'N' (last character)
  - `text[-2]` = 'O' (second last character)

- **String Slicing** - Extracting substrings
  - Syntax: `string[start:end:step]`
  - `text[0:3]` = 'PYT' (characters 0, 1, 2)
  - `text[1:4]` = 'YTH' (characters 1, 2, 3)
  - `text[:3]` = 'PYT' (from start to index 3)
  - `text[3:]` = 'HON' (from index 3 to end)
  - `text[::2]` = 'pto' (every 2nd character)
  - `text[::-1]` = 'NOHTYP' (reverse string)

- **String In-Built Methods** (13+ methods covered)
  - **Case Conversion:**
    - `.upper()` - Convert to uppercase: `"hello".upper()` = `"HELLO"`
    - `.lower()` - Convert to lowercase: `"HELLO".lower()` = `"hello"`
    - `.capitalize()` - First letter uppercase: `"hello".capitalize()` = `"Hello"`
    - `.title()` - First letter of each word: `"hello world".title()` = `"Hello World"`
    - `.swapcase()` - Toggle case: `"HeLLo".swapcase()` = `"hEllO"`
    
  - **Searching Methods:**
    - `.find(substring)` - Returns index of first occurrence (or -1 if not found)
      - `"hello".find("l")` = `2`
      - `"hello".find("x")` = `-1`
    - `.index(substring)` - Similar to find() but raises error if not found
      - `"hello".index("e")` = `1`
    - `.count(substring)` - Count occurrences
      - `"hello".count("l")` = `2`
    
  - **Manipulation Methods:**
    - `.strip()` - Remove leading/trailing whitespace
      - `"  hello  ".strip()` = `"hello"`
    - `.replace(old, new)` - Replace occurrences
      - `"hello".replace("l", "L")` = `"heLLo"`
    - `.split(separator)` - Split into list
      - `"a,b,c".split(",")` = `['a', 'b', 'c']`
    - `.join(list)` - Join list into string
      - `"-".join(['a', 'b', 'c'])` = `"a-b-c"`
    
  - **Validation Methods:**
    - `.isdigit()` - Check if all characters are digits
      - `"12345".isdigit()` = `True`
      - `"123a5".isdigit()` = `False`
    - `.isalpha()` - Check if all characters are alphabetic
      - `"hello".isalpha()` = `True`
      - `"hello123".isalpha()` = `False`
    - `.isspace()` - Check if all characters are whitespace
      - `"   ".isspace()` = `True`
    - `.startswith(substring)` - Check if starts with
      - `"hello".startswith("he")` = `True`
    - `.endswith(substring)` - Check if ends with
      - `"hello".endswith("lo")` = `True`

- **String Formatting:**
  - Concatenation: `"Hello " + "World"` = `"Hello World"`
  - f-strings (modern way): 
    - `name = "Alice"` 
    - `f"Hello, {name}!"` = `"Hello, Alice!"`
  - format() method: `"Hello, {}!".format(name)`

### ✅ Lists - Ordered Collections
- **List Creation** - Creating lists
  - `numbers = [1, 2, 3, 4, 5]`
  - `mixed = [1, "hello", 3.14, True]`
  - `empty = []`
  - `using_list()` = `list()`

- **List Indexing** - Accessing elements
  - `numbers[0]` = `1` (first element)
  - `numbers[4]` = `5` (fifth element)
  - `numbers[-1]` = `5` (last element)
  - `numbers[-2]` = `4` (second last element)

- **List Slicing** - Extracting sublists
  - `numbers[1:4]` = `[2, 3, 4]`
  - `numbers[:3]` = `[1, 2, 3]`
  - `numbers[2:]` = `[3, 4, 5]`
  - `numbers[::2]` = `[1, 3, 5]` (every 2nd element)
  - `numbers[::-1]` = `[5, 4, 3, 2, 1]` (reversed)

- **List In-Built Methods:**
  - `.append(item)` - Add element at end
    - `numbers.append(6)` → `[1, 2, 3, 4, 5, 6]`
  - `.remove(item)` - Remove first occurrence
    - `numbers.remove(3)` → `[1, 2, 4, 5]`
  - `.pop(index)` - Remove and return element (default: last)
    - `numbers.pop()` removes last element
    - `numbers.pop(0)` removes first element
  - `.reverse()` - Reverse list in place
    - `numbers.reverse()` → `[5, 4, 3, 2, 1]`
  - `.sort()` - Sort in ascending order
    - `[3, 1, 4, 1, 5].sort()` → `[1, 1, 3, 4, 5]`
  - `.count(item)` - Count occurrences
    - `[1, 2, 2, 3].count(2)` = `2`
  - `.index(item)` - Find first index of item
    - `[1, 2, 3].index(2)` = `1`
  - `.insert(index, item)` - Insert at position
    - `numbers.insert(1, 10)` → `[1, 10, 2, 3, 4, 5]`
  - `.clear()` - Remove all elements
    - `numbers.clear()` → `[]`
  - `.extend(list)` - Add multiple elements
    - `numbers.extend([6, 7])` → `[1, 2, 3, 4, 5, 6, 7]`

- **List Operations:**
  - Concatenation: `[1, 2] + [3, 4]` = `[1, 2, 3, 4]`
  - Repetition: `[1, 2] * 3` = `[1, 2, 1, 2, 1, 2]`
  - Membership: `2 in [1, 2, 3]` = `True`

### ✅ Tuples - Immutable Sequences
- **Tuple Creation** - Creating tuples
  - `coordinates = (10, 20)`
  - `single = (5,)` (note comma for single element)
  - `multiple = (1, 2, 3, 4, 5)`
  - `empty = ()`

- **Tuple Indexing** - Accessing elements
  - Same as lists: `coordinates[0]` = `10`
  - Negative indexing: `coordinates[-1]` = `20`

- **Tuple Slicing** - Extracting sub-tuples
  - `(1, 2, 3, 4, 5)[1:3]` = `(2, 3)`
  - `(1, 2, 3)[::2]` = `(1, 3)`

- **Tuple Immutability** - Cannot modify tuples
  - `tuple[0] = 5` causes `TypeError`
  - Cannot add, remove, or modify elements

- **Tuple In-Built Methods:**
  - `.count(item)` - Count occurrences
    - `(1, 2, 2, 3).count(2)` = `2`
  - `.index(item)` - Find index of item
    - `(1, 2, 3).index(2)` = `1`

- **Tuple Unpacking** - Assigning to multiple variables
  - `x, y = (10, 20)`
  - Now `x = 10` and `y = 20`
  - `a, b, c = (1, 2, 3)`

- **Tuple Advantages:**
  - Immutable (safer from accidental changes)
  - Hashable (can be used as dictionary keys)
  - Slightly faster than lists
  - Protect data from modification

### ✅ Loops - Repetitive Execution
#### **for Loop** - Iterate a fixed number of times
- **Basic for loop with range():**
  ```python
  for i in range(5):
      print(i)  # Prints 0, 1, 2, 3, 4
  ```

- **range() variations:**
  - `range(5)` = 0, 1, 2, 3, 4 (0 to 4)
  - `range(1, 5)` = 1, 2, 3, 4 (1 to 4)
  - `range(0, 10, 2)` = 0, 2, 4, 6, 8 (0 to 10 with step 2)
  - `range(10, 0, -1)` = 10, 9, 8...1 (reverse)

- **Iterating over sequences:**
  ```python
  fruits = ['apple', 'banana', 'orange']
  for fruit in fruits:
      print(fruit)
  
  for char in "PYTHON":
      print(char)  # Prints P, Y, T, H, O, N
  ```

- **Loop with index (enumerate):**
  ```python
  for index, fruit in enumerate(fruits):
      print(f"{index}: {fruit}")
  ```

#### **while Loop** - Repeat while condition is true
- **Basic while loop:**
  ```python
  count = 0
  while count < 5:
      print(count)
      count += 1
  ```

- **While with user input:**
  ```python
  while True:
      user_input = input("Enter something (q to quit): ")
      if user_input == 'q':
          break
      print(f"You entered: {user_input}")
  ```

#### **Loop Control Statements**
- **break** - Exit loop prematurely
  ```python
  for i in range(10):
      if i == 5:
          break  # Exits loop when i equals 5
      print(i)  # Prints 0, 1, 2, 3, 4
  ```

- **continue** - Skip current iteration
  ```python
  for i in range(5):
      if i == 2:
          continue  # Skips when i equals 2
      print(i)  # Prints 0, 1, 3, 4
  ```

- **for-else** - Else executes if loop completes normally
  ```python
  for i in range(5):
      if i == 10:
          break
  else:
      print("Loop completed normally")  # This executes
  ```

- **while-else** - Similar behavior with while loops
  ```python
  count = 0
  while count < 5:
      count += 1
  else:
      print("Condition became false")  # Executes when while condition is false
  ```

#### **Nested Loops** - Loops within loops
```python
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})")
```
Output:
```
(0, 0) (0, 1) (0, 2)
(1, 0) (1, 1) (1, 2)
(2, 0) (2, 1) (2, 2)
```

### ✅ Functions - Modular Programming
- **Function Definition** - Creating reusable code blocks
  ```python
  def greet(name):
      print(f"Hello, {name}!")
  ```

- **Function Calling** - Invoking functions
  ```python
  greet("Alice")  # Output: Hello, Alice!
  greet("Bob")    # Output: Hello, Bob!
  ```

- **Parameters and Arguments:**
  - **Parameter** - Variable in function definition
  - **Argument** - Value passed when calling function
  
  ```python
  def add(a, b):  # a, b are parameters
      return a + b
  
  result = add(5, 3)  # 5, 3 are arguments
  ```

- **Multiple Parameters:**
  ```python
  def calculate(a, b, c, d, e):
      return a + b + c + d + e
  
  total = calculate(1, 2, 3, 4, 5)  # Returns 15
  ```

- **Return Statements** - Returning values from functions
  ```python
  def square(x):
      return x * x
  
  result = square(5)  # result = 25
  ```

- **Default Parameters** - Providing default values
  ```python
  def greet(name="Guest"):
      print(f"Hello, {name}!")
  
  greet()           # Output: Hello, Guest!
  greet("Alice")    # Output: Hello, Alice!
  ```

- **Function Best Practices:**
  - Use meaningful function names
  - Keep functions focused (do one thing)
  - Add comments for complex logic
  - Return values instead of printing (for reusability)
  - Use parameters instead of global variables

- **Practical Examples:**
  - **Temperature Converter:**
    ```python
    def celsius_to_fahrenheit(celsius):
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit
    
    temp_f = celsius_to_fahrenheit(25)
    print(f"25°C = {temp_f}°F")
    ```
  
  - **Factorial Calculator:**
    ```python
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
    print(factorial(5))  # Output: 120
    ```

---

## 📚 Topics Covered - Day 2

### ✅ Object-Oriented Programming (OOPs) - Introduction

#### **What is OOPs?**
- Programming paradigm based on objects and classes
- Real-world modeling through code
- Four pillars: Encapsulation, Abstraction, Inheritance, Polymorphism
- We'll cover: **Encapsulation** and **Inheritance** today

---

### ✅ Classes and Objects - Fundamentals

#### **Class Definition** - Creating a blueprint
```python
class Student:
    pass
```

#### **Creating Objects** - Instances of a class
```python
student1 = Student()
student2 = Student()
```

#### **Object Identity**
- Each object is unique with its own memory address
- Multiple objects created from same class are independent

---

### ✅ Encapsulation - Data Hiding and Access Control

#### **What is Encapsulation?**
- Bundling data (attributes) and methods together
- Controlling access to data
- Protecting data from unwanted modifications
- Hiding internal implementation details

#### **Access Modifiers - Three Levels of Access**

##### **1. Public Members (No prefix)**
- Accessible from anywhere: outside class, in other classes
- Syntax: `self.attribute` or `def method():`
- Convention: No underscore prefix

```python
class Student:
    def __init__(self, name, marks):
        self.name = name      # Public attribute
        self.marks = marks    # Public attribute
    
    def display(self):        # Public method
        print(f"Name: {self.name}, Marks: {self.marks}")

# Usage
s1 = Student("Alice", 85)
print(s1.name)        # ✅ Can access directly
s1.display()          # ✅ Can call method
s1.marks = 90         # ✅ Can modify directly
```

##### **2. Protected Members (Single Underscore `_`)**
- Convention for "use with caution" - intended for internal/subclass use
- Not truly protected in Python (no enforcement)
- Syntax: `self._attribute` or `def _method():`
- Used to signal: "This is internal, modify with care"

```python
class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number  # Protected
        self._balance = balance               # Protected
    
    def _validate_amount(self, amount):  # Protected method
        return amount > 0

# Usage
account = BankAccount("12345", 5000)
print(account._balance)      # Can access but shouldn't (convention)
account._balance = 0         # Possible but discouraged
```

##### **3. Private Members (Double Underscore `__`)**
- Name mangling: `__attribute` becomes `_ClassName__attribute`
- Cannot access directly from outside class
- Intended for strict data hiding
- Syntax: `self.__attribute` or `def __method():`

```python
class Account:
    def __init__(self, username, password):
        self.username = username    # Public - OK to access
        self.__password = password  # Private - CANNOT access directly
    
    def change_password(self, old_pwd, new_pwd):
        """Public method to safely change password"""
        if old_pwd == self.__password:
            self.__password = new_pwd
            print("Password changed successfully")
        else:
            print("Old password incorrect")

# Usage
acc = Account("alice", "secret123")
print(acc.username)                    # ✅ OK
# print(acc.__password)                # ❌ AttributeError!

# Name mangling allows access (but don't do this!)
print(acc._Account__password)          # ⚠️ Technically possible, but WRONG

# Use the public method instead
acc.change_password("secret123", "newpass456")  # ✅ Correct way
```

#### **Getter and Setter Methods** - Controlled Access
```python
class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius
    
    # Getter method
    def get_celsius(self):
        return self.__celsius
    
    # Setter method with validation
    def set_celsius(self, temp):
        if isinstance(temp, (int, float)):
            self.__celsius = temp
        else:
            print("Temperature must be a number")
    
    def get_fahrenheit(self):
        return (self.__celsius * 9/5) + 32

# Usage
temp = Temperature(25)
print(temp.get_celsius())              # 25
print(temp.get_fahrenheit())           # 77.0
temp.set_celsius(30)                   # Valid
temp.set_celsius("hot")                # Invalid - prints error
```

#### **Constructor (`__init__`) Method** - Initialization
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__ssn = ""  # Private attribute
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating object (constructor called automatically)
person1 = Person("John", 30)
person1.display_info()
```

#### **Instance Methods** - Operating on object data
```python
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    
    def circumference(self):
        return 2 * 3.14 * self.radius

# Usage
circle = Circle(5)
print(f"Area: {circle.area()}")              # 78.5
print(f"Circumference: {circle.circumference()}")  # 31.4
```

#### **Instance vs Class Attributes**
```python
class Car:
    wheels = 4  # Class attribute (shared by all instances)
    
    def __init__(self, brand, model):
        self.brand = brand      # Instance attribute (unique per object)
        self.model = model      # Instance attribute (unique per object)

# Usage
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

print(car1.brand)          # "Toyota"
print(car2.brand)          # "Honda"
print(Car.wheels)          # 4 (class attribute)
print(car1.wheels)         # 4 (accessible via instance too)
```

---

### ✅ Inheritance - Code Reusability

#### **What is Inheritance?**
- Child class inherits attributes and methods from parent class
- Code reusability and hierarchy
- "is-a" relationship

#### **Single Inheritance** - One parent, one child
```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def sound(self):
        print("Some generic animal sound")

class Dog(Animal):  # Dog inherits from Animal
    def sound(self):  # Method overriding
        print(f"{self.name} barks: Woof! Woof!")

# Usage
dog = Dog("Buddy")
dog.sound()  # Output: Buddy barks: Woof! Woof!
print(dog.name)  # Output: Buddy (inherited attribute)
```

#### **Constructor Chaining with `super()`** - Initializing parent
```python
class Vehicle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    
    def display(self):
        print(f"Vehicle: {self.brand}, Color: {self.color}")

class Car(Vehicle):
    def __init__(self, brand, color, fuel_type):
        super().__init__(brand, color)  # Call parent constructor
        self.fuel_type = fuel_type

# Usage
car = Car("Toyota", "Red", "Petrol")
car.display()  # Output: Vehicle: Toyota, Color: Red
print(car.fuel_type)  # Output: Petrol
```

#### **Method Overriding** - Child redefining parent method
```python
class Shape:
    def area(self):
        print("Calculating area...")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):  # Override parent method
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):  # Override parent method
        return 3.14 * self.radius ** 2

# Usage
rect = Rectangle(5, 4)
print(f"Rectangle area: {rect.area()}")  # 20

circle = Circle(3)
print(f"Circle area: {circle.area()}")   # 28.26
```

#### **Multi-level Inheritance** - Grandparent → Parent → Child
```python
class Animal:
    def __init__(self, name):
        self.name = name

class Mammal(Animal):
    def feed_milk(self):
        print(f"{self.name} feeds milk to offspring")

class Dog(Mammal):
    def bark(self):
        print(f"{self.name} says: Woof!")

# Usage
dog = Dog("Buddy")
print(dog.name)         # Inherited from Animal
dog.feed_milk()         # Inherited from Mammal
dog.bark()              # Own method
```

#### **Multiple Inheritance** - Multiple parents (use with caution)
```python
class Flyer:
    def fly(self):
        print("Flying in the sky")

class Swimmer:
    def swim(self):
        print("Swimming in water")

class Duck(Flyer, Swimmer):
    pass

# Usage
duck = Duck()
duck.fly()    # Inherited from Flyer
duck.swim()   # Inherited from Swimmer
```

#### **Accessing Parent Methods with `super()`**
```python
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        super().greet()  # Call parent's greet()
        print("Hello from Child")

# Usage
child = Child()
child.greet()
# Output:
# Hello from Parent
# Hello from Child
```

---

## 🏆 Practice Questions - Day 1

### 📝 **Installation & Basic Syntax (2+ Questions):**
1. ✅ Setting up Python environment
2. ✅ Writing and running first program
3. ✅ Understanding Python syntax basics

### 📝 **DataTypes & Variables (5+ Questions):**
4. ✅ Identifying data types using `type()`
5. ✅ Creating and manipulating variables
6. ✅ Understanding naming rules for identifiers
7. ✅ Type conversion problems

### 📝 **Operators (6+ Questions):**
8. ✅ Arithmetic operations with different operators
9. ✅ Comparison operators and boolean results
10. ✅ Compound assignment operators
11. ✅ Logical operators with multiple conditions

### 📝 **String Operations (5+ Questions):**
12. ✅ String indexing and slicing
13. ✅ String manipulation using methods
14. ✅ String formatting with f-strings
15. ✅ Email validation using string methods
16. ✅ Text processing and case conversion

### 📝 **Lists Operations (4+ Questions):**
17. ✅ List creation and indexing
18. ✅ List slicing and element access
19. ✅ List methods (append, remove, sort, etc.)
20. ✅ List iteration and manipulation

### 📝 **Tuples & Immutability (2+ Questions):**
21. ✅ Tuple creation and indexing
22. ✅ Understanding immutability
23. ✅ Tuple unpacking

### 📝 **Conditional Statements (5+ Questions):**
24. ✅ if-else conditions
25. ✅ if-elif-else chains
26. ✅ Nested conditions
27. ✅ Multiple condition checking with logical operators

### 📝 **Loops (6+ Questions):**
28. ✅ for loops with range()
29. ✅ while loops and loop control
30. ✅ break and continue statements
31. ✅ Nested loops
32. ✅ for-else and while-else
33. ✅ Iterating over sequences

### 📝 **Functions (5+ Questions):**
34. ✅ Function definition and calling
35. ✅ Parameters and return values
36. ✅ Multiple parameter functions
37. ✅ Mathematical functions (factorial, etc.)
38. ✅ Default parameters

**Total Questions Day 1: 40+** 🎉

---

## 🏆 Practice Questions - Day 2

### 📝 **Classes & Objects (3+ Questions):**
1. ✅ Creating classes and instantiating objects
2. ✅ Instance attributes and methods
3. ✅ Constructor (`__init__`) with parameters

### 📝 **Encapsulation (4+ Questions):**
4. ✅ Public member access
5. ✅ Protected members convention
6. ✅ Private members and name mangling
7. ✅ Getter and Setter methods

### 📝 **Real-World Applications (3+ Questions):**
8. ✅ Student class with methods
9. ✅ BankAccount class with encapsulation
10. ✅ Circle/Shape class calculations

### 📝 **Inheritance (4+ Questions):**
11. ✅ Single inheritance implementation
12. ✅ Constructor chaining with `super()`
13. ✅ Method overriding
14. ✅ Multi-level inheritance

### 📝 **Advanced Concepts (2+ Questions):**
15. ✅ Multiple inheritance
16. ✅ Accessing parent methods

**Total Questions Day 2: 16+** 🎉

---

## 🎓 Self-Study Guide

### 📖 **When Learning DataTypes:**
- **Step 1:** Understand each type with examples
- **Step 2:** Practice type conversion with real data
- **Step 3:** Combine different types in operations
- **Time to Master:** 2-3 hours

### 📖 **When Learning Operators:**
- **Step 1:** Learn each operator category
- **Step 2:** Combine operators in expressions
- **Step 3:** Practice with conditional logic
- **Time to Master:** 2-3 hours

### 📖 **When Learning Strings:**
- **Step 1:** Master indexing and slicing
- **Step 2:** Practice each string method
- **Step 3:** Build string manipulation programs
- **Time to Master:** 3-4 hours

### 📖 **When Learning Lists:**
- **Step 1:** Create and access list elements
- **Step 2:** Learn and practice each method
- **Step 3:** Combine with loops for iteration
- **Time to Master:** 3-4 hours

### 📖 **When Learning Loops:**
- **Step 1:** Understand for and while loops
- **Step 2:** Master break and continue
- **Step 3:** Practice with nested loops and patterns
- **Time to Master:** 3-4 hours

### 📖 **When Learning Functions:**
- **Step 1:** Understand definition and calling
- **Step 2:** Practice parameters and returns
- **Step 3:** Build reusable function libraries
- **Time to Master:** 3-4 hours

### 📖 **When Learning OOPs:**
- **Step 1:** Understand classes and objects
- **Step 2:** Practice encapsulation with examples
- **Step 3:** Implement inheritance hierarchies
- **Time to Master:** 4-5 hours (per day)

---

## 💾 Important Code Patterns

### **Reading and Processing User Input:**
```python
# Single input
name = input("Enter name: ")
age = int(input("Enter age: "))

# Multiple inputs
x = float(input("Enter x: "))
y = float(input("Enter y: "))
print(f"Sum: {x + y}")
```

### **Conditional with String Comparison:**
```python
username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "pass123":
    print("Login successful")
else:
    print("Invalid credentials")
```

### **Loop Pattern - Processing List:**
```python
numbers = [10, 20, 30, 40, 50]

for num in numbers:
    if num > 25:
        print(f"{num} is greater than 25")
```

### **Function Pattern - Calculation:**
```python
def calculate_average(scores):
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)

student_scores = [85, 90, 78, 92]
avg = calculate_average(student_scores)
print(f"Average: {avg}")
```

### **Class Pattern - Student Management:**
```python
class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.__marks = marks
    
    def get_marks(self):
        return self.__marks
    
    def update_marks(self, new_marks):
        if 0 <= new_marks <= 100:
            self.__marks = new_marks
        else:
            print("Invalid marks")

# Usage
student = Student("Raj", 101, 85)
print(student.get_marks())
student.update_marks(92)
```

---

## 📚 Learning Resources

- 📖 **Official Python Documentation:** https://docs.python.org/3/
- 🎥 **Interactive Coding:** Your classroom materials and examples
- 🔗 **Practice Platforms:** [HackerRank](https://www.hackerrank.com/), [CodeChef](https://www.codechef.com/)
- 📚 **Online Tutorials:** W3Schools Python, GeeksforGeeks

---

## 💡 Tips for Success

| Tip | Why It Works |
|:----|:------------|
| **Code Every Day** | Builds muscle memory and intuition |
| **Write Notes** | Reinforces understanding |
| **Practice Problems** | Real application of concepts |
| **Debug Errors** | Learn from mistakes |
| **Ask Questions** | Clarify doubts immediately |
| **Review Daily** | Reinforces memory |
| **Build Projects** | Practical experience |
| **Help Peers** | Teaching strengthens your understanding |

---

## 🎯 What's Next?

After mastering these fundamentals, explore:

- 📚 **More OOPs:** Abstraction, Polymorphism
- 🔄 **Recursion:** Function calling itself
- 📁 **File Handling:** Reading and writing files
- 🗂️ **Data Structures:** Dictionaries, Sets
- 🔧 **Error Handling:** Exception management
- 🎮 **Mini Projects:** Building real applications

---

## 📞 Support & Contact

- **Ask During Class:** Don't hesitate to ask questions
- **Review Materials:** Go through examples multiple times
- **Practice Consistently:** Regular practice is key
- **Participate Actively:** Engage in coding exercises

---

## 📝 Session Notes

### Day 1 Summary:
- ✅ Covered all fundamental data types
- ✅ Learned to work with operators
- ✅ Practiced string and list operations
- ✅ Mastered loops and conditionals
- ✅ Implemented functions for code reusability

### Day 2 Preview:
- 🎨 Introduction to Object-Oriented Programming
- 🔒 Encapsulation for data protection
- 👨‍👩‍👦 Inheritance for code hierarchy
- 🔧 Building real-world applications with classes

---


## 🤝 Need Help?

<div align="center">

### Got stuck? Don't worry!

**💬 Ask Questions** | **🐛 Report Issues** | **💡 Share Ideas**

Remember: *Every expert was once a beginner!*

---

### 🌟 **Keep Coding, Keep Growing!** 🌟

<br>



<div align="center">

### ✨ Created By ✨

## <a href="https://whatsapp.com/channel/0029Vb74kBaL2ATzZBnRka19" target="_blank">✨ **Shine_Beyond_Syntax** ✨</a>

<br>

[![WhatsApp Channel](https://img.shields.io/badge/Join%20My-WhatsApp%20Channel-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://whatsapp.com/channel/0029Vb74kBaL2ATzZBnRka19)

<br>

<p style="font-size: 1.5em; color: #fff; margin: 5px;">
  <em>Empowering D Y Patil School Of Engineering and Management Students to Master Python</em>
</p>

<br>


</div>

---

![Python](https://img.shields.io/badge/Built%20with-Python-blue?style=flat-square&logo=python)
![Learning](https://img.shields.io/badge/Learning-Fundamentals-orange?style=flat-square)
![D Y Patil SEM](https://img.shields.io/badge/D%20Y%20Patil%20SEM-Excellence-green?style=flat-square)
