import wx

class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)
        
        # Tạo một nút
        aButton = wx.Button(self, label="Click Me")
        
        # Liên kết sự kiện nhấp chuột của nút với phương thức xử lý sự kiện OnClick
        self.Bind(wx.EVT_BUTTON, self.OnClick, aButton)
        
        # Thiết lập giao diện cơ bản
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(aButton, 0, wx.ALL | wx.CENTER, 5)
        self.SetSizerAndFit(self.sizer)

    def OnClick(self, event):
        wx.MessageBox("Nút đã được nhấp!", "Thông báo", wx.OK | wx.ICON_INFORMATION)

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, title="Event Handling Example")
        self.frame.Show()
        return True

app = MyApp(False)
app.MainLoop()
