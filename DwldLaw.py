class DwldLaw:

    """Initialise le constructeur et apporte des éléments nécéssaire si besoin"""
    def __init__(self, **kwargs):
        self.fetchedData = {
            ("https://docs.google.com/document/d/1b66kpyNnqtgMj9hWKaR2pMIX-90QuE9DCRnbXxqaFCs",
             "Journal Officiel dit « Code Civil » de la République Participative du Dibistan.txt"),
            ("https://docs.google.com/document/d/1qBbN03kcRAcsEYjo3_p51cOzaLZYi5py4NQ_xCOoi7g",
             "Première Constitution du 09_01_2022.txt")
        }
        self.unfechedData = []
        for row in kwargs['cleanedData']:
            urls = self.findURLs(row[1])
            if urls != None or urls==[]:
                for url in urls:
                    if self.isFetched(url):
                        pass
                    else:
                        self.unfechedData.append(url)
            urls = self.findURLs(row[2])
            if urls != None or urls == []:
                for url in urls:
                    if self.isFetched(url):
                        pass
                    else:
                        self.unfechedData.append(url)
        for anFetchedData in self.fetchedData:
            noLine = 1
            with open("sourceDwnld/"+anFetchedData[1], 'r') as file:
                for line in file:
                    urls = self.findURLs(line)
                    if urls != None or urls == []:
                        for url in urls:
                            if self.isFetched(url):
                                print(line)
                            else:
                                self.unfechedData.append(url)
                                print(line)



    def isFetched(self, url: str):
        for entry in self.fetchedData:
            if entry[0] == url:
                return True
        return False

    def findURLs(self, dataToParse: str):
        import re
        pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        return re.findall(pattern, dataToParse)

    def data(self):
        return self.fetchedData, self.unfechedData
