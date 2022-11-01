def total_print(number_of_locations):
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

    print("Total Printing Cost: $" + str(printing_cost))
    return printing_cost

def total_setup(quantity):
    if quantity < 288:
        setup_cost = float(input("Setup Cost: $"))
        number_of_setups = float(input("Number of set ups: "))
        if quantity > 0:
            setup_piece = round(setup_cost / quantity, 2)
            print("Setup cost per piece: $" + str(setup_piece))
        else:
            setup_piece = 0.00
    elif quantity >= 288:
         setup_cost = 0
         setup_piece = 0.00

    return setup_piece

def private_label(check_private_label):
    if check_private_label == "y":
        private_label_float = float(0.25)
    else:
        private_label_float = 0

    print("Private Label Cost: $" + str(private_label_float))
    return private_label_float

def finishing(check_finishing):
    if check_finishing == "y":
        finishing_cost_float = float(input("Finishing Cost: $"))
    else: finishing_cost_float = 0

    return finishing_cost_float

def margin_convert(margin_input):
    try:
        margin_float = float(margin_input)
    except:
        print("Please enter a valid number.")
        margin_input = input("Profit Margin: ")
        margin_float = margin_convert(margin_input)
        return margin_float
    else:
        return margin_float

def margin_invert(margin_output):
    if margin_output < 0:
        inverted_margin = 1 - margin_output
    elif margin_output > 0:
        inverted_margin = 1 - margin_output / 100
    return inverted_margin

def add_cost(blank_cost, printing_cost, setup_piece, private_label, finishing_cost):
    cost = float(blank_cost) + float(printing_cost) + float(setup_piece) + float(private_label_cost) + float(finishing_cost)
    return cost

def calc_fun(check):
    if check != "y":
        exit_check()
    elif check == "y":
        item_number = input("Item Number: ")
        quantity = float(input("Quantity: "))
        blank_cost = float(input("Blank Cost: $"))
        two_xl_check = input("2XLs? y/n ")

        if two_xl_check == "y":
            two_xl_cost = float(input("2XL Cost: $"))
        else: two_xl_cost = 0

        three_xl_check = input("3XLs? y/n ")

        if three_xl_check == "y":
            three_xl_cost = float(input("3XL Cost: $"))
        else: three_xl_cost = 0

        number_of_locations = float(input("Number of Locations: "))
        printing_cost = total_print(number_of_locations)
        set_piece = total_setup(quantity)

        check_private_label = input("Private Label? y/n ")
        private_label_cost = private_label(check_private_label)

        check_finishing = input("Finishing? y/n ")
        finishing_cost = finishing(check_finishing)

        margin_input = input("Profit Margin: ")
        margin_output = margin_convert(margin_input)
        final_margin = margin_invert(margin_output)
        total_cost = add_cost(blank_cost, printing_cost, set_piece, private_label_cost, finishing_cost)
        print(margin_output)
        print(final_margin)
        print(total_cost)

def exit_check():
    want_to_exit = input("Would you like to exit? y/n ")

    if want_to_exit == "y":
        quit()
    else:
        check = input("Would you like to price a garment? y/n ")
        calc_fun(check)


print("Welcome to the pricing calculator.")
print("Type 'y' or 'n' when promted.")
check = input("Would you like to price a garment? y/n ")

calc_fun(check)
