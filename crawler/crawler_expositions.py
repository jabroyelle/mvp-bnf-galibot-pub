import requests
from bs4 import BeautifulSoup

print("Starting Web Crawling ...")

#website to crawl
website="https://www.bnf.fr/fr/agenda?quand=&quoi%5B0%5D=6&Appliquer=Appliquer#resultats"
pagesVisited = []
pagesToVisit = [website]

while len(pagesToVisit) != 0 :
    if pagesToVisit[0] not in pagesVisited:
        print(pagesToVisit[0])

        # Part 0 : get page content
        page = requests.get(pagesToVisit[0])

        content = BeautifulSoup(page.text, 'html.parser')

        # Part 1 : get links on page to visit them later on
        # If is a cheat to only get pages from the initial page
        if content.find('div', {'class': 'evenements-agenda'}) != None : 
            for tag in content.find_all('h3', {'class': 'views-field-title'}):
                if tag.findChild('a')['href'] not in pagesVisited and tag.findChild('a')['href'] not in pagesToVisit :
                    pagesToVisit.append('https://www.bnf.fr' + tag.findChild('a')['href'])

        # Part 2 : Save content to a file

        if content.find('div', {'class': 'content-page'}) != None : 
            filename = "./expositions/" + content.find_all('h1')[0].get_text().strip() + ".txt"
            file = open(filename, 'w')
            file.write(content.find('div', {'class': 'content-page'}).get_text())
        else :
            filename = "./litterature/unknown-" + content.find_all('h1')[0].get_text().strip() + ".txt"
            file = open(filename, 'w')
            file.write(pagesToVisit[0])


        file.close()

        pagesVisited.append(pagesToVisit[0])
        pagesToVisit.pop(0)
    else:
        pagesToVisit.pop(0)
        