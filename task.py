from dataclasses import dataclass
import json
from statistics import mean
import logging

logging.basicConfig(filename='data.log', level=logging.DEBUG)


@dataclass
class GradeBook:
    school_name: str
    students: list

    def add_student(self, name, surname, class_name):
        student_data = {
            "first_name": name,
            "last_name": surname,
            "class_name": class_name,
            "grades": [],
            "attendance": []
        }
        self.students.append(student_data)

    def get_student(self, name, surname):
        for stud in self.students:
            if stud["first_name"] == name and stud["last_name"] == surname:
                return stud

    def get_subject_grades(self, stud_name, stud_surname, subject):
        student = self.get_student(stud_name, stud_surname)
        grades = student["grades"]
        for grade in grades:
            if grade["subject"] == subject:
                return grade
            

    def add_grade(self, stud_name, stud_surname, subject, grade):
        grades = self.get_subject_grades(stud_name, stud_surname, subject)

        grades["grades"].append(grade)

    def add_attendance(self, stud_name, stud_surname, date, was_present=True):
        student = self.get_student(stud_name, stud_surname)
        attendance_dict = {
            "date": date,
            "was_present": was_present
        }
        student["attendance"].append(attendance_dict)

    def student_class_average(self, name, surname, subject):
        grades = self.get_subject_grades(name, surname, subject)
        return mean(grades["grades"])

    def student_average(self, name, surname):
        student = self.get_student(name, surname)
        all_subjects_grades = student["grades"]
        grade_list = [grade["grades"] for grade in all_subjects_grades]
        subjects_average = map(lambda grades: mean(grades), grade_list)
        return mean(list(subjects_average))

    def class_average(self, class_name, subject):
        grades_list = []
        for stud in self.students:
            if stud["class_name"] == class_name:
                grades_list.append(self.get_subject_grades(stud["first_name"], stud["last_name"], subject))
        grades = [grade["grades"] for grade in grades_list]
        each_stud_average = map(lambda grades: mean(grades), grades)
        return mean(list(each_stud_average))

    def student_attendance(self, name, surname):
        student = self.get_student(name, surname)
        return student["attendance"]


if __name__ == "__main__":

    f = open("students.json")
    students = json.load(f)
    gradebook1 = GradeBook("Good School", students)

    logging.info("Average math scores of students from 3a: "
    f"{gradebook1.class_average('3a', 'math')}")

    tom_smith = gradebook1.get_student("Tom", "Smith")
    logging.info(f"example student: {tom_smith}")
    gradebook1.add_attendance("Tom", "Smith", "13.04.2020")
    gradebook1.add_attendance("Tom", "Smith", "14.04.2020")
    gradebook1.add_attendance("Tom", "Smith", "15.04.2020", False)


    logging.info(f"Tom smith attendance: "
    f"{gradebook1.student_attendance('Tom', 'Smith')}")

    logging.info(f"Average math grades of tom smith: "
        f"{gradebook1.student_class_average('Tom', 'Smith', 'math')}")
    gradebook1.add_grade("Tom", "Smith", "math", 6)
    logging.info(f"Average math grades of tom smith after adding new grade: " 
        f"{gradebook1.student_class_average('Tom', 'Smith', 'math')}")

    logging.info(f"Average Tom Smith's grades: "
    f"{gradebook1.student_average('Tom', 'Smith')}")
    
    gradebook1.add_grade("Tom", "Smith", "biology", 6)
    gradebook1.add_grade("Tom", "Smith", "english", 6)

    logging.info(f"Average Tom Smith's grades after adding new ones: "
    f"{gradebook1.student_average('Tom', 'Smith')}")

    logging.info("Average math scores of students from 3a: "
    f"{gradebook1.class_average('3a', 'math')}")
    
    logging.info(f"All students from good school: {gradebook1.students}")