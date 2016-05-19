#changereturn.py

# Some supermarkets have automatic change dispensers. Let's write code that
#figures out how to divy up an amount of change into the fewest quarters, dimes,
#nickels, and pennies

value_quarter = 25
value_dime = 10
value_nickel = 5
value_penny = 1

number_cents = int(input("How much change do you have?: "))




my_extracted_change = ("Your change is {quarters} quarters ,{dimes} dimes, {nickels} nickels and {pennies} pennies ")


quarters = number_cents % value_quarter
dimes = quarters % value_dime
nickels = dimes % value_nickel
pennies = nickels % value_penny

my_transformed_extracted_change = my_extracted_change.format(
quarters = quarters,
dimes = dimes,
nickels = nickels,
pennies = pennies

)

print(my_transformed_extracted_change)
print()
