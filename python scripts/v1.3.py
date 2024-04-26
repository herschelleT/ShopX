# import mysql.connector
import mariadb
from tabulate import tabulate

# Buy - Functions
def phone():
    try:
        mycon = mariadb.connect(
            user="root",
            password="123",
            host="127.0.0.1",
            database="shop"
        )
        query="SELECT ID,Brand,Model,RAM,Storage,Screen_Size,Camera,Battery,Storage,Price FROM phones where Price<{} and Type='{}'".format(
        budget,type)
        mycursor.execute(query)
        myresult = mycursor.fetchall()

        if mycursor.rowcount==0:
            print("No such devices found.")
        else:
            print(tabulate(myresult, headers=['ID','Brand','Model','RAM','Storage','Screen Size','Camera','Battery','Storage','Price'], tablefmt='fancy_grid'))
            add_to_cart('phones', budget, type)
            mycursor = mycon.cursor()

    except mariadb.Error as e:
        print(e)

    # mycon = mysql.connector.connect(host="localhost",user="root",password="qwerty",database="cs_project")
    # mycursor = mycon.cursor()
    



def tablet():
    # mycon = mysql.connector.connect(host="localhost",user="root",password="qwerty",database="cs_project")
    # mycursor = mycon.cursor()
    try:
        mycon = mariadb.connect(
            user="root",
            password="123",
            host="127.0.0.1",
            database="shop"
        )
        mycursor = mycon.cursor()

    except mariadb.Error as e:
        print(e)

    
    query="SELECT ID,Brand,Model,Processor,RAM,Storage,Screen_Size,Battery,Price FROM tablets where Price<{} and Type='{}' and Screen_Size='{}'".format(
        budget,type,screen_size)
    mycursor.execute(query)
    myresult = mycursor.fetchall()

    if mycursor.rowcount==0:
        print("No such devices found.")
    else:
        print(tabulate(myresult, headers=['ID', 'Brand','Model','Processor','RAM','Storage','Screen Size','Battery','Price'], tablefmt='fancy_grid'))
        add_to_cart('tablets', budget, type)

    
def laptop():
    try:
        mycon = mariadb.connect(
            user="root",
            password="123",
            host="127.0.0.1",
            database="shop"
        )
        mycursor = mycon.cursor()
        query="SELECT ID,Brand,Model,Processor,Processor_Type,RAM,Storage,GPU,Price FROM laptops where Price<{} and Type='{}'".format(
        budget,type)
        mycursor.execute(query)
        myresult = mycursor.fetchall()

        if mycursor.rowcount==0:
            print("No such devices found.")
        else:
            print(tabulate(myresult, headers=['ID','Brand','Model','Processor','Processor Type','RAM','Storage','GPU','Price'], tablefmt='fancy_grid'))
            add_to_cart('laptops', budget, type)

    except mariadb.Error as e:
        print(e)
    # mycon = mysql.connector.connect(host="localhost",user="root",password="qwerty",database="cs_project")

    # mycursor = mycon.cursor()



def smart_watch():
    try:
        mycon = mariadb.connect(
            user="root",
            password="123",
            host="127.0.0.1",
            database="shop"
        )
        mycursor = mycon.cursor()
        query="SELECT ID,Brand,Model,Battery,Battery_Life,Display,Bluetooth,Fitness_Tracker,Price FROM smart_watches where Price<{} and Type='{}'".format(budget,type)
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        if mycursor.rowcount==0:
            print("No such devices found.")
        else:
            print(tabulate(myresult, headers=['ID', 'Brand','Model','Battery','Battery Life','Display','Bluetooth','Fitness Tracker','Price'], tablefmt='fancy_grid'))
            add_to_cart('smart_watches', budget, type)

    except mariadb.Error as e:
        print(e)
    # mycon = mysql.connector.connect(host="localhost",user="root",password="qwerty",database="cs_project")

    # mycursor = mycon.cursor()



