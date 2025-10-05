#Nested Dict

students = {
    "Ankit" : {"age": 20, "grade": "A"},
    "Ravi": {"age": 19, "grade": "B"}
}

for name, dets in students.items():
    print(name + ":" + str(dets["age"]))