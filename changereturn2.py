#changereturn2.py

total = int(input("How much change do you have?: "))


def change(total):

        quarters = total // 25
        total %= 25
        dimes = total // 10
        total %= 10
        nickles = total // 5
        total %= 5
        pennies = total
        return print("quarters: %s\ndimes: %s\nnickles: %s\npennies: %s"  %  (quarters, dimes, nickles, pennies))


change(total)
