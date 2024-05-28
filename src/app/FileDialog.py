import wx

class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)

        # Thiết lập GUI
        self.InitUI()
    
    def InitUI(self):
        # Tạo menu bar
        menubar = wx.MenuBar()

        # Tạo menu File
        fileMenu = wx.Menu()
        open_item = fileMenu.Append(wx.ID_OPEN, '&Open\tCtrl+O', 'Open file')
        save_item = fileMenu.Append(wx.ID_SAVE, '&Save\tCtrl+S', 'Save file')
        fileMenu.AppendSeparator()
        exit_item = fileMenu.Append(wx.ID_EXIT, 'E&xit\tCtrl+Q', 'Exit application')

        menubar.Append(fileMenu, '&File')

        # Thiết lập menu bar cho frame
        self.SetMenuBar(menubar)

        # Tạo status bar
        self.CreateStatusBar()
        self.SetStatusText('Ready')

        # Kết nối các sự kiện
        self.Bind(wx.EVT_MENU, self.OnOpen, open_item)
        self.Bind(wx.EVT_MENU, self.OnSave, save_item)
        self.Bind(wx.EVT_MENU, self.OnExit, exit_item)

        # Thiết lập kích thước và tiêu đề cho frame
        self.SetSize((800, 600))
        self.SetTitle('wxPython File Dialog Example')
        self.Centre()
    
    def OnOpen(self, event):
        with wx.FileDialog(self, "Choose a file to open", wildcard="All files (*.*)|*.*", style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return     # Người dùng đã hủy

            # Lấy đường dẫn tệp tin được chọn
            path = fileDialog.GetPath()
            self.SetStatusText(f'File chosen: {path}')

    def OnSave(self, event):
        with wx.FileDialog(self, "Choose a file to save", wildcard="All files (*.*)|*.*", style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return     # Người dùng đã hủy

            # Lấy đường dẫn tệp tin được chọn
            path = fileDialog.GetPath()
            self.SetStatusText(f'File saved: {path}')

    def OnExit(self, event):
        self.Close(True)


if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame(None)
    frame.Show()
    app.MainLoop()
