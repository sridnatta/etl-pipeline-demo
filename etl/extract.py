import csv

def extract_data(path="data/imput.csv"):
    rows = []
    with open(path,newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)

    ## test feature extract 1 - testing rebase
    # adding additional changes to extract
    return rows