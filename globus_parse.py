import requests
from bs4 import BeautifulSoup


base_url = 'https://globus-online.kg'


def get_categories():
    response = requests.get(f'{base_url}/catalog')
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.find('div', {'id': 'content'})
    categories = content.find_all('li', {'class': 'section'})
    parsed_categories = []

    for category in categories:
        parsed_categories.append({
            'title': category.find('a', {'class': 'parent'}).get_text(),
            'image': f"{base_url}{category.find('a', {'class': 'around_image'}).img.get('src')}",
            'sub_category_url': f"{base_url}{category.find('a', {'class': 'around_image'}).get('href')}"
        })

    return parsed_categories


def get_sub_categories(url):
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'html.parser')
    catalog = soup.find('div', {'class': 'sidebar'})
    sub_categories = []

    for sub_category in catalog.find_all('li', {'class': 'first'}):
        sub_categories.append({
            'title': sub_category.a.span.get_text(),
            'products_url': f'{base_url}{sub_category.a.get('href')}'
        })
    
    return sub_categories
