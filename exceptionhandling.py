# 1. Exceptional Weather Forecast


try:   
   user_input = float(input("Please enter a temperature in Fahrenheit. "))
except ValueError:
   print("That was not a valid number. Please try again. ")


def converter(user_input):
   try:
       celsuis = (user_input - 32) * 5/9
   except ZeroDivisionError:
       print("Sorry but you can not divide by zero. ")
   else:
       print(f"You've successfully converted the temperature {celsuis} to celsius")

converter(user_input)



try:
    recipe_servings = float(input("How many servings does the recipe make? "))
    user_servings = float(input("How many servings would you like to make? "))
except ValueError:
    print("Please enter a valid number. ")

def quantity_calculator(recipe_servings, user_servings):
    try:
        calculation = recipe_servings / user_servings
    except ZeroDivisionError:
        print("You can not divide by zero. Please enter another number. ")
    except ValueError:
        print("Please enter a valid number. ")
    else:
        print(f"Your calculation is complete. The serving size is {calculation}")
    finally:
        print("Hope you enjoy cooking! ")

quantity_calculator(recipe_servings, user_servings)




