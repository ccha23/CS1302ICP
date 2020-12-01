#!/usr/bin/env python
# coding: utf-8

# # Card guessing game
# CS1302 Introduction to Computer Programming
# ___

# ## Rules of the game

# Consider a deck of 52 cards:
# <table>
#     <tr>
#         <td></td>
#         <th>1 (A)</th>
#         <th>2</th>
#         <th>3</th>
#         <th>4</th>
#         <th>5</th>
#         <th>6</th>
#         <th>7</th>
#         <th>8</th>
#         <th>9</th>
#         <th>10</th>
#         <th>11 (J)</th>
#         <th>12 (Q)</th>
#         <th>13 (K)</th>
#     </tr>
#     <tr>
#         <th style="transform: rotate(-90deg);">Diamond</th>
#         <td><a title="GW Simulations / Public domain" href="https://commons.wikimedia.org/wiki/File:Cards-A-Diamond.svg"><img width="50" alt="Cards-A-Diamond" src="https://upload.wikimedia.org/wikipedia/commons/e/e9/Cards-A-Diamond.svg"></a></td>
#         <td><a title="GW Simulations / Public domain" href="https://commons.wikimedia.org/wiki/File:Cards-2-Diamond.svg"><img width="50" alt="Cards-2-Diamond" src="https://upload.wikimedia.org/wikipedia/commons/9/99/Cards-2-Diamond.svg"></a></td>
#         <td><a title="GW Simulations / Public domain" href="https://commons.wikimedia.org/wiki/File:Cards-3-Diamond.svg"><img width="50" alt="Cards-3-Diamond" src="https://upload.wikimedia.org/wikipedia/commons/4/44/Cards-3-Diamond.svg"></a></td>
#         <td><a title="GW Simulations / Public domain" href="https://commons.wikimedia.org/wiki/File:Cards-4-Diamond.svg"><img width="50" alt="Cards-4-Diamond" src="https://upload.wikimedia.org/wikipedia/commons/a/af/Cards-4-Diamond.svg"></a></td>
#         <td><a title="GW Simulations / Public domain" href="https://commons.wikimedia.org/wiki/File:Cards-5-Diamond.svg"><img width="50" alt="Cards-5-Diamond" src="https://upload.wikimedia.org/wikipedia/commons/d/dd/Cards-5-Diamond.svg"></a></td>
#         <td><a title="GW Simulations / Public domain" href="https://commons.wikimedia.org/wiki/File:Cards-6-Diamond.svg"><img width="50" alt="Cards-6-Diamond" src="https://upload.wikimedia.org/wikipedia/commons/4/44/Cards-6-Diamond.svg"></a></td>
#         <td><a title="GW Simulations / Public domain" href="https://commons.wikimedia.org/wiki/File:Cards-7-Diamond.svg"><img width="50" alt="Cards-7-Diamond" src="https://upload.wikimedia.org/wikipedia/commons/2/2b/Cards-7-Diamond.svg"></a></td>
#         <td><a title="GW Simulations / Public domain" href="https://commons.wikimedia.org/wiki/File:Cards-8-Diamond.svg"><img width="50" alt="Cards-8-Diamond" src="https://upload.wikimedia.org/wikipedia/commons/9/90/Cards-8-Diamond.svg"></a></td>
#         <td><a title="GW Simulations / Public domain" href="https://commons.wikimedia.org/wiki/File:Cards-9-Diamond.svg"><img width="50" alt="Cards-9-Diamond" src="https://upload.wikimedia.org/wikipedia/commons/2/25/Cards-9-Diamond.svg"></a></td>
#         <td><a title="GW Simulations / Public domain" href="https://commons.wikimedia.org/wiki/File:Cards-10-Diamond.svg"><img width="50" alt="Cards-10-Diamond" src="https://upload.wikimedia.org/wikipedia/commons/c/c2/Cards-10-Diamond.svg"></a></td>
#         <td><a title="GW Simulations / Public domain" href="https://commons.wikimedia.org/wiki/File:Cards-J-Diamond.svg"><img width="50" alt="Cards-J-Diamond" src="https://upload.wikimedia.org/wikipedia/commons/7/78/Cards-J-Diamond.svg"></a></td>
#         <td><a title="GW Simulations / Public domain" href="https://commons.wikimedia.org/wiki/File:Cards-Q-Diamond.svg"><img width="50" alt="Cards-Q-Diamond" src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Cards-Q-Diamond.svg"></a></td>
#         <td><a title="GW Simulations / Public domain" href="https://commons.wikimedia.org/wiki/File:Cards-K-Diamond.svg"><img width="50" alt="Cards-K-Diamond" src="https://upload.wikimedia.org/wikipedia/commons/5/55/Cards-K-Diamond.svg"></a></td>
#     </tr>
#     <tr>
#         <th style="transform: rotate(-90deg);">Club</th>
#         <td><a title="GW Simulations / Public domain" href="https://commons.wikimedia.org/wiki/File:Cards-A-Club.svg"><img width="50" alt="Cards-A-Club" src="https://upload.wikimedia.org/wikipedia/commons/c/c4/Cards-A-Club.svg"></a></td>
#         <td><a title="GW Simulations / Public domain" href="https://commons.wikimedia.org/wiki/File:Cards-2-Club.svg"><img width="50" alt="Cards-2-Club" src="https://upload.wikimedia.org/wikipedia/commons/b/b0/Cards-2-Club.svg"></a></td>
#         <td><a title="GW Simulations / Public domain" href="https://commons.wikimedia.org/wiki/File:Cards-3-Club.svg"><img width="50" alt="Cards-3-Club" src="https://upload.wikimedia.org/wikipedia/commons/e/e0/Cards-3-Club.svg"></a></td>
#         <td><a title="GW Simulations / Public domain" href="https://commons.wikimedia.org/wiki/File:Cards-4-Club.svg"><img width="50" alt="Cards-4-Club" src="https://upload.wikimedia.org/wikipedia/commons/6/69/Cards-4-Club.svg"></a></td>
#         <td><a title="GW Simulations / Public domain" href="https://commons.wikimedia.org/wiki/File:Cards-5-Club.svg"><img width="50" alt="Cards-5-Club" src="https://upload.wikimedia.org/wikipedia/commons/7/7e/Cards-5-Club.svg"></a></td>
#         <td><a title="GW Simulations / Public domain" href="https://commons.wikimedia.org/wiki/File:Cards-6-Club.svg"><img width="50" alt="Cards-6-Club" src="https://upload.wikimedia.org/wikipedia/commons/a/af/Cards-6-Club.svg"></a></td>
#         <td><a title="GW Simulations / Public domain" href="https://commons.wikimedia.org/wiki/File:Cards-7-Club.svg"><img width="50" alt="Cards-7-Club" src="https://upload.wikimedia.org/wikipedia/commons/8/8e/Cards-7-Club.svg"></a></td>
#         <td><a title="GW Simulations / Public domain" href="https://commons.wikimedia.org/wiki/File:Cards-8-Club.svg"><img width="50" alt="Cards-8-Club" src="https://upload.wikimedia.org/wikipedia/commons/f/fd/Cards-8-Club.svg"></a></td>
#         <td><a title="GW Simulations / Public domain" href="https://commons.wikimedia.org/wiki/File:Cards-9-Club.svg"><img width="50" alt="Cards-9-Club" src="https://upload.wikimedia.org/wikipedia/commons/a/ac/Cards-9-Club.svg"></a></td>
#         <td><a title="GW Simulations / Public domain" href="https://commons.wikimedia.org/wiki/File:Cards-10-Club.svg"><img width="50" alt="Cards-10-Club" src="https://upload.wikimedia.org/wikipedia/commons/2/25/Cards-10-Club.svg"></a></td>
#         <td><a title="GW Simulations / Public domain" href="https://commons.wikimedia.org/wiki/File:Cards-J-Club.svg"><img width="50" alt="Cards-J-Club" src="https://upload.wikimedia.org/wikipedia/commons/c/c7/Cards-J-Club.svg"></a></td>
#         <td><a title="GW Simulations / Public domain" href="https://commons.wikimedia.org/wiki/File:Cards-Q-Club.svg"><img width="50" alt="Cards-Q-Club" src="https://upload.wikimedia.org/wikipedia/commons/3/37/Cards-Q-Club.svg"></a></td>
#         <td><a title="GW Simulations / Public domain" href="https://commons.wikimedia.org/wiki/File:Cards-K-Club.svg"><img width="50" alt="Cards-K-Club" src="https://upload.wikimedia.org/wikipedia/commons/9/9e/Cards-K-Club.svg"></a></td>
#     </tr>
#     <tr>
#         <th style="transform: rotate(-90deg);">Heart</th>
#         <td><a title="GW Simulations / Public domain" href="https://commons.wikimedia.org/wiki/File:Cards-A-Heart.svg"><img width="50" alt="Cards-A-Heart" src="https://upload.wikimedia.org/wikipedia/commons/6/60/Cards-A-Heart.svg"></a></td>
#         <td><a title="GW Simulations / Public domain" href="https://commons.wikimedia.org/wiki/File:Cards-2-Heart.svg"><img width="50" alt="Cards-2-Heart" src="https://upload.wikimedia.org/wikipedia/commons/6/6e/Cards-2-Heart.svg"></a></td>
#         <td><a title="GW Simulations / Public domain" href="https://commons.wikimedia.org/wiki/File:Cards-3-Heart.svg"><img width="50" alt="Cards-3-Heart" src="https://upload.wikimedia.org/wikipedia/commons/5/57/Cards-3-Heart.svg"></a></td>
#         <td><a title="GW Simulations / Public domain" href="https://commons.wikimedia.org/wiki/File:Cards-4-Heart.svg"><img width="50" alt="Cards-4-Heart" src="https://upload.wikimedia.org/wikipedia/commons/3/39/Cards-4-Heart.svg"></a></td>
#         <td><a title="GW Simulations / Public domain" href="https://commons.wikimedia.org/wiki/File:Cards-5-Heart.svg"><img width="50" alt="Cards-5-Heart" src="https://upload.wikimedia.org/wikipedia/commons/9/91/Cards-5-Heart.svg"></a></td>
#         <td><a title="GW Simulations / Public domain" href="https://commons.wikimedia.org/wiki/File:Cards-6-Heart.svg"><img width="50" alt="Cards-6-Heart" src="https://upload.wikimedia.org/wikipedia/commons/5/55/Cards-6-Heart.svg"></a></td>
#         <td><a title="GW Simulations / Public domain" href="https://commons.wikimedia.org/wiki/File:Cards-7-Heart.svg"><img width="50" alt="Cards-7-Heart" src="https://upload.wikimedia.org/wikipedia/commons/d/d4/Cards-7-Heart.svg"></a></td>
#         <td><a title="GW Simulations / Public domain" href="https://commons.wikimedia.org/wiki/File:Cards-8-Heart.svg"><img width="50" alt="Cards-8-Heart" src="https://upload.wikimedia.org/wikipedia/commons/5/55/Cards-8-Heart.svg"></a></td>
#         <td><a title="GW Simulations / Public domain" href="https://commons.wikimedia.org/wiki/File:Cards-9-Heart.svg"><img width="50" alt="Cards-9-Heart" src="https://upload.wikimedia.org/wikipedia/commons/d/d2/Cards-9-Heart.svg"></a></td>
#         <td><a title="GW Simulations / Public domain" href="https://commons.wikimedia.org/wiki/File:Cards-10-Heart.svg"><img width="50" alt="Cards-10-Heart" src="https://upload.wikimedia.org/wikipedia/commons/7/76/Cards-10-Heart.svg"></a></td>
#         <td><a title="GW Simulations / Public domain" href="https://commons.wikimedia.org/wiki/File:Cards-J-Heart.svg"><img width="50" alt="Cards-J-Heart" src="https://upload.wikimedia.org/wikipedia/commons/e/e7/Cards-J-Heart.svg"></a></td>
#         <td><a title="GW Simulations / Public domain" href="https://commons.wikimedia.org/wiki/File:Cards-Q-Heart.svg"><img width="50" alt="Cards-Q-Heart" src="https://upload.wikimedia.org/wikipedia/commons/2/28/Cards-Q-Heart.svg"></a></td>
#         <td><a title="GW Simulations / Public domain" href="https://commons.wikimedia.org/wiki/File:Cards-K-Heart.svg"><img width="50" alt="Cards-K-Heart" src="https://upload.wikimedia.org/wikipedia/commons/b/bf/Cards-K-Heart.svg"></a></td>
#     </tr>        
#     <tr>
#         <th style="transform: rotate(-90deg);">Spade</th>
#         <td><a title="GW Simulations / Public domain" href="https://commons.wikimedia.org/wiki/File:Cards-A-Spade.svg"><img width="50" alt="Cards-A-Spade" src="https://upload.wikimedia.org/wikipedia/commons/9/9d/Cards-A-Spade.svg"></a></td>
#         <td><a title="GW Simulations / Public domain" href="https://commons.wikimedia.org/wiki/File:Cards-2-Spade.svg"><img width="50" alt="Cards-2-Spade" src="https://upload.wikimedia.org/wikipedia/commons/e/e7/Cards-2-Spade.svg"></a></td>
#         <td><a title="GW Simulations / Public domain" href="https://commons.wikimedia.org/wiki/File:Cards-3-Spade.svg"><img width="50" alt="Cards-3-Spade" src="https://upload.wikimedia.org/wikipedia/commons/d/d0/Cards-3-Spade.svg"></a></td>
#         <td><a title="GW Simulations / Public domain" href="https://commons.wikimedia.org/wiki/File:Cards-4-Spade.svg"><img width="50" alt="Cards-4-Spade" src="https://upload.wikimedia.org/wikipedia/commons/4/4e/Cards-4-Spade.svg"></a></td>
#         <td><a title="GW Simulations / Public domain" href="https://commons.wikimedia.org/wiki/File:Cards-5-Spade.svg"><img width="50" alt="Cards-5-Spade" src="https://upload.wikimedia.org/wikipedia/commons/b/b1/Cards-5-Spade.svg"></a></td>
#         <td><a title="GW Simulations / Public domain" href="https://commons.wikimedia.org/wiki/File:Cards-6-Spade.svg"><img width="50" alt="Cards-6-Spade" src="https://upload.wikimedia.org/wikipedia/commons/6/68/Cards-6-Spade.svg"></a></td>
#         <td><a title="GW Simulations / Public domain" href="https://commons.wikimedia.org/wiki/File:Cards-7-Spade.svg"><img width="50" alt="Cards-7-Spade" src="https://upload.wikimedia.org/wikipedia/commons/c/c6/Cards-7-Spade.svg"></a></td>
#         <td><a title="GW Simulations / Public domain" href="https://commons.wikimedia.org/wiki/File:Cards-8-Spade.svg"><img width="50" alt="Cards-8-Spade" src="https://upload.wikimedia.org/wikipedia/commons/7/7e/Cards-8-Spade.svg"></a></td>
#         <td><a title="GW Simulations / Public domain" href="https://commons.wikimedia.org/wiki/File:Cards-9-Spade.svg"><img width="50" alt="Cards-9-Spade" src="https://upload.wikimedia.org/wikipedia/commons/0/0a/Cards-9-Spade.svg"></a></td>
#         <td><a title="GW Simulations / Public domain" href="https://commons.wikimedia.org/wiki/File:Cards-10-Spade.svg"><img width="50" alt="Cards-10-Spade" src="https://upload.wikimedia.org/wikipedia/commons/6/67/Cards-10-Spade.svg"></a></td>
#         <td><a title="GW Simulations / Public domain" href="https://commons.wikimedia.org/wiki/File:Cards-J-Spade.svg"><img width="50" alt="Cards-J-Spade" src="https://upload.wikimedia.org/wikipedia/commons/e/ea/Cards-J-Spade.svg"></a></td>
#         <td><a title="GW Simulations / Public domain" href="https://commons.wikimedia.org/wiki/File:Cards-Q-Spade.svg"><img width="50" alt="Cards-Q-Spade" src="https://upload.wikimedia.org/wikipedia/commons/e/ef/Cards-Q-Spade.svg"></a></td>
#         <td><a title="GW Simulations / Public domain" href="https://commons.wikimedia.org/wiki/File:Cards-K-Spade.svg"><img width="50" alt="Cards-K-Spade" src="https://upload.wikimedia.org/wikipedia/commons/1/18/Cards-K-Spade.svg"></a></td>
#     </tr>
# </table>

