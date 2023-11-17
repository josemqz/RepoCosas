# https://www.learndatasci.com/tutorials/ultimate-guide-web-scraping-w-python-requests-and-beautifulsoup/

# 1: Obtener datos de tabla de sitio web

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

# descargar DOM
# soup = get_soup('https://www.allsides.com/media-bias/media-bias-ratings', address_file='allsides_com') 

# usar cache de DOM
soup = get_soup(address_file='allsides_com', use_cache=True)


# Obtener filas de tabla

# #block-views-list-of-ratings-block > div > div.view-content > table

rows = soup.select('tbody tr')
# print("rows:\n", rows)


# Obtener nombres de filas

# probando
# rows_names = rows[0].select("td a") 
# print(rows_names)

row = rows[0]
name = row.select_one('.bias-ratings-list tbody tr .views-field-title').text.strip()
print("First row name:", name, "\n")

allsides_page = row.select_one('.bias-ratings-list tbody tr .views-field-title a')['href']
allsides_page = 'https://www.allsides.com' + allsides_page

print("First row url:", allsides_page, "\n")

# Obtener bias
# href="/media-bias/left-center"
bias = row.select_one(".views-field-field-bias-image a")['href'].split('/')[-1]

print("bias:", bias)

feedback_agree = int(row.select_one(".agree").text)
feedback_disagree = int(row.select_one(".disagree").text)

print(f"community feedback: {feedback_agree}/{feedback_disagree}")


# Categoria de community feedback

print(row.select_one('.community-feedback-rating-page'))
# imprime None porque está definido en JS, ahora habría que buscar la función
# que lo define en los archivos .js en el código fuente del sitio, para poder replicarlo aquí
