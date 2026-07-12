# utils/helpers.py

def highest_score(students):
    """Return the student with the highest score."""
    return max(students, key=lambda student: student["score"])


def lowest_score(students):
    """Return the student with the lowest score."""
    return min(students, key=lambda student: student["score"])


def average_score(students):
    """Return the average score."""
    total = sum(student["score"] for student in students)
    return total / len(students)

def highest_score(students):
    if not students:
        return None
    return max(students, key=lambda student: student["score"])


def lowest_score(students):
    if not students:
        return None
    return min(students, key=lambda student: student["score"])
    
