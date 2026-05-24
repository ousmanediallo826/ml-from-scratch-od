from dataclasses import dataclass
from descriptors import PositiveInt, WeightValue

@dataclass
class Exercise:
    name: str
    category: str          # "PUSH" | "PULL" | "LEGS" | "CARDIO"
    sets: int
    reps: int
    weight: float
    note: str = ""

    sets = PositiveInt()
    reps = PositiveInt()
    weight = WeightValue()

    def __post_init__(self):
        self.sets = self.sets
        self.reps = self.reps
        self.weight = self.weight
    @property
    def volume(self) -> float:
        return self.sets * self.reps * self.weight


    def __str__(self) -> str:
        return f"{self.name} — {self.sets}x{self.reps} @ {self.weight}kg (volume: {self.volume}kg)"