def add_to_cart(device, budget, column):
    global cart
    flag=0
    while flag ==0 :
        # mycon = mysql.connector.connect(host="localhost",user="root",password="qwerty",database="cs_project")
        # mycursor=mycon.cursor()

        try:
            mycon = mariadb.connect(
                user="root",
                password="123",
                host="127.0.0.1",
                database="shop"
            )
            mycursor = mycon.cursor()
            query="SELECT ID, Brand, Model, Price FROM {} WHERE Price<{} and Type='{}'".format(device,budget,column)
            mycursor.execute(query)
            choice = input("Enter the ID of the device to be added in cart (enter 0 if you want nothing from displayed items): ").strip().upper()
            if choice == '0':
                print("Continue shopping other items")
                flag=1
            else:
                for x in mycursor:
                    if choice == x[0]:
                        cart.append(x[1:])
                        flag=1
                        # mycon = mysql.connector.connect(host="localhost",user="root",password="qwerty",database="cs_project")
                        # mycursor=mycon.cursor()
                        mycursor.execute("UPDATE {} SET Stock=Stock-1 WHERE ID='{}'".format(device,choice))
                        mycon.commit()
                        mycon.close()
                        break
                else:
                    print("Please enter a valid ID")
        except mariadb.Error as e:
            print(e)




#-------------------------------------------------------------------------------------------------------------------------------------
# Sell - Functions
def model(device):
    try:
        mycon = mariadb.connect(
            user="root",
            password="123",
            host="127.0.0.1",
            database="shop"
        )
        mycursor = mycon.cursor()
        query="SELECT ID, Brand, Model, Price FROM {}".format(device)
        mycursor.execute(query)
        myresult=mycursor.fetchall()

        model=''
        for x in range(len(myresult)):
            model += str(x+1)+' -> '+myresult[x][1]+' '+myresult[x][2]+'\n'

        s_no = int(input("Enter the model of the phone :\n"+model+str(1+len(myresult))+" -> not here\n"))
        while True:
            if 1 <= s_no <= len(myresult):
                id = myresult[s_no-1][0]
                return s_no,1+len(myresult),id
            elif s_no == 1+len(myresult):
                return s_no,1+len(myresult),None
            else:
                print("Enter a valid Model")

    except mariadb.Error as e:
        print(e)
    
    


def add_one(device,id):
    try:
        mycon = mariadb.connect(
            user="root",
            password="123",
            host="127.0.0.1",
            database="shop"
        )
        # mycursor = mycon.cursor()
        # mycon = mysql.connector.connect(host="localhost",user="root",password="qwerty",database="cs_project")
        mycursor = mycon.cursor()
        mycursor.execute("SELECT Brand, Model, Price FROM {} WHERE ID='{}'".format(device,id))
        myresult = mycursor.fetchall()
        mycursor.execute("UPDATE {} SET Stock=Stock+1 WHERE ID='{}'".format(device,id))
        mycon.commit()
        mycon.close()

    except mariadb.Error as e:
        print(e)



def sell_phones():
    price=float(input('Please enter the price at which your phone was bought: '))
    age=int(input('Please enter how old the device is [Yrs]: '))
    buy_price=price-(age*1000)
    sell_price=buy_price+2000
    
    print('Please enter the following specifications :')
    Brand=input('Brand :')
    Model=input('Model :')
    RAM=input('RAM :')
    Storage=input('Storage :')
    Screen_Size=input('Screen size (Small/Medium/Large) :').capitalize()
    Camera=input('Camera quality (Good/Excellent) :').capitalize()
    Battery_Life=input('Battery Life (Good/Excellent) :').capitalize()
    Battery=input('Battery Capacity :')
    Type=input('Type (Gaming/General) :').capitalize()

    try:
        mycon = mariadb.connect(
            user="root",
            password="123",
            host="127.0.0.1",
            database="shop"
        )
        mycursor = mycon.cursor()
        # mycon = mysql.connector.connect(host ='localhost',user = 'root',password = 'qwerty',
        #                                 database = 'cs_project')
        # mycursor = mycon.cursor()
        mycursor.execute("SELECT * FROM phones")
        count=len(mycursor.fetchall())
        ID='P'+str(count+1)

        q = "INSERT INTO phones VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}',{},'{}',1)".format(
            ID,Brand,Model,RAM,Storage,Screen_Size,Camera,Battery_Life,Battery,sell_price,Type)
        mycursor.execute(q)
        mycon.commit()
        mycon.close()

        return [Brand,Model,buy_price]

    except mariadb.Error as e:
        print(e)



