
dog = {}
dog ["name"] = "doggy"
dog ["color"] = "white"
dog ["breed"]  ="shih tzu terrier"
dog ["age"] = 12
dog ["legs"] = 4

student = {"first_name":"Tom", "last_name":"VDM", "gender":"M", "age":190, "marital status":"S", "country":"US", "skills":[]}
print(len(student))
print(student["first_name"], type(student["first_name"]))
student["skills"].append("python")
student["skills"].append("C")
student["skills"].append("web exploitation")
print(student["skills"], type(student["skills"]))

print(student.keys())
print(student.values())

student_as_tuples = student.items()
print(student_as_tuples)

student.pop("age")
print(student)
del student
