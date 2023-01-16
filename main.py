class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def calculate_total_grades(self):
        total_grades = 0
        for grade in self.grades.values():
            total_grades += sum(grade)
        return total_grades

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in \
                lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nИмя: {self.surname}\nСредняя оценка за домашние задания" ' \
               f'{self.calculate_total_grades()/(len(self.courses_in_progress) + len(self.finished_courses))}\n' \
               f'Курсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}\n'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def calculate_total_grades(self):
        total_grades = 0
        for grade in self.grades.values():
            total_grades += sum(grade)
        return total_grades

    def __str__(self):
        return f'Имя: {self.name}\nИмя: {self.surname}\nСредняя оценка за лекции" ' \
               f'{self.calculate_total_grades()/len(self.courses_attached)}\n '


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nИмя: {self.surname}\n'


student_1 = Student('Ruoy', 'Eman', 'female')
student_1.courses_in_progress += ['Python', 'French']

student_2 = Student('Testov', 'Test', 'male ')
student_2.courses_in_progress += ['Python', 'English']

lecturer_1 = Lecturer('The world', 'Is gonna roll me')
lecturer_1.courses_attached = ['Python', 'French']

lecturer_2 = Lecturer('I ain''t the sharpest', 'tool in the shed')
lecturer_2.courses_attached = ['Python', 'English']

reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_1.courses_attached += ['Python', 'French']

reviewer_2 = Reviewer('Once', 'Told me')
reviewer_2.courses_attached += ['Python', 'English']

reviewer_1.rate_hw(student_1, 'Python', 8)
reviewer_1.rate_hw(student_1, 'French', 8)
reviewer_2.rate_hw(student_2, 'Python', 9)
reviewer_2.rate_hw(student_2, 'English', 9)

student_1.rate_lecturer(lecturer_1, 'Python', 8)
student_1.rate_lecturer(lecturer_1, 'French', 8)
student_2.rate_lecturer(lecturer_2, 'Python', 9)
student_2.rate_lecturer(lecturer_2, 'English', 9)

print('\nОценки студентов:')
print(student_1.grades)
print(student_2.grades)

print('\nОценки лекторов:')
print(lecturer_1.grades)
print(lecturer_2.grades)

print('\nРевьюеры:')
print(reviewer_1)
print(reviewer_2)

print('\nЛекторы:')
print(lecturer_1)
print(lecturer_2)

print('\nСтуденты:')
print(student_1)
print(student_2)

def homeworks_result(students, course):
    pass

def lecturers_result(lectors, course):
    pass

homeworks_result([student_1, student_2], 'Python')
lecturers_result([lecturer_1, lecturer_2], 'Python')

