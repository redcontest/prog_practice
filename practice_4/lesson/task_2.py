class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        print(f"{self.author} - {self.title} ({self.year})")


class Ebook(Book):
    def __init__(self, title: str, author: str, year: int, format: str):
        super().__init__(title, author, year)
        self.format = format

    def info(self):
        print(f"{self.author} - {self.title} ({self.year}).\n"
              f"Тип книги - {self.format}")
