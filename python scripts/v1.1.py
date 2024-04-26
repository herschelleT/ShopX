import mysql.connector
from tabulate import tabulate

def phone():
    mycon = mysql.connector.connect(host="localhost",user="root",password="qwerty",database="cs_project")
    mycursor = mycon.cursor()
    
    query="SELECT ID,Brand,Model,RAM,Storage,Screen_Size,Camera,Battery,Storage,Price FROM phones where Price<{} and Type='{}'".format(budget,type1)
    mycursor.execute(query)
    myresult = mycursor.fetchall()

    if mycursor.rowcount==0:
        print("No such devices found.")
    else:
        print(tabulate(myresult, headers=['ID','Brand','Model','RAM','Storage','Screen Size','Camera','Battery','Storage','Price'], tablefmt='fancy_grid'))
        add_to_cart('phones', budget, type1)


def tablet():
    mycon = mysql.connector.connect(host="localhost",user="root",password="qwerty",database="cs_project")
    mycursor = mycon.cursor()
    
    query="SELECT ID,Brand,Model,Processor,RAM,Storage,Screen_Size,Battery,Price FROM tablets where Price<{} and Type='{}' and Screen_Size='{}'".format(budget,type,screen_size)
    mycursor.execute(query)
    myresult = mycursor.fetchall()

    if mycursor.rowcount==0:
        print("No such devices found.")
    else:
        print(tabulate(myresult, headers=['ID', 'Brand','Model','Processor','RAM','Storage','Screen Size','Battery','Price'], tablefmt='fancy_grid'))
        add_to_cart('tablets', budget, type)

    
def laptop():
    mycon = mysql.connector.connect(host="localhost",user="root",password="qwerty",database="cs_project")

    mycursor = mycon.cursor()
    query="SELECT ID,Brand,Model,Processor,Processor_Type,RAM,Storage,GPU,Price FROM laptops where Price<{} and Type='{}'".format(budget,type)
    mycursor.execute(query)
    myresult = mycursor.fetchall()

    if mycursor.rowcount==0:
        print("No such devices found.")
    else:
        print(tabulate(myresult, headers=['ID','Brand','Model','Processor','Processor Type','RAM','Storage','GPU','Price'], tablefmt='fancy_grid'))
        add_to_cart('laptops', budget, type)


def smart_watch():
    mycon = mysql.connector.connect(host="localhost",user="root",password="qwerty",database="cs_project")

    mycursor = mycon.cursor()
    query="SELECT ID,Brand,Model,Battery,Battery_Life,Display,Bluetooth,Fitness_Tracker,Price FROM smart_watches where Price<{} and Type='{}'".format(budget,type)
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    if mycursor.rowcount==0:
        print("No such devices found.")
    else:
        print(tabulate(myresult, headers=['ID', 'Brand','Model','Battery','Battery Life','Display','Bluetooth','Fitness Tracker','Price'], tablefmt='fancy_grid'))
        add_to_cart('smart_watches', budget, type)


def add_to_cart(device, budget, column):
    global cart
    flag=0
    while flag ==0 :
        mycon = mysql.connector.connect(host="localhost",user="root",password="qwerty",database="cs_project")
        mycursor=mycon.cursor()
        query="SELECT ID, Brand, Model, Price FROM {} WHERE Price<{} and Type='{}'".format(device,budget,column)
        mycursor.execute(query)
        choice = input("Enter the ID of the device to be added in cart (enter 0 if you want nothing from displayed items): ").strip().upper()
        mycon.close()
        if choice == '0':
            print("Continue shopping other items")
            flag=1
        else:
            
            for x in mycursor:
                if choice == x[0]:
                    cart.append(x[1:])
                    flag=1

                    mycon = mysql.connector.connect(host="localhost",user="root",password="qwerty",database="cs_project")
                    mycursor=mycon.cursor()
                    mycursor.execute("UPDATE {} SET Stock=Stock-1 WHERE ID='{}'".format(device,choice))
                    mycon.commit()
                    mycon.close()

                    break
            else:
                print("Please enter a valid ID")

# Sell - Functions
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
def model(device):
    mycon = mysql.connector.connect(host="localhost",user="root",password="qwerty",database="cs_project")
    mycursor = mycon.cursor()
    
    query="SELECT ID, Brand, Model, Price FROM {}".format(device)
    mycursor.execute(query)
    myresult=mycursor.fetchall()

    model=''
    for x in range(len(myresult)):
        model += str(x+1)+' -> '+myresult[x][0]+' '+myresult[x][1]+'\n'


    while True:
        s_no = int(input("Enter the model of the phone :\n"+model+str(1+len(myresult))+" -> not here\n"))
        if 1 <= s_no <= 1+len(myresult):
            id = myresult[s_no-1][0]
            break
        else:
            print("Enter a valid Model")

    return s_no,1+len(myresult),id

