#!/usr/bin/env python
# coding: utf-8

# # More on Functions

# **CS1302 Introduction to Computer Programming**
# ___

# In[1]:


get_ipython().run_line_magic('reload_ext', 'mytutor')


# ## Recursion

# Consider computing the [Fibonacci number](https://en.wikipedia.org/wiki/Fibonacci_number) of order $n$:
# 
# $$
# F_n := 
# \begin{cases}
# F_{n-1}+F_{n-2} & n>1 \kern1em \text{(recurrence)}\\
# 1 & n=1 \kern1em \text{(base case)}\\
# 0 & n=0 \kern1em \text{(base case)}.
# \end{cases}$$
# Fibonacci numbers have practical applications in generating [pseudorandom numbers](https://en.wikipedia.org/wiki/Lagged_Fibonacci_generator).

# **Can we define the function by calling the function itself?**

# In[2]:


get_ipython().run_cell_magic('mytutor', '-r -h 450', 'def fibonacci(n):\n    if n > 1:\n        return fibonacci(n - 1) + fibonacci(n - 2)  # recursion\n    elif n == 1:\n        return 1\n    else:\n        return 0\n\nfibonacci(2)')


# [*Recursion*](https://en.wikipedia.org/wiki/Recursion_(computer_science)) is a function that calls itself (*recurs*).

# **Exercise** Write a function `gcd` that implements the [Euclidean algorithm for the greatest common divisor](https://en.wikipedia.org/wiki/Euclidean_algorithm): 
# 
# $$\operatorname{gcd}(a,b)=\begin{cases}a & b=0\\ \operatorname{gcd}(b, a\operatorname{mod}b) & \text{otherwise} \end{cases}$$

# In[3]:


get_ipython().run_cell_magic('mytutor', '-r -h 550', 'def gcd(a, b):\n    ### BEGIN SOLUTION\n    return gcd(b, a % b) if b else a\n    ### END SOLUTION\n\n\ngcd(3 * 5, 5 * 7)')


# **Is recursion strictly necessary?**  

# No. We can always convert a recursion to an iteration.  
# E.g., the following computes the Fibonnacci number of order using a while loop instead.

# In[4]:


get_ipython().run_cell_magic('mytutor', '-r -h 550', 'def fibonacci_iteration(n):\n    if n > 1:\n        _, F = 0, 1  # next two Fibonacci numbers\n        while n > 1:\n            _, F, n = F, F + _, n - 1\n        return F\n    elif n == 1:\n        return 1\n    else:\n        return 0\n    \nfibonacci_iteration(3)')


# In[5]:


# more tests
for n in range(5):
    assert fibonacci(n) == fibonacci_iteration(n)


# **Exercise** Implement `gcd_iteration` using a while loop instead of a recursion.

# In[6]:


get_ipython().run_cell_magic('mytutor', '-r -h 550', 'def gcd_iteration(a, b):\n    ### BEGIN SOLUTION\n    while b:\n        a, b = b, a % b\n    return a\n    ### END SOLUTION\n\n\ngcd_iteration(3 * 5, 5 * 7)')


# In[7]:


# test
for n in range(5):
    assert fibonacci(n) == fibonacci_iteration(n)


# **What is the benefit of recursion?**

# - Recursion is often shorter and easier to understand.
# - It is also easier to write code by *wishful thinking* or *[declarative programming](https://en.wikipedia.org/wiki/Declarative_programming)*.

# **Is recusion more efficient than iteration?**

# **Exercise** Find the smallest values of `n` for`fibonacci(n)` and `fibonacci_iteration(n)` respectively to run for more than a second.

# In[8]:


# Assign n
### BEGIN SOLUTION
n = 33
### END SOLUTION
fib_recursion = fibonacci(n)


# In[9]:


# Assign n
### BEGIN SOLUTION
n = 300000
### END SOLUTION
fib_iteration = fibonacci_iteration(n)


# To see why recursion is slow, we will modify `fibonacci` to print each function call as follows.

# In[10]:


def fibonacci(n):
    '''Returns the Fibonacci number of order n.'''
    print('fibonacci({!r})'.format(n))
    return fibonacci(n - 1) + fibonacci(n - 2) if n > 1 else 1 if n == 1 else 0


fibonacci(5)


# `fibonacci(5)` calls `fibonacci(3)` and `fibonacci(4)`, which in turn call `fibonacci(2)` and `fibonacci(3)`. `fibonacci(3)` is called twice.

# ## Global Variables

# Consider the problem of generating a sequence of Fibonacci numbers.

# In[11]:


for n in range(5):
    print(fibonacci_iteration(n))


# **Is the above loop efficient?**

# No. Each call to `fibonacci_iteration(n)` recomputes the last two Fibonacci numbers $F_{n-1}$ and $F_{n-2}$ for $n\geq 2$.

# **How to avoid redundant computations?**

# One way is to store the last two computed Fibonacci numbers.

# In[12]:


get_ipython().run_cell_magic('mytutor', '-h 600', "def next_fibonacci():\n    '''Returns the next Fibonacci number.'''\n    global _Fn, _Fn1, _n  # global declaration\n    value = _Fn\n    _Fn, _Fn1, _n = _Fn1, _Fn + _Fn1, _n + 1\n    return value\n\ndef print_fibonacci_state():\n    print('''States:\n    _Fn  : Next Fibonacci number      = {}\n    _Fn1 : Next next Fibonacci number = {}\n    _n   : Next order                 = {}'''.format(_Fn,_Fn1,_n))\n\n# global variables for next_fibonacci and print_fibonacci_state\n_Fn, _Fn1, _n = 0, 1, 0\n\nfor n in range(5):\n    print(next_fibonacci())\nprint_fibonacci_state()")


# Rules for [*global/local variables*](https://docs.python.org/3/faq/programming.html#what-are-the-rules-for-local-and-global-variables-in-python):
# 1. A local variable must be defined within a function.
# 1. An assignment defines a local variable except in a [`global` statement](https://docs.python.org/3/reference/simple_stmts.html#the-global-statement).

# **Why `global` is NOT needed in `print_fibonacci_state`?**

# Without ambiguity, `_Fn, _Fn1, _n` in `print_fibonacci_state` are not local variables by Rule 1 because they are not defined within the function.

# **Why `global` is needed in `next_fibonacci`?**

# What happens otherwise:

# In[13]:


def next_fibonacci():
    '''Returns the next Fibonacci number.'''
    # global _Fn, _Fn1, _n
    value = _Fn
    _Fn, _Fn1, _n = _Fn1, _Fn + _Fn1, _n + 1
    return value

next_fibonacci()


# Why is there an `UnboundLocalError`?

# - The assignment defines `_Fn` as a local variable by Rule 2.  
# - However, the assignment requires first evaluating `_Fn`, which is not yet defined.

# **Are global variables preferred over local ones?**

# Suppose for aesthetic reasons we remove the underscores in global variable names?

# In[16]:


get_ipython().run_cell_magic('mytutor', '-h 600', "def next_fibonacci():\n    '''Returns the next Fibonacci number.'''\n    global Fn, Fn1, n\n    value = Fn\n    Fn, Fn1, n = Fn1, Fn + Fn1, n + 1\n    return value\n\ndef print_fibonacci_state():\n    print('''States:\n    Fn  : Next Fibonacci number      = {}\n    Fn1 : Next next Fibonacci number = {}\n    n   : Next order                 = {}'''.format(Fn,Fn1,n))\n\n# global variables renamed without underscores\nFn, Fn1, n = 0, 1, 0\n\nn = 0\nwhile n < 5:\n    print(next_fibonacci())\n    n += 1\nprint_fibonacci_state()")


# **Exercise** Why does the while loop prints only 3 instead of 5 Fibonacci numbers?

# There is a name collision. `n` is also incremented by `next_fibonacci()`, and so the while loop is only executed 3 times in total. 

# With global variables
# - codes are less predictable, more difficult to reuse/extend, and
# - tests cannot be isolated, making debugging difficult.

# **Is it possible to store the function states without using global variables?**

# Yes. We can use nested functions and [`nonlocal` variables](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-nonlocal-stmt).