def sell_laptops():
    price=float(input('Please enter the price at which your laptop was bought: '))
    age=int(input('Please enter how old the device is [Yrs]: '))

    buy_price=price-(age*1000)
    sell_price=buy_price+2000

    print('Please enter the following specifications :')
    Brand=input('Brand :')
    Model=input('Model :')
    Processor=input('Processor :')
    Processor_type = input('Processor type (Light/Moderate/Performance) :')
    RAM = input("RAM :")
    Storage=input('Storage :')
    GPU = input('GPU :')
    Type = input('Type (Gaming/Light/Power) :')

    try:
        mycon = mariadb.connect(
            user="root",
            password="123",
            host="127.0.0.1",
            database="shop"
        )
        mycursor = mycon.cursor()
        # mycon = mysql.connector.connect(host ='localhost',user = 'root',password = 'qwerty',
        #                             database = 'cs_project')
        # mycursor = mycon.cursor()
        mycursor.execute("SELECT * FROM laptops")
        count=len(mycursor.fetchall())
        ID='L'+str(count+1)

        q = "INSERT INTO laptops VALUES ('{}','{}','{}','{}','{}','{}','{}','{}',1,'{}','{}')".format(
            ID,Brand,Model,Processor,Processor_type,RAM,Storage,GPU,sell_price,Type)
        mycursor.execute(q)
        mycon.commit()
        mycon.close()

        return [Brand,Model,buy_price]

    except mariadb.Error as e:
        print(e)


def sell_tablets():
    price=float(input('Please enter the price at which your tablet was bought: '))
    age=int(input('Please enter how old the device is [Yrs]: '))

    buy_price=price-(age*1000)
    sell_price=buy_price+2000

    print('Please enter the following specifications :')
    Brand=input('Brand :')
    Model=input('Model :')
    Processor=input('Processor :')
    RAM = input("RAM :")
    Storage=input('Storage :')
    Screen_Size = input('Screen Size :')
    Battery=input('Battery Capacity :')
    Type = input('Type (Gaming/Light/Power) :')

    try:
        mycon = mariadb.connect(
            user="root",
            password="123",
            host="127.0.0.1",
            database="shop"
        )
        mycursor = mycon.cursor()
        # mycon = mysql.connector.connect(host ='localhost',user = 'root',password = 'qwerty',
        #                             database = 'cs_project')
        # mycursor = mycon.cursor()
        mycursor.execute("SELECT * FROM tablets")
        count=len(mycursor.fetchall())
        ID='T'+str(count+1)

        q = "INSERT INTO tablets VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}',1)".format(
            ID,Brand,Model,Processor,RAM,Storage,Screen_Size,Battery,sell_price,Type)
        mycursor.execute(q)
        mycon.commit()
        mycon.close()

        return [Brand,Model,buy_price]

    except mariadb.Error as e:
        print(e)

    

def sell_smart_watches():
    price=float(input('Please enter the price at which your smartwatch was bought: '))
    age=int(input('Please enter how old the device is [Yrs]: '))

    buy_price=price-(age*1000)
    sell_price=buy_price+2000

    print('Please enter the following specifications :')
    Brand=input('Brand :')
    Model=input('Model :')
    Battery=input('Battery Capacity :')
    Battery_Life=input('Battery Life :')
    Display=input('Display category (AMOLED/LED/LCD/OLED/OLED retina) :')
    Bluetooth= input('Bluetooth (Yes/No) :').capitalize()
    Fitness_Tracker=input('Fitness Tracker (Yes/No) :').capitalize()
    Type = input('Type (General/Fitness/Hybrid) :')

    try:
        mycon = mariadb.connect(
            user="root",
            password="123",
            host="127.0.0.1",
            database="shop"
        )
        # mycursor = mycon.cursor()
        # mycon = mysql.connector.connect(host ='localhost',user = 'root',password = 'qwerty',
        #                             database = 'cs_project')
        mycursor = mycon.cursor()
        mycursor.execute("SELECT * FROM smart_watches")
        count=len(mycursor.fetchall())
        ID='S'+str(count+1)

        q = "INSERT INTO smart_watches VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}',1)".format(
            ID,Brand,Model,Battery,Battery_Life,Display,Bluetooth,Fitness_Tracker,sell_price,Type)
        mycursor.execute(q)
        mycon.commit()
        mycon.close()

        return [Brand,Model,buy_price]

    except mariadb.Error as e:
        print(e)


