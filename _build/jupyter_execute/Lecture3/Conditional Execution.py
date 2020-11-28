#!/usr/bin/env python
# coding: utf-8

# # Conditional Execution

# **CS1302 Introduction to Computer Programming**
# ___

# In[1]:


get_ipython().run_line_magic('reload_ext', 'mytutor')


# ## Motivation

# Conditional execution means running different pieces of code based on different conditions. Why?

# For instance, when trying to compute `a/b`, `b` may be `0` and division by `0` is invalid.

# In[2]:


def multiply_or_divide(a, b):
    print('a:{}, b:{}, a*b:{}, a/b:{}'.format(a, b, a * b, a / b))


multiply_or_divide(1, 2)
multiply_or_divide(1, 0)  # multiplication is valid but not shown


# Can we skip only the division but not multiplication when `b` is `0`? 

# In[3]:


def multiply_or_divide(a, b):
    fix = a / b if b else 'undefined'
    print('a:{}, b:{}, a*b:{}, a/b:{}'.format(a, b, a * b, fix))


multiply_or_divide(1, 2)
multiply_or_divide(1, 0)  # multiplication is valid but not shown


# The above solution involve:
# - a *boolean expression* `fix` that checks whether a condition holds, and
# - a *conditional construct* `... if ... else ...` that specify which code block should be executed under what condition. 

# ## Boolean expressions

# ### Comparison Operators

# **How to compare different values?**

# Like the equality and inequality relationships in mathematics,  
# Python also have binary [*comparison/relational operators*](https://docs.python.org/3/reference/expressions.html#comparisons):

# | Expression |  True iff  |
# | ---------: | :--------- |
# |   `x == y` | $x=y$.     |
# |    `x < y` | $x<y$.     |
# |   `x <= y` | $x\leq y$. |
# |    `x > y` | $x>y$.     |
# |   `x >= y` | $x\geq y$. |
# |   `x != y` | $x\neq y$. |

# Explore these operators using the widgets below:

# In[5]:


# Comparisons
from ipywidgets import interact
comparison_operators = ['==','<','<=','>','>=','!=']
@interact(operand1='10',
          operator=comparison_operators,
          operand2='3')
def comparison(operand1,operator,operand2):
    expression = f"{operand1} {operator} {operand2}"
    value = eval(expression)
    print(f"""{'Expression:':>11} {expression}\n{'Value:':>11} {value}\n{'Type:':>11} {type(value)}""")


# - These operators return either `True` or `False`, which are `keywords` of type *boolean*.
# - The expressions are called *boolean expressions* or *predicates*, named after [George Boole](https://en.wikipedia.org/wiki/George_Boole).
# - N.b., the equality operator `==` consists of *two equal signs*, different from the assignment operator `=`.

# **What is the precedence of comparison operators?**

#  All the comparison operators have the [same precedence](https://docs.python.org/3/reference/expressions.html?highlight=precedence#operator-precedence) lower than that of `+` and `-`.

# In[6]:


1 + 2 >= 3  # (1 + 2) >= 3


# Python allows multiple comparison operations to be chained together:

# In[83]:


2.0 == 2>1 #equivalent to (2.0 ==2) and (2>1)


# **What is the associativity?**

# Comparison operations are [*non-associative*](https://en.wikipedia.org/wiki/Operator_associativity#Non-associative_operators):

# In[8]:


(2.0 == 2) > 1, 2.0 == (2 > 1)  # not the same as 2.0 == 2 > 1


# **Errorata** in [Halterman17] due to a misunderstanding of non-associativity vs left-to-right evaluation order:
# 
# - [Halterman17, p.69](https://archive.org/stream/2018Fundamentals.ofPython?ref=ol#page/n79/mode/1up):
#     > The relational operators are binary operators and are all ~left associative~ **non-associative**.
# - [Halterman17, p.50, Table 3.2](https://archive.org/stream/2018Fundamentals.ofPython?ref=ol#page/n60/mode/1up):
#     - `=` should be non-associative instead of right-associative.
#     - The corresponding table in `Lecture2/Expressions and Arithmetic.ipynb` should also be corrected accordingly.

