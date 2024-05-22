#! /usr/bin/env python 

"""Hello.py is a starting point for a wxPython program."""

import wx 

class Frame(wx.Frame): # wx.Frame là subclass của wx.Window, nó là một cửa sổ chứa các controls
    """Frame class that displays an image."""

    def __init__(self, image, parent=None, id=-1, 
                pos=wx.DefaultPosition, title='Hello, wxPython!'):
        """Create a Frame instance and display image."""
        temp = image.ConvertToBitmap()
        size = temp.GetWidth(), temp.GetHeight()
        wx.Frame.__init__(self, parent, id, title, pos, size)
        self.bmp = wx.StaticBitmap(parent=self, bitmap=temp)

class App(wx.App): # wx.App là class chứa ứng dụng
    """Application class."""
    def OnInit(self):
        #image = wx.Image('wxPython.png', wx.BITMAP_TYPE_JPEG) # Tạo một image từ file wxPython.jpg
        image = wx.Image('D:\\SAP\\Python\\UILibrary\\src\\app\\wxPython.png', wx.BITMAP_TYPE_PNG) # Tạo một image từ file wxPython.jpg
        self.frame = Frame(image)
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

def main():
    app = App()
    app.MainLoop()

if __name__ == '__main__':
    main()