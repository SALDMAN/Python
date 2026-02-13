
class Person:
    #This represents a simple class definition for a Person.
    # The Person class has two attributes: name and age.
    def __init__ (self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"
    def display(self):
        print(f"{self.name} is {self.age} years old")
    def ChangeName(self, new_name):
        self.name = new_name
    def ChangeAge(self, new_age):
        self.age = new_age


# This represents a simple inheritance example.
# where the Student class inherits from the Person class.
# The Student class has an additional attribute student_id
# also it overrides the __str__ method to include this information when printing the student's details.
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def __str__(self):
        return f"{self.name} is {self.age} years old and has student ID {self.student_id}"


def main():
    # This is a simple example for lists (arrays in Python).
    a = [2,4,12,33,3204]
    a.sort()
    if (a.__contains__(4)):
        print ("4 is in the list")
    else:
        print("4 is not in the list")
    # A simple loop's example.
    for i in range(a.__len__()):
        print(a[i])
    while (a[i] != 3204):
        i += 1
    print("Found 3204 at index", i)


    # This is a simple example for tuples.
    # Tuples are immutable, meaning that once they are created, their values cannot be changed.
    b = (3,2,54)
    for i in range(b.__len__()):
        print(b[i])

    # This is a simple example for dictionaries.
    # Dictionaries are a collection of key-value pairs, where each key is unique and maps to a specific value.
    c = {"Algebra" : 80, "Logics and sets Theory" :60, "Intro to computer Science" : 67}
    d = c.keys()
    e = c.values()
    f = c.items()
    print( d,e,f)

if __name__ == "__main__":
    main()

