- [Python Exceptions](#python-exceptions)
  - [Syntax Errors](#syntax-errors)
- [Exceptions](#exceptions)
  - [Handling Exceptions](#handling-exceptions)
  - [Raising Exceptions](#raising-exceptions)
- [Built-in Types](#built-in-types)
  - [Sequence Types](#sequence-types)
    - [Lists](#lists)
    - [Tuples](#tuples)
    - [Ranges](#ranges)
  - [Set Types](#set-types)
  - [Mapping Types](#mapping-types)
    - [dict](#dict)
    - [Dictionery View Objects](#dictionery-view-objects)
  - [Text Sequence Types Str](#text-sequence-types-str)
    - [String Methods](#string-methods)
    - [`printf-style` String Formatting](#printf-style-string-formatting)
- [Numbers in python](#numbers-in-python)
  - [Integers](#integers)
  - [Floating-Point Numbers](#floating-point-numbers)
  - [Mathematical Functions](#mathematical-functions)
  - [Displaying Numbers](#displaying-numbers)

## Python Exceptions

**Kinds of errors**:
*syntex errors* and *exceptions*

### Syntax Errors

```python
# example: missing colon
while True print('print world')
```

## Exceptions

> Errors detected during execution and are not unconditionally fatal

```shell
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

[Built in exceptions][builtInEx]


[builtInEx]: https://docs.python.org/3/library/exceptions.html#bltin-exceptions

### Handling Exceptions

```python
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
```

*Unhandled exceptions* stops execution

- A try statement may have more than one except clause
- At most one handler will be executed

```python
# naming multiple exceptions as a parenthesized tuple
except (RuntimeError, TypeError, NameError):
    pass
```

> A class in an except clause is compatible with an exception if it is the same class or a base class thereof (but not the other way around — an except clause listing a derived class is not compatible with a base class)

`BaseException` - mother of all exceptions

```python
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise #  re-raise the exception (allowing a caller to handle the exception as well)
```

`else` clause: runs only if the try clause does not raise an exception

```python

try:
     raise Exception('spam', 'eggs')
except Exception as inst:
     print(type(inst))    # the exception instance
     print(inst.args)     # arguments stored in .args
     print(inst)          # __str__ allows args to be printed directly,
                          # but may be overridden in exception subclasses
     x, y = inst.args     # unpack args
     print('x =', x)
     print('y =', y)

# <class 'Exception'>
# ('spam', 'eggs')
# ('spam', 'eggs')
# x = spam
# y = eggs
```

> If an exception has arguments, they are printed as the last part (‘detail’) of the message for unhandled exceptions.

### Raising Exceptions

use the `raise` keyword


--- 

## Built-in Types

### Sequence Types

#### [Lists][Lists]

[Lists]: https://docs.python.org/3.10/library/stdtypes.html#lists
#### [Tuples][Tuples]

> Immutable Suquences. Tuples are also used for cases where an immutable sequence of homogeneous data is needed (such as allowing storage in a set or dict instance).

**Constructing Tuples**

1. Using a pair of parentheses to denote the empty tuple: `()`
2. Using a trailing comma for a singleton tuple: `a`, or `(a,)`
3. Separating items with commas: `a, b, c` or `(a, b, c)`
4. Using the `tuple()` built-in: `tuple()` or `tuple(iterable)`
    For example, `tuple('abc')` returns `('a', 'b', 'c')`


[Tuples]: https://docs.python.org/3.10/library/stdtypes.html#tuples

#### [Ranges][Ranges]

**Constructors**
`range(stop)`, 
`range(start = 0, stop[, step = 1])`

Range implement the `collections.abc.Sequence` ABC

> The arguments to the range constructor must be integers (either built-in int or any object that implements the `__index__()` special method).

```python

>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(1, 11))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> list(range(0, 30, 5))
[0, 5, 10, 15, 20, 25]
>>> list(range(0, 10, 3))
[0, 3, 6, 9]
>>> list(range(0, -10, -1))
[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
>>> list(range(0))
[]
>>> list(range(1, 0))
[]
```
> The advantage of the range type over a regular list or tuple is that a range object will always take the same (small) amount of memory, no matter the size of the range it represents (as it only stores the start, stop and step values, calculating individual items and subranges as needed)

```python shell
>>> r = range(0, 20, 2)
>>> r
range(0, 20, 2)
>>> 11 in r
False
>>> 10 in r
True
>>> r.index(10)
5
>>> r[5]
10
>>> r[:5]
range(0, 10, 2)
>>> r[-1]
18
```
> Testing range objects for equality with == and != _compares them as sequences_. That is, two range objects are considered equal if they represent the same sequence of values. (Note that two range objects that compare equal might have different start, stop and step attributes, for example range(0) == range(2, 1, 3) or range(0, 3, 2) == range(0, 4, 2).)

[Ranges]: https://docs.python.org/3.10/library/stdtypes.html#ranges

### [Set Types][SetTypes]

[SetTypes]: https://docs.python.org/3.10/library/stdtypes.html#set

### Mapping Types

#### [dict][mappingdict]

creating dictioneries

1. Use a comma-separated list of key: value pairs within braces: `{'jack': 4098, 'sjoerd': 4127} or {4098: 'jack', 4127: 'sjoerd'}`

2. Use a dict comprehension: `{}`, `{x: x ** 2 for x in range(10)}`

3. Use the type constructor: `dict()`, `dict([('foo', 100), ('bar', 200)]), dict(foo=100, bar=200)`


```python
#  following examples all return a dictionary equal to {"one": 1, "two": 2, "three": 3}:

a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
f = dict({'one': 1, 'three': 3}, two=2)

a == b == c == d == e == f # return True

```

**Operators that dictioneries support**

`list(d)`, `len(d)`, `d[key]` for more check the docs

[mappingdict]: https://docs.python.org/3.10/library/stdtypes.html#dict

#### [Dictionery View Objects][dicView]

> The objects returned by `dict.keys()`, `dict.values()` and `dict.items()` are view objects. They provide a dynamic view on the dictionary’s entries, which means that when the dictionary changes, the view reflects these changes.

Dictionary views can be iterated over to yield their respective data, and support membership tests:


[dicView]: https://docs.python.org/3.10/library/stdtypes.html#dictionary-view-objects

### [Text Sequence Types Str][TStypes]

1. Immutable sequence of unicode
2. Constructor: `str(object = '')` , `str(object=b'', encoding='utf-8', errors='strict')`

```python

# Can be written in a variety of ways
single_quotes = 'allows embedded "double" quotes'
double_quotes = "allows embedded 'single' quotes"
triple_quoted = '''Three single quotes'''# or """Three double quotes""", may span multiple lines
```

> String literals that are part of a single expression and have only whitespace between them will be implicitly converted to a single string literal. That is, ("spam " "eggs") == "spam eggs".

See **[String literals][strLiteral]** for more.


#### [String Methods][strMethods]

link to the docs provided

#### [`printf-style` String Formatting][strPrintf]

<mark>read again</mark>

[ref](https://realpython.com/python-string-formatting/)

`%`: string _formatting_ or _interpolation operator_ => similar to using `System.out.printf()` in java


```python
print('%(language)s has %(number)03d quote types.' %
      {'language': "Python", "number": 2})
# output: Python has 002 quote types.

'Hey {name}, there is a 0x{errno:x} error!'.format( # the `:x' converts it to a Signed hexadecimal (lowercase).
    name=name, errno=errno)
# output: 'Hey Bob, there is a 0xbadc0ffee error!'

def greet(name, question):
    return f"Hello, {name}! How's it {question}?"

greet('Bob', 'going')
# output: "Hello, Bob! How's it going?"
```

```python
from string import Template
t = Template('Hey, $name!') # we need to import the Template class from Python’s built-in string module
t.substitute(name=name)
# output: 'Hey, Bob!'
```


[TStypes]: https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
[strLiteral]: https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals
[strMethods]: https://docs.python.org/3/library/stdtypes.html#string-methods
[strPrintf]: https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting


## [Numbers in python][Numbers]

[Real Python][RPythonNumbers]

### Integers

```python
>>> int("1")
1

>>> type(1)
<class 'int'>

>>> 1_000_000
1000000

```

There's is no limit to how large an integer may be in python.

### Floating-Point Numbers

**float**: number with a decimal  place `1.0`, `-1.4`


```python

>>> type(1.0)
<class 'float'>

>>> float("1.25")
1.25

>>> 1_000_000.0
1000000.0 

>>> 1e6 #  1e6 is equivalent to 1×10⁶.
1000000.0

>>> 2e400
inf
# inf stands for infinity, and it just means that the number you’ve tried 
# to create is beyond the maximum floating-point value allowed on your computer

```

> Unlike integers, floats do have a maximum size. The maximum floating-point number depends on your system, but something like 2e400 ought to be well beyond most machines’ capabilities.


### [Mathematical Functions][MathsFunctions]
link to docs included. Also check out out real python.

- [Mathematical functions for complex numbers][mfuncComplex]
- [Generate pseudo random numbers][genRandomNum]
- [Mathematical statistics functions][mathStatsFunc]


### Displaying Numbers

[Format spec][FormatSpec]

```python
>>> n = 7.125
>>> f"The value of n is {n:.2f}"
'The value of n is 7.12'

# The colon (:) after the variable n indicates that everything after it is
# part of the formatting specification. In this example, the formatting 
# specification is .2f.

# The .2 in .2f rounds the number to two decimal places, and the f tells
# Python to display n as a fixed-point number. This means that the number is
# displayed with exactly two decimal places, even if the original number has
# fewer decimal places.
```

[FormatSpec]: https://docs.python.org/3/library/string.html#format-specification-mini-language
[mathStatsFunc]: https://docs.python.org/3/library/statistics.html
[genRandomNum]: https://docs.python.org/3/library/random.html
[mfuncComplex]: https://docs.python.org/3/library/cmath.html
[Numbers]: https://docs.python.org/3/library/numeric.html
[RPythonNumbers]: https://realpython.com/python-numbers/#:~:text=Python%20has%20three%20built%2Din,numbers%20in%20a%20later%20section.
[MathsFunctions]: https://docs.python.org/3/library/math.html