import mysql.connector
cnx = mysql.connector.connect(user='testing', password='testing',
                              host='192.168.2.102',
                              database='testing')
cursor = cnx.cursor()
query = ("SELECT vreme, temperatura_1, temperatura_2, pritisak, vlaznost_vazduha FROM meteo_uslovi order by id desc limit 5")

cursor.execute(query)

for(vreme, temperatura_1, temperatura_2, pritisak, vlaznost_vazduha) in cursor:
    print(vreme)
    print(temperatura_1)
cursor.close()
cnx.close()
