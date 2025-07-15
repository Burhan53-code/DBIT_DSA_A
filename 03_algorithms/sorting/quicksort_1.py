import random

def quick_sort(values):
    if len(values) <= 1:
        return values

    # first element is the pivot
    pivot = values[0]

    left = [x for x in values[1:] if x <= pivot]
    right = [x for x in values[1:] if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


# 10 unique numbers from 1 to 99
random_list = random.sample(range(1, 100), 10)

print("Unsorted list:", random_list)
sorted_list = quick_sort(random_list.copy())
print("Sorted list:", sorted_list)