# **Exercise** Explain why the following boolean expressions have different values.

# In[10]:


1 <= 2 < 3 != 4, (1 <= 2) < (3 != 4)


# The second expression is not a chained comparison: 
# - The expressions in the parentheses are evaluated to boolean values first to `True`, and so
# - the overall expression `True < True` is evaluated to `False`.

# **Exercise** The comparison operators can be applied to different data types, as illustrated below.  
# Explain the meaning of the operators in each of the following expressions.

# In[11]:


# Comparisons beyond numbers
@interact(expression=[
    '10 == 10.', '"A" == "A"', '"A" == "A "', '"A" != "a"', 
    '"A" > "a"', '"aBcd" < "abd"', '"A" != 64', '"A" < 64'
])
def relational_expression(expression):
    print(eval(expression))


# 1. Checks whether an integer is equal to a floating point number.
# 1. Checks whether two characters are the same.
# 1. Checks whether two strings are the same. Note the space character.
# 1. Checks whether a character is larger than the order character according to their unicodes.
# 1. Checks whether a string is lexicographically smaller than the other string.
# 1. Checks whether a character is not equal to an integer.
# 1. TypeError because there is no implementation that evaluates whether a string is smaller than an integer.

# **Is `!` the same as the `not` operator?**

# **Errata** There is an error in [Halterman17, p.69](https://archive.org/stream/2018Fundamentals.ofPython?ref=ol#page/n79/mode/1up) due to confusion with C language:  
# > ... `!(x >= 10)` and `!(10 <= x)` are ~equivalent~ **invalid**.
# - We can write `1 != 2` as `not 1 == 2` but not `!(1 == 2)` because
# - `!` is not a logical operator. It is used to call a [system shell command](https://ipython.readthedocs.io/en/stable/interactive/tutorial.html?highlight=system%20call#system-shell-commands) in IPython.

# In[ ]:


get_ipython().system('(1 == 2)')


# In[ ]:


get_ipython().system('ls  # a bash command that lists files in the current directory')


# **How to compare floating point numbers?**

# In[31]:


x = 10
y = (x**(1/3))**3
x == y


# Why False? Shouldn't $(x^{\frac13})^3=x$?

# - Floating point numbers have finite precisions and so  
# - we should instead check whether the numbers are close enough.

# One method of comparing floating point numbers:

# In[32]:


abs(x - y) <= 1e-9


# `abs` is a function that returns the absolute value of its argument. Hence, the above translates to
# 
# $$|x - y| \leq \delta_{\text{abs}}$$ 
# or equivalently 
# 
# $$y-\delta_{\text{abs}} \leq x \leq y+\delta_{\text{abs}} $$
# where $\delta_{\text{abs}}$ is called the *absolute tolerance*. 

# **Is an absolute tolerance of `1e-9` good enough?**

# What if we want to compare `x = 1e10` instead of `10`?

# In[36]:


x = 1e10
y = (x**(1/3))**3
abs(x - y) <= 1e-9


# Floating point numbers "float" at different scales.  
# A better way to use the [`isclose`](https://docs.python.org/3/library/math.html#math.isclose) function from `math` module. 

# In[37]:


import math
math.isclose(x, y)


# **How does it work?**

# `math.isclose(x,y)` implements
# 
# $$ |x - y| \leq \max\{\delta_{\text{rel}} \max\{|x|,|y|\},\delta_{\text{abs}}\}$$
# with the default
# - *relative tolerance* $\delta_{\text{rel}}$ equal to `1e-9`, and
# - absolute tolerance $\delta_{\text{abs}}$ equal to `0.0`.

# **Exercise** Write the boolean expression implemented by `isclose`. You can use the function `max(a,b)` to find the maximum of `a` and `b`. 

# In[28]:


rel_tol, abs_tol = 1e-9, 0.0
x, y = 1e-100, 2e-100
### BEGIN SOLUTION
abs(x-y) <= max(rel_tol * max(abs(x), abs(y)), abs_tol)
### END SOLUTION


