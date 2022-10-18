# Python NOTES


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