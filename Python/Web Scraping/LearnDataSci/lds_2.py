# 2: Obtener datos de múltiples sitios web y guardar en JSON

# Almacenamiento de DOM de sitio web

def save_html(html, path):
    with open(path, 'wb') as f:
        f.write(html)

def open_html(path):
    with open(path, 'rb') as f:
        return f.read()
    

import requests
from bs4 import BeautifulSoup

# obtener DOM de sitio web
# address: website url
# use_cache: wether to use cache or not
# address_file: website cache file name
def get_soup(address="", use_cache=False, address_file=""):
    
    try:
        if use_cache:
            html = open_html(address_file)
        else:
            #url = 'https://www.allsides.com/media-bias/media-bias-ratings'
            r = requests.get(address)

            html = r.content
            # print(html[:100])
            save_html(html, address_file)
    except:
        print("Error accediendo a fuente.")
        exit(1)

    return BeautifulSoup(html, 'html.parser')


# Obtener info para todas las filas

def get_page_data(address, it):

    print("add:", address.split('.')[1] + "-" + str(it))
    soup = get_soup(address_file=address.split('.')[1] + "-" + str(it), use_cache=True)

    rows = soup.select('tbody tr')

    data= []

    for row in rows:
        d = dict()
        
        d['name'] = row.select_one('.bias-ratings-list tbody tr .views-field-title').text.strip()
        d['allsides_page'] = 'https://www.allsides.com' + row.select_one('.bias-ratings-list tbody tr .views-field-title a')['href']
        d['bias'] = row.select_one('.views-field-field-bias-image a')['href'].split('/')[-1]
        d['agree'] = int(row.select_one('.agree').text)
        d['disagree'] = int(row.select_one('.disagree').text)
        d['agree_ratio'] = d['agree'] / d['disagree']
        # d['agreeance_text'] = get_agreeance_text(d['agree_ratio'])
        
        data.append(d)

    return data


# Iterar por paginas
from time import sleep

def get_full_data():

    pages = [
        'https://www.allsides.com/media-bias/media-bias-ratings',
        'https://www.allsides.com/media-bias/media-bias-ratings?page=1',
        'https://www.allsides.com/media-bias/media-bias-ratings?page=2'
    ]

    p_data = []
    for it, p in enumerate(pages):
        
        # extend inserta los elementos de la lista
        p_data.extend(get_page_data(p, it))
        
        sleep(10)

    return p_data


full_data = get_full_data()


# Almacenar datos

import json

def save_data(data):
    with open('allsides.json', 'w') as f:
        json.dump(data, f)

def load_data(file):
    with open(file, 'r') as f:
        return json.load(f)
    

save_data(full_data)
