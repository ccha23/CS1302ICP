#!/usr/bin/env python
# coding: utf-8

# # Writing Function

# **CS1302 Introduction to Computer Programming**
# ___

# In[1]:


get_ipython().run_line_magic('reload_ext', 'mytutor')


# ## Function Definition

# **How to write a function?**

# A function is defined using the [`def` keyword](https://docs.python.org/3/reference/compound_stmts.html#def):

# The following is a simple function that prints "Hello, World!".

# In[2]:


# Function definition
def say_hello():
    print('Hello, World!')


# In[3]:


# Function invocation
say_hello()


# To make a function more powerful and solve different problems,  
# we can 
# - use a [return statement](https://docs.python.org/3/reference/simple_stmts.html#the-return-statement) to return a value that
# - depends on some input arguments.

# In[4]:


def increment(x):
    return x + 1


increment(3)


# We can also have multiple input arguments.

# In[5]:


def length_of_hypotenuse(a, b):
    if a >= 0 and b >= 0:
        return (a**2 + b**2)**0.5
    else:
        print('Input arguments must be non-negative.')


# In[6]:


length_of_hypotenuse(3, 4)


# In[7]:


length_of_hypotenuse(-3, 4)


# ## Documentation

# **How to document a function?**

# In[8]:


# Author: John Doe
# Last modified: 2020-09-14
def increment(x):
    '''The function takes in a value x and returns the increment x + 1.
    
    It is a simple example that demonstrates the idea of
    - parameter passing, 
    - return statement, and 
    - function documentation.'''
    return x + 1  # + operation is used and may fail for 'str'


# The `help` command shows the docstring we write 
# - at beginning of the function body
# - delimited using triple single/double quotes. 

# In[9]:


help(increment)


# The docstring should contain the *usage guide*, i.e., information for new users to call the function properly.  
# There is a Python style guide (PEP 257) for
# - [one-line docstrings](https://www.python.org/dev/peps/pep-0257/#one-line-docstrings) and
# - [multi-line docstrings](https://www.python.org/dev/peps/pep-0257/#multi-line-docstrings).

# **Why doesn't `help` show the comments that start with `#`?**

# ```Python
# # Author: John Doe
# # Last modified: 2020-09-14
# def increment(x):
#     ...
#     return x + 1  # + operation is used and may fail for 'str'
# ```

# Those comments are not usage guide. They are intended for programmers who need to maintain/extend the function definition.

# - Information about the author and modification date facilitate communications among programmers.
# - Comments within the code help explain important and not-so-obvious implementation details.

# **How to let user know the data types of input arguments and return value?**

# We can [annotate](https://docs.python.org/3/library/typing.html) the function with *hints* of the types of the arguments and return value.

# In[10]:


# Author: John Doe
# Last modified: 2020-09-14
def increment(x: float) -> float:
    '''The function takes in a value x and returns the increment x + 1.
    
    It is a simple example that demonstrates the idea of
    - parameter passing, 
    - return statement, and 
    - function documentation.'''
    return x + 1  # + operation is used and may fail for 'str'


help(increment)


# The above annotations is not enforced by the Python interpreter.  
# Nevertheless, such annotations make the code easier to understand and can be used by editor with type-checking tools.

# In[11]:


def increment_user_input():
    return increment(input())  # does not raise error even though input returns str


# In[12]:


increment_user_input()  # still lead to runtime error


# ## Parameter Passing

# **Can we increment a variable instead of returning its increment?**

# In[13]:


def increment(x):
    x += 1


# In[14]:


x = 3
increment(x)
print(x)  # 4?


# Does the above code increment `x`?

# In[15]:


get_ipython().run_cell_magic('mytutor', '-h 350', 'def increment(x):\n    x += 1\n\n\nx = 3\nincrement(x)\nprint(x)')


# - Step 3: The function `increment` is invoked with the argument evaluated to the value of `x`.
# - Step 3-4: A local frame is created for variables local to `increment` during its execution.    
#     - The *formal parameter* `x` in `def increment(x):` becomes a local variable and
#     - it is assigned the value `3` of the *actual parameter* given by the global variable `x`.
# - Step 5-6: The local (but not the global) variable `x` is incremented.
# - Step 6-7: The function call completes and the local frame is removed.
