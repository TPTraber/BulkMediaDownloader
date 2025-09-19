import csv

with open('data.csv', 'r', newline='') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        url = row[1]
        if url.__contains__("maps"):
            print(url.split("!1s")[1].split("!2e")[0])