# -   Each card is in one of the four suits: **Diamond**, **Club**, **Heart**, and **Spade**.
# -   Each card has a value $1 \text{ (A)} < 2 < 3 < 4 < 5 < 6 < 7 < 8 < 9 < 10 < 11 \text{ (J)} < 12 \text{ (Q)} < 13 \text{ (K)}$.

# The following code creates a deck of cards. (You do not need to understand the code for now.)

# In[1]:


# Create a deck of cards
from collections import namedtuple

suits = ("Diamond", "Club", "Heart", "Spade")
values = range(1, 14)
Card = namedtuple('Card', ['value', 'suit'])

deck = [Card(value, suit) for value in values for suit in suits]
print(deck)


# To play the game, a dealer randomly pick a card without letting you know, and you're going to guess what exactly that card is.

# In[2]:


# Randomly draw a card from the deck with replacement
import random
print(random.choice(deck))


# You are allowed to make an informed guess after the dealer answers some of your **yes/no** questions.

# For instance, you may ask:
# - Is the suit club?
# - Is the card diamond 1 (ace)?
# - Is the value at least 10?

# However, you cannot ask:
# - What is the value?
# - What is the suite?

# **Exercise** You win if you can **guess the card correctly with no more than 6 questions**. What is the winning strategy?

# YOUR ANSWER HERE