# In[17]:


def fibonacci_closure(Fn, Fn1):
    def next_fibonacci():
        '''Returns the next (generalized) Fibonacci number starting with 
        Fn and Fn1 as the first two numbers.'''
        nonlocal Fn, Fn1, n  # declare nonlocal variables
        value = Fn
        Fn, Fn1, n = Fn1, Fn + Fn1, n + 1
        return value

    def print_fibonacci_state():
        print('''States:
        Next Fibonacci number      = {}
        Next next Fibonacci number = {}
        Next order                 = {}'''.format(Fn, Fn1, n))

    n = 0  # Fn and Fn1 specified in the function arguments
    return next_fibonacci, print_fibonacci_state


next_fibonacci, print_fibonacci_state = fibonacci_closure(0, 1)
n = 0
while n < 5:
    print(next_fibonacci())
    n += 1
print_fibonacci_state()


# The state variables `Fn, Fn1, n` are now *encapsulated*, and so    
# the functions returned by `fibonacci_closure` no longer depends on any global variables.

# Another benefit of using nested functions is that we can also create different Fibonacci sequence with different base cases.

# In[18]:


my_next_fibonacci, my_print_fibonacci_state = fibonacci_closure('cs', '1302')
for n in range(5):
    print(my_next_fibonacci())
my_print_fibonacci_state()


# `next_fibonacci` and `print_fibonacci_state` are *local functions* of `fibonacci_closure`.  
# - They can access (*capture*) the other local variables of `fibonacci_closure` by forming the so-called *closures*.
# - Similar to the use of `global` statement, a [`non-local` statement](https://docs.python.org/3/reference/simple_stmts.html#the-nonlocal-statement) is needed for assigning nonlocal variables.

# Each local function has an attribute named `__closure__` that stores the captured local variables.

# In[19]:


def print_closure(f):
    '''Print the closure of a function.'''
    print('closure of ', f.__name__)
    for cell in f.__closure__:
        print('    {} content: {!r}'.format(cell, cell.cell_contents))


print_closure(next_fibonacci)
print_closure(print_fibonacci_state)


# ## Generator

# Another way to generate a sequence of objects one-by-one is to write a *generator*.

# In[20]:


fibonacci_generator = (fibonacci_iteration(n) for n in range(3))
fibonacci_generator


# The above uses a [*generator expression*](https://docs.python.org/3/reference/expressions.html#grammar-token-generator-expression) to define `fibonacci_generator`.

# **How to obtain items from a generator?**

# We can use the [`next` function](https://docs.python.org/3/library/functions.html#next).

# In[21]:


while True: 
    print(next(fibonacci_generator)) # raises StopIterationException eventually


# A generator object is [*iterable*](https://www.programiz.com/python-programming/iterator), i.e., it implements both `__iter__` and `__next__` methods that are automatically called in a `for` loop as well as the `next` function.

# In[22]:


fibonacci_generator = (fibonacci_iteration(n) for n in range(5))
for fib in fibonacci_generator:  # StopIterationException handled by for loop
    print(fib)


# **Is `fibonacci_generator` efficient?**

# No again due to redundant computations.  
# A better way to define the generator is to use the keyword [`yield`](https://docs.python.org/3/reference/expressions.html?highlight=yield#yield-expressions):

# In[23]:


get_ipython().run_cell_magic('mytutor', '-h 450', "def fibonacci_sequence(Fn, Fn1, stop):\n    '''Return a generator that generates Fibonacci numbers\n    starting from Fn and Fn1 until stop (exclusive).'''\n    while Fn < stop:\n        yield Fn  # return Fn and pause execution\n        Fn, Fn1 = Fn1, Fn1 + Fn\n\n\nfor fib in fibonacci_sequence(0, 1, 5):\n    print(fib)")


# 1. `yield` causes the function to return a *generator* without executing the function body.
# 1. Calling `__next__` resumes the execution, which 
#     - pauses at the next `yield` expression, or
#     - raises the `StopIterationException` at the end.

