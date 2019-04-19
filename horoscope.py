import requests
from bs4 import BeautifulSoup

rq = requests.get("https://www.cheriefm.fr/horoscope")
page = rq.content
soup = BeautifulSoup(page, "html.parser")

#récupération des
astro = soup.find_all("h2", {"class": "thumbnailHoroscope-title titleAside"})
horo = soup.find_all("p", {"class": "thumbnailHoroscope-text"})

#boucle sur les listes récupérés
liste_titre = [elt.string.strip() for elt in astro]
liste_desc = [elt.string.strip() for elt in horo]

#Variables pour vérifier la longueur des listes
tlistetitre = len(liste_titre)
tlistdesc = len(liste_desc)

#print(tlistetitre)
#print(tlistdesc)
#print(liste_titre)
#print(liste_desc)


result = zip()
resultlist = list(result)
print(resultlist)
result = zip(liste_titre, liste_desc)
resultSet = set(result)
print(resultSet)