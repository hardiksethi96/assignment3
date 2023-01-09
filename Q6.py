students = {}
more_students = "Y"
while more_students == "Y":
    name = input("Enter the student's name: ")
    sid = input("Enter the student's SID: ")
    students[sid] = name
    more_students = input("Enter more students? (Y/N) ")
print("\nStudents:")
for sid, name in students.items():
    print(f"{name} ({sid})")
print("\nSorted by name:")
for sid, name in sorted(students.items(), key=lambda x: x[1]):
    print(f"{name} ({sid})")
print("\nSorted by SID:")
for sid, name in sorted(students.items()):
    print(f"{name} ({sid})")
search_sid = input("\nEnter a student SID to search: ")
if search_sid in students:
    print(f"Name: {students[search_sid]}")
else:
    print("Error: SID not found")
