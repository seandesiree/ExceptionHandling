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
