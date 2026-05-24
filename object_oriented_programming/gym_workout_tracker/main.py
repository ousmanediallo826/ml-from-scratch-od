from exercise import *
from tracker import *


session = PersonalRecord("Alice", "2024-01-15", goal="hit 100kg bench")

session.add_exercise(Exercise("Bench Press", "push",  4, 10, 80.0)) \
       .add_exercise(Exercise("Pull Ups",    "pull",  3, 8,  0.0)) \
       .add_exercise(Exercise("Squats",      "legs",  4, 8,  100.0)) \
       .add_exercise(Exercise("Bicep Curl",  "pull",  3, 12, 15.0)) \
       .add_exercise(Exercise("Plank",       "cardio",3, 1,  0.0))

print(session)                        # __str__
print(len(session))                   # __len__
print("Squats" in session)            # __contains__
print(session.total_volume)           # property
print(session.heaviest)               # property
print(session.categories)            # property

for ex in session:                    # __iter__
    print(ex)

# Merge two workouts
morning = Workout("Alice", "2024-01-15")
morning.add_exercise(Exercise("Running", "cardio", 1, 1, 0.0))
combined = session + morning          # __add__
print(len(combined))                  # should be 6

# Descriptor validation
Exercise("Bad", "push", 1, 10, 80)  # should raise ValueError
Exercise("Bad", "push", 4, 10, 20)  # should raise ValueError

# PR tracking
session.log_pr(session._exercises[0])
print(session.prs)