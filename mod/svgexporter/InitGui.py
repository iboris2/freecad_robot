class MyWorkbench ( Workbench ):
	"My workbench object"
	Icon = """
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
	"""
	MenuText = "My Workbench"
	ToolTip = "This is my extraordinary workbench"

	def GetClassName(self):
		return "Gui::PythonWorkbench"

	def Initialize(self):
		import module1
		self.appendToolbar("My Tools", ["MyCommand1"])
		self.appendMenu("My Tools", ["MyCommand1"])
		Log ("Loading MyModule... done\n")

	def Activated(self):
		# do something here if needed...
		Msg ("MyWorkbench.Activated()\n")

	def Deactivated(self):
		# do something here if needed...
		Msg ("MyWorkbench.Deactivated()\n")

FreeCADGui.addWorkbench(MyWorkbench)
