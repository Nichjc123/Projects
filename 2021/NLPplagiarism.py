import nltk
import requests
import urllib
from requests_html import HTML
from requests_html import HTMLSession
from bs4 import BeautifulSoup

# PLAN _____________________
# 1. TODO: Open romeo nad juliet file and save the content
rj = open('/Users/nicholashockey/Desktop/rj.txt', 'r')
sus_file = rj.read()
rj.close()

# 2. TODO: Figure out how to save the text of top 3 searches from google
# 2.a get top 3 url results


def get_source(url):
    try:
        session = HTMLSession()
        response = session.get(url)
        return response

    except requests.exceptions.RequestException as e:
        print(e)


def scrape_google(query):

    query = urllib.parse.quote_plus(query)
    response = get_source("https://www.google.co.uk/search?q=" + query)

    links = list(response.html.absolute_links)
    google_domains = ('https://www.google.',
                      'https://google.',
                      'https://webcache.googleusercontent.',
                      'http://webcache.googleusercontent.',
                      'https://policies.google.',
                      'https://support.google.',
                      'https://maps.google.')

    for url in links[:]:
        if url.startswith(google_domains):
            links.remove(url)

    return links


links = scrape_google('romeo and juliet')
# 2.b download the 3 sites
searched_info = []
for i in range(3):
    url = links[i]
    r = requests.get(url, allow_redirects=True)
    soup = BeautifulSoup(r.content, features="lxml")
    searched_info.append(soup.get_text().rstrip("\n"))

print(searched_info)
print(len(searched_info))
# 3. TODO: Find similarity(plagiarism pourcentage) by comparing the 'suspicious' text to all 5 results
# 4. TODO: Get average of all similiarity pourcentages as final number
