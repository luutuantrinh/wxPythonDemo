import wx

# Bước 1: Định nghĩa lớp sự kiện mới
class TwoButtonEvent(wx.PyCommandEvent):                
    def __init__(self, evtType, id):                    
        super().__init__(evtType, id)
        self.clickCount = 0
    
    def GetClickCount(self): 
        return self.clickCount
    
    def SetClickCount(self, count): 
        self.clickCount = count

# Bước 2: Tạo kiểu sự kiện và đối tượng binder
myEVT_TWO_BUTTON = wx.NewEventType()   # Generating an event type
EVT_TWO_BUTTON = wx.PyEventBinder(myEVT_TWO_BUTTON, 1)   # Creating a binder object

# Bước 3: Tạo widget tùy chỉnh
class TwoButtonPanel(wx.Panel): 
    def __init__(self, parent, id=-1, leftText="Left", rightText="Right"): 
        super().__init__(parent, id)
        self.leftButton = wx.Button(self, label=leftText) 
        self.rightButton = wx.Button(self, label=rightText, pos=(100,0)) 
        self.leftClick = False 
        self.rightClick = False 
        self.clickCount = 0 
        self.leftButton.Bind(wx.EVT_LEFT_DOWN, self.OnLeftClick)     # Binding the lower level events
        self.rightButton.Bind(wx.EVT_LEFT_DOWN, self.OnRightClick)   # Binding the lower level events
    
    def OnLeftClick(self, event): 
        self.leftClick = True 
        self.OnClick() 
        event.Skip()   
    
    def OnRightClick(self, event): 
        self.rightClick = True 
        self.OnClick() 
        event.Skip()   
    
    def OnClick(self): 
        self.clickCount += 1 
        if self.leftClick and self.rightClick: 
            self.leftClick = False 
            self.rightClick = False 
            evt = TwoButtonEvent(myEVT_TWO_BUTTON, self.GetId())   #  Creating the custom event
            evt.SetClickCount(self.clickCount)   # Adding data to the event
            self.GetEventHandler().ProcessEvent(evt)   # Processing the event

# Tạo khung chính và liên kết sự kiện tùy chỉnh
class CustomEventFrame(wx.Frame): 
    def __init__(self, parent, id): 
        super().__init__(parent, id, 'Click Count: 0', size=(300, 100)) 
        panel = TwoButtonPanel(self) 
        self.Bind(EVT_TWO_BUTTON, self.OnTwoClick, panel)   # Binding the custom event
    
    def OnTwoClick(self, event):                                 
        self.SetTitle(f"Click Count: {event.GetClickCount()}")   # Define an event handler function 

if __name__ == '__main__': 
    app = wx.App(False) 
    frame = CustomEventFrame(parent=None, id=wx.ID_ANY) 
    frame.Show() 
    app.MainLoop()
