def phone():
    import mysql.connector
    from tabulate import tabulate

    mycon = mysql.connector.connect(host="localhost",user="root",password="qwerty",database="cs_project")
    mycursor = mycon.cursor()
    
    query="SELECT ID,Brand,Model,RAM,Storage,Screen_Size,Camera,Battery,Storage,Price FROM phones where Price<{} and Type='{}'".format(budget,type1)
    mycursor.execute(query)
    myresult = mycursor.fetchall()

    if mycursor.rowcount==0:
        print("No such devices found.")
    else:
        print(tabulate(myresult, headers=['ID','Brand','Model','RAM','Storage','Screen Size','Camera','Battery','Storage','Price'], tablefmt='fancy_grid'))

def tablet():
    import mysql.connector
    from tabulate import tabulate

    mycon = mysql.connector.connect(host="localhost",user="root",password="qwerty",database="cs_project")
    mycursor = mycon.cursor()
    
    query="SELECT ID,Brand,Model,Processor,RAM,Storage,Screen_Size,Battery,Price FROM tablets where Price<{} and Type='{}' and Screen_Size='{}'".format(budget,type,screen_size)
    mycursor.execute(query)
    myresult = mycursor.fetchall()

    if mycursor.rowcount==0:
        print("No such devices found.")
    else:
        print(tabulate(myresult, headers=['ID', 'Brand','Model','Processor','RAM','Storage','Screen Size','Battery','Price'], tablefmt='fancy_grid'))

    
def laptop():
    import mysql.connector
    from tabulate import tabulate

    mycon = mysql.connector.connect(host="localhost",user="root",password="qwerty",database="cs_project")

    mycursor = mycon.cursor()
    query="SELECT ID,Brand,Model,Processor,Processor_Type,RAM,Storage,GPU,Price FROM laptops where Price<{} and Type='{}'".format(budget,type)
    mycursor.execute(query)
    myresult = mycursor.fetchall()

    if mycursor.rowcount==0:
        print("No such devices found.")
    else:
        print(tabulate(myresult, headers=['ID','Brand','Model','Processor','Processor Type','RAM','Storage','GPU','Price'], tablefmt='fancy_grid'))


def smart_watch():
    import mysql.connector
    from tabulate import tabulate

    mycon = mysql.connector.connect(host="localhost",user="root",password="qwerty",database="cs_project")

    mycursor = mycon.cursor()
    query="SELECT ID,Brand,Model,Battery,Battery_Life,Display,Bluetooth,Fitness_Tracker,Price FROM smart_watches where Price<{} and Type='{}'".format(budget,type)
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    if mycursor.rowcount==0:
        print("No such devices found.")
    else:
        print(tabulate(myresult, headers=['ID', 'Brand','Model','Battery','Battery Life','Display','Bluetooth','Fitness Tracker','Price'], tablefmt='fancy_grid'))

while True:
    choice = int(input('''HELLO! WELCOME TO XYZ ELECTRONICS.
What would you like to do today ?
(1) Buy
(2) Sell
(3) Exit
'''))
    if choice == 1:
        device= input('''Which device are you looking for?
a) Phone
b) Tablet
c) Laptop
d) Smartwatch
''')

        budget = int(input("Enter your budget :"))

        if device=='a':
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
                if type1=='b':
                    type1="General"
                    phone()
            if type=='b':
                type1="Feature"

        if device=='b':
            type = input('''What kind of user are you :
a)Power
b)Light
''')
            if type=='a':
                type="Power"
            if type=='b':
                type=="Light"
            screen_size = input('''What is your preferred screen size:
a)6 inches
b)8 inches
c)10 inches
''')
            if screen_size=='a':
                screen_size=="6 inch"
            if screen_size=='b':
                screen_size=="8 inch"
            if screen_size=='c':
                screen_size=="10 inch"
            tablet()
                
        if device=='c':
            type = input('''What will you be using it for?
(a) Gaming
(b) Office work
(c) Personal use
''')
            if type=='a':
                type="Gaming"
                laptop()
            
            if type=='b':
                type=="Power"

            if type=='c':
                type=="Light"

        if device=='d':
            type = input('''What will you be using it for ?
a) General
b) Fitness-oriented
c) Hybrid
''')
            if type=='a':
                type="General"
                smart_watch()
            if type=='b':
                type="Fitness"
                smart_watch()
            if type=='c':
                type="Hybrid"
                smart_watch()
    elif choice == 2:
        print("Gotta work on this!!!")

    elif choice == 3:
        break

    else:
        print("Invalid choice")
                 

    

