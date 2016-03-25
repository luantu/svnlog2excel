#!/usr/bin/python

from xml.dom.minidom import parse
from UserString import MutableString
import xml.dom.minidom
import codecs  
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

file_name=sys.argv[1]
xml_name = file_name + '.xml'
csv_name = file_name + '.csv'

domtree = xml.dom.minidom.parse(xml_name)
collection = domtree.documentElement

logentrys = collection.getElementsByTagName("logentry")

with open(csv_name, 'wb') as csvfile:
	for logentry in logentrys:
		path_str = MutableString()
		msg_str = ''
		i = 0
		rev = logentry.getAttribute("revision")
		author = logentry.getElementsByTagName('author')[0]
		date = logentry.getElementsByTagName('date')[0]
		msgs = logentry.getElementsByTagName('msg')
		if msgs.length > 0:
			for msg in msgs:  
				for msgchild in msg.childNodes:  
					msg_str = msg_str + msgchild.nodeValue + '\n'
		paths = logentry.getElementsByTagName("path")
		for path in paths:  
			for child in path.childNodes:  
				path_str = child.nodeValue
				swriter = csv.writer(csvfile, dialect='excel')
				swriter.writerow([rev, author.childNodes[0].data, date.childNodes[0].data, msg_str.encode('gbk')  , path_str])
