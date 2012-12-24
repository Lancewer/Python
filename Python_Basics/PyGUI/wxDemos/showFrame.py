'''
This app dementrate how to show a frame
'''
__author__ = 'Lancewer'

import wx

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, title="The main frame")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

class MyFrame(wx.Frame):
    def __init__(self, parent, id=wx.ID_ANY, title="",
                 pos=wx.DefaultPosition, size=wx.DefaultSize,
                 style=wx.CLIP_CHILDREN, name='MyFrame'):
        super(MyFrame, self).__init__(parent, id, title, pos, size, style, name)

        #Attributes
        self.panel = wx.Panel(self)

if __name__ == '__main__':
    app = MyApp(False)
    app.MainLoop()

