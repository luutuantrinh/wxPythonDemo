import wx

class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)
        
        # Tạo một nút bấm
        self.button = wx.Button(self, label="Click Me")
        
        # Liên kết sự kiện nhấp nút với phương thức xử lý sự kiện OnButtonClick
        self.Bind(wx.EVT_BUTTON, self.OnButtonClick, self.button)
        
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.button, 0, wx.ALL | wx.CENTER, 5)
        self.SetSizerAndFit(self.sizer)

    def OnButtonClick(self, event):
        wx.MessageBox("Nút đã được nhấp!", "Thông báo", wx.OK | wx.ICON_INFORMATION)

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, title="Button Click Event Example")
        self.frame.Show()
        return True

app = MyApp(False)
app.MainLoop()
