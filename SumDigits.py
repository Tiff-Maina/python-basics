# Find the sum of digits of a number

# Input number
num = int(input("Enter a number: "))

# Initialize sum
sum_of_digits = 0

# Loop to extract and add each digit
while num > 0:
    digit = num % 10  # Get the last digit
    sum_of_digits += digit  # Add it to the sum
    num //= 10  # Remove the last digit

# Print the result
print("Sum of digits:", sum_of_digits)