# **Exercise** The yield expression `yield ...` is mistaken in [Halterman17] to be a statement. It is actually an expression because 
# - The value of a `yield` expression is `None` by default, but 
# - it can be set by the `generator.send` method.
# 
# Add the document string to the following function. In particular, explain the effect of calling the method `send` on the returned generator.

# In[24]:


get_ipython().run_cell_magic('mytutor', '-r -h 500', "def fibonacci_sequence(Fn, Fn1, stop):\n    ### BEGIN SOLUTION\n    '''Return a generator that generates Fibonacci numbers\n    starting from Fn and Fn1 to stop (exclusive). \n    generator.send(value) sets next number to value.'''\n    ### END SOLUTION\n    while Fn < stop:\n        value = yield Fn\n        if value is not None: \n            Fn1 = value  # set next number to the value of yield expression\n        Fn, Fn1 = Fn1, Fn1 + Fn ")


# ## Optional Arguments

# **How to make function arguments optional?**

# In[25]:


def fibonacci_sequence(Fn=0, Fn1=1, stop=None):
    while stop is None or Fn < stop:
        value = yield Fn
        Fn, Fn1 = Fn1, Fn1 + Fn


# In[26]:


for fib in fibonacci_sequence(0,1,5):
    print(fib)  # with all arguments specified


# In[27]:


for fib in fibonacci_sequence(stop=5):
    print(fib)  # with default Fn=0, Fn1=1


# `stop=5` is called a [keyword argument](https://docs.python.org/3/glossary.html#term-keyword-argument). Unlike `positional arguments`, it specifies the name of the argument explicitly.

# **Exercise** `stop` is an [optional argument](https://docs.python.org/3/tutorial/controlflow.html#default-argument-values) with the *default value* `None`. What is the behavior of the following code?

# In[28]:


for fib in fibonacci_sequence(5):
    print(fib)
    if fib > 10:  
        break  # Will this be executed?


# With the default value of `None`, the while loop becomes an infinite loop. The generator will keep generating the next Fibonacci number without any bound on the order. In particular, `fibonacci_sequence(5)` creates an unstoppable (default) generator with base case `Fn=5` (specified) and `Fn1=1` (default).

# Rules for specifying arguments:
# 1. Keyword arguments must be after all positional arguments.
# 1. Duplicate assignments to an argument are not allowed.

# E.g., the following results in error:

# In[29]:


fibonacci_sequence(stop=10, 1)


# In[ ]:


fibonacci_sequence(1, Fn=1)


# The following shows that the behavior of `range` is different.

# In[30]:


for count in range(1, 10, 2):
    print(count, end=' ')  # counts from 1 to 10 in steps of 2
print()
for count in range(1, 10):
    print(count, end=' ')  # default step=1
print()
for count in range(10):
    print(count, end=' ')  # default start=0, step=1
range(stop=10)  # fails


# `range` takes only positional arguments.  
# However, the first positional argument has different intepretations (`start` or `stop`) depending on the number of arguments (2 or 1).

# `range` is indeed NOT a generator.

# In[31]:


print(type(range),type(range(10)))


# ## Variable number of arguments

# We can simulate the behavior of range by having a [variable number of arguments](https://docs.python.org/3.4/tutorial/controlflow.html#arbitrary-argument-lists).

# In[32]:


def print_arguments(*args, **kwargs):
    '''Take any number of arguments and prints them'''
    print('args ({}): {}'.format(type(args),args))
    print('kwargs ({}): {}'.format(type(kwargs),kwargs))

print_arguments(0, 10, 2, start=1, stop=2)
print("{k}".format(greeting="Hello",k=8),"*"  )


# - `args` is a tuple of positional arguments.
# - `kwargs` is a dictionary of keyword arguments.

# `*` and `**` are *unpacking operators* for tuple/list and dictionary respectively:

# In[33]:


args = (0, 10, 2)
kwargs = {'start': 1, 'stop': 2}
print_arguments(*args, **kwargs)


# The following function converts all the arguments to a string.  
# It will be useful later on.

# In[34]:


