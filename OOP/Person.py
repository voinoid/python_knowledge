class Person:
    # Constructor with default values
    # NOTE: self can be called anything; however, it must be the first parameter
    def __init__(self, name="John", age=18) -> None:
        self.name = name
        self.age = age

    # What will be displayed if asked for object as a string print(person)
    def __str__(self) -> str:
        return f"{self.name}({self.age})"
  
    def myfunc(self) -> None:
        print("Hello my name is " + self.name)

    def set_Name(self, name: str) -> None:
        self.name = name

    def set_Age(self, age: int) -> None:
        self.age = age

    def get_Name(self) -> str:
        return self.name
    
    def get_Age(self) -> int:
        return self.age

p1 = Person("John", 36)
p2 = Person()

print(p1)
print(p2)

class Student(Person):
    def __init__(self, name="Larry", age=5, school="None") -> None:
        # Inherits from parent
        super().__init__(name, age) # Person.__init__(self, name, age)
        self.school = school

    def __str__(self) -> str:
        return f"{self.name}({self.age}) at {self.school}"

s1 = Student()

print(s1)