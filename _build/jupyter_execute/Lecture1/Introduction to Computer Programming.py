#!/usr/bin/env python
# coding: utf-8

# # Introduction to Computer Programming

# **CS1302 Introduction to Computer Programming**
# ___

# ## Computer

# ### What is a computer?

# Is computer a calculator that is bigger and more advanced?

# <center><figure>
# <a title="Ccha23 / CC BY-SA (https://creativecommons.org/licenses/by-sa/4.0)" href="https://commons.wikimedia.org/wiki/File:Calculator_app.png"><img width="400" alt="Calculator app" src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Calculator_app.png/512px-Calculator_app.png"></a>
#   <figcaption>A calculator on a computer.</figcaption>
# </figure>
# </center>

# If computer is a calculator, then, is [abacus](https://en.wikipedia.org/wiki/Abacus) the first computer invented?  

# <center><figure>
# <a title="Encyclopædia Britannica / Public domain" href="https://commons.wikimedia.org/wiki/File:Abacus_6.png"><img width="400" alt="Abacus 6" src="https://upload.wikimedia.org/wikipedia/commons/a/af/Abacus_6.png"></a>
#   <figcaption>Abacus - an ancient mechanical computing device.</figcaption>
# </figure>
# </center>

# Is your [smartphone](https://en.wikipedia.org/wiki/Samsung_DeX) a computer?  
# What defines a computer?

# - In addition to performing arithmetic calculations, a computer is designed in such a way that  
# - we can write different programs (in a process called **programming** or **software development**)
# - for the computer to execute to perform different tasks.

# ### What is the architecture of a computer?

# A computer contains three main hardware components:
# - Input device
# - Processing unit
# - Output device

# #### Peripherals

# <center><figure>
# <a title="Unsplash" href="https://unsplash.com/photos/gyRa86ExKTw"><img width="600" alt="Computer peripherals" src="https://images.unsplash.com/flagged/photo-1551954810-43cd6aef5b1f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=3580&q=80"></a>
#   <figcaption>Computer Peripherals.</figcaption>
# </figure>
# </center>

# Input and output devices connected to a computer are called *peripherals*.  
# They allow users to interact with the computer in different ways.

# **Exercise** Some examples of output devices are:
# - Monitor
# - Speaker
# 
# Can you give an awesome example in the following box?

# - 3D printer available at [CityU](https://www.cityu.edu.hk/lib/create/3dprint.htm)

# **Exercise** Some examples of input devices are:
# - Keyboard
# - Mouse
# 
# Can you give an awesome example?

# - 3D scanner available at [CityU](https://www.cityu.edu.hk/lib/create/3dscan.htm)

# **Exercise** Many devices are both input and output device. Can you give at least 3 examples?

# - hard disk
# - CD/DVD Rom (writable)
# - touch screen

# #### Central Processing Unit

# <center><figure>
# <a title="Unsplash" href="https://unsplash.com/photos/CKpBhTXvLis"><img width="600" alt="CPU" src="https://images.unsplash.com/photo-1555617981-dac3880eac6e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1950&q=80"></a>
#   <figcaption>An Intel CPU.</figcaption>
# </figure>
# </center>

# The brain of a computer is its processor unit, or the [**C**entral **P**rocesisng **U**nit (CPU)](https://en.wikipedia.org/wiki/Central_processing_unit).  
# It is located on the [*motherboard*](https://en.wikipedia.org/wiki/Motherboard) and connects to different peripherals using different [*connectors*](https://en.wikipedia.org/wiki/Category:Computer_connectors).

# Two important components in the CPU are:
# -  **A**rithmetic and **L**ogic **U**nit (**ALU**): Performs arithmetics like a calculator (but for binary numbers)
# -  **C**ontrol **U**nit (**CU**): Directs the operations of the processor in executing a program.

# Let's run a CPU Simulator below from a [GitHub project](https://github.com/pddring/cpu-simulator).
# - Note that all values are zeros in the RAM (**R**andom **A**cess **M**emory) initially.
# - Under Settings, click `Examples->Add two numbers`. Observe that the values in the RAM have changed.
# - Click `Run` at the bottom right-hand corner.

# In[1]:


get_ipython().run_cell_magic('html', '', '<iframe src="https://tools.withcode.uk/cpu" width="800" height="800">\n</iframe>')


# ## Programming

# ### What is programming?

# Programming is the process of writing programs.  
# But what is a program?

# **Exercise** You have just seen a program written in [machine language](https://en.wikipedia.org/wiki/Machine_code). Where is it?

# The first six lines of binary sequences in the RAM. The last line `Ends` the program.

