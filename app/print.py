import win32com.client as win
import pathlib

class Printer(): 

    def __init__(self):
        self.printer = "DYMO LabelWriter 450 Turbo"

    
    def print_label(self, name:str):
        label_path = pathlib.Path("./labelname here")
        printer_com = win.Dispatch("Dymo.DymoAddIn")
        printer_label = win.Dispatch("Dymo.DymoLabels")
        printer_com.Open(label_path)
        printer_label.SetField('Text', name)

        printer_com.StartPrintJob()
        printer_com.Print(1,False)
        printer_com.EndPrintJob()