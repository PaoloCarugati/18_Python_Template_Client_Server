class record:
    id = 0
    artist = ""
    title = ""
    year = 0
    company = ""
    
    def __init__(self, _id, _artist, _title, _year, _company):
        self.id = _id
        self.artist = _artist
        self.title = _title
        self.year = _year
        self.company = _company
