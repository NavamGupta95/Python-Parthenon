r"""
2026-10-11_execs_runtime_probe.py
=================================
Lesson 01 Hands-On: Meeting Your Python Interpreter

Theory Guide:
  ./2026-10-11_docs_execution_mechanics_and_environments.md

HOW TO RUN THIS CODE:
  1. Open PowerShell on your computer.
  2. Make sure you are in the Python Parthenon folder:
     cd "E:/Academy/Python Parthenon"
  3. Type the following command and press Enter:
     python 01_runtime_and_environments/2026-10-11_execs_runtime_probe.py
"""

# ==============================================================================
# SECTION 1: What are Comments and What is `print()`?
# ==============================================================================
# Any line starting with a hash symbol (#) is a COMMENT.
# Comments are notes written for humans. The Python interpreter completely ignores them!
#
# `print(...)` is Python's built-in command to display words onto your screen.
# The quotation marks " " tell Python: "This is raw text, don't try to calculate it as math!"

print("=" * 60)
print("WELCOME TO THE PYTHON PARTHENON!")
print("=" * 60)


# ==============================================================================
# SECTION 2: What is `import` and What is `sys`?
# ==============================================================================
# When you install Python, it brings along built-in toolboxes called "modules".
# One of the most famous toolboxes is called `sys` (short for "system").
# The word `import` tells Python: "Go grab the `sys` toolbox from your backpack so we can use it!"

import sys

# Now that we imported `sys`, we can ask Python questions about itself:

# Question 1: What version of Python are you?
# `sys.version` gives us the exact version number of the interpreter program.
python_version = sys.version.split()[0]
print("\n[Question 1] Hey Python, what version are you?")
print(f"-> Python says: I am Python version {python_version}!")


# Question 2: Where do you live on my computer?
# `sys.executable` tells us the exact folder where `python.exe` is stored.
python_location = sys.executable
print("\n[Question 2] Hey Python, where is your executable program located?")
print(f"-> Python says: My python.exe file lives at:\n   {python_location}")


# ==============================================================================
# SECTION 3: Are We Running in a Virtual Environment?
# ==============================================================================
# In our theory reading, we learned about Virtual Environments (.venv).
# How does Python know if it is running inside a private project folder?
#
# It looks at two addresses:
# 1. `sys.prefix`      : The folder where Python is currently working from.
# 2. `sys.base_prefix` : The folder where the main computer Python is installed.
#
# If both addresses are IDENTICAL:
# -> You are running on the main computer's Python (no private .venv active yet).
# If the addresses are DIFFERENT:
# -> You are running safely inside a private project .venv!

print("\n[Question 3] Are we running inside a private virtual environment (.venv)?")
if sys.prefix == sys.base_prefix:
    print("-> Python says: NO.")
    print("   We are currently using your computer's main Scoop Python.")
    print("   (Don't worry! This is completely normal right now. We will create a .venv soon!)")
else:
    print("-> Python says: YES!")
    print("   We are running safely inside a private project virtual environment.")


# ==============================================================================
# SECTION 4: YOUR FIRST HANDS-ON EXERCISE!
# ==============================================================================
# Now it's your turn to edit some code!
# Below is a Python "function". A function is simply a mini-recipe with a name.
# You give it some input, and it gives you back a result.

def create_welcome_badge(architect_name: str) -> str:
    """Take a name and return a custom welcome badge."""
    # You can change the words inside the quotes below if you'd like!
    return f"Official Badge: Architect {architect_name} has entered the Parthenon!"


# ------------------------------------------------------------------------------
# YOUR TASK:
# Change the name "Navam" below to whatever name or title you prefer!
# ------------------------------------------------------------------------------
your_name = "Navam"
badge = create_welcome_badge(your_name)

print("\n" + "=" * 60)
print(badge)
print("=" * 60)
print("\n[+] Congratulations! You have successfully run your first Parthenon script.")
print("============================================================")
