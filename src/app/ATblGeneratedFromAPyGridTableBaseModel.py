import wx
import wx.grid

class LineupTable(wx.grid.GridTableBase):
    data = (("CF", "Bob", "Dernier"), ("2B", "Ryne", "Sandberg"), 
            ("LF", "Gary", "Matthews"), ("1B", "Leon", "Durham"), 
            ("RF", "Keith", "Moreland"), ("3B", "Ron", "Cey"), 
            ("C", "Jody", "Davis"), ("SS", "Larry", "Bowa"), 
            ("P", "Rick", "Sutcliffe"))
    colLabels = ("First", "Last")
    
    def __init__(self):
        wx.grid.GridTableBase.__init__(self)
    
    def GetNumberRows(self):
        return len(self.data)
    
    def GetNumberCols(self):
        return len(self.data[0]) - 1
    
    def GetColLabelValue(self, col):
        return self.colLabels[col]
    
    def GetRowLabelValue(self, row):
        return self.data[row][0]
    
    def IsEmptyCell(self, row, col):
        return False
    
    def GetValue(self, row, col):
        return self.data[row][col + 1]
    
    def SetValue(self, row, col, value):
        pass

class SimpleGrid(wx.grid.Grid):
    def __init__(self, parent):
        wx.grid.Grid.__init__(self, parent, -1)
        self.SetTable(LineupTable(), takeOwnership=True)

class TestFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, "A Grid", size=(275, 275))
        grid = SimpleGrid(self)
        self.Show()

if __name__ == '__main__':
    app = wx.App(False)  # False to not redirect stdout/stderr
    frame = TestFrame(None)
    app.MainLoop()
