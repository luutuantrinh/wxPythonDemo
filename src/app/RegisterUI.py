import wx
import wx.adv

class RegisterFrame(wx.Frame):
    def __init__(self, *args, **kw):
        # Remove the taskbar entry by using wx.FRAME_NO_TASKBAR
        kw['style'] = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.CLOSE_BOX | wx.SYSTEM_MENU | wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX) | wx.FRAME_NO_TASKBAR
        super(RegisterFrame, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):
        panel = wx.Panel(self)

        vbox = wx.BoxSizer(wx.VERTICAL)

        title = wx.StaticText(panel, label='Register', style=wx.ALIGN_CENTER)
        title_font = title.GetFont()
        title_font.PointSize += 10
        title_font = title_font.Bold()
        title.SetFont(title_font)
        vbox.Add(title, flag=wx.ALIGN_CENTER | wx.TOP, border=20)

        fg_sizer = wx.FlexGridSizer(rows=6, cols=2, hgap=10, vgap=10)

        fields = [
            ('First Name', wx.TE_LEFT),
            ('Last Name', wx.TE_LEFT),
            ('Email', wx.TE_LEFT),
            ('Username', wx.TE_LEFT),
            ('Password', wx.TE_PASSWORD),
            ('Confirm Password', wx.TE_PASSWORD)
        ]

        self.text_controls = {}

        for field, style in fields:
            label = wx.StaticText(panel, label=field)
            tc = wx.TextCtrl(panel, style=style)
            fg_sizer.Add(label, flag=wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT)
            fg_sizer.Add(tc, flag=wx.EXPAND)
            self.text_controls[field] = tc

        fg_sizer.AddGrowableCol(1, 1)
        vbox.Add(fg_sizer, flag=wx.EXPAND | wx.ALL, border=20)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        register_btn = wx.Button(panel, label='Register', size=(90, 30))
        hbox2.Add(register_btn, flag=wx.RIGHT, border=5)
        cancel_btn = wx.Button(panel, label='Cancel', size=(90, 30))
        hbox2.Add(cancel_btn)
        back_btn = wx.Button(panel, label='Back', size=(90, 30))
        hbox2.Add(back_btn, flag=wx.LEFT, border=5)
        
        vbox.Add(hbox2, flag=wx.ALIGN_CENTER | wx.ALL, border=20)

        panel.SetSizer(vbox)

        self.Bind(wx.EVT_BUTTON, self.OnRegister, register_btn)
        self.Bind(wx.EVT_BUTTON, self.OnCancel, cancel_btn)

        self.SetTitle('Register')
        self.SetSize((400, 400))
        self.Centre()

    def OnRegister(self, event):
        data = {field: tc.GetValue() for field, tc in self.text_controls.items()}
        # Add your register logic here
        wx.MessageBox(f'Registering with:\n{data}', 'Info', wx.OK | wx.ICON_INFORMATION)

    def OnCancel(self, event):
        self.Close()

def main():
    app = wx.App()
    ex = RegisterFrame(None)
    ex.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
