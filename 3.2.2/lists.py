

# a list of menu items
food = ["Burger", "Shake", "Fries"]
first_menu_item = food[0]

print(first_menu_item, "is located at index 0.")

if "Shake" in food:
  print("One shake, coming up!")
else:
  print("Sorry, we don't carry sundaes")
if "Burger" in food:
    print("One burger, coming up!")
else:
    print("We don't carry serve burgers, sorry!")
if "Fries" in food:
    print("One order of fries on the way!")
else:
    print("We don't sell fries here, sorry!")

if "Pizza" in food:
    print("One pizza coming up!")
else:
    print("Sorry, we don't have pizza at the moment")

#print(food[-1]) # prints the last element of the list, food