#!/usr/bin/env python
# coding: utf-8

# # Values and Variables

# **CS1302 Introduction to Computer Programming**
# ___

# In[1]:


get_ipython().run_line_magic('reload_ext', 'mytutor')


# ## Integers

# **How to enter an [integer](https://docs.python.org/3/reference/lexical_analysis.html#integer-literals) in a program?**

# In[2]:


15  # an integer in decimal


# In[3]:


0b1111  # a binary number


# In[4]:


0xF  # hexadecimal (base 16) with possible digits 0, 1,2,3,4,5,6,7,8,9,A,B,C,D,E,F


# **Why all outputs are the same?**

# - What you have entered are *integer literals*, which are integers written out literally. 
# - All the literals have the same integer value in decimal.
# - By default, if the last line of a code cell has a value, the jupyter notebook (*IPython*) will store and display the value as an output. 

# In[5]:


3  # not the output of this cell
4 + 5 + 6


# - The last line above also has the same value, `15`.
# - It is an *expression* (but not a literal) that *evaluates* to the integer value.

# **Exercise** Enter an expression that evaluates to an integer value, as big as possible.  
# (You may need to interrupt the kernel if the expression takes too long to evaluate.)

# In[6]:


# There is no maximum for an integer for Python3. 
# See https://docs.python.org/3.1/whatsnew/3.0.html#integers
11 ** 100000


# ## Strings

# **How to enter a [string](https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals) in a program?**

# In[7]:


'\U0001f600: I am a string.'  # a sequence of characters delimited by single quotes.


# In[8]:


"\N{grinning face}: I am a string."  # delimited by double quotes.


# In[9]:


"""\N{grinning face}: I am a string."""  # delimited by triple single/double quotes.


# - `\` is called the *escape symbol*.  
# - `\U0001f600` and `\N{grinning face}` are *escape sequences*.  
# - These sequences represent the same grinning face emoji by its Unicode in hexadecimal and its name.

# **Why use different quotes?**

# In[10]:


print('I\'m line #1.\nI\'m line #2.')  # \n is a control code for line feed
print("I'm line #3.\nI'm line #4.")  # no need to escape single quote.
print('''I'm line #5.
I'm line #6.''')  # multi-line string


# Note that:
# - The escape sequence `\n` does not represent any symbol.  
# - It is a *control code* that creates a new line when printing the string.  
# - Another common control code is `\t` for tab.

# Using double quotes, we need not escape the single quote in `I'm`.  

# Triple quotes delimit a multi-line string, so there is no need to use `\n`.  
# (You can copy and paste a multi-line string from elsewhere.)

# In programming, there are often many ways to do the same thing.  
# The following is a one-line code ([one-liner](https://en.wikipedia.org/wiki/One-liner_program)) that prints multiple lines of strings without using `\n`:

# In[11]:


print("I'm line #1", "I'm line #2", "I'm line #3", sep='\n')  # one liner


# - `sep='\n'` is a *keyword argument* that specifies the separator of the list of strings.
# - By default, `sep=' '`, a single space character.

# In IPython, we can get the *docstring* (documentation) of a function conveniently using the symbol `?`.

# In[12]:


get_ipython().run_line_magic('pinfo', 'print')


# In[13]:


get_ipython().run_line_magic('pinfo', 'print')


# **Exercise** Print a cool multi-line string below.

# In[14]:


print('''
 (ง •̀_•́)ง 
 ╰(●’◡’●)╮ 
 (..•˘_˘•..)
 (づ￣ 3￣)づ
''')
# See also https://github.com/glamp/bashplotlib
# Star Wars via Telnet http://asciimation.co.nz/


# ## Variables and Assignment

# It is useful to store a value and retrieve it later.  
# To do so, we assign the value to a variable:

# In[15]:


x = 15
x  # output the value of x


# **Is assignment the same as equality?**

# No because:
# - you cannot write `15 = x`, but
# - you can write `x = x + 1`, which increases the value of `x` by `1`.

# **Exercise** Try out the above code yourself.

# In[16]:


x = x + 1
x


# Let's see the effect of assignment step-by-step:
# 1. Run the following cell.
# 1. Click `Next >` to see the next step of the execution.

# In[17]:


get_ipython().run_cell_magic('mytutor', '-h 200', 'x = 15\nx = x + 1')


# The following *tuple assignment* syntax can assign multiple variables in one line.

# In[18]:


get_ipython().run_cell_magic('mytutor', '-h 200', "x, y, z = '15', '30', 15")


# One can also use *chained assignment* to set different variables to the same value.

# In[19]:


