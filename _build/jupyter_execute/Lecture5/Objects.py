#!/usr/bin/env python
# coding: utf-8

# # Objects

# **CS1302 Introduction to Computer Programming**
# ___

# In[1]:


get_ipython().run_line_magic('reload_ext', 'mytutor')


# ## Object-Oriented Programming

# **Why object-oriented programming?**

# In[2]:


import jupyter_manim
from manimlib.imports import *


# In[3]:


get_ipython().run_cell_magic('manim', 'HelloWorld -l', "class HelloWorld(Scene):\n    def construct(self):\n        self.play(Write(TextMobject('Hello, World!')))")


#  - `HelloWorld` is a specific `Scene` that is
#  - `construct`ed by `play`ing an animation that `Write`
#  - the `TextMobject` of the message `'Hello, World!'`. 

# **Exercise** Try changing
# - Mobjects: `TextMobject('Hello, World!')` to `TexMobject(r'E=mc^2')` or `Circle()` or `Square()`.
# - Animation objects: `Write` to `FadeIn` or `GrowFromCenter`.
# 
# See the [documentation](https://eulertour.com/docs/) for other choices.

# More complicated behavior can be achieved by using different objects.

# In[4]:


get_ipython().run_cell_magic('html', '', '<iframe width="912" height="513" src="https://www.youtube.com/embed/ENMyFGmq5OA" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')


# **What is an object?**

# Almost everything is an [`object`](https://docs.python.org/3/library/functions.html?highlight=object#object) in Python.

# In[5]:


get_ipython().run_line_magic('pinfo', 'isinstance')
isinstance(1, object), isinstance(1.0, object), isinstance('1', object)


# A function is also a [first-class](https://en.wikipedia.org/wiki/First-class_function) object object.

# In[6]:


isinstance(print, object), isinstance(''.isdigit, object)


# A data type is also an object.

# In[7]:


# chicken and egg relationship
isinstance(type, object), isinstance(object, type), isinstance(object, object)


# Python is a [*class-based* object-oriented programming](https://en.wikipedia.org/wiki/Object-oriented_programming#Class-based_vs_prototype-based) language:  
# - Each object is an instance of a *class* (also called type in Python).
# - An object is a collection of *members/attributes*, each of which is an object.

# In[8]:


get_ipython().run_line_magic('pinfo', 'hasattr')
hasattr(str, 'isdigit')


# Different objects of a class
# - have the same set of attributes as that of the class, but
# - the attribute values can be different.

# In[9]:


get_ipython().run_line_magic('pinfo', 'dir')
dir(1)==dir(int), complex(1, 2).imag != complex(1, 1).imag


# **How to operate on an object?**

# - A class can define a function as an attribute for all its instances.  
# - Such a function is called a *method* or *member function*.

# In[10]:


complex.conjugate(complex(1, 2)), type(complex.conjugate)


# A [method](https://docs.python.org/3/tutorial/classes.html#method-objects) can be accessed by objects of the class:

# In[11]:


complex(1, 2).conjugate(), type(complex(1, 2).conjugate)


# `complex(1,2).conjugate` is a *callable* object:
# - Its attribute `__self__` is assigned to `complex(1,2)`.
# - When called, it passes `__self__` as the first argument to `complex.conjugate`.

# In[12]:


callable(complex(1,2).conjugate), complex(1,2).conjugate.__self__


# ## File Objects

# **How to read a text file?**

# Consider reading a csv (comma separated value) file:

# In[13]:


get_ipython().system("more 'contact.csv'")


# To read the file by a Python program:

# In[14]:


f = open('contact.csv')  # create a file object for reading
print(f.read())   # return the entire content
f.close()         # close the file


# 1. [`open`](https://docs.python.org/3/library/functions.html?highlight=open#open) is a function that creates a file object and assigns it to `f`.
# 1. Associated with the file object, 
#  - [`read`](https://docs.python.org/3/library/io.html#io.TextIOBase.read) returns the entire content of the file as a string.
#  - [`close`](https://docs.python.org/3/library/io.html#io.IOBase.close) flushes and closes the file.

# **Why close a file?**

# If not, depending on the operating system,
# - other programs may not be able to access the file, and
# - changes may not be written to the file.

# To ensure a file is closed properly, we can use the [`with` statement](https://docs.python.org/3/reference/compound_stmts.html#with):

# In[15]:


with open('contact.csv') as f:
    print(f.read())


# The `with` statement applies to any [context manager](https://docs.python.org/3/reference/datamodel.html#context-managers) that provides the methods
# - `__enter__` for initialization, and
# - `__exit__` for finalization.

# In[16]:


with open('contact.csv') as f:
    print(f, hasattr(f, '__enter__'), hasattr(f, '__exit__'), sep='\n')


