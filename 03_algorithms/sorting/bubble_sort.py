import random

def bubble_sort(unsorted_list):
    number_of_elements = len(unsorted_list)
    
    for outerloop in range(number_of_elements):
        for innerloop in range(0,number_of_elements - 1 - outerloop):
            if unsorted_list[innerloop] > unsorted_list[innerloop + 1]:
                # unsorted_list[innerloop], unsorted_list[innerloop + 1] = (
                #     unsorted_list[innerloop+1] ,unsorted_list[innerloop] 
                # )
                
                # diffrent way of swapping values
                temp = unsorted_list[innerloop]
                unsorted_list[innerloop] = unsorted_list[innerloop + 1]
                unsorted_list[innerloop + 1] = temp
                
            # inside inner loop
            # print(f"Innerloop {unsorted_list}")
            
        # inside outer loop
        # print(f"Outerloop {unsorted_list}")
    return unsorted_list

# 10 unique numbers from 1 to 99
random_list = random.sample(range(1, 100), 10)
print("Unsorted list:", random_list)

sorted_list = bubble_sort(random_list.copy())
print("Sorted list:", sorted_list)