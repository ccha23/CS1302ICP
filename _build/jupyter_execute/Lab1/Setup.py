#!/usr/bin/env python
# coding: utf-8

# # Setup
# CS1302 Introduction to Computer Programming
# ___

# ## JupyterHub

# ### How to access the JupyterHub Server?

# 1. Enter the url of the Jupyterhub server [ltjh.cs.cityu.edu.hk](https://ltjh.cs.cityu.edu.hk) in a web browser.
# 1. Enter your [EID](https://www.cityu.edu.hk/esu/eid.htm) and Password in the fields `Username` and `Password` respectively.
# 1. Click the `Sign In` button.

# <img src="https://www.cs.cityu.edu.hk/~ccha23/cs1302/Login.gif" />

# **Tips**
# - If the browser is stuck at the following page loading the server, `refresh` your browser.  
#   ![server stuck](https://www.cs.cityu.edu.hk/~ccha23/cs1302/server_stuck.png)
# - If you see the following page with ``My Server`` button, click on that button.  
#   ![server start](https://www.cs.cityu.edu.hk/~ccha23/cs1302/server_start.png)
# - If you see the ``Start My Server`` button instead, click on that button to start your server.  
#   ![server stopped](https://www.cs.cityu.edu.hk/~ccha23/cs1302/server_stopped.png)
# - For other issues, try logging out using the `Logout` button at the top right-hand corner, and then logging in again. You may also click the `Control Panel` button and restart your server.

# ### How to access course materials?

# 1. Click on the `Assignments` tab, and ensure `cs1302` is chosen in the drop down list.
# 1. In the `Released assignments panel`, click the button `Fetch` to download `Lab1`. 
# 1. `Lab1` should appear in the `Downloaded assignments panel`. 
# 1. Click on the little arrow next to `Lab1` to show its content.  
# 1. Ctrl-Click on `Lab1` to open the assignment folder on a new browser tab. 
# 1. On the new browser, click the folder `cs1302` to navigate to the notebook `Setup.ipynb`.
# 1. Click on `Setup.ipynb` to open the notebook.

# <img src="https://www.cs.cityu.edu.hk/~ccha23/cs1302/Fetch.gif" />

# **Tips**
# 1. Note that all the downloaded course materials will be placed under the `cs1302` folder of your home directory by default, so you need not go to the `Assignments` tab again to open the downloaded materials. 
# E.g., you can access the `Setup.ipynb` notebook as follows:
#     1. Going to the `File` tab, which is the default JupyterHub homepage after login or when you click the logo on the top left-hand corner.
#     1. Enter the notebook URL [ltjh.cs.cityu.edu.hk/user-redirect/tree/cs1302/Lab1/Setup.ipynb](https://ltjh.cs.cityu.edu.hk/user-redirect/tree/cs1302/Lab1/Setup.ipynb). (See the [documentation](https://jupyterhub.readthedocs.io/en/stable/reference/urls.html) for details.)
# 1. If for any reason you want to Fetch `Lab1` again, you have to first rename your `Lab1` folder to a different name such as `Lab1_orig`. You can do so by selecting the folder and click rename. You can also remove the folder by evaluating `!rm -rf ~/cs1302/Lab1` in a code cell. (Be very cautious as removed folders cannot be recovered.)

# ## Jupyter Notebook

# ### How to complete a lab assignment?

# After opening the `Lab1` notebook `Setup.ipynb`:
# 1. Click `Help->User Interface Tour` to learn the jupyter notebook interface. 
# 1. Click `Help->Notebook Help` and skim through the tutorials on `Running Code` and `Working with Markdown Cells`.

# **Exercise** In learning a new computer language, the first program to write is often the ["Hello, World!"](https://en.wikipedia.org/wiki/%22Hello,_World!%22_program) program, which says Hello to the world. Type the program `print('Hello, World!')` below and run it with `Shift+Enter`.

# In[1]:


### BEGIN SOLUTION
print('Hello, World!')
### END SOLUTION


# We often ask you to write a code in a particular cell. Make sure you fill in any place that says `YOUR CODE HERE` or "YOUR ANSWER HERE".

# In order to check your work thoroughly, there will visible and hidden test cases. The following is a visible test you can run to check your answer: The test returns an assertion error only if your program does not print the correct message.

# In[2]:


