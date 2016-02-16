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

	def parsePath(self, node):
		path = {'x':[],'y':[]}
		CMDS = "MmLl"
		FreeCAD.Console.PrintMessage(str(node) +"\n")
		s = node.attrib.get('d')
		l = s.split()
		l.reverse()
		FreeCAD.Console.PrintMessage("list: " + str(l) +"\n")
		while(len(l) > 0):
			cmd = l.pop()
			if cmd in CMDS:
				path['x'].append(int(l.pop()))
				path['y'].append(int(l.pop()))
		FreeCAD.Console.PrintMessage("svgnode: " + str(path) +"\n")
		return path

	def Activated(self):
		execfile("/home/iboris/freecad/freecad_robot/mod/svgexporter/do.py")
		
FreeCADGui.addCommand('MyCommand1',MyTool())
