
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






