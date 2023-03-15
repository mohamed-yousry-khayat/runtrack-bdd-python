import mysql.connector

bd = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='laplateforme'
)

cursor = bd.cursor()

cursor.execute("use laplateforme")
cursor.execute("select sum(superficie) from etage;")

req = cursor.fetchall()

print("La superficie de La Plateforme est", req, "m²")