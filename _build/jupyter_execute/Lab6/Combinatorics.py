#!/usr/bin/env python
# coding: utf-8

# # Combinatorics

# **CS1302 Introduction to Computer Programming**
# ___

# ## Permutation using Recursion

# A [$k$-permutation of $n$](https://en.wikipedia.org/wiki/Permutation#k-permutations_of_n) items $a_0,\dots,a_{n-1}$ is an ordered tuple 
# 
# $$
# (a_{i_0},\dots,a_{i_{k-1}})
# $$ 
# of $k$ out of the $n$ objects, where $0\leq i_0,\dots,i_{k-1}<n$ are distinct indices. An $n$-permutation of $n$ objects is simply called a permutation of $n$ objects.

# For examples:
# - The list of ($3$-)permutations of `1,2,3` is:

# In[ ]:


[(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]


# - The list of $2$-permutations of `1,2,3` is:

# In[ ]:


[(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]


# In the above, we used
# - a `tuple` delimited by `()` such as `(1,2,3)` to store items of a permutation, and 
# - a `list` delimited by `[]` such as `[(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]` to store all the permutations.

# Generating permutations is a fundamental problem in computing and combinatorics.  
# A simple way to generate permutations is by recursion. (There are also [other algorithms](https://www.topcoder.com/generating-permutations/).)

# **Recurrence relation (Line 10):**  
# - Removing the first element of a $k$-permutation of $n$ objects gives a different $(k-1)$-permutation of the remaining $n-1$ objects.
# 
# $$ (a_{i_0}, \underbrace{a_{i_1},\dots,a_{i_{k-1}}}_{\text{($k-1$)-permutation of $a_{i_1},\dots,a_{i_{k-1}}$.}\kern-5em} ) $$
# - Reversing the above removal process gives a way of constructing a $k$-permutation from a $(k-1)$-permutation.  
#   E.g., the permutations of $1,2,3$ can be constructed as follows:
# 
# $$[\overbrace{({\color{red} 1}, {\color{blue}{2, 3}}), ({\color{red} 1}, {\color{blue}{3, 2}})}^{\text{prepend 1 to permutations of $2,3$.} }, \overbrace{({\color{red} 2}, {\color{blue}{1, 3}}), ({\color{red} 2}, {\color{blue}{3, 1}})}^{\text{prepend 2 to permutations of $1,3$.} }, \overbrace{({\color{red} 3}, {\color{blue}{1, 2}}), ({\color{red} 3}, {\color{blue}{2, 1}})}^{\text{prepend 3 to permutations of $1,2$.} }]$$

# The following is an implementation of the recursion `permutation(*a,k=None)` that
# - takes in a variable number $n$ of objects as positional arguments (in `a`),
# - takes in an integer $k$ using a keyword argument (`k`, with the default `k=None` for $k=n$), and
# - returns the list of all $k$-permutations represented as ordered tuples of the $n$ objects.

# In[ ]:


def permutation(*a, k=None):
    '''Returns the list of (k-)permutations of the position arguments.'''
    n = len(a)
    output = []
    if k is None:
        k = n
    if 0 < k <= n:
        for i in range(n):
            output.extend([(a[i], ) + p for p in permutation(*a[:i], *a[i + 1:], k=k - 1)])
    elif k == 0:
        return [()]
    return output

print(permutation(1, 2, 3))
print(permutation(1, 2, 3, k=2))


# The recurrence is implemented by the for loop:
# ```Python
#         ...
#         for i in range(n):
#             output.extend([(a[i], ) + p
#                            for p in permutation(*a[:i], *a[i + 1:], k=k - 1)])
#         ...
# ```

# In the above code, `(a[i], ) + p` creates a $k$-permutation of the items in `a` by concatenating for each index `i`
# - a singleton tuple `(a[i], )` and 
# - a $k-1$ permutation `p` of all elements but `a[i]`.
# 
# (See the example in the recurrence relation described earlier.)

# Note that:
# - The comma in `(a[i], )` is not a typo. Without commas, `(...)` does not create a tuple. 
# - `a[:i]` returns a tuple of `a[0]` up to and excluding `a[i]`. `*a[:i]` unpacks the tuple such that its items are separate arguments to `permutation`. 
# - Similarly, `*a[i + 1:]` provides items as separate arguments starting from `a[i + 1]` until the last item in `a`.
# - `[... for ...]` generates a list of $k$-permutations, and `output.extend([...])` added the list to the end of the `output` list.

# **Exercise** One of the base cases of the recusion happens when $k=0$, in which case there is only one $k$-permutation, namely the empty tuple $()$, and so the function returns `[()]`. There is another base case of the recursion. Explain the condition of that base case and its return value.

# YOUR ANSWER HERE

# ## Number of permutations

# Computing permutations using recursion is slow. Why?  
# There are simply too many permutations even for a reasonably small $n$.

# In[ ]:


n = 9
output = permutation(*range(1,n+1))
print('# permutations:',len(output))


# Surprisingly, the number $P_n$ of ($n-$)permutations of $n$ items can be calculated much faster without enumerating all the permutations. It satisfies the following recurrence:
# 
# $$
# P_n = \begin{cases}
# n P_{n-1} & n>0\\
# 1 & n=0\\
# 0 & \text{otherwise.}
# \end{cases}
# $$
# 
# This quantity is fundamental in the field of [combinatorics](https://en.wikipedia.org/wiki/Combinatorics) with enormous applications.

# **Exercise** Implement the above recurrence equation as a recursion `num_permutation(n)` which
# - takes in an integer `n`, and
# - returns the number of permutations of `n` items.
# 
# *Hint: Ensure all base cases are covered, and can run efficiently for large $n$.*

# In[ ]:


def num_permutation(n):
    # YOUR CODE HERE
    raise NotImplementedError()


# In[ ]:


# tests
assert num_permutation(10) == 3628800
assert num_permutation(0) == 1
assert num_permutation(-1) == 0


# **Exercise** Extend the function to `num_permutation(n,k=None)` which
# - takes in an additional optional keyword argument `k`, and
# - returns the INTEGER number of `k`-permutations of `n` items.
# 
# The number is given by the formula
# 
# $$P_{n,k} = \begin{cases}
# \frac{P_n}{P_{n-k}} & 0\leq k \leq n\\
# 0 & \text{otherwise.}
# \end{cases}$$

# In[ ]:


def num_permutation(n,k=None):
    # YOUR CODE HERE
    raise NotImplementedError()


# In[ ]:


# tests
assert isinstance(num_permutation(0), int)
assert num_permutation(3) == 6
assert num_permutation(3,0) == 1
assert num_permutation(3,2) == 6
assert num_permutation(10,5) == 30240


# ## Permutation using Iteration

# The following function `permutation_sequence(*a)` returns a generator that generates the list of $k$-permutations one-by-one for $k$ from $0$ to `len(a)`.

# In[ ]:


def permutation_sequence(*a):
    '''Returns a generator for the k-permuations of the positional arguments
    for k from 0 to len(a).'''
    n = len(a)
    output, idx_left = [()], [tuple(range(n))]
    for k in range(0, n + 1):
        yield output
        next_output, next_idx_left = [], []
        for m in range(len(idx_left)):
            for j in range(len(idx_left[m])):
                i = idx_left[m][j]
                next_output.append(output[m] + (a[i], ))
                next_idx_left.append(idx_left[m][:j] + idx_left[m][j + 1:])
        output, idx_left = next_output, next_idx_left


for permutation_list in permutation_sequence(1, 2, 3):
    print(permutation_list)


# In[ ]:


a=tuple(range(3))
print(a)


# Unlike the recursion `permutation`, the above generates a $k$-permutation $(a_{i_0},\dots,a_{i_{k-1}})$ of $n$ object iteratively by 
# - choosing $i_j$ for $j$ from $0$ to $k-1$ such that
# - $i_j$ is not already chosen, i.e., $i_j\not\in \{i_0,\dots,i_{j-1}\}$.

# E.g., the permutations of $1,2,3$ is generated iteratively as follows:
# - 1
#  - 1,2
#    - **(1,2,3)**
#  - 1,3
#    - **(1,3,2)**
# - 2
#  - 2,1
#    - **(2,1,3)**
#  - 2,3
#    - **(2,3,1)**
# - 3
#  - 3,1
#    - **(3,1,2)**
#  - 3,2
#    - **(3,2,1)**

# **Invariance maintained at the beginning of iteration:**
# - `output` is the list of $k$-permutations, and
# - `idx_left[m]` is the list of indices of arguments not yet in `output[m]`. 
# 
# A $(k+1)$-permutation (in `next_output`) can then be generated by (Line 10) appending an argument (with an index from `idx_left`) to a $k$-permutation (in `output`).

# Is iteration significantly faster?

# In[ ]:


n = 9
for k, permutation_list in enumerate(permutation_sequence(*range(1,n+1))):
    print('# {}-permutations of {} items: {}'.format(k, n, len(permutation_list)))


# Unfortunately, there is not much improvement. Nevertheless, we can efficiently compute the number of $k$-permutations based on the previously computed number of $k-1$-permutations:
# 
# For $k$ from $0$ to $n$,
# 
# $$
# P_{n,k} = \underbrace{\overbrace{n\times  (n-1)\times \cdots }^{P_{n,k-1}\text{  if }k>0}\times(n-k+1)}_{\text{$k$ terms in the product.}}.$$

# **Exercise** Use the `yield` statement to write the function `num_permutation_sequence(n)` that returns a generator of $P_{n,k}$ with `k` from `0` to `n`.

# In[ ]:


def num_permutation_sequence(n):
    output = 1
    for k in range(0, n + 1):
        # YOUR CODE HERE
        raise NotImplementedError()


# In[ ]:


# tests
assert [m for m in num_permutation_sequence(3)] == [1, 3, 6, 6]
assert [m for m in num_permutation_sequence(10)] == [1, 10, 90, 720, 5040, 30240, 151200, 604800, 1814400, 3628800, 3628800]


# **Exercise (Challenge)** Extend the function `num_permutation_sequence(n)` so that calling `send(0)` method causes the generator to increment $n$ instead of $k$ for the next number to generate. i.e., for $0\leq k \leq n$,
# 
# $$\dots P_{n,k-1}\to P_{n,k} \xrightarrow{\text{send(0)}} P_{n+1,k} \to P_{n+1,k+1}\dots$$
# where $\to$ without labels is the normal transition without calling the `send` method.
# 
# *Hint:*
# 
# $$P_{n+1,k}=P_{n,k} \times \frac{n+1}{n-k+1}.$$

# In[ ]:


def num_permutation_sequence(n):
    # YOUR CODE HERE
    raise NotImplementedError()


# In[ ]:


# tests
g = num_permutation_sequence(3)
assert (next(g), next(g), g.send(0), next(g), next(g), next(g), g.send(0)) == (1, 3, 4, 12, 24, 24, 120)


# ## Deduplication using Decorator

# An issue with the function `permutation` is that it regards arguments at different positions as distinct even if they may have the same value. E.g.,  
# `permutation(1,1,2)` returns `[(1, 1, 2), (1, 2, 1), (1, 1, 2), (1, 2, 1), (2, 1, 1), (2, 1, 1)]`  
# where each distinct permutation appears twice.

# To remove duplicates from a list, we can 
# - convert the list to a `set` (which automatically remove duplicates),
# - and then convert the set back to a list.

# In[ ]:


print('Deduplicated:',list(set(permutation(1,1,2))))


# Using a decorator, we can fix `permutation` without rewriting the function.

# In[ ]:


import functools


def deduplicate_output(f):
    '''Takes in a function f that returns a list possibly with duplicates,
    returns a decorator that remove duplicates from the output list.'''
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        return list(set(f(*args, **kwargs)))

    return wrapper


permutation = deduplicate_output(permutation)
print('Deduplicated: ', permutation(1, 1, 2))
permutation = permutation.__wrapped__
print('Original: ', permutation(1, 1, 2))


# **Exercise:** Create a decorator to eliminate duplicate input positional arguments instead of the ouput, i.e.,  
# `permutation(1,1,2)` will return the same result as `permutation(1,2)`.

# In[ ]:


def deduplicate_input(f):
    '''Takes in a function f that takes a variable number of arguments 
    possibly with duplicates, returns a decorator that remove duplicates 
    in the positional argument.'''
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        # YOUR CODE HERE
        raise NotImplementedError()

    return wrapper


# In[ ]:


# tests
permutation = deduplicate_input(permutation)
assert set(permutation(1,1,2)) == set([(1, 2), (2, 1)])
permutation = permutation.__wrapped__

