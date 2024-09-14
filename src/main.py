import sys
from classes import *

NUMBER_OF_DATA_PER_PROFESOR = 3


if (len(sys.argv) < 2):
    file = open("DummyData.txt")
else:
    file = open(sys.argv[1], "r")

allCourse = []

for i in file:
    tokens = i.split(", ")
    courseName = tokens.pop(0).split(" ")
    profesorList = []
    for x in range(0, len(tokens), NUMBER_OF_DATA_PER_PROFESOR):
        profesorName = tokens[x].split(' ', 1)
        profesorList.append(Profesor(profesorName[0], profesorName[1], float(tokens[x + 2])))
    
    allCourse.append(Course(courseName[0], int(courseName[1]), profesorList))


allCourse.sort()


def getStr():
    for i in allCourse:
        print(i)

def findeCourse(subject: str, courseNumber: int):
    for i in allCourse:
        if i.subject == subject and i.number == courseNumber:
            return i.__str__()



