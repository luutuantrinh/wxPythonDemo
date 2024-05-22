#!/usr/bin/env python

import wx

class InsertFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'InsertFrame', size=(300, 200))
        panel = wx.Panel(self) # tạo một panel mới
        button = wx.Button(panel, label='Close', pos=(125, 10), size=(50, 50)) # thêm một button vào panel với thông số là label, pos, size
        self.Bind(wx.EVT_BUTTON, self.OnCloseMe, button) # bind sự kiện click chuột vào button với hàm OnCloseMe
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow) # bind sự kiện đóng cửa sổ với hàm OnCloseWindow

    def OnCloseMe(self, event):
        self.Close(True)
    
    def OnCloseWindow(self, event):
        self.Destroy()
    
if __name__ == '__main__':
    app = wx.PySimpleApp() 
    frame = InsertFrame(parent=None, id=-1) # tạo một frame mới với parent là None và id là -1
    frame.Show()
    app.MainLoop()