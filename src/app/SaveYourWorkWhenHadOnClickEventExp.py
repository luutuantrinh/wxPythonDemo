import wx

class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)
        
        # Tạo một nút lưu
        saveButton = wx.Button(self, label="Save Work")
        
        # Liên kết sự kiện nhấn nút với phương thức xử lý sự kiện OnSave
        self.Bind(wx.EVT_BUTTON, self.OnSave, saveButton)
        
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(saveButton, 0, wx.ALL | wx.CENTER, 5)
        self.SetSizerAndFit(self.sizer)

    def OnSave(self, event):
        # Giả sử đây là phương thức lưu công việc
        self.SaveWork()

    def SaveWork(self):
        # Mã để lưu công việc, ví dụ ghi một tệp
        with open("work.txt", "w") as file:
            file.write("Work saved!")

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, title="Event-Driven Design Example")
        self.frame.Show()
        return True

app = MyApp(False)
app.MainLoop()
