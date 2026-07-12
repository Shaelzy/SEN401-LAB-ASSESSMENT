


from students import students

ranked_students = sorted(students, key=lambda s: s.score, reverse=True)

print("\nStudent Ranking")
for i, student in enumerate(ranked_students, start=1):
    print(f"{i}. {student.name} - {student.score}")