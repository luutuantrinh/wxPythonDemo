import wx
import wx.adv

class LoginFrame(wx.Frame):
    def __init__(self, *args, **kw):
        # Remove the taskbar entry by using wx.FRAME_NO_TASKBAR
        kw['style'] = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.CLOSE_BOX | wx.SYSTEM_MENU | wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX) | wx.FRAME_NO_TASKBAR
        super(LoginFrame, self).__init__(*args, **kw)

        self.InitUI()
    
    def InitUI(self):
        panel = wx.Panel(self)

        vbox = wx.BoxSizer(wx.VERTICAL)

        st1 = wx.StaticText(panel, label='Username')
        vbox.Add(st1, flag=wx.LEFT | wx.TOP, border=10)

        self.tc1 = wx.TextCtrl(panel)
        vbox.Add(self.tc1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)

        st2 = wx.StaticText(panel, label='Password')
        vbox.Add(st2, flag=wx.LEFT | wx.TOP, border=10)

        self.tc2 = wx.TextCtrl(panel, style=wx.TE_PASSWORD)
        vbox.Add(self.tc2, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)

        self.cb1 = wx.CheckBox(panel, label='Remember me')
        vbox.Add(self.cb1, flag=wx.LEFT | wx.TOP, border=10)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        btn1 = wx.Button(panel, label='Login', size=(70, 30))
        hbox1.Add(btn1)

        btn2 = wx.Button(panel, label='Register', size=(70, 30))
        hbox1.Add(btn2, flag=wx.LEFT | wx.BOTTOM, border=5)

        btn3 = wx.Button(panel, label='Cancel', size=(70, 30))
        hbox1.Add(btn3, flag=wx.LEFT | wx.BOTTOM, border=5)

        vbox.Add(hbox1, flag=wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, border=10)

        link = wx.adv.HyperlinkCtrl(panel, id=wx.ID_ANY, label="Forgot Password?", url="")
        vbox.Add(link, flag=wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, border=10)

        panel.SetSizer(vbox)

        self.Bind(wx.EVT_BUTTON, self.OnLogin, btn1)
        self.Bind(wx.EVT_BUTTON, self.OnRegister, btn2)
        self.Bind(wx.EVT_BUTTON, self.OnCancel, btn3)
        self.Bind(wx.adv.EVT_HYPERLINK, self.OnForgotPassword, link)

        self.SetTitle('Login')
        self.Centre()
    
    def OnLogin(self, event):
        username = self.tc1.GetValue()
        password = self.tc2.GetValue()
        # Add your login logic here
        wx.MessageBox(f'Logging in with\nUsername: {username}\nPassword: {password}', 'Info', wx.OK | wx.ICON_INFORMATION)

    def OnRegister(self, event):
        # Add your register logic here
        wx.MessageBox('Go to register page', 'Info', wx.OK | wx.ICON_INFORMATION)

    def OnCancel(self, event):
        self.Close()

    def OnForgotPassword(self, event):
        # Add your forgot password logic here
        wx.MessageBox('Go to forgot password page', 'Info', wx.OK | wx.ICON_INFORMATION)


def main():
    app = wx.App()
    ex = LoginFrame(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
