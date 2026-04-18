# Number Analyzer Tool (Broken Version)

def get_numbers():
    numbers = input("Enter numbers separated by commas: ")
    numbers_list = numbers.split(",")
    return numbers_list  # ❌ still strings


def calculate_average(numbers):
    total = 0
    for n in numbers:
        total += n   # ❌ cannot add string to int
    return total / len(numbers)


def find_largest(numbers):
    largest = 0   # ❌ fails if all numbers are negative
    for n in numbers:
        if n > largest:
            largest = n
    return largest


def count_even(numbers):
    count = 0
    for n in numbers:
        if n % 2 == 0:   # ❌ n is string
            count += 1
    return count


nums = get_numbers()

print("Numbers:", nums)
print("Average:", calculate_average(nums))
print("Largest:", find_largest(nums))
print("Even count:", count_even(nums))  