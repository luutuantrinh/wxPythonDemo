import wx

class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        styles = wx.DEFAULT_FRAME_STYLE | wx.STAY_ON_TOP | wx.FRAME_NO_TASKBAR
        super(MyFrame, self).__init__(parent=None, title="Bitmask Example", style=styles)
        
        panel = wx.Panel(self)
        button = wx.Button(panel, label="Click Me", pos=(50, 50))
        
        self.SetSize((400, 300))
        self.Centre()

if __name__ == '__main__':
    app = wx.App(False)
    frame = MyFrame()
    frame.Show()
    app.MainLoop()
