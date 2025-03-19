'''
Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
Perform the operation based on the user's input and print the result.
Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.
'''

def calculate():
    num1=float(input('Enter your first number:'))
    num2 = float(input('Enter your second number:'))
    operation=input('Enter operation:')
    answer = 0
    if operation == '+':
        answer=num1+num2
    elif operation == '/':
        answer=num1/num2
    elif operation == '-':
        answer=num1-num2
    elif operation == '*':
        answer=num1*num2

    print(f'{num1} {operation} {num2} = {answer}')

calculate()