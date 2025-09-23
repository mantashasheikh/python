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
