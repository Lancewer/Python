"""
This is the test program for Stock Button
"""
__author__ = 'Lancewer'

import wx
from stockbuttons import MyPanel

class MyFrame(wx.Frame):
    def __init__(self, parent, id=wx.ID_ANY, title='',
                 pos=wx.DefaultPosition, size=wx.DefaultSize,
                 style = wx.DEFAULT_FRAME_STYLE, name='MyFrame'):
        super(MyFrame, self).__init__(parent, id, title, pos, size, style, name)
        self.panel = MyPanel(self)

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None)
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

if __name__ == '__main__':
    app = MyApp(False)
    app.MainLoop()