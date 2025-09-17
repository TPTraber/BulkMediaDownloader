import customtkinter as CTkin
from streetlevel import streetview
import csv
from tkinter import filedialog

def updateLabel(label, text):
    label._text = text

def BulkPanoDownload(CSVPath, outputPath, bar):
    with open(CSVPath, 'r', newline='') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row[0] == "":
                count += 1
            else:
                name = row[0]
                count = 0
            url = row[1]

            if url.__contains__("maps"):
                id = url.split("!1s")[1].split("!2e")[0]
                print(f"Downloading {id} to {name}_{count}.jpg")
                pano = streetview.find_panorama_by_id(id)
                streetview.download_panorama(pano, f"{outputPath}/{name}_{count}.jpg")


class FileUploadFrame(CTkin.CTkFrame):
    def __init__(self, master, title, type):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.title = title
        self.title = CTkin.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.pack()
        self.type = type
        #self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")
        self.path = ""
        

        def ChoosePath(event=None):
            if type == "file":
                self.path = filedialog.askopenfilename()
            else:
                self.path = filedialog.askdirectory()
            pathLabel.configure(text="Selected: " + self.path)
            print('Selected:', self.path)

        button = CTkin.CTkButton(self, text="Choose File", command=ChoosePath)
        #button.grid(row=0, column=1, padx=20, pady=20)
        button.pack()

        pathLabel = CTkin.CTkLabel(self, text="Selected: ")
        pathLabel.pack()
        


app = CTkin.CTk()

app.title("BulkMediaDownloader")

title = CTkin.CTkLabel(app, text="BulkMediaDownloader", font=CTkin.CTkFont(size=10))
#title.grid(row=0,column=0)

CSVFrame = FileUploadFrame(app, "Step 1: Choose CSV", "file")
#CSVFrame.grid(row=1, column=0)

outputFrame = FileUploadFrame(app, "Step 2: Choose Output Folder", "Folder")
#outputFrame.grid(row=2, column=0)

downloadBttn = CTkin.CTkButton(app, text="Download")
#downloadBttn.grid(row=3,column=0)

CSVFrame.pack(padx=10,pady=5)
outputFrame.pack(padx=10,pady=5)
downloadBttn.pack(padx=10,pady=5)

bar = CTkin.CTkProgressBar(app, mode="determinate")
#bar.grid(row=4, column=0)

bar.pack()

app.mainloop()

