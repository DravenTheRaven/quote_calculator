#every input has validation and won't let you enter anything invalid

#takes the menu input as check and gets blank cost
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

#takes the menu input and gets quantity all of the check things
#will be depreciated soon
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

#setup fees are only for orders less than 288. this will only show if the quantity is >= 288
def total_setup(quantity):
    num_set_str = "Number of Setups:"
    set_str = "Setup Cost: $"

    if int(quantity) < 288:
        setup_cost = float_validate(set_str)
        number_of_setups = int_validate(num_set_str)
        if int(quantity) > 0:
            setup_piece = float(setup_cost) * float(number_of_setups) / float(quantity)

            print(f"Setup cost per piece: ${setup_piece:.2f}")
        else:
            setup_piece = 0.00
    elif int(quantity) >= 288:
         setup_cost = 0
         setup_piece = 0.00

    return setup_piece

#the setups fees work differently in hard goods
def hard_setup(quantity, set_check_str, more_set_str, p_code_str):
    check = simple_y_n(set_check_str)
    if check == "y":
        i = 1
        hard_setup = 0
        while i != 0:
            var_str = f"Location {i} Cost: $"
            #set_float = input(f"Location {i} Cost: $")
            set_float = float_validate(var_str)

            net_set = price_code(p_code_str, set_float)
            hard_setup += float(net_set)
            check = simple_y_n(more_set_str)
            if check == "y":
                i += 1
            else:
                i = 0
        else:
            set_piece = round(float(hard_setup) / float(quantity), 2)
            if float(set_piece) < 0.01:
                set_piece += 0.01
                print(f"Total Setup Cost: ${hard_setup:.2f}")
                print(f"Setup per Piece: ${set_piece:.2f}")
                return set_piece
            else:
                print(f"Total Setup Cost: ${hard_setup:.2f}")
                print(f"Setup per Piece: ${set_piece:.2f}")
                return set_piece

            print(f"Total Setup Cost: ${hard_setup:.2f}")
            print(f"Setup per Piece: ${set_piece:.2f}")
            return set_piece
    else:
        set_piece = 0
        return set_piece

#checks if the order needs private neck labels. they have a static price of $0.25
def private_label(private_check_str):
    check_private_label = input(f"{private_check_str}")
    if check_private_label == "y":
        private_label_float = float(0.25)
    elif check_private_label == "n":
        private_label_float = 0
    else:
        print("Please enter a valid option")
        private_label_float = private_label(private_check_str)
        return private_label_float

    print(f"Private Label Cost: $ {private_label_float}")
    return private_label_float

#adds the total cost. in previous versions there were three of these to account for 2xl and 3xl
def add_cost(blank_cost, printing_cost, setup_piece, private_label_cost, finishing_cost):
    if blank_cost != 0:
        cost = float(blank_cost) + float(printing_cost) + float(setup_piece) + float(private_label_cost) + float(finishing_cost)
        return cost
    else:
        cost = 0
        return cost

#different function because it has a different amount of arguments. will consolidate later
def hard_add_cost(blank_cost, printing_cost, total_setup_cost):
    if blank_cost != 0:
        cost = float(blank_cost) + float(printing_cost) + float(total_setup_cost)
        print(f"Total Cost: ${cost:.2f}")
        return cost
    else:
        cost = 0
        return cost

#makes sure there are 3xl before it prints
def three_xl_cost_check(total_three_xl_cost):
    if total_three_xl_cost > 0:
        print(f"Total 3XL Cost: ${total_three_xl_cost:.2f}")
    else:
        pass

#same for this one. will consolidate
def two_xl_cost_check(total_two_xl_cost):
    if total_two_xl_cost > 0:
        print(f"Total 2XL Cost: ${total_two_xl_cost:.2f}")
    else:
        pass

#these are seperate functions becuase of the order I want them to print
def three_xl_price_check(three_xl_price):
    if float(three_xl_price) > 0:
        print(f"3XL Price: ${three_xl_price:.2f}")
    else:
        pass

#same here. will consolidate
def two_xl_price_check(two_xl_price):
    if float(two_xl_price) > 0:
        print(f"2XL Price: ${two_xl_price:.2f}")
    else:
        pass

#calculates sell cost with a simple profit margin equation
def price_margin(total_cost, final_margin):
    price_float = float(total_cost) / float(final_margin)
    return price_float

#the user inputs the margin they want. this converts that input into what is needed for the equation
def margin_invert(margin_output):
    if margin_output < 1:
        inverted_margin = 1 - margin_output
        return inverted_margin
    elif margin_output >= 1:
        inverted_margin = (100 - margin_output) / 100
        return inverted_margin

