#!/usr/bin/env python
# coding: utf-8

# # Information Theory

# **CS1302 Introduction to Computer Programming**
# ___

# As mentioned in previous lectures, the following two lists `coin_flips` and `dice_rolls` simulate the random coin flips and rollings of a dice:

# In[ ]:


# Do NOT modify any variables defined here because some tests rely on them
import random
random.seed(0)  # for reproducible results.
num_trials = 200
coin_flips = ['H' if random.random() <= 1/2 else 'T' for i in range(num_trials)]
dice_rolls = [random.randint(1,6) for i in range(num_trials)]
print('coin flips: ',*coin_flips)
print('dice rolls: ',*dice_rolls)


# **What is the difference of the two random processes?  
# Can we say one process has more information content than the other?**

# In this Lab, we will use dictionaries to store their distributions and then compute their information content using information theory, which was introduced by *Claude E. Shannon*. It has [numerous applications](https://www.khanacademy.org/computing/computer-science/informationtheory): 
# - *compression* (to keep files small)
# - *communications* (to send data mobile phones), and 
# - *machine learning* (to identify relevant features to learn from). 

# ## Entropy

# Mathematically, we denote a distribution as $\mathbf{p}=[p_i]_{i\in \mathcal{S}}$, where 
# - $\mathcal{S}$ is the set of distinct outcomes, and
# - $p_i$ denotes the probability (chance) of seeing outcome $i$.

# The following code shown in the lecture uses a dictionary to store the distribution for a sequence efficiently without storing outcomes with zero counts:

# In[ ]:


# Do NOT modify any variables defined here because some tests rely on them
def distribute(seq):
    '''Returns a dictionary where each value in a key-value pair is 
    the probability of the associated key occuring in the sequence.
    '''
    p = {}
    for i in seq:
            p[i] = p.get(i,0) + 1/len(seq)
    return p

# tests
coin_flips_dist = distribute(coin_flips)
dice_rolls_dist = distribute(dice_rolls)
print('Distribution of coin flips:', coin_flips_dist)
print('Distribution of dice rolls:', dice_rolls_dist)


# For $\mathbf{p}$ to be a valid distribution, the probabilities $p_i$'s have to sum to $1$, i.e.,
# 
# $$\sum_{i\in \mathcal{S}} p_i = 1, $$
# which can be verified as follows:

# In[ ]:


import math
assert math.isclose(sum(coin_flips_dist.values()),1) and math.isclose(sum(dice_rolls_dist.values()),1)


# **How to measure the information content?**

# In[ ]:


get_ipython().run_cell_magic('html', '', '<iframe width="912" height="513" src="https://www.youtube.com/embed/2s3aJfRr9gE" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')


# In information theory, the information content of a distribution is measured by its [*entropy*](https://en.wikipedia.org/wiki/Entropy_(information_theory)) defined as:
# 
# $$ \begin{aligned} H(\mathbf{p}) &:= \sum_{i\in \mathcal{S}} p_i \overbrace{\log_2 \tfrac{1}{p_i}}^{\text{called surprise} } \\ &= - \sum_{i\in \mathcal{S}} p_i \log_2 p_i \kern1em \text{(bits)} \end{aligned}  $$
# with $p_i \log_2 \frac{1}{p_i} = 0$ if $p_i = 0$ because $\lim_{x\downarrow 0} x \log_2 \frac1x = 0$.

# For instance, if $\mathbf{p}=(p_{H},p_{T})=(0.5,0.5)$, then
# 
# $$\begin{aligned} H(\mathbf{p}) &= 0.5 \log_2 \frac{1}{0.5} + 0.5 \log_2 \frac{1}{0.5} \\ &= 0.5 + 0.5 = 1  \text{ bit,}\end{aligned} $$
# i.e., an outcome of a fair coin flip has one bit of information content, as expected. 

# On the other hand, if $\mathbf{p}=(p_{H},p_{T})=(1,0)$, then
# $$\begin{aligned} H(\mathbf{p}) &= 1 \log_2 \frac{1}{1} + 0 \log_2 \frac{1}{0} \\ &= 0 + 0 = 0  \text{ bits,}\end{aligned} $$
# i.e., an outcome of a biased coin flip that always comes up head has no information content, again as expected.

# **Exercise** Define a function `entropy` that
# - takes a distribution $\mathbf{p}$ as its argument, and
# - returns the entropy $H(\mathbf{p})$.
# 
# Handle the case when $p_i=0$, e.g., using the short-circuit evaluation of logical `and`.

