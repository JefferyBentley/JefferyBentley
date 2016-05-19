#simpleunitconvert.py

#a simple program that prompts the user for a number of miles
#then prints the equivalent number of feet.

#x = 5280
#a = input
#print(input("How many miles do you want to convert?: "), a)
#print(a)

#y = a / x

#print(y)



def miles_to_feet(): #function to convert miles to feet
    miles = float(input("Enter distance in miles: ")) # miles = input in miles use a float or integer
    feet = 5280 * miles#turn miles into feet, this is the conversion
    print(miles, "miles = ", feet, "feet")#print the input(miles) and the conversion(feet)

    #if miles is not float or int:
        #print("You must enter a NUMBER! ")

miles_to_feet()#call the function to execute the program
