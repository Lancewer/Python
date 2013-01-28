"""
Utilizing Stock IDs -- wxPython 2.8 Application Development Cookbook
"""
__author__ = 'Lancewer'

import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, id=wx.ID_ANY, title='',
                 pos = wx.DefaultPosition, size=wx.DefaultSize,
                 style=wx.DEFAULT_FRAME_STYLE, name='MyFrame'):
        super(MyFrame, self).__init__(parent, id, title, pos, size,style, name)

        #Attributes
        self.panel = wx.Panel(self)

        #Setup
        ob_btn = wx.Button(self.panel, wx.ID_OK)
        cancel_btn = wx.Button(self.panel, wx.ID_CANCEL, pos=(100, 0))

        menu_bar = wx.MenuBar()
        edit_menu = wx.Menu()
        edit_menu.Append(wx.NewId(), "Test")
        edit_menu.Append(wx.ID_PREFERENCES)
        menu_bar.Append(edit_menu, "Edit")
        self.SetMenuBar(menu_bar)

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, title='Bitmaps')
        self.SetTopWindow(self.frame)
        self.frame.Show()

        return True

if __name__ == '__main__':
    app = MyApp(False)
    app.MainLoop()