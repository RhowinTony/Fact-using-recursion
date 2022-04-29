#Write a program to calculate factorial of a number using recursion


def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)

try:
    input_val = int(input("Enter any number "))
except ValueError as e:
    print(f"Input is not valid, Please re-run with valid input. - {e}")
else:
    
