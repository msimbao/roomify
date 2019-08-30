import wx
import pygame
import wx.xrc
from threading import Thread
from mutagen.mp3 import MP3

###########################################################################
## Class MusicPlayerFrame
###########################################################################

class MusicPlayerFrame ( wx.Frame ):

	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 418,164 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
#		self.music_file=""
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )
		
		self.m_slider1 = wx.Slider( sbSizer3.GetStaticBox(), wx.ID_ANY, 0, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		sbSizer3.Add( self.m_slider1, 0, wx.ALL|wx.EXPAND, 5 )
		
		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_button18 = wx.Button( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Play", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.m_button18, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_button19 = wx.Button( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Pause", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.m_button19, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_button20 = wx.Button( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Stop", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.m_button20, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_button21 = wx.Button( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Resume", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.m_button21, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		
		sbSizer3.Add( gbSizer2, 1, wx.EXPAND, 5 )
		
		
		bSizer3.Add( sbSizer3, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer3 )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Open File", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.m_menuItem1 )
		
		self.m_menubar1.Append( self.m_menu1, u"File" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.m_menuItem1OnMenuSelection, id = self.m_menuItem1.GetId() )
		self.m_button18.Bind( wx.EVT_BUTTON, self.m_button18OnButtonClick )
		self.m_button19.Bind( wx.EVT_BUTTON, self.m_button19OnButtonClick )
		self.m_button20.Bind( wx.EVT_BUTTON, self.m_button20OnButtonClick )
		self.m_button21.Bind( wx.EVT_BUTTON, self.m_button21OnButtonClick )
		self.m_slider1.Bind( wx.EVT_SCROLL, self.m_slider1OnScroll )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def m_menuItem1OnMenuSelection( self, event ):
		event.Skip()
		dlg = wx.FileDialog(self,message = "Choose a file",defaultDir="",defaultFile="",
			wildcard="MP3 files (*.mp3)|*.mp3",style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR)
		if dlg.ShowModal() == wx.ID_OK:
			paths=dlg.GetPaths()
			music_file = ""
			for path in paths:
				music_file = path

			audio = MP3(music_file)
			#global player_thread
			#player_thread = Thread (target = self.play(music_file))
			#player_thread.start()
			self.m_slider1.SetMax(audio.info.length)

			self.play(music_file)

	def m_button18OnButtonClick( self, event ): #Play
		event.Skip()

	def m_button19OnButtonClick( self, event ): #Pause
		event.Skip()
		pygame.mixer.music.pause()

	def m_button20OnButtonClick( self, event ): #Stop
		event.Skip()
		pygame.mixer.music.stop()

	def m_button21OnButtonClick( self, event ): #Resume
		event.Skip()
		pygame.mixer.music.unpause()

	def m_slider1OnScroll( self, event ):
		event.Skip()
		obj = event.GetEventObject()
		val = obj.GetValue()
		pygame.mixer.music.play(0,val)

		


	def play(a,music_file):
#		clock = pygame.time.Clock()
		pygame.mixer.init()
		pygame.mixer.music.load(music_file)
		pygame.mixer.music.play()
		#while pygame.mixer.music.get_busy():
		#	clock.tick(30)
		

            


#default music on clicking just Play => /home/sabareesh/Code/hoh.mp3


app = wx.App(False)
frame = MusicPlayerFrame(None)
frame.Show()
app.MainLoop()
