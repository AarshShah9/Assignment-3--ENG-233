# school_data.py
# STUDENT NAME, ENDG 233 F21
# A terminal-based application to process and plot data based on given user input and provided csv files.
# You may only import numpy, matplotlib, and math. 
# No other modules may be imported. Only built-in functions that support compound data structures, user entry, or casting may be used.
# Remember to include docstrings for any functions/classes, and comments throughout your code.

import numpy as np
import matplotlib.pyplot as plt

# The following class is provided and should not be modified.
class School:
    """A class used to create a School object.

        Attributes:
            name (str): String that represents the school's name
            code (int): Integer that represents the school's code
    """

    def __init__(self, name, code):
        self.name = name 
        self.code = code

    def print_all_stats(self):
        """A function that prints the name and code of the school instance.

        Parameters: None
        Return: None

        """
        print("School Name: {0}, School Code: {1}".format(self.name, self.code))


# Import data here
# Hint: Create a dictionary for all school names and codes
# Hint: Create a list of school codes to help with index look-up in arrays


# Add your code within the main function. A docstring is not required for this function.
def main():
    print("ENDG 233 School Enrollment Statistics\n")

    # Print array data here

    # Add request for user input here

    
    print("\n***Requested School Statistics***\n")

    # Print school name and code using the given class
    # Add data processing and plotting here


# Do not modify the code below
if __name__ == '__main__':
    main()

