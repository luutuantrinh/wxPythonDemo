import wx

app = wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, "Message Dialog Example")

# Tạo một hộp thoại thông báo
dlg = wx.MessageDialog(frame, "Đây là một thông báo đơn giản.", "Thông báo", wx.OK | wx.ICON_INFORMATION  | wx.CANCEL, 
    pos=wx.DefaultPosition)
dlg.ShowModal()  # Hiển thị hộp thoại
dlg.Destroy()    # Hủy hộp thoại khi hoàn tất

frame.Show(True)
app.MainLoop()
