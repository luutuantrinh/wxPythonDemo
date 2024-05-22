import wx

app = wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, "Single Choice Dialog Example")

# Tạo một hộp thoại lựa chọn
choices = ["Lựa chọn 1", "Lựa chọn 2", "Lựa chọn 3"]
dlg = wx.SingleChoiceDialog(frame, "Chọn một mục:", "Chọn từ Danh Sách", choices)
if dlg.ShowModal() == wx.ID_OK:
    selected = dlg.GetStringSelection()  # Lấy giá trị đã chọn
    print("Bạn đã chọn:", selected)
dlg.Destroy()

frame.Show(True)
app.MainLoop()
