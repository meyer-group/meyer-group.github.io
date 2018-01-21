---
layout: pubs
title: "Publications"
---

## Selected

<ol>
<li>{% reference halter2016uranium %}
	<a href="http://www.nature.com/nature/journal/vaop/ncurrent/abs/nature16530.html" _target="blank">get it here</a>
	[(fau news)](https://www.fau.de/2016/01/news/wissenschaft/abfall-der-kernindustrie-dient-als-katalysator-fuer-die-produktion-von-wasserstoff-aus-wasser/)
	[(BR news)](http://www.br.de/nachrichten/mittelfranken/inhalt/katalysator-uran-uni-erlangen-102.html)
	[(Spectrum.de news)](http://www.spektrum.de/news/uran-zum-wasserspalten/1400543)
	[(labo.de news)](http://www.labo.de/news/produktion-von-wasserstoff-aus-wasser-mittels-uran-basiertem-katalysator.htm)
	[(analytic news)](http://www.analytik-news.de/Presse/2016/54.html)
</li>
<li>{% reference malischewski2016isolation %}
	[(get it here)](http://apps.webofknowledge.com/InboundService.do?mode=FullRecord&customersID=RID&IsProductCode=Yes&product=WOS&Init=Yes&Func=Frame&DestFail=http%3A%2F%2Fwww.webofknowledge.com&action=retrieve&SrcApp=RID&SrcAuth=RID&SID=Y2K5QSTTakAgNknlDRE&UT=WOS%3A000381561200035)
</li>
<li>{% reference schmidt2014molecular %}
	[(get it here)](http://pubs.acs.org/doi/abs/10.1021/ja411627z)
	[(cover)](http://pubs.acs.org/doi/pdf/10.1021/ja504528n)
	[(spotlight)](http://pubs.acs.org/action/showLargeCover?issue=407259848)
</li>
<li>{% reference pierre2014synthesis %}
	[(get it here)](http://onlinelibrary.wiley.com/doi/10.1002/anie.201402050/abstract)
</li>
<li>{% reference scholz2013crystal %}
	[(get it here)](http://www.sciencemag.org/content/341/6141/62.full)
	[(cen highlight)](http://cen.acs.org/articles/91/i27/Solving-Old-Bonding-Debate.html)
	[(rsc highlight)](http://www.rsc.org/chemistryworld/2013/07/norbornyl-cation-nonclassical-structure-olah-herb-brown)
	[(rsc follow-up)](http://www.rsc.org/chemistryworld/2013/07/norbornyl-nonclassical-cation-brown-winstein-olah)
	[(science daily news)](http://www.sciencedaily.com/releases/2013/07/130709124000.htm)
	[(phys.org news)](http://phys.org/news/2013-07-german-scientists-nonclassical-norbornyl-carbocation.html)
	[(commentary)](http://luysii.wordpress.com/2013/07/08/schleyer-is-still-pumping-out-papers-crystallization-of-a-nonclassical-norbornyl-cation/)
	[(ChiuZ report)](/assets/pdf/ChiuZ.pdf)
</li>
<li>{% reference kropp2012manganese %}
	[(get it here)](http://pubs.acs.org/doi/abs/10.1021/ja306647c)
</li>
<li>{% reference scepaniak2011synthesis %}
	[(get it here0}(http://www.sciencemag.org/content/331/6020/1049.full)
	[(RSC news)](/assets/pdf/RSC_NEWS.pdf)
	[(C&E news)](/assets/pdf/C&amp;E%20News.pdf)
	[(GDCh Nachrichten der Chemie)](/assets/pdf/GDCh%20NachrChem.pdf)
	[(NatChem news&views)](/assets/pdf/NatChem%20news&amp;views.pdf)
</li>
<li>{% reference vogel2008an %}
	[(get it here)](http://www3.interscience.wiley.com/journal/117924280/abstract)
	[(science editor's choice)](/assets/pdf/science_editors_choice.pdf)
	[("german chemical news")](/assets/pdf/VogelIronNachChemie.pdf)
</li>
<li>{% reference fox2008towards %}
	[(get it here)](http://apps.webofknowledge.com/InboundService.do?mode=FullRecord&customersID=RID&IsProductCode=Yes&product=WOS&Init=Yes&Func=Frame&DestFail=http%3A%2F%2Fwww.webofknowledge.com&action=retrieve&SrcApp=RID&SrcAuth=RID&SID=Y2K5QSTTakAgNknlDRE&UT=WOS%3A000259265200035)
</li>
<li>{% reference castro-rodriguez2004a %}
	[(get it here)](http://www.sciencemag.org/cgi/content/abstract/sci;305/5691/1757?maxtoshow=&HITS=10&hits=10&RESULTFORMAT=&andorexacttitleabs=and&andorexactfulltext=and&searchid=1&FIRSTINDEX=0&volume=305&firstpage=1757&resourcetype=HWCIT)
	[(C&E news)](/assets/pdf/CuENewsUCO2.pdf)
	[("german chemical news")](/assets/pdf/UOCO-German.jpg)
</li>
</ol>

## Selected Reviews

<ol>
<li>{% reference pierre2014activation %}
	[(get it here)](http://onlinelibrary.wiley.com/doi/10.1002/9781118792797.ch05/summary)
</li>
<li>{% reference hohenberger2012the %}
	[(get it here)](http://www.nature.com/ncomms/journal/v3/n3/full/ncomms1718.html)
</li>
<li>{% reference fox2008towards %}
	[(get it here)](http://pubs.acs.org/cgi-bin/abstract.cgi/jacsat/2008/130/i37/abs/ja804263w.html)
</li>
<li>{% reference bart2008highlights %}
	[(get it here)](http://www.springerlink.com/content/y3410061814q5183/)
</li>
</ol>


## Most cited

{% reference hu2004group %}


## Bibliography

<p>
{% for i in (1998..2017) reversed %}
<a href="#{{i}}">{{i}}</a>{% unless forloop.last %}, {% endunless %}
{% endfor %}
</p>

{% for i in (1998..2017) reversed %}
<h2 id="{{i}}">{{i}} <a href="#bibliography"><i class="fa fa-arrow-up"></i></a></h2>
{% bibliography --query @*[year={{i}}] %}
{% endfor %}
