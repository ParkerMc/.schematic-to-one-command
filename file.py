#open and save Uis
import wx
import os

def openf():
    app = wx.PySimpleApp()
    wildcard = "Schematic file (*.schematic)|*.schematic| All files (*.*)|*.*"
    dialog = wx.FileDialog(None, "Choose a file", os.getcwd(), "", wildcard, wx.OPEN)
    if dialog.ShowModal() == wx.ID_OK:
        file = dialog.GetPath()

    dialog.Destroy()
    return file
def savef():
    app = wx.PySimpleApp()
    wildcard = "Text Document (*.txt)|*.txt| All files (*.*)|*.*"
    dialog = wx.FileDialog(None, "Save the file", os.getcwd(), "", wildcard, wx.SAVE)
    if dialog.ShowModal() == wx.ID_OK:
        file = dialog.GetPath()

    dialog.Destroy()
    return file
