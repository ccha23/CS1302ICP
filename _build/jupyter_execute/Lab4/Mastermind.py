#!/usr/bin/env python
# coding: utf-8

# # Mastermind

# **CS1302 Introduction to Computer Programming**
# ___

# In this notebook, you will write a game called [*Mastermind*](https://en.wikipedia.org/wiki/Mastermind_(board_game)).  
# Play the video below to learn about the rule of the game.

# In[ ]:


get_ipython().run_cell_magic('html', '', '<iframe width="912" height="513" src="https://www.youtube.com/embed/wsYPsrzCKiA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')


# 1. **Mastermind** first creates a hidden `code` of length `code_length` consisting code pegs with possibly duplicate colors chosen from a sequence of `colors`.
# 1. **Coderbreaker** provides a `guess` of the `code`.
# 1. **Mastermind** generates a `feedback` consisting of key pegs of black and white colors:
#     - The number of black pegs (`black_key_pegs_count`) is the number of code pegs that are the correct colors in the correct positions. 
#     - The number of white pegs (`white_key_pegs_count`) is the number of code pegs that are the correct colors but in incorrect positions.
#     - Each code peg should be counted only once, i.e., a code peg cannot be awarded more than one key peg. E.g.,
#         - If the `code` is `'RBGG'` and `guess` is `'BGGG'`, then 
#         - the feedback should be `'bbw'` with 
#             - `black_key_pegs_count == 2` because of `__GG` in the guess, and
#             - `white_key_pegs_count == 1` because of `_B__` in the guess. 
#             - `_G__` in the `guess` should not be awarded an additional white peg because `__GG` in the `code` has been counted.
# 1. **Codebreaker** wins if the code is correctly guessed within certain number (`max_num_guesses`) of guesses.

# ## Random Code Generation

# The first exercise is to generate a random hidden code so even one person can play the game as Codebreaker.  
# Watch the following video to understand how computers generate random objects.

# In[ ]:


get_ipython().run_cell_magic('html', '', '<iframe width="912" height="513" src="https://www.youtube.com/embed/GtOt7EBNEwQ" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')


# To generate random content in Python, we can import the **random** module, which provides some useful functions to generate random objects as follows.

# In[ ]:


import random
for i in range(10): print(random.random())  # random floating point numbers in [0,1)


# In[ ]:


for i in range(10): print(random.randint(3,10),end=' ')  # random integer in range [3,10]


# In[ ]:


for i in range(10): print(random.choice('RBG'),end='')  # random element in the sequence 'RBG'


# We can generate a reproducible pseudo-random sequence by specifying the seed.  
# By default Python uses the system time as seed.

# In[ ]:


# repeatedly run the cell to see new sequences.
random.seed(123456)
for i in range(10): print(random.randint(3,10),end=' ')


# **Exercise** Define a function that generates a random `code`. The functions takes in
# - a string `colors` whose characters represent distinct colors to choose from, and
# - a positive integer `code_length` representing the length of the code.
# 
# For instance, `get_code('ROYGBP',4)` returns a code of `4` code pegs randomly with colors chosen from `'R'`ed, `'O'`range, `'Y'`ellow, `'G'`reen, `'B'`lue, and `'P'`urple. One possible outcome is `'ROYY'`.

# In[ ]:


import random
def get_code(colors, code_length):
    code = ''
    """
    The function body will iterate code_length times.
    In each iteration, generate a random (integer) position in range 0 to len(colors)-1. 
    From color, get the character at that random position and append the character to code
    """
    # YOUR CODE HERE
    raise NotImplementedError()
    return code


# In[ ]:





# ## Guess Validation

# **Exercise** Define a function `valid_code` that 
# - takes `colors`, `code_length`, and `guess` as the first, second, and third arguments respectively, and
# - return `True` if `guess` is a valid code, i.e., a string of length `code_length` with characters from those of `colors`, and
# - `False` otherwise.

