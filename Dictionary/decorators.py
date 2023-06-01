import requests
from bs4 import BeautifulSoup

def synonyms(term):
    response = requests.get('https://www.thesaurus.com/browse/'+term)
    soup = BeautifulSoup(response.text, 'lxml')
    soup.find('div', {'class': 'css-1fsijta eebb9dz0'})
    return [span.text for span in soup.findAll('a', {'class': 'css-1kg1yv8 eh475bn0'})] # class = .css-7854fb for less relevant

# print(synonyms("health"))


def antonyms(term):
    response = requests.get('https://www.thesaurus.com/browse/'+term)
    soup = BeautifulSoup(response.text, 'lxml')
    soup.find('div', {'id': 'antonyms'})
    return [span.text for span in soup.findAll('a', {'class': 'css-15bafsg eh475bn0'})] # class = .css-7854fb for less relevant

# print(antonyms("kind"))
