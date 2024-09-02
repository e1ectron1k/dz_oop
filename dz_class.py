class Mentor:
    """Родительский класс для преподавателей"""

    def __init__(self, name, surname, courses_attached):
        self.name = name
        self.surname = surname
        self.courses_attached = courses_attached

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Lecturer(Mentor):
    """Класс для лекторов"""

    def __init__(self, name, surname, courses_attached):
        super().__init__(name, surname, courses_attached)
        self.grades = {}  # Словарь для хранения оценок за лекции

    def __str__(self):
        average_grade = self.get_average_grade()
        return f"{super().__str__()}\nСредняя оценка за лекции: {average_grade:.1f}"

    def get_average_grade(self):
        """Возвращает среднюю оценку за лекции"""
        total_grades = 0
        num_grades = 0
        for course in self.grades:
            total_grades += sum(self.grades[course])
            num_grades += len(self.grades[course])
        if num_grades > 0:
            return total_grades / num_grades
        else:
            return 0.0


class Reviewer(Mentor):
    """Класс для экспертов, проверяющих домашние задания"""

    def __init__(self, name, surname, courses_attached):
        super().__init__(name, surname, courses_attached)

    def __str__(self):
        return super().__str__()

    def set_grade(self, student, course, grade):
        """Выставляет оценку студенту за домашнее задание"""
    def set_grade(self, student, course, grade):
        if course not in student.grades:
            student.grades[course] = []
        student.grades[course].append(grade)


class Student:
    """Класс для студентов"""

    def __init__(self, name, surname, courses_in_progress=None, finished_courses=None):
        self.name = name
        self.surname = surname
        self.courses_in_progress = courses_in_progress or []
        self.finished_courses = finished_courses or []
        self.grades = {}  # Словарь для хранения оценок за домашние задания

    def __str__(self):
        average_grade = self.get_average_grade()
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average_grade:.1f}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}"

    def get_average_grade(self):
        """Возвращает среднюю оценку за домашние задания"""
        total_grades = 0
        num_grades = 0
        for course in self.grades:
            total_grades += sum(self.grades[course])
            num_grades += len(self.grades[course])
        if num_grades > 0:
            return total_grades / num_grades
        else:
            return 0.0

    def rate_lecturer(self, lecturer, course, grade):
        """Выставляет оценку лектору за лекцию"""
        if course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            print(f"Ошибка: Лектор {lecturer.name} {lecturer.surname} не ведет курс {course} или студент {self.name} {self.surname} не записан на этот курс.")

    def finish_course(self, course):
        """Добавляет курс в список завершенных"""
        if course in self.courses_in_progress:
            self.courses_in_progress.remove(course)
            self.finished_courses.append(course)
        else:
            print(f"Ошибка: Студент {self.name} {self.surname} не записан на курс {course}")

    def __lt__(self, other):
        """Сравнивает студентов по средней оценке за домашние задания"""
        return self.get_average_grade() < other.get_average_grade()

    def __gt__(self, other):
        """Сравнивает студентов по средней оценке за домашние задания"""
        return self.get_average_grade() > other.get_average_grade()

    def __le__(self, other):
        return self.get_average_grade() <= other.get_average_grade()

    def __ge__(self, other):
        """Сравнивает студентов по средней оценке за домашние задания"""
        return self.get_average_grade() >= other.get_average_grade()

    def __eq__(self, other):
        """Сравнивает студентов по средней оценке за домашние задания"""
        return self.get_average_grade() == other.get_average_grade()

    def __ne__(self, other):
        """Сравнивает студентов по средней оценке за домашние задания"""
        return self.get_average_grade() != other.get_average_grade()


class Lecturer(Mentor):
    """Класс для лекторов"""

    def __init__(self, name, surname, courses_attached):
        super().__init__(name, surname, courses_attached)
        self.grades = {}  # Словарь для хранения оценок за лекции

    def __str__(self):
        average_grade = self.get_average_grade()
        return f"{super().__str__()}\nСредняя оценка за лекции: {average_grade:.1f}"

    def get_average_grade(self):
        """Возвращает среднюю оценку за лекции"""
        total_grades = 0
        num_grades = 0
        for course in self.grades:
            total_grades += sum(self.grades[course])
            num_grades += len(self.grades[course])
        if num_grades > 0:
            return total_grades / num_grades
        else:
            return 0.0

    def __lt__(self, other):
        """Сравнивает лекторов по средней оценке за лекции"""
        return self.get_average_grade() < other.get_average_grade()

    def __gt__(self, other):
        """Сравнивает лекторов по средней оценке за лекции"""
        return self.get_average_grade() > other.get_average_grade()

    def __le__(self, other):
        """Сравнивает лекторов по средней оценке за лекции"""
        return self.get_average_grade() <= other.get_average_grade()

    def __ge__(self, other):
        """Сравнивает лекторов по средней оценке за лекции"""
        return self.get_average_grade() >= other.get_average_grade()

    def __eq__(self, other):
        """Сравнивает лекторов по средней оценке за лекции"""
        return self.get_average_grade() == other.get_average_grade()

    def __ne__(self, other):
        """Сравнивает лекторов по средней оценке за лекции"""
        return self.get_average_grade() != other.get_average_grade()


def calculate_average_grade_for_students(students, course):
    """Подсчитывает среднюю оценку за домашние задания по всем студентам в рамках конкретного курса"""
    grades = []
    for student in students:
        if course in student.grades:
            grades.extend(student.grades[course])
    if grades:
        return sum(grades) / len(grades)
    else:
        return 0.0


def calculate_average_grade_for_lecturers(lecturers, course):
    """Подсчитывает среднюю оценку за лекции всех лекторов в рамках курса"""
    grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            grades.extend(lecturer.grades[course])
    if grades:
        return sum(grades) / len(grades)
    else:
        return 0.0


# Создание экземпляров классов
lecturer_1 = Lecturer("Some", "Buddy", ["Python"])
lecturer_2 = Lecturer("Another", "Lecturer", ["Git"])
reviewer_1 = Reviewer("Some", "Buddy", ["Python"])
reviewer_2 = Reviewer("Another", "Reviewer", ["Git"])
student_1 = Student("Ruoy", "Eman", ["Python", "Git"], ["Введение в программирование"])
student_2 = Student("Some", "Student", ["Python"])

# Вызов методов
reviewer_1.set_grade(student_1, "Python", 8)
reviewer_1.set_grade(student_1, "Python", 9)
reviewer_2.set_grade(student_2, "Git", 10)
student_1.rate_lecturer(lecturer_1, "Python", 9)
student_1.rate_lecturer(lecturer_1, "Python", 10)
student_2.rate_lecturer(lecturer_2, "Git", 8)

# Тестирование сравнений
print(f"Лектор 1 лучше лектора 2: {lecturer_1 > lecturer_2}")
print(f"Студент 1 лучше студента 2: {student_1 > student_2}")

# Подсчет средних оценок

print(f"Средняя оценка за домашние задания по курсу Python: {calculate_average_grade_for_students([student_1, student_2], 'Python')}")
print(f"Средняя оценка за лекции по курсу Python: {calculate_average_grade_for_lecturers([lecturer_1, lecturer_2], 'Python')}")

# Вывод информации об объектах
print(student_1)
print(student_2)
print(lecturer_1)
print(lecturer_2)
print(reviewer_1)
print(reviewer_2)