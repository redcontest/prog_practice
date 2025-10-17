class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        print(f"{self.author} - {self.title} ({self.year})")
