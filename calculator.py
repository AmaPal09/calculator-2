"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

import arithmetic


loop_bool = True

while loop_bool:
    input_str = input("> ")
    input_list = input_str.split(" ")

    if input_list[0] == 'q': 
        loop_bool = False 
        quit()
    else:
        solution = 0
        if input_list[0] == '+':
            solution = arithmetic.add(float(input_list[1]), float(input_list[2]))
        print(solution)

        

    

# Your code goes here
