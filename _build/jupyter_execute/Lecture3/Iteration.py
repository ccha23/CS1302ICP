#!/usr/bin/env python
# coding: utf-8

# # Iteration

# **CS1302 Introduction to Computer Programming**
# ___

# In[1]:


get_ipython().run_line_magic('reload_ext', 'mytutor')


# ## Motivation

# Many tasks are repetitive:
# - To print from 1 up to a user-specified number, which can be arbitrarily large.
# - To compute the maximum of a sequence of numbers, which can be arbitrarily long.
# - To repeatedly ask users for input until the input is within the right range.

# **How to write code to perform repetitive tasks?**

# E.g., can you complete the following code to print from 1 up to a user-specified number?

# In[2]:


get_ipython().run_cell_magic('mytutor', '-h 300', "num = int(input('>'))\nif 1 < num: print(1)\nif 2 < num: print(2)\nif 3 < num: print(3)\n# YOUR CODE HERE ")


# *code duplication* is not good because:
# - Duplicate code is hard to read/write/maintain.  
#     Imagine there is a small change needed to every duplicate code.
# - The number of repetitions may not be known before runtime.

# Instead, programmers write a *loop* which specifies a piece of code to be executed iteratively.

# ## For Loop

# ### Iterate over a sequence

# **How to print from 1 up to 4?**

# We can use a [`for` statement](https://docs.python.org/3.3/tutorial/controlflow.html#for-statements) as follows:

# In[3]:


get_ipython().run_cell_magic('mytutor', '-h 300', 'for i in 1, 2, 3, 4:\n    print(i)')


# - `i` is automatically assigned to each element in the sequence `1, 2, 3, 4` one-by-one from left to right.
# - After each assignment, the body `print(i)` is executed. 
# 
# N.b., if `i` is defined before the for loop, its value will be overwritten.  

# The assignment is not restricted to integers and can also be a tuple assignment.

# In[4]:


tuples = (0,'l'), (1,'o'), (2,'o'), (3,'p')
for i,c in tuples: print(i,c)  # one-liner


# An even shorter code...

# In[5]:


for i,c in enumerate('loop'): print(i,c)


# ### Iterate over a range

# **How to print up to a user-specified number?**

# We can use [`range`](https://docs.python.org/3/library/stdtypes.html#range):

# In[6]:


stop = int(input('>')) + 1
for i in range(stop):
    print(i)


# **Why add 1 to the user input number?**

# `range(stop)` generates a sequence of integers from `0` up to *but excluding* `stop`.

# **How to start from a number different from `0`?**

# In[8]:


for i in range(1,5): print(i)


# **What about a step size different from `1`?**

# In[9]:


for i in range(0,5,2): print(i)  # starting number must also be specified. Why?


# **Exercise** How to count down from 4 to 0? Do it without addition or subtraction.

# In[10]:


### BEGIN SOLUTION
for i in range(4,-1,-1): print(i)
### END SOLUTION


# **Exercise** Print from `0` to a user-specified number but in steps of `0.5`.  
# E.g., if the user inputs `2`, the program should print:
# ```
# 0.0
# 0.5
# 1.0
# 1.5
# 2.0
# ```
# 
# *Note:* `range` only accepts integer arguments.

# In[12]:


num = int(input('>'))
### BEGIN SOLUTION
for i in range(0, 2 * num + 1, 1):
    print(i / 2)
### END SOLUTION


# **Exercise** How to print the character `'*'` repeatedly for `m` rows and `n` columns?  
# *Hint:* Use a *nested for loop*, i.e., write a for loop (called *inner loop*) inside the body of another for loop (*outer loop*).

# In[13]:


@interact(m=(0, 10), n=(0, 10))
def draw_rectangle(m=5, n=5):
    ### BEGIN SOLUTION
    for i in range(m):
        for j in range(n):
            print('*', end='')
        print()
    ### END SOLUTION


# ### Iterate over a string

# **What does the following do?**

# In[7]:


get_ipython().run_cell_magic('mytutor', '-h 300', "for character in 'loop': print(character)")


# A string is *iterable* because it can be regarded as a sequence of characters.
# - The function [`len`](https://docs.python.org/3/library/functions.html#len) can return the length of a string.
# - The indexing operator `[]` can return the character of a string at a specified location.

# In[15]:


message = "loop"
print('length:', len(message))
print('characters:', message[0], message[1], message[2], message[3])


# We can also iterate over a string as follows although it is less elegant:

# In[16]:


for i in range(len('loop')): print('loop'[i])


# **Exercise** Print a string assigned to `message` in reverse.  
# E.g., `'loop'` should be printed as `'pool'`.

# In[17]:


@interact(message='loop')
def reverse_print(message):
    ### BEGIN SOLUTION
    for i in range(len(message)):
        print(message[-i - 1], end='')
    ### END SOLUTION


# ## While Loop

# **How to repeatedly ask the user to enter an input until the user input is not empty?**

# Python provides the [`while` statement](https://docs.python.org/3/reference/compound_stmts.html#while) to loop until a specified condition is false.

# In[18]:


while not input('Input something please:'): pass


