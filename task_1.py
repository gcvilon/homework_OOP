class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        ratings = [
            sum(v) if isinstance(v, list) else v
            for v in self.grades.values()
        ]
        count = sum(len(v) if isinstance(v, list) else 1 for v in self.grades.values() if v)
        average_rating = sum(ratings) / count if count > 0 else 0

        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {average_rating}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}'
        )

    def __lt__(self, other):
        """Сравнение студентов по средней оценке за домашние задания"""
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_rating() < other.average_rating()

    def average_rating(self):
        """Средняя оценка за домашние задания"""
        ratings = [
            grade for grades in self.grades.values() for grade in grades
        ]
        return sum(ratings) / len(ratings) if ratings else 0

    def rate_lectures(self, lectures, course, grade):
        if isinstance(lectures, Lectures) and course in self.courses_in_progress:
            if course in lectures.list_ratings:
                lectures.list_ratings[course] += [grade]
            else:
                lectures.list_ratings[course] = [grade]
        else:
            print("Ошибка")


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lectures(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.list_ratings = {}

    def __str__(self):
        ratings = [
            sum(v) if isinstance(v, list) else v
            for v in self.list_ratings.values()
        ]
        count = sum(len(v) if isinstance(v, list) else 1 for v in self.list_ratings.values() if v)
        average_rating = sum(ratings) / count if count > 0 else 0

        return (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка на лекции: {average_rating}'
        )

    def __lt__(self, other):
        """Сравнение лекторов по средней оценке за лекции"""
        if not isinstance(other, Lectures):
            return NotImplemented
        return self.average_rating() < other.average_rating()

    def average_rating(self):
        """Средняя оценка за лекции"""
        ratings = [
            grade for grades in self.list_ratings.values() for grade in grades
        ]
        return sum(ratings) / len(ratings) if ratings else 0


class Reviewer(Mentor):
    def __str__(self):
        return (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}'
        )

    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


# Пример сравнения
student_1 = Student('Artem', 'Deev', 'male')
student_1.courses_in_progress += ['Python', 'Git']
student_2 = Student('Julia', 'Lopacheva', 'female')
student_2.courses_in_progress += ['Python', 'English']

lectures_1 = Lectures('Mikhail', 'Eremin')
lectures_1.courses_attached += ['Python', 'Git']
lectures_2 = Lectures('Nikita', 'Zaycev')
lectures_2.courses_attached += ['Python', 'English']

student_1.rate_lectures(lectures_1, 'Python', 8)
student_1.rate_lectures(lectures_1, 'Git', 10)
student_2.rate_lectures(lectures_2, 'Python', 9)
student_2.rate_lectures(lectures_2, 'English', 8)

reviewer_1 = Reviewer('Elena', "Serikova")
reviewer_1.courses_attached += ['Python', 'Git']
reviewer_1.rate_student(student_1, 'Python', 9)
reviewer_1.rate_student(student_1, 'Git', 8)
reviewer_2 = Reviewer('Artem', 'Babeshkov')
reviewer_2.courses_attached += ['Python', 'English']
reviewer_2.rate_student(student_2, 'Python', 10)
reviewer_2.rate_student(student_2, 'English', 9)

print(student_1 < student_2)  # Сравнение студентов
print(lectures_1 < lectures_2)  # Сравнение лекторов
