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
			for face in obj.SubObjects:
				f = face.copy()
				box = f.BoundBox
				f.translate(box.Center * -1)
				#v = FreeCAD.Vector(box.XLength,box.YLength,box.ZLength)
				#diag = v.cross(f.normalAt(0,0))
				svg.append(Drawing.projectToSVG(f,f.normalAt(0,0)))
				del f
		data = ""
		for s in svg:
			data += s 
		open("/tmp/svg.svg","w").write("<svg>"+data+"</svg>")
		
FreeCADGui.addCommand('MyCommand1',MyTool())
