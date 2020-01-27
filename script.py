last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]
subjects.append("computer science")
grades.append(100)
gradebook = list(zip(subjects, grades))
gradebook.append(("visual arts", 93))
subjects_from_last_semester = ["physics", "calculus", "ceramics", "graphic design"]
grades_from_last_semester = [92, 99, 31, 56]
last_semester_gradebook = list(zip(subjects_from_last_semester, grades_from_last_semester))
full_gradebook = gradebook + last_semester_gradebook
print(full_gradebook)