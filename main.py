#Write a program to calculate factorial of a number using recursion


def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)



input_val = int(input("Enter any number "))
print(fact(input_val))