# ### Boolean Operations

# Since chained comparisons are non-associative. It follows a different evaluation rule than arithmetical operators.

# E.g., `1 <= 2 < 3 != 4` is evaluated as follows:

# In[38]:


1 <= 2 and 2 < 3 and 3 != 4


# The above is called a *compound boolean expression*, which is formed using the *boolean/logical operator* `and`.

# **Why use boolean operators?**

# What if we want to check whether a number is either $< 0$ or $\geq 100$?  
# Can we achieve this only by chaining the comparison operators or applying the logical `and`?

# In[69]:


# Check if a number is outside a range.
@interact(x='15')
def check_out_of_range(x):
    x_ = float(x)
    is_out_of_range = x_<0 or x_>=100
    print('Out of range [0,100):', is_out_of_range)


# - `and` alone is not [functionally complete](https://en.wikipedia.org/wiki/Functional_completeness),  i.e., not enough to give all possible boolean functions. 
# - In addition to `and`, we can also use `or` and `not`. 

# |   `x`   |   `y`   | `x and y` | `x or y` | `not x` |
# | :-----: | :-----: | :-------: | :------: | :-----: |
# | `True`  | `True`  |  `True`   |  `True`  | `False` |
# | `True`  | `False` |  `False`  |  `True`  | `False` |
# | `False` | `True`  |  `False`  |  `True`  | `True`  |
# | `False` | `False` |  `False`  | `False`  | `True`  |

# The above table is called a *truth table*. It enumerates all possible input and output combinations for each boolean operator. 

# **How are chained logical operators evaluated?  
# What are the precedence and associativity for the logical operators?**

# - All binary boolean operators are left associative.  
# - [Precedence](https://docs.python.org/3/reference/expressions.html?highlight=precedence#operator-precedence): `comparison operators` > `not` > `and` > `or` 
# 
# 
# 
# 

# **Exercise** Explain what the values of the following two compound boolean expressions are:
# - Expression A: `True or False and True`
# - Expression B: `True and False and True`
# - Expression C: `True or True and False`

# - Expression A evaluates to `True` because `and` has higher precedence and so the expression has the same value as `True or (False and True)`.
# - Expression B evaluates to `False` because `and` is left associative and so the expression has the same value as `(True and False) and True`.
# - Expression C evaluates to `True` because `and` has a higher precedence and so the expression has the same value as `True or (True and False)`. Note that `(True or True) and False` evaluates to something `False` instead, so precedence matters.

# Instead of following the precedence and associativity, however, a compound boolean expression uses a [short-circuit evaluation](https://docs.python.org/3/reference/expressions.html?highlight=precedence#boolean-operations).  

# To understand this, we will use the following function to evaluate a boolean expression verbosely.

# In[47]:


def verbose(id,boolean):
    '''Identify evaluated boolean expressions.'''
    print(id,'evaluated:',boolean)
    return boolean


# In[45]:


verbose('A',verbose(1,True) or verbose(2,False) and verbose(3,True))  # True or (False and True)


# **Why expression 2 and 3 are not evaluated?**

# Because True or ... must be True (Why?) so Python does not look further. From the [documentation](https://docs.python.org/3/reference/expressions.html?highlight=precedence#boolean-operations):

# > The expression `x or y` first evaluates `x`; if `x` is true, its value is returned; otherwise, `y` is evaluated and the resulting value is returned.

# Note that:
# - Even though `or` has lower precedence than `and`, it is still evaluated first. 
# - The evaluation order for logical operators is left-to-right.

# In[48]:


verbose('B',verbose(4,True) and verbose(5,False) and verbose(6,True))  # (True and False) and True


# **Why expression 6 is not evaluated?**

# `True and False and ...` must be `False` so Python does not look further.

# > The expression `x and y` first evaluates `x`; if `x` is false, its value is returned; otherwise, `y` is evaluated and the resulting value is returned.

# Indeed, logical operators can even be applied to non-boolean operands. From the [documentation](https://docs.python.org/3/reference/expressions.html?highlight=precedence#boolean-operations):

