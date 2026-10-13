# very first lines of the app, before any other imports
import os, certifi

try:
    import truststore
    truststore.inject_into_ssl()   # trust the macOS keychain (covers corporate CAs)
except Exception as e:
    print("truststore unavailable, falling back to certifi:", e)
    os.environ.setdefault("SSL_CERT_FILE", certifi.where())

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from BulkMediaDownload import BulkMediaDownloader as BMD

import sv_ttk
import darkdetect
import webbrowser

version = "v1.0.4"

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

def completePopup(errors):

    #Test Errors
    #errors = ["test1", "blahblah", "really really bad error"]
    #for i in range(0,20):
            #errors.append(i)

    win = tk.Toplevel()
    win.title("Download Complete")
    win.grid_columnconfigure(0, weight=1)

    title = ttk.Label(win, text="Download Complete!", font=("Arial", 14, "bold"))
    title.grid(row=0, column=0,padx=20,pady=10)

    label = ttk.Label(win, text="Completed with " + str(len(errors)) + " errors:")
    label.grid(row=1,column=0, pady=10)

    curRow = 2
    if(len(errors) != 0):
        frame = ttk.Frame(win, borderwidth=1, relief="solid")

        eList = tk.Listbox(frame, height=5)
        s = ttk.Scrollbar(frame, orient=VERTICAL, command=eList.yview)
        s.grid(row=0,column=1, sticky="ns")
        eList['yscrollcommand'] = s.set
        for error in errors:
            eList.insert('end', error)
        eList.grid(row=0, column=0, sticky="nsew")

        frame.grid(row=curRow, column=0, pady=5, padx=20, sticky="nsew")
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(0, weight=1)

        win.grid_rowconfigure(curRow, weight=1)
        curRow += 1

    closeButton = ttk.Button(win, text="Great!", command=win.destroy)
    closeButton.grid(row = curRow, column=0, pady=20,padx=20)
    
class PathSelectFrame(ttk.Frame): 
    def __init__(self, master, type):
        super().__init__(master)

        self.path = tk.StringVar()

        self.grid_rowconfigure(0, weight = 1, pad=20)

        upperFrame = ttk.Frame(self)
        lowerFrame = ttk.Frame(self)
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
        elif (type.lower() == "url"):
                    subtitle = ttk.Label(upperFrame, text="URL List:")
                    chooseButton  = FileSelectButton(upperFrame, self.path, "folder", text="Choose Folder")
        else:
            subtitle = ttk.Label(upperFrame, text="Select File:")
            chooseButton  = FileSelectButton(upperFrame, self.path, "file", text="Choose File")
            
        subtitle.grid(column=0, row=0, sticky="w")
        if(type.lower() !="url"):
            chooseButton.grid(column=1, row=0, padx=(5,0))
        
    def getPath(self):
        return self.path.get()

root = tk.Tk()

root.minsize(width=400, height=600)

root.title("BulkMediaDownloader")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

app = ttk.Frame(root)
app.grid(row=0,column=0, sticky="nsew")

# Set the initial theme

sv_ttk.set_theme(darkdetect.theme())

app.grid_columnconfigure(0, weight=1)

title = ttk.Label(app, text="BulkMediaDownloader", font=("Arial", 16, "bold"))
title.grid(row=0,column=0, sticky="we", padx=20,pady=10)
app.grid_columnconfigure(0, weight=1)

notebook = ttk.Notebook(app,)
notebook.grid(column=0, row=1, sticky="we", padx=20,pady=10)

## BULK DOWNLOAD FRAME SETUP

bulkDownloadFrame = ttk.Frame(notebook, borderwidth=1, relief="solid")
bulkDownloadFrame.grid(column=0, row=0, sticky="nswe")

notebook.add(bulkDownloadFrame, text="CSV BulkDownload")

CSVFrame = PathSelectFrame(bulkDownloadFrame, "CSV")
CSVFrame.grid(column=0, row=0, sticky="we",padx=10, pady=5)

FolderFrame = PathSelectFrame(bulkDownloadFrame, "folder")
FolderFrame.grid(column=0, row=1, sticky="we", pady=20,padx=10)

bulkDownloadFrame.grid_columnconfigure(0, weight=1,)

CSVFrame.grid_columnconfigure(0, weight=1)
FolderFrame.grid_columnconfigure(0, weight=1)

progressBar = ttk.Progressbar(bulkDownloadFrame, value=0, maximum=100, mode='determinate', length=150)
progressBar.grid(row=3, column=0, pady=20, sticky="n")

progressLabel = ttk.Label(bulkDownloadFrame, text="")
progressLabel.grid(row=4, column=0)

def requestBulkCSVDownload():
    errors = BMD.BulkMediaDownload(FolderFrame.getPath(), CSVPath=CSVFrame.getPath(), ProgressLabel=progressLabel, ProgressBar=progressBar, Root=root, WaitTime=0.1)
    print(errors)
    completePopup(errors)

downloadBttn = ttk.Button(bulkDownloadFrame, text="Download", command=requestBulkCSVDownload)
downloadBttn.grid(row=2,column=0)

# ## SINGLE DOWNLOAD FRAME SETUP

URLDownloadFrame = ttk.Frame(notebook, borderwidth=1, relief="solid")
URLDownloadFrame.grid(column=0, row=0, sticky="nswe")

notebook.add(URLDownloadFrame, text="URL")

urlFrame = PathSelectFrame(URLDownloadFrame, "url")
urlFrame.grid(column=0, row=0, sticky="we",padx=10, pady=5)

FolderFrameURL = PathSelectFrame(URLDownloadFrame, "folder")
FolderFrameURL.grid(column=0, row=1, sticky="we", pady=20,padx=10)


URLDownloadFrame.grid_columnconfigure(0, weight=1,)

urlFrame.grid_columnconfigure(0, weight=1)
FolderFrameURL.grid_columnconfigure(0, weight=1)

progressBarURL = ttk.Progressbar(URLDownloadFrame, value=0, maximum=100, mode='determinate', length=150)
progressBarURL.grid(row=3, column=0, pady=20, sticky="n")

progressLabelURL = ttk.Label(URLDownloadFrame, text="")
progressLabelURL.grid(row=4, column=0)

def requestURLDownload():
    errors = BMD.BulkMediaDownload(FolderFrameURL.getPath(), urlList=urlFrame.getPath(), ProgressLabel=progressLabelURL, ProgressBar=progressBarURL, Root=root, WaitTime=0.1)
    print(errors)
    completePopup(errors)

downloadBttnURL = ttk.Button(URLDownloadFrame, text="Download", command=requestURLDownload)
downloadBttnURL.grid(row=2,column=0)


## INFO FRAME SETUP
infoFrame = ttk.Frame(notebook, padding=20, borderwidth=1, relief="solid")
infoFrame.grid_columnconfigure(0, weight=1)

infoTitle = ttk.Label(infoFrame, text="App Info:", font=("Arial", 14, "bold"))
infoTitle.grid(row=0, column=0, sticky="w")

verLabel = ttk.Label(infoFrame, text="Version: " + version)
verLabel.grid(row=1,column=0, pady=10, sticky="w")

repoBtn = ttk.Button(infoFrame, text="Github Repo", command=lambda: webbrowser.open("https://github.com/TPTraber/BulkMediaDownloader"))
repoBtn.grid(row=2, column=0, sticky="w")

notebook.add(infoFrame, text="Info")



app.mainloop()