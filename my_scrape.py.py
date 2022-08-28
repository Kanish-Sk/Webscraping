import requests
from bs4 import BeautifulSoup
import pprint#prity print

res = requests.get('https://news.ycombinator.com/')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
#duplicate for page 2,like that we can use for page3

soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

links = (soup.select('.titlelink'))
subtext = soup.select('.subtext')

links2 = (soup2.select('.titlelink'))#only for titles
subtext2 = soup2.select('.subtext')
#inside the subtext class we have score.inside the score we have no of lines of news

mega_link = links + links2
mega_subtext = subtext + subtext2

def sotr_stories_by_votes(hnlist):
	return sorted(hnlist, key = lambda k:k['votes'],reverse = True)

def create_custom_hn(links, subtext):#hn-hackers news
	hn = []
	for idx, item in enumerate(links):#get the index value and access it.
		title = item.getText()#It gives the title news only.
		href = item.get('href',None)#href is defaut in html that has a link to content of th news
		#none is default.if there is no link in href then it return none.
		vote = subtext[idx].select('.score')
		#some cases there is no point news only title news only.
		if len(vote):
		    points = int(vote[0].getText().replace(' points', ''))
		    #65 points we need to remove points and convert to int
		    if points > 99:
		        hn.append({'title': title, 'link': href, 'votes': points },)
	return sotr_stories_by_votes(hn)

pprint.pprint(create_custom_hn(mega_link,mega_subtext))