# > In the context of Boolean operations, and also when expressions are used by control flow statements, the following values are interpreted as false: `False`, None, numeric zero of all types, and empty strings and containers (including strings, tuples, lists, dictionaries, sets and frozensets). All other values are interpreted as true.

# **Exercise** How does the following code work?

# In[50]:


print('You have entered', input() or 'nothing')


# - The code replaces empty user input by the default string `nothing` because empty string is regarded as False in a boolean operation.
# - If user input is non-empty, it is regarded as True in the boolean expression and returned immediately as the value of the boolean operation.

# **Is empty string equal to False?**

# In[92]:


print('Is empty string equal False?',''==False)


# - An empty string is regarded as False in a boolean operation but
# - a *comparison operation is not a boolean operation*, even though it forms a boolean expression.

# ## Conditional Constructs

# Consider writing a program that sorts values in *ascending* order.  
# A *sorting algorithm* refers to the procedure of sorting values in order.  

# ### If-Then Construct

# **How to sort two values?**

# Given two values are stored as `x` and `y`, we want to 
# - `print(x,y)` if `x <= y`, and
# - `print(y,x)` if `y < x`.

# Such a program flow is often represented by a flowchart like the following:

# <img src="https://www.cs.cityu.edu.hk/~ccha23/cs1302/Lecture3/sort_two_values1.svg" style="max-width:300px;" alt="sort_two_values(x,y);
# if(x<=y) {
#   print(x, y)
# }
# if (y<x) {
#   print(y, x)
# }">

# Python provides the [`if` statement](https://docs.python.org/3/reference/compound_stmts.html#the-if-statement) to implement the above [*control flow*](https://en.wikipedia.org/wiki/Control_flow) specified by the diamonds.

# In[52]:


# Sort two values using if statement
def sort_two_values(x, y):
    if x <= y:
        print(x, y)
    if y < x: print(y, x)


@interact(x='1', y='0')
def sort_two_values_app(x, y):
    sort_two_values(eval(x), eval(y))


# We can visualize the execution as follows:

# In[53]:


get_ipython().run_cell_magic('mytutor', '-h 350', 'def sort_two_values(x, y):\n    if x <= y:\n        print(x, y)\n    if y < x: print(y, x)\n        \nsort_two_values(1,0)\nsort_two_values(1,2)')


# Python use indentation to indicate code blocks or *suite*: 
# - `print(x, y)` (Line 5) is indented to the right of `if x <= y:` (Line 4) to indicate it is the body of the if statement.
# - For convenience, `if y < x: print(y, x)` (Line 6) is a one-liner for an `if` statement that only has one line in its block.
# - Both `if` statements (Line 4-6) are indented to the right of `def sort_two_values(x,y):` (Line 3) to indicate that they are part of the body of the function `sort_two_values`.

# **How to indent?**

# - The [style guide](https://www.python.org/dev/peps/pep-0008/#indentation) recommends using 4 spaces for each indentation.  
# - In IPython, you can simply type the `tab` key and IPython will likely enter the correct number of spaces for you.

# **What if you want to leave a block empty?**

# In programming, it is often useful to delay detailed implementations until we have written an overall skeleton.  
# To leave a block empty, Python uses the keyword [`pass`](https://docs.python.org/3/tutorial/controlflow.html#pass-statements).

# In[61]:


# write a code skeleton
def sort_two_values(x, y):
    pass
    # print the smaller value first followed by the larger one
    
sort_two_values(1,0)
sort_two_values(1,2)


# Without `pass`, the code will fail to run, preventing you from checking other parts of the code.

# In[63]:


# You can add more details to the skeleton step-by-step
def sort_two_values(x, y):
    if x <= y:
        pass  
        # print x before y
    if y < x: pass  # print y before x

sort_two_values(1,0)
sort_two_values(1,2)


# ### If-Then-Else Construct

# The sorting algorithm is not efficient enough. Why not?  
# Hint: `(x <= y) and not (y < x)` is a *tautology*, i.e., always true.

# To improve the efficient, we should implement the following program flow.