def argument_string(*args, **kwargs):
    '''Return the string representation of the list of arguments.'''
    return '({})'.format(', '.join([
        *['{!r}'.format(v) for v in args],  # arguments
        *['{}={!r}'.format(k, v)
          for k, v in kwargs.items()]  # keyword arguments
    ]))

argument_string(0, 10, 2, start=1, stop=2)


# **Exercise** Redefine `fibonacci_sequence` so that the positional arguments depend on the number of arguments:

# In[35]:


def fibonacci_sequence(*args):
    '''Return a generator that generates Fibonacci numbers
    starting from Fn and Fn1 to stop (exclusive). 
    generator.send(value) sets next number to value.
    
    fibonacci_sequence(stop)
    fibonacci_sequence(Fn,Fn1)
    fibonacci_sequence(Fn,Fn1,stop)
    '''
    Fn, Fn1, stop = 0, 1, None  # default values

    # handle different number of arguments
    if len(args) is 1:
        ### BEGIN SOLUTION
        stop = args[0]
        ### END SOLUTION
    elif len(args) is 2:
        Fn, Fn1 = args[0], args[1]
    elif len(args) > 2:
        Fn, Fn1, stop = args[0], args[1], args[2]
    
    while stop is None or Fn < stop:
        value = yield Fn
        if value is not None: 
            Fn1 = value  # set next number to the value of yield expression
        Fn, Fn1 = Fn1, Fn1 + Fn


# In[36]:


for fib in fibonacci_sequence(5): # default Fn=0, Fn=1
    print(fib)


# In[37]:


for fib in fibonacci_sequence(1, 2): # default stop=None
    print(fib)  
    if fib>5:
        break


# In[38]:


args = (1, 2, 5)
for fib in fibonacci_sequence(*args): # default stop=None
    print(fib) 


# ## Decorator

# **What is function decoration?**  
# **Why decorate a function?**

# In[39]:


def fibonacci(n):
    '''Returns the Fibonacci number of order n.'''
    global count, depth
    count += 1
    depth += 1
    print('{:>3}: {}fibonacci({!r})'.format(count, '|' * depth, n))
    
    value = fibonacci(n - 1) + fibonacci(n - 2) if n > 1 else 1 if n == 1 else 0
    
    depth -= 1
    if depth is -1:  # recursion done
        print('Done')
        count = 0  # reset count for subsequent recursions
    return value


count, depth = 0, -1
for n in range(6):
    print(fibonacci(n))


# The code decorates the `fibonacci` function by printing each recursive call and the depth of the call stack.  
# The decoration is useful in showing the efficiency of the function, but it rewrites the function definition.

# **How to decorate a function without changing its code?**

# - What if the decorations are temporary and should be removed later?  
# - Go through the source codes of all decorated functions to remove the decorations?  
# - When updating a piece of code, switch back and forth between original and decorated codes?

# What about defining a new function that calls and decorates the original function?

# In[40]:


def fibonacci(n):
    '''Returns the Fibonacci number of order n.'''
    return fibonacci(n - 1) + fibonacci(n - 2) if n > 1 else 1 if n is 1 else 0

def fibonacci_decorated(n):
    '''Returns the Fibonacci number of order n.'''
    global count, depth
    count += 1
    depth += 1
    print('{:>3}: {}fibonacci({!r})'.format(count, '|' * depth, n))
    
    value = fibonacci(n)
    
    depth -= 1
    if depth is -1:  # recursion done
        print('Done')
        count = 0  # reset count for subsequent recursions
    return value


count, depth = 0, -1
for n in range(6):
    print(fibonacci_decorated(n))    


# We want `fibonacci` to call `fibonacci_decorated` instead.  
# What about renaming `fibonacci_decorated` to `fibonacci`?
# 
# ```Python
# fibonacci = fibonacci_decorated
# count, depth = 0, -1
# fibonacci_decorated(10)
# ```
# 
# (If you are faint-hearted, don't run the above code.)

# We want `fibonacci_decorated` to call the original `fibonacci`.

# The solution is to capture the original `fibonacci` in a closure:

# In[41]:


import functools


