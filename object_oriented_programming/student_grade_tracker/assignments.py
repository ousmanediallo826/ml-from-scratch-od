from dataclasses import dataclass
from descriptors import ValidScores
@dataclass
class Assignment:
    title: str
    subject: str
    score: float
    max_score: float = 100.0
    due_date: str = ""

    score = ValidScores()



    @property
    def grade_letter(self):
        if self.score >= 90 and self.score <= 100:
            return 'A'
        elif self.score >= 80 and self.score <= 89:
            return 'B'
        elif self.score >= 70 and self.score <= 79:
            return 'C'
        elif self.score >= 60 and self.score <= 69:
            return 'D'
        else:
            return 'F'
    def __str__(self):
        return f"{self.title} - {self.subject}: {self.score}/{self.max_score} ({self.grade_letter})"
