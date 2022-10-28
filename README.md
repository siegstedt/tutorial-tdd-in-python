# Tutorial: Test Driven Development in Python

In this exercises, we will implement the function convert_to_int() using Test Driven Development (TDD). In TDD, we write the tests first and implement the function later.

## Organise the test cases

Using pytest, it is recommended to integrate a **tests directory** at the same level as your package's directory. Below is the directory tree we will set up.

```bash
.
├── src
│   ├── __init__.py
│   └── converters.py
└── tests
    ├── __init__.py
    └── test_converters.py
```

There's a top level directory called src, which holds all application code. For now, it only captures the converters.py module.

Inside that module, we will store a placeholder for the function we want to create.

```python
# src/converters.py

def convert_to_int():
    pass
```

The tests are stored in the folder called tests. pytest will now automatically find all test scripts stored in this directory.

**Test scripts** are to be defined with the prefix "test_". In each script, we organise our tests in test classes and test functions.

**Test functions** represent a test case. Within a test script, test functions can either stand alone or be a subset of test classes. When setting up a larger number of test cases, or test functions, we recommend to group them under test classes.

**Test classes** are simple containers for tests of a specific function. Test classes are a great means of organising test cases as they allow to collect multiple test cases for a given function.

The name of the class should be in CamelCase, and should always start with “Test”. The best way to name a test class is to follow the “Test” with the name of the function. In our case, we will put all tests of convert_to_int in the test class TestConvertToInt.

The \_\_init\_\_.py in the tests folders allow pytest to correctly fetch all tests across the tests folder. Please note that each subfolder inside requires a \_\_init\_\_.py file.

```python
# tests/test_converters.py
from  src.converters import convert_to_int


class TestConvertToInt(object):
    def test_dummy(self):
        pass

```

## Define the normal test arguments first

Normal arguments for convert_to_int() are integer strings with comma as thousand separators. Since the best practice is to test a function for two to three normal arguments, here are three examples with no comma, one comma and two commas respectively.

| Argument value | Expected return value |
| - | - |
| "756" | 756 |
| "2,081" | 2081 |
| "1,034,891" | 1034891 |

Since the convert_to_int() function does not process anything yet, any test will result in an error. But we will use it in the tests anyway. That's how TDD works.

```python
# tests/test_converters.py
from src.converters import convert_to_int


class TestConvertToInt(object):
    def test_with_no_comma(self):
        expected = 756
        actual = convert_to_int("756")
        message = f"Expected: {expected}, Actual: {actual}"
        assert actual == expected, message
        
    def test_with_one_comma(self):
        expected = 2081
        actual = convert_to_int("2,081")
        message = f"Expected: {expected}, Actual: {actual}"
        assert actual == expected, message
    def test_with_two_commas(self):    
        expected = 1034891
        actual = convert_to_int("1,034,891")
        message = f"Expected: {expected}, Actual: {actual}"
        assert actual == expected, message
```

## Implement basic functionality

Now, we can go ahead and try ourselves in implementing this basic functionality.

We expect a string value that includes some digits and commas. We want to split up the string by the commas. Then, we join the separate parts and convert the string into an integer.

```python
# src/converters.py
def convert_to_int(integer_string_with_commas: str) -> int:
    comma_separated_parts = integer_string_with_commas.split(",")
    integer_string_with_commas = "".join(comma_separated_parts)
    return int(integer_string_with_commas)

```

To check, whether our implementation works according to the defined requirements, we simply run the test cases.

```bash
pytest
```

This command will run all tests that pytest can retrieve from the tests folder.

## Next, define special test arguments

What should convert_to_int() do if the arguments are not normal? An essential part of working towards a good test coverage, we want to write tests for special and bad arguments.

In particular, there are three special argument types:

1. Arguments that are missing a comma e.g. "178100,301".
2. Arguments that have the comma in the wrong place e.g. "12,72,891".
3. Float valued strings e.g. "23,816.92".

Let's assume the team agrees to implement the function in a way that convert_to_int() should return None for every special argument and there are no bad arguments for this function.

```python
# tests/test_converters.py
from src.converters import convert_to_int


class TestConvertToInt(object):
    # 
    # add these cases to the existing stack of test cases
    #
     
    def test_on_string_with_missing_comma(self):
        actual = convert_to_int("178100,301")
        message = f"Expected: None, Actual: {actual}"
        assert actual is None, message
    
    def test_on_string_with_incorrectly_placed_comma(self):
        actual = convert_to_int("12,72,891")
        message = f"Expected: None, Actual: {actual}"
        assert actual is None, message
    
    def test_on_float_valued_string(self):
        actual = convert_to_int("23,816.92")
        message = f"Expected: None, Actual: {actual}"
        assert actual is None, message
```  

## Final touch up for the function

Since we have extended our test cases, while our function remained rather basic, running pytest will throw us errors again.

Now, we will refine the function until it stops failing. Let's remind ourselves of the requirements for which convert_to_int() returns a None value.

1. Arguments with missing thousands comma e.g. "178100,301". If we split the string at the comma using "178100,301".split(","), then the resulting list ["178100", "301"] will have at least one entry with length greater than 3 e.g. "178100".
2. Arguments with incorrectly placed comma e.g. "12,72,891". If we split this at the comma, then the resulting list is ["12", "72", "891"]. Note that the first entry is allowed to have any length between 1 and 3. But if any other entry has a length other than 3, like "72", then there's an incorrectly placed comma.
3. Float valued strings e.g. "23,816.92". If you remove the commas and call int() on this string i.e. int("23816.92"), you will get a ValueError.

An example of an implementation can be found below.

```python
def convert_to_int(integer_string_with_commas):
    comma_separated_parts = integer_string_with_commas.split(",")
    for i in range(len(comma_separated_parts)):
        if len(comma_separated_parts[i]) > 3:
            return None
        if i != 0 and len(comma_separated_parts[i]) != 3:
            return None
    
    integer_string_without_commas = "".join(comma_separated_parts)
    try:
        return int(integer_string_without_commas)
    except ValueError:
        return None
```

While implementing your function, continue checking whether your function meets all test cases.

You can continue to run all tests with the pytest terminal command. Yet, a faster and more flexible way to do this is by using keyword expressions. To run tests using keyword expressions, use the -k option. This option takes a quoted string containing a pattern as the value.

```bash
pytest -k test_on_float_valued_string
```

In this example, pytest will parse through our test cases and only run the test classes or functions that are named similar to given strings, e.g. the test function test_on_float_valued_string.

## Wrap up

That's it! Well done!
