# 99 Bottles

# Create a program that prints out every line to the song "99 bottles of beer on the wall."
# Do not use a list for all of the numbers, and do not manually type them all in. Use a built in function instead.
# Besides the phrase "take one down," you may not type in any numbers/names of numbers directly into your song lyrics.
# Remember, when you reach 1 bottle left, the word "bottles" becomes singular.

for bottles in range(99, 0, -1):
    next_bottles = bottles - 1
    if bottles > 1:
        print(f'{bottles} bottles of beer on the wall.')
        print(f'{bottles} bottles of beer.')
        print('If one of the bottles just happen to fall,')
        print(f'{next_bottles} bottles of beer on the wall.')
    elif bottles == 1:
        print(f'{bottles} bottle of beer on the wall.')
        print(f'{bottles} bottle of beer.')
        print('If one of the bottles just happen to fall,')
        print(f'{next_bottles} bottles of beer on the wall.')
    else:
        print(f"No more bottles of beer on the wall,\nno more bottles of beer.\nThere's nothing else to fall,\nbecause there's no more bottles of beer on the wall.")
        break