#float validation that loops until valid input is given
def float_validate(var_str):
    num = input(f"{var_str}")
    try:
        float_num = float(num)
    except:
        print("Please enter a valid number...")
        float_num = float_validate(var_str)
        return float_num
    else:
        return float_num

#same as above but integers
def int_validate(var_str):
    num = input(f"{var_str}")
    try:
        int_num = int(num)
    except:
        print("Please enter a valid whole number...")
        int_num = int_validate(var_str)
        return int_num
    else:
        return int_num

#validates yes no questions and gets input if yes
def yes_no_validation(var_str, val_op_str):

    check = input(f"{var_str}")
    if check == "y":
        float_value = float_validate(val_op_str)
        return float_value
    elif check == "n":
        float_value = 0
        return float_value
    else:
        print(f"Please enter a valid option")
        float_value = yes_no_validation(var_str, val_op_str)
        return float_value

#this is the replacement for all the location functions in previous versions
#essentially I learned how to do while loops to write this bit
def location_validation(check):
    if check == "y":
        i = 1
        total_print = 0
        while i != 0:
            var_str = f"Location {i} Cost: $"
            print_cost = float_validate(var_str)
            total_print += float(print_cost)
            check = input("Is there another location? y/n ")
            if check == "y":
                i += 1
            else:
                i = 0
        else:
            print(f"Total Printing Cost: ${total_print:.2f}")
            return total_print
    else:
        total_print = 0
        print(total_print)
        return total_print

#yes no validation without prompting for input
def simple_y_n(var_str):
    check = input(f"{var_str}")
    if check == "y":
        return check
    elif check == "n":
        return check
    else:
        print("Please enter a valid option")
        check = simple_y_n(var_str)
        return check

#similar to location validation but with hard goods there are price codes against
#which the listed price has to be multiplied
#returns 0 if check equals no
def net_print(run_check_str, p_code_str):
    check = simple_y_n(run_check_str)
    if check == "y":
        i = 1
        total_print = 0
        while i != 0:
            var_str = f"Location {i} Cost: $"
            print_cost = float_validate(var_str)
            net_float = price_code(p_code_str, print_cost)
            total_print += float(net_float)
            check = simple_y_n(run_check_str)
            if check == "y":
                i += 1
            elif check == "n":
                i = 0
        else:
            print(f"Total Printing Cost: ${total_print:.2f}")
            return total_print
    else:
        total_print = 0
        print(f"Total Printing Cost: ${total_print:.2f}")
        return total_print

