"""
Creating Stock Buttons -- wxPython 2.8 Application Development chapter3
"""
__author__ = 'Lancewer'

import wx

class MyPanel(wx.Panel):
    def __init__(self, parent):
        super(MyPanel, self).__init__(parent)

        #Make some buttons
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        for bid in (wx.ID_OK, wx.ID_CANCEL, wx.ID_APPLY, wx.ID_HELP): #bid for button  id
            button = wx.Button(self, bid)
            sizer.Add(button, 0, wx.ALL, 5)
        self.SetSizer(sizer)