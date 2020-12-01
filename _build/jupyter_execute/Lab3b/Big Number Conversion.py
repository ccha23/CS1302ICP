#!/usr/bin/env python
# coding: utf-8

# # Big Number Conversion

# **CS1302 Introduction to Computer Programming**
# ___

# ## Conversion to Decimal

# In this notebook, we will use iterations to convert numbers with arbitrary size.

# ### Binary-to-Decimal

# In a previous lab, we considered converting a byte string to decimal.  
# What about converting a binary string of arbitrary length to decimal?

# Given a binary string of an arbitrarily length $k$,
# 
# $$ 
# b_{k-1}\circ \dots \circ b_1\circ b_0,
# $$
# the decimal number can be computed by the formula
# 
# $$
# 2^0 \cdot b_0 + 2^1 \cdot b_1 + \dots + 2^{k-1} \cdot b_{k-1}.
# $$

# In mathematics, we use the summation notation to write the above formula:
# 
# $$ 
# \sum_{i=0}^{k-1} 2^i \cdot b_{i}.
# $$

# In a program, the formula can be implemented as a for loop:

# ```Python
# def binary_to_decimal(binary_str):
#     k = len(binary_str)
#     decimal = 0                                     # initialization
#     for i in range(k):
#         decimal += 2**i * int(binary_str[(k-1)-i])  # iteration
#     return decimal
# ```

# Note that $b_i$ is given by `binary_str[(k-1)-i]`:
# 
# $$
# \begin{array}{c|c:c:c:c|}\texttt{binary_str} & b_{k-1} & b_{k-2} & \dots & b_0\\ \text{indexing} & [0] & [1] & \dots & [k-1] \end{array}
# $$

# The following is another way to write the for loop.

# ```Python
# def binary_to_decimal(binary_str):
#     decimal = 0                                # initialization
#     for bit in binary_str:
#         decimal = decimal * 2 + int(bit)       # iteration
#     return decimal
# ```

# The algorithm implements the same formula factorized as follows:
# 
# $$
# \begin{aligned} \sum_{i=0}^{k-1} 2^i \cdot b_{i} 
# &=  \left(\sum_{i=1}^{k-1} 2^i \cdot b_{i}\right) + b_0\\
# &=  \left(\sum_{i=1}^{k-1} 2^{i-1} \cdot b_{i}\right)\times 2 + b_0 \\
# &=  \left(\sum_{j=0}^{k-2} 2^{j} \cdot b_{j+1}\right)\times 2 + b_0 && \text{with $j=i-1$} \\
# &= \underbrace{(\dots (\underbrace{(\underbrace{\overbrace{0}^{\text{initialization}\kern-2em}\times 2 + b_{k-1}}_{\text{first iteration} }) \times 2 + b_{k-2}}_{\text{second iteration} }) \dots )\times 2 + b_0}_{\text{last iteration} }.\end{aligned}
# $$ 

# **Exercise** Complete the code for `binary_to_decimal` with the most efficient implementation you can think of.  
# (You can choose one of the two implementations above but take the time to type in the code instead of copy-and-paste.)

# In[ ]:


def binary_to_decimal(binary_str):
    # YOUR CODE HERE
    raise NotImplementedError()
    return decimal


# In[ ]:


# tests
import numpy as np
def test_binary_to_decimal(decimal, binary_str):
    decimal_ = binary_to_decimal(binary_str)
    correct = isinstance(decimal_, int) and decimal_ == decimal
    if not correct:
        print(f'{binary_str} should give {decimal} not {decimal_}.')
    assert correct

test_binary_to_decimal(0, '0')
test_binary_to_decimal(255, '11111111')
test_binary_to_decimal(52154, '1100101110111010')
test_binary_to_decimal(3430, '110101100110')


# In[ ]:


# binary-to-decimal converter
from ipywidgets import interact
bits = ['0', '1']
@interact(binary_str='1011')
def convert_byte_to_decimal(binary_str):
    for bit in binary_str:
        if bit not in bits:
            print('Not a binary string.')
            break
    else:
        print('decimal:', binary_to_decimal(binary_str))


# ### Undecimal-to-Decimal

# A base-11 number system is called an [undecimal system](https://en.wikipedia.org/wiki/Undecimal). The digits range from 0 to 10 with 10 denoted as X:
# 
# $$
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, X.
# $$
# 
# The [International Standard Book Number (ISBN)](https://en.wikipedia.org/wiki/International_Standard_Book_Number) uses an undecimal digit.

# **Exercise** In the following code, assign to `decimal` the integer represented by an undecimal string of arbitrary length.  

