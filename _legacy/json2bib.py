#!/usr/bin/python

import json, os, re, sys

reload(sys)
sys.setdefaultencoding('utf-8')

with open('pubs.json', 'r') as inf:
	pubs = json.load(inf)



def bibtex(p, store):
	# first, get the obvious
	authors = p['authors']
	title = p['title']
	year = p['year']

	# now extract journal, volume and pages (if any)
	# journalname... YEAR, ...volume..., pages
	jstr = p['jour']
	note = None
	journal = jstr[:jstr.index(str(year))].strip()
	
	entry = {
		'author': authors,
		'title' : title,
		'journal': journal,
		'year': year,
	}


	parts = jstr[jstr.index(str(year))+4:].split(', ')

	pages = None
	if re.match(r'\d+-\d+', parts[-1]):
		entry['pages'] = parts[-1].strip()
		v = ", ".join(parts[1:-1]).strip()
	else:
		v = ", ".join(parts[1:]).strip()  # no pages

	if v:
		entry['volume'] = v


	url = None
	if p['links']:
		url = '; '.join(map(lambda x: x['href'], p['links']))
		if url:
			entry['url'] = url

	if 'note' in p:
		entry['note'] = p['note']

	# make key: first-authorYearTitle
	key = "%s%s%s" % (
		re.sub(r'[^\x00-\x7f]',r'', authors.split(', ')[0].split(' ')[-1].lower()),
		str(year), 
		re.findall(r'\w+', title)[0].lower())

	# prevent collision
	if key in store:
		print >> sys.stderr, 'Collision for ' + key
		i = 1
		nkey = key + str(i)
		i = i + 1
		while nkey in store:
			nkey = key + str(i)
			i = i + 1
		key = nkey

	return key, entry


# global store of bib entries
bibstore = {}

for k, l in pubs.iteritems():
	for p in l:
		key, bib = bibtex(p, bibstore)
		bibstore[key] = bib
		bstr = '''@article{%s,
	author = {%s},
	title = {{%s}},
	journal = {%s},
	year = {%s}''' % (key, bib['author'], bib['title'], bib['journal'], str(bib['year']))
		
		if 'volume' in bib:
			bstr += ",\n\tvolume = {%s}" % bib['volume']

		if 'pages' in bib:
			bstr += ",\n\tpages = {%s}" % bib['pages']

		if 'url' in bib:
			bstr += ",\n\turl = \"%s\"" % bib['url']

		if 'note' in bib:
			bstr += ",\n\tbote = \"%s\"" % bib['note']

		bstr += "\n}"

		print bstr
