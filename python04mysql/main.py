import mysql.connector 

connection = mysql.connector.connect(user="root", password="", host="localhost", database="python")



cursor = connection.cursor()




insertQuery = "INSERT INTO users(username, city) VALUES(%(username)s, %(city)s)"
insertData = {
    "username" : "Ryszard, Cwel",
    "city" : " Bąbkowice, Sraluch"

}
cursor.execute(insertQuery, insertData)
connection.commit()

query = "SELECT id, username, city FROM users"
cursor.execute(query)


for (id, username, city) in cursor:
    print(f"{id} - {username} from {city}")

connection.close()

