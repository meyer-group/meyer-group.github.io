#!/usr/bin/python

import json, os, re, string, sys, traceback
from bs4 import BeautifulSoup

f = open('pubs-2017-12-27.html')
# f = open('blah.html')
content = f.read()

soup = BeautifulSoup(content, 'html.parser')

pubs = {
	'selected': [],
	'most-cited': [],
	'selected-reviews': [],
	'publications': []
}

def process(p):
	# print(p)
	pub = {}
	try:
		# author: first em, until br
		pub['authors'] = re.sub('\s+', ' ', p.find('em').contents[0].encode('utf8').strip())
		pub['authors'] = re.sub(r'\.$', '', pub['authors'])
		
		# title: first span
		pub['title'] = re.sub(r'\s+', ' ', p.find('span').get_text().encode('utf-8').strip())
		pub['title'] = re.sub(r'\.$', '', pub['title'])

		# journal: nodes after the span...br, until em
		it = p.find('span').next_sibling #.next_sibling
		jour = []
		while it:
			try:
				tag_name = it.name
			except AttributeError:
				tag_name = ""
			if tag_name == "em":
				break
			# print('>>> ' + str(it))
			try:
				text = it.get_text().encode('utf-8').strip()
			except:
				text = it.string.encode('utf-8').strip()
			
			try:
				year = int(text)
				pub['year'] = year
			except:
				pass

			if text and text != '.':
				jour.append(text)

			it = it.next_sibling

		pub['jour'] = re.sub(r'\s+', ' ', " ".join(jour)).strip()
		pub['jour'] = re.sub(r' ,', ',', pub['jour']).strip()
		pub['jour'] = re.sub(r'get it here.*', '', pub['jour']).strip()
		pub['jour'] = re.sub(r'\.$', '', pub['jour']).strip()


		# links:
		pub['links'] = map(lambda x: {'text': re.sub('\s+', ' ', x.get_text().strip()), 'href': x['href']}, p.find_all('a'))
	
	except Exception as e:
		print >> sys.stderr, e
		print >> sys.stderr, p
		print >> sys.stderr, traceback.format_exc()
		raise e
	return pub


for g in pubs:
	for p in soup.find('div', {'id': g}).find_all('p'):
		try:
			if 'highlight' in p['class']:
				print >> sys.stderr, 'ignoring ' + p.get_text()
				continue
			parsed = process(p)
			pubs[g].append(parsed)
		except KeyError as k:
			# from ['class'], ignore.
			pass
		except Exception as e:
			print >> sys.stderr, e
			print >> sys.stderr, traceback.format_exc()

print json.dumps(pubs, sort_keys=True, indent=4, separators=(',', ': '))

