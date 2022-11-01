from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

root = Tk()
root.title("Quote Calculator")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

blankframe = ttk.Frame(mainframe, padding="3 3 12 12")
blankframe.grid(column=0, row=0, sticky=(NE, NW))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

customer = StringVar()
customer_entry = ttk.Entry(blankframe, width=20, textvariable=customer)
customer_entry.grid(column=2, row=1, sticky=(W, E))

job_name = StringVar()
job_entry = ttk.Entry(blankframe, width=20, textvariable=job_name)
job_entry.grid(column=4, row=1, sticky=(W, E))

item_number = StringVar()
item_entry = ttk.Entry(blankframe, width=20, textvariable=item_number)
item_entry.grid(column=2, row=2, sticky=(W, E))

item_color = StringVar()
color = ttk.Entry(blankframe, width=20, textvariable=item_color)
color.grid(column=4, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Get Quote", command=calculate).grid(column=2, row=4, sticky=E)

ttk.Label(blankframe, text="Customer").grid(column=1, row=1, sticky=W)
ttk.Label(blankframe, text="Job Name").grid(column=3, row=1, sticky=E)
ttk.Label(blankframe, text="Item Number").grid(column=1, row=2, sticky=W)
ttk.Label(blankframe, text="Item Color").grid(column=3, row=2, sticky=E)

blankcostframe = ttk.Frame(mainframe, padding="3 3 12 12")
blankcostframe.grid(column=0, row=1, sticky=(W, E))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

blank_cost = StringVar()
blank_entry = ttk.Entry(blankcostframe, width=20, textvariable=blank_cost)
blank_entry.grid(column=2, row=1, sticky=(W, E))

quantity = StringVar()
quantity_entry = ttk.Entry(blankcostframe, width=20, textvariable=quantity)
quantity_entry.grid(column=4, row=1, sticky=(W, E))

ttk.Label(blankcostframe, text="Blank Cost").grid(column=1, row=1, sticky=W)
ttk.Label(blankcostframe, text="Quantity").grid(column=3, row=1, sticky=E)


oversizedframe = ttk.Frame(mainframe, padding="3 3 12 12")
oversizedframe.grid(column=0, row=2, sticky=(W, E))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

two_x_check = StringVar()
two_x_checkbox = ttk.Checkbutton(oversizedframe, text='2XLs?',
	    variable=two_x_check,
	    onvalue='yes', offvalue='no')
two_x_checkbox.grid(column=1, row=2, sticky=W)

three_x_check = StringVar()
three_x_checkbox = ttk.Checkbutton(oversizedframe, text='3XLs?',
	    variable=two_x_check,
	    onvalue='yes', offvalue='no')
three_x_checkbox.grid(column=3, row=2, sticky=E)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

for child in blankframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

for child in blankcostframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

customer_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()
