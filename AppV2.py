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
    
class UploadFrame(ttk.Frame): 
    def __init__(self, master, type):
        super().__init__(master)

        self.path = Tkn.StringVar()

        upperFrame = ttk.Frame(self)
        lowerFrame = ttk.Frame(self)
        upperFrame.grid(column=0, row=0)
        lowerFrame.grid(column=0, row=1)

        textBox = ttk.Entry(lowerFrame, textvariable= self.path)
        textBox.grid(column=0, row=0)

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

app = ttk.Frame(root)
app.pack(fill="both", expand=True)

# Set the initial theme
root.tk.call("source", "azure.tcl")
root.tk.call("set_theme", "light")

title = ttk.Label(app, text="BulkMediaDownloader")
title.grid(row=0,column=0)

bulkDownloadFrame = ttk.Frame(app)
bulkDownloadFrame.grid(column=0, row=1)

CSVFrame = UploadFrame(bulkDownloadFrame, "CSV")
CSVFrame.grid(column=0, row=1)

FolderFrame = UploadFrame(bulkDownloadFrame, "folder")
FolderFrame.grid(column=0, row=2)

# Configure the root window's row and column to expand
app.grid_columnconfigure(0, weight=1,pad=20)
for index in [0,1,2]:
    app.grid_rowconfigure(index, pad=20)

# Configure the frame's row and column to expand
CSVFrame.grid_columnconfigure(0, weight=1)
FolderFrame.grid_columnconfigure(0, weight=1)

def requestBulkDownload():
    errors = BMD.BulkMediaDownload(FolderFrame.getPath(), CSVPath=CSVFrame.getPath())
    print(errors)


downloadBttn = ttk.Button(app, text="Download", command=requestBulkDownload)
downloadBttn.grid(row=3,column=0)

app.mainloop()