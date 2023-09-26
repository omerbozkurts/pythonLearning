#q1 take students information from user and keep it in a dictionary

students={ int(input()):{
    'name':str(input()),
    'surname':str(input()),
    'phone number':int(input())
    },
    int(input()):{
    'name':str(input()),
    'surname':str(input()),
    'phone number':int(input())
    }
}
print(students)

#q2 take student number from user and show the students information

studentNumber=int(input())
print(students[studentNumber])