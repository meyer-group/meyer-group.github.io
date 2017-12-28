#!/usr/bin/python

import os, re
from bs4 import BeautifulSoup

f = open('news-2017-12-27.html')
content = f.read()

soup = BeautifulSoup(content, 'html.parser')

news = []
imgs = set()

n = None
for p in soup.find_all('p'):
	# print(p.get_text())
	if re.match('news...news', p.get_text()):
		# print 'neuer Eintrag'
		if n:
			n['imgs'] = filter(lambda x: ('topicon.gif' not in x), n['imgs'])
			news.append(n)
			# print "fertiger Eintrag: %s" % n
		n = {'texts': [], 'imgs': set()}
	elif p.find_all('img'):
		# print "extrahiere Bilder..."
		map(lambda img: n['imgs'].add(img['src']), p.find_all('img'))
		map(lambda img: imgs.add(img['src']), p.find_all('img'))
	elif not len(p.get_text().strip()):
		continue
	else:
		n['texts'].append(p.get_text())

if n:
	# print "letzter Eintrag: %s" % news
	n['imgs'] = filter(lambda x: ('topicon.gif' not in x), n['imgs'])
	news.append(n)


if not os.path.exists('scraped-news'):
    os.makedirs('scraped-news')

i = 0
for n in news:
	with open("scraped-news/%02d.md" % i, 'w') as f:
		f.write('\n'.join(n['texts']).encode('utf8'))
		f.write('\n\n')
		f.write('\n'.join(n['imgs']))
	i = i + 1

with open('scraped-news/img-dl.sh', 'w') as f:
	for i in imgs:
		f.write("wget 'http://inorganic-chemistry.net/kmpages/%s'\n" % i)
