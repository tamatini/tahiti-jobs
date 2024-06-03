class job:
    def __init__(self, title, url, location, description, qualifications):
        self.title = title
        self.url = url
        self.location = location
        self.description = description
        self.qualifications = qualifications
    
    def __str__(self):
        return f"{self.title} - {self.location} - {self.url} - {self.description} - {self.qualifications}"

    def save(self):
        import src.utils.saveCsvFile as saveCsvFile
        saveCsvFile.csvData.save_to_csv(self)