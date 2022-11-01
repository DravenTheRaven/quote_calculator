item_number = input("Blank Item Number: ")
blank_cost = float(input("Blank Cost: $"))
two_xl_check = input("2XLs? y/n ")

if two_xl_check == "y":
    two_xl_cost = float(input("2XL Cost: $"))
else: two_xl_cost = 0

three_xl_check = input("3XLs? y/n ")

if three_xl_check == "y":
    three_xl_cost = float(input("3XL Cost: $"))
else: three_xl_cost = 0

quantity = float(input("Quantity: "))
number_of_locations = float(input("Number of Locations: "))

if number_of_locations == 0:
    printing_cost = 0
elif number_of_locations == 1:
    printing_cost = float(input("Location 1: $"))
elif number_of_locations == 2:
    location_one = float(input("Location 1: $"))
    location_two = float(input("Location 2: $"))
    printing_cost = location_one + location_two
elif number_of_locations == 3:
    location_one = float(input("Location 1: $"))
    location_two = float(input("Location 2: $"))
    location_three = float(input("Location 3 $" ))
    printing_cost = location_one + location_two + location_three
elif number_of_locations == 4:
    location_one = float(input("Location 1: $"))
    location_two = float(input("Location 2: $"))
    location_three = float(input("Location 3: $" ))
    location_four = float(input("Location 4: $"))
    printing_cost = location_one + location_two + location_three + location_four
elif number_of_locations == 5:
    location_one = float(input("Location 1: $"))
    location_two = float(input("Location 2: $"))
    location_three = float(input("Location 3: $" ))
    location_four = float(input("Location 4: $"))
    location_five = float(input("Location 5: $"))
    printing_cost = location_one + location_two + location_three + location_four + location_five

print("Total Printing Cost: " + str(printing_cost))

if quantity < 288:
    setup_cost = float(input("Setup Cost: $"))
    number_of_setups = float(input("Number of set ups: "))
    if quantity > 0:
        setup_piece = round(setup_cost / quantity, 2)
        print("Setup cost per piece: $", setup_piece)
    else:
        setup_piece = 0.00
elif quantity >= 288:
     setup_cost = 0
     setup_piece = 0.00

check_private_label = input("Private Label? y/n ")

if check_private_label == "y":
    private_label = 0.25
else:
    private_label = 0.00

check_finishing = input("Finishing? y/n " )

if check_finishing == "y":
    finishing = float(input("Finishing: $"))
else:
    finishing = 0.00

profit_margin = (100 - float(input("Profit Margin: "))) / 100

total_cost = blank_cost + printing_cost + setup_piece + private_label + finishing

if two_xl_check == "y":
    total_two_xl_cost = two_xl_cost + printing_cost + setup_piece + private_label + finishing
else:
    total_two_xl_cost = 0

if three_xl_check == "y":
    total_three_xl_cost = three_xl_cost + printing_cost + setup_piece + private_label + finishing
else:
    total_three_xl_cost = 0

print("Total Cost: $" + str(total_cost))

if two_xl_cost > 0:
    print("Total 2XL Cost: $" + str(total_two_xl_cost))

if three_xl_cost > 0:
    print("Total 3XL Cost: $" + str(total_three_xl_cost))


price = total_cost / profit_margin
two_xl_price = total_two_xl_cost / profit_margin
three_xl_price = total_three_xl_cost / profit_margin

print("Price SM-XL: $" + str(price))

if two_xl_price > 0:
    print("Price 2XL: $" + str(two_xl_price))

if three_xl_price > 0:
    print("Price 3XL: $" + str(three_xl_price))
