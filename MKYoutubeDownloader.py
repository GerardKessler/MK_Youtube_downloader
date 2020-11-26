import os
import wx
import pytube
import ffmpeg
import re, string
import pydub
from pydub import AudioSegment
from Data import Description_Download
from Convert import Convert

class Window(wx.Frame):
	def __init__(self,parent):
		super().__init__(parent)
		self.Main()

	def Main(self):
		self.SetTitle('MKYoutube Downloader')
		Panel = wx.Panel(self)
		wx.StaticText(Panel,-1,'Ingrese el link del video y pulse énter')
		self.Link = wx.TextCtrl(Panel,wx.ID_ANY,style=wx.TE_PROCESS_ENTER)
		self.Link.Bind(wx.EVT_TEXT_ENTER,self.Data)
		self.CloseButton = wx.Button(Panel,label='Cerrar el programa')
		self.CloseButton.Bind(wx.EVT_BUTTON,self.CloseProgram)
		self.Show()

	def Data(self,event):
		v = pytube.YouTube(self.Link.GetValue())
		seconds = v.length
		h=(int(seconds/3600))
		m=int((seconds-(h*3600))/60)
		s=seconds-((h*3600)+(m*60))
		Duration = str(h)+':'+str(m)+':'+str(s)
		D_D = Description_Download(self)
		D_D.Text.SetValue(v.title+', '+Duration)
		D_D.Text2.SetValue(v.description)
		if D_D.ShowModal() == wx.ID_OK:
			self.Downloader()

	def Downloader(self):
		v = pytube.YouTube(self.Link.GetValue())
		self.CleanName = re.sub('[%s]' % re.escape(string.punctuation), ' ', v.title)
		v.streams.first().download('Descargas/'+self.CleanName)
		self.Conversion()

	def Conversion(self):
		v = pytube.YouTube(self.Link.GetValue())
		C_N = Convert(self)
		if C_N.ShowModal() == wx.ID_OK:
			FileName = os.listdir('Descargas/'+self.CleanName)
			AudioSegment.from_file('Descargas/'+self.CleanName+'/'+FileName[0]).export('Descargas/'+self.CleanName+'/'+self.CleanName+'.mp3', format='mp3')

	def CloseProgram(self,evt):
		self.Close()

app = wx.App()
Window(None)
app.MainLoop()