# <img src="https://www.cs.cityu.edu.hk/~ccha23/cs1302/Lecture3/sort_two_values2.svg" style="max-width:300px;" alt="sort_two_values(x,y);
# if(x<=y) {
#   print(x, y)
# }
# else {
#   print(y, x)
# }">

# This can be down by the `else` clause of the [`if` statement](https://docs.python.org/3/tutorial/controlflow.html#if-statements).

# In[64]:


get_ipython().run_cell_magic('mytutor', '-h 350', 'def sort_two_values(x, y):\n    if x <= y:\n        print(x, y)\n    else:\n        print(y,x)\n        \nsort_two_values(1,0)\nsort_two_values(1,2)')


# We can also use a [*conditional expression*](https://docs.python.org/3/reference/expressions.html#conditional-expressions) to shorten the code.

# In[65]:


def sort_two_values(x, y):
    print(('{0} {1}' if x <= y else '{1} {0}').format(x, y))


@interact(x='1', y='0')
def sort_two_values_app(x, y):
    sort_two_values(eval(x), eval(y))


# **Exercise** Explain why the followings have syntax errors.

# In[ ]:


1 if True


# In[ ]:


x = 1 if True else x = 0 


# A conditional expression must be an expression:
# 1. It must give a value under all cases. To enforce that, `else` keyword must be provided.
# 1. An assignment statement does not return any value and therefore cannot be used for the conditional expression.  
#     `x = 1 if True else 0` is valid because `x =` is not part of the conditional expression.

# ### Nested Conditionals

# Consider sorting three values instead of two. A feasible algorithm is as follows:

# <img src="https://www.cs.cityu.edu.hk/~ccha23/cs1302/Lecture3/sort_three_values1.svg" style="max-width:800px;" alt="sort_three_values(x,y,z);
# if(x<=y<=z) {
#   print(x, y, z)
# } else
# if (x<=z<=y) {
#   print(x, z, y)
# } else
# if (y<=x<=z) {
#   print(y, x, z)
# } else
# if (y<=z<=x) {
#   print(y, z, x)
# } else
# if (z<=x<=y) {
#   print(z, x, y)
# } else {
#   print(z, y, x)
# }">

# We can implement the flow using *nested conditional constructs*:

# In[66]:


def sort_three_values(x, y, z):
    if x <= y <= z:
        print(x, y, z)
    else:
        if x <= z <= y:
            print(x, z, y)
        else:
            if y <= x <= z:
                print(y, x, z)
            else:
                if y <= z <= x:
                    print(y, z, x)
                else:
                    if z <= x <= y:
                        print(z, x, y)
                    else:
                        print(z, y, x)

def test_sort_three_values():
    sort_three_values(0,1,2)
    sort_three_values(0,2,1)
    sort_three_values(1,0,2)
    sort_three_values(1,2,0)
    sort_three_values(2,0,1)
    sort_three_values(2,1,0)

test_sort_three_values()


# Imagine what would happen if we have to sort many values.  
# To avoid an excessively long line due to the indentation, Python provides the `elif` keyword that combines `else` and `if`.

# In[67]:


def sort_three_values(x, y, z):
    if x <= y <= z:
        print(x, y, z)
    elif x <= z <= y:
        print(x, z, y)
    elif y <= x <= z:
        print(y, x, z)
    elif y <= z <= x:
        print(y, z, x)
    elif z <= x <= y:
        print(z, x, y)
    else:
        print(z, y, x)


test_sort_three_values()


# **Exercise** The above sorting algorithm is inefficient because some conditions may be checked more than once.  
# Improve the program to eliminate duplicate checks.  
# *Hint:* Do not use chained comparison operators or compound boolean expressions.

# In[88]:


def sort_three_values(x, y, z):
    if x <= y:
        if y <= z:
            print(x, y, z)
        elif x <= z:
            print(x, z, y)
        else:
            print(z, x, y)
    ### BEGIN SOLUTION
    elif z <= y:
        print(z, y, x)
    elif z <= x:
        print(y, z, x)
    else:
        print(y, x, z)
    ### END SOLUTION
        
sort_three_values(10,17,14)

