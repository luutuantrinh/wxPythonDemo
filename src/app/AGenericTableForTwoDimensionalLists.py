import wx
import wx.grid

class GenericTable(wx.grid.GridTableBase):
    def __init__(self, data, rowLabels=None, colLabels=None):
        wx.grid.GridTableBase.__init__(self)
        self.data = data
        self.rowLabels = rowLabels
        self.colLabels = colLabels
    
    def GetNumberRows(self):
        return len(self.data)
    
    def GetNumberCols(self):
        return len(self.data[0])
    
    def GetColLabelValue(self, col):
        if self.colLabels:
            return self.colLabels[col]
        return ""
    
    def GetRowLabelValue(self, row):
        if self.rowLabels:
            return self.rowLabels[row]
        return ""
    
    def IsEmptyCell(self, row, col):
        return False
    
    def GetValue(self, row, col):
        return self.data[row][col]
    
    def SetValue(self, row, col, value):
        pass

class SimpleGrid(wx.grid.Grid):
    def __init__(self, parent):
        wx.grid.Grid.__init__(self, parent, -1)
        data = [
            ["Bob", "Dernier"], 
            ["Ryne", "Sandberg"], 
            ["Gary", "Matthews"], 
            ["Leon", "Durham"], 
            ["Keith", "Moreland"], 
            ["Ron", "Cey"], 
            ["Jody", "Davis"], 
            ["Larry", "Bowa"], 
            ["Rick", "Sutcliffe"]
        ]
        colLabels = ["First", "Last"]
        rowLabels = ["CF", "2B", "LF", "1B", "RF", "3B", "C", "SS", "P"]
        table = GenericTable(data, rowLabels, colLabels)
        self.SetTable(table, takeOwnership=True)

class TestFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, "A Grid", size=(275, 275))
        grid = SimpleGrid(self)
        self.Show()

if __name__ == '__main__':
    app = wx.App(False)  # False to not redirect stdout/stderr
    frame = TestFrame(None)
    app.MainLoop()
