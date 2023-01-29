



student_scores = [78, 65, 89, 86, 55, 91, 64, 89] #input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)


max=0
for i in student_scores:
  if i > max:
    max = i


print(f"The highest score in class is: {max}")