# - `f.__enter__` is called after the file object is successfully created and assigned to `f`, and
# - `f.__exit__` is called at the end, which closes the file.
# - `f.closed` indicates whether the file is closed.

# In[17]:


f.closed


# We can iterate a file object in a for loop,  
# which implicitly call the method `__iter__` to read a file line by line.

# In[18]:


with open('contact.csv') as f:
    for line in f:
        print(line, end='')

hasattr(f, '__iter__')


# **Exercise** Print only the first 5 lines of the file `contact.csv`.

# In[19]:


with open('contact.csv') as f:
    ### BEGIN SOLUTION
    for i, line in enumerate(f):
        print(line, end='')
        if i >= 5: break
    ### END SOLUTION


# **How to write to a text file?**

# Consider backing up `contact.csv` to a new file:

# In[20]:


destination = 'private/new_contact.csv'


# The directory has to be created first if it does not exist:

# In[21]:


import os
os.makedirs(os.path.dirname(destination), exist_ok=True)


# In[22]:


get_ipython().run_line_magic('pinfo', 'os.makedirs')
get_ipython().system('ls')


# To write to the destination file:

# In[23]:


with open('contact.csv') as source_file:
    with open(destination, 'w') as destination_file:
        destination_file.write(source_file.read())


# In[24]:


get_ipython().run_line_magic('pinfo', 'destination_file.write')
get_ipython().system('more {destination}')


# - The argument `'w'` to `open` sets the file object to write mode.
# - The method `write` writes the input strings to the file.

# **Exercise** We can also use `a` mode to *append* new content to a file.   
# Complete the following code to append `new_data` to the file `destination`.

# In[25]:


new_data = 'Effie, Douglas,galnec@naowdu.tc, (888) 311-9512'
with open(destination, 'a') as f:
    ### BEGIN SOLUTION
    f.write('\n')
    f.write(new_data)
    ### END SOLUTION
get_ipython().system('more {destination}')


# **How to delete a file?**

# Note that the file object does not provide any method to delete the file.  
# Instead, we should use the function `remove` of the `os` module.

# In[26]:


if os.path.exists(destination):
    os.remove(destination)


# ## String Objects

# **How to search for a substring in a string?**

# A string object has the method `find` to search for a substring.  
# E.g., to find the contact information of Tai Ming:

# In[27]:


get_ipython().run_line_magic('pinfo', 'str.find')
with open('contact.csv') as f:
    for line in f:
        if line.find('Tai Ming') != -1:
            record = line
            print(record)
            break


# **How to split and join strings?**

# A string can be split according to a delimiter using the `split` method.

# In[28]:


record.split(',')


# The list of substrings can be joined back together using the `join` methods.

# In[29]:


print('\n'.join(record.split(',')))


# **Exercise** Print only the phone number (last item) in `record`. Use the method `rstrip` or  `strip` to remove unnecessary white spaces at the end.

# In[30]:


get_ipython().run_line_magic('pinfo', 'str.rstrip')
### BEGIN SOLUTION
print(record.split(',')[-1].rstrip())
### END SOLUTION


# **Exercise** Print only the name (first item) in `record` but with
# - surname printed first with all letters in upper case 
# - followed by a comma, a space, and
# - the first name as it is in `record`.
# 
# E.g., `Tai Ming Chan` should be printed as `CHAN, Tai Ming`.  
# 
# *Hint*: Use the methods `upper` and `rsplit` (with the parameter `maxsplit=1`).

# In[31]:


get_ipython().run_line_magic('pinfo', 'str.rsplit')
### BEGIN SOLUTION
first, last = record.split(',')[0].rsplit(' ', maxsplit=1)
print('{}, {}'.format(last.upper(),first))
### END SOLUTION


# ## Operator Overloading

# ### What is overloading?

# Recall that the addition operation `+` behaves differently for different types.

# In[32]:


for x, y in (1, 1), ('1', '1'), (1, '1'):
    print(f'{x!r:^5} + {y!r:^5} = {x+y!r}')


# - Having an operator perform differently based on its argument types is called [operator *overloading*](https://en.wikipedia.org/wiki/Operator_overloading).
# - `+` is called a *generic* operator.
# - We can also have function overloading to create generic functions.

# ### How to dispatch on type?

# The strategy of checking the type for the appropriate implementation is called *dispatching on type*.

# A naive idea is to put all different implementations together with case-by-case checks of operand types.

# In[24]:


def add_case_by_case(x, y):
    if isinstance(x, int) and isinstance(y, int):
        print('Do integer summation...')
    elif isinstance(x, str) and isinstance(y, str):
        print('Do string concatenation...')
    else:
        print('Return a TypeError...')
    return x + y  # replaced by internal implementations


