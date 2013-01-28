"""
This example shows Referencing controls

Result:

Frame GetChildren:
<wx._windows.Panel; proxy of <Swig Object of type 'wxPanel *' at 0x2523ca0> >

 Panel FindWindowById:
<wx._controls.Button; proxy of <Swig Object of type 'wxButton *' at 0x25231e0> >

Button GetParent:
<wx._windows.Panel; proxy of <Swig Object of type 'wxPanel *' at 0x2523ca0> >

Get the Application Object:
<__main__.MyApp; proxy of <Swig Object of type 'wxPyApp *' at 0x2885dc0> >

Get the Frame from the App:
<__main__.MyFrame; proxy of <Swig Object of type 'wxFrame *' at 0x291b4c8> >
"""
__author__ = 'Lancewer'

import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, id=wx.ID_ANY, title = '',
                 pos = wx.DefaultPosition, size=wx.DefaultSize,
                 style = wx.DEFAULT_FRAME_STYLE, name = 'MyFrame'):
        super(MyFrame, self).__init__(parent, id, title, pos, size,style,  name)

        #Attributes
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour(wx.BLACK)
        button = wx.Button(self.panel, label='Get Children', pos=(50, 50))
        #Get the button's ID
        self.btnId = button.GetId()
        #Event Handlers
        self.Bind(wx.EVT_BUTTON, self.OnButton, button)

    def OnButton(self, event):
        """
        Called when the Button is clicked
        """
        print '\nFrame GetChildren:'
        for child in self.GetChildren():
            print '%s' % repr(child)

        print '\n Panel FindWindowById:'
        button = self.panel.FindWindowById(self.btnId)
        print '%s' % repr(button)
        #Change the Button's label
        button.SetLabel("Changed Label")

        print '\nButton GetParent:'
        panel = button.GetParent()
        print '%s' %  repr(panel)

        print '\nGet the Application Object:'
        app = wx.GetApp()
        print '%s' % repr(app)

        print '\nGet the Frame from the App:'
        frame = app.GetTopWindow()
        print '%s' % repr(frame)

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None)
        self.SetTopWindow(self.frame)
        self.frame.Show()

        return True

if __name__ == '__main__':
    app = MyApp(False)
    app.MainLoop()

