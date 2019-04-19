import pymysql
import requests
from bs4 import BeautifulSoup

connexion = pymysql.connect(host = 'localhost',
                            user = 'user1',
                            password = 'mdpuser1',
                            db = 'Promotion10',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor
                            )
curseur = connexion.cursor()

sql = 'SELECT * FROM Eleves'
curseur.execute(sql)

data = curseur.fetchall()

def signe_astrologique(date):
    if (date.month == 3 and date.day >= 21) or (date.month == 4 and date.day <= 19):
        sign = "Bélier"
    elif (date.month == 4 and date.day >= 20) or (date.month == 5 and date.day <= 20):
        sign = "Taureau"
    elif (date.month == 5 and date.day >= 21) or (date.month == 6 and date.day <= 20):
        sign = "Gémeaux"
    elif (date.month == 6 and date.day >= 21) or (date.month == 7 and date.day <= 22):
        sign = "Cancer"
    elif (date.month == 7 and date.day >= 23) or (date.month == 8 and date.day <= 23):
        sign = "Lion"
    elif (date.month == 8 and date.day >= 24) or (date.month == 9 and date.day <= 22):
        sign = "Vierge"
    elif (date.month == 9 and date.day >= 23) or (date.month == 10 and date.day <= 22):
        sign = "Balance"
    elif (date.month == 10 and date.day >= 23) or (date.month == 11 and date.day <= 21):
        sign = "Scorpion"
    elif (date.month == 11 and date.day >= 22) or (date.month == 12 and date.day <= 21):
        sign = "Sagittaire"
    elif (date.month == 12 and date.day >= 22) or (date.month == 1 and date.day <= 19):
        sign = "Capricorne"
    elif (date.month == 1 and date.day >= 20) or (date.month == 2 and date.day <= 19):
        sign = "Verseau"
    else:
        sign = "Poissons"
    return sign

'''for i in range(0, len(data)):
    print(signe_astrologique(data[i]["Date_naissance"]))'''



requete = requests.get("https://www.20minutes.fr/horoscope/")
page = requete.content
soup = BeautifulSoup(page, "html.parser")

signe = soup.find_all("h2", {"class": "titleblock-titles-title"})

p = soup.find_all("p", {"class": "mb2"})

horoscope = {}

for i in range(len(signe)):
    horoscope[signe[i].string.replace("Horoscope ", "")] = p[i * 2].string + p[i * 2 + 1].string


horoscope_promo = {}

for i in data:
    horoscope_promo[i["Prenom"]] = horoscope[signe_astrologique(i["Date_naissance"])]

for k, b in horoscope_promo.items():
    print(k,": ", b)