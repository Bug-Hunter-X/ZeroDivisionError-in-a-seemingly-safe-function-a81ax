# ZeroDivisionError in a seemingly safe function

This repository demonstrates a common, yet subtle, coding error in Python that leads to a `ZeroDivisionError`.  The error is masked by the initial checks for zero in individual arguments but fails to consider the scenario where both arguments are simultaneously zero.

The `bug.py` file contains the erroneous code, and `bugSolution.py` presents a corrected version with detailed explanation in the comments.  This example highlights the importance of comprehensive error handling in function design.