def main():
    course_no = input('Enter a Course Number: ')
    
    myroom = room_dict()
    myinstructor = instructor_dict()
    mytime = time_dict()

    course_summary(course_no,myroom,myinstructor,mytime)



#create dictionaries
def room_dict():
    CourseRoom = {'CS101':3004, 'CS102':4501,'CS103':6755,'NT110':1244,'CM241':1411}
    return CourseRoom

def instructor_dict():
    CourseInstructor = {'CS101':'Haynes', 'CS102':'Alvarado','CS103':'Rich','NT110':'Burke','CM241':'Lee'}
    return CourseInstructor

def time_dict():
    CourseTime = {'CS101':'8:00 a.m.', 'CS102':'9:00 a.m.','CS103':'10:00 a.m.','NT110':'11:00 a.m.','CM241':'1:00 p.m.'}
    return CourseTime



#display output
def course_summary(course_no,myroom,myinstructor,mytime):
    print()
    if course_no not in myroom:
        print("Invalid Course Number")
    else:
        print('Room Number: ',myroom[course_no])
        print('Instructor:  ',myinstructor[course_no])
        print('Meeting Time:',mytime[course_no])
        print()


main()

