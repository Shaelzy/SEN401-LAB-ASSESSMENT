# app.py

from students import students
from Utils.helpers import highest_score, lowest_score, average_score


def main():
    print("===== STUDENT REPORT =====\n")

    print("Student Records")
    for student in students:
        print(f"{student['name']} - {student['score']}")

    highest = highest_score(students)
    lowest = lowest_score(students)
    average = average_score(students)

    print("\nSummary")
    print(f"Highest Score: {highest['name']} ({highest['score']})")
    print(f"Lowest Score: {lowest['name']} ({lowest['score']})")
    print(f"Average Score: {average:.2f}")


if __name__ == "__main__":
    main()
