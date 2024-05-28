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
        new_item = fileMenu.Append(wx.ID_NEW, '&New\tCtrl+N', 'New file')
        open_item = fileMenu.Append(wx.ID_OPEN, '&Open\tCtrl+O', 'Open file')
        save_item = fileMenu.Append(wx.ID_SAVE, '&Save\tCtrl+S', 'Save file')
        fileMenu.AppendSeparator()
        exit_item = fileMenu.Append(wx.ID_EXIT, 'E&xit\tCtrl+Q', 'Exit application')

        menubar.Append(fileMenu, '&File')

        # Tạo menu Help
        helpMenu = wx.Menu()
        about_item = helpMenu.Append(wx.ID_ABOUT, '&About\tF1', 'About application')

        menubar.Append(helpMenu, '&Help')

        # Thiết lập menu bar cho frame
        self.SetMenuBar(menubar)

        # Tạo status bar với 3 trường
        self.CreateStatusBar(3)
        self.SetStatusWidths([-2, -1, -1])
        self.SetStatusText('Ready', 0)
        self.SetStatusText('Welcome to wxPython!', 1)
        self.SetStatusText('Version 1.0', 2)

        # Kết nối các sự kiện
        self.Bind(wx.EVT_MENU, self.OnNew, new_item)
        self.Bind(wx.EVT_MENU, self.OnOpen, open_item)
        self.Bind(wx.EVT_MENU, self.OnSave, save_item)
        self.Bind(wx.EVT_MENU, self.OnExit, exit_item)
        self.Bind(wx.EVT_MENU, self.OnAbout, about_item)

        # Thiết lập kích thước và tiêu đề cho frame
        self.SetSize((800, 600))
        self.SetTitle('wxPython Menu and Status Bar Example')
        self.Centre()
    
    def OnNew(self, event):
        self.SetStatusText('New file selected', 0)
        self.SetStatusText('Creating new file...', 1)

    def OnOpen(self, event):
        self.SetStatusText('Open file selected', 0)
        self.SetStatusText('Opening file...', 1)

    def OnSave(self, event):
        self.SetStatusText('Save file selected', 0)
        self.SetStatusText('Saving file...', 1)

    def OnExit(self, event):
        self.Close(True)

    def OnAbout(self, event):
        wx.MessageBox('This is a wxPython example', 'About', wx.OK | wx.ICON_INFORMATION)


if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame(None)
    frame.Show()
    app.MainLoop()
