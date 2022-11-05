import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror


#gets two xl cost
class Window(tk.Toplevel):
    def __init__(self, container):
        tk.Toplevel.__init__(self, container)

        self.title('Toplevel Window')
        self.__create_widgets()

        for child in self.winfo_children():
            child.grid_configure(padx=10, pady=10)

    def __create_widgets(self):
        self.two_x_label = ttk.Label(self, text="2XL Cost")
        self.two_x_label.grid(column=0, row=0)
        self.two_x_entry = ttk.Entry(self, width=20)
        self.two_x_entry.grid(column=0, row=1)


#get 3xl cost
class WindowFrame(tk.Toplevel):
    def __init__(self, container):
        tk.Toplevel.__init__(self, container)


        self.title('Toplevel Window')
        self.__create_widgets()
        for child in self.winfo_children():
            child.grid_configure(padx=10, pady=10)

    def __create_widgets(self):
        self.three_x_label = ttk.Label(self, text="3XL Cost")
        self.three_x_label.grid(column=0, row=0)
        self.three_x_entry = ttk.Entry(self, width=20)
        self.three_x_entry.grid(column=0, row=1)

#controls changing frames
class ControlFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.title('ControlFrame')
        self.geometry('400x150')
        self.grid()

        self.__create_widgets()

    def __create_widgets(self):
        QuoteFrame.grid()
        ResultFrame.grid()
        switch_window_button = tk.Button(
            self,
            text="Go to the Side Page",
            command=lambda: controller.show_frame(SidePage),
        )
        switch_window_button.grid(column=0, row=4)


#gets basic job information
class QuoteFrame(ttk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.grid()
        self.__create_widgets(controller)

    def __create_widgets(self, controller):
        self.customer_label = ttk.Label(self, text="Customer:")
        self.customer_label.grid(column=0, row=0)
        self.customer_entry = ttk.Entry(self, width=20)
        self.customer_entry.grid(column=1, row=0)
        self.customer_entry.focus()

        self.job_label = ttk.Label(self, text="Job Name:")
        self.job_label.grid(column=0, row=1)
        self.job_entry = ttk.Entry(self, width=20)
        self.job_entry.grid(column=1, row=1)

        self.item_label = ttk.Label(self, text="Item Number:")
        self.item_label.grid(column=0, row=2)
        self.item_entry = ttk.Entry(self, width=20)
        self.item_entry.grid(column=1, row=2)

        self.color_label = ttk.Label(self, text="Item Color:")
        self.color_label.grid(column=2, row=0)
        self.color_entry = ttk.Entry(self, width=20)
        self.color_entry.grid(column=3, row=0)

        self.blank_label = ttk.Label(self, text="Blank Cost:")
        self.blank_label.grid(column=2, row=1)
        self.blank_entry = ttk.Entry(self, width=20)
        self.blank_entry.grid(column=3, row=1)

        self.quantity_label = ttk.Label(self, text="Quantity:")
        self.quantity_label.grid(column=2, row=2)
        quantity = self.quantity_entry = ttk.Entry(self, width=20)
        self.quantity_entry.grid(column=3, row=2)

        self.two_x_button = ttk.Button(self, text='2XL Cost')
        self.two_x_button['command']= self.open_two_x
        self.two_x_button.grid(column=1, row=3)

        self.three_x_button = ttk.Button(self, text='3XL Cost')
        self.three_x_button['command']= self.open_three_x
        self.three_x_button.grid(column=2, row=3)

        #button to change windows
        switch_window_button = tk.Button(
            self,
            text="Generate Quote",
            command=lambda: controller.show_frame(ResultFrame, quantity),
        )
        switch_window_button.grid(column=3, row=3)
        return quantity
    #opens toplevel window to get 2xl cost
    def open_two_x(self):
        window_two = Window(self)
        window_two.grab_set()

    #opens toplevel window to get 3xl cost
    def open_three_x(self):
        window_three = WindowFrame(self)
        window_three.grab_set()



#gets more price information
class ResultFrame(tk.Frame):
    def __init__(self, parent, controller, quantity):

        tk.Frame.__init__(self, parent, quantity)

        # setup the grid layout manager

        self.switch_window_button = tk.Button(self, text='Change', command=lambda: controller.show_frame(CompletionScreen))
        self.switch_window_button.grid(column=1, row=1)
        self.__create_widgets()


    def __create_widgets(self):

        self.setup_label = ttk.Label(self, text="Setup Charges:")
        self.setup_label.grid(column=0, row=0)
        self.setup_entry = ttk.Entry(self, width=20)
        self.setup_entry.grid(column=1, row=0)
        self.setup_entry.focus()


        self.set_cost_label = ttk.Label(self, text="Number of Setups:")

        self.set_cost_label.grid(column=0, row=1)
        self.set_cost_entry = ttk.Entry(self, width=20)
        self.set_cost_entry.grid(column=1, row=1)

        self.quantity = OrderFrame.quantity_entry
        self.set_piece = (self.setup_entry * self.set_cost_entry) / self.quantity




#shows the customer facing quote
class CompletionScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        switch_window_button = ttk.Button(
            self, text="Return to menu", command=lambda: controller.show_frame(QuoteFrame)
        )
        switch_window_button.grid(column=0, row=0)

#defines frames
class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title('Quote Calculator')
        container = tk.Frame(self, height=400, width=600)
        container.grid(column=0, row=0)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        #for statment to change frames
        self.frames = {}

        for F in (QuoteFrame, ResultFrame, CompletionScreen):
            frame = F(container, self, quantity)

            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

            #gives children the same padding
            for child in frame.winfo_children():
                child.grid_configure(padx=10, pady=10)

        self.show_frame(QuoteFrame)
        #function that changes frames
    def show_frame(self, cont):
        frame=self.frames[cont]

        frame.tkraise()

        # layout on the root window


#main loop initialising
if __name__ == "__main__":
    app = App()
    app.mainloop()