get_ipython().run_cell_magic('mytutor', '-h 250', 'x = y = z = 0')


# Variables can be deleted using `del`. Accessing a variable before assignment raises a Name error.

# In[20]:


del x, y
x, y


# ## Identifiers

# *Identifiers* such as variable names are case sensitive and follow certain rules.

# **What is the syntax for variable names?**

# 1. Must start with a letter or `_` (an underscore) followed by letters, digits, or `_`.
# 1. Must not be a [keyword](https://docs.python.org/3.7/reference/lexical_analysis.html#keywords) (identifier reserved by Python):

# <pre>False      await      else       import     pass
# None       break      except     in         raise
# True       class      finally    is         return
# and        continue   for        lambda     try
# as         def        from       nonlocal   while
# assert     del        global     not        with
# async      elif       if         or         yield</pre>

# **Exercise** Evaluate the following cell and check if any of the rules above is violated.

# In[16]:


from ipywidgets import interact
@interact
def identifier_syntax(assignment=['a-number = 15',
                     'a_number = 15',
                     '15 = 15',
                     '_15 = 15',
                     'del = 15',
                     'Del = 15',
                     'type = print',
                     'print = type',
                     'input = print']):
    exec(assignment)
    print('Ok.')


# 1. `a-number = 15` violates Rule 1 because `-` is not allowed. `-` is interpreted as an operator.
# 1. `15 = 15` violates Rule 1 because `15` starts with a digit instead of letter or _.
# 1. `del = 15` violates Rule 2 because `del` is a keyword.

# What can we learn from the above examples?

# - `del` is a keyword and `Del` is not because identifiers are case sensitive.
# - Function/method/type names `print`/`input`/`type` are not keywords and can be reassigned.  
#   This can useful if you want to modify the default implementations without changing their source code.

# To help make code more readable, additional style guides such as [PEP 8](https://www.python.org/dev/peps/pep-0008/#function-and-variable-names) are available:

# - Function names should be lowercase, with words separated by underscores as necessary to improve readability.  
# - Variable names follow the same convention as function names.

# ## User Input

# **How to let the user input a value at *runtime*,  
# i.e., as the program executes?**

# We can use the method `input`:
# - There is no need to delimit the input string by quotation marks.
# - Simply press `enter` after typing a string.

# In[ ]:


print('Your name is', input('Please input your name: '))


# - The `input` method prints its argument, if any, as a [prompt](https://en.wikipedia.org/wiki/Command-line_interface#Command_prompt).  
# - It takes user's input and *return* it as its value. `print` takes in that value and prints it.

# **Exercise** Explain whether the following code prints `'My name is Python'`. Does `print` return a value? 

# In[ ]:


print('My name is', print('Python'))


# - Unlike `input`, the function `print` does not return the string it is trying to print. Printing a string is, therefore, different from returning a string.
# - `print` actually returns a `None` object that gets printed as `None`.

# ## Type Conversion

# The following program tries to compute the sum of two numbers from user inputs:

# In[ ]:


num1 = input('Please input an integer: ')
num2 = input('Please input another integer: ')
print(num1, '+', num2, 'is equal to', num1 + num2)


# **Exercise** There is a [bug](https://en.wikipedia.org/wiki/Software_bug) in the above code. Can you locate the error?

# The two numbers are concatenated instead of added together.

# `input` *returns* user input as a string.  
# E.g., if the user enters `12`, the input is
# - not treated as the integer twelve, but rather
# - treated as a string containing two characters, one followed by two.

# To see this, we can use `type` to return the data type of an expression.

# In[ ]:


num1 = input('Please input an integer: ')
print('Your input is', num1, 'with type', type(num1))


# **Exercise** `type` applies to any expressions. Try it out below on `15`, `print`, `print()`, `input`, and even `type` itself and `type(type)`.

# In[ ]:


type(15), type(print), type(print()), type(input), type(type), type(type(type))


# **So what happens when we add strings together?**

# In[ ]:


'4' + '5' + '6'


# **How to fix the bug then?**

# We can convert a string to an integer using `int`.

# In[ ]:


int('4') + int('5') + int('6')


# We can also convert an integer to a string using `str`.

# In[ ]:


str(4) + str(5) + str(6)


# **Exercise** Fix the bug in the following cell.

# In[ ]:


num1 = input('Please input an integer: ')
num2 = input('Please input another integer: ')
# print(num1, '+', num2, 'is equal to', num1 + num2)  # fix this line below
### BEGIN SOLUTION
print(num1, '+', num2, 'is equal to', int(num1) + int(num2))
### END SOLUTION


# ## Error

