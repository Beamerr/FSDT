import csv

def open_csv(data):
    with open(data, 'r') as csvfile:
        data = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in data:
            return data



data = "MobilePhoneMasts.csv"
open_csv(data)