# - The CPU is capable of carrying out 
#     - a set of instructions such as *addition*, *negation*, *Copy*, etc.
#     - some numbers stored in the RAM.
# - Both the instructions and the numbers are represented as binary sequences.
# - E.g., in Intel-based CPU, the command for addition is like **00000011 00000100**

# ### Why computer uses binary representation?

# In[2]:


get_ipython().run_cell_magic('html', '', '<iframe width="912" height="513" src="https://www.youtube.com/embed/Xpk67YzOn5w" allowfullscreen></iframe>')


# **Exercise** The first electronic computer, called [Electronic Numerical Integrator and Computer (ENIAC)](https://en.wikipedia.org/wiki/ENIAC), was programmed using binary circuitries, namely *switches* that can be either `On` or `Off`. 
# 
# <center>
#     <figure>
# <a title="United States Army / Public domain" href="https://commons.wikimedia.org/wiki/File:Two_women_operating_ENIAC.gif"><img width="512" alt="Two women operating ENIAC" src="https://upload.wikimedia.org/wikipedia/commons/8/8c/Two_women_operating_ENIAC_%28full_resolution%29.jpg"></a>
#         <figcaption>Programmers controlling the switches of ENIAC.</figcaption>
#     </figure>
# </center>
# 
# However, it did not represent values efficiently in binary. 10 binary digits (bits) was used to represent a decimal number 0 to 9.  
# Indeed, how many decimals can be represented by 10 bits?

# In[3]:


2 ** 10 # because there are that many binary sequences of length 10.


# As mentioned in the video, there are *International Standards* for representing characters:
# - [ASCII](https://en.wikipedia.org/wiki/ASCII) (American Standard Code for Information Interchange) maps English letters and some other symbols to 8-bits (8 binary digits, also called a byte). E.g., `A` is `01000001`.
# - [Unicode](https://en.wikipedia.org/wiki/Unicode) can also represent characters in different languages such as Chinese, Japanese...etc. 

# There are additional standards to represent numbers other than non-negative integers:
# - [2's complement format](https://en.wikipedia.org/wiki/Two%27s_complement) for negative integers (e.g. -123)
# - [IEEE floating point format](https://en.wikipedia.org/wiki/IEEE_754) for floating point numbers such as $1.23 x 10^{-4}$.

# **Why define different standards?**

# - Different standards have different benefits. ASCII requires less storage for a character, but it represents less characters.
# - Although digits are also represented in ASCII, the 2's complement format is designed for arithmetic operations.

# ## Different generations of programming languages

# Machine language is known as the **1st Generation Programming Language**.  

# **Are we going to start with machine language?**
# Start with learning 2's complement and the binary codes for different instructions?

# No. Programmers do not write machine codes directly because it is too hard to think in binary representations. 

# Instead, programmers write human-readable **mnemonics** such as **ADD**, **SUB**...,  
# called **Assembly language**, or the **2nd Generation Programming Language**.

# <center>
#     <figure>
# <a title="Swtpc6800 en:User:Swtpc6800 Michael Holley / Public domain" href="https://commons.wikimedia.org/wiki/File:Motorola_6800_Assembly_Language.png"><img width="600" alt="Motorola 6800 Assembly Language" src="https://upload.wikimedia.org/wikipedia/commons/f/f3/Motorola_6800_Assembly_Language.png"></a>
#         <figcaption>
#             A Code written in an assembly language.
#         </figcaption>
#     </figure>
#  </center>

# **Are you going to learn an assembly language?**

# Both machine language and assembly language are low-level language which
# - are difficult to write for complicated tasks (requiring many lines of code), and
# - are platform specific:
#     - the sets of instructions and their binary codes can be different for different [types of CPUs](https://en.wikipedia.org/wiki/Comparison_of_CPU_microarchitectures), and
#     - different operating systems use [different assembly languages/styles](https://en.wikipedia.org/wiki/X86_assembly_language).

# Anyone want to learn assembly languages, and write a program in many versions to support different platforms?

# Probably for programmers who need to write fast or energy-efficient code such as
# - a driver that controls a 3D graphics card, and
# - a program that control a microprocessor with limited power supply.

# But even in the above cases, there are often better alternatives. Play with the following microprocessor simulator:
# - Click `CHOOSE A DEMO->LED`.
# - Click `RUN SCRIPT` and observes the LED of the board.
# - Run the demos `ASSEMBLY` and `MATH` respectively and compare their capabilities.
# 

# In[4]:


get_ipython().run_cell_magic('html', '', '<iframe width="900", height="1000" src="https://micropython.org/unicorn/"></iframe>')


# ## High-level Language

# In[5]:


get_ipython().run_cell_magic('html', '', '<iframe width="912" height="513" src="https://www.youtube.com/embed/QdVFvsCWXrA" allowfullscreen></iframe>')


