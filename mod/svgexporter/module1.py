import FreeCAD,FreeCADGui,Drawing

class MyTool:
	"My tool object"

	def GetResources(self):
		return {"MenuText": "My Command",
			"Accel": "Ctrl+M",
			"ToolTip": "My extraordinary command",
			"Pixmap"  : """
			/* XPM */
			static const char *test_icon[]={
			"16 16 2 1",
			"a c #000000",
			". c None",
			"................",
			"................",
			"..############..",
			"................",
			"................",
			"......####......",
			"......####......",
			"......####......",
			"......####......",
			"......####......",
			"......####......",
			"......####......",
			"......####......",
			"......####......",
			"................",
			"................"};
			"""}

	def IsActive(self):
		if FreeCAD.ActiveDocument == None:
			return False
		else:
			return True

	def Activated(self):
		# do something here...
		svg = []
		for obj in FreeCADGui.Selection.getSelectionEx():
			#obj.Object.Placement = FreeCAD.Placement()
			for face in obj.SubObjects:
				f = face.copy()
				box = f.BoundBox
				f.translate(box.Center * -1)
				#v = FreeCAD.Vector(box.XLength,box.YLength,box.ZLength)
				#diag = v.cross(f.normalAt(0,0))
				svg.append(Drawing.projectToSVG(f,f.Surface.Axis))
				del f
				
		#FreeCAD.Console.PrintMessage("placement " + str(obj) + str(pl) + "\n")
		#orient = face.Surface.Axis
		#FreeCAD.Console.PrintMessage("orient " + str(orient) + "\n")
		#r = FreeCAD.Rotation(FreeCAD.Vector(0,0,1),orient)
		#pl.Rotation = r
		#obj.Object.Placement = pl
				
		data = ""
		for s in svg:
			data += s
		data = "<svg>"+data+"</svg>"
		import sys
		import os
		from xml.etree.ElementTree import fromstring, Element, ElementTree

		l_size=5

		root = fromstring(data)
		et = ElementTree(root)

		for wr in root.findall('.//g'):
			wr.attrib['stroke-width']="0.30 px"
			for node in wr.findall('.//circle'):
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
					  
				wr.append(l1)
				wr.append(l2)
				
		et.write("/tmp/svg.svg")

		
FreeCADGui.addCommand('MyCommand1',MyTool())
