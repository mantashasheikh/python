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

