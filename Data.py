import wx

class Description_Download(wx.Dialog):
	def __init__(self,parent):
		super().__init__(parent)
		self.Main()
	
	def Main(self):
		self.SetTitle("Datos del video")
		Panel=wx.Panel(self)
		wx.StaticText(Panel, -1,'Nombre y duración del video')
		self.Text = wx.TextCtrl(Panel, wx.ID_ANY)
		wx.StaticText(Panel, -1,'Descripción del video')
		self.Text2 = wx.TextCtrl(Panel, wx.ID_ANY)
		self.Text.SetFocus()
		wx.Button(Panel, wx.ID_OK, "descargar")
		wx.Button(Panel, wx.ID_CANCEL, "cancelar")