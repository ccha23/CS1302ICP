#!/usr/bin/env python
# coding: utf-8

# # Cybersecurity

# **CS1302 Introduction to Computer Programming**
# ___

# Python is a popular tool among hackers and engineers. In this lab, you will learn Cryptology in cybersecurity, which covers
# - [Cryptography](https://en.wikipedia.org/wiki/Cryptography): Encryption and decryption using a cipher.
# - [Cryptanalysis](https://en.wikipedia.org/wiki/Cryptanalysis): Devising an attack to break a cipher.

# ## Caesar symmetric key cipher

# We first implements a simple cipher called the [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher).

# In[ ]:


get_ipython().run_cell_magic('html', '', '<iframe width="912" height="513" src="https://www.youtube.com/embed/sMOZf4GN3oc" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')


# ### Encrypt/decrypt a character

# **How to encrypt a character?**

# The following code encrypts a character `char` using a non-negative integer `key`.

# In[ ]:


cc_n = 1114112


def cc_encrypt_character(char, key):
    '''
    Return the encryption of a character by an integer key using Caesar cipher.
    
    Parameters
    ----------
    char (str): a unicode (UTF-8) character to be encrypted.
    key (int): secret key to encrypt char.
    '''
    char_code = ord(char)
    shifted_char_code = (char_code + key) % cc_n
    encrypted_char = chr(shifted_char_code)
    return encrypted_char


# For example, to encrypt the letter `'A'` using a secret key `5`:

# In[ ]:


cc_encrypt_character('A', 5)


# The character `'A'` is encrypted to the character `'F'` as follows:
# 
# 1. `ord(char)` return the integer `65` that is the code point (integer representation) of the unicode of `'A'`. 
# 2. `(char_code + key) % cc_n` cyclic shifts the code by the key `5`.
# 3. `chr(shifted_char_code)` converts the shifted code back to a character, which is `'F'`.
# 
# | Encryption                      |     |       |     |     |     |     |     |     |
# | ------------------------------- | --- | ----- | --- | --- | --- | --- | --- | --- |
# | `char`                          | ... | **A** | B   | C   | D   | E   | F   | ... |
# | `ord(char)`                     | ... | **65**| 66  | 67  | 68  | 69  | 70  | ... |
# | `(ord(char) + key) % cc_n`      | ... | **70**| 71  | 72  | 73  | 74  | 75  | ... |
# | `(chr(ord(char) + key) % cc_n)` | ... | **F** | G   | H   | I   | J   | K   | ... |

# You may learn more about `ord` and `chr` from their docstrings:

# In[ ]:


help(ord)
help(chr)


# **How to decrypt a character?**

# Mathematically, we define the encryption and decryption of a character for Caesar cipher as
# 
# $$ \begin{aligned} E(x,k) &:= x + k \mod n & \text{(encryption)} \\
# D(x,k) &:= x - k \mod n & \text{(decryption),} \end{aligned}
# $$
# where $x$ is the character code in $\{0,\dots,n\}$ and $k$ is the secret key. `mod` operator above is the modulo operator. In Mathematics, it has a lower precedence than addition and multiplication and is typeset with an extra space accordingly.

# The encryption and decryption satisfies the recoverability condition
# 
# $$ D(E(x,k),k) = x $$
# so two people with a common secret key can encrypt and decrypt a character, but others not knowing the key cannot. This is a defining property of a [symmetric cipher](https://en.wikipedia.org/wiki/Symmetric-key_algorithm).  

# The following code decrypts a character using a key.

# In[ ]:


def cc_decrypt_character(char, key):
    '''
    Return the decryption of a character by the key using Caesar cipher.
    
    Parameters
    ----------
    char (str): a unicode (UTF-8) character to be decrypted.
    key (int): secret key to decrypt char.
    '''
    char_code = ord(char)
    shifted_char_code = (char_code - key) % cc_n
    decrypted_char = chr(shifted_char_code)
    return decrypted_char


# For instance, to decrypt the letter `'F'` by the secret key `5`:

# In[ ]:


cc_decrypt_character('F',5)


# The character `'F'` is decrypted back to `'A'` because
# `(char_code - key) % cc_n` reverse cyclic shifts the code by the key `5`.
# 
# | Encryption                      |     |       |     |     |     |     |     |     | Decryption                      |
# | ------------------------------- | --- | ----- | --- | --- | --- | --- | --- | --- | ------------------------------- |
# | `char`                          | ... | **A** | B   | C   | D   | E   | F   | ... | `(chr(ord(char) - key) % cc_n)` |
# | `ord(char)`                     | ... | **65**| 66  | 67  | 68  | 69  | 70  | ... | `(ord(char) - key) % cc_n`      |
# | `(ord(char) + key) % cc_n`      | ... | **70**| 71  | 72  | 73  | 74  | 75  | ... | `ord(char)`                     |
# | `(chr(ord(char) + key) % cc_n)` | ... | **F** | G   | H   | I   | J   | K   | ... | `char`                          |

