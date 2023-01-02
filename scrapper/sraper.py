import requests
from bs4 import BeautifulSoup
import glob
import os
import time

box_l = []

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
        box = soup.find('div', class_='container_generico').get_text()
        #box_list = '\n'.join(box)
        #print(box)

        filename = url.split('/')[-1]
        with open(filename + '.txt', 'w') as file:
            file.write(box)
        #time.sleep(5)
    except:
        print("Erro de requisição no site")

filenames = glob.glob('seccion1*.txt')
with open('sec1-comunes.txt', 'w', encoding='utf-8') as out_file:
    for filename in filenames:
        with open(filename, 'r') as in_file:
            lines = in_file.read().splitlines()
            filtered_lines = filter(lambda x: x.strip(), lines)
            content = '\n'.join(filtered_lines)
            out_file.write(content)

filenames = glob.glob('seccion2*.txt')
with open('sec2-mercancias.txt', 'w', encoding='utf-8') as out_file:
    for filename in filenames:
        with open(filename, 'r') as in_file:
            lines = in_file.read().splitlines()
            filtered_lines = filter(lambda x: x.strip(), lines)
            content = '\n'.join(filtered_lines)
            out_file.write(content)

filenames = glob.glob('seccion3*.txt')
with open('sec3-viajeros.txt', 'w') as out_file:
    for filename in filenames:
        with open(filename, 'r') as in_file:
            lines = in_file.read().splitlines()
            filtered_lines = filter(lambda x: x.strip(), lines)
            content = '\n'.join(filtered_lines)
            out_file.write(content)

filenames = glob.glob('seccion4-m*.txt')
with open('sec4-compl-mercancias.txt', 'w') as out_file:
    for filename in filenames:
        with open(filename, 'r') as in_file:
            lines = in_file.read().splitlines()
            filtered_lines = filter(lambda x: x.strip(), lines)
            content = '\n'.join(filtered_lines)
            out_file.write(content)

filenames = glob.glob('seccion5-m*.txt')
with open('sec5-compl-viajeros.txt', 'w') as out_file:
    for filename in filenames:
        with open(filename, 'r') as in_file:
            lines = in_file.read().splitlines()
            filtered_lines = filter(lambda x: x.strip(), lines)
            content = '\n'.join(filtered_lines)
            out_file.write(content)

filenames = glob.glob('seccion4-5*.txt')
with open('sec6-mercancias.txt', 'w') as out_file:
    for filename in filenames:
        with open(filename, 'r') as in_file:
            lines = in_file.read().splitlines()
            filtered_lines = filter(lambda x: x.strip(), lines)
            content = '\n'.join(filtered_lines)
            out_file.write(content)

# files = glob.glob('*seccion*.txt')
# for file in files:
#     os.remove(file)
