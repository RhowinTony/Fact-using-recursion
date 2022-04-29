#Write a program to calculate factorial of a number using recursion

def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)

def int_check(n):
        check_val = int(n)
        if check_val < 0:
            raise ValueError("Value is less than 0.")
        else:
            return check_val

def main():
    try:
        input_val = (input("Enter any number "))
        checked_int = int_check(input_val)
    except ValueError as e:
        print(f"Input is not valid, Please re-run with valid input. - {e}")
    else:
        print(f"The factorial is {fact(checked_int)}")

main()