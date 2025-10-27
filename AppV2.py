import tkinter as Tkn
from tkinter import ttk
from tkinter import filedialog
from BulkMediaDownload import BulkMediaDownloader as BMD

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
    
class CSVFileUploadFrame(ttk.Frame): 
    def __init__(self, master):
        super().__init__(master)
        self.path = Tkn.StringVar()

        upperFrame = ttk.Frame(self)
        lowerFrame = ttk.Frame(self)
        upperFrame.grid(column=0, row=0)
        lowerFrame.grid(column=0, row=1)

        textBox = ttk.Entry(lowerFrame, textvariable= self.path)
        textBox.grid(column=0, row=0)

        subtitle = ttk.Label(upperFrame, text="Select CSV:")
        chooseButton  = FileSelectButton(upperFrame, self.path, "file", text="Choose File")
        subtitle.grid(column=0, row=0)
        chooseButton.grid(column=1, row=0)
    
    def getPath(self):
        return self.path.get()

class FolderUploadFrame(ttk.Frame): 
    def __init__(self, master):
        super().__init__(master)
        self.path = Tkn.StringVar()

        upperFrame = ttk.Frame(self)
        lowerFrame = ttk.Frame(self)
        upperFrame.grid(column=0, row=0)
        lowerFrame.grid_columnconfigure(0, weight=1)
        lowerFrame.grid(column=0, row=1)
        lowerFrame.grid_columnconfigure(0, weight=1)

        textBox = ttk.Entry(lowerFrame, textvariable= self.path)
        textBox.grid(column=0, row=0)

        subtitle = ttk.Label(upperFrame, text="Select Ouput Folder:")
        chooseButton  = FileSelectButton(upperFrame, self.path, "folder", text="Choose Folder")
        subtitle.grid(column=0, row=0)
        chooseButton.grid(column=1, row=0)

    def getPath(self):
        return self.path.get()


app = Tkn.Tk()

app.minsize(width=400, height=600)

app.title("BulkMediaDownloader")

title = Tkn.Label(app, text="BulkMediaDownloader")
title.grid(row=0,column=0)

bulkDownloadFrame = ttk.Frame(app)
bulkDownloadFrame.grid(column=0, row=1)

CSVFrame = CSVFileUploadFrame(bulkDownloadFrame)
CSVFrame.grid(column=0, row=1)

FolderFrame = FolderUploadFrame(bulkDownloadFrame)
FolderFrame.grid(column=0, row=2)

# Configure the root window's row and column to expand
app.grid_columnconfigure(0, weight=1)

# Configure the frame's row and column to expand
CSVFrame.grid_columnconfigure(0, weight=1)
FolderFrame.grid_columnconfigure(0, weight=1)

def requestBulkDownload():
    errors = BMD.BulkMediaDownload(FolderFrame.getPath(), CSVPath=CSVFrame.getPath())
    print(errors)


downloadBttn = Tkn.Button(app, text="Download", command=requestBulkDownload)
downloadBttn.grid(row=3,column=0)

app.mainloop()