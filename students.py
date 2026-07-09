from dataclasses import dataclass

@dataclass
class Student:
    name: str
    score: float

# Initial dataset
STUDENTS_DATA = [
    Student(name="John", score=90.5),
    Student(name="Mary", score=70.0),
    Student(name="Grace", score=85.4),
    Student(name="Wale", score=95.0),
    Student(name="Funom", score=71.0),
] 