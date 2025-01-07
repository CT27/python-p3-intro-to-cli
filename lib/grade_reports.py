#!/usr/bin/env python3
import os

def create_grade_report(student_grades):
    # Ensure the reports directory exists
    if not os.path.exists('reports'):
        os.makedirs('reports')

    # Open the grade_report.txt file in append mode ('a') to avoid overwriting
    with open('./reports/grade_report.txt', 'a') as gr:
        for grade in student_grades:
            gr.write(grade + '\n')

if __name__ == '__main__':
    student_grades = []

    # Collect student grades until the user presses enter without typing anything
    grade = input("Student name, grade: ")
    while grade:
        student_grades.append(grade)
        grade = input("Student name, grade: ")

    # Create the grade report by appending the grades to the file
    create_grade_report(student_grades)