# Hint 1: <span style="color:white">Obviously, you should not ask whether the card is precisely certain card, e.g., Is it Diamond Ace? Is it Diamond 2? ... Why not? The card may be one of the remaining $52-6=46$ possibilities you did not ask.</span>

# Hint 2: <span style="color:white">Think of each **Yes/No** question as splitting the set of possible cards into two smaller groups of possible cards corresponding to each possible answer **Yes/No**.</span>

# Hint 3: <span style="color:white">How many questions is required to split the set of 52 cards into groups of size $1$, i.e., with only one possible card?</span>

# ## Challenge the computer

# Play the role of the dealer and test if the program below can guess the card correctly after 6 questions.

# In[3]:


suitIdx = 0
number = 0

if "y" == input(
        "Is the suite either heart or spade? (y/[n]) ").strip().lower():
    suitIdx += 2

if "y" == input("Is the suite either club or spade? (y/[n]) ").strip().lower():
    suitIdx += 1

if "y" == input(
        f"Is the number {number+8} or above? (y/[n]) ").strip().lower():
    number += 8

if "y" == input(
        f"Is the number {number+4} or above? (y/[n]) ").strip().lower():
    number += 4

if "y" == input(
        f"Is the number {number+2} or above? (y/[n]) ").strip().lower():
    number += 2

