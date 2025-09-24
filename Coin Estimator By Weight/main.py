import math
# Coin Estimator By Weight

# When some people receive change after shopping, they put it into a container and let it add up over time. Once they fill up the container, they'll roll them up in coin wrappers which can then be traded in at a bank for what they are worth.

# Allow the user to input the total weight of each type of coin they have (pennies, nickels, dimes, and quarters).
# Print out how many of each type of coin wrapper they would need, how many coins they have, and the estimated total value of all their money.

# Subgoals:
# Round all numbers printed out to the nearest whole number.
# Allow the user to select whether they want to submit the weight in either grams or pounds.


print("\nCoin Estimator By Weight\n")

grams_or_pounds = input(
    "Select unit of measurement.\n"
    'Type "grams" or "pounds" (leave blank for grams): '
)

if grams_or_pounds.lower() == "pounds":
    print("You selected pounds.")
else:
    print("You selected grams.")

one_gram_in_lb = 0.0022046226

penny_in_grams = 2.500
nickel_in_grams = 5.000
dime_in_grams = 2.268
quarter_in_grams = 5.670

penny_in_pounds = penny_in_grams * one_gram_in_lb
nickel_in_pounds = nickel_in_grams * one_gram_in_lb
dime_in_pounds = dime_in_grams * one_gram_in_lb
quarter_in_pounds = quarter_in_grams * one_gram_in_lb

coins_in_penny_roll = 50
coins_in_nickel_roll = 40
coins_in_dime_roll = 50
coins_in_quarter_roll = 40

dollar_value_penny = 0.01
dollar_value_nickel = 0.05
dollar_value_dime = 0.10
dollar_value_quarter = 0.25

dollar_value_penny_roll = dollar_value_penny * coins_in_penny_roll
dollar_value_nickel_roll = dollar_value_nickel * coins_in_nickel_roll
dollar_value_dime_roll = dollar_value_dime * coins_in_dime_roll
dollar_value_quarter_roll = dollar_value_quarter * coins_in_quarter_roll

user_pennies_weight = float(input("Enter weight of all pennies: "))
user_nickels_weight = float(input("Enter weight of all nickels: "))
user_dimes_weight = float(input("Enter weight of all dimes: "))
user_quarters_weight = float(input("Enter weight of all quarters: "))

if grams_or_pounds.lower() == "pounds":
    user_number_of_pennies = user_pennies_weight / penny_in_pounds
    user_number_of_nickels = user_nickels_weight / nickel_in_pounds
    user_number_of_dimes = user_dimes_weight / dime_in_pounds
    user_number_of_quarters = user_quarters_weight / quarter_in_pounds
else:
    user_number_of_pennies = user_pennies_weight / penny_in_grams
    user_number_of_nickels = user_nickels_weight / nickel_in_grams
    user_number_of_dimes = user_dimes_weight / dime_in_grams
    user_number_of_quarters = user_quarters_weight / quarter_in_grams

user_number_penny_rolls = math.ceil(user_number_of_pennies / coins_in_penny_roll)
user_number_nickel_rolls = math.ceil(user_number_of_nickels / coins_in_nickel_roll)
user_number_dime_rolls = math.ceil(user_number_of_dimes / coins_in_dime_roll)
user_number_quarter_rolls = math.ceil(user_number_of_quarters / coins_in_quarter_roll)

total_user_penny_value = round((user_number_of_pennies) * dollar_value_penny)
total_user_nickel_value = round((user_number_of_nickels) * dollar_value_nickel)
total_user_dime_value = round((user_number_of_dimes) * dollar_value_dime)
total_user_quarter_value = round((user_number_of_quarters) * dollar_value_quarter)

print("You have:")
print(f'{round(user_number_of_pennies)} pennies, worth ${total_user_penny_value}.')
print(f'{round(user_number_of_nickels)} nickels, worth ${total_user_nickel_value}.')
print(f'{round(user_number_of_dimes)} dimes, worth ${total_user_dime_value}.')
print(f'{round(user_number_of_quarters)} quarters, worth ${total_user_quarter_value}.')
print(f'In total your coins are worth ${sum([total_user_penny_value, total_user_nickel_value, total_user_dime_value, total_user_quarter_value])}')
print("You will need:")
print(f'Penny wrappers: {user_number_penny_rolls}')
print(f'Nickel wrappers: {user_number_nickel_rolls}')
print(f'Dime wrappers: {user_number_dime_rolls}')
print(f'Quarter wrappers: {user_number_quarter_rolls}')
