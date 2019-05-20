def procitajIstoriju():
    import mysql.connector
    cnx = mysql.connector.connect(user='testing', password='testing',
                                  host='192.168.2.102',
                                  database='testing')
    cursor = cnx.cursor()
    query = ("SELECT vreme, temperatura_1, temperatura_2, pritisak, vlaznost_vazduha FROM meteo_uslovi order by id desc limit 5")

    cursor.execute(query)

    vrednosti = []
    for (vreme, temperatura_1, temperatura_2, pritisak, vlaznost_vazduha) in cursor:
        vrednosti.append({'vreme':vreme, 'temperatura_1':temperatura_1, 'temperatura_2':temperatura_2, 'pritisak':pritisak, 'vlaznost_vazduha':vlaznost_vazduha})

    cursor.close()
    cnx.close()
    return vrednosti