# In[ ]:


def entropy(dist):
    # YOUR CODE HERE
    raise NotImplementedError()


# In[ ]:


# tests
assert math.isclose(entropy({'H': 0.5, 'T': 0.5}), 1)
assert math.isclose(entropy({'H': 1, 'T': 0}), 0)
assert math.isclose(entropy(dict.fromkeys(range(1, 7), 1 / 6)), math.log2(6))


# ## Uniform distribution maximizes entropy

# Intuitively,
# - for large enough numbers of fair coin flips, we should have $\mathcal{S}=\{H,T\}$ and $p_H=p_T=0.5$, i.e., equal chance for head and tail.
# - for large enough numbers of fair dice rolls, we should have $p_i=\frac16$ for all $i\in \mathcal{S}=\{1,2,3,4,5,6\}$.

# In[ ]:


import matplotlib.pyplot as plt

def plot_distribution(seq):
    dist = distribute(seq)
    plt.stem(dist.keys(),   # set-like view of the keys
             dist.values(), # view of the values
             use_line_collection=True)
    plt.xlabel('Outcomes')
    plt.title('Distribution')
    plt.ylim(0, 1)
    
import ipywidgets as widgets
n_widget = widgets.IntSlider(
    value=1,
    min=1,
    max=num_trials,
    step=1,
    description='n:',
    continuous_update=False,
)

widgets.interactive(lambda n: plot_distribution(coin_flips[:n]),n=n_widget)


# In[ ]:


widgets.interactive(lambda n: plot_distribution(dice_rolls[:n]),n=n_widget)


# A distribution is called a *uniform distribution* if all its distinct outcomes have the same probability of occuring, i.e.,
# 
# $$ p_i = \frac{1}{|\mathcal{S}|}\kern1em  \text{for all }i\in \mathcal{S},  $$
# where $|\mathcal{S}|$ is the mathematical notation to denote the size of the set $\mathcal{S}$.

# **Exercise** Define a function `uniform` that
# - takes a sequence of possibly duplicate outcomes, and
# - returns a uniform distribution on the distinct outcomes.

# In[ ]:


def uniform(outcomes):
    '''Returns the uniform distribution (dict) over distinct items in outcomes.'''
    # YOUR CODE HERE
    raise NotImplementedError()


# In[ ]:


# tests
assert uniform('HT') == {'H': 0.5, 'T': 0.5}
assert uniform('HTH') == {'H': 0.5, 'T': 0.5}
fair_dice_dist = uniform(range(1, 7))
assert all(
    math.isclose(fair_dice_dist[k], v) for k, v in {
        1: 0.16666666666666666,
        2: 0.16666666666666666,
        3: 0.16666666666666666,
        4: 0.16666666666666666,
        5: 0.16666666666666666,
        6: 0.16666666666666666
    }.items())


# **What is the entropy for uniform distributions?**

# By definition,
# 
# $$ \begin{aligned} H(\mathbf{p}) &:= \sum_{i\in \mathcal{S}} p_i \log_2 \tfrac{1}{p_i} \\ &= \sum_{i\in \mathcal{S}} \frac{1}{|\mathcal{S}|} \log_2 |\mathcal{S}| = \log_2 |\mathcal{S}|  \kern1em \text{(bits)} \end{aligned}  $$
# 
# This reduces to the formula you learned in Lecture 1 and Lab 1 regarding the number of bits required to represent a set. This is the maximum possible entropy for a given finite set of possible outcomes.

# You can use this result to test whether you have implemented both `entropy` and `uniform` correctly:

# In[ ]:


assert all(math.isclose(entropy(uniform(range(n))), math.log2(n)) for n in range(1,100)) 


# ## Joint distribution and its entropy

# If we duplicate a sequence of outcomes multiple times, the total information content should remain unchanged, NOT doubled, because the duplicate contain the same information as the original. We will verify this fact by creating a [joint distribution](https://en.wikipedia.org/wiki/Joint_probability_distribution) 
# 
# $$\mathbf{p}=[p_{ij}]_{i\in \mathcal{S},j\in \mathcal{T}}$$ 
# - where $\mathcal{S}$ and $\mathcal{T}$ are sets of outcomes; and
# - $p_{ij}$ is the chance we see outcomes $i$ and $j$ simultaneously. 
# 
# The subscript $ij$ in $p_{ij}$ denotes a tuple $(i,j)$, NOT the multiplication $i\times j$. We also have
# 
# $$\sum_{i\in \mathcal{S}} \sum_{j\in \mathcal{T}} p_{ij} = 1.$$
# 
# 
# 
# 

