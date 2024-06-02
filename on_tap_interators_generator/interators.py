from abc import abstractmethod, ABC
class Person(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def thongtin(self):
        pass

class Student(Person):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
    def thongtin(self):
        print(f"Student name: {self.name} - age: {self.age}")

st = Student("Nguyen Van A", 20)
st.thongtin()