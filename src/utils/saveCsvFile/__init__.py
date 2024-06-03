import csv
from .csvData import save_to_csv

with open("jobs.csv", mode="w") as file:
    fieldnames = ["title", "location", "url", "description", "qualifications"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

save_to_csv