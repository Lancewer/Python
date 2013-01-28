"""
11.2 basic sizer: grid sizer
"""
__author__ = 'Lancewer'

import wx
from blockwindow import BlockWindow

labels = 'one two three four five six seven eight nine'.split()

class GridSizerFrame(wx.Frame):
    def __init__(self):
        super(GridSizerFrame, self).__init__(None, -1, "Basic Grid Sizer")
        sizer = wx.GridSizer(rows = 3, cols =3, hgap = 5, vgap = 5) #create the grid sizer
        for label in labels:
            bw = BlockWindow(self,label = label)
            sizer.Add(bw, 0, 0) # add the window into the sizer
        self.SetSizer(sizer)
        self.Fit()

if __name__ == '__main__':
    app = wx.PySimpleApp()
    GridSizerFrame().Show()
    app.MainLoop()