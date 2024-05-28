import wx
import wx.adv

class SplashScreenFrame(wx.adv.SplashScreen):
    def __init__(self):
        # Load the bitmap for the splash screen
        bitmap = wx.Image("splash.bmp", wx.BITMAP_TYPE_BMP).Scale(300, 200).ConvertToBitmap() # Resize bitmap
        
        # Create the splash screen
        wx.adv.SplashScreen.__init__(self, bitmap,
                                wx.adv.SPLASH_CENTRE_ON_SCREEN | wx.adv.SPLASH_TIMEOUT,
                                3000,  # Display for 3000 milliseconds (3 seconds)
                                None, -1,
                                style=wx.SIMPLE_BORDER | wx.FRAME_NO_TASKBAR | wx.STAY_ON_TOP)
        
        # Bind the event to close the splash screen when it is clicked
        self.Bind(wx.EVT_CLOSE, self.OnExit)

        # Call Yield to allow the splash screen to be shown
        wx.Yield()

        # Set up a timer to automatically close the splash screen after the timeout
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.OnExit, self.timer)
        self.timer.Start(3000, oneShot=True)

    def OnExit(self, event):
        self.timer.Stop()
        self.Destroy()
        main_frame = MainFrame(None)
        main_frame.Show()
        wx.GetApp().SetTopWindow(main_frame)

class MainFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MainFrame, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        about_item = fileMenu.Append(wx.ID_ABOUT, '&About\tF1', 'About application')
        fileMenu.AppendSeparator()
        exit_item = fileMenu.Append(wx.ID_EXIT, 'E&xit\tCtrl+Q', 'Exit application')

        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.OnAbout, about_item)
        self.Bind(wx.EVT_MENU, self.OnExit, exit_item)

        self.CreateStatusBar()
        self.SetStatusText('Ready')

        self.SetSize((800, 600))
        self.SetTitle('wxPython Splash Screen Example')
        self.Centre()

    def OnAbout(self, event):
        wx.MessageBox('This is a wxPython example', 'About', wx.OK | wx.ICON_INFORMATION)

    def OnExit(self, event):
        self.Close(True)

class MyApp(wx.App):
    def OnInit(self):
        splash = SplashScreenFrame()
        splash.Show()
        return True

if __name__ == "__main__":
    app = MyApp(False)
    app.MainLoop()
