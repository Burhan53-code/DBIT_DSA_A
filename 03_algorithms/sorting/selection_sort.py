import random

def selection_sort(unsorted_list):
    number_of_elements = len(unsorted_list)
    
    for outerloop in range(number_of_elements):
        minimum_index = outerloop
        for innerloop in range(outerloop + 1, number_of_elements):
            # find the smallest value
            if unsorted_list[innerloop] < unsorted_list[minimum_index]:
                minimum_index = innerloop
                print(f"Minimum values is {unsorted_list[minimum_index]}")
            
        # swap the values           
        temp = unsorted_list[outerloop]
        unsorted_list[outerloop] = unsorted_list[minimum_index]
        unsorted_list[minimum_index] = temp
        
        # print(f"Values {unsorted_list}")
        
    return unsorted_list

# 10 unique numbers from 1 to 99
random_list = random.sample(range(1, 100), 10)

print("Unsorted list:", random_list)
sorted_list = selection_sort(random_list.copy())
print("Sorted list:", sorted_list)