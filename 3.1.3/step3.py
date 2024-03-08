subtotal = 0.0

# Explaining Menu Options
print("What type of sandwich would you like?")
print("chicken $5.25, beef $6.25, tofu $5.75")
sandwich_type = input("Sandwich Choice: ")
# Calculating Sandwich Price
if sandwich_type == "chicken":
    print("You chose chicken, which will be $5.25")
    subtotal += 5.25
elif sandwich_type == "tofu":
    print("You chose tofu, which will be $5.75")
    subtotal += 5.75
else:
    print("You chose beef, which will be $6.25")
    subtotal += 6.25

drink = input("Would you like a beverage?:")
drink_size = input("What size drink?:")

if drink == "yes":
    if drink_size == "small":
        print("You chose small, which will be $1.00")
        subtotal += 1.00
    elif drink_size == "medium":
        print("You chose medium, which will be $1.75")
        subtotal += 1.75
    else:
        print("You chose large, which will be $2.25")
        subtotal += 2.25
fries = input("Would you like french fries?:")
fries_size = input("What size would you like?:")
if fries == "yes":
    if fries_size == "small":
        print("You chose small, which will be $1.00")
        megasize = input("Would you like to Mega-Size your fries?:")
        if megasize == "yes":
            print("You chose to Mega-Size your fries! That will be $2.00")
            subtotal += 2.00
        else:
            subtotal += 1.00
    elif fries_size == "medium":
        print("You chose medium, which will be $1.50")
        subtotal += 1.50
    else:
        print("You chose large, which will be $2.00")
        subtotal += 2.00

ketchup = float(input("How many ketchup packets would you like? $0.25 each"))
if ketchup >= 0:
    subtotal += ketchup * .25


if drink == "yes":
    if fries == "yes":
        subtotal -= 1.00
print(subtotal)

