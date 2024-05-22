import wx

class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)
        
        # Liên kết sự kiện di chuyển chuột với phương thức xử lý sự kiện OnMouseMove
        self.Bind(wx.EVT_MOTION, self.OnMouseMove)
        
        self.text = wx.StaticText(self, label="Di chuyển chuột trong cửa sổ này")
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.text, 0, wx.ALL | wx.CENTER, 5)
        self.SetSizerAndFit(self.sizer)

    def OnMouseMove(self, event):
        pos = event.GetPosition()
        self.text.SetLabel(f"Vị trí chuột: {pos}")

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, title="Mouse Move Event Example")
        self.frame.Show()
        return True

app = MyApp(False)
app.MainLoop()