# In addition to writing code, a programmer spends significant time in *debugging* code that contains errors.
# 

# **Can an error be automatically detected by the computer?**

# - You have just seen an example of *logical error*, which is due to an error in the logic.  
# - The ability to debug or even detect such error is, unfortunately, beyond Python's intelligence.

# Other kinds of error may be detected automatically.  
# As an example, note that we can omit `+` for string concatenation, but we cannot omit it for integer summation:

# In[ ]:


print('Skipping + for string concatenation')
'4' '5' '6'


# In[ ]:


print('Skipping + for integer summation')
4 5 6


# Python interpreter detects the bug and raises a *syntax* error.

# **Why Syntax error can be detected automatically?  
# Why is the print statement before the error not executed?**

# - The Python interpreter can easily detect syntax error even before executing the code simply because
# - the interpreter fails to interpret the code, i.e., translates the code to lower-level executable code.

# The following code raises a different kind of error.

# In[ ]:


print("Evaluating '4' + '5' + 6")
'4' + '5' + 6  # summing string with integer


# **Why Python throws a TypeError when evaluating `'4' + '5' + 6`?**

# There is no default implementation of `+` operation on a value of type `str` and a value of type `int`. 

# - Unlike syntax error, the Python interpreter can only detect type error at runtime (when executing the code.) 
# - Hence, such error is called a *runtime error*.
# 

# **Why is TypeError a runtime error?**

#  The short answer is that Python is a [strongly-and-dynamically-typed](https://en.wikipedia.org/wiki/Strong_and_weak_typing) language:
# - Strongly-typed: Python does not force a type conversion to avoid a type error.
# - Dynamically-typed: Python allow data type to change at runtime.

# The underlying details are more complicated than required for this course. It helps if you already know the following languages:
# - JavaScript, which is a *weakly-typed* language that forces a type conversion to avoid a type error.
# - C, which is a *statically-typed* language that does not allow data type to change at runtime.

# In[ ]:


get_ipython().run_cell_magic('javascript', '', "alert('4' + '5' + 6)  // no error because 6 is converted to a str automatically")


# A weakly-typed language may seem more robust, but it can lead to [more logical errors](https://www.oreilly.com/library/view/fluent-conference-javascript/9781449339203/oreillyvideos1220106.html).  
# To improve readability, [typescript](https://www.typescriptlang.org/) is a strongly-typed replacement of javascript.

# **Exercise** Not all the strings can be converted into integers. Try breaking the following code by providing invalid inputs and record them in the subsequent cell. Explain whether the errors are runtime errors.

# In[ ]:


num1 = input('Please input an integer: ')
num2 = input('Please input another integer: ')
print(num1, '+', num2, 'is equal to', int(num1) + int(num2))


# The possible invalid inputs are:
# > `4 + 5 + 6`, `15.0`, `fifteen`
# 
# It raises a value error, which is a runtime error detected during execution.  
# 
# Note that the followings are okay
# > int('-1'), eval('4 + 5 + 6')

# ## Floating Point Numbers

# Not all numbers are integers. In Enginnering, we often need to use fractions.

# **How to enter fractions in a program?**

# In[ ]:


x = -0.1 # decimal number
y = -1.0e-1 # scientific notation
z = -1/10 # fraction
x, y, z, type(x), type(y), type(z)


# **What is the type `float`?**

# - `float` corresponds to the [*floating point* representation](https://en.wikipedia.org/wiki/Floating-point_arithmetic#Floating-point_numbers).  
# - A `float` in stored exactly the way we write it in scientific notation: 
# 
# $$
# \overbrace{-}^{\text{sign}} \underbrace{1.0}_{\text{mantissa}\kern-1em}e\overbrace{-1}^{\text{exponent}\kern-1em}=-1\times 10^{-1}
# $$
# - The [truth](https://www.h-schmidt.net/FloatConverter/IEEE754.html) is more complicated than required for the course.

# Integers in mathematics may be regarded as a `float` instead of `int`:

# In[ ]:


type(1.0), type(1e2)


# You can also convert an `int` or a `str` to a `float`.

# In[ ]:


float(1), float('1')


# **Is it better to store an integer as `float`?**

# Python stores a [floating point](https://docs.python.org/3/library/sys.html#sys.float_info) with finite precision (usually as a 64bit binary fraction):

# In[ ]:


import sys
sys.float_info


# It cannot represent a number larger than the `max`:

# In[ ]:


sys.float_info.max * 2


# The precision also affects the check for equality.

# In[33]:


