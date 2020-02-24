from bs4 import BeautifulSoup
import requests
import re

def scrapFnacLatestReleases(offset):
	headers = {
		"User-Agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; Avant Browser; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)"
	}
	page = requests.get("https://www.fnac.com/n263429/Nouveautes-musique-de-la-semaine", headers=headers)
	soup = BeautifulSoup(page.content, 'html.parser')
	soup.prettify()
	articles = soup.find_all(class_="clearfix Article-item js-Search-hashLinkId")[0:offset]
	releases = ""
	for article in articles:
		albumName = article.find(class_="Article-title js-minifa-title js-Search-hashLink").get_text().strip()
		bandName = re.sub("(\(Interprète\))", "", article.find(class_="Casting").get_text()).strip()
		releases += f'Titre: {albumName} - Artiste: {bandName}\n'
	return releases