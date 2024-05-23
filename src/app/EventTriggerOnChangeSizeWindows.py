import wx

class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)
        
        self.Bind(wx.EVT_SIZE, self.OnSize)
        
        self.text = wx.StaticText(self, label="Thay đổi kích thước cửa sổ này")
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.text, 0, wx.ALL | wx.CENTER, 5)
        self.SetSizerAndFit(self.sizer)

    def OnSize(self, event):
        size = event.GetSize()
        self.text.SetLabel(f"Kích thước mới: {size}")

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, title="Window Size Event Example")
        self.frame.Show()
        return True

app = MyApp(False)
app.MainLoop()
