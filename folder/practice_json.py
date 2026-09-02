import json
#Convert from Python to JSON
student = {
    "name" : "Abdikani",
    "Age" : 23,
    "Skills" : ["python", "django", "Accounting", "Ai Engineering",]
}

x = json.dumps(student, indent=4)
print(x)