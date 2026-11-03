
# DIP Lab 02 - Task 1
# Program to perform arithmetic operations on two numbers

# Take input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform arithmetic operations
sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2

# Display results
print("\n--- Arithmetic Operations ---")
print("Sum:", sum_result)
print("Difference:", difference)
print("Product:", product)

# Perform division if the second number is not zero
if num2 != 0:
    division = num1 / num2
    print("Division:", division)
else:
    print("Division: Cannot divide by zero.")