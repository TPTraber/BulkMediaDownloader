import tkinter as Tkn
from tkinter import ttk
from tkinter import filedialog
from BulkMediaDownload import BulkMediaDownloader as BMD

import sv_ttk
import darkdetect


def updateLabel(label, text):
    label._text = text

class FileSelectButton(ttk.Button):
    def __init__(self, master, pathVar, type, *, class_ = "", command = "", compound = "", cursor = "", default = "normal", image = "", name = ..., padding=..., state = "normal", style = "", takefocus = ..., text = "", textvariable = ..., underline = -1, width = ""):
        def ChoosePath(event=None):
            if type == "file":
                pathVar.set(filedialog.askopenfilename())
            else:
                pathVar.set(filedialog.askdirectory())
            
            print('Selected:',pathVar.get())

        super().__init__(master, command=ChoosePath, text=text)
    
class UploadFrame(ttk.Frame): 
    def __init__(self, master, type):
        super().__init__(master)

        self.path = Tkn.StringVar()

        self.grid_rowconfigure(0, weight = 1, pad=20)

        upperFrame = ttk.Frame(self, style='Frame1.TFrame')
        lowerFrame = ttk.Frame(self, style='Frame1.TFrame')
        upperFrame.grid(column=0, row=0, sticky="we")
        lowerFrame.grid(column=0, row=1, sticky="we")

        textBox = ttk.Entry(lowerFrame, textvariable= self.path)
        textBox.grid(column=0, row=0, sticky="we")
        lowerFrame.grid_columnconfigure(0, weight=1)

        if(type.lower() == "csv"):
            subtitle = ttk.Label(upperFrame, text="Select CSV:")
            chooseButton  = FileSelectButton(upperFrame, self.path, "file", text="Choose File")
        elif (type.lower() == "folder"):
            subtitle = ttk.Label(upperFrame, text="Select Ouput Folder:")
            chooseButton  = FileSelectButton(upperFrame, self.path, "folder", text="Choose Folder")
        else:
            subtitle = ttk.Label(upperFrame, text="Select File:")
            chooseButton  = FileSelectButton(upperFrame, self.path, "file", text="Choose File")
            
        subtitle.grid(column=0, row=0, sticky="w")
        chooseButton.grid(column=1, row=0)
        
    def getPath(self):
        return self.path.get()
root = Tkn.Tk()

root.minsize(width=400, height=600)

root.title("BulkMediaDownloader")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

app = ttk.Frame(root)
app.grid(row=0,column=0, sticky="nsew")

# Set the initial theme

sv_ttk.set_theme(darkdetect.theme())

# root.tk.call("source", "azure.tcl")
# root.tk.call("set_theme", "light")

title = ttk.Label(app, text="BulkMediaDownloader", font=("Arial", 16, "bold"))
title.grid(row=0,column=0, sticky="we", padx=20)
app.grid_columnconfigure(0, weight=1)


bulkDownloadFrame = ttk.Frame(app, borderwidth=1, relief="solid")
bulkDownloadFrame.grid(column=0, row=1, sticky="we", padx=20,pady=10)


CSVFrame = UploadFrame(bulkDownloadFrame, "CSV")
CSVFrame.grid(column=0, row=1, sticky="we",padx=10)

FolderFrame = UploadFrame(bulkDownloadFrame, "folder")
FolderFrame.grid(column=0, row=2, sticky="we", pady=20,padx=10)

bulkDownloadFrame.grid_columnconfigure(0, weight=1,)


CSVFrame.grid_columnconfigure(0, weight=1)
FolderFrame.grid_columnconfigure(0, weight=1)

def requestBulkDownload():
    errors = BMD.BulkMediaDownload(FolderFrame.getPath(), CSVPath=CSVFrame.getPath())
    print(errors)


downloadBttn = ttk.Button(app, text="Download", command=requestBulkDownload)
downloadBttn.grid(row=3,column=0)

app.mainloop()