"""
Adding icons to windows -- wxPython 2.8 Application Development Cookbook
"""
__author__ = 'Lancewer'

import os
import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, id=wx.ID_ANY, title='',
                 pos = wx.DefaultPosition, size=wx.DefaultSize,
                 style=wx.DEFAULT_FRAME_STYLE, name='MyFrame'):
        super(MyFrame, self).__init__(parent, id, title, pos, size,style, name)

        #Attributes
        self.panel = wx.Panel(self)

        #Setup
        path = os.path.abspath('./python.png')
        icon = wx.Icon(path, wx.BITMAP_TYPE_PNG)
        self.SetIcon(icon)
        img_path = os.path.abspath('./face-grin.png')
        bitmap = wx.Bitmap(img_path, type=wx.BITMAP_TYPE_PNG)
        self.bitmap = wx.StaticBitmap(self.panel, bitmap=bitmap)

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, title='Bitmaps')
        self.SetTopWindow(self.frame)
        self.frame.Show()

        return True

if __name__ == '__main__':
    app = MyApp(False)
    app.MainLoop()