# *Hint:* Solution template:
# ```Python
# def __________(colors, code_length, guess):
#     if len(guess) __ code_length:
#         is_valid = ____
#     else:
#         for peg in guess:
#             for color in colors:
#                 if peg == color: ____
#             else:
#                 is_valid = _____
#                 ____
#         else:
#             is_valid = ____
#     return is_valid
# ```

# In[ ]:


# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


# tests
assert valid_code('RBG',1,'R') == True
assert valid_code('RBG',2,'B') == False
assert valid_code('RBG',2,'RP') == False
assert valid_code('RBG',0,'') == True


# ## Feedback Generation

# According to the rules of Mastermind, double-counting of a single peg (as black and white) is not allowed. To facilitate this check, we have written a new module `markposition` that allows you to mark any non-negative integer position as counted.

# **Exercise** Write an `import` statement to import from the module `markposition` the functions 
# - `mark_as_counted`
# - `check_if_counted`, and 
# - `reset_all_to_not_counted`.

# In[ ]:


# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


# Tests
reset_all_to_not_counted()
mark_as_counted(3)
assert check_if_counted(3) and not check_if_counted(0)


# **Exercise** Using the functions imported from `markposition`, mark only the positions `0`, `2`, `4`, `6`, `8`, and `10` as counted. All other positions are not counted.   
# *Hint*: Use `help` to learn how to use the imported functions.

# In[ ]:


# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


# Tests
for i in range(11):
    assert not check_if_counted(i) if i % 2 else check_if_counted(i)


# **Exercise** Define a function `get_feedback` that 
# - takes `code` and `guess` as the first and second arguments respectively, and
# - returns a feedback string that starts with the appropriate number of characters `'b'` (for black key pegs) followed by the appropriate number of characters `'w'` (for white key pegs).

# *Hint:* Solution template:
# ```Python
# def get_feedback(code, guess):
#     black_key_pegs_count = white_key_pegs_count = counted = 0
#     reset_all_to_not_counted()
#     for i in _________________:
#         if ___________________:
#             black_key_pegs_count += 1
#             mark_as_counted(i)
#     for i in range(len(guess)):
#         for j in range(len(code)):
#             if  __________________________________________________________:
#                 white_key_pegs_count += 1
#                 mark_as_counted(j)
#                 break
#     key = 'b' * black_key_pegs_count + 'w' * white_key_pegs_count
#     return key
# ```

# In[ ]:


# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:


# tests
def test_get_feedback(feedback,code,guess):
    feedback_ = get_feedback(code,guess)
    correct = feedback == feedback_
    if not correct:
        print(
            f'With code="{code}" and guess="{guess}", feedback should be "{feedback}", not "{feedback_}".'
        )
    assert correct

test_get_feedback(10*'b'+'w'*0,"RGBRGBRGBY","RGBRGBRGBY")
test_get_feedback(0*'b'+'w'*10,"RGBRGBRGBY","YRGBRGBRGB")
test_get_feedback(8*'b'+'w'*0,"RGRGRGRG","RGRGRGRG")
test_get_feedback(0*'b'+'w'*8,"RGRGRGRG","GRGRGRGR")
test_get_feedback(0*'b'+'w'*6,"RRRRGGG","GGGGRRR")
test_get_feedback(1*'b'+'w'*6,"RRRRGGG","GGGRRRR")
test_get_feedback(5*'b'+'w'*2,"RRRRGGG","RRRGGGR")
test_get_feedback(1*'b'+'w'*0,"RRRRGGG","RYYPPBB")
test_get_feedback(0*'b'+'w'*1,"RRRRG","GBBBB")
test_get_feedback(0*'b'+'w'*0,"RRRRG","YBBBB")


# ## Play the Game

# After finishing the previous exercises, you can play the game as a code breaker against a random mastermind.

# In[ ]:


# mastermind
import ipywidgets as widgets
from IPython.display import display, HTML