def receipt(receipt_details):
    print("--------------------RECEIPT--------------------")
    print(tabulate([receipt_details], headers=['Brand','Model','Price'], tablefmt='fancy_grid'))
    print("-----------------------------------------------")



#-------------------------------------------------------------------------------------------------------------------------------------
# Main
print("--------------- HELLO! WELCOME TO XYZ ELECTRONICS. ---------------")
while True:
    choice = int(input('''What would you like to do today ?
(1) Buy
(2) Sell
(3) Exit
'''))
#------------------------------------------------------------------------------------------------------------------------------------
    cart = []
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
                type=input('''Enter the type of smartphone you want :
a)Gaming
b)General
''').lower()
                if type=='a':
                    type="Gaming"
                    phone()
                elif type=='b':
                    type="General"
                    phone()
                else:
                    print("Invalid choice.")

            elif device=='b':
                budget = int(input("Enter your budget for this device: "))
                type = input('''What kind of user are you :
a)Power
b)Light
''').lower()
                if type=='a':
                    type="Power"
                elif type=='b':
                    type="Light"
                else:
                    print('Invalid choice.')
                screen_size = input('''What is your preferred screen size:
a)6 inches
b)8 inches
c)10 inches
''').lower()
                if screen_size=='a':
                    screen_size="6 inch"
                    tablet()
                elif screen_size=='b':
                    screen_size="8 inch"
                    tablet()
                elif screen_size=='c':
                    screen_size="10 inch"
                    tablet()
                else:
                    print('Invalid choice.')
                
            elif device=='c':
                budget = int(input("Enter your budget for this device: "))
                type = input('''What will you be using it for?
(a) Gaming
(b) Office work
(c) Personal use
''').lower()
                if type=='a':
                    type="Gaming"
                    laptop()
                elif type=='b':
                    type="Power"
                    laptop()
                elif type=='c':
                    type="Light"
                    laptop()
                else:
                    print('Invalid choice.')


            elif device=='d':
                budget = int(input("Enter your budget for this device: "))
                type = input('''What will you be using it for ?
a) General
b) Fitness-oriented
c) Hybrid
''').lower()
                if type=='a':
                    type="General"
                    smart_watch()
                elif type=='b':
                    type="Fitness"
                    smart_watch()
                elif type=='c':
                    type="Hybrid"
                    smart_watch()
                else:
                    print('Invalid choice.')

            elif device=='e':
                if cart == []:
                    print("Nothing to see here.")
                else:
                    show_cart = [(i+1,)+cart[i] for i in range(len(cart))]   #[(1,'samsung','s10',53000),(2,---),(3,---)]

                    total_price = 0
                    for i in range(len(show_cart)):
                        total_price += int(show_cart[i][3])
                    show_cart = show_cart + [('Total Price : ', '', '', total_price)]
                    
                    print("----- YOUR CART -----")
                    print(tabulate(show_cart, headers=['S.no.','Brand','Model','Price'], tablefmt='fancy_grid'))

            else:
                print("Invalid choice.")
    
            cont = input("Do you want to continue?( Y->More Shopping! / N->Proceed to check out): ").strip().upper()
                    
        else:
            if cart == []:
                print("Empty Cart!\nThank you for your time.")
            else:
                cart = [(i+1,)+cart[i] for i in range(len(cart))]

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
d) Smartwatch
''')
        if device == 'a':
            s_no,not_here,id = model('phones')
            if s_no != not_here:
                add_one('phones',id)
            else:
                receipt_details = sell_phones()
                receipt(receipt_details)

        elif device == 'b':
            s_no, not_here ,id = model('tablets')
            if s_no != not_here:
                add_one('tablets',id)
            else:
                receipt_details = sell_tablets()
                receipt(receipt_details)  

        elif device == 'c':
            s_no, not_here, id = model('laptops')
            if s_no != not_here:
                add_one('laptops',id)
            else:
                receipt_details = sell_laptops()
                receipt(receipt_details)

        elif device == 'd':
            s_no ,not_here, id = model('smart_watches')
            if s_no != not_here:
                add_one('smart_watches',id)
            else:
                receipt_details = sell_smart_watches()
                receipt(receipt_details)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
    elif choice == 3:
        print('Thank you!')
        break

    else:
        print("Invalid choice.")
                 

    

