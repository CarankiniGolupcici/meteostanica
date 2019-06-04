def zapisujPodatke(temperatura_1, temperatura_2, pritisak, vlaznost_vazduha):
    import mysql.connector
    cnx = mysql.connector.connect(user='admin', password='admin',
                                  host='127.0.0.1',
                                  database='dbkarina')
    cursor = cnx.cursor()
    query = ("INSERT INTO meteo_uslovi ( temperatura_1, temperatura_2, pritisak, vlaznost_vazduha) VALUES (%(temperatura_1)s, %(temperatura_2)s, %(pritisak)s, %(vlaznost_vazduha)s)")
    vrednosti = {
        'temperatura_1':temperatura_1,
        'temperatura_2':temperatura_2,
        'pritisak':pritisak,
        'vlaznost_vazduha':vlaznost_vazduha
    }

    cursor.execute(query,vrednosti)
    cnx.commit()
    cursor.close()
    cnx.close()