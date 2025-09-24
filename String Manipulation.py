# 1. Basics of Python Using Strings

#1. Greeting Message
# Create a variable `customer_name` with the value "Priya". Print a personalized greeting
# message: "Hello, Priya! Welcome."

customer_name = "Priya"
print(f"Hello, {customer_name}! Welcome.")

# #2. Item Label </br>
# Create two variables: `item_name` with "Mango Blast" and `price_per_item` with 80. </br>
# Print a formatted label showing both pieces of information: "Item: Mango Blast, Price: 80 INR".

item_name ="Mango Blast"
price_per_item = 80.0
print(f"Item: {item_name}, Price: {price_per_item} INR")

#3. Order Summary
# Create variables `item1` ("Vanilla Delight"), `item2` ("Chocolate Chip"), and `total_cost`
# (300). Print a summary line: "Order: Vanilla Delight, Chocolate Chip. Total: 300 INR."

item1 = "Vanilla Delight"
item2 = "Chocolate Chip"
total_cost = 300
print(f"Order: {item1}, {item2}. Total: {total_cost} INR")

#4. Dynamic Message
# Create variables `staff_name` ("Arjun") and `current_time` ("10:00 AM"). Print a message
# announcing the staff member on duty: "Current staff member on duty: Arjun. Time: 10:00
# AM."

staff_name = "Arjun"
current_time = "10:00 AM"
print(f"Current staff member on duty: {staff_name}. Time: {current_time}.")

#5. String Length
# Find and print the length of the string "Strawberry Sensation".

print(len("Strawberry Sensation"))

#6. Capitalization
# Create a variable `flavor_name` with "butterscotch crunch". Print the flavor name with the
# first letter of each word capitalized.

flavor_name = "butterscotch crunch"
print(flavor_name.title())

#7. Finding Substrings
# Check if the word "Milk" is present in the ingredient list string "Milk, Cream, Sugar,
# Vanilla". Print `True` or `False` based on the result.

cart = ["Milk", "Cream", "Sugar", "Vanilla"]
print("Milk" in cart)
print("Milky" in cart)

#8. Replacing Text
# In the string "The order is for Rahul. Total amount: 250 INR.", replace the name "Rahul"
# with "Sneha". Print the new string.

s1= "The order is for Rahul. Total amount: 250 INR."
s1_new=s1.replace("Rahul", "Sneha")
print(f"The new string is '{s1_new}'")

#9. Trimming Whitespace
# Remove any leading or trailing spaces from the string " Chocolate Fudge " and print the
# cleaned string.

z = " Chocolate Fudge  "
print(f"Before trimming whitespaces: '{z}'")
print(f"After trimming whitespaces: '{z.strip()}'")

#10. Splitting a String
# Split the string "Monday,Tuesday,Wednesday" by the comma and print the resulting list
# of days.

count = 0
week_days = "Monday,Tuesday,Wednesday"
l = week_days.split(',')
print(f"The resulting list of days is {l}")

#11.Joining a List
# Join the list of ingredients `['Milk', 'Sugar', 'Cream']` into a single string separated by
# hyphens: "Milk-Sugar-Cream".

breakfast_cart = ['Milk', 'Sugar', 'Cream']
print('-'.join(breakfast_cart))

#12. Formatted Receipt Line
# Use an f-string to print a receipt line for an item. The item is "Pista" and the price is 120
# INR. The output should be "Item: Pista, Price: 120.00 INR".

item = "Pista"
price = 120.00
print(f"Item: {item}, Price: {price:.2f} INR")

#13. Multi-line String
# Create a multi-line string that holds an address: "Shop No. 5, Main Road, City Center".
# Print this string.

address= '''Shop No. 5,
Main Road,
City Center.'''
print(address)

 #14. String Reversal
# Take the string "Daily Report" and print it in reverse order.

rep = "Daily Report"
rep[::-1]

#15. Character Counting
# Count the number of times the letter 'a' appears in the string "Banana Caramel".

cup = "Banana Caramel"
count = 0
for i in range(len(cup)):
  if cup[i] == "a":
    count +=1
    print(f"found a vowel 'a' for {count} time")

print(f"No. of a's in {cup} is {count}")



#2. Reading data from command line using input() functions

##1. Simple String Input
# Ask the user for their name and then print a greeting message that includes their name.

username = input("Enter your name: ")
print(f"Hello, {username} !")

