#! /usr/bin/env python 

"""Bare.py is a starting point for a wxPython program."""

import sys # sys là một module trong Python cung cấp các biến và hàm để làm việc với môi trường runtime của Python
import os # os là một module trong Python cung cấp các hàm để làm việc với hệ điều hành
import wx # wxPython là một giao diện người dùng đồ họa (GUI) cho Python
from wx import xrc # wxPython XRC (XML Resource) là một cách để tạo và quản lý các thành phần giao diện người dùng trong wxPython
import urllib # urllib là một module trong Python cung cấp các hàm để làm việc với URL



class Frame(wx.Frame): # Tạo một class Frame kế thừa từ wx.Frame
    pass 

class App(wx.App): # Tạo một class App kế thừa từ wx.App
    def OnInit(self): # Khởi tạo ứng dụng
        self.frame = Frame(parent=None, title='Spare') # Tạo một frame mới
        self.frame.Show()
        self.SetTopWindow(self.frame) # Đặt frame là frame chính   
        return True
    
if __name__ == '__main__':
    app = App() # Tạo một ứng dụng mới
    app.MainLoop() # Chạy ứng dụng
