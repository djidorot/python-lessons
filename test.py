"""
Problem Statement:
You are tasked with creating a program that calculates and assigns grades based on the marks obtained by a student in an exam.

Your program should prompt the user to enter the marks obtained by the student. It should then use the following grading criteria to determine the grade:

A: 90 or above
B: 80 - 89
C: 70 - 79
D: 60 - 69
E: 50 - 59
F: Below 50

Write a Python program to implement the above functionality. Ensure that your program provides clear prompts for input and displays the assigned grade.

Your program should follow the structure outlined in the provided code snippet. Make sure to handle both integer and floating-point input for marks obtained.

Remember, your program should not accept negative marks or marks greater than 100. If the user enters invalid marks, your program should display an appropriate error message and prompt the user to enter valid marks.
"""

marks = input("Enter the marks obtained: ")

if marks >= 90:
    grade = 'A'
elif marks >= 80:
    grade = 'B'
elif marks >= 70:
    grade = 'C'
elif marks >= 60:
    grade = 'D'
elif marks >= 50:
    grade = 'E'
else:
    grade = 'F'
