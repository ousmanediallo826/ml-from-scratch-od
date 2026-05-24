from dataclasses import dataclass, field
from descriptors import StartingRating
@dataclass
class Book:
    title: str
    author: str
    pages: int
    status: str = "unread"
    rating: int = 0
    notes: str = ""

    StarRating = StartingRating()
