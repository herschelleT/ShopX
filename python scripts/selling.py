import mysql.connector

mycon = mysql.connector.connect(host="localhost",user="root",password="qwerty",database="cs_project")

mycursor = mycon.cursor()

device = input("Enter your device :").split()
model = input("Enter your device :")

q1 = "SELECT Model FROM {} WHERE Model='{}'".format(device,model)
mycursor.execute(q1)

x = mycursor.fetchall()

for i in x:
    if 
