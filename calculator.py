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

        try:
            num1 = float(input_list[1])         
        except ValueError as e:
            print("Invalid input. Please enter a number.")
            continue

        if len(input_list) > 2:
            try:
                num2 = float(input_list[2])
            except ValueError as e:
                print("Invalid input. Please enter a number.")
                continue


        if input_list[0] == '+':
            solution = arithmetic.add(num1, num2)
        elif input_list[0] == '-': 
            solution = arithmetic.subtract(num1, num2)
        elif input_list[0] == '*':
            solution = arithmetic.multiply(num1, num2)
        elif input_list[0] == '/':
            solution = arithmetic.divide(num1, num2)
        elif input_list[0] == 'square':
            solution = arithmetic.square(num1)
        elif input_list[0] == 'cube':
            solution = arithmetic.cube(num1)
        elif input_list[0] == 'pow':
            solution = arithmetic.power(num1, num2)
        elif input_list[0] == 'mod':
            solution = arithmetic.mod(num1, num2)

        else:
            print("Not a valid arithmetic operator. Please enter a real one.")
            continue

        print(solution)

        

    

# Your code goes here
