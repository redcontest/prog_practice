from datetime import datetime


class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    @classmethod
    def from_string(cls, data: str):
        title, author, year = data.split(';')
        return cls(title, author, int(year))

    @property
    def age(self) -> int:
        return datetime.now().year - self.year

    @age.setter
    def age(self, value: int):
        self.year = datetime.now().year - value

    def info(self):
        print(f"{self.author} - {self.title} ({self.year})")

    def __str__(self) -> str:
        return f"{self.author} - {self.title} ({self.year})"

    def __eq__(self, other: any) -> bool:
        return isinstance(other, Book) and self.title == other.title