# As long as the condition after `while` is true, the body gets executed repeatedly. In the above example,
# - if user press enter without inputting anything, 
# - `input` returns an empty string `''`, which is [regarded as `False`](https://docs.python.org/3/reference/expressions.html#booleans), and so
# - the looping condition `not input('...')` is `True`.

# **Is it possible to use a for loop instead of a while loop?**

# - Not without hacks because the for loop is a *definite loop* which has a definite number of iterations before the execution of the loop.
# - `while` statement is useful for an *indefinite loop* where the number of iterations is unknown before the execution of the loop.

# It is possible, however, to replace a for loop by a while loop.  
# E.g., the following code prints from `0` to `4` using a while loop instead of a for loop.

# In[19]:


i = 0
while i <= 4:
    print(i)
    i += 1


# - A while loop may not be as elegant (short), c.f., `for i in range(5): print(i)`, but
# - it can always be as efficient.

# **Should we just use while loop?**

# Consider using the following while loop to print from `0` to a user-specified value.

# In[ ]:


num = int(input('>'))
i = 0
while i!=num+1: 
    print(i)
    i += 1


# **Exercise** Is the above while loop doing the same thing as the for loop below?

# In[24]:


for i in range(int(input('>')) + 1): print(i)


# When user input negative integers smaller than or equal to -2,
# - the while loop becomes an infinite loop, but
# - the for loop terminates without printing any number.

# We have to be careful not to create unintended *infinite loops*.  
# The computer can't always detect whether there is an infinite loop. ([Why not?](https://en.wikipedia.org/wiki/Halting_problem))

# ## Break/Continue/Else Constructs of a Loop

# ### Breaking out of a loop

# **Is the following an infinite loop?**

# In[3]:


get_ipython().run_cell_magic('mytutor', '-h 300', "while True:\n    message = input('Input something please:')\n    if message: break\nprint('You entered:', message)")


# The loop is terminated by the [`break` statement](https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops) when user input is non-empty.

# **Why is the `break` statement useful?**

#  Recall the earlier `while` loop:

# In[4]:


get_ipython().run_cell_magic('mytutor', '-h 300', "while not input('Input something please:'): pass ")


# This while loop is not useful because it does not store the user input.

# **Is the `break` statement strictly necessary?** 

# We can avoid `break` statement by using *flags*, which are boolean variables for flow control:

# In[6]:


get_ipython().run_cell_magic('mytutor', '-h 350', "has_no_input = True\nwhile has_no_input:\n    message = input('Input something please:')\n    if message: has_no_input = False\nprint('You entered:', message)")


# Using flags makes the program more readable, and we can use multiple flags for more complicated behavior.  
# The variable names for flags are often `is_...`, `has_...`, etc.

# ### Continue to Next Iteration

# **What does the following program do?  
# Is it an infinite loop?**

# In[7]:


get_ipython().run_cell_magic('mytutor', '-h 300', "while True:\n    message = input('Input something please:')\n    if not message: continue\n    print('You entered:', message)")


# - The program repeatedly ask the user for input.
# - If the input is empty, the `continue` statement will skip to the next iteration.
# - The loop can only be terminated by interrupting the kernel.
# - Such an infinite loop can be useful. E.g., your computer clock continuously updates the current time.

# **Exercise** Is the `continue` statement strictly necessary? Can you rewrite the above program without the `continue` statement? 

# In[10]:


get_ipython().run_cell_magic('mytutor', '-h 350', "while True:\n    message = input('Input something please:')\n    ### BEGIN SOLUTION\n    if message:\n        print('You entered:', message)\n    ### END SOLUTION")


# ### Else construct for a loop

# The following program 
# - checks whether the user input is a positive integer using `isdigit`, and if so,
# - check if the positive integer is a composite number, i.e., a product of two smaller positive integers.

# In[8]:


@interact(num='1')
def check_composite(num):
    if num.isdigit():
        num = int(num)
        for divisor in range(2,num):
            if num % divisor:
                continue
            else:
                print('It is composite.')
                break
        else:
            print('It is not composite.')
    else:
        print('Not a positive integer.')


# In[ ]:


get_ipython().run_cell_magic('mytutor', '-h 500 ', "def check_composite(num):\n    if num.isdigit():\n        num = int(num)\n        for divisor in range(2,num):\n            if num % divisor:\n                continue\n            else:\n                print('It is composite.')\n                break\n        else:\n            print('It is not composite.')\n    else:\n        print('Not a positive integer.')\n        \ncheck_composite('1')\ncheck_composite('2')\ncheck_composite('3')\ncheck_composite('4')")


# In addition to using `continue` and `break` in an elegant way,  
# the code also uses an else clause that is executed only when the loop terminates *normally* not by `break`.

# **Exercise** There are three else claues in the earlier code. Which one is for the loop?

# - The second else clause that `print('It is not composite.')`.
# - The clause is called when there is no divisor found in the range from `2` to `num`.

# **Exercise** Convert the for loop to a while loop.  
# Can you improve the code to use fewer iterations?

# In[7]:


@interact(num='1')
def check_composite(num):
    if num.isdigit():
        num = int(num)
        # for divisor in range(2,num):    # use while instead
        divisor = 2
        while divisor <= num**0.5: 
            if num % divisor:
                divisor += 1
            else:
                print('It is composite.')
                break
        else:
            print('It is not composite.')
    else:
        print('Not a positive integer.')

