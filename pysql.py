import pymysql
import datetime

connexion = pymysql.connect(host = '34.76.9.141',
                            user = 'plb',
                            password = 'plbpass',
                            db = 'promo',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor
                            )
curseur = connexion.cursor()

insert = 'INSERT INTO apprenant VALUES (NULL, "Fulleringer", "Adrien", "1993-12-22", 52.530644, 13.383068)'
sql = 'SELECT * FROM apprenant'
curseur.execute(insert)
connexion.commit()
curseur.execute(sql)

data = curseur.fetchall()
print(data)