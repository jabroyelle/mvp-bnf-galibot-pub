import requests
from bs4 import BeautifulSoup

print("Starting Web Crawling ...")

#website to crawl
website="https://essentiels.bnf.fr/fr/litterature"
pagesVisited = []
pagesToVisit = [website]

while len(pagesToVisit) != 0 :
    if pagesToVisit[0] not in pagesVisited:
        print(pagesToVisit[0])

        # Part 0 : get page content
        page = requests.get(pagesToVisit[0])

        content = BeautifulSoup(page.text, 'html.parser')

        # Part 1 : get links on page to visit them later on
        for tag in content.find_all('a', {'class': 'preview-entity'}):
            if tag['href'] not in pagesVisited and tag['href'] not in pagesToVisit :
                pagesToVisit.append(tag['href'])

        # Part 2 : Save content to a file
        # filename = "./litterature/" + content.find_all('h1')[0].get_text().strip() + ".txt"
        # print("-",filename )

        if content.find('div', {'class': 'person'}) != None : 
            filename = "./litterature/person-" + content.find_all('h1')[0].get_text().strip() + ".txt"
            file = open(filename, 'w')
            file.write(content.find('div', {'class': 'person'}).get_text())
        elif content.find('div', {'class': 'theme'}) != None : 
            filename = "./litterature/theme-" + content.find_all('h1')[0].get_text().strip() + ".txt"
            file = open(filename, 'w')
            file.write(content.find('div', {'class': 'theme'}).get_text())
        elif content.find('div', {'class': 'folder'}) != None : 
            filename = "./litterature/folder-" + content.find_all('h1')[0].get_text().strip() + ".txt"
            file = open(filename, 'w')
            file.write(content.find('div', {'class': 'folder'}).get_text())
        elif content.find('div', {'class': 'container-preview-article'}) != None: 
            filename = "./litterature/article-" + content.find_all('h1')[0].get_text().strip() + ".txt"
            file = open(filename, 'w')
            file.write(content.find('div', {'class': 'container-preview-article'}).get_text())
        elif content.find('div', {'class': 'container-preview-gallery'}) != None: 
            filename = "./litterature/album-" + content.find_all('h1')[0].get_text().strip() + ".txt"
            file = open(filename, 'w')
            file.write(content.find('div', {'class': 'container-preview-gallery'}).get_text())
        elif content.find('div', {'class': 'container-preview-sound'}) != None: 
            filename = "./litterature/podcast-" + content.find_all('h1')[0].get_text().strip() + ".txt"
            file = open(filename, 'w')
            file.write(content.find('div', {'class': 'container-preview-sound'}).get_text())
        elif content.find('div', {'class': 'container-preview-video'}) != None: 
            filename = "./litterature/video-" + content.find_all('h1')[0].get_text().strip() + ".txt"
            file = open(filename, 'w')
            file.write(content.find('div', {'class': 'container-preview-video'}).get_text())
        elif content.find('div', {'class': 'container-preview-anthologie'}) != None: 
            filename = "./litterature/anthologie-" + content.find_all('h1')[0].get_text().strip() + ".txt"
            file = open(filename, 'w')
            file.write(content.find('div', {'class': 'container-preview-anthologie'}).get_text())
        elif content.find('div', {'class': 'container-preview-book'}) != None: 
            filename = "./litterature/book-" + content.find_all('h1')[0].get_text().strip() + ".txt"
            file = open(filename, 'w')
            file.write(content.find('div', {'class': 'container-preview-book'}).get_text())
        elif content.find('div', {'class': 'container-preview-extract'}) != None: 
            filename = "./litterature/extract-" + content.find_all('h1')[0].get_text().strip() + ".txt"
            file = open(filename, 'w')
            file.write(content.find('div', {'class': 'container-preview-extract'}).get_text())
        else :
            filename = "./litterature/unknown-" + content.find_all('h1')[0].get_text().strip() + ".txt"
            file = open(filename, 'w')
            file.write(pagesToVisit[0])
            # print(pagesToVisit[0])


        file.close()

        pagesVisited.append(pagesToVisit[0])
        pagesToVisit.pop(0)
    else:
        pagesToVisit.pop(0)
        