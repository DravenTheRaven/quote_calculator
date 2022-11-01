def blank(check):
    if check == "y":
        blank_cost = input("Blank Cost: $")
        try:
            blank_float = float(blank_cost)
        except:
            print("Please enter a valid number.")
            blank_float = blank(check)
            return blank_float
        else:
            return blank_float
    return blank_cost

def quantity_check(check):
    if check == "y":
        quantity_output = input("Quantity: ")
        try:
            quantity_int = int(quantity_output)
        except:
            print("Please enter a valid number")
            quantity_int = quantity_check(check)
            return quantity_int
        else:
            return quantity_int
    return quantity_output

def locations():
    num_loc = input("Number of Locations: ")
    try:
        float(num_loc) >= 0 or float(num_loc) <= 5
    except:
        print("Please enter a valid number.")
        num_loc = locations()
        return num_loc
    return num_loc

def lo_one():
    lo_one_cost = input("Location One: $")
    try:
        lo_one_float = float(lo_one_cost)
    except:
        print("Please enter a valid number.")
        lo_one_float = lo_one()
        return lo_one_float
    else:
        return lo_one_float
    return lo_one_cost

def lo_two():
    lo_two_cost = input("Location Two: $")
    try:
        lo_two_float = float(lo_two_cost)
    except:
        print("Please enter a valid number.")
        lo_two_float = lo_two()
        return lo_two_float
    else:
        return lo_two_float
    return lo_two_cost

def lo_three():
    lo_three_cost = input("Location Three: $")
    try:
        lo_three_float = float(lo_three_cost)
    except:
        print("Please enter a valid number.")
        lo_three_float = lo_three()
        return lo_three_float
    else:
        return lo_three_float
    return lo_three_cost

def lo_four():
    lo_four_cost = input("Location Four: $")
    try:
        lo_four_float = float(lo_four_cost)
    except:
        print("Please enter a valid number.")
        lo_four_float = lo_four()
        return lo_four_float
    else:
        return lo_four_float
    return lo_four_cost

def lo_five():
    lo_five_cost = input("Location Five: $")
    try:
        lo_five_float = float(lo_five_cost)
    except:
        print("Please enter a valid number.")
        lo_five_float = lo_five()
        return lo_five_float
    else:
        return lo_five_float
    return lo_five_cost

def total_print(number_of_locations):
    if float(number_of_locations) == 0:
        printing_cost = 0
    elif float(number_of_locations) == 1:
        printing_cost = lo_one()
    elif float(number_of_locations) == 2:
        location_one = lo_one()
        location_two = lo_two()
        printing_cost = location_one + location_two
    elif float(number_of_locations) == 3:
        location_one = lo_one()
        location_two = lo_two()
        location_three = lo_three()
        printing_cost = location_one + location_two + location_three
    elif float(number_of_locations) == 4:
        location_one = lo_one()
        location_two = lo_two()
        location_three = lo_three()
        location_four = lo_four()
        printing_cost = location_one + location_two + location_three + location_four
    elif float(number_of_locations) == 5:
        location_one = lo_one()
        location_two = lo_two()
        location_three = lo_three()
        location_four = lo_four()
        location_five = lo_five()
        printing_cost = location_one + location_two + location_three + location_four + location_five
    else:
        print("Please enter a valid number.")
        number_of_locations = locations()
        printing_cost = total_print(number_of_locations)
        return printing_cost
    print("Total Printing Cost: $" + str(printing_cost))
    return printing_cost

def total_setup(quantity):
    if int(quantity) < 288:
        setup_cost = input("Setup Cost: $")
        number_of_setups = input("Number of set ups: ")
        if int(quantity) > 0:
            setup_piece = round(float(setup_cost) * float(number_of_setups) / float(quantity), 2)
            print("Setup cost per piece: $" + str(setup_piece))
        else:
            setup_piece = 0.00
    elif int(quantity) >= 288:
         setup_cost = 0
         setup_piece = 0.00

    return setup_piece

def hard_setup(quantity, check):
    if check == "y":
        i = 1
        hard_setup = 0
        while i != 0:
            set_float = input(f"Location {i} Cost: $")
            letter_code = input("Price Code: ")
            net_set = price_code(letter_code, set_float)
            hard_setup += float(net_set)
            check = input("Is there another setup? y/n ")
            if check == "y":
                i += 1
            else:
                i = 0
        else:
            set_piece = hard_setup / quantity
            print(f"Total Setup Cost: ${hard_setup}")
            print(f"Setup per Piece: ${set_piece}")
            return set_piece
    else:
        set_piece = 0
        return set_piece



