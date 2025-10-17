from abc import ABC, abstractmethod


class Printable(ABC):
    @abstractmethod
    def print_info(self):
        pass


class Book(Printable):
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def print_info(self):
        print(f"{self.author} - {self.title} ({self.year})")