# *Hint:* Write a conditional to 
# 1. check if a digit is (capital) `'X'`, and if so, 
# 2. convert the digit to the integer value 10.

# In[ ]:


def undecimal_to_decimal(undecimal_str):
    # YOUR CODE HERE
    raise NotImplementedError()
    return decimal


# In[ ]:


# tests
def test_undecimal_to_decimal(decimal, undecimal_str):
    decimal_ = undecimal_to_decimal(undecimal_str)
    correct = isinstance(decimal_, int) and decimal_ == decimal
    if not correct:
        print(f'{undecimal_str} should give {decimal} not {decimal_}.')
    assert correct


test_undecimal_to_decimal(27558279079916281, '6662X0X584839464')
test_undecimal_to_decimal(23022771839270, '73769X2556695')
test_undecimal_to_decimal(161804347284488, '476129248X2067')


# In[ ]:


# undecimal-to-decimal calculator
from ipywidgets import interact
undecimal_digits = [str(i) for i in range(10)] + ['X']
@interact(undecimal_str='X')
def convert_undecimal_to_decimal(undecimal_str):
    for digit in undecimal_str:
        if digit not in undecimal_digits:
            print('Not an undecimal string.')
            break
    else:
        print('decimal:', undecimal_to_decimal(undecimal_str))


# ## Conversion from Decimal

# Consider the reverse process that converts a non-negative decimal number of arbitrary size to a string representation in another number system.

# ### Decimal-to-Binary

# The following code converts a decimal number to a binary string.

# ```Python
# def decimal_to_binary(decimal):
#     binary_str = str(decimal % 2)
#     while decimal // 2:
#         decimal //= 2
#         binary_str = str(decimal % 2) + binary_str
#     return binary_str
# ```

# To understand the while loop, consider the same formula before, where the braces indicate the value of `decimal` at different times:
# 
# $$
# \begin{aligned} \sum_{i=0}^{k-1} 2^i \cdot b_{i} &=  \left(\sum_{i=0}^{k-2} 2^{i-2} \cdot b_{i-1}\right)\times 2 + b_0 \\
# &= \underbrace{(\underbrace{ \dots (\underbrace{(0\times 2 + b_{k-1}) \times 2 + b_{k-2}}_{\text{right before the last iteration} }  )\times 2 \dots + b_1}_{\text{right before the second iteration} })\times 2 + b_0}_{\text{right before the first iteration} }.\end{aligned}
# $$ 

# - $b_0$ is the remainder `decimal % 2` right before the first iteration,
# - $b_1$ is the remainder `decimal // 2 % 2` right before the second iteration, and
# - $b_{k-1}$ is the remainder `decimal // 2 % 2` right before the last iteration.

# We can also write a for loop instead of a while loop:

# In[ ]:


from math import floor, log2
def decimal_to_binary(decimal):
    binary_str = ''
    num_bits = 1 + (decimal and floor(log2(decimal)))
    for i in range(num_bits):
        binary_str = str(decimal % 2) + binary_str
        decimal //= 2
    return binary_str


# In[ ]:


# decimal-to-binary calculator
@interact(decimal='11')
def convert_decimal_to_binary(decimal):
    if not decimal.isdigit():
        print('Not a non-negative integer.')
    else:
        print('binary:', decimal_to_binary(int(decimal)))


# **Exercise** Explain what the expression `1 + (decimal and floor(log2(decimal)))` calculates. In particular, explain the purpose of the logical `and` operation in the expression?

# YOUR ANSWER HERE

# ### Decimal-to-Undecimal

# **Exercise** Assign to `undecimal_str` the undecimal string that represents a non-negative integer `decimal` of any size.

# *Hint:* For loop or while loop?

# In[ ]:


def decimal_to_undecimal(decimal):
    # YOUR CODE HERE
    raise NotImplementedError()
    return undecimal_str


# In[ ]:


# tests
def test_decimal_to_undecimal(undecimal,decimal):
    undecimal_ = decimal_to_undecimal(decimal)
    correct = isinstance(undecimal, str) and undecimal == undecimal_
    if not correct:
        print(
            f'{decimal} should be represented as the undecimal string {undecimal}, not {undecimal_}.'
        )
    assert correct

test_decimal_to_undecimal('X', 10)
test_decimal_to_undecimal('0', 0)
test_decimal_to_undecimal('1752572309X478', 57983478668530)


# In[ ]:


# undecimal-to-decimal calculator
from ipywidgets import interact
@interact(decimal='10')
def convert_decimal_to_undecimal(decimal):
    if not decimal.isdigit():
        print('Not a non-negative integer.')
    else:
        print('undecimal:', decimal_to_undecimal(int(decimal)))

