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
                f'Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {', '.join(self.finished_courses)}'
        )

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

def rating_course(students, course):
    summ_rate, count_rate = 0, 0
    for student in students:
        summ_rate += student.grades[course][0]
        count_rate += 1
    return summ_rate / count_rate

def rating_lectures(lectures, course):
    summ_rate, count_rate = 0, 0
    for lecturer in lectures:
        summ_rate += lecturer.list_ratings[course][0]
        count_rate += 1
    return summ_rate / count_rate


student_1 = Student('Artem', 'Deev', 'male')
student_1.courses_in_progress += ['Python', 'Git']
student_2 = Student('Julia', 'Lopacheva', 'female')
student_2.courses_in_progress += ['Java', 'English']

lectures_1 = Lectures('Mikhail', 'Eremin')
lectures_1.courses_attached += ['Python', 'Git']
lectures_2 = Lectures('Nikita', 'Zaycev')
lectures_2.courses_attached += ['Java', 'English']

student_1.rate_lectures(lectures_1, 'Python', 8)
student_1.rate_lectures(lectures_1, 'Git', 10)
student_2.rate_lectures(lectures_2, 'Java', 9)
student_2.rate_lectures(lectures_2, 'English', 8)

reviewer_1 = Reviewer('Elena', "Serikova")
reviewer_1.courses_attached += ['Python', 'Git']
reviewer_1.rate_student(student_1, 'Python', 9)
reviewer_1.rate_student(student_1, 'Git', 8)
reviewer_2 = Reviewer('Artem', 'Babeshkov')
reviewer_2.courses_attached += ['Java', 'English']
reviewer_2.rate_student(student_2, 'Java', 10)
reviewer_2.rate_student(student_2, 'English', 9)
