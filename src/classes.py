

class Course:
    def __init__(self, subject: str, number: int, profesorList) -> None:
        self.subject = subject
        self.number = number
        self.profesorList = profesorList

    def __str__(self) -> str:
        return self.subject + " " + self.number.__str__() + " : " + [i.__str__() for i in self.profesorList].__str__()



class Profesor:
    def __init__(self, firstName: str, lastName: str, difficulty: float) -> None:
        self.firstName = firstName
        self.lastName = lastName
        self.difficulty = difficulty

    def __str__(self) -> str:
        return self.firstName + " " + self.lastName + " Dif: " + self.difficulty.__str__()