(1.0 == 1.0 + sys.float_info.epsilon * 0.5, # returns true if equal
 1.0 == 1.0 + sys.float_info.epsilon * 0.6, sys.float_info.max + 1 == sys.float_info.max)


# Another issue with float is that it may keep more decimal places than desired.

# In[ ]:


1/3


# **How to [round](https://docs.python.org/3/library/functions.html#round) a floating point number to the desired number of decimal places?**

# In[ ]:


round(2.665,2), round(2.675,2)


# **Why 2.675 rounds to 2.67 instead of 2.68?**

# - A `float` is actually represented in binary.  
# - A decimal fraction [may not be represented exactly in binary](https://docs.python.org/3/tutorial/floatingpoint.html#tut-fp-issues).

# The `round` function can also be applied to an integer.

# In[ ]:


round(150,-2), round(250,-2)


# **Why 250 rounds to 200 instead of 300?**

# - Python 3 implements the default rounding method in [IEEE 754](https://en.wikipedia.org/w/index.php?title=IEEE_754#Rounding_rules).

# ## String Formatting

# **Can we round a `float` or `int` for printing but not calculation?**

# This is possible with [*format specifications*](https://docs.python.org/3/library/string.html#format-specification-mini-language).

# In[ ]:


x = 10000/3
print('x ≈ {:.2f} (rounded to 2 decimal places)'.format(x))
x


# - `{:.2f}` is a *format specification* 
# - that gets replaced by a string 
# - that represents the argument `x` of `format` 
# - as a decimal floating point number rounded to 2 decimal places.

# **Exercise** Play with the following widget to learn the effect of different format specifications. In particular, print `10000/3` as `3,333.33`.

# In[21]:


from ipywidgets import interact
@interact(x='10000/3',
          align={'None':'','<':'<','>':'>','=':'=','^':'^'},
          sign={'None':'','+':'+','-':'-','SPACE':' '},
          width=(0,20),
          grouping={'None':'','_':'_',',':','},
          precision=(0,20))
def print_float(x,sign,align,grouping,width=0,precision=2):
    format_spec = f"{{:{align}{sign}{'' if width==0 else width}{grouping}.{precision}f}}"
    print("Format spec:",format_spec)
    print("x ≈",format_spec.format(eval(x)))


# In[23]:


print('{:,.2f}'.format(10000/3))


# String formatting is useful for different data types other than `float`.  
# E.g., consider the following program that prints a time specified by some variables.

# In[ ]:


# Some specified time
hour = 12
minute = 34
second = 56

print("The time is " + str(hour) + ":" + str(minute) + ":" + str(second)+".")


# Imagine you have to show also the date in different formats.  
# The code can become very hard to read/write because 
# - the message is a concatenation of multiple strings and
# - the integer variables need to be converted to strings.

# Omitting `+` leads to syntax error. Removing `str` as follows also does not give the desired format.

# In[ ]:


print("The time is ", hour, ":", minute, ":", second, ".")  # note the extra spaces


# To make the code more readable, we can use the `format` function as follows.

# In[ ]:


message = "The time is {}:{}:{}."
print(message.format(hour,minute,second))


# - We can have multiple *place-holders* `{}` inside a string.
# - We can then provide the contents (any type: numbers, strings..) using the `format` function, which
# - substitutes the place-holders by the function arguments from left to right.

# According to the [string formatting syntax](https://docs.python.org/3/library/string.html#format-string-syntax), we can change the order of substitution using 
# - indices *(0 is the first item)* or 
# - names inside the placeholder `{}`:

# In[10]:


print("You should {0} {1} what I say instead of what I {0}.".format("do", "only"))
print("The surname of {first} {last} is {last}.".format(first="John", last="Doe"))


# You can even put variables inside the format specification directly and have a nested string formatting.

# In[ ]:


align, width = "^", 5
print(f"{{:*{align}{width}}}".format(x))  # note the syntax f"..."


# **Exercise** Play with the following widget to learn more about the formating specification.  
# 1. What happens when `align` is none but `fill` is `*`?
# 1. What happens when the `expression` is a multi-line string?

# In[20]:


from ipywidgets import interact
@interact(expression=r"'ABC'",
          fill='*',
          align={'None':'','<':'<','>':'>','=':'=','^':'^'},
          width=(0,20))
def print_objectt(expression,fill,align='^',width=10):
    format_spec = f"{{:{fill}{align}{'' if width==0 else width}}}"
    print("Format spec:",format_spec)
    print("Print:",format_spec.format(eval(expression)))


# 1. It returns a ValueError because align must be specified when fill is.
# 1. The newline character is simply regarded a character. The formatting is not applied line-by-line. E.g., try 'ABC\nDEF'.