##2. Input with a prompt
# Ask the user, "What is today's special flavor?" and store the response in a variable. Print
# the user's response to confirm.

special = input("What is today's special flavor?: ")
print(f"Today's special flavor is {special}.")

##3. Converting input to a number (integer)
# Ask the user for the number of scoops they want. Convert the input to an integer and
# print a confirmation message, e.g., "You ordered 3 scoops."

user_scoops = int(input("Enter the number of scoops user wants : "))
print(f"you ordered {user_scoops} scoops.")

##4. Converting input to a number (float)
# Ask the user for the total price of their purchase. Convert the input to a floating-point
# number and print the total with two decimal places, e.g., "Your total is 125.50 INR."

total_price = float(input("Enter the total price of your purchase: "))
print(f"Your total is {total_price:.2f} INR.")

##5. Basic Calculation with User Input
# Ask for the number of scoops and the price per scoop (e.g., 80 INR). Calculate and print
# the total cost.

price_per_scoop = 80.00
number_of_scoops = int(input("Enter the number of scoops:"))
icecream_total_cost = number_of_scoops * price_per_scoop
print(f"The total cost of your icecream is : {icecream_total_cost:.2f} INR.")

##6. Input for a conditional check
# Ask the user for a password. If the password is "password123", print "Access granted."
# Otherwise, print "Access denied."

password = input("Enter password: ")
if password == 'password123':
  print("Access granted.")
else:
  print("Access denied.")

##7. Input for a loop

# Ask the user how many items they want to add to their order. Use a loop to repeatedly
# ask for the name of an item that many times, and then print a final message confirming
# the number of items added.

no_of_items = int(input("How many items do you want to add to your order? : "))
for i in range(no_of_items):
  input("Enter the name of the item: ")
print(f"{no_of_items} items added to your order!")

##8. Handling potential errors with input
# Ask the user for their age. Write a program that can handle non-numeric input gracefully

# by printing an error message like "Invalid input. Please enter a number." (Hint: Use a `try-
# except` block).

try:
  age = int(input("Enter your age: "))
except:
  print("invalid input. Please enter a number")

##9. Multiple inputs for a transaction
# Ask for the customer's name, the item they purchased, and the total amount. Print a
# complete transaction summary on a single line, e.g., "Transaction for: Anjali, Item: Mango,
# Amount: 150 INR."

name = input("Enter customer name: ")
item = input("Enter item they purchased: ")
amt = eval(input("Enter amount for item: "))
print(f"Transaction for: {name}, Item: {item}, Amount: {amt} INR.")

##10. Using input for a simple menu
# Display a menu: "1. View Menu, 2. Place Order, 3. Exit". Ask the user to enter a number
# and then print a message based on their choice (e.g., "You chose to place an order.").

Main_menu = {1: "View Menu", 2: "Place Order", 3: "Exit"}
user_choice = eval(input("Select an option(1/2/3): "))
print(f"You chose to {Main_menu[user_choice]}.")

##11. Input and string concatenation
# Ask for the customer's first name and last name separately. Combine them and print their
# full name.

last_name = input("Enter customer's last name:  ")
first_name = input("Enter customer's first name: ")
print(f"Customer's full name is {first_name + last_name}")
print(f"{first_name.title()} {last_name.title()}")

##12. Input to check stock
# Ask the user for an ingredient name. If the ingredient is "Milk", print "Stock is available."
# Otherwise, print "Ingredient not in stock."

ingredient = input("Enter the ingredient name: ")
if ingredient == "Milk":
  print("Stock is available.")
else:
  print("Ingredient not in stock.")

##13. Input to update a value
# A variable `daily_target` is 50. Ask the user for the number of items sold today. If the sales
# number is greater than or equal to the target, print "Daily target met!"

daily_target = 50
items_sold = eval(input("Enter the number of items sold today: "))
if items_sold >= 50:
  print("Daily target met!")

#14. Input to control a `while` loop
# Ask the user for input. The program should continue to ask for input until the user types
# "exit".

while 1:
  j= input("Enter an input: ")
  if j == "exit":
    break

#15. Password verification with a loop
# Ask the user for a password. If it is incorrect, tell them and ask again. The loop should
# stop only when the correct password is entered. The correct password is "admin".

while 1:
  password = input("Enter password: ")
  if password == "admin":
    break
  else:
    print("incorrect password")