def main():
    '''The main function that runs the mastermind game.'''
    max_num_guesses = code_length = code = num_guesses_left = None
    is_game_ended = True
    colors = 'ROYGBP'
    color_code = {
        "R": "#F88,#F00,#800",
        "O": "#FD8,#F80,#840",
        "Y": "#FF8,#FF0,#AA0",
        "G": "#8F8,#0F0,#080",
        "B": "#88F,#00F,#008",
        "P": "#F8F,#F0F,#808",
        "b": "#888,#000,#000",
        "w": "#FFF,#EEE,#888"
    }

    # returns the HTML code for a colored peg.
    def getPeg(color, size=30):
        return '''<div style='display:inline-block;
                              background-image: radial-gradient(circle, {0}); 
                              width:{1}px; height:{1}px; border-radius:50%;'>
                  </div>'''.format(color_code[color], size)

    colors_display = widgets.HBox([widgets.Label(value='Color codes:')] + [
        widgets.HBox([widgets.Label(value=color),
                      widgets.HTML(getPeg(color))]) for color in colors
    ])

    max_num_guesses_input = widgets.IntSlider(min=5,
                                              max=15,
                                              value=10,
                                              description="# guesses:")
    code_length_input = widgets.IntSlider(min=2,
                                          max=10,
                                          value=4,
                                          description="Code length:")
    code_input = widgets.Password(description="Code:")
    start_new_game_button = widgets.Button(description="Start a new game")

    guess_input = widgets.Text(description="Guess:")
    submit_guess_button = widgets.Button(description="Submit guess")
    board = widgets.Output()
    message = widgets.Output()

    display(
        widgets.VBox([
            max_num_guesses_input, code_length_input, colors_display,
            widgets.HBox([code_input, start_new_game_button]),
            widgets.HBox([guess_input, submit_guess_button]), board, message
        ]))

    # A listener that starts a new game
    def start_new_game(button):
        nonlocal code, num_guesses_left, is_game_ended, max_num_guesses, code_length
        max_num_guesses = max_num_guesses_input.value
        code_length = code_length_input.value
        board.clear_output()
        message.clear_output()
        code = code_input.value or get_code(colors, code_length)
        with message:
            if not valid_code(colors, code_length, code):
                display(
                    HTML('''<p>The code {} is invalid.<br>
                        Leave the code box empty to randomly generated a code.
                        </p>'''.format(code)))
                is_game_ended = True
            else:
                num_guesses_left = max_num_guesses
                is_game_ended = num_guesses_left <= 0
                display(
                    HTML('<p>Game started! {} Guesses left.</p>'.format(
                        num_guesses_left)))

    # A listener that submits a guess
    def submit_guess(button):
        nonlocal num_guesses_left, is_game_ended
        guess = guess_input.value
        with message:
            message.clear_output()
            if is_game_ended:
                display(
                    HTML('''<p>Game has not started.<br> 
                        Please start a new game.</p>'''))
                return
            if not valid_code(colors, code_length, guess):
                display(HTML('<p>Invalid guess.</p>'))
                return
        feedback = get_feedback(code, guess)
        num_guesses_left -= 1
        with board:
            content = ""
            for k in guess:
                content += getPeg(k)
            content += '''<div style='display:inline-block; 
                             margin: 0px 5px 0px 30px; 
                             position:relative; top:5px;'>Feeback:</div>
                          <div style='display:inline-block; 
                             border: 1px solid; width:120px; height:30px;'>'''
            for k in feedback:
                content += getPeg(k, 28)
            content += "</div>"
            display(HTML(content))

        with message:
            message.clear_output()
            if feedback == 'b' * code_length:
                is_game_ended = True
                display(
                    HTML('<p>You won with {} guesses left!</p>'.format(
                        num_guesses_left)))
                return
            is_game_ended = num_guesses_left <= 0
            if is_game_ended:
                display(HTML('<p>Game over...</p>'))
                return
            display(HTML('<p>{} Guesses left.</p>'.format(num_guesses_left)))

    start_new_game_button.on_click(start_new_game)
    submit_guess_button.on_click(submit_guess)


main()


# In[ ]:




