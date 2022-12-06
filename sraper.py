import requests
from bs4 import BeautifulSoup

box_l = []
box = []

url_l = 'https://www.mitma.gob.es/areas-de-actividad/transporte-terrestre/servicios-al-transportista/cap/examenes-de-formacion-de-conductores-profesionales-cap'
req_l = requests.get(url_l)
links = BeautifulSoup(req_l.text, "html.parser")
box_links = links.find('div', class_='container_generico')

for link in box_links.find_all("a"):
    link_t = link.get("href")
    if ("https" or "http") in link_t:
        pass
    else:
        print("Found. " + "https://www.mitma.gob.es"+link.get("href"))
        box_l.append("https://www.mitma.gob.es"+link.get("href"))

for i in range (len(box_l)):
    url = box_l[i]
    print("Processing. "+url)
    try:
        req = requests.get(url)
        soup = BeautifulSoup(req.text, features="lxml")
        box.append(soup.find('div', class_='container_generico').get_text())
    except:
        print("Erro de requisição no site")


print(len(box_l))
l_box = (len(box_l))
with open("myLinks1.txt", 'w', encoding='utf-8') as saved:
    for i in range(len(box_l)):
        saved.write("%s\n" % box_l[i])
        print("saved URL")
        print(i)

print(len(box))
ll_box = (len(box))
with open("cap_scrap.txt", 'w', encoding='utf-8') as saved:
    for i in range(len(box)):
        saved.write("%s\n" % box[i])
        print("saved Questions")
        print(i)

