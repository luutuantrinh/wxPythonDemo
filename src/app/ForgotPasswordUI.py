import wx
import wx.adv

class ForgotPasswordFrame(wx.Frame):
    def __init__(self, *args, **kw):
        # Remove the taskbar entry by using wx.FRAME_NO_TASKBAR
        kw['style'] = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.CLOSE_BOX | wx.SYSTEM_MENU | wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX) | wx.FRAME_NO_TASKBAR
        super(ForgotPasswordFrame, self).__init__(*args, **kw)
        
        self.InitUI()
    
    def InitUI(self):
        panel = wx.Panel(self)

        vbox = wx.BoxSizer(wx.VERTICAL)

        title = wx.StaticText(panel, label='Forgot Password', style=wx.ALIGN_CENTER)
        title_font = title.GetFont()
        title_font.PointSize += 10
        title_font = title_font.Bold()
        title.SetFont(title_font)
        vbox.Add(title, flag=wx.ALIGN_CENTER | wx.TOP, border=20)

        instruction = wx.StaticText(panel, label='Please enter your email address to reset your password.')
        vbox.Add(instruction, flag=wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, border=20)

        fg_sizer = wx.FlexGridSizer(rows=1, cols=2, hgap=10, vgap=10)

        email_label = wx.StaticText(panel, label='Email')
        self.email_tc = wx.TextCtrl(panel, style=wx.TE_LEFT)
        fg_sizer.Add(email_label, flag=wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT)
        fg_sizer.Add(self.email_tc, flag=wx.EXPAND)

        fg_sizer.AddGrowableCol(1, 1)
        vbox.Add(fg_sizer, flag=wx.EXPAND | wx.ALL, border=20)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        reset_btn = wx.Button(panel, label='Reset Password', size=(120, 30))
        hbox2.Add(reset_btn, flag=wx.RIGHT, border=5)
        cancel_btn = wx.Button(panel, label='Cancel', size=(90, 30))
        hbox2.Add(cancel_btn)
        back_btn = wx.Button(panel, label='Back', size=(90, 30))
        hbox2.Add(back_btn, flag=wx.LEFT, border=5)

        vbox.Add(hbox2, flag=wx.ALIGN_CENTER | wx.ALL, border=20)

        panel.SetSizer(vbox)

        self.Bind(wx.EVT_BUTTON, self.OnResetPassword, reset_btn)
        self.Bind(wx.EVT_BUTTON, self.OnCancel, cancel_btn)

        self.SetTitle('Forgot Password')
        self.SetSize((400, 300))
        self.Centre()

    def OnResetPassword(self, event):
        email = self.email_tc.GetValue()
        # Add your reset password logic here
        wx.MessageBox(f'Reset link sent to {email}', 'Info', wx.OK | wx.ICON_INFORMATION)

    def OnCancel(self, event):
        self.Close()

def main():
    app = wx.App()
    ex = ForgotPasswordFrame(None)
    ex.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
