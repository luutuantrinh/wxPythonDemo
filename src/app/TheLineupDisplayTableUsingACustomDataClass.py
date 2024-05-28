import wx
import wx.grid

class LineupEntry:
    def __init__(self, pos, first, last):
        self.pos = pos
        self.first = first
        self.last = last

class LineupTable(wx.grid.GridTableBase):
    colLabels = ("First", "Last")
    colAttrs = ("first", "last")
    
    def __init__(self, entries):
        wx.grid.GridTableBase.__init__(self)
        self.entries = entries
    
    def GetNumberRows(self):
        return len(self.entries)
    
    def GetNumberCols(self):
        return len(self.colAttrs)
    
    def GetColLabelValue(self, col):
        return self.colLabels[col]
    
    def GetRowLabelValue(self, row):
        return self.entries[row].pos
    
    def IsEmptyCell(self, row, col):
        return False
    
    def GetValue(self, row, col):
        entry = self.entries[row]
        attr = self.colAttrs[col]
        return getattr(entry, attr)
    
    def SetValue(self, row, col, value):
        pass

class SimpleGrid(wx.grid.Grid):
    def __init__(self, parent):
        wx.grid.Grid.__init__(self, parent, -1)
        entries = [
            LineupEntry("CF", "Bob", "Dernier"),
            LineupEntry("2B", "Ryne", "Sandberg"),
            LineupEntry("LF", "Gary", "Matthews"),
            LineupEntry("1B", "Leon", "Durham"),
            LineupEntry("RF", "Keith", "Moreland"),
            LineupEntry("3B", "Ron", "Cey"),
            LineupEntry("C", "Jody", "Davis"),
            LineupEntry("SS", "Larry", "Bowa"),
            LineupEntry("P", "Rick", "Sutcliffe")
        ]
        self.SetTable(LineupTable(entries), takeOwnership=True)

class TestFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, "A Grid", size=(275, 275))
        grid = SimpleGrid(self)
        self.Show()

if __name__ == '__main__':
    app = wx.App(False)  # False để không chuyển hướng stdout/stderr
    frame = TestFrame(None)
    app.MainLoop()
