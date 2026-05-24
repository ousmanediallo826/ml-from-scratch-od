from exercise import *

class Workout:
    gym_name = "IronPit GYM"
    _total_workout = 0


    def __init__(self, athlete, date):
        self.athlete = athlete
        self.date = date
        self._exercises = []

    @property
    def total_volume(self) -> float:
        return round(sum(ex.volume for ex in self._exercises), 2)

    @property
    def exercise_count(self) -> int:
        return len(self._exercises)
    @property
    def exercise_category(self):
        return {ex.category for ex in self._exercises}
    @property
    def heaviest(self):
        if not self._exercises:
            return None
        return max(self._exercises, key=lambda ex: ex.weight)



    def __str__(self) -> str:
        return f"{self.gym_name} | {self.athlete} | {self.date} | {self.exercise_count} exercises"

    def __len__(self):
        return len(self._exercises)

    def __contains__(self, name: str) -> bool:
        return any(ex.name == name for ex in self._exercises)

    def __iter__(self):
        return iter(self._exercises)

    def __add__(self, other: "Workout") -> "Workout":
        if not isinstance(other, Workout):
            return NotImplemented
        merged = Workout(
            athlete=f"{self.athlete} & {other.athlete}",
            date=self.date
        )
        for ex in self._exercises:
            merged.add_exercise(ex)
        for ex in other._exercises:
            merged.add_exercise(ex)
        return merged

    def add_exercise(self, exercise):
        if not isinstance(exercise, Exercise):
            raise TypeError(
                "Only Exercise can be added to a WorkoutTracker"
            )
        self._exercises.append(exercise)
        return self

    def remove_exercise(self, exercise):
        if exercise not in self._exercises:
            raise KeyError(
                "Exercise not in WorkoutTracker"
            )
        self._exercises.remove(exercise)

    def filter_by_category(self, category: str) -> list:
        return [ex for ex in self._exercises if ex.category.lower() == category.lower()]



class PersonalRecord(Workout):
    pr_label = "🏆 PR"
    def __init__(self, athlete, date, goal: str = ""):
        super().__init__(athlete, date)
        self.goal = goal
        self._records = {}

    @property
    def prs(self) -> list:
        return [ex for ex in self._exercises if self._records.get(ex.name) == ex.weight]

    def log_pr(self, exercise) -> bool:
        current_best = self._records.get(exercise.name, 0)
        if exercise.weight > current_best:
            self._records[exercise.name] = exercise.weight
            return True  # it's a new PR
        return False

    def __str__(self) -> str:
        base = super().__str__()
        return f"{base} | Goal: {self.goal}"

