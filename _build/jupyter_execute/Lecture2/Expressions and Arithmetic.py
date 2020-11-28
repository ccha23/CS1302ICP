#!/usr/bin/env python
# coding: utf-8

# # Expressions and Arithmetic

# **CS1302 Introduction to Computer Programming**
# ___

# ## Operators

# The followings are common operators you can use to form an expression in Python:

# | Operator  |   Operation    | Example |
# | --------: | :------------- | :-----: |
# | unary `-` | Negation       |  `-y`   |
# |       `+` | Addition       | `x + y` |
# |       `-` | Subtraction    | `x - y` |
# |       `*` | Multiplication |  `x*y`  |
# |       `/` | Division       |  `x/y`  |

# - `x` and `y` in the examples are called the *left and right operands* respectively.
# - The first operator is a *unary operator*, which operates on just one operand.   
#     (`+` can also be used as a unary operator, but that is not useful.)
# - All other operators are *binary operators*, which operate on two operands.

# Python also supports some more operators such as the followings:

# | Operator |    Operation     | Example |
# | -------: | :--------------- | :-----: |
# |     `//` | Integer division | `x//y`  |
# |      `%` | Modulo           |  `x%y`  |
# |     `**` | Exponentiation   | `x**y`  |

# In[1]:


# ipywidgets to demonstrate the operations of binary operators
from ipywidgets import interact
binary_operators = {'+':' + ','-':' - ','*':'*','/':'/','//':'//','%':'%','**':'**'}
@interact(operand1=r'10',
          operator=binary_operators,
          operand2=r'3')
def binary_operation(operand1,operator,operand2):
    expression = f"{operand1}{operator}{operand2}"
    value = eval(expression)
    print(f"""{'Expression:':>11} {expression}\n{'Value:':>11} {value}\n{'Type:':>11} {type(value)}""")


# **Exercise** What is the difference between `/` and `//`?

# - `/` is the usual division, and so `10/3` returns the floating-point number $3.\dot{3}$.
# - `//` is integer division, and so `10//3` gives the integer quotient 3.

# **What does the modulo operator `%` do?**

# You can think of it as computing the remainder, but the [truth](https://docs.python.org/3/reference/expressions.html#binary-arithmetic-operations) is more complicated than required for the course.

# **Exercise** What does `'abc' * 3` mean? What about `10 * 'a'`?

# - The first expression means concatenating `'abc'` three times.
# - The second means concatenating `'a'` ten times.

# **Exercise** How can you change the default operands (`10` and `3`) for different operators so that the overall expression has type `float`.  
# Do you need to change all the operands to `float`?

# - `/` already returns a `float`.
# - For all other operators, changing at least one of the operands to `float` will return a `float`.

# ## Operator Precedence and Associativity

# An expression can consist of a sequence of operations performed in a row such as `x + y*z`.

# **How to determine which operation should be performed first?**

# Like arithmetics, the order of operations is decided based on the following rules applied sequentially: 
# 1. *grouping* by parentheses: inner grouping first
# 1. operator *precedence/priority*: higher precedence first
# 1. operator *associativity*:
#     - left associativity: left operand first
#     - right associativity: right operand first

# **What are the operator precedence and associativity?**

# The following table gives a concise summary:

# |    Operators     | Associativity |
# | :--------------- | :-----------: |
# | `**`             |     right     |
# | `-` (unary)      |     right     |
# | `*`,`/`,`//`,`%` |     left      |
# | `+`,`-`          |     left      |

# **Exercise** Play with the following widget to understand the precedence and associativity of different operators.  
# In particular, explain whether the expression `-10 ** 2*3` gives $(-10)^{2\times 3}= 10^6 = 1000000$.

# In[2]:


from ipywidgets import fixed
@interact(operator1={'None':'','unary -':'-'},
          operand1=fixed(r'10'),
          operator2=binary_operators,
          operand2=fixed(r'2'),
          operator3=binary_operators,
          operand3=fixed(r'3')
          )
def three_operators(operator1,operand1,operator2,operand2,operator3,operand3):
    expression = f"{operator1}{operand1}{operator2}{operand2}{operator3}{operand3}"
    value = eval(expression)
    print(f"""{'Expression:':>11} {expression}\n{'Value:':>11} {value}\n{'Type:':>11} {type(value)}""")


# The expression evaluates to $(-(10^2))\times 3=-300$ instead because the exponentiation operator `**` has higher precedence than both the multiplication `*` and the negation operators `-`.

# **Exercise** To avoid confusion in the order of operations, we should follow the [style guide](https://www.python.org/dev/peps/pep-0008/#other-recommendations) when writing expression.  
# What is the proper way to write `-10 ** 2*3`? 

# In[3]:


print(-10**2 * 3)  # can use use code-prettify extension to fix incorrect styles
print((-10)**2 * 3)


# ## Augmented Assignment Operators

# - For convenience, Python defines the [augmented assignment operators](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-augmented-assignment-stmt) such as `+=`, where  
# - `x += 1` means `x = x + 1`.

# The following widgets demonstrate other augmented assignment operators.

# In[4]:


from ipywidgets import interact, fixed
@interact(initial_value=fixed(r'10'),
          operator=['+=','-=','*=','/=','//=','%=','**='],
          operand=fixed(r'2'))
def binary_operation(initial_value,operator,operand):
    assignment = f"x = {initial_value}\nx {operator} {operand}"
    _locals = {}
    exec(assignment,None,_locals)
    print(f"""Assignments:\n{assignment:>10}\nx: {_locals['x']} ({type(_locals['x'])})""")


# **Exercise** Can we create an expression using (augmented) assignment operators? Try running the code to see the effect.

# In[5]:


3*(x = 15)


# Assignment operators are used in assignment statements, which are not expressions because they cannot be evaluated.
