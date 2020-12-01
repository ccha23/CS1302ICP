#!/usr/bin/env python
# coding: utf-8

# # Review Questions

# **CS1302 Introduction to Computer Programming**
# ___

# In[1]:


get_ipython().run_line_magic('reload_ext', 'mytutor')


# ## Dictionaries and Sets

# **Exercise (Concatenate two dictionaries with precedence)** Define a function `concat_two_dicts` that accepts two arguments of type `dict` such that `concat_two_dicts(a, b)` will return a new dictionary containing all the items in `a` and the items in `b` that have different keys than those in `a`.  The input dictionaries should not be mutated.

# In[2]:


def concat_two_dicts(a, b):
    ### BEGIN SOLUTION
    return {**b, **a}
    ### END SOLUTION


# In[3]:


#tests
a={'x':10, 'z':30}; b={'y':20, 'z':40}
a_copy = a.copy(); b_copy = b.copy()
assert concat_two_dicts(a, b) == {'x': 10, 'z': 30, 'y': 20}
assert concat_two_dicts(b, a) == {'x': 10, 'z': 40, 'y': 20}
assert a == a_copy and b == b_copy
### BEGIN HIDDEN TESTS
a={'x':10, 'z':30}; b={'y':20}
a_copy = a.copy(); b_copy = b.copy()
assert concat_two_dicts(a, b) == {'x': 10, 'z': 30, 'y': 20}
assert concat_two_dicts(b, a) == {'x': 10, 'z': 30, 'y': 20}
assert a == a_copy and b == b_copy
### END HIDDEN TESTS


# - `{**dict1,**dict2}` creates a new dictionary by unpacking the dictionaries `dict1` and `dict2`.
# - By default, `dict2` overwrites `dict1` if they have identical keys.

# **Exercise (Count characters)** Define a function `count_characters` which
# - accepts a string and counts the numbers of each character in the string, and 
# - returns a dictionary that stores the results.

# In[4]:


def count_characters(string):
    ### BEGIN SOLUTION
    counts = {}
    for char in string:
        counts[char] = counts.get(char, 0) + 1
    return counts
    ### END SOLUTION


# In[5]:


# tests
assert count_characters('abcbabc') == {'a': 2, 'b': 3, 'c': 2}
assert count_characters('aababcccabc') == {'a': 4, 'b': 3, 'c': 4}
### BEGIN HIDDEN TESTS
assert count_characters('abcdefgabc') == {'a': 2, 'b': 2, 'c': 2, 'd': 1, 'e': 1, 'f': 1, 'g': 1}
assert count_characters('ab43cb324abc') == {'2': 1, '3': 2, '4': 2, 'a': 2, 'b': 3, 'c': 2}
### END HIDDEN TESTS


# - Create an empty dictionary `counts`.
# - Use a `for` loop to iterate over each character of `string` to count their numbers of occurrences.
# - The `get` method of `dict` can initialize the count of a new character before incrementing it.

# **Exercise (Count non-Fibonacci numbers)** Define a function `count_non_fibs` that 
# - accepts a container as an argument, and 
# - returns the number of items in the container that are not [fibonacci numbers](https://en.wikipedia.org/wiki/Fibonacci_number).

# In[6]:


def count_non_fibs(container):
    ### BEGIN SOLUTION
    def fib_sequence_inclusive(stop):
        Fn, Fn1 = 0, 1
        while Fn <= stop:
            yield Fn
            Fn, Fn1 = Fn1, Fn + Fn1

    non_fibs = set(container)
    non_fibs.difference_update(fib_sequence_inclusive(max(container)))
    return len(non_fibs)
    ### END SOLUTION


# In[7]:


# tests
assert count_non_fibs([0, 1, 2, 3, 5, 8]) == 0
assert count_non_fibs({13, 144, 99, 76, 1000}) == 3
### BEGIN HIDDEN TESTS
assert count_non_fibs({5, 8, 13, 21, 34, 100}) == 1
assert count_non_fibs({0.1, 0}) == 1
### END HIDDEN TESTS


