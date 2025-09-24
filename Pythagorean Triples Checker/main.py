from math import gcd as comprime
# Pythagorean Triples Checker

# Allows the user to input the sides of any triangle in any order.
# Return whether the triangle is a Pythagorean Triple or not.
# Loop the program so the user can use it more than once without having to restart the program.

while True:
    print("Welcome to Pythagorean Triples Checker!")
    print('Type "quit" and press enter at any time to quit.')

    input_one = input("Input the first side of the triangle:\n")
    if input_one == "quit":
        break
    input_two = input("Input the second side of the triangle:\n")
    if input_two == "quit":
        break
    input_three = input("Input the third side of the triangle:\n")
    if input_three == "quit":
        break

    triangle = [int(input_one), int(input_two), int(input_three)]
    triangle.sort()
    [a, b, c] = triangle
    if a**2 + b**2 == c**2:
        is_coprime = comprime(a, b, c) == 1
        if is_coprime:
            print("You got a primitive Pythagorean Triple!\n")
        else:
            print("You got a Pythagorean Triple.\n")
    else:
         print("You do not have a Pythagorean Triple.\n")