# Run this test cell right after running your "Hello, World!" program.
import sys, io
old_stdout, sys.stdout = sys.stdout, io.StringIO()
exec(In[-2])
printed = sys.stdout.getvalue()
sys.stdout = old_stdout
assert printed == 'Hello, World!\n'


# **Tips**
# 1. You can repeatedly modify your solution and run the test cell until your solution passes the test. You are not required to know how the test cell is written. 
# 1. To assess your solution thoroughly, we often run new tests hidden from you after you have submitted your notebook. There is no partial credit for a partially correct solution that works for the visible test but fails for the hidden test. Therefore, *you should ensure your solution works in general rather than just the visible tests*.
# 1. You can click the `Validate` button to run all the visible tests.
# 1. If you open the same notebook multiple times in different browser windows, be careful in making changes in different windows. Inconsistent changes may lead to conflicts or loss of your data.
# 1. If your notebook fails to run any code, the Kernel might have died. You can restart the kernel with `Kernel->Restart`. If restarting fails, check your code cells to see if there is any code that breaks the kernel.

# ### How to submit a notebook

# - Although Lab1 does not count towards your final grade, you are required to submit it, to get familiar with the procedure.
# - Before you submit, make sure everything runs as expected:
#     1. **Restart the kernel**: `Kernel->Restart` 
#     1. **run all cells**: `Cell->Run All`

# To submit your notebook:
# 1. Go to `Assignment` tab of JupyterHub where you fetched the Lab assignment. 
# 1. Expand the Lab1 folder and click the `validate` button next to the notebook(s) to check if all visible tests pass.
# 1. Click `Submit` to submit your notebook. 
# 1. You may submit as many times as you wish before the due date as we collect your latest submission for grading. 
#     - *No late submission* will be collected without valid justifications.
#     - *Double check* that you have submitted the correct Lab assignment.
#     - You are responsible for *recording your submission attempt* with a valid timestamp in case of technical issues.

# **Tips**
# 1. You normally have at least 5 days to work on the lab after your lab session. 
# 1. You can check the due dates of all the labs from the course homepage. 
# 1. You may seek help from us or your classmates. However, you must write your own solution and indicate who your collaborators are using the code:

# In[7]:


COLLABORATORS = ['WONG Xiu Fong', 'LEE Man Kit']


# ## Advanced Usage

# ### How to print or backup a notebook?

# To convert a notebook to pdf, we can print it to pdf instead: 
# - `File->Print Preview`
# 
# However, animation and video cannot be properly printed. You are highly recommended to takes notes on the dynamic notebook instead on the hard copy.

# To download a copy of your notebook:
# - `File->Download as->Notebook (.ipynb)`
# 
# You can run the notebook
# - locally using [Anaconda](https://www.anaconda.com/products/individual), or
# - remotely on other JupyHub services such as [Google Colab](https://colab.research.google.com/).
# 
# However, you would need to learn how to manage and install the additional packages required by the course.

# ### Jupyter Lab and extensions

# Instead of the classic notebook interface, you may also play with the new interface called JupyterLab by visiting [ltjh.cs.cityu.edu.hk/user-redirect/lab/](https://ltjh.cs.cityu.edu.hk/user-redirect/lab/). 
# 
# 
# Note that the new interface does not support the validation and submission of lab assignment. It is currently under [active development on GitHub](https://github.com/jupyterlab/jupyterlab), so be prepared to see [bugs](https://en.wikipedia.org/wiki/Software_bug).

# You may use the [visual debugger](https://github.com/jupyterlab/debugger) in JupyterLab to debug a jupyter notebook. To do you, you should open the notebook and choose XPython as the kernel.

# Both the notebook/lab interface is extensible. For the notebook interface, you can enable extensions from the [nbextensions page](https://ltjh.cs.cityu.edu.hk/user-redirect/nbextensions).

# ### Visual Studio Code

# For a complete IDE experience, you can open VS Code as follows:
# - [ltjh.cs.cityu.edu.hk/user-redirect/vscode/](https://ltjh.cs.cityu.edu.hk/user-redirect/vscode/)
# - In classic notebook interface: `File` tab -> `New` menu -> `VS Code` menu item.
# - In JupyterLab interface: `File` menu -> `New Launcher` menu item -> `VS Code` icon
