# Exercise 1: School Grading Sistem

"""
     Create a function that takes a student's name and their scores in different subjects as input.
    The function calculates the average score and prints the student's name, average, and a message indicating whether the student passed the exam (average >= 60) or failed.
    Create a for loop to iterate over a list of students and scores, calling the function for each student.
"""


def grading_system(name: str, votes: dict) -> dict:

    print(f"Student's name: {name.title()} ")

    for subject, vote in votes.items():
        print(f"{subject}: {vote}")

    average_score: float = sum(votes.values()) / len(votes.values())

    print(f"Average score: {average_score:.2f}")

    match average_score:

        case _ if average_score < 60:
            print("Sorry, u didn't pass the exam.\n")

        case _:
            print("Congratulation! You passed the exam!.\n")


all_students: list[tuple[str, dict]] = [
    ("alessio", {"python": 89, "rust": 56, "java": 77}),
    ("elisa", {"python": 45, "rust": 99, "java": 34}),
    ("delia", {"python": 34, "rust": 77, "java": 100}),
]

for name, votes in all_students:
    grading_system(name, votes)
