"""
This example is the same with wx3, just for self practise
"""
__author__ = 'Lancewer'

import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title="", id=wx.ID_ANY,
                 pos = wx.DefaultPosition, size=wx.DefaultSize,
                 style=wx.DEFAULT_FRAME_STYLE, name='MyFrame'):
        super(MyFrame, self).__init__(parent, id, title, pos, size, style, name)

        #Attributes
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour(wx.BLUE)
        self.button = wx.Button(self.panel, label='Hello Lance', pos=(100, 100))

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None)
        self.SetTopWindow(self.frame)
        self.frame.Show()

        return True

if __name__ == '__main__':
    app = MyApp(False)
    app.MainLoop()