if "y" == input(
        f"Is the number {number+1} or above? (y/[n]) ").strip().lower():
    number += 1

print(f"The card is {suits[suitIdx]} {number}")


# **Exercise** Does the above program always win? Explain your answer?

# YOUR ANSWER HERE

# ## Challenge your understanding

# The following table gives the binary representions of unsigned decimal integers from 0 to 7.

# <table>
#     <tr><th>Binary</th><th>Decimal</th></tr>
#     <tr><td>000</td><td>0</td></tr>
#     <tr><td>001</td><td>1</td></tr>
#     <tr><td>010</td><td>2</td></tr>
#     <tr><td>011</td><td>3</td></tr>
#     <tr><td><b style="color:magenta">1</b>00</td><td style="color:magenta">4</td></tr>
#     <tr><td><b style="color:magenta">1</b>01</td><td style="color:magenta">5</td></tr>
#     <tr><td><b style="color:magenta">1</b>10</td><td style="color:magenta">6</td></tr>
#     <tr><td><b style="color:magenta">1</b>11</td><td style="color:magenta">7</td></tr>
# </table><br>

# To convert binary to decimal, think of the conversion as a guessing game where
# - the binary sequence is a sequence of **yes (1)** or **no (0)** answers to certain **yes/no** questions, and
# - the informed guess is the integer represented by the binary sequence.

# For instance, observe that the binary representation of 4, 5, 6, and 7 actually have <b style="color:magenta">1</b> in the leftmost (most significant) bit. Therefore we can consider that bit as the answer to the following **yes/no** question:
# 
# > Is the integer 4 or above?

# **Exercise** What are the **yes/no** questions corresponding to the 2nd bit and 3rd bit?

# YOUR ANSWER HERE

# <h2>References</h2>
# <ul>
#     <li><a href=https://www.mathsisfun.com/binary-number-system.html>Binary Number Sytem</a></li>
#     <li><a href=https://www.purplemath.com/modules/numbbase.htm>Binary Number Conversions</a></li>
# </ul>
