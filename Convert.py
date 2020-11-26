import wx

class Convert(wx.Dialog):
	def __init__(self,parent):
		super().__init__(parent)
		self.Main()
	
	def Main(self):
		self.SetTitle("¿Deseas extraer el audio en mp3?")
		Panel=wx.Panel(self)
		wx.Button(Panel, wx.ID_OK, "Si")
		wx.Button(Panel, wx.ID_CANCEL, "No")