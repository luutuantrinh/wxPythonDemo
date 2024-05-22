#! /usr/bin/env python 

"""StreamRedirection.py is a starting point for a wxPython program."""

import wx
import sys 

class Frame(wx.Frame):
    def __init__(self, parent, id, title):
        print("Frame __init__")
        wx.Frame.__init__(self, parent, id, title)

class App(wx.App):
    def __init__(self, redirect=True, filename=None):
        super(App, self).__init__(redirect, filename)

    def OnInit(self):
        print("App OnInit")
        self.frame = Frame(parent=None, id=-1, title='Redirect') # Tạo một frame mới
        self.frame.Show() # Hiển thị frame 
        self.SetTopWindow(self.frame) 
        print("A pretend error message", file=sys.stderr) # In ra màn hình console
        return True
    
    def OnExit(self):
        print("App OnExit")
        wx.Exit()

if __name__ == '__main__':
    app = App(redirect=True) # Tạo một ứng dụng mới với redirect = True để chuyển hướng output
    print("before MainLoop")
    app.MainLoop()
    print("after MainLoop")
