try:
    students = {'Aman':'43','Shristi':'52','Rahul':'64','Jaya':'92'}
    name = input("Give name of the student: ")
    print(students[name])

except:
    print("Student does not exist.")