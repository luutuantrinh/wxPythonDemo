import wx
import time

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="Yield Example")
        panel = wx.Panel(self)
        self.button = wx.Button(panel, label="Start Long Task", pos=(50, 50))
        self.button.Bind(wx.EVT_BUTTON, self.on_button_click)
        self.Show()

    def on_button_click(self, event):
        self.button.Disable()  # Vô hiệu hóa nút trong khi thực hiện tác vụ dài
        for i in range(10):
            print(f"Processing step {i+1}")
            time.sleep(1)  # Giả lập một tác vụ dài
            wx.Yield()  # Cho phép các sự kiện khác được xử lý
        self.button.Enable()  # Kích hoạt lại nút sau khi hoàn thành

if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()
