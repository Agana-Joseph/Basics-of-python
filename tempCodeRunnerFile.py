try:
    num = float(input("Enter a number: "))
    result = check_number(num)
    print(f"The number {num} is {result}.")
except ValueError:
    print("Invalid input. Please enter a valid number.")