#the function for calculating screen printing costs
def calc_fun(check):
    if check != "y":
        exit_check()

    #string variables for my string literals
    #trying to think of a better way to do things
    #i bet money it's classes
    elif check == "y":
        b_cost_str = "Blank Cost: $"
        valid_num_str = "Please enter a valid number."
        to_print_str = "Total Printing Cost: $"
        set_str = "Setup Cost: $"
        net_str = "Net Cost: $"
        set_piece_str = "Setup per piece: $"
        to_set_str = "Total Setup Cost: $"
        priv_str = "Private Label Cost: $"
        two_x_str = "2XL Cost: $"
        three_x_str = "3XL Cost: $"
        prof_mar_str = "Profit Margin: "
        fin_cost_str = "Finishing Cost: $"
        #yes no questions
        save_str = "Would you like to save this quote? y/n "
        yes_str = "y"
        no_str = "n"
        price_check_str = "Would you like to price an item? y/n "
        two_x_ch_str = "2XLs? y/n "
        three_x_ch_str = "3XLs? y/n "
        men_check_str = "Return to menu? y/n"
        ex_check_str = "Would you like to exit? y/n "
        set_check_str = "Are there set up costs? y/n "
        fin_check_str = "Finishing? y/n "
        private_check_str = "Private labels? y/n "
        more_set_str = "Is there another setup? y/n "
        run_check_str = "Run charge? y/n"
        menu_check_str = "Return to menu? y/n "
        # string inputs
        val_code_str = "Please enter a valid price code. "
        val_op_str = "Please enter a valid option. "
        p_code_str = "Price Code: "
        sa_as_str = "Save as: "
        #integer input
        num_set_str = "Number of Setups:"
        quant_str = "Quantity: "
        num_loc_str = "Number of Locations: "
        val_int_str = "Please enter a valid whole number."
        #end of string definitions

        #basic information about the job. this is printed onto the document that gets saved
        customer = input("Customer: ")
        job_name = input("Job Name: ")
        item_number = input("Item Number: ")
        color = input("Color: ")

        #most of the input and output is handled within the validation functions
        #they loop until you give a valid answer
        quantity = int_validate(quant_str)
        blank_cost = float_validate(b_cost_str)
        #two and three xl are not always on orders and the cost more
        #if yes it functions like the rest of the functions. if no it skips the rest
        two_xl_cost= yes_no_validation(two_x_ch_str, two_x_str)
        three_xl_cost = yes_no_validation(three_x_ch_str, three_x_str)
        #the location validation function asks if there are costs. if yes it takes input and adds it to the total cost and repeats
        #if no it returns the total printing cost. if it is the first iteration printing cost is zero
        printing_cost = location_validation(check)
        set_piece = total_setup(quantity)
        private_label_cost = private_label(private_check_str)
        #uses the same function as 2xl and 3xl
        finishing_cost = yes_no_validation(fin_check_str, fin_cost_str)
        #gets the user's desired profit margin. it can be integer or float
        margin_output = float_validate(prof_mar_str)
        #makes the margin input usable for the program
        final_margin = margin_invert(margin_output)
        #this one is just simple addition
        total_cost = add_cost(blank_cost, printing_cost, set_piece, private_label_cost, finishing_cost)
        print(f"Total Cost: ${total_cost:.2f}")
        #runs even if there are no 2xl/3xl. the price is just zero. the next function prints the cost if it is > 0
        total_two_xl_cost = add_cost(two_xl_cost, printing_cost, set_piece, private_label_cost, finishing_cost)
        two_xl_print_toggle = two_xl_cost_check(total_two_xl_cost)
        total_three_xl_cost = add_cost(three_xl_cost, printing_cost, set_piece, private_label_cost, finishing_cost)
        three_xl_print_toggle = three_xl_cost_check(total_three_xl_cost)
        #price divided by margin
        price = price_margin(total_cost, final_margin)
        print(f"Price SM-XL: ${price:.2f}")
        two_xl_price = price_margin(total_two_xl_cost, final_margin)
        two_xl_price_check(two_xl_price)
        three_xl_price = price_margin(total_three_xl_cost, final_margin)
        three_xl_price_check(three_xl_price)
        print("Hit enter to continue...")
        input(".....")

        #checks if the user wants to save. passes the arguments to be printed for the customer
        save_check(customer, job_name, color, price, two_xl_price, three_xl_price, item_number, quantity)

        #simple return to menu function
        menu_check = simple_y_n(men_check_str)
        if menu_check == "n":
            exit_check()
        elif menu_check == "y":
            menu()
    exit_check()

#takes the price listed on the website and multiplies it by a discount code represented by a letter
#this just takes the letter input and converts it to make it easier for the user
#has similar built in validation to the other functions in this program
def price_code(p_code_str, price):
    letter_code = input(f"{p_code_str}")
    price = float(price)
    if letter_code == 'a' or letter_code =='p':
        price *= 0.5

    elif letter_code == 'b' or letter_code == 'q':
        price *= 0.55

    elif letter_code == 'c' or letter_code == 'r':
        price *= 0.6

    elif letter_code == 'd' or letter_code == 's':
        price *= 0.65

    elif letter_code == 'e' or letter_code =='t':
        price *= 0.70

    elif letter_code == 'f' or letter_code == 'u':
        price *= 0.75

    elif letter_code == 'g' or letter_code == 'v':
        price *= 0.8

    elif letter_code == 'h':
        price *= .85

    elif letter_code =='n' or letter_code == 'none' or letter_code == 0 or letter_code == 'no':
        price += 0
    else:
        print("Please enter a valid price code: ")
        price_float = price_code(p_code_str, price)
        return price_float

    print(f"Net cost: ${price:.2f}")
    return price

#def net_convert(float_code, blank_cost)


#hard goods function all put together. takes input from the menu function
def hard_fun(check):
    if check != "y":
        exit_check()
    elif check == "y":
        #string for literals. i'm trying to consolitdate them down
        b_cost_str = "Blank Cost: $"
        valid_num_str = "Please enter a valid number."
        to_print_str = "Total Printing Cost: $"
        set_str = "Setup Cost: $"
        net_str = "Net Cost: $"
        set_piece_str = "Setup per piece: $"
        to_set_str = "Total Setup Cost: $"
        prof_mar_str = "Profit Margin: "
        #yes no questions
        save_str = "Would you like to save this quote? y/n  "
        yes_str = "y"
        no_str = "n"
        price_check_str = "Would you like to price an item? y/n  "
        men_check_str = "Return to menu? y/n "
        set_check_str = "Are there set up costs? y/n  "
        more_set_str = "Is there another setup? y/n  "
        run_check_str = "Run charge? y/n "
        # string inputs
        val_code_str = "Please enter a valid price code. "
        val_op_str = "Please enter a valid option. "
        p_code_str = "Price Code:  "
        sa_as_str = "Save as:  "
        #integer input
        quant_str = "Quantity:  "
        val_int_str = "Please enter a valid whole number."

        #basic job input
        customer = input("Customer: ")
        job_name = input("Job Name: ")
        item_number = input("Item Number: ")
        color = input("Color: ")
        #gets and validates quantity
        quantity = quantity_check(check)
        #takes blank cost and multiplies by price code
        blank_cost = blank(check)
        net_cost = price_code(p_code_str, blank_cost)
        #get the rest of the costs and multiply by price codes
        total_setup_cost = hard_setup(quantity, set_check_str, more_set_str, p_code_str)
        net_print_cost = net_print(run_check_str, p_code_str)
        total_hard_cost = hard_add_cost(net_cost, total_setup_cost, net_print_cost)
        #margin works the same as with screen printing
        margin_output = float_validate(prof_mar_str)
        final_margin = margin_invert(margin_output)
        #calculates price
        price = price_margin(total_hard_cost, final_margin)
        print(f"Price: ${price:.2f}")

        #save check that takes what is saved to the document as arguments
        hard_save_check(customer, job_name, color, price, item_number, quantity)
        check = simple_y_n(men_check_str)
        if check == "n":
            exit_check()
        elif check == "y":
            menu()

#basic about section
def about():
    print("Welcome to the pricing calculator.")
    print("Type 'y' or 'n' when prompted.")
    print("The program is kind of dumb, so you have to enter those exactly")
    print("It shouldn't throw any errors, but if it gets stuck in a loop,")
    print("then you should close the program and try again")
    input("Press any key to continue...")
    menu_check_str = "Return to menu? y/n "
    menu_check = simple_y_n(menu_check_str)
    if menu_check == "y":
        menu()
    elif menu_check == "n":
        exit_check()

#basic exit/menu check
def exit_check():
    want_to_exit = "Would you like to exit? y/n "
    check = simple_y_n(want_to_exit)
    if check == "y":
        quit()
    elif check == "n":
        menu_check_str = "Return to menu? y/n "
        menu_check = simple_y_n(menu_check_str)
        if menu_check == "n":
            exit_check()
        elif menu_check == "y":
            menu()

#save function for screen printing. need to consolidate with the hard goods one
def save_check(customer, job_name, color, price, two_xl_price, three_xl_price, item_number, quantity):
    want_to_save = "Would you like to save this quote? y/n "
    want_save_check = simple_y_n(want_to_save)
    if want_save_check == "n":
        want_to_menu = "Would you like to return to the menu? y/n "
        want_menu_check = simple_y_n(want_to_menu)
        if want_menu_check == "n":
            exit_check()
        elif want_menu_check == "y":
            menu()
    elif want_save_check == "y":
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
f"""Price SM-XL: ${price:.2f}
""")
        if float(two_xl_price) > 0:
            f.write(
f"""Price 2XL: ${two_xl_price:.2f}
""")
        else:
            pass

        if float(three_xl_price) > 0:
            f.write(
f"""Price 3XL: ${three_xl_price:.2f}
""")
        else:
            pass

        f.write(
"""
""")
        f.close()

#same as the screen printing one, just less arguments
#i made this one myself. i'll probably add an actual one
def hard_save_check(customer, job_name, color, price, item_number, quantity):
    want_to_save = "Would you like to save this quote? y/n "
    check = simple_y_n(want_to_save)
    if check == "n":
        exit_check()
    elif check == "y":
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
f"""Price: ${price:.2f}
""")


        f.write(
"""
""")
        f.close()


#menu function that acts as the main loop
#gets options based on letter. i'm going to add keybindings
def menu():
    print("Main Menu: ")
    print("Screen Printing")
    print("Hard Goods")
    print("Embroidery")
    print("Exit")
    print("About")
    print("Type 's' for screen printing, 'h' for hard goods, and 'e for embroidery'")
    print("Type 'exit' to exit and 'a' to learn about the program")
    menu_input = input("Choose an option: ")
    if menu_input == "s":
        menu_input = 'y'
        calc_fun(menu_input)
    elif menu_input == "exit":
        exit_check()
    elif menu_input == "e":
        embroidery_fun()
    elif menu_input == "a":
        about()
    elif menu_input == "h":
        menu_input = "y"
        hard_fun(menu_input)
    else:
        menu_input = input("Please enter a valid option: ")
        menu()
    return

#runs the whole thing. i did this before i messed with tkinter or infinite loops in general
#i just rememberd that games had a main loop so i tried it and it worked
#sorta proud of that one
menu()
