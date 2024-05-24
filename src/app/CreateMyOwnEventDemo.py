import wx

# Định nghĩa một loại sự kiện mới
myEVT_CUSTOM = wx.NewEventType()

# Tạo một lớp sự kiện mới, thừa kế từ wx.PyCommandEvent
class MyCustomEvent(wx.PyCommandEvent):
    def __init__(self, etype, eid, data=None):
        wx.PyCommandEvent.__init__(self, etype, eid)
        self.data = data

    def GetData(self):
        return self.data

# Liên kết sự kiện với lớp sự kiện
EVT_CUSTOM = wx.PyEventBinder(myEVT_CUSTOM, 1)

class CustomButton(wx.Button):
    def __init__(self, *args, **kwargs):
        super(CustomButton, self).__init__(*args, **kwargs)
        self.Bind(wx.EVT_BUTTON, self.on_click)
    
    def on_click(self, event):
        # Phát ra sự kiện tùy chỉnh khi nút được nhấp
        evt = MyCustomEvent(myEVT_CUSTOM, self.GetId(), "Hello World!")
        self.GetEventHandler().ProcessEvent(evt)

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="Custom Event Example")
        panel = wx.Panel(self)
        self.button = CustomButton(panel, label="Click Me", pos=(50, 50))
        self.Bind(EVT_CUSTOM, self.on_custom_event)
        self.Show()

    def on_custom_event(self, event):
        wx.MessageBox(f"Received custom event with data: {event.GetData()}")

if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()
