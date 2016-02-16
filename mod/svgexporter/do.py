import FreeCAD,FreeCADGui,Drawing, Part

from xml.etree.ElementTree import fromstring, Element, ElementTree, tostring

def parsePath(node):
	path = {'x':[],'y':[]}
	CMDS = "MmLl"
	s = node.attrib.get('d')
	l = s.split()
	l.reverse()
	while(len(l) > 0):
		cmd = l.pop()
		if cmd in CMDS:
			path['x'].append(int(l.pop()))
			path['y'].append(int(l.pop()))
	return path

def findPlacement(bb, page, placed_bbox):
	for x in range(int(page.XMin), int(page.XMax), 5):
		for y in range(int(page.YMin), int(page.YMax), 5):
			pos = FreeCAD.Vector(x,y,0)
			bb.move(pos - bb.Center)
			if page.isInside(bb):
				intersect = False
				for box in placed_bbox:
					if bb.intersect(box):
						intersect = True
						break
				if intersect == False:
					FreeCAD.Console.PrintMessage("placement founded " + str(bb) + "\n")
					return bb
	return bb
		
# do something here...
svg = []
margin = 10
page = FreeCAD.BoundBox(margin,margin,0,210-margin,290-margin,0)
placed_bbox=[]
for obj in FreeCADGui.Selection.getSelectionEx():
	for face in obj.SubObjects:
		if type(face) != Part.Face:
			break
		f = face.copy()
		box = f.BoundBox
		f.translate(box.Center * -1)
		#f.translate(FreeCAD.Vector(box.XLength/2, box.YLength/2, box.ZLength/2))
		svgproj = Drawing.projectToSVG(f,f.Surface.Axis)
		del f
		
		l_size=5
		root = fromstring(svgproj)
		del root.attrib['stroke-width']
		for node in root.findall('.//circle'):
			print node
			x = float(node.attrib.get('cx'))
			y = float(node.attrib.get('cy'))
			#node.attrib["style"]='stroke-width:0.35;stroke-miterlimit:4;stroke-dasharray:none;fill:none'
			l1 = Element('line')
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
				  
			root.append(l1)
			root.append(l2)
			
		bbox = {'xmin':0,'ymin':0,'xmax':0,'ymax':0}
		for node in root.findall('.//path'):
			path = parsePath(node)
			bbox['xmin'] = min(min(path['x']), bbox['xmin'])
			bbox['ymin'] = min(min(path['y']), bbox['ymin'])
			bbox['xmax'] = max(max(path['x']), bbox['xmax'])
			bbox['ymax'] = max(max(path['y']), bbox['ymax'])
		FreeCAD.Console.PrintMessage(str(bbox))
		space = 2
		bb = FreeCAD.BoundBox(bbox['xmin']-space, bbox['ymin']-space, 0, bbox['xmax']+space, bbox['ymax']+space, 0)
		bb = findPlacement(bb, page, placed_bbox)
		placed_bbox.append(bb)
		root.attrib['transform'] += "translate(" + str(bb.Center.x) + "," + str(- bb.Center.y) + ")" 
		svgproj = tostring(root)
		svg.append(svgproj)
		
		
		
data = ""
for s in svg:
	data += s
	viewBox="0 0 210 297.00001"
data = '<svg width="210mm" height="297mm" viewBox="0 0 210 297" stroke-width="0.3">'+data+'</svg>'
open("/tmp/svg.svg","w").write(data)


