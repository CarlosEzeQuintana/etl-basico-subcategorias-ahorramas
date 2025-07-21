import requests
from bs4 import BeautifulSoup

def obtener_productos_categoria(cgid, url_base, max_paginas=10):
    productos = []
    for pagina in range(max_paginas):
        start = pagina * 20
        params = {
            'cgid': cgid,
            'pmin': '0.01',
            'start': start,
            'sz': '20',
            'selectedUrl': url_base
        }

        res = requests.get(
            'https://www.ahorramas.com/on/demandware.store/Sites-Ahorramas-Site/es/Search-UpdateGrid',
            params=params
        )

        if res.status_code != 200 or not res.text.strip():
            break  # Fin del paginado

        soup = BeautifulSoup(res.text, 'html.parser')
        items = soup.select('.tile-body')

        if not items:
            break

        for item in items:
            name = item.select_one('.product-name-gtm')
            price = item.select_one('span.value')
            if name and price:
                productos.append({
                    'categoria': cgid,
                    'nombre': name.text.strip(),
                    'precio': price.text.strip()
                })

    return productos


def obtener_subcategorias_alimentacion():
    url = "https://www.ahorramas.com/alimentacion/"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    categorias = {}
    for a in soup.select('a[href^="/alimentacion/"]'):
        href = a.get('href')
        if href and '/alimentacion/' in href:
            cgid = href.strip('/').split('/')[-1]
            categorias[cgid] = f"https://www.ahorramas.com{href}"

    return categorias
