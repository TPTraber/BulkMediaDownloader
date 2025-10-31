from streetlevel import streetview
import csv
import requests
import time


class BulkMediaDownloader(): 

    @staticmethod
    def PanoDownload(url, path):
        id = url.split("!1s")[1].split("!2e")[0]
        print(f"Downloading Pano {id} to {path}.jpg")
        pano = streetview.find_panorama_by_id(id)
        streetview.download_panorama(pano, f"{path}.jpg")

    @staticmethod
    def DownloadImage(url, path):
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        try:
            print(f"Downloading image to {path}.jpg")
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
            with open(path + ".jpg", "wb") as f:
                f.write(response.content)
            print("Image downloaded successfully!")
        except requests.exceptions.HTTPError as e:
            print(f"HTTP Error: {e}")
        except requests.exceptions.RequestException as e:
            print(f"Request Error: {e}")

    @staticmethod
    def __URLHandler(url, outputPath, name, count=0):
        if url.__contains__("maps"):
            BulkMediaDownloader.PanoDownload(url, outputPath + f"/{name}_{count}")
        elif url.__contains__(".jpg") or url.__contains__(".png"):
            BulkMediaDownloader.DownloadImage(url, outputPath + f"/{name}_{count}")
        else:
            raise Exception("Unknown URL Type")

    
    @staticmethod
    def SingleMediaDownload(outputPath, URL, name):
        errors = []

        try:
            BulkMediaDownloader.__URLHandler(URL, outputPath, name)
        except Exception as e:
            # A general exception handler for any other unexpected errors
            print(f"An unexpected error occurred: {e}")
            errors.append(name)
        
        return errors


    @staticmethod
    def BulkMediaDownload(outputPath:str, CSVPath:str=None, urlList:list=None , ProgressLabel=None, ProgressBar=None, Root=None, WaitTime:float=None):

        if CSVPath == None and urlList == None:
            raise Exception("No url input")

        if CSVPath != None:
            with open(CSVPath, 'r', newline='') as file:
                csv_num = csv.reader(file)
                if (ProgressBar != None): ProgressBar.config(maximum=len(list(csv_num)))

            with open(CSVPath, 'r', newline='') as file:
                csv_reader = csv.reader(file)
                errors = []

                val = 0
                
                for row in csv_reader:
                    if row[0] == "":
                        name_count += 1
                    else:
                        name = row[0]
                        name_count = 0
                    url = row[1]

                    try:
                       if (ProgressLabel != None): ProgressLabel.config(text=f"Downloading: {name}_{name_count}")
                       BulkMediaDownloader.__URLHandler(url, outputPath, name, count=name_count)

                    except Exception as e:
                        # A general exception handler for any other unexpected errors
                        print(f"An unexpected error occurred: {e}")
                        errors.append(outputPath + f"/{name}_{name_count}")
                    val += 1

                    #If tkinter elements present, update them
                    if (ProgressBar != None): ProgressBar.config(value=val)
                    if(Root != None): Root.update_idletasks()
                    if (WaitTime != None): time.sleep(WaitTime)
        elif urlList != None:
                count = 0
                for url in urlList:
                    try:
                        if url.__contains__("maps"):
                            BulkMediaDownloader.PanoDownload(url, outputPath + f"/{name}_{count}")
                        elif url.__contains__(".jpg") or url.__contains__(".png"):
                            BulkMediaDownloader.DownloadImage(url, outputPath + f"/{name}_{count}")

                    except Exception as e:
                        # A general exception handler for any other unexpected errors
                        print(f"An unexpected error occurred: {e}")
                        errors.append(outputPath + f"/{name}_{count}")
                    count += 1
                    val += 1

                    #If tkinter elements present, update them
                    if (ProgressBar != None): ProgressBar.config(value=val)
                    if(Root != None): Root.update_idletasks()
                    if (WaitTime != None): time.sleep(WaitTime)

        return errors
        
    