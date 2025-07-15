import random

def quick_sort(values):
    # If the list has 1 or no elements, it's already sorted
    if len(values) <= 1:
        return values

    # pivot (first element)
    pivot = values[0]

    # Split the rest of the list into two parts
    # left part: numbers less than or equal to pivot
    left = []

    # right part: numbers greater than pivot
    right = []

    # start from index to skip the pivot
    for number in values[1:]:  
        if number <= pivot:
            left.append(number)
        else:
            right.append(number)
            
    # print(f"Left {left}")
    # print(f"Right {right}")

    # Recursively sort both parts and put them together
    return quick_sort(left) + [pivot] + quick_sort(right)

# 10 unique numbers from 1 to 99
random_list = random.sample(range(1, 100), 3)

print("Unsorted list:", random_list)
sorted_list = quick_sort(random_list.copy())
print("Sorted list:", sorted_list)