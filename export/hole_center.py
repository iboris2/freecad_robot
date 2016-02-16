import sys
import os
from xml.etree.ElementTree import parse, Element

l_size=5

doc = parse(os.path.abspath(sys.argv[1]))
root = doc.getroot()

for wr in root.findall('.//g'):
	for node in wr.findall('.//circle'):
		print node
		x = float(node.attrib.get('cx'))
		y = float(node.attrib.get('cy'))
		#node.attrib["style"]='stroke-width:0.35;stroke-miterlimit:4;stroke-dasharray:none;fill:none'
		l1 = Element('line')
		stroke-width="0.25 px"
		l1.attrib['x1']= str(x - l_size)
		l1.attrib['y1']= str(y)
		l1.attrib['x2']= str(x + l_size)
		l1.attrib['y2']= str(y)
		#l1.attrib['style']="stroke-width:0.35"

		l2 = Element('line')
		#l2.attrib['stroke']="black"
		l2.attrib['x1']= str(x)
		l2.attrib['y1']= str(y - l_size)
		l2.attrib['x2']= str(x)
		l2.attrib['y2']= str(y + l_size)
		#l2.attrib['style']="stroke-width:0.35"
			  
		wr.append(l1)
		wr.append(l2)

print os.path.abspath(sys.argv[2])
doc.write(os.path.abspath(sys.argv[2]))

