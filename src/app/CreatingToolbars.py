import wx

class ToolbarFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Toolbars', size=(300, 200))
        panel = wx.Panel(self)
        panel.SetBackgroundColour('White')
        statusBar = self.CreateStatusBar() # Tạo một status bar mới

        # Tạo một toolbar mới
        toolbar = self.CreateToolBar()

        # Thêm một tool vào toolbar với hình ảnh từ wx.ArtProvider
        new_tool_id = wx.NewId()
        new_bitmap = wx.ArtProvider.GetBitmap(wx.ART_NEW, wx.ART_TOOLBAR, (16, 16))
        toolbar.AddTool(new_tool_id, 'New', new_bitmap, 'Create a new document')

        # Hiển thị toolbar
        toolbar.Realize()

        # Tạo một menu bar mới
        menuBar = wx.MenuBar()
        
        # Tạo menu File
        menu1 = wx.Menu()
        menuBar.Append(menu1, "&File")

        # Tạo menu Edit
        menu2 = wx.Menu()
        menu2.Append(wx.NewId(), "&Copy", "Copy in status bar")
        menu2.Append(wx.NewId(), "C&ut", "")
        menu2.Append(wx.NewId(), "Paste", "")
        menu2.AppendSeparator()
        menu2.Append(wx.NewId(), "&Options...", "Display Options")
        menuBar.Append(menu2, "&Edit")
        
        self.SetMenuBar(menuBar)

if __name__ == '__main__':
    app = wx.App(False)
    frame = ToolbarFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
