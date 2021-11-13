from Plugins.Plugin import PluginDescriptor
from Components.NimManager import nimmanager
from Components.ActionMap import ActionMap
from Components.Sources.ServiceEvent import ServiceEvent
from Components.ServiceEventTracker import ServiceEventTracker
from Components.Label import Label
from Components.Button import Button
from Components.ProgressBar import ProgressBar
from Screens.Screen import Screen
from ServiceReference import ServiceReference
from enigma import eTimer, eDVBDB, eServiceCenter, eServiceReference, iPlayableService, iFrontendInformation

class LCNScannerAbout(Screen):
	skin = """
		<screen position="80,100" size="560,400" title="SIFTeam - LCN Scanner">
			<widget name="about" position="10,10" size="540,330" font="Regular;18" />
			<widget name="key_red" position="0,360" size="140,40" valign="center" halign="center" zPosition="5" transparent="1" foregroundColor="white" font="Regular;18"/>
			<widget name="key_green" position="140,360" size="140,40" valign="center" halign="center" zPosition="5" transparent="1" foregroundColor="white" font="Regular;18"/>
			<widget name="key_yellow" position="280,360" size="140,40" valign="center" halign="center" zPosition="5" transparent="1" foregroundColor="white" font="Regular;18"/>
			<widget name="key_blue" position="420,360" size="140,40" valign="center" halign="center" zPosition="5" transparent="1" foregroundColor="white" font="Regular;18"/>
			<ePixmap name="red" pixmap="skin_default/buttons/red.png" position="0,360" size="140,40" zPosition="4" transparent="1" alphatest="on"/>
			<ePixmap name="green" pixmap="skin_default/buttons/green.png" position="140,360" size="140,40" zPosition="4" transparent="1" alphatest="on"/>
			<ePixmap name="yellow" pixmap="skin_default/buttons/yellow.png" position="280,360" size="140,40" zPosition="4" transparent="1" alphatest="on"/>
			<ePixmap name="blue" pixmap="skin_default/buttons/blue.png" position="420,360" size="140,40" zPosition="4" transparent="1" alphatest="on"/>
		</screen>"""

	def __init__(self, session, args = None):
		Screen.__init__(self, session)
		self.session = session
		
		self["key_red"] = Button(_("Exit"))
		self["key_green"] = Button("")
		self["key_yellow"] = Button("")
		self["key_blue"] = Button("")
		self["about"] = Label("""SIFTeam LCN Scanner 2.0\n\nCredits:
Skaman (developer & coder)
Morpheus883(Settings Master Chief)
Tideglo (original idea and beta tester)
Ukiller_Bestia (web master and server maintainer)
Genge (manager)
Bobsilvio (coder)
Ipbox2008 (coder)
Katapip (betaster)
Barrett (betaster)
Margy82 (skinner)
Cus2k (betatester)
Raskino (betatester)
Theseven (betatester)
Biondo79 (betatester)""")
		
		self["actions"] = ActionMap(["SetupActions", "ColorActions"],
		{
			"red": self.quit,
			"cancel": self.quit
		}, -2)		
		
	def quit(self):
		self.close()
		