# Programmer nowadays use human-readable language known as the **3rd generation language (3GL)** or **high-level language.**
# - Examples includes: C, C++, Java, JavaScript, Basic, Python, PHP, ...

# ### What is a high-level language?

# - A code written in high-level language gets converted automatically to a low-level machine code for the desired platform. 
# - Hence, it *abstracts* away details that can be handled by the computer (low-level code) itself.

# For instance, a programmer needs not care where a value should be physically stored if the computer can find a free location automatically to store the value.

# Different high-level languages can have different implementations of the conversion processes:
# - **Compilation** means converting a program well before executing of the program. E.g., C++ and Java programs are compiled.
# - **Interpretation** means converting a program on-the-fly during the execution of a program. E.g., JavaScript and Python programs are often interpreted.
# 
# Roughly speaking, compiled programs run faster but interpreted programs are more flexible and can be modified at run time.  
# (The [truth](https://finematics.com/compiled-vs-interpreted-programming-languages/) is indeed more complicated than required for this course.)

# ### What programming language will you learn?

# You will learn to program using **Python**. The course covers:
# -  Basic topics including *values*, *variables*, *conditional*, *iterations*, *functions*, *composite data types*.
# -  Advanced topics that touch on functional and object-oriented programming.
# -  Engineering topics such as *numerical methods*, *optimizations*, and *machine learning*.
# 
# See the [course homepage](https://canvas.cityu.edu.hk/courses/36768) for details.

# **Why Python?**

# In[6]:


get_ipython().run_cell_magic('html', '', '<iframe width="912" height="513" src="https://www.youtube.com/embed/Y8Tko2YC5hA?end=200" allowfullscreen></iframe>')


# In summary:
# -   Python is expressive and can get things done with fewer lines of code as compared to other languages.
# -   Python is one of the most commonly used languages. It has an extensive set of libraries for Mathematics, graphics, AI, Machine Learning, etc.
# -   Python is Free and Open Source, so you get to see everything and use it without restrictions.
# -   Python is portable. The same code runs in different platforms without modifications.

# **How does a Python program look like?**

# In[7]:


get_ipython().run_line_magic('reload_ext', 'mytutor')


# In[8]:


get_ipython().run_cell_magic('mytutor', '-h 400', '# The program here reads the cohort and reports which year the user is in\n# Assumption: Input is integer no greater than 2020\nimport datetime  # load a library to tell the current year\ncohort = input("In which year did you join CityU? ")\nyear = datetime.datetime.now().year - int(cohort) + 1\nprint("So you are a year", year, "student.")')


# A Python program contains *statements* just like sentences in natural languages.  
# E.g., `cohort = input("In which year did you join CityU? ")` is a statement that gives some value a name called `cohort`.

# For the purpose of computations, a statement often contains *expressions* that evaluate to certain values.  
# E.g., `input("In which year did you join CityU? ")` is an expression with the value equal to what you input to the prompt.  
# That value is then given the name `cohort`.

# Expressions can be composed of:
# - *Functions* such as `input`, `now`, and `int`, etc., which are like math functions the return some values based on its arguments, if any.
# - *Literals* such as the string `"In which year did you join CityU? "` and the integer `1`. They are values you type out literally.
# - *Variables* such as `cohort` and `year`, which are meaningful names to values.

# To help others understand the code, there are also *comments* that start with `#`.  
# These are descriptions meant for human to read but not to be executed by the computer.

# **Exercise** What do you think the next generation programmimng should be?

# Perhaps programming using natural languages. Write programs that people enjoy reading, like [literate programming](https://www.youtube.com/watch?v=bTkXg2LZIMQ).  
# Indeed, Jupyter notebook is arguably a step towards this direction. See [nbdev](https://github.com/fastai/nbdev).

# In[9]:


get_ipython().run_cell_magic('html', '', '<iframe width="912" height="513" src="https://www.youtube.com/embed/bTkXg2LZIMQ" allowfullscreen></iframe>')


# 
# ```{toctree}
# :hidden:
# :titlesonly:
# 
# 
# ../Lecture2/Values and Variables
# ../Lecture2/Expressions and Arithmetic
# ../Lecture3/Conditional Execution
# ../Lecture3/Iteration
# ../Lecture4/Using Functions
# ../Lecture4/Writing Functions
# ../Lecture5/Objects
# ../Lecture6/More on Functions
# ../Lecture7/Lists and Tuples
# ../Lecture8/Dictionaries and Sets
# ../Lecture9/Monte Carlo Simulation and Linear Algebra
# ../Review/Mock Exam Questions
# ```
# 
