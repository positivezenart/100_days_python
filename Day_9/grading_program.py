student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for name,scores in student_scores.items():
    if scores >=91  and scores <= 100:
        student_grades[name] = "Outstanding"
    elif scores >= 81 and scores <= 90:
        student_grades[name] = "Exceeds Expectations"
    elif scores >= 71 and scores <= 80:
        student_grades[name] = "Acceptable"
    else:
        student_grades[name] = "Fail"

print(student_grades)
        
        