# **Exercise** Define a function `jointly_distribute` that 
# - takes two sequences `seq1` and `seq2` of outcomes with the same length, and
# - returns the joint distribution represented as a dictionary where each key-value pair has the key being a tuple `(i,j)` associated with the probability $p_{ij}$ of seeing `(i,j)` in `zip(seq1,seq2)`.

# In[ ]:


def jointly_distribute(seq1, seq2):
    '''Returns the joint distribution of the tuple (i,j) of outcomes from zip(seq1,seq2).'''
    # YOUR CODE HERE
    raise NotImplementedError()


# In[ ]:


# tests
assert jointly_distribute('HT', 'HT') == {('H', 'H'): 0.5, ('T', 'T'): 0.5}
assert jointly_distribute('HHTT', 'HTHT') == {
    ('H', 'H'): 0.25,
    ('H', 'T'): 0.25,
    ('T', 'H'): 0.25,
    ('T', 'T'): 0.25
}
coin_flips_duplicate_dist = {
    ('T', 'T'): 0.5350000000000004,
    ('H', 'H'): 0.4650000000000003
}
coin_flips_duplicate_ans = jointly_distribute(coin_flips, coin_flips)
assert all(
    math.isclose(coin_flips_duplicate_ans[i], pi)
    for i, pi in coin_flips_duplicate_dist.items())


# If you have implemented `entropy` and `jointly_distribute` correctly, you can verify that duplicating a sequence will give the same entropy.

# In[ ]:


assert math.isclose(entropy(jointly_distribute(coin_flips,coin_flips)), entropy(distribute(coin_flips)))
assert math.isclose(entropy(jointly_distribute(dice_rolls,dice_rolls)), entropy(distribute(dice_rolls)))


# However, for two sequences generated independently, the joint entropy is roughly the sum of the individual entropies.

# In[ ]:


coin_flips_entropy = entropy(distribute(coin_flips))
dice_rolls_entropy = entropy(distribute(dice_rolls))
cf_dr_entropy = entropy(jointly_distribute(coin_flips, dice_rolls))
print(f'''Entropy of coin flip: {coin_flips_entropy}
Entropy of dice roll: {dice_rolls_entropy}
Sum of the above entropies: {coin_flips_entropy + dice_rolls_entropy}
Joint entropy: {cf_dr_entropy}''')


# ## Conditional distribution and entropy

# Mathematically, we denote a [conditional distribution](https://en.wikipedia.org/wiki/Conditional_probability_distribution) as $\mathbf{q}:=[q_{j|i}]_{i\in \mathcal{S}, j\in \mathcal{T}}$, where 
# - $\mathcal{S}$ and $\mathcal{T}$ are two sets of distinct outcomes, and
# - $q_{j|i}$ denotes the probability (chance) of seeing outcome $j$ given the condition that outcome $i$ is observed.
# 
# For $\mathbf{q}$ to be a valid distribution, the probabilities $q_{j|i}$'s have to sum to $1$ for every $i$, i.e.,
# 
# $$\sum_{j\in \mathcal{T}} q_{j|i} = 1 \kern1em \text{for all }i\in \mathcal{S} $$

# For example, suppose we want to compute the distribution of coin flips given dice rolls, then the following assign `q_H_1` and `q_T_1` to the values $q_{H|1}$ and $q_{T|1}$ respectively:

# In[ ]:


coin_flips_1 = [j for i, j in zip(dice_rolls, coin_flips) if i == 1]
q_H_1 = coin_flips_1.count('H') / len(coin_flips_1)
q_T_1 = coin_flips_1.count('T') / len(coin_flips_1)
print('Coin flips given dice roll is 1:', coin_flips_1)
print('Distribution of coin flip given dice roll is 1: {{ "H": {}, "T": {}}}'.format(q_H_1, q_T_1))
assert math.isclose(q_H_1 + q_T_1, 1)


# Note that `q_H_1 + q_T_1` is 1 as expected. Similarly, we can assign `q_H_2` and `q_T_2` to the values $q_{H|2}$ and $q_{T|2}$ respectively.

