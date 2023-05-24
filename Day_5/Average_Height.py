student_heights = [180, 124, 165, 173, 189, 169, 146]

sum =0
count_people = 0
for i in student_heights:
    sum += i
    count_people += 1
average = round(sum / count_people)
print(f"average height of students {average} CM's")
    