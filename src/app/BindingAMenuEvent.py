#!/usr/bin/env python
import wx

class MenuEventFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Menus', size=(300, 200))
        
        # Tạo một thanh menu
        menuBar = wx.MenuBar()
        
        # Tạo một menu
        menu1 = wx.Menu()
        
        # Thêm một mục vào menu
        menuItem = menu1.Append(-1, "&Exit...")
        
        # Thêm menu vào thanh menu
        menuBar.Append(menu1, "&File")
        
        # Đặt thanh menu cho khung hình
        self.SetMenuBar(menuBar)
        
        # Liên kết sự kiện menu với trình xử lý sự kiện OnCloseMe
        self.Bind(wx.EVT_MENU, self.OnCloseMe, menuItem)
        
    def OnCloseMe(self, event):
        self.Close(True)

if __name__ == '__main__':
    app = wx.App(False)
    frame = MenuEventFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
