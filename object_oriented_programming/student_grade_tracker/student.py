from python_basics.exercises import average
from assignments import Assignment

class Student:
    school = "Python High School"
    _total_students = 0


    def __ini__(self, name, grade):
        self.name = name
        self.grade = grade
        self._assignments = []

        Student._total_students += 1


    @property
    def average(self):
        if not self._assignments:
            return 0.0
        scores = [a.score for a in self._assignments]
        return round(sum(scores) / len(scores), 2)

    @property
    def letter_grade(self):
        avg = self.average
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        return 'F'

    @property
    def passed(self):
        return self.average >= 60


    def add_assignment(self, assignment: Assignment) -> "Student":
        if not isinstance(assignment, Assignment):
            raise TypeError("Only Assignment instances can be added.")
        self._assignments.append(assignment)
        return self   # enables chaining

    def best_score(self) -> Assignment:
        if not self._assignments:
            return None
        return max(self._assignments, key=lambda a: a.score)

    def worst_score(self) -> Assignment:
        if not self._assignments:
            return None
        return min(self._assignments, key=lambda a: a.score)

    def assignments_by_subject(self, subject: str) -> list:
        return [a for a in self._assignments if a.subject.lower() == subject.lower()]

    def __str__(self) -> str:
        return f"{self.name} ({self.grade}) — avg: {self.average} ({self.letter_grade})"

    def __repr__(self) -> str:
        return f"Student(name={self.name!r}, grade={self.grade!r}, assignments={len(self)})"

    def __len__(self) -> int:
        return len(self._assignments)

    def __lt__(self, other: "Student") -> bool:
        if not isinstance(other, Student):
            return NotImplemented
        return self.average < other.average

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Student):
            return NotImplemented
        return self.name == other.name and self.grade == other.grade

    def __bool__(self) -> bool:
        return self.passed




class HonorsStudent(Student):


    gpa_scale = 4.0

    def __init__(self, name: str, grade: str):
        super().__init__(name, grade)   # run Student.__init__ first
        self.weighted_bonus = 0.5       # instance attribute unique to HonorsStudent


    @property
    def gpa(self) -> float:
        return round((self.average / 100) * self.gpa_scale, 2)

    def __str__(self) -> str:
        base = super().__str__()   # reuse Student's version, then extend it
        return f"{base} [Honors] — GPA: {self.gpa}"






