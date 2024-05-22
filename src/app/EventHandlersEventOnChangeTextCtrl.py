import wx

class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)
        
        self.textCtrl = wx.TextCtrl(self)
        
        # Liên kết sự kiện thay đổi giá trị với phương thức xử lý sự kiện OnTextChange
        self.Bind(wx.EVT_TEXT, self.OnTextChange, self.textCtrl)
        
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.textCtrl, 0, wx.ALL | wx.EXPAND, 5)
        self.SetSizerAndFit(self.sizer)

    def OnTextChange(self, event):
        newValue = self.textCtrl.GetValue()
        self.SetTitle(f"TextCtrl Value: {newValue}")

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, title="Text Change Event Example")
        self.frame.Show()
        return True

app = MyApp(False)
app.MainLoop()
