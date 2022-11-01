# quote_calculator
A quote calculator for a promo company 
Screenprinting refers to shirts, hoodies, pants, etc. that are screenprinted
Hard goods are things like cups, glasses, sunglasses, and various trinkets. 

This started as a simple command line program. After I finished writing that, I wanted to consolidate everything
down with functions. Then I added input validation methods so that the program could function if someone made a mistake 
but also to ensure that things are input properly. I also made a function for hard goods as well as one for exiting, saving,
and a main menu that acts as a main loop.

My next step is making a tkinter gui, which is requiring me to learn classes, although I think the way I did things is similar to classes?

The basics are:
Blank cost is the cost of the thing being printed
Printing costs are based on quantity and the number of colors
Locations refer to a front print, back print, sleeve print, etc
Setup costs are based on the number of colors in a print 
Private label is when the tag is ripped out and a new one is printed
Finishing is folding, bagging, and putting tags on the bag

So total cost is blank cost + printing costs + setup costs + private label cost + finishing cost
After that a profit margin is applied to it to get the sell cost. This program accepts both integers and floats for this.
For example: 25 and 0.25 with both be valid

Two and three xl are not always in orders and they cost more generally, so they have their own functions 
If they don't exist then they are skipped 

If the user chooses to save then the output is appended onto a file. I haven't added any sort of validation to that yet
so it will abort when not given a valid file name. 

Hard goods have more or less the same process, except their are wholesale discount codes that have to be used to know the true price of things
and there aren't different sizes that cost different amounts.

When a quote is printed, it prints:
Customer
Job Name
Item Number
Color 
Quantity 
Price 

