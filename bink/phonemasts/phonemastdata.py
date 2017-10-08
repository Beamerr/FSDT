import csv

def open_csv
    with open('MobilePhoneMasts.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            print(row)