

class Course:
    def __init__(self, subject: str, number: int, profesorList) -> None:
        self.subject = subject
        self.number = number
        self.profesorList = profesorList



class profesor:
    def __init__(self, firstName: str, lastName: str, difficulty: float) -> None:
        self.firstName = firstName
        self.lastName = lastName
        self.difficulty = difficulty 


