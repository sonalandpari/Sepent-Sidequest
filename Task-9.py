student_name= {
    "sonal" : 98,
    "rahul" : 47,
    "swarnim":80,
    "divyanshi": 99,
    "pari":79,
    "sandhya": 70,
    "rajiv":94,
    "alice" : 85
    }


name = input("Enter the student's name: ").lower

if name in student_name:
    print(name+"'s marks:",student_name[name])

else:
    print("Student not found")