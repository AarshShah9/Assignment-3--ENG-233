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
        print("School Name: {0}, School Code: {1}".format(
            self.name, self.code))


# Import data here
# Hint: Create a dictionary for all school names and codes
# Hint: Create a list of school codes to help with index look-up in arrays

schools = {'1224': 'Centennial High School',
           '1679': 'Robert Thirsk School',
           '9626': 'Louise Dean School',
           '9806': 'Queen Elizabeth High School',
           '9813': 'Forest Lawn High School',
           '9815': 'Crescent Heights High School',
           '9816': 'Western Canada High School',
           '9823': 'Central Memorial High School',
           '9825': 'James Fowler High School',
           '9826': 'Ernest Manning High School',
           '9829': 'William Aberhart High School',
           '9830': 'National Sport School',
           '9836': 'Henry Wise Wood High School',
           '9847': 'Bowness High School',
           '9850': 'Lord Beaverbrook High School',
           '9856': 'Jack James High School',
           '9857': 'Sir Winston Churchill High School',
           '9858': 'Dr. E. P. Scarlett High School',
           '9860': 'John G Diefenbaker High School',
           '9865': 'Lester B. Pearson High School'
           }

school_number = list(schools.keys())
school_name = list(schools.values())

# Add your code within the main function. A docstring is not required for this function.


def main():
    print("ENDG 233 School Enrollment Statistics\n")

    # Print array data here
    data_2021 = np.genfromtxt(
        'SchoolData_2020-2021.csv', delimiter=',', skip_header=True)
    print(f'Array Data for 2020 - 2021:\n{data_2021}')

    data_2020 = np.genfromtxt(
        'SchoolData_2019-2020.csv', delimiter=',', skip_header=True)
    print(f'Array Data for 2019 - 2020:\n{data_2020}')

    data_2019 = np.genfromtxt(
        'SchoolData_2018-2019.csv', delimiter=',', skip_header=True)
    print(f'Array Data for 2018 - 2019:\n{data_2019}')

    # Add request for user input here

    valid = True
    while valid == True:
        requested_school = str(input(
            'Please enter the high school name or school code: '))
        if requested_school in schools.values():
            chosen_school_code = school_number[school_name.index(
                requested_school)]
            valid = False
        elif requested_school in school_number:
            chosen_school_code = requested_school
            valid = False
        else:
            print('You must enter a valid school name or code.')

    print("\n***Requested School Statistics***\n")

    # Print school name and code using the given class
    school_1 = School(schools.get(chosen_school_code), chosen_school_code)
    print(school_1.print_all_stats())

    # Add data processing and plotting here
    print(data_2021[0:1][0:1])

    position_2021 = np.argwhere(data_2021 == int(chosen_school_code))
    a = data_2021[position_2021]
    print(a)


    # print(position_2021)
    # for i in data_2021, data_2020, data_2019:
    #     if i == chosen_school:
    # a =
    # print(f'Mean enrollment for Grade 10:' + ({data_2021[0][1]} + {data_2020[]}
    # print(f'Mean enrollment for Grade 11: {}')
    # print(f'Mean enrollment for Grade 12: {}')
    # Do not modify the code below
if __name__ == '__main__':
    main()
