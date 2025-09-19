from streetlevel import streetview
import csv


name = ""

count = 0

with open('data.csv', 'r', newline='') as file:
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
            streetview.download_panorama(pano, f"{name}_{count}.jpg")



