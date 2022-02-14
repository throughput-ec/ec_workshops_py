---
type: slides
---

<div><h1><img src="https://github.com/throughput-ec/ec-workshops/blob/main/static/module1/00_ec_slide1.png?raw=true" alt="EC Theme" width=25% align="left"/> Lesson 4<br>Testing</h1></div>

---

## What is Testing?

- Method to check whether the actual software product matches expected requirements
- Ensures that software product is Defect free. 
- It involves execution of software components using manual or automated tools to evaluate properties of interest. 
- The purpose is to identify errors or missing requirements in contrast to actual requirements.

---

## Types of Testing

- Unit testing  
    - Tests whether an individual component of a piece of software works as expected.

- Integration testing  
    - Tests whether separate components of a piece of software, which depend upon eachother, work together as expected.

- Regression testing
    - Tests that recent changes do not break older features.

---

## Unit Testing

How can we be so sure that the code we wrote is doing what we want it to?

Does our code work 100% of the time?

- The answer is: units tests.

- In Python unit tests can be implemented using assert statements although there are other ways.

- Let’s first discuss the syntax of an assert statement and then how they can be applied to the bigger concept, which is unit tests.

---

## Assert Statements

``` python
assert 1 == 2 , "1 is not equal to 2."
```

``` out
AssertionError: 1 is not equal to 2.

Detailed traceback: 
  File "<string>", line 1, in <module>
```

---

`assert` statements can be used as sanity checks for our program.

We implement them as a “debugging” tactic to make sure our code runs as
we expect it to.

When Python reaches an `assert` statement, it evaluates the condition to
a Boolean value.

If the statement is `True`, Python will continue to run. However, if the
Boolean is `False`, the code stops running, and an error message is
printed.


---

## Example 1

Let’s take a look at an example where the Boolean is `True`.

``` python
assert 1 == 1 , "1 is not equal to 1."
print('Will this line execute?')
```

What do you think the output will be?

---

Answer: 

```out
Will this line execute?
```

Here, since the `assert` statement results in a `True` values, Python
continues to run, and the next line of code is executed.

---

## Example 2

``` python
assert 1 == 2 , "1 is not equal to 2."
print('Will this line execute?')
```

What do you think the output will be?

---

Answer: 

``` out
AssertionError: 1 is not equal to 2.

Detailed traceback: 
  File "<string>", line 1, in <module>
```


When an assert is thrown due to a Boolean evaluating to `False`, the
next line of code does not get an opportunity to be executed.

---

## When to test?


- You probably are used to creating a function, and only after that,  you might want to write the tests.

- Actually, writing tests should be done *before* the actual function. This is called Test-Driven Development.

- This may seem a little counter-intuitive, but we’re creating the  expectations of our function before the actual function code.

- Often we have an idea of what our function should be able to do and what output is expected.

- Writing tests before the function, help understand what code is needed and it avoids encountering large bugs down the line.

- It is recommended to write multiple tests.

---

## What to test?

- Keep these tests simple - things that we know are true or
could be easily calculated by hand.

For example, let’s look at our `exponent_a_list()` function.

Easy cases for this function would be lists containing numbers that we
can easily square or cube.

For example, we expect the square output of `[1, 2, 4, 7]` to be
`[1, 4, 16, 49]`.

---

``` python
def exponent_a_list(numerical_list, exponent=2):
    new_exponent_list = list()
    
    for number in numerical_list:
        new_exponent_list.append(number ** exponent)
    
    return new_exponent_list
```

``` python
assert exponent_a_list([1, 2, 4, 7], 2) == [1, 4, 16, 49], "incorrect output for exponent = 2"
```

``` python
assert exponent_a_list([1, 2, 3], 3) == [1, 8, 27], "incorrect output for exponent = 3"
```

``` python
assert type(exponent_a_list([1,2,4], 2)) == list, "output type not a list"
```

---

## Systematic Approach

We use a **systematic approach** to design our function using a general
set of steps to follow when writing programs.

***1. Write the function stub: a function that does nothing but accepts
all input parameters and returns the correct datatype.***

``` python
def exponent_a_list(numerical_list, exponent=2):
    return list()
```

---

***2. Write tests to satisfy the design specifications.***

``` python
def exponent_a_list(numerical_list, exponent=2):
    return list()
   
assert type(exponent_a_list([1,2,4], 2)) == list, "output type not a list"
assert exponent_a_list([1, 2, 4, 7], 2) == [1, 4, 16, 49], "incorrect output for exponent = 2"
assert exponent_a_list([1, 2, 3], 3) == [1, 8, 27], "incorrect output for exponent = 3"
```

``` out
AssertionError: incorrect output for exponent = 2

Detailed traceback: 
  File "<string>", line 1, in <module>
```

---

***3. Outline the program with pseudo-code.***

``` python
def exponent_a_list(numerical_list, exponent=2):

    # create a new empty list
    # loop through all the elements in numerical_list
    # for each element calculate element ** exponent
    # append it to the new list 
    
    return list()
    
assert type(exponent_a_list([1,2,4], 2)) == list, "output type not a list"
assert exponent_a_list([1, 2, 4, 7], 2) == [1, 4, 16, 49], "incorrect output for exponent = 2"
assert exponent_a_list([1, 2, 3], 3) == [1, 8, 27], "incorrect output for exponent = 3"
```

``` out
AssertionError: incorrect output for exponent = 2

Detailed traceback: 
  File "<string>", line 1, in <module>
```

---

***4. Write code and test frequently.***

``` python
def exponent_a_list(numerical_list, exponent=2):
    new_exponent_list = list()
    
    for number in numerical_list:
        new_exponent_list.append(number ** exponent)
    
    return new_exponent_list
    
assert type(exponent_a_list([1,2,4], 2)) == list, "output type not a list"
assert exponent_a_list([1, 2, 4, 7], 2) == [1, 4, 16, 49], "incorrect output for exponent = 2"
assert exponent_a_list([1, 2, 3], 3) == [1, 8, 27], "incorrect output for exponent = 3"
```

---

***5. Write documentation.***

``` python
def exponent_a_list(numerical_list, exponent=2):
    """ Creates a new list containing specified exponential values of the input list. 
    
    Parameters
    ----------
    numerical_list : list
        The list from which to calculate exponential values from
    exponent : int or float, optional
        The exponent value (the default is 2, which implies the square).
    
    Returns
    -------
    new_exponent_list : list
        A new list containing the exponential value specified of each of
        the elements from the input list 
        
    Examples
    --------
    >>> exponent_a_list([1, 2, 3, 4])
    [1, 4, 9, 16]
    """
    new_exponent_list = list()
    for number in numerical_list:
        new_exponent_list.append(number ** exponent)
    return new_exponent_list
```

--- 

## Organizing tests

Tests are organised hierarchically: expectations are grouped into tests which are organised in files:

An expectation is the atom of testing:
- It describes the expected result of a computation. Examples:
    - Does it have the right value and right class? 
    - Does it produce error messages when it should? 
    
A test groups together multiple expectations to test the output from a simple function.
This is why they are sometimes called unit as they test one unit of functionality. 

---

## Tools for Testing

There are automated tools we can take advantage of: 
- `pytest` and `asssert` for Python
- `testthat` for R

---

# Let's practice what we learned!