for x, y in (1, 1), ('1', '1'), (1, '1'):
    print(f'{x!r:^10} + {y!r:^10} = {add_case_by_case(x,y)!r}')


# It can get quite messy with all possible types and combinations.

# In[26]:


for x, y in ((1, 1.1), (1, complex(1, 2)), ((1, 2), (1, 2))):
    print(f'{x!r:^10} + {y!r:^10} = {x+y!r}')


# **What about new data types?**

# In[27]:


from fractions import Fraction  # non-built-in type for fractions
for x, y in ((Fraction(1, 2), 1), (1, Fraction(1, 2))):
    print(f'{x} + {y} = {x+y}')


# Weaknesses of the naive approach:
# 1. New data types require rewriting the addition operation.
# 1. A programmer may not know all other types and combinations to rewrite the code properly.

# ### How to have data-directed programming?

# The idea is to treat an implementation as a datum that can be returned by the operand types.

# - `x + y` is a [*syntactic sugar*](https://en.wikipedia.org/wiki/Syntactic_sugar) that
# - invokes the method `type(x).__add__(x,y)` of `type(x)` to do the addition.

# In[28]:


for x, y in (Fraction(1, 2), 1), (1, Fraction(1, 2)):
    print(f'{x} + {y} = {type(x).__add__(x,y)}')  # instead of x + y


# - The first case calls `Fraction.__add__`, which provides a way to add `int` to `Fraction`.
# - The second case calls `int.__add__`, which cannot provide any way of adding `Fraction` to `int`. (Why not?)

# **Why return a [`NotImplemented` object](https://docs.python.org/3.6/library/constants.html#NotImplemented) instead of raising an error/exception?**

# - This allows `+` to continue to handle the addition by
# - dispatching on `Fraction` to call its reverse addition method [`__radd__`](https://docs.python.org/3.6/library/numbers.html#implementing-the-arithmetic-operations).

# In[36]:


get_ipython().run_cell_magic('mytutor', '-h 500', "from fractions import Fraction\ndef add(x, y):\n    '''Simulate the + operator.'''\n    sum = x.__add__(y)\n    if sum is NotImplemented:\n        sum = y.__radd__(x)\n    return sum\n\n\nfor x, y in (Fraction(1, 2), 1), (1, Fraction(1, 2)):\n    print(f'{x} + {y} = {add(x,y)}')")


# The object-oriented programming techniques involved are formally called:
# - [*Polymorphism*](https://en.wikipedia.org/wiki/Polymorphism_(computer_science)): Different types can have different implementations of the `__add__` method.  
# - [*Single dispatch*](https://en.wikipedia.org/wiki/Dynamic_dispatch): The implementation is chosen based on one single type at a time. 

# Remarks:
# - A method with starting and trailing double underscores in its name is called a [*dunder method*](https://dbader.org/blog/meaning-of-underscores-in-python).  
# - Dunder methods are not intended to be called directly. E.g., we normally use `+` instead of `__add__`.
# - [Other operators](https://docs.python.org/3/library/operator.html?highlight=operator) have their corresponding dunder methods that overloads the operator.
# 

# ## Object Aliasing

# **When are two objects identical?**

# - Two objects are the same if they occupy the same memory.  
# - The keyword `is` checks whether two objects are the same object.
# - The function `id` returns a unique id number for each object.

# In[38]:


get_ipython().run_cell_magic('mytutor', '-h 400', "x, y = complex(1,2), complex(1,2)\nz = x\n\nfor expr in 'id(x)', 'id(y)', 'id(z)', 'x == y == z', 'x is y', 'x is z':\n    print(expr,eval(expr))")


# As the box-pointer diagram shows:
# - `x` is not `y` because they point to objects at different memory locations,  
#   even though the objects have the same type and value.
# - `x` is `z` because the assignment `z = x` binds `z` to the same memory location `x` points to.  
#     `z` is said to be an *alias* (another name) of `x`. 

# **Should we use `is` or `==`?**

# `is` is faster but:

# In[39]:


1 is 1, 1 is 1., 1 == 1.


# - `1 is 1.` returns false because `1` is `int` but `1.` is `float`.
# - `==` calls the method `__eq__` of `float` which returns mathematical equivalence.

# *Can we use `is` for integer comparison?*

# In[40]:


x, y = 1234, 1234
1234 is 1234, x is y


# No. The behavior of `is` is not entirely predictable. 

# **When should we use `is`?**

# `is` can be used for [built-in constants](https://docs.python.org/3/library/constants.html#built-in-constants) such as `None` and  `NotImplemented`  
# because there can only be one instance of each of them.