# **Exercise** Why did we set `cc_n = 1114112`? Explain whether the recoverability property may fail if we set `cc_n` to a bigger number or remove `% cc_n` for both `cc_encrypt_character` and `cc_decrypt_character`.

# YOUR ANSWER HERE

# ### Encrypt a plaintext and decrypt a ciphertext

# Of course, it is more interesting to encrypt a string instead of a character. The following code implements this in one line.

# In[ ]:


def cc_encrypt(plaintext, key):
    '''
    Return the ciphertext of a plaintext by the key using Caesar cipher.
    
    Parameters
    ----------
    plaintext (str): a unicode (UTF-8) message in to be encrypted.
    key (int): secret key to encrypt plaintext.
    '''
    return ''.join([chr((ord(char) + key) % cc_n) for char in plaintext])


# The above function encrypts a message, referred to as the *plaintext*, by replacing each character with its encryption.  
# This is referred to as a [*substitution cipher*](https://en.wikipedia.org/wiki/Substitution_cipher).

# **Exercise** Define a function `cc_decrypt` that
# - takes a string `ciphertext` and an integer `key`, and
# - returns the plaintext that encrypts to `ciphertext` by the key using Caesar cipher.

# In[ ]:


def cc_decrypt(ciphertext, key):
    '''
    Return the plaintext that encrypts to ciphertext by the key using Caesar cipher.
    
    Parameters
    ----------
    ciphertext (str): message to be decrypted.
    key (int): secret key to decrypt the ciphertext.
    '''
    # YOUR CODE HERE
    raise NotImplementedError()


# In[ ]:


# tests
assert cc_decrypt(r'bcdefghijklmnopqrstuvwxyz{',1) == 'abcdefghijklmnopqrstuvwxyz'
assert cc_decrypt(r'Mjqqt1%\twqi&',5) == 'Hello, World!'


# ## Brute-force attack

# ### Create an English dictionary

# You will launch a brute-force attack to guess the key that encrypts an English text. The idea is simple: 
# 
# - You try decrypting the ciphertext with different keys, and 
# - see which of the resulting plaintexts make most sense (most english-like).

# To check whether a plaintext is English-like, we need to have a list of English words. One way is to type them out
# but this is tedious. Alternatively, we can obtain the list from the *Natural Language Toolkit (NLTK)*: 

# In[ ]:


import nltk
nltk.download('words')
from nltk.corpus import words


# `words.words()` returns a list of words. We can check whether a string is in the list using the operator `in`. 

# In[ ]:


for word in 'Ada', 'ada', 'Hello', 'hello':
    print('{!r} in dictionary? {}'.format(word, word in words.words()))


# However there are two issues:
# - Checking membership is slow for a long list.
# - Both 'Hello' and 'ada' are English-like but they are not in the words_list.

# **Exercise** Using the method `lower` of `str` and the constructor `set`, assign `dictionary` to a set of lowercase English words from `words.words()`.

# In[ ]:


# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


# tests
assert isinstance(dictionary,set) and len(dictionary) == 234377
assert all(word in dictionary for word in ('ada', 'hello'))
assert all(word not in dictionary for word in ('Ada', 'hola'))
### BEGIN TESTS
assert 'world' in dictionary
assert not 'mundo' in dictionary
### END TESTS


# ### Identify English-like text

# To determine how English-like a text is, we calculate the following score:
# 
# $$
# \frac{\text{number of English words in the text}}{\text{number of tokens in the text}} 
# $$
# where tokens are substrings (not necessarily an English word) separated by white space characters in the text.

# In[ ]:


def tokenizer(text):
    '''Returns the list of tokens of the text.'''
    return text.split()

def get_score(text):
    '''Return the fraction of tokens which appear in dictionary.'''
    tokens = tokenizer(text)
    words = [token for token in tokens if token in dictionary]
    return len(words)/len(tokens)

# tests
get_score('hello world'), get_score('Hello, World!')


# As shown in tests above, the code fails to handle text with punctuations and uppercase letters properly.  
# In particular, 
# - while `get_score` recognizes `hello world` as English-like and returns the maximum score of 1, 
# - it fails to recognize `Hello, World!` as English-like and returns the minimum score of 0.

