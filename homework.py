class Student:
    student_list = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.student_list.append(self)

    def rate_hw_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades_lecturer:
                lecturer.grades_lecturer[course] += [grade]
            else:
                lecturer.grades_lecturer[course] = [grade]
        else:
            return 'Ошибка'
        
    def average_grades_hm(self):
        grades_count = 0
        grades_sum = 0
        for grade in self.grades:
            grades_count += len(self.grades[grade])
            grades_sum += sum(self.grades[grade])
        if grades_count > 0:
            return grades_sum / grades_count
        else:
            return 0
        
    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {round(self.average_grades_hm(), 0)}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses)}\n")
    
    def __lt__(self, other):
        return self.average_grades_hm() < other.average_grades_hm()
    
    def __eq__(self, other):
        return self.average_grades_hm() == other.average_grades_hm()
    
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
 
class Lecturer(Mentor):
    lecturer_list = []
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades_lecturer = {}
        Lecturer.lecturer_list.append(self)

    def average_grades_(self):
        grades_count = 0
        grades_sum = 0
        for grade in self.grades_lecturer:
            grades_count += len(self.grades_lecturer[grade])
            grades_sum += sum(self.grades_lecturer[grade])
        if grades_count > 0:
            return grades_sum / grades_count
        else:
            return 0

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {round(self.average_grades_(), 0)}\n")
    
    def __lt__(self, other):
        return self.average_grades_() < other.average_grades_()
    
    def __eq__(self, other):
        return self.average_grades_() == other.average_grades_()

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n")

def courses_average_students(student_list, course):
    for student in student_list:
        for cours_name, average in student.grades.items():
            if course == cours_name:
                sum_average = sum(average) / len(average)
                print(f"Студент: {student.name} {student.surname}\n"
                      f"Курс: {cours_name}\n"
                      f"Средняя оценка за домашние задания: {round(sum_average, 0)}\n")

def courses_average_lecturer(lecturer_list, course):
    for lecturer in lecturer_list:
        for cours_name, average in lecturer.grades_lecturer.items():
            if course == cours_name:
                sum_average = sum(average) / len(average)
                print(f"Лектор: {lecturer.name} {lecturer.surname}\n"
                      f"Курс: {cours_name}\n"
                      f"Cредняя оценка за домашние задания: {round(sum_average, 0)}\n")
                
student_1 = Student('Nikita', 'Golova', 'Мужской')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Java']
student_1.finished_courses += ["Введение в программирование"]

student_2 = Student('Denis', 'Rawow', 'Мужской')
student_2.courses_in_progress += ['Git']
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Django']
student_2.finished_courses += ['Введение в программирование']

mentor_reviewer_1 = Reviewer('Roman', 'Qaswedo')
mentor_reviewer_1.courses_attached += ['Python']
mentor_reviewer_1.courses_attached += ['Git']
mentor_reviewer_1.courses_attached += ['Django']

mentor_reviewer_2 = Reviewer('Roman', 'Neofidi')
mentor_reviewer_2.courses_attached += ['Python']
mentor_reviewer_2.courses_attached += ['Git']
mentor_reviewer_2.courses_attached += ['Django']

mentor_lecturer_1 = Lecturer('Samir', 'Samgun')
mentor_lecturer_1.courses_attached += ['Python']
mentor_lecturer_1.courses_attached += ['Git']
mentor_lecturer_1.courses_attached += ['Django']

mentor_lecturer_2 = Lecturer('Andrew', 'Livensmile')
mentor_lecturer_2.courses_attached += ['Python']
mentor_lecturer_2.courses_attached += ['Git']
mentor_lecturer_2.courses_attached += ['Django']

mentor_reviewer_1.rate_hw(student_1, 'Python', 5)
mentor_reviewer_1.rate_hw(student_1, 'Python', 10)
mentor_reviewer_1.rate_hw(student_1, 'Python', 9)
mentor_reviewer_1.rate_hw(student_1, 'Git', 10)
mentor_reviewer_1.rate_hw(student_1, 'Django', 7)

mentor_reviewer_1.rate_hw(student_2, 'Python', 9)
mentor_reviewer_1.rate_hw(student_2, 'Python', 8)
mentor_reviewer_1.rate_hw(student_2, 'Python', 6)
mentor_reviewer_1.rate_hw(student_2, 'Git', 5)
mentor_reviewer_1.rate_hw(student_2, 'Django', 9)

student_1.rate_hw_lecturer(mentor_lecturer_1, 'Python', 10)
student_1.rate_hw_lecturer(mentor_lecturer_1, 'Python', 10)
student_1.rate_hw_lecturer(mentor_lecturer_1, 'Python', 9)
student_1.rate_hw_lecturer(mentor_lecturer_1, 'Git', 8)
student_1.rate_hw_lecturer(mentor_lecturer_1, 'Django', 7)

student_2.rate_hw_lecturer(mentor_lecturer_2, 'Python', 7)
student_2.rate_hw_lecturer(mentor_lecturer_2, 'Python', 5)
student_2.rate_hw_lecturer(mentor_lecturer_2, 'Python', 8)
student_2.rate_hw_lecturer(mentor_lecturer_2, 'Git', 10)
student_2.rate_hw_lecturer(mentor_lecturer_2, 'Django', 10)

if student_1 > student_2:
    print(f'Средняя оценка {student_1.name} {student_1.surname} больше, чем средняя оценка {student_2.name} {student_2.surname}')
elif student_1 < student_2:
    print(f'Средняя оценка {student_1.name} {student_1.surname} меньше, чем средняя оценка {student_2.name} {student_2.surname}')
else:
    print(f'Средняя оценка {student_1.name} {student_1.surname} равна средней оценке {student_2.name} {student_2.surname}')

if mentor_lecturer_1 > mentor_lecturer_2:
    print(f'Средняя оценка {mentor_lecturer_1.name} {mentor_lecturer_1.surname} больше, чем средняя оценка {mentor_lecturer_2.name} {mentor_lecturer_2.surname}')
elif mentor_lecturer_1 < mentor_lecturer_2:
    print(f'Средняя оценка {mentor_lecturer_1.name} {mentor_lecturer_1.surname} меньше, чем средняя оценка {mentor_lecturer_2.name} {mentor_lecturer_2.surname}')
else:
    print(f'Средняя оценка {mentor_lecturer_1.name} {mentor_lecturer_1.surname} равна средней оценке {mentor_lecturer_2.name} {mentor_lecturer_2.surname}')

courses_average_students(Student.student_list, 'Python')
courses_average_lecturer(Lecturer.lecturer_list, 'Git')