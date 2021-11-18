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

schools = {1224: 'Centennial High School', 
    1679: 'Robert Thirsk School',
    9626: 'Louise Dean School',
    9806: 'Queen Elizabeth High School',
    9813: 'Forest Lawn High School', 
    9815: 'Crescent Heights High School',
    9816: 'Western Canada High School',
    9823: 'Central Memorial High School',
    9825: 'James Fowler High School',
    9826: 'Ernest Manning High School',
    9829: 'William Aberhart High School',
    9830: 'National Sport School',
    9836: 'Henry Wise Wood High School',
    9847: 'Bowness High School',
    9850: 'Lord Beaverbrook High School',
    9856: 'Jack James High School',
    9857: 'Sir Winston Churchill High School',
    9858: 'Dr. E. P. Scarlett High School',
    9860: 'John G Diefenbaker High School',
    9865: 'Lester B. Pearson High School'
    }

schoolslist = list(schools.keys())


# Add your code within the main function. A docstring is not required for this function.
def main():
    print("ENDG 233 School Enrollment Statistics\n")

    # Print array data here

    # Add request for user input here
    requested_school = str(input('Please enter the high school name or school code: '))

    
    print("\n***Requested School Statistics***\n")

    # Print school name and code using the given class
    # Add data processing and plotting here


# Do not modify the code below
if __name__ == '__main__':
    main()



# for i in school_data2019:
    #if school_data2019[:0] = requested_school:
        # a = 
