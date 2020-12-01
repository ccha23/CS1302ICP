#!/usr/bin/env python
# coding: utf-8

# # Using Functions

# **CS1302 Introduction to Computer Programming**
# ___

# In[1]:


get_ipython().run_line_magic('reload_ext', 'mytutor')


# ## Motivation

# **How to reuse code so we can write less?**

# When we write a loop, the code is executed multiple times, once for each iteration.

# This is a simple form of *code reuse* that 
# - gives your code an elegant *structure* that
# - can be executed efficiently by a computer, and
# - *interpreted* easily by a programmer.

# **How to repeat execution at different times, in different programs, and in slightly different ways?**

# ## Functions

# **How to calculate the logarithm?**

# There is no arithmetic operator for logarithm.  
# Do we have to implement it ourselves?

# We can use the function `log` from the [`math` *module*](https://docs.python.org/3/library/math.html):

# In[2]:


from math import log
log(256, 2)  # log base 2 of 256


# The above computes the base-$2$ logarithm, $\log_2(256)$. Like functions in mathematics, a computer function `log` 
# - is *called/invoked* with some input *arguments* `(256, 2)` following the function, and
# - *returns* an output value computed from the input arguments.

# In[3]:


# A function is callable while an integer is not
callable(log), callable(1)


# Unlike mathematical functions:
# - A computer function may require no arguments, but we still need to call it with `()`. 

# In[4]:


input()


# - A computer function may have side effects and return `None`.

# In[5]:


x = print()
print(x, 'of type', type(x))


# An argument of a function call can be any expression.

# In[6]:


print('1st input:', input(), '2nd input', input())


# Note also that
# - the argument can also be a function call like function composition in mathematics. 
# - Before a function call is executed, its arguments are evaluated first from left to right.

# **Why not implement logarithm yourself?**

# - The function from standard library is efficiently implemented and thoroughly tested/documented.
# - Knowing what a function does is often insufficient for an efficient implementation.  
#     (See [how to calculate logarithm](https://en.wikipedia.org/wiki/Logarithm#Calculation) as an example.)

# Indeed, the `math` library does not implement `log` itself:
# > **CPython implementation detail:** The `math` module consists mostly of thin *wrappers* around the platform C math library functions. - [pydoc last paragraph](https://docs.python.org/3/library/math.html)
# 
# (See the [source code wrapper for `log`](https://github.com/python/cpython/blob/457d4e97de0369bc786e363cb53c7ef3276fdfcd/Modules/mathmodule.c#L731).) 

# **Exercise** What is a function in programming?

# - A function is a structure that allows a piece of code to be reused in a program.  
# - A function can adapt its computations to different situations using input arguments.  

# ## Import Functions from Modules

# **How to import functions?**

# We can use the [`import` statement](https://docs.python.org/3/reference/simple_stmts.html#import) to import multiple functions into the program *global frame*.

# In[7]:


get_ipython().run_cell_magic('mytutor', '-h 300', "from math import log10, ceil\nx = 1234\nprint('Number of digits of x:', ceil(log10(x)))")


# The above import both the functions `log10` and `ceil` from `math` to compute the number $\lceil \log_{10}(x)\rceil$ of digits of a *strictly positive* integer $x$.

# **How to import all functions from a library?**

# In[8]:


get_ipython().run_cell_magic('mytutor', '-h 300', "from math import *  # import all except names starting with an underscore\nprint('{:.2f}, {:.2f}, {:.2f}'.format(sin(pi / 6), cos(pi / 3), tan(pi / 4)))")


# The above uses the wildcard `*` to import ([nearly](https://docs.python.org/3/tutorial/modules.html#more-on-modules)) all the functions/variables provided in `math`.

# **What if different packages define the same function?**

# In[9]:


get_ipython().run_cell_magic('mytutor', '-h 300', "print('{}'.format(pow(-1, 2)))\nprint('{:.2f}'.format(pow(-1, 1 / 2)))\nfrom math import *\nprint('{}'.format(pow(-1, 2)))\nprint('{:.2f}'.format(pow(-1, 1 / 2)))")


# - The function `pow` imported from `math` overwrites the built-in function `pow`.  
# - Unlike the built-in function, `pow` from `math` returns only floats but not integers nor complex numbers. 
# - We say that the import statement *polluted the namespace of the global frame* and caused a *name collision*. 

# **How to avoid name collisions?**

# In[10]:


get_ipython().run_cell_magic('mytutor', '-h 250', "import math\nprint('{:.2f}, {:.2f}'.format(math.pow(-1, 2), pow(-1, 1 / 2)))")


# We can use the full name (*fully-qualified name*) `math.pow` prefixed with the module name (and possibly package names containing the module).

# **Can we shorten a name?**

# The name of a library can be very long and there can be a hierarchical structure as well.  
# E.g., to plot a sequence using `pyplot` module from `matplotlib` package:

# In[11]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot
matplotlib.pyplot.stem([4, 3, 2, 1])
matplotlib.pyplot.ylabel(r'$x_n$')
matplotlib.pyplot.xlabel(r'$n$')
matplotlib.pyplot.title('A sequence of numbers')
matplotlib.pyplot.show()


# It is common to rename `matplotlib.pyplot` as `plt`:

# In[12]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
plt.stem([4, 3, 2, 1])
plt.ylabel(r'$x_n$')
plt.xlabel(r'$n$')
plt.title('A sequence of numbers')
plt.show()


# We can also rename a function as we import it to avoid name collision:

# In[13]:


from math import pow as fpow
fpow(2, 2), pow(2, 2)


# **Exercise** What is wrong with the following code?

# In[14]:


import math as m
for m in range(5): m.pow(m, 2)


# There is a name collision: `m` is assigned to an integer in the for loop and so it is no longer the module `math` when calling `m.pow`.

# **Exercise** Use the `randint` function from `random` to simulate the rolling of a die, by printing a random integer from 1 to 6. 

# In[15]:


import random
print(random.randint(1, 6))


# ## Built-in Functions

# **How to learn more about a function such as `randint`?**

# There is a built-in function `help` for showing the *docstring* (documentation string). 

# In[16]:


import random
help(random.randint)  # random must be imported before


# In[17]:


help(random)  # can also show the docstring of a module


# In[18]:


help(help)


# **Does built-in functions belong to a module?**

# Indeed, every function must come from a module.

# In[19]:


__builtin__.print('I am from the __builtin__ module.')


# `__builtin__` module is automatically loaded because it provides functions that are commonly use for all programs.

# **How to list everything in a module?** 

# We can use the built-in function `dir` (*directory*).

# In[20]:


dir(__builtin__)


# We can also call `dir` without arguments.  
# What does it print?

# In[21]:


dir()

