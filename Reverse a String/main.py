# Reverse a String
# Enter a string and the program will reverse it and print it out.

def reverse_string(string: str) -> str:
    return string[::-1]

input_string: str = reverse_string(input("Type string to reverse: "))

print(input_string)