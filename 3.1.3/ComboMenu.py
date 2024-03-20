subtotal = 0.00

selected_a_sandwich = True
selected_a_beverage = True
selected_fries = True
order = []

food = input("Do you want chicken($5.25), beef($6.25), tofu(5.75), or no food?")
# Explaining Menu Options
sandwich_type = input("Sandwich Choice: ")

# Calculating Sandwich Price
if sandwich_type == "chicken":
    print("You chose chicken, which will be $5.25")
    subtotal += 5.25
    order.append("Chicken Sandwich")
elif sandwich_type == "tofu":
    print("You chose tofu, which will be $5.75")
    subtotal += 5.75
    order.append("Tofu Sandwich")
else:
    print("You chose beef, which will be $6.25")
    subtotal += 6.25
    order.append("Beef Sandwich")

# Beverage Choice
bev_choice = input("Do you want a beverage? yes or no")
if bev_choice == "yes":
    order.append("Beverage")
    bev_size = input("What size beverage would you like? Small, Medium, or Large")
    if bev_size == "small":
        print("You chose small, so $1.00")
        subtotal += 1
    if bev_size == "medium":
        print("You chose medium, so $1.75")
        subtotal += 1.75
    if bev_size == "large":
        print("You chose large, so $2.25")
        subtotal += 2.25
else:
    selected_a_beverage = False

# Fries
fry_choice = input("Do you want french fries? yes or no")
if fry_choice == "yes":
    order.append("Fries")
    fry_size = input("What size fries would you like? Small, Medium, or Large")
    if fry_size == "small":
        supersize = input("Do you want to supersize that for $2? Yes or no")
        if supersize == "yes":
            fry_size = "large"
            subtotal += 2
        else:
            print("You chose small fries for $1")
            subtotal += 1
    elif fry_size == "medium":
        print("You chose medium for $1.50")
        subtotal += 1.50
    else:
        print("You chose large fries for $2")
        subtotal += 2
else:
    selected_fries = False

# Ketchup
ketchup = float(input("How many ketchup packets would you like? $0.25 each"))
if ketchup >= 0:
    subtotal += ketchup * .25
    order.append("Ketchup")

if bev_choice == "yes" and fry_choice == "yes":
    subtotal -= 1

if bev_choice == "yes":
    print(bev_size)
if fry_choice == "yes":
    print(fry_size)

print(subtotal)
print("You ordered the following:", order)








