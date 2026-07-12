
from pydantic import BaseModel, Field, ValidationError

class Student(BaseModel):
    name: str = Field(min_length=1)
    score: int = Field(ge=1, le=100)  # Score must be between 0 and 100


# Student data
student_data = [
    {"name": "Funom", "score": 109},
    {"name": "Ola", "score": 92},
    {"name": "Funom", "score": 66},
    {"name": "Peter", "score": 88},
    {"name": "Tirnom", "score": 65}
]

# Validate data
students = []

for data in student_data:
    try:
        students.append(Student(**data))
    except ValidationError as e:
        print(f"Invalid student record:\n{e}")

# Find highest and lowest scores
highest = max(students, key=lambda student: student.score, default=None)
lowest = min(students, key=lambda student: student.score, default=None)

if highest is None:
    print("No valid student records available.")
else:
    print(f"Highest Score: {highest.name} - {highest.score}")
    print(f"Lowest Score: {lowest.name} - {lowest.score}")