# Why? This is because every words in `dictionary`
# - are in lowercase, and
# - have no leading/trailing punctuations.

# **Exercise** Define a funtion `tokenizer` that 
# - takes a string `text` as an argument, and
# - returns a `list` of tokens obtained by
#   1. splitting `text` into a list using `split()`;
#   2. removing leading/trailing punctuations in `string.punctuation` using the `strip` method; and
#   3. converting all items of the list to lowercase using `lower()`.

# In[ ]:


import string

def tokenizer(text):
    '''Returns the list of tokens of the text such that 
    1) each token has no leading or training spaces/punctuations, and 
    2) all letters in each tokens are in lowercase.'''
    # YOUR CODE HERE
    raise NotImplementedError()


# In[ ]:


# tests
assert tokenizer('Hello, World!') == ['hello', 'world']
assert get_score('Hello, World!') >= 0.99999
assert tokenizer('Do you know Jean-Pierre?') == ['do', 'you', 'know', 'jean-pierre']
assert get_score('Do you know Jean-Pierre?') >= 0.99999


# ### Launch a brute-force attack

# **Exercise** Define the function `cc_attack` that 
# - takes as arguments
#     - a string `ciphertext`,
#     - a floating point number `threshold` in the interval $(0,1)$ with a default value of $0.6$, and
# - returns a generator that  
#     - generates one-by-one in ascending order guesses of the key that
#     - decrypt `ciphertext` to texts with scores at least the `threshold`.

# In[ ]:


def cc_attack(ciphertext, threshold = 0.6):
    '''Returns a generator that generates the next guess of the key that 
    decrypts the ciphertext to a text with get_score(text) at least the threshold.
    '''
    # YOUR CODE HERE
    raise NotImplementedError()


# In[ ]:


# tests
ciphertext = cc_encrypt("Hello, World!",12345)
key_generator = cc_attack(ciphertext)
key_guess = next(key_generator)
assert key_guess == 12345
text = cc_decrypt(ciphertext, key_guess)
print('guess of the key: {}\nscore: {}\ntext :{}'.format(key_guess,get_score(text),text))


# ## Challenge

# Another symmetric key cipher is [columnar transposition cipher](https://en.wikipedia.org/wiki/Transposition_cipher#Columnar_transposition). A transposition cipher encrypts a text by permuting instead of substituting characters.

# **Exercise** Study and implement the irregular case of the [columnar transposition cipher](https://en.wikipedia.org/wiki/Transposition_cipher#Columnar_transposition) as described in Wikipedia page. Define the functions 
# - `ct_encrypt(plaintext, key)` for encryption, and 
# - `ct_decrypt(ciphertext, key)` for decryption. 
# 
# You can assume the plaintext is in uppercase and has no spaces/punctuations. 

# *Hints:* See the text cases for an example of `plaintext`, `key`, and the corresponding `ciphertext`. You can but are not required to follow the solution template below:
# 
# ```Python
# def argsort(seq):
#     '''A helper function that returns the tuple of indices that would sort the
#     sequence seq.'''
#     return tuple(x[0] for x in sorted(enumerate(seq), key=lambda x: x[1]))
# 
# 
# def ct_idx(length, key):
#     '''A helper function that returns the tuple of indices that would permute 
#     the letters of a message according to the key using the irregular case of 
#     columnar transposition cipher.'''
#     seq = tuple(range(length))
#     return [i for j in argsort(key) for i in _______________]
# 
# 
# def ct_encrypt(plaintext, key):
#     '''
#     Return the ciphertext of a plaintext by the key using the irregular case
#     of columnar transposition cipher.
#     
#     Parameters
#     ----------
#     plaintext (str): a message in uppercase without punctuations/spaces.
#     key (str): secret key to encrypt plaintext.
#     '''
#     return ''.join([plaintext[i] for i in ct_idx(len(plaintext), key)])
# 
# 
# def ct_decrypt(ciphertext, key):
#     '''
#     Return the plaintext of the ciphertext by the key using the irregular case
#     of columnar transposition cipher.
#     
#     Parameters
#     ----------
#     ciphertext (str): a string in uppercase without punctuations/spaces.
#     key (str): secret key to decrypt ciphertext.
#     '''        
#     return _______________________________________________________________________
# ```

# In[ ]:


# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


# tests
key = 'ZEBRAS'
plaintext = 'WEAREDISCOVEREDFLEEATONCE'
ciphertext = 'EVLNACDTESEAROFODEECWIREE'
assert ct_encrypt(plaintext, key) == ciphertext
assert ct_decrypt(ciphertext, key) == plaintext

