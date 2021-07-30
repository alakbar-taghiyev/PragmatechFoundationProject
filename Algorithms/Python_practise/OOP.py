""" class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
   
    def brandmodel(self):
        return f'Maşın modeli {self.brand}, maşın ili {self.year} '

car_1 = Car('BMW', 'i5', 2010)
car_2 = Car('Audi', 'x6', 2020)

print(car_1.brand)
print(car_1.brandmodel()) """

""" class Movie:
    def __init__(self, name, janr, year):
        self.name = name
        self.janr = janr
        self.year = year

    def movieName(self):
        return f'filmin adı {self.name}'

    
movie_1 = Movie('Titanic', 'dram', 2009)
movie_2 = Movie('Nemo', 'adventure', 2011)

print(movie_2.year)
print(movie_1.name)
print(movie_2.movieName()) """

""" class Student:

    school_name = 'X Lisesi'
    number_of_students = 0

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        Student.number_of_students += 1

    def average(self):
        return sum(self.grade)/len(self.grade)

    def schoolName(self):
        return 'Mektebin adi' + self.school_name

    
student_1 = Student('Alik', 22, [10,20,30,40])
student_2 = Student('Aida', 19, [15,25,35,45])

print(student_1.age)
print(student_2.name)
print(student_1.average())
print(student_2.average()) 
print(student_1.school_name)
print(student_2.school_name)
print(Student.school_name)
print(student_1.schoolName())
print(student_1.__dict__)
print(Student.__dict__)
print(Student.number_of_students) """


""" class Student:

    school_name = 'X Lisesi'
    number_of_students = 0

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        Student.number_of_students += 1

    def average(self):
        return sum(self.grade)/len(self.grade)
    
    @classmethod
    def display_school_name(cls, name_of_school):
        cls.school_name = name_of_school
    @staticmethod
    def statik():
        return 'Sadece mesaj gonderirem'

Student.display_school_name('Y Lisesi')


student_1 = Student('Alik', 22, [10,20,30,40])
student_2 = Student('Aida', 19, [15,25,35,45])

print(student_1.school_name)
student_1.school_name = "Z Lisesi"

print(Student.school_name)
print(student_1.school_name)
print(student_2.school_name)
print(Student.statik())
print(student_1.statik()) """

# Ozumuzden misal
""" class Animal:
    varliq = 'canli'
    animal_counts = 0
    def __init__(self, name, kind, color):
        self.name = name
        self.kind = kind
        self.color = color
        Animal.animal_counts +=1
    def animal_kind(self):
        return 'heyvanin novu ' + self.kind
    @classmethod
    def varliqDeyishme(cls, name_change):
        cls.varliq = name_change
    @staticmethod
    def statik():
        return 'Biz ejdahayiq'

Animal.varliqDeyishme('cansiz')
    
print(Animal.animal_counts)

animal_1 = Animal('ceyran', 'heyvan', 'narinci')
animal_2 = Animal('ilan', 'surunen', 'boz')


print(animal_1.name)
print(animal_2.color)
print(animal_2.animal_kind())
print(animal_2.__dict__)
print(animal_1.varliq)
print(Animal.varliq)
print(Animal.animal_counts)

print(Animal.varliq)
print(animal_1.varliq)
print(animal_1.statik()) """


class Student:
    test = 'Test Student'
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def average(self):
        return sum(self.grade)/len(self.grade)
    

student_1 = Student('Alik', 22, [10,20,30,40])
student_2 = Student('Aida', 19, [15,25,35,45])

class UniversityStudent(Student):
    test = 'Test University'
    def __init__(self, name, age, grade, university):
        super().__init__(name, age, grade)
        self.university = university

u_studen_1 = UniversityStudent('nurlan', 24, [12,14,16,18], 'ADNSU')

print(u_studen_1.name)
print(u_studen_1.university)
print(UniversityStudent.test)
print(Student.test)