def private_label(check_private_label):
    if check_private_label == "y":
        private_label_float = float(0.25)
    else:
        private_label_float = 0

    print("Private Label Cost: $" + str(private_label_float))
    return private_label_float

def finishing(check_finishing):
    if check_finishing == "y":
        finishing_cost = input("Finishing Cost: $")
        try:
            finishing_float = float(finishing_cost)
        except:
            print("Please enter a valid number.")
            finishing_float = finishing(check_finishing)
            return finishing_float
        else:
            return finishing_float
    else:
        finishing_float = 0
        return finishing_float

    return finishing_cost

def three_xl_cost_input(three_xl_check):
    if three_xl_check == "y":
        three_xl_cost = input("3XL Cost: $")
        try:
            three_xl_float = float(three_xl_cost)
        except:
            print("Please enter a valid number.")
            three_xl_float = three_xl_cost_input(three_xl_check)
            return three_xl_float
        else:
            return three_xl_float
    else:
        three_xl_cost = 0
        return three_xl_cost

def two_xl_cost_input(two_xl_check):
    if two_xl_check == "y":
        two_xl_cost = input("2XL Cost: $")
        try:
            two_xl_float = float(two_xl_cost)
        except:
            print("Please enter a valid number.")
            two_xl_float = two_xl_cost_input(two_xl_check)
            return two_xl_float
        else:
            return two_xl_float
    else:
        two_xl_cost = 0
    return two_xl_cost

def add_cost(blank_cost, printing_cost, setup_piece, private_label_cost, finishing_cost):
    if blank_cost != 0:
        cost = float(blank_cost) + float(printing_cost) + float(setup_piece) + float(private_label_cost) + float(finishing_cost)
        return cost
    else:
        cost = 0
        return cost

def three_xl_cost_check(total_three_xl_cost):
    if total_three_xl_cost > 0:
        print("Total 3XL Cost: $" + str(total_three_xl_cost))
    else:
        pass

def two_xl_cost_check(total_two_xl_cost):
    if total_two_xl_cost > 0:
        print("Total 2XL Cost: $" + str(total_two_xl_cost))
    else:
        pass

def three_xl_price_check(three_xl_price):
    if three_xl_price > 0:
        print("3XL Price: $" + str(three_xl_price))
    else:
        pass

def two_xl_price_check(two_xl_price):
    if two_xl_price > 0:
        print("2XL Price: $" + str(two_xl_price))
    else:
        pass

def price_margin(total_cost, final_margin):
    price_float = float(total_cost) / float(final_margin)
    return price_float

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
    if margin_output < 1:
        inverted_margin = 1 - margin_output
        return inverted_margin
    elif margin_output >= 1:
        inverted_margin = (100 - margin_output) / 100
        return inverted_margin

def calc_fun(check):
    if check != "y":
        exit_check()
    elif check == "y":
        customer = input("Customer: ")
        job_name = input("Job Name: ")
        item_number = input("Item Number: ")
        color = input("Color: ")
        quantity = quantity_check(check)
        blank_cost = blank(check)

        two_xl_check = input("2XLs? y/n ")
        two_xl_cost = two_xl_cost_input(two_xl_check)

        three_xl_check = input("3XLs? y/n ")
        three_xl_cost = three_xl_cost_input(three_xl_check)

        number_of_locations = locations()
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
        print("Total Cost: $" + str(total_cost))

        total_two_xl_cost = add_cost(two_xl_cost, printing_cost, set_piece, private_label_cost, finishing_cost)
        two_xl_print_toggle = two_xl_cost_check(total_two_xl_cost)

        total_three_xl_cost = add_cost(three_xl_cost, printing_cost, set_piece, private_label_cost, finishing_cost)
        three_xl_print_toggle = three_xl_cost_check(total_three_xl_cost)

        price = price_margin(total_cost, final_margin)
        print("Price SM-XL: $" + str(price))

        two_xl_price = price_margin(total_two_xl_cost, final_margin)
        two_xl_price_check(two_xl_price)

        three_xl_price = price_margin(total_three_xl_cost, final_margin)
        three_xl_price_check(three_xl_price)

        print("Hit enter to continue...")
        input(".....")

        save_check(customer, job_name, color, price, two_xl_check, two_xl_price, three_xl_check, three_xl_price, item_number, quantity)
    exit_check()