# In[ ]:


coin_flips_2 = [j for i, j in zip(dice_rolls, coin_flips) if i == 2]
q_H_2 = coin_flips_2.count('H') / len(coin_flips_2)
q_T_2 = coin_flips_2.count('T') / len(coin_flips_2)
print('Coin flips given dice roll is 2:', coin_flips_2)
print('Distribution of coin flip given dice roll is 2: {{ "H": {}, "T": {}}}'.format(q_H_2, q_T_2))
assert math.isclose(q_H_2 + q_T_2, 1)


# Finally, we want to store the conditional distribution as a nested dictionary so that `q[i]` points to the distribution 
# 
# $$[q_{j|i}]_{j\in \mathcal{T}} \kern1em \text{for }i\in \mathcal{S}.$$

# In[ ]:


q = {}
q[1] = dict(zip('HT',(q_H_1, q_T_1)))
q[2] = dict(zip('HT',(q_H_2, q_T_2)))
q


# Of course, the above dictionary is missing the entries for other possible outcomes of the dice rolls.

# **Exercise** Define a function `conditionally_distribute` that
# - takes two sequences `seq1` and `seq2` of outcomes of the same length, and
# - returns the conditional distribution of `seq2` given `seq1` in the form of a nested dictionary efficiently without storing the unobserved outcomes.
# 
# In the above example, `seq1` is `dice_rolls` while `seq2` is `coin_flips`.
# 
# *Hint:* For an efficient implementation without traversing the input sequences too many times, consider using the following solution template and the `setdefault` method.
# ```Python
# def conditionally_distribute(seq1, seq2):
#     q, count = {}, {}  # NOT q = count = {}
#     for i in seq1:
#         count[i] = count.get(i, 0) + 1
#     for i, j in zip(seq1, seq2):
#         q[i][j] = ____________________________________________________
#     return q
# ```

# In[ ]:


def conditionally_distribute(seq1, seq2):
    '''Returns the conditional distribution q of seq2 given seq1 such that
    q[i] is a dictionary for observed outcome i in seq1 and
    q[i][j] is the probability of observing j in seq2 given the 
    corresponding outcome in seq1 is i.'''
    # YOUR CODE HERE
    raise NotImplementedError()


# In[ ]:


# tests
cf_given_dr_dist = {
    4: {
        'T': 0.5588235294117647,
        'H': 0.4411764705882353
    },
    1: {
        'T': 0.46511627906976744,
        'H': 0.5348837209302325
    },
    3: {
        'H': 0.5135135135135135,
        'T': 0.4864864864864865
    },
    6: {
        'H': 0.5454545454545454,
        'T': 0.45454545454545453
    },
    2: {
        'T': 0.7586206896551724,
        'H': 0.2413793103448276
    },
    5: {
        'T': 0.5416666666666666,
        'H': 0.4583333333333333
    }
}
cf_given_dr_ans = conditionally_distribute(dice_rolls, coin_flips)
assert all(
    math.isclose(cf_given_dr_ans[i][j], v)
    for i, d in cf_given_dr_dist.items() for j, v in d.items())


# The [*conditional entropy*](https://en.wikipedia.org/wiki/Conditional_entropy) is defined for a conditional distribution $\mathbf{q}=[q_{j|i}]_{i\in \mathcal{S},j\in\mathcal{T}}$ and a distribution $\mathbf{p}=[p_i]_{i\in \mathcal{S}}$ as follows:
# 
# $$ H(\mathbf{q}|\mathbf{p}) = \sum_{i\in \mathcal{S}} p_i \sum_{j\in \mathcal{T}} q_{j|i} \log_2 \frac{1}{q_{j|i}}, $$
# where, by convention,  
# - the summand of the outer sum is 0 if $p_i=0$ (regardless of the values of $q_{j|i}$), and
# - the summand of the inner sum is 0 if $q_{j|i}=0$.

# **Exercise** Define a function `conditional_entropy` that
# - takes 
#   - a distribution p as its first argument,
#   - a conditional distribution q as its second argument, and
# - returns the conditional entropy $H(\mathbf{q}|\mathbf{p})$.
# 
# Handle the cases when $p_i=0$ and $q_{j|i}=0$ as well.

# In[ ]:


# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


