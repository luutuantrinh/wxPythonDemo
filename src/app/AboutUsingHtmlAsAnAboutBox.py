import wx
import wx.html

class SketchAbout(wx.Dialog):
    text = '''
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            background-color: #f8f9fa;
            font-family: Arial, sans-serif;
        }
        .container {
            max-width: 600px;
            margin: auto;
            padding: 20px;
            background-color: #ffffff;
            border: 1px solid #dee2e6;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #343a40;
            text-align: center;
        }
        p {
            color: #6c757d;
        }
        .footer {
            text-align: center;
            margin-top: 20px;
            font-size: 12px;
            color: #adb5bd;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Sketch!</h1>
        <p><b>Sketch</b> is a demonstration program for <b>wxPython In Action</b> Chapter 6. It is based on the SuperDoodle demo included with wxPython, available at <a href="http://www.wxpython.org/">http://www.wxpython.org/</a></p>
        <p><b>SuperDoodle</b> and <b>wxPython</b> are brought to you by <b>Robin Dunn</b> and <b>Total Control Software</b>, Copyright &copy; 1997-2006.</p>
        <div class="footer">
            &copy; 2023 Sketch Application
        </div>
    </div>
</body>
</html>
''' 
    def __init__(self, parent): 
        wx.Dialog.__init__(self, parent, -1, 'About Sketch', size=(460, 400))
        html = wx.html.HtmlWindow(self)
        html.SetPage(self.text)
        button = wx.Button(self, wx.ID_OK, "Okay")
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(html, 1, wx.EXPAND|wx.ALL, 5)
        sizer.Add(button, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        self.SetSizer(sizer)
        self.Layout()

class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)
        
        self.InitUI()
    
    def InitUI(self):
        menubar = wx.MenuBar()
        helpMenu = wx.Menu()
        about_item = helpMenu.Append(wx.ID_ABOUT, '&About\tF1', 'About application')

        menubar.Append(helpMenu, '&Help')
        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.OnAbout, about_item)

        self.CreateStatusBar()
        self.SetStatusText('Ready')

        self.SetSize((800, 600))
        self.SetTitle('wxPython About Dialog Example')
        self.Centre()

    def OnAbout(self, event):
        dlg = SketchAbout(self)
        dlg.ShowModal()
        dlg.Destroy()

if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame(None)
    frame.Show()
    app.MainLoop()
