# import mysql.connector

# mycon = mysql.connector.connect(host ='localhost',user = 'root',password = 'qwerty',database = 'cs_project')


import mariadb
try:
    mycon = mariadb.connect(
        user="root",
        password="123",
        host="127.0.0.1",
        database="shop"
    )
    mycursor = mycon.cursor()
    q1="CREATE TABLE phones (ID varchar(5), Brand varchar(10), Model varchar(25), RAM varchar(5), Storage varchar(5),Screen_Size varchar(10),Camera varchar(10), Battery_Life varchar(10),Battery varchar(10), Price float(10,2), Type varchar(10), Stock int(10))"
    q2 = "INSERT INTO phones VALUES ('P1','Samsung','Galaxy10','6GB','128GB','Large','Excellent','Excellent','4000mAh',29564,'General',10)"
    q3 = "INSERT INTO phones VALUES ('P2','Samsung','Galaxy8','6GB','64GB','Medium','Excellent','Excellent','4600mAh',24570,'General',10)"
    q4 = "INSERT INTO phones VALUES ('P3','Samsung','Galaxy7','4GB','32GB','Medium','Excellent','Excellent','3500mAh',20010,'Gaming',10)"
    q5 = "INSERT INTO phones VALUES ('P4','Samsung','J80','4GB','32GB', 'Small','Excellent','Good','3700mAh',14830,'General',10)"
    q6 = "INSERT INTO phones VALUES ('P5','Samsung','J30','2GB','16GB','Medium','Excellent','Good','4100mAh',12440,'General',10)"

    q7 = "INSERT INTO phones VALUES ('P6','Apple', 'XR','4GB','256GB','Large','Excellent','Good','5000mAh',29789,'Gaming',10)"
    q8 = "INSERT INTO phones VALUES ('P7','Apple','XS','4GB','256GB','Medium','Good','Excellent','4305mAh',24789,'General',10)"
    q9 = "INSERT INTO phones VALUES ('P8','Apple','i12','2GB','256GB','Small','Good','Excellent','3000mAh',25789,'Gaming',10)"
    q10= "INSERT INTO phones VALUES ('P9','Apple','i11','2GB','256GB','Small','Excellent','Good','3400mAh',27789,'General',10)"
    q11= "INSERT INTO phones VALUES ('P10','Apple','i10','2GB','256GB','Medium','Good','Excellent','4700mAh',28789,'General',10)"

    q12= "INSERT INTO phones VALUES ('P11','ASUS','G1','8GB','256GB','Large','Good','Good','4990mAh',18975,'Gaming',10)"
    q13= "INSERT INTO phones VALUES ('P12','ASUS','G2','8GB','128GB','Medium','Good','Excellent','4000mAh',22589,'Gaming',10)"

    q14= "INSERT INTO phones VALUES ('P13','HUAWEI','M30Pro','8GB','128GB','Large','Good','Excellent','4600mAh',25475,'General',10)"
    q15= "INSERT INTO phones VALUES ('P14','HUAWEI','M30','4GB','64GB','Medium','Good','Excellent','3990mAh',19679,'General',10)"
    q16= "INSERT INTO phones VALUES ('P15','HUAWEI','M20','4GB','64GB','Medium','Good','Excellent','4190mAh',22678,'General',10)"
    q17= "INSERT INTO phones VALUES ('P16','Xiaomi','MiLite','4GB','64GB','Medium','Excellent','Excellent','4010mAh',18075,'Gaming',10)"
    q18= "INSERT INTO phones VALUES ('P17','Xiaomi','MiPro','8GB','128GB','Large','Good','Excellent','3800mAh',17453,'General',10)"
    q19= "INSERT INTO phones VALUES ('P18','Xiaomi','Mi8','4GB','16GB','Small','Good','Good','4500mAh',15789,'General',10)"


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
    mycursor.execute(q17)
    mycursor.execute(q18)
    mycursor.execute(q19)

    mycon.commit()
    mycon.close()

except mariadb.Error as e:
    print(e)



