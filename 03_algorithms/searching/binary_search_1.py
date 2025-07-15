import random

# recursive binary search

def binary_search(list_of_values, target_search, low, high):
    # Base case
    # check if there are values
    if low > high:
        return -1
    
    mid = (low + high)//2
    print(f"Low {low} mid {mid} high {high}")
    
    
    # another base for when we find what we are looking for
    if list_of_values[mid] == target_search:
        return mid
    elif list_of_values[mid] < target_search:
        return binary_search(list_of_values, target_search, mid +1, high)
    else:
        return binary_search(list_of_values,target_search,low, mid - 1)
    
# generate 10 random values between 1 and 100
values = sorted([random.randint(1,100) for _ in range(10)])
print(f"Values {values}")

# enter the value to search for
target = int(input("Enter number to search : "))

# call the function and pass in the parameters
result = binary_search(values, target, 0, len(values) - 1)

# check what has been returned
if result != -1:
    print(f"Value {values[result]} found at index {result}")
else:
    print(f"Value {target} not found")








