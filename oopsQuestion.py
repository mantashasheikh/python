# create a class of maxfinder thet identifies the largest number in a list
class MaxFinder:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_max(self):
        if not self.numbers:  # check for empty list
            return None
        max_num = self.numbers[0]
        for num in self.numbers:
            if num > max_num:
                max_num = num
        return max_num


# Example usage
nums = [5, 12, 8, 21, 3]
finder = MaxFinder(nums)
print("The largest number is:", finder.find_max())





# student grade calculator implement a student class with attribute for name and list of marks (for 5 subjects)
# Include a method to calcuatethe average and determine the grade
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks  # list of marks for 5 subjects

    def calculate_average(self):
        if not self.marks:
            return 0
        return sum(self.marks) / len(self.marks)

    def determine_grade(self):
        avg = self.calculate_average()

        if avg >= 90:
            return "A+"
        elif avg >= 80:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 50:
            return "D"
        else:
            return "F"

    def display_result(self):
        print(f"Student: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"Average: {self.calculate_average():.2f}")
        print(f"Grade: {self.determine_grade()}")


# Example usage
s1 = Student("Alice", [85, 92, 78, 88, 90])
s1.display_result()

s2 = Student("Bob", [45, 50, 39, 60, 55])
s2.display_result()








# define an abstract base class polygon with an abstract method area classes rectangle and triangle

from abc import ABC, abstractmethod

# Abstract Base Class
class Polygon(ABC):
    @abstractmethod
    def area(self):
        """Abstract method to calculate area"""
        pass

# Rectangle class inheriting from Polygon
class Rectangle(Polygon):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return self.length * self.breadth

# Triangle class inheriting from Polygon
class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

# Example usage

rect = Rectangle(10, 5)
tri = Triangle(6, 4)

print("Area of Rectangle:", rect.area())
print("Area of Triangle:", tri.area())








# design a class that tracks how many object have been created from it and has a method to display this count
class ObjectCounter:
    # class variable to track number of objects
    __count = 0

    def __init__(self):
        ObjectCounter.__count += 1   # increment whenever object is created

    @classmethod
    def display_count(cls):
        """Displays how many objects have been created"""
        print(f"Total objects created: {cls.__count}")
        return cls.__count


# Example usage

o1 = ObjectCounter()
o2 = ObjectCounter()
o3 = ObjectCounter()
o4 = ObjectCounter()

ObjectCounter.display_count()  # Output: Total objects created: 3
