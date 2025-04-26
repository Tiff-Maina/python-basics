# Compute factorial using a loop

# Input number
n = int(input("Enter a number: "))

# Initialize factorial result
factorial = 1

# Loop from 1 to n
for i in range(1, n + 1):
    factorial *= i  # Multiply each number

# Print the factorial result
print("Factorial of", n, "is", factorial)
