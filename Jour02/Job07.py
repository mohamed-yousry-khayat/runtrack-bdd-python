import mysql.connector

bd = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='laplateforme'
)

cursor = bd.cursor()

cursor.execute("use laplateforme")
cursor.execute("select sum(capacite) from salles;")

req = cursor.fetchall()

print("La capacité de toute les salles est de", req)