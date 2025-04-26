# Compute factorial using recursion

def factorial(n):
    # Base Case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive Case: n * factorial of (n-1)
        return n * factorial(n - 1)

# Input number
number = int(input("Enter a number: "))

# Call the recursive function
result = factorial(number)

# Print the result
print("Factorial of", number, "is", result)
