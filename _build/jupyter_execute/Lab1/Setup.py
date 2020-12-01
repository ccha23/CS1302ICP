#!/usr/bin/env python
# coding: utf-8

# # Setup
# CS1302 Introduction to Computer Programming
# ___

# ## JupyterHub

# **What is JupyterHub?**

# ### How to access the JupyterHub Server?

# 1. Enter the url [ltjh.cs.cityu.edu.hk](https://ltjh.cs.cityu.edu.hk) in a web browser.
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
# - For other issues, try logging out using the `Logout` button at the top right-hand corner, and then logging in again. You may also click the `Control Panel` button and restarting your server.

# ### How to access course materials?

# 1. Click on the `Assignments` tab, and ensure `cs1302` is chosen in the drop down list.
# 1. In the `Released assignments panel`, click the button `Fetch` to download `Lab1`. 
# 1. `Lab1` should appear in the `Downloaded assignments panel`. 
# 1. Click on the little arrow next to `Lab1` to shows its content.  
# 1. Ctrl-Click on `Lab1` to open the assignment folder on a new browser tab. 
# 1. On the new browser, click the folder `cs1302` to navigate to the notebook `Setup.ipynb`.
# 1. Click on `Setup.ipynb` to open the notebook.

# <img src="https://www.cs.cityu.edu.hk/~ccha23/cs1302/Fetch.gif" />

# **Tips**
# 1. Note that all the downloaded course materials will be placed under the `cs1302` folder of your home directory by default, so you need not go to the `Assignments` tab again to open the downloaded materials. 
# E.g., you can access the `Setup.ipynb` notebook as follows:
#     1. Going to the `File` tab, which is the default JupyterHub homepage after login or when you click the logo on the top left-hand corner.
#     1. Enter the notebook URL https://ltjh.cs.cityu.edu.hk/user-redirect/tree/cs1302/Lab1/Setup.ipynb. (See the [documentation](https://jupyterhub.readthedocs.io/en/stable/reference/urls.html) for details.)
# 1. If for any reason you want to Fetch `Lab1` again, you have to first rename your `Lab1` folder to a different name such as `Lab1_orig`. You can do so by selecting the folder and click rename. You can also remove the folder by evaluating `!rm -rf ~/cs1302/Lab1` in a code cell. (Be very cautious as removed folders cannot be recovered.)
# 1. You may also play with the new interface called JupyterLab https://ltjh.cs.cityu.edu.hk/user-redirect/lab/.
# However, the new interface does not support all the tools we need for lectures/labs. It is currently under [active development on GitHub](https://github.com/jupyterlab/jupyterlab), so be prepared to see [bugs](https://en.wikipedia.org/wiki/Software_bug).

# ## Jupyter Notebook

# ### How to complete a lab assignment?

# After opening the `Lab1` notebook `Setup.ipynb`:
# 1. Click `Help->User Interface Tour` to learn the jupyter notebook interface. 
# 1. Click `Help->Notebook Help` and skim through the tutorials on `Running Code` and `Working with Markdown Cells`.

# Note that the tutorial page is static but you can copy to this notebook to run them. Let's run some code in this notebook.

# **Exercise** Run the following cell to enable and configure the notebook extensions for this course.

# In[1]:


get_ipython().run_cell_magic('javascript', '', 'IPython.notebook.config.update({\n  "load_extensions": {\n    "validate_assignment/main": true,\n    "execute_time/ExecuteTime": true,\n    "init_cell/main": true,\n    "printview/main": true,\n    "skip-traceback/main": true,\n    "hide_input/main": true,\n    "codefolding/main": true,\n    "scratchpad/main": true,\n    "spellchecker/main": true,\n    "create_assignment/main": true,\n    "ruler/main": true,\n    "collapsible_headings/main": true,\n    "latex_envs/latex_envs": true,\n    "exercise/main": true,\n    "select_keymap/main": true,\n    "toc2/main": true,\n    "code_prettify/code_prettify": true\n  },\n  "rise": {\n    "scroll": true\n  },\n  "toc": {\n    "skip_h1_title": true\n  }\n})')


# - Refresh the page for the notebook extensions to take effect.
# - You can learn more about the extensions from the [nbextensions page](/user-redirect/nbextensions).

# Instead of evaluation a code cell, we often ask you to write a code in a particular cell. Make sure you fill in any place that says `YOUR CODE HERE` or "YOUR ANSWER HERE".

# **Exercise** In learning a new computer language, the first program to write is often the ["Hello, World!"](https://en.wikipedia.org/wiki/%22Hello,_World!%22_program) program, which says Hello to the world. Type the program `print('Hello, World!')` below and run it with `Shift+Enter`.

# In[2]:


# YOUR CODE HERE
raise NotImplementedError()


# In order to check your work thoroughly, there will visible and hidden test cases. The following is a visible test you can run to check your answer: The test returns an assertion error only if your program does not print the correct message.

# In[ ]:


# Run this test cell right after running your "Hello, World!" program.
import sys, io
old_stdout, sys.stdout = sys.stdout, io.StringIO()
exec(In[-2])
assert sys.stdout.getvalue() == 'Hello, World!\n'
sys.stdout = old_stdout


# **Tips**
# 1. You can repeatedly modify your solution and run the test cell your solution passes the test. You are not required to know how the test cell is written. 
# 1. To assess your solution thoroughly, we often run new tests hidden from you after you have submitted your notebook. There is no partial credit for a partially correct solution that works for the visible test but fails for the hidden test. Therefore, *you should ensure your solution works in general rather than just the visible tests*.
# 1. You can click the `Validate` button to run all the visible tests.
# 1. If you open the same notebook multiple times in different browser windows, be careful in making changes in different windows. Inconsistent changes may lead to conflicts or loss of your data.
# 1. If your notebook fails to run any code, the Kernel might have died. You can restart the kernel with `Kernel->Restart`. If restarting fails, check your code cells to see if there are unsafe code that breaks the kernel.

# ### How to submit a notebook

# - Although this Lab is not graded, you are required to submit it, to get familiar with the procedure.
# - Before you submit, however, make sure everything runs as expected:
#     1. **Restart the kernel**: `Kernel->Restart` 
#     1. **run all cells**: `Cell->Run All`

# To submit your notebook:
# 1. Go to `Assignment` tab of JupyterHub where you fetched the Lab assignment. 
# 1. Expand the Lab folder and click the `validate` button next to the notebook(s) to check if all visible tests pass.
# 1. Click the `Submit` to submit your notebook. 
# 1. You may submit as many time as your wish but we will only collect your latest submission before the [Lab 1 due date](https://canvas.cityu.edu.hk/courses/36768/assignments/128315?return_to=https%3A%2F%2Fcanvas.cityu.edu.hk%2Fcalendar%3Finclude_contexts%3Dcourse_36768%23view_name%3Dmonth%26view_start%3D2020-09-01) for grading.

# **Tips**
# 1. You normally have at least 5 days to work on the lab after your lab session. 
# 1. You can check the due dates of all the labs from the [course homepage](https://canvas.cityu.edu.hk/courses/36768) or [course calendar](https://canvas.cityu.edu.hk/calendar?include_contexts=course_36768). 
# 1. You may seek help from us or your classmates. However, you must write your own solution and indicate who your collaborators are using the code `COLLABORATORS = 'WONG Xiu Fong, LEE Man Kit'`.

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
# However, you would need to learn how to manage and install any additional packages required.
