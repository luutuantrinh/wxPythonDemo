import wx

app = wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, "Text Entry Dialog Example")

# Tạo một hộp thoại nhập văn bản
dlg = wx.TextEntryDialog(frame, "Nhập tên của bạn:", "Nhập Văn Bản", "Tên mặc định")
if dlg.ShowModal() == wx.ID_OK:
    user_input = dlg.GetValue()  # Lấy giá trị người dùng đã nhập
    print("Tên của bạn là:", user_input)
dlg.Destroy()

frame.Show(True)
app.MainLoop()
