import csv

def save_to_csv(self):
    with open("jobs.csv", mode="a", newline='') as file:
        fieldnames = ["title", "location", "url", "description", "qualifications"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow({
            'title': self.title, 
            'url': self.url, 
            'location': self.location,
            'description': self.description,
            'qualifications': self.qualifications
        })