# - Create a set of Fibonacci numbers up to the maximum of the items in the container.
# - Use `difference_update` method of `set` to create a set of items in the container but not in the set of Fibonacci numbers.

# **Exercise (Calculate total salaries)** Suppose `salary_dict` contains information about the name, salary, and working time about employees in a company. An example of `salary_dict` is as follows:  
# ```Python
# salary_dict = {
#      'emp1': {'name': 'John', 'salary': 15000, 'working_time': 20},
#      'emp2': {'name': 'Tom', 'salary': 16000, 'working_time': 13},
#      'emp3': {'name': 'Jack', 'salary': 15500, 'working_time': 15},
# }
# ```
# 
# Define a function `calculate_total` that accepts `salary_dict` as an argument, and returns a `dict` that uses the same keys in `salary_dict` but the total salaries as their values.  The total salary of an employee is obtained by multiplying his/her salary and his/her working_time. 
# E.g.,, for the `salary_dict` example above, `calculate_total(salary_dict)` should return
# ```Python
# {'emp1': 300000, 'emp2': 208000, 'emp3': 232500}.
# ```
# where the total salary of `emp1` is $15000 \times 20 = 300000$.

# In[8]:


def calculate_total(salary_dict):
    ### BEGIN SOLUTION
    return {
        emp: record['salary'] * record['working_time']
        for emp, record in salary_dict.items()
    }
    ### END SOLUTION


# In[9]:


# tests
salary_dict = {
     'emp1': {'name': 'John', 'salary': 15000, 'working_time': 20},
     'emp2': {'name': 'Tom', 'salary': 16000, 'working_time': 13},
     'emp3': {'name': 'Jack', 'salary': 15500, 'working_time': 15},
}
assert calculate_total(salary_dict) == {'emp1': 300000, 'emp2': 208000, 'emp3': 232500}
### BEGIN HIDDEN TESTS
salary_dict = {
     'emp1': {'name': 'John', 'salary': 15000, 'working_time': 20},
     'emp2': {'name': 'Tom', 'salary': 16000, 'working_time': 13},
     'emp3': {'name': 'Jack', 'salary': 15500, 'working_time': 15},
     'emp4': {'name': 'Bob', 'salary': 20000, 'working_time': 10}
}
assert calculate_total(salary_dict) == {'emp1': 300000, 'emp2': 208000, 'emp3': 232500, 'emp4': 200000}
### END HIDDEN TESTS


# - Use `items` method of `dict` to return the list of key values pairs, and
# - use a dictionary comprehension to create the desired dictionary by iterating through the list of items.

# **Exercise (Delete items with value 0 in dictionary)** Define a function `zeros_removed` that 
# - takes a dictionary as an argument,
# - mutates the dictionary to remove all the keys associated with values equal to `0`,
# - and return `True` if at least one key is removed else `False`.

# In[10]:


def zeros_removed(d):
    ### BEGIN SOLUTION
    to_delete = [k for k in d if d[k] == 0]
    for k in to_delete:
        del d[k]
    return len(to_delete) > 0


## Memory-efficient but not computationally efficient
# def zeros_removed(d):
#     has_deleted = False
#     while True:
#         for k in d:
#             if d[k] == 0:
#                 del d[k]
#                 has_deleted = True
#                 break
#         else: return has_deleted

### END SOLUTION


# In[11]:


# tests
d = {'a':0, 'b':1, 'c':0, 'd':2}
assert zeros_removed(d) == True
assert zeros_removed(d) == False
assert d == {'b': 1, 'd': 2}
### BEGIN HIDDEN TESTS
d = {'a':0, 'b':1, 'c':0, 'd':2, 'e':0, 'f':'0'}
assert zeros_removed(d) == True
assert zeros_removed(d) == False
assert d == {'b': 1, 'd': 2, 'f':'0'}
### END HIDDEN TESTS


# - The main issue is that, for any dicionary `d`,
# ```Python
#     for k in d: 
#         if d[k] == 0: del d[k]
# ```
# raises the [`RuntimeError: dictionary changed size during iteration`](https://www.geeksforgeeks.org/python-delete-items-from-dictionary-while-iterating/). 
# - One solution is to duplicate the list of keys, but this is memory inefficient especially when the list of keys is large.
# - Another solution is to record the list of keys to delete before the actual deletion. This is memory efficient if the list of keys to delete is small.

# **Exercise (Fuzzy search a set)** Define a function `search_fuzzy` that accepts two arguments `myset` and `word` such that
# - `myset` is a `set` of `str`s;
# - `word` is a `str`; and
# - `search_fuzzy(myset, word)` returns `True` if `word` is in `myset` by changing at most one character in `word`, and returns `False` otherwise.  

# In[12]:


def search_fuzzy(myset, word):
    ### BEGIN SOLUTION
    for myword in myset:
        if len(myword) == len(word) and len(
            [True
             for mychar, char in zip(myword, word) if mychar != char]) <= 1:
            return True
    return False
    ### END SOLUTION


# In[13]:


# tests
assert search_fuzzy({'cat', 'dog'}, 'car') == True
assert search_fuzzy({'cat', 'dog'}, 'fox') == False
### BEGIN HIDDEN TESTS
myset = {'cat', 'dog', 'dolphin', 'rabbit', 'monkey', 'tiger'}
assert search_fuzzy(myset, 'lion') == False
assert search_fuzzy(myset, 'cat') == True
assert search_fuzzy(myset, 'cat ') == False
assert search_fuzzy(myset, 'fox') == False
assert search_fuzzy(myset, 'ccc') == False
### END HIDDEN TESTS


# - Iterate over each word in `myset`.
# - Check whether the length of the word is the same as that of the word in the arguments.
# - If the above check passes, use a list comprehension check if the words differ by at most one character.

# **Exercise (Get keys by value)** Define a function `get_keys_by_value` that accepts two arguments `d` and `value` where `d` is a dictionary, and returns a set containing all the keys in `d` that have `value` as its value. If no key has the query value `value`, then return an empty set.

# In[14]:


def get_keys_by_value(d, value):
    ### BEGIN SOLUTION
    return {k for k in d if d[k] == value}
    ### END SOLUTION


# In[15]:


# tests
d = {'Tom':'99', 'John':'88', 'Lucy':'100', 'Lily':'90', 'Jason':'89', 'Jack':'100'}
assert get_keys_by_value(d, '99') == {'Tom'}
### BEGIN HIDDEN TESTS
d = {'Tom':'99', 'John':'88', 'Lucy':'100', 'Lily':'90', 'Jason':'89', 'Jack':'100'}
assert get_keys_by_value(d, '100') == {'Jack', 'Lucy'}
d = {'Tom':'99', 'John':'88', 'Lucy':'100', 'Lily':'90', 'Jason':'89', 'Jack':'100'}
assert get_keys_by_value(d, '0') == set()
### END HIDDEN TESTS


# - Use set comprehension to create the set of keys whose associated values is `value`.

# **Exercise (Count letters and digits)** Define a function `count_letters_and_digits` which  
# - take a string as an argument,
# - returns a dictionary that stores the number of letters and digits in the string using the keys 'LETTERS' and 'DIGITS' respectively.

# In[16]:


def count_letters_and_digits(string):
    ### BEGIN SOLUTION
    check = {'LETTERS': str.isalpha, 'DIGITS': str.isdigit}
    counts = dict.fromkeys(check.keys(), 0)
    for char in string:
        for t in check:
            if check[t](char):
                counts[t] += 1
    return counts
    ### END SOLUTION


# In[17]:


assert count_letters_and_digits('hello world! 2020') == {'DIGITS': 4, 'LETTERS': 10}
assert count_letters_and_digits('I love CS1302') == {'DIGITS': 4, 'LETTERS': 7}
### BEGIN HIDDEN TESTS
assert count_letters_and_digits('Hi CityU see you in 2021') == {'DIGITS': 4, 'LETTERS': 15}
assert count_letters_and_digits('When a dog runs at you, whistle for him. (Philosopher Henry David Thoreau, 1817-1862)') == {'DIGITS': 8, 'LETTERS': 58}
### END HIDDEN TESTS


# - Use the class method `fromkeys` of `dict` to initial the dictionary of counts.

# **Exercise (Dealers with lowest price)** Suppose `apple_price` is a list in which each element is a `dict` recording the dealer and the corresponding price, e.g., 
# ```Python
# apple_price = [{'dealer': 'dealer_A', 'price': 6799},
#  {'dealer': 'dealer_B', 'price': 6749},
#  {'dealer': 'dealer_C', 'price': 6798},
#  {'dealer': 'dealer_D', 'price': 6749}]
# ```
# Define a function `dealers_with_lowest_price` that takes `apple_price` as an argument, and returns the `set` of dealers providing the lowest price.

# In[18]:


def dealers_with_lowest_price(apple_price):
    ### BEGIN SOLUTION
    dealers = {}
    lowest_price = None
    for pricing in apple_price:
        if lowest_price == None or lowest_price > pricing['price']:
            lowest_price = pricing['price']
        dealers.setdefault(pricing['price'], set()).add(pricing['dealer'])
    return dealers[lowest_price]

## Shorter code that uses comprehension
# def dealers_with_lowest_price(apple_price):
#     lowest_price = min(pricing['price'] for pricing in apple_price)
#     return set(pricing['dealer'] for pricing in apple_price
#                if pricing['price'] == lowest_price)
    ### END SOLUTION


# In[19]:


# tests
apple_price = [{'dealer': 'dealer_A', 'price': 6799},
 {'dealer': 'dealer_B', 'price': 6749},
 {'dealer': 'dealer_C', 'price': 6798},
 {'dealer': 'dealer_D', 'price': 6749}]
assert dealers_with_lowest_price(apple_price) == {'dealer_B', 'dealer_D'}
### BEGIN HIDDEN TESTS
apple_price = [{'dealer': 'dealer_A', 'price': 6799},
 {'dealer': 'dealer_B', 'price': 6799},
 {'dealer': 'dealer_C', 'price': 6799},
 {'dealer': 'dealer_D', 'price': 6799}]
assert dealers_with_lowest_price(apple_price) == {'dealer_A', 'dealer_B', 'dealer_C', 'dealer_D'}
### END HIDDEN TESTS


# - Use the class method `setdefault` of `dict` to create a dictionary that maps different prices to different sets of dealers.
# - Compute the lowest price at the same time.
# - Alternatively, use comprehension to find lowest price and then create the desired set of dealers with the lowest price.
# 

# ## Lists and Tuples

# **Exercise** (Binary addition) Define a function `add_binary` that 
# - accepts two arguments of type `str` which represent two non-negative binary numbers, and 
# - returns the binary number in `str` equal to the sum of the two given binary numbers.

# In[20]:


