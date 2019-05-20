import mysql.connector

cnx = mysql.connector.connect(user='testing', password='testing',
                              host='192.168.2.102',
                              database='testing')
cursor = cnx.cursor()

add_statistike = ("INSERT INTO meteo_uslovi ( temperatura_1, temperatura_2, pritisak, vlaznost_vazduha) "
                  "VALUES (%s, %s, %s, %s)")
podaci = (50,49,1000,60)
cursor.execute(add_statistike,podaci)

cnx.commit()
cursor.close()
cnx.close()
