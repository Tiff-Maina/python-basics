# Reverse a string without using [::-1] or built-in reversed()

# Input string
text = input("Enter a string: ")

# Initialize an empty string to store reversed result
reversed_text = ""

# Loop through the string from last character to first
for i in range(len(text) - 1, -1, -1):
    reversed_text += text[i]  # Add each character in reverse order

# Print the reversed string
print("Reversed string:", reversed_text)