def add_binary(*binaries):
    ### BEGIN SOLUTION
    def binary_to_decimal(binary):
        return sum(2**i * int(b) for i, b in enumerate(reversed(binary)))

    def decimal_to_binary(decimal):
        return ((decimal_to_binary(decimal // 2) if decimal > 1 else '') +
                str(decimal % 2)) if decimal else '0'
    
    return decimal_to_binary(sum(binary_to_decimal(binary) for binary in binaries))

## Alternative 1 using recursion
# def add_binary(bin1, bin2, carry=False):
#     if len(bin1) > len(bin2):
#         return add_binary(bin2, bin1)
#     if bin1 == '':
#         return add_binary('1', bin2, False) if carry else bin2
#     s = int(bin1[-1]) + int(bin2[-1]) + carry
#     return add_binary(bin1[:-1], bin2[:-1], s > 1) + str(s % 2)

## Alternatve 2 using iteration
# def add_binary(a, b):
#     answer = []
#     n = max(len(a), len(b))
#     # fill necessary '0' to the beginning to make a and b have the same length
#     if len(a) < n: a = str('0' * (n -len(a))) + a 
#     if len(b) < n: b = str('0' * (n -len(b))) + b
#     carry = 0
#     for i in range(n-1, -1, -1):
#         if a[i] == '1': carry += 1
#         if b[i] == '1': carry += 1
#         answer.insert(0, '1') if carry % 2 == 1 else answer.insert(0, '0')
#         carry //= 2
#     if carry == 1: answer.insert(0, '1')
#     answer_str = ''.join(answer) # you can also use "answer_str = '';  for x in answer: answer_str += x"
#     return answerastr

    ### END SOLUTION


# In[21]:


# tests
assert add_binary('0', '0') == '0'
assert add_binary('11', '11')  == '110'
assert add_binary('101', '101')  == '1010'
### BEGIN HIDDEN TESTS
assert add_binary('1111', '10')  == '10001'
assert add_binary('111110000011','110000111')  == '1000100001010'
### END HIDDEN TESTS


# - Use comprehension to convert the binary numbers to decimal numbers.
# - Use comprehension to convert the sum of the decimal numbers to a binary number.
# - Alternatively, perform bitwise addition using a recursion or iteration.

# **Exercise (Even-digit numbers)** Define a function `even_digit_numbers`, which finds all numbers between `lower_bound` and `upper_bound` such that each digit of the number is an even number. Please return the numbers as a list.

# In[22]:


def even_digit_numbers(lower_bound, upper_bound):
    ### BEGIN SOLUTION
    return [
        x for x in range(lower_bound, upper_bound)
        if not any(int(d) % 2 for d in str(x))
    ]
    ### END SOLUTION


# In[23]:


# tests
assert even_digit_numbers(1999, 2001) == [2000]
assert even_digit_numbers(2805, 2821) == [2806,2808,2820]
### BEGIN HIDDEN TESTS
assert even_digit_numbers(1999, 2300) == [2000,2002,2004,2006,2008,2020,2022,2024,2026,2028,2040,2042,2044,2046,2048,2060,2062,2064,2066,2068,2080,2082,2084,2086,2088,2200,2202,2204,2206,2208,2220,2222,2224,2226,2228,2240,2242,2244,2246,2248,2260,2262,2264,2266,2268,2280,2282,2284,2286,2288]
assert even_digit_numbers(8801, 8833) == [8802,8804,8806,8808,8820,8822,8824,8826,8828]
assert even_digit_numbers(3662, 4001) == [4000]
### END HIDDEN TESTS


# - Use list comprehension to generate numbers between the bounds, and
# - use comprehension and the `any` function to filter out those numbers containing odd digits. 

# **Exercise (Maximum subsequence sum)** Define a function `max_subsequence_sum` that 
# - accepts as an argument a sequence of numbers, and 
# - returns the maximum sum over nonempty contiguous subsequences.  
# 
# E.g., when `[-6, -4, 4, 1, -2, 2]` is given as the argument, the function returns `5` because the nonempty subsequence `[4, 1]` has the maximum sum `5`.

# In[24]:


def max_subsequence_sum(a):
    ### BEGIN SOLUTION
    ## see https://en.wikipedia.org/wiki/Maximum_subarray_problem
    t = s = 0
    for x in a:
        t = max(0, t + x)
        s = max(s, t)
    return s

## Alternative (less efficient) solution using list comprehension
# def max_subsequence_sum(a):
#     return max(sum(a[i:j]) for i in range(len(a)) for j in range(i,len(a)+1))

    ### END SOLUTION


# In[25]:


# tests
assert max_subsequence_sum([-6, -4, 4, 1, -2, 2]) == 5
assert max_subsequence_sum([2.5, 1.4, -2.5, 1.4, 1.5, 1.6]) == 5.9
### BEGIN HIDDEN TESTS
seq = [-24.81, 25.74, 37.29, -8.77, 0.78, -15.33, 30.21, 34.94, -40.64, -20.06]
assert round(max_subsequence_sum(seq),2) == 104.86
### BEGIN HIDDEN TESTS


# In[26]:


# test of efficiency
assert max_subsequence_sum([*range(1234567)]) == 762077221461


# - For a list $[a_0,a_1,\dots]$, let 
# 
# $$
# t_k:=\max_{j<k} \sum_{i=j}^{k-1} a_i = \max\{t_{k-1}+a_{k-1},0\},
# $$ 
# namely the maximum tail sum of $[a_0,\dots,a_{k-1}]$. 
# - Then, the maximum subsequence sum of $[a_0,\dots,a_{k-1}]$ is 
# 
# $$
# s_k:=\max_{j\leq k} t_j.
# $$

# **Exercise (Mergesort)** *For this question, do not use the `sort` method or `sorted` function.*
# 
# Define a function called `merge` that
# 
# - takes two sequences sorted in ascending orders, and
# - returns a sorted list of items from the two sequences.
# 
# Then, define a function called `mergesort` that
# 
# - takes a sequence, and
# - return a list of items from the sequence sorted in ascending order.
# 
# The list should be constructed by 
# 
#  - recursive calls to `mergesort` the first and second halves of the sequence individually, and
#  - merge the sorted halves.

# In[27]:


def merge(left,right):
    ### BEGIN SOLUTION
    if left and right:
        if left[-1] > right[-1]: left, right = right, left
        return merge(left,right[:-1]) + [right[-1]]
    return list(left or right)
    ### END SOLUTION


# In[28]:


def mergesort(seq):
    ### BEGIN SOLUTION
    if len(seq) <= 1:
        return list(seq)
    i = len(seq)//2
    return merge(mergesort(seq[:i]),mergesort(seq[i:]))
    ### END SOLUTION


# In[29]:


# tests
assert merge([1,3],[2,4]) == [1,2,3,4]
assert mergesort([3,2,1]) == [1,2,3]
### BEGIN HIDDEN TESTS
assert mergesort([3,5,2,4,2,1]) == [1,2,2,3,4,5]
### END HIDDEN TESTS


# ## More Functions

# **Exercise (Arithmetic geometric mean)** Define a function `arithmetic_geometric_mean_sequence` which
# 
# - takes two floating point numbers  `x` and `y` and 
# - returns a generator that generates the tuple \\((a_n, g_n)\\) where
# 
# $$
# \begin{aligned}
# a_0 &= x, g_0 = y \\
# a_n &= \frac{a_{n-1} + g_{n-1}}2 \quad \text{for }n>0\\
# g_n &= \sqrt{a_{n-1} g_{n-1}}
# \end{aligned}
# $$

# In[30]:


def arithmetic_geometric_mean_sequence(x, y):
    ### BEGIN SOLUTION
    a, g = x, y
    while True:
        yield a, g
        a, g = (a + g)/2, (a*g)**0.5
    ### END SOLUTION


# In[31]:


# tests
agm = arithmetic_geometric_mean_sequence(6,24)
assert [next(agm) for i in range(2)] == [(6, 24), (15.0, 12.0)]
### BEGIN HIDDEN TESTS
agm = arithmetic_geometric_mean_sequence(100,400)
for sol, ans in zip([next(agm) for i in range(5)], [(100, 400), (250.0, 200.0), (225.0, 223.60679774997897), (224.30339887498948, 224.30231718318308), (224.30285802908628, 224.30285802843423)]):
    for a, b in zip(sol,ans):
        assert round(a,5) == round(b,5)
### END HIDDEN TESTS


# - Use the `yield` expression to return each tuple of $(a_n,g_n)$ efficiently without redundant computations.