def print_function_call(f):
    '''Return a decorator that prints function calls.'''
    @functools.wraps(f)  # give wrapper the identity of f and more
    def wrapper(*args, **kwargs):
        nonlocal count, depth
        count += 1
        depth += 1
        call = '{}{}'.format(f.__name__, argument_string(*args, **kwargs))
        print('{:>3}:{}{}'.format(count, '|' * depth, call))

        value = f(*args, **kwargs)  # wrapper calls f

        depth -= 1
        if depth is -1:
            print('Done')
            count = 0
        return value

    count, depth = 0, -1
    return wrapper  # return the decorated function


# `print_function_call` takes in `f` and returns `wrapper`, which captures and decorates `f`:
# - `wrapper` expects the same set of arguments for `f`,  
# - returns the same value returned by `f` on the arguments, but
# - can execute additional codes before and after calling `f` to print the function call.

# By redefining `fibonacci` as the returned `wrapper`, the original `fibonacci` captured by `wrapper` calls `wrapper` as desired.

# In[42]:


def fibonacci(n):
    return fibonacci(n - 1) + fibonacci(n - 2) if n > 1 else 1 if n is 1 else 0


fibonacci = print_function_call(
    fibonacci)  # so original fibonnacci calls wrapper
fibonacci(5)


# The redefinition does not change the original `fibonacci` captured by `wrapper`.

# In[43]:


import inspect
for cell in fibonacci.__closure__:
    if callable(cell.cell_contents):
        print(inspect.getsource(cell.cell_contents))


# Python provides the syntatic sugar below to simplify the redefinition.

# In[44]:


@print_function_call
def fibonacci(n):
    return fibonacci(n - 1) + fibonacci(n - 2) if n > 1 else 1 if n is 1 else 0


fibonacci(5)


# There are many techniques used in the above decorator.

# **Why use a variable number of arguments in `wrapper`**

# To decorate any function with possibly different number of arguments.

# **Why decorate the wrapper with `@functools.wraps(f)`?**

# - Ensures some attributes (such as `__name__`) of the wrapper function is the same as those of `f`.
# - Add useful attributes. E.g., `__wrapped__` stores the original function so we can undo the decoration.
# 

# In[45]:


fibonacci, fibonacci_decorated = fibonacci.__wrapped__, fibonacci  # recover
print('original fibonacci:')
print(fibonacci(5))

fibonacci = fibonacci_decorated  # decorate
print('decorated fibonacci:')
print(fibonacci(5))


# **How to use decorator to improve recursion?**

# We can also use a decorator to make recursion more efficient by caching the return values.  
# `cache` is a dictionary where `cache[n]` stores the computed value of $F_n$ to avoid redundant computations.

# In[46]:


def caching(f):
    '''Return a decorator that caches a function with a single argument.'''
    @functools.wraps(f)
    def wrapper(n):
        if n not in cache:
            cache[n] = f(n)
        else:
            print('read from cache')
        return cache[n]

    cache = {}
    wrapper.clear_cache = lambda : cache.clear()  # add method to clear cache
    return wrapper


@print_function_call
@caching
def fibonacci(n):
    return fibonacci(n - 1) + fibonacci(n - 2) if n > 1 else 1 if n == 1 else 0


# In[47]:


fibonacci(5)
fibonacci(5)
fibonacci.clear_cache()
fibonacci(5)


# A method `clear_cache` is added to the wrapper to clear the cache.   
# `lambda <argument list> : <expression>`is called a [*lambda* expression](https://docs.python.org/3/reference/expressions.html#lambda), which conveniently defines an *anonymous function*.

# In[48]:


type(fibonacci.clear_cache), fibonacci.clear_cache.__name__


# ## Module

# **How to create a module?**

# To create a module, simply put the code in a python source file `<module name>.py` in
# - the current directory, or
# - a python *site-packages* directory in system path.

# In[49]:


import sys
print(sys.path)


# For example, to create a module for generating Fibonacci numbers:

# In[50]:


get_ipython().run_line_magic('more', 'fibonacci.py')


# In[51]:


import fibonacci as fib # as statement shortens name
help(fib)


# In[52]:


print(fib.fibonacci(5))
print(fib.fibonacci_iteration(5))

