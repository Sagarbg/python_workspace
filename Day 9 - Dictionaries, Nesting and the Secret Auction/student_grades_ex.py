'''
This is the scoring criteria: 

- Scores 91 - 100: Grade = "Outstanding" 

- Scores 81 - 90: Grade = "Exceeds Expectations" 

- Scores 71 - 80: Grade = "Acceptable" 

- Scores 70 or lower: Grade = "Fail" 
'''

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

i = 1

print(len(student_scores))

while i <= len(student_scores):

    for score in student_scores:
        if student_scores[score] >= 91 and student_scores[score] < 100:
            student_grades[score] = "Outstanding"
        elif student_scores[score] >= 81 and student_scores[score] < 90:
            student_grades[score] = "Exceeds Expectations"
        elif student_scores[score] >= 71 and student_scores[score] < 80:
            student_grades[score] = "Acceptable"
        elif student_scores[score] <= 70:
            student_grades[score] = "Fail"
    
    i = i + 1

print(student_grades)