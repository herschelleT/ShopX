# import mysql.connector

# mycon = mysql.connector.connect(host="localhost",user="root",password="qwerty",database="cs_project")

# mycursor = mycon.cursor()

import mariadb
try:
    mycon = mariadb.connect(
        user="root",
        password="123",
        host="127.0.0.1",
        database="shop"
    )
    mycursor = mycon.cursor()
    q1="CREATE TABLE smart_watches (ID varchar(5),Brand varchar(20), Model varchar(20), Battery varchar(20), Battery_Life varchar(20), Display varchar(20), Bluetooth varchar(5), Fitness_Tracker varchar(5), Price float(10,2), Type varchar(10), Stock int(3))"
    q2="INSERT INTO smart_watches values('S1','Samsung','Watch3','340mAh','2 days','AMOLED','Yes','Yes',35000,'Hybrid',10)"
    q3="INSERT INTO smart_watches values('S2','Samsung','Watch3','300mAh','2 days','AMOLED','Yes','Yes',32599,'Hybrid',10)"
    q4="INSERT INTO smart_watches values('S3','Samsung','Active5','400mAh','5 days','LED','Yes','Yes',19999,'Hybrid',10)"
    q5="INSERT INTO smart_watches values('S4','Samsung','Active5','370mAh','5 days','LED','Yes','Yes',15499,'Hybrid',10)"
    q6="INSERT INTO smart_watches values('S5','Apple','Series6','350mAh','1 days','OLED Retina','Yes','Yes',45000,'Hybrid',10)"
    q7="INSERT INTO smart_watches values('S6','Apple','Series5','350mAh','1 days','OLED Retina','Yes','Yes',42599,'Hybrid',10)"
    q8="INSERT INTO smart_watches values('S7','Apple','SE','340mAh','4 days','OLED','Yes','No',20000,'General',10)"
    q9="INSERT INTO smart_watches values('S8','Fitbit','Versa 2','400mAh','1 week','LCD','No','Yes',13000,'Fitness',10)"
    q10="INSERT INTO smart_watches values('S9','Firbit','Versa 3','390mAh','1 week','LED','Yes','Yes',22000,'Hybrid',10)"
    q11="INSERT INTO smart_watches values('S10','Fitbit','Sense','400mAh','2 weeks','LED','Yes','Yes',23000,'Hybrid',10)"
    q12="INSERT INTO smart_watches values('S11','Garmin','Forerunner 55','500mAh','2 days','LCD','No','Yes',20990,'Fitness',10)"
    q13="INSERT INTO smart_watches values('S12','Garmin','Venus 2','445mAh','11 days','AMOLED','No','Yes',41990,'Fitness',10)"


    mycursor.execute(q1)
    mycursor.execute(q2)
    mycursor.execute(q3)
    mycursor.execute(q4)
    mycursor.execute(q5)
    mycursor.execute(q6)
    mycursor.execute(q7)
    mycursor.execute(q8)
    mycursor.execute(q9)
    mycursor.execute(q10)
    mycursor.execute(q11)
    mycursor.execute(q12)
    mycursor.execute(q13)

    mycon.commit()

    mycon.close()

except mariadb.Error as e:
    print(e)


