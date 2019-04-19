import requests
from bs4 import BeautifulSoup

#requete sur l'url pour récupérer le html du site
rq = requests.get("https://www.cheriefm.fr/horoscope")
page = rq.content
soup = BeautifulSoup(page, "html.parser")

#récupération des données dans les balises html
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

#utilisation de la fonction zip pour regrouper les 2 listes en un dictionnaire
result = zip()
resultlist = list(result)
print(resultlist)
result = zip(liste_titre, liste_desc)
resultSet = set(result)
print(resultSet)
