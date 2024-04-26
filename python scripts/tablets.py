# import mysql.connector





# mycon = mysql.connector.connect(host ='localhost',user = 'root',password = 'qwerty',database = 'cs_project')

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

    q1="CREATE TABLE tablets (ID varchar(5), Brand varchar(10), Model varchar(25), Processor varchar(30), RAM varchar(5), Storage varchar(5), Screen_Size varchar(10), Battery varchar(10), Price float(10,2), Type varchar(10), Stock int(3))"
    q2 = "INSERT INTO tablets VALUES ('T1','Lenovo','M10','Qualcomm SD429','4GB','32GB','8 inch','4000mAh',21230,'Light',10)"
    q3 = "INSERT INTO tablets VALUES ('T2','Lenovo','M8','Qualcomm SD425','2GB','16GB','6 inch','3200mAh',17370,'Light',10)"
    q4 = "INSERT INTO tablets VALUES ('T3','Lenovo','M7','Cortex A53','2GB','16GB',	'6 inch','3200mAh',13510,'Light',10)"
    q5 = "INSERT INTO tablets VALUES ('T4','ASUS','Chromebook Tablet CT100','Rockchip OP1','4GB',	'32GB',	'8 inch','4200mAh',21230,'Light',10)"
    q6 = "INSERT INTO tablets VALUES ('T5','ASUS','ZenPad 8','Qualcomm MSM8916 Snapdragon',	'2GB','32GB','6 inch','4000mAh',15440,'Light',10)"
    q7 = "INSERT INTO tablets VALUES ('T6','ASUS', 'ZenPad 7','Intel Atom x3-C3230','2GB',	'16GB',	'6 inch','3500mAh',13510,'Light',10)"
    q8 = "INSERT INTO tablets VALUES ('T7','ASUS','ZenPad 3S','Intel Atom x3-C3200','4GB','32GB','8 inch','3000mAh',11580,'Light',10)"
    q9 = "INSERT INTO tablets VALUES ('T8','Samsung','Galaxy Tab A7','Qualcomm Snapdragon','4GB',	'64GB',	'10 inch','7000mAh',23160,'Power',10)"
    q10="INSERT INTO tablets VALUES ('T9','Samsung','Galaxy Tab S7+','Snapdragon 865+','8GB','256GB','12 inch','10000mAh',48250,'Power',10)"
    q11="INSERT INTO tablets VALUES ('T10','Samsung','Galaxy Tab S7','Snapdragon 778G','6GB','128GB','10 inch','8000mAh',38600,'Power',10)"
    q12="INSERT INTO tablets VALUES ('T11','Samsung','Galaxy Tab S6','Snapdragon 855','4GB','64GB','8 inch','7000mAh',25090,'Power',10)"
    q13="INSERT INTO tablets VALUES ('T12','Apple','iPad Pro','A12Z Bionic','8GB','256GB','10 inch','8000mAh',67550,'Power',10)"
    q14="INSERT INTO tablets VALUES ('T13',	'Apple','iPad Air', 'A12 Bionic','4GB',	'64GB',	'8 inch','8000mAh', 48250,'Power',10)"
    q15="INSERT INTO tablets VALUES ('T14',	'Microsoft','Surface Pro 7','Intel Core i5-1135G7', '16GB', '256GB','12 inch','7000mAh',57900,'Power',10)"
    q16="INSERT INTO tablets VALUES ('T15',	'Microsoft','Surface Pro 6','Intel Core i5-8250U','8GB','128GB','10 inch','6500mAh',48250,'Power',10)"

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
    mycursor.execute(q14)
    mycursor.execute(q15)
    mycursor.execute(q16)

    mycon.commit()
    mycon.close()

except mariadb.Error as e:
    print(e)


