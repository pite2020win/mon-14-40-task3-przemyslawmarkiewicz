# Class diary
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
#
# Please, use your imagination and create more functionalities.
# Your project should be able to handle entire school(s?).
# If you have enough courage and time, try storing (reading/writing)
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface (might be text-like).
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to your github repository. 
#
#Delete these comments before commit!
#Good luck.
import pandas as pd


class GradeBook:
    def __init__(self, subject, group_id, student_list=None):
        self.subject = subject
        self.sroup_id = group_id
        

    def add_students(self, students):
        self.students = students

    def add_grade_category(self):
        pass

    def add_grade(self):
        pass

    def add_attendance(self):
        pass

    def class_average(self):
        pass


if __name__ == "__main__":

    df = pd.read_csv("students.csv")
    students = df.to_dict(orient='records')

    gradebook_1 = GradeBook("Math", 1)
    gradebook_1.add_students(students)

    print(gradebook_1.students)

