def linear_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1