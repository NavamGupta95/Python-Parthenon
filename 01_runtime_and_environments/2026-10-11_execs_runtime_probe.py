"""
2026-10-11_execs_runtime_probe.py
=================================
Lesson 01 Hands-on: Meeting Your Python Interpreter

Theory Guide:
  ./2026-10-11_docs_execution_mechanics_and_environments.md

HOW TO RUN THIS FILE:
  Open your PowerShell terminal and type:
  python 01_runtime_and_environments/2026-10-11_execs_runtime_probe.py
"""

# ==============================================================================
# STEP 1: The Foundation — Printing to the Screen
# ==============================================================================
# In Python, `print(...)` is how you display text on your computer screen.
print("==================================================")
print("Welcome to the Python Parthenon!")
print("==================================================")


# ==============================================================================
# STEP 2: Borrowing a Built-in Tool (`import sys`)
# ==============================================================================
# Python comes with many built-in toolboxes. One of them is called `sys`.
# `sys` stands for "system". It lets your code ask questions about your computer
# and the Python program itself.
import sys

# Let's ask Python what version it is:
print("\n[Question 1] Hey Python, what version are you?")
print(f"-> Python says: I am version {sys.version.split()[0]}")

# Let's ask Python where it is installed on your hard drive:
print("\n[Question 2] Hey Python, where do you live on my computer?")
print(f"-> Python says: My executable file is at:\n   {sys.executable}")


# ==============================================================================
# STEP 3: Checking if We Are in a Virtual Environment
# ==============================================================================
# In our theory doc, we learned that a "virtual environment" is just a private
# folder (.venv) for our project.
#
# Python knows if it's in a private folder by checking two values:
# - sys.prefix: Where Python is currently running from.
# - sys.base_prefix: Where the main Python on your computer is installed.
#
# If they are EQUAL, you are using the main computer Python (not a private .venv yet).
# If they are DIFFERENT, you are inside a private .venv!
print("\n[Question 3] Are we running inside a private virtual environment (.venv)?")
if sys.prefix == sys.base_prefix:
    print("-> Answer: NO. You are currently using your main Scoop Python.")
    print("   (That is completely fine! We will learn how to make a .venv next.)")
else:
    print("-> Answer: YES! You are running safely inside an isolated .venv.")


# ==============================================================================
# STEP 4: YOUR TURN TO EXPERIMENT! (A Mini-Exercise)
# ==============================================================================
# Below is a simple function called `greet_builder`.
# A function is like a recipe: you give it some input, and it gives you a result.
def greet_builder(architect_name: str) -> str:
    """Take a name and return a warm welcome message."""
    # TASK: You can customize this message if you want!
    return f"Welcome, Architect {architect_name}, to the Python Parthenon!"


# Let's test the function:
my_greeting = greet_builder("Navam")
print(f"\n[Your Custom Greeting]:\n{my_greeting}")
print("==================================================")
print("[+] Script finished successfully!")
print("==================================================")
