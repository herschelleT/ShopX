#import mysql.connector

#mycon = mysql.connector.connect(host = 'localhost',user = 'root',password = 'qwerty',database = 'cs_project')


import mariadb
try:
    mycon = mariadb.connect(
        user="root",
        password="123",
        host="127.0.0.1",
        database="shop"
    )
    mycursor = mycon.cursor()

    q1="CREATE TABLE laptops (Id varchar(5),Brand varchar(10),Model varchar(20),Processor varchar(15),Processor_Type varchar(15),RAM varchar(5),Storage varchar(5),GPU varchar(25),Stock int,Price int,Type varchar(10))"
    q2="INSERT INTO laptops VALUES ('L1', 'Razer', 'Blade 17', 'Intel Core i7', 'Performance', '32GB', '1TB', 'GeForce RTX 3080', 5, 130000, 'Gaming')"
    q3="INSERT INTO laptops VALUES ('L2', 'Razer', 'Blade 15', 'Intel Core i5', 'Moderate', '16GB', '512GB', 'GeForce RTX 3070', 4, 115000, 'Gaming')"
    q4="INSERT INTO laptops VALUES ('L3', 'Razer', 'Blade 13', 'Intel Core i3', 'Light', '16GB', '512GB', 'GeForce RTX 3060', 6, 105000, 'Gaming')"
    q5="INSERT INTO laptops VALUES ('L4', 'Razer', 'Blade Stealth15', 'Intel Core i5', 'Moderate', '16GB', '512GB', 'GeForce RTX 3070', 5, 85000, 'Gaming')"
    q6="INSERT INTO laptops VALUES ('L5', 'Razer', 'Blade Stealth13', 'Intel Core i3', 'Light', '16GB', '256GB', 'GeForce RTX 3060', 6, 77000, 'Gaming')"
    q7="INSERT INTO laptops VALUES ('L6', 'MSI', 'GP75', 'Intel Core i7', 'Performance', '32GB', '1TB', 'GeForce GTX 1080', 3, 65000, 'Gaming')"
    q8="INSERT INTO laptops VALUES ('L7', 'MSI', 'GP70', 'Intel Core i5', 'Moderate', '16GB', '512GB', 'GeForce GTX 1070', 3, 63000, 'Gaming')"
    q9="INSERT INTO laptops VALUES ('L8', 'MSI', 'GF65', 'Intel Core i5', 'Moderate', '16GB', '512GB', 'GeForce GTX 1060', 4, 57000, 'Gaming')"
    q10="INSERT INTO laptops VALUES ('L9', 'MSI', 'GF60', 'Intel Core i3', 'Light', '8GB', '256GB', 'GeForce GTX 1050', 3, 50000, 'Gaming')"
    q11="INSERT INTO laptops VALUES ('L10', 'Asus', 'Zenbook', 'Intel Core i7', 'Performance', '12GB', '512GB', 'GeForce MX150', 6, 47000, 'Light')"
    q12="INSERT INTO laptops VALUES ('L11', 'Asus', 'Vivobook', 'Intel Core i5', 'Moderate', '8GB', '256GB', 'GeForce MX150', 5, 35000, 'Light')"
    q13="INSERT INTO laptops VALUES ('L12', 'Asus', 'Chromebook', 'Intel Core i3', 'Light', '4GB', '128GB', 'Intel HD Graphics 505', 7, 25000, 'Light')"
    q14="INSERT INTO laptops VALUES ('L13', 'Lenovo', 'ThinkPad', 'Intel Core i7', 'Performance', '16GB', '512GB', 'GeForce GTX 1060', 5, 50000, 'Light')"
    q15="INSERT INTO laptops VALUES ('L14', 'Lenovo', 'Yoga', 'Intel Core i5', 'Moderate', '8GB', '256GB', 'GeForce GTX', 5, 40000, 'Light')"
    q16="INSERT INTO laptops VALUES ('L15', 'Lenovo', 'IdeaPad', 'Intel Core i5', 'Moderate', '8GB', '256GB', 'GeForce MX150', 7, 35000, 'Light')"
    q17="INSERT INTO laptops VALUES ('L16', 'Lenovo', 'IdeaPad Slim', 'Intel Core i3', 'Light', '4GB', '128GB', 'GeForce MX130', 3, 20000, 'Light')"
    q18="INSERT INTO laptops VALUES ('L17', 'Apple', 'Macbook Air', 'M1', 'Performance', '8GB', '256GB', 'M1', 4, 67000, 'Light')"
    q19="INSERT INTO laptops VALUES ('L18', 'HP', 'Probook G8', 'Intel Core i7', 'Performance', '16GB', '2TB', 'GeForce GTX 1650 Ti', 8, 60000, 'Power')"
    q20="INSERT INTO laptops VALUES ('L19', 'HP', 'Probook G7', 'Intel Core i5', 'Moderate', '16GB', '1TB', 'GeForce GTX 1650', 6, 55000, 'Power')"
    q21="INSERT INTO laptops VALUES ('L20', 'HP', 'Spectre x360 15', 'Intel Core i7', 'Moderate', '32GB', '512GB', 'GeForce GTX 1660 Ti', 6, 85000, 'Power')"
    q22="INSERT INTO laptops VALUES ('L21', 'HP', 'Spectre x360 14', 'Intel Core i5', 'Moderate', '16GB', '512GB', 'GeForce GTX 1660', 3, 80000, 'Power')"
    q23="INSERT INTO laptops VALUES ('L22', 'Dell', 'XPS 15', 'Intel Core i7', 'Performance', '16GB', '1TB', 'GeForce GTX 1660 Ti', 5, 85000, 'Power')"
    q24="INSERT INTO laptops VALUES ('L23', 'Dell', 'XPS 13', 'Intel Core i5', 'Moderate', '8GB', '512GB', 'GeForce GTX 1650', 6, 67000, 'Power')"
    q25="INSERT INTO laptops VALUES ('L24', 'Acer', 'Aspire', 'Intel Core i7', 'Performance', '16GB', '1TB', 'GeForce GTX 1660 Ti', 4, 60000, 'Power')"
    q26="INSERT INTO laptops VALUES ('L25', 'Acer', 'Swift', 'Intel Core i5', 'Moderate', '12GB', '512GB', 'GeForce GTX 1660', 8, 53000, 'Power')"
    q27="INSERT INTO laptops VALUES ('L26', 'Acer', 'Nitro', 'Intel Core i3', 'Light', '8GB', '256GB', 'GeForce GTX 1650', 6, 47000, 'Power')"
    q28="INSERT INTO laptops VALUES ('L27', 'Apple', 'Macbook Pro 13', 'M1', 'Performance', '16GB', '1TB', 'M1', 6, 97000, 'Power')"
    q29="INSERT INTO laptops VALUES ('L28', 'Apple', 'Macbook Pro 15', 'M1', 'Performance', '32GB', '2TB', 'M1', 8, 140000, 'Power')"
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
    mycursor.execute(q20)
    mycursor.execute(q21)
    mycursor.execute(q22)
    mycursor.execute(q23)
    mycursor.execute(q24)
    mycursor.execute(q25)
    mycursor.execute(q26)
    mycursor.execute(q27)
    mycursor.execute(q28)
    mycursor.execute(q29)

    mycon.commit()
    mycon.close()
except mariadb.Error as e:
    print(e)