def add_one(device,id):
    mycon = mysql.connector.connect(host="localhost",user="root",password="qwerty",database="cs_project")
    mycursor = mycon.cursor()
    mycursor.execute("SELECT Brand, Model, Price FROM {} WHERE ID='{}'".format(device,id))
    myresult = mycursor.fetchall()
    print("--------------------RECEIPT--------------------")
    print(tabulate(myresult, headers=['Brand','Model', 'Price'], tablefmt='fancy_grid'))
    mycursor.execute("UPDATE {} SET Stock=Stock+1 WHERE ID='{}'".format(device,id))
    mycon.commit()
    mycon.close()


# Main

print("--------------- HELLO! WELCOME TO XYZ ELECTRONICS ---------------")
while True:
    choice = int(input('''What would you like to do today ?
(1) Buy
(2) Sell
(3) Exit
'''))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
    cart=[]
    if choice == 1:
        cont='Y'
        while cont == 'Y':
            device = input('''Which device are you looking for?
a) Phone
b) Tablet
c) Laptop
d) Smartwatch
e) Show cart
''')

            

            if device=='a':
                budget = int(input("Enter your budget for this device: "))
                type = input('''Which type of phone are you looking for?
a) Smartphone
b) Feature phone
''')
                if type=='a':
                    type1=input('''Enter the type of smartphone you want :
a)Gaming
b)General
''')
                    if type1=='a':
                        type1="Gaming"
                        phone()
                    elif type1=='b':
                        type1="General"
                        phone()
                elif type=='b':
                    type1="Feature"

            elif device=='b':
                budget = int(input("Enter your budget for this device: "))
                type = input('''What kind of user are you :
a)Power
b)Light
''')
                if type=='a':
                    type="Power"
                elif type=='b':
                    type="Light"
                screen_size = input('''What is your preferred screen size:
a)6 inches
b)8 inches
c)10 inches
''')
                if screen_size=='a':
                    screen_size="6 inch"
                elif screen_size=='b':
                    screen_size="8 inch"
                elif screen_size=='c':
                    screen_size="10 inch"
                tablet()
                
            elif device=='c':
                budget = int(input("Enter your budget for this device: "))
                type = input('''What will you be using it for?
(a) Gaming
(b) Office work
(c) Personal use
''')
                if type=='a':
                    type="Gaming"
                elif type=='b':
                    type="Power"
                elif type=='c':
                    type="Light"
                laptop()

            elif device=='d':
                budget = int(input("Enter your budget for this device: "))
                type = input('''What will you be using it for ?
a) General
b) Fitness-oriented
c) Hybrid
''')
                if type=='a':
                    type="General"
                elif type=='b':
                    type="Fitness"
                elif type=='c':
                    type="Hybrid"
                smart_watch()

            elif device=='e':
                if cart == []:
                    print("Nothing to see here.")
                else:
                    show_cart = [(i+1,)+cart[i] for i in range(len(cart))]
                    #[(1,'samsung','s10',53000),(2,---),(3,---)]

                    total_price = 0
                    for i in range(len(show_cart)):
                        total_price += int(show_cart[i][3])
                    show_cart = show_cart + [('Total Price : ', '', '', total_price)]
                    
                    print("----- YOUR CART -----")
                    print(tabulate(show_cart, headers=['S.no.','Brand','Model','Price'],
                                   tablefmt='fancy_grid'))

            cont = input("Do you want to continue?( Y->More Shopping! / N->Proceed to check out): ").strip().upper()
            
        else:
            if cart == []:
                print("Empty Cart!\nThank you for your time.")
            else:
                cart = [(i+1,)+cart[i] for i in range(len(cart))]   #[(1,'samsung','s10',53000),(2,---),(3,---)]

                total_price = 0
                for i in range(len(cart)):
                    total_price += int(cart[i][3])
                cart = cart + [('Total Price : ', '', '', total_price)]
                
                print("----- BILL -----")
                print(tabulate(cart, headers=['S.no.','Brand','Model','Price'], tablefmt='fancy_grid'))
#-----------------------------------------------------------------------------------------------------------------------------------------------------------               
    elif choice == 2:

        device = input('''What Device are you selling?
a) Phone
b) Tablet
c) Laptop
d) smart Watch
''')
        if device == 'a':
            s_no,not_here,id = model('phones')
            if s_no != not_here:
                add_one('phones',id)
            else:
                print("\n----- The asking info about device and adding to mysql table part -----\n")

        elif device == 'b':
            s_no, not_here ,id = model('tablets')
            if s_no != not_here:
                add_one('tablets',id)
            else:
                print("\n----- The asking info about device and adding to mysql table part -----\n")

        elif device == 'c':
            s_no, not_here, id = model('laptops')
            if s_no != not_here:
                add_one('laptops',id)
            else:
                print("\n----- The asking info about device and adding to mysql table part -----\n")

        elif device == 'd':
            s_no ,not_here, id = model('smart_watches')
            if s_no != not_here:
                add_one('smart_watches',id)
            else:
                print("\n----- The asking info about device and adding to mysql table part -----\n")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
    elif choice == 3:
        print('Thank you!')
        break

    else:
        print("Invalid choice.")
                 

    