# tests
cf_given_dr_dist = {
    4: {
        'T': 0.5588235294117647,
        'H': 0.4411764705882353
    },
    1: {
        'T': 0.46511627906976744,
        'H': 0.5348837209302325
    },
    3: {
        'H': 0.5135135135135135,
        'T': 0.4864864864864865
    },
    6: {
        'H': 0.5454545454545454,
        'T': 0.45454545454545453
    },
    2: {
        'T': 0.7586206896551724,
        'H': 0.2413793103448276
    },
    5: {
        'T': 0.5416666666666666,
        'H': 0.4583333333333333
    }
}
assert conditional_entropy({'H': 0.5, 'T': 0.5},{'H': {'H': 0.5, 'T': 0.5}, 'T': {'H': 0.5, 'T': 0.5}}) == 1
assert conditional_entropy({'H': 0, 'T': 1},{'H': {'H': 0.5, 'T': 0.5}, 'T': {'H': 0.5, 'T': 0.5}}) == 1
assert conditional_entropy({'H': 0.5, 'T': 0.5},{'H': {'H': 1, 'T': 0}, 'T': {'H': 0, 'T': 1}}) == 0
assert conditional_entropy({'H': 0.5, 'T': 0.5},{'H': {'H': 1, 'T': 0}, 'T': {'H': 0.5, 'T': 0.5}}) == 0.5
assert math.isclose(conditional_entropy(dice_rolls_dist, cf_given_dr_dist), 0.9664712793722372)


# The joint probability $p_{ij}$ over $i\in \mathcal{S}$ and $j\in \mathcal{T}$ can be calculated as follows
# 
# $$p_{ij} = p_{i} q_{j|i}$$
# where $p_i$ is the probability of $i$ and $q_{j|i}$ is the conditional probability of $j$ given $i$.

# **Exercise** Define a function `joint_distribution` that
# - takes the distribution $p$ and conditional distribution $q$ as arguments, and
# - returns their joint distribution.

# In[ ]:


def joint_distribution(p,q):
    # YOUR CODE HERE
    raise NotImplementedError()


# In[ ]:


# tests
assert joint_distribution({'H': 0.5, 'T': 0.5},{'H': {'H': 0.5, 'T': 0.5}, 'T': {'H': 0.5, 'T': 0.5}}) == {('H', 'H'): 0.25, ('H', 'T'): 0.25, ('T', 'H'): 0.25, ('T', 'T'): 0.25}
assert joint_distribution({'H': 0, 'T': 1},{'H': {'H': 0.5, 'T': 0.5}, 'T': {'H': 0.5, 'T': 0.5}}) == {('H', 'H'): 0.0, ('H', 'T'): 0.0, ('T', 'H'): 0.5, ('T', 'T'): 0.5}
assert joint_distribution({'H': 0.5, 'T': 0.5},{'H': {'H': 1, 'T': 0}, 'T': {'H': 0, 'T': 1}}) == {('H', 'H'): 0.5, ('H', 'T'): 0.0, ('T', 'H'): 0.0, ('T', 'T'): 0.5}, {'H': 0.5, 'T': 0.5}


# Finally, a fundamental information identity, called the [*chain rule*](https://en.wikipedia.org/wiki/Conditional_entropy#Chain_rule), is that the joint entropy is equal to
# 
# $$ H(\mathbf{p}) + H(\mathbf{q}|\mathbf{p})$$
# for any distribution $\mathbf{p}$ over outcome $i\in \mathcal{S}$ and conditional distribution $\mathbf{q}$ over outcome $j\in \mathcal{T}$ given outcome $i \in \mathcal{S}$. 

# If you have implemented `jointly_distribute`, `conditionally_distribute`, `entropy`, and `conditional_entropy` correctly, we can verify the identity as follows.

# In[ ]:


def validate_chain_rule(seq1,seq2):
    p = distribute(seq1)
    q = conditionally_distribute(seq1,seq2)
    pq = jointly_distribute(seq1,seq2)
    H_pq = entropy(pq)
    H_p = entropy(p)
    H_q_p = conditional_entropy(p,q)
    print(f'''Entropy of seq1: {H_p}
Conditional entropy of seq2 given seq1: {H_q_p}
Sum of the above entropies: {H_p + H_q_p}
Joint entropy: {H_pq}''')
    assert math.isclose(H_pq,H_p + H_q_p)


# In[ ]:


validate_chain_rule(coin_flips,coin_flips)


# In[ ]:


validate_chain_rule(dice_rolls,coin_flips)

