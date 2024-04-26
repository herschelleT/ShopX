import mysql.connector
from tabulate import tabulate
def sell_phone():
    price=float(input('Please enter the price at which your phone was bought: '))
    age=int(input('Please enter how old the device is [Yrs]: '))
    
    print('Please enter the following specifications :')
    Brand=input('Brand :')
    Model=input('Model :')
    RAM=input('RAM :')
    Storage=input('Storage :')
    Screen_Size = input('Screen size (Small/Medium/Large) :')
    Camera = input('Camera quality (Good/Excellent) :')
    Battery_Life = input('Battery Life (Good/Excellent) :')
    Battery = input('Battery Capacity :')
    Type = input('Type (Gaming/General) :')

    mycon = mysql.connector.connect(host ='localhost',user = 'root',password = 'qwerty',
                                    database = 'cs_project')
    mycursor = mycon.cursor()
    mycursor.execute("SELECT * FROM phones")
    count=len(mycursor.fetchall())
    ID='P'+str(count+1)

    q = "INSERT INTO phones VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}',{},'{}',1)".format(
        ID,Brand,Model,RAM,Storage,Screen_Size,Camera,Battery_Life,Battery,sell_price,Type)
    mycursor.execute(q)
    mycon.commit()
    mycon.close()

    #RECEIPT
    print("--------------------RECEIPT--------------------")
    print(tabulate([[Brand,Model,buy_price]], headers=['Brand','Model', 'Price'], tablefmt='fancy_grid'))
    print("THANK YOU !")
sell_phone()
def sell_laptops():
    price=float(input('Please enter the price at which your laptop was bought: '))
    age=int(input('Please enter how old the device is [Yrs]: '))

    buy_price=price-(age*1000)
    sell_price=buy_price+2000

    print('Please enter the following specifications :')
    Brand=input('Brand :')
    Model=input('Model :')
    Processor=input('Processor :')
    Processor_type = input('Processor type (Light/Moderate/Performance)')
    RAM = input("RAM :")
    Storage=input('Storage :')
    GPU = input('GPU :')
    Type = input('Type (Gaming/Light/Power) :')

    mycon = mysql.connector.connect(host ='localhost',user = 'root',password = 'qwerty',
                                    database = 'cs_project')
    mycursor = mycon.cursor()
    mycursor.execute("SELECT * FROM laptops")
    count=len(mycursor.fetchall())
    ID='L'+str(count+1)

    q = "INSERT INTO laptops VALUES ('{}','{}','{}','{}','{}','{}','{}','{}',1,'{}','{}')".format(
        ID,Brand,Model,Processor,Processor_type,RAM,Storage,GPU,sell_price,Type)
    mycursor.execute(q)
    mycon.commit()
    mycon.close()

    #RECEIPT
    print("--------------------RECEIPT--------------------")
    print(tabulate([[Brand,Model,buy_price]], headers=['Brand','Model', 'Price'], tablefmt='fancy_grid'))
    print("THANK YOU !")

sell_laptops()
    


    
    
    