def price_code(letter_code, price):
    price = float(price)
    if letter_code == 'a' or letter_code =='p':
        price *= 0.5
        print(f"Net cost: {price}")
    elif letter_code == 'b' or letter_code == 'q':
        price *= 0.55
        print(f"Net cost: {price}")
    elif letter_code == 'c' or letter_code == 'r':
        price *= 0.6
        print(f"Net cost: {price}")
    elif letter_code == 'd' or letter_code == 's':
        price *= 0.65
        print(f"Net cost: {price}")
    elif letter_code == 'e' or letter_code =='t':
        price *= 0.70
        print(f"Net cost: {price}")
    elif letter_code == 'f' or letter_code == 'u':
        price *= 0.75
        print(f"Net cost: {price}")
    elif letter_code == 'g' or letter_code == 'v':
        price *= 0.8
        print(f"Net cost: {price}")
    elif letter_code == 'h':
        price *= .85
        print(f"Net cost: {price}")
    elif letter_code =='n' or letter_code == 'none' or letter_code == 0 or letter_code == 'no':
        print(f"Net cost: {price}")
    else:
        letter_code = input("Please enter a valid price code: ")
        price_float = price_code(letter_code, price)
        return price_float
    return price

#def net_convert(float_code, blank_cost)

def hard_fun(check):
    if check != "y":
        exit_check()
    elif check == "y":
        customer = input("Customer: ")
        job_name = input("Job Name: ")
        item_number = input("Item Number: ")
        color = input("Color: ")
        quantity = quantity_check(check)
        blank_cost = blank(check)
        letter_code = input("Price Code: ")
        net_cost = price_code(letter_code, blank_cost)
        setup_check = input("Are there setup costs? y/n")
        total_setup_cost = hard_setup(quantity, setup_check)
        exit_check()
def exit_check():
    want_to_exit = input("Would you like to exit? y/n ")

    if want_to_exit == "y":
        quit()
    else:
        check = input("Return to menu? y/n ")
        if check == "n":
            quit()
        else: menu()

def save_check(customer, job_name, color, price, two_xl_check, two_xl_price, three_xl_check, three_xl_price, item_number, quantity):
    want_to_save = input("Would you like to save this quote? y/n")
    if want_to_save == "n":
        exit_check()
    elif want_to_save == "y":
        f_name = input("Save as: ")
        f = open(f"{f_name}", "a")

        f.write(
f"""Customer: {customer}
Job Name: {job_name}
Item Number: {item_number}
Color: {color}
""")
        f.write(
f"""Quantity: {quantity}
""")
        f.write(
f"""Price SM-XL: ${price}.
""")
        if two_xl_check == "y":
            f.write(
f"""Price 2XL: ${two_xl_price}
""")
        else:
            pass
        if three_xl_check == "y":
            f.write(
f"""Price 3XL: ${three_xl_price}
""")
        else:
            pass

        f.write(
"""
""")
        f.close()

def menu():
    print("Main Menu: ")
    print("Screen Printing")
    print("Hard Goods")
    print("Embroidery")
    print("Exit")
    print("About")
    print("Type 's' for screen printing, 'h' for hard goods, and 'e for embroidery'")
    print("Type 'exit' to exit and 'about' to learn about the program")
    menu_input = input("Choose an option: ")
    if menu_input == "s":
        menu_input = 'y'
        calc_fun(menu_input)
    elif menu_input == "exit":
        exit_check()
    elif menu_input == "e":
        embroidery_fun()
    elif menu_input == "about":
        about()
    elif menu_input == "h":
        menu_input = "y"
        hard_fun(menu_input)
    else:
        menu_input = input("Please enter a valid option: ")
        menu()
    return


menu()
print("Welcome to the pricing calculator.")
print("Type 'y' or 'n' when promted.")
print("The program is kind of dumb, so you have to enter those exactly")
print("It shouldn't throw any errors, but if it gets stuck in a loop,")
print("then you should close the program and try again")
input("Press any key to continue...")
check = input("Would you like to price an item? y/n ")

calc_fun(check)
