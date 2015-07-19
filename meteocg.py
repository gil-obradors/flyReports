#!/usr/bin/python
# -*- coding: utf-8 -*-
# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
### sudo apt-get install python-beautifulsoup
import urllib2
import urllib
from BeautifulSoup import BeautifulSoup
__author__ = "gil"
__date__ = "$19/07/2015 10:05:14$"


if __name__ == "__main__":
    mydata=[('lugar','LELL LEGE LERS'),('tipo','ALL'),('ord','REV'),('nil','NO'),('fmt','txt'),('ano','2015'),
    ('mes','07'),('day','19'),('hora','08'),('anof','2015'),('mesf','07'),('dayf','19'),
    ('horaf','10'),('minf','59'),('enviar','Ver')]
    mydata=urllib.urlencode(mydata)
    web='http://www.ogimet.com/display_metars2.php'
    response = urllib2.urlopen(web,mydata)
    html = response.read()
    parsed_html = BeautifulSoup(html)
    print parsed_html.body.pre
