"""
     Create a function that takes a student's name and their scores in different subjects as input.
    The function calculates the average score and prints the student's name, average, and a message indicating whether the student passed the exam (average >= 60) or failed.
    Create a for loop to iterate over a list of students and scores, calling the function for each student.
"""


def grading_system(name: str, votes: dict) -> dict:
    print(f"Student: {name}")

    for subject, vote in votes.items():
        print(f"{subject}: {vote}")

    average_vote: float = sum(votes.values()) / len(votes)
    print(f"The average for the student {name} is {average_vote}")

    if average_vote >= 60:
        print(f"Congratulation {name.title()} you passed the exam with an average score of {average_vote}.")
    else:
        print("We are sorry to tell you that you didn't pass the exam.")
    
    #  I need to finish this part:  Create a for loop to iterate over a list of students and scores, calling the function for each student.


grading_system("Mario", {"Math": 70, "History": 80})

