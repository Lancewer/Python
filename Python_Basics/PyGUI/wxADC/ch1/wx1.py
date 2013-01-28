"""This is an example to show the simplest wxpython application should
have.
"""
__author__ = 'Lancewer'
import wx

class MyApp(wx.App):
    def OnInit(self):
        wx.MessageBox('Hello WxPython', 'wxApp')
        return True

if __name__ == '__main__':
    app = MyApp(False)
    app.MainLoop()