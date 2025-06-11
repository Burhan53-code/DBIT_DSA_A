#Q1 Write a Python function to rotate/reverse a list.
def rotate_list(lst, k, direction='right'):
    """
    Rotates the list `lst` by `k` steps.
    
    Parameters:
    - lst: List to rotate.
    - k: Number of positions to rotate.
    - direction: 'right' or 'left' (default is 'right').

    Returns:
    - A new rotated list.
    """
    if not lst:
        return []
    
    k %= len(lst)
    if direction == 'right':
        return lst[-k:] + lst[:-k]
    elif direction == 'left':
        return lst[k:] + lst[:k]
    else:
        raise ValueError("Direction must be 'right' or 'left'")
    
    
def reverse_list(lst):
    return lst[::-1]
    
print(rotate_list([1, 2, 3, 4, 5], 2))           # [4, 5, 1, 2, 3]
print(rotate_list([1, 2, 3, 4, 5], 2, 'left'))   # [3, 4, 5, 1, 2]
print(reverse_list([1, 2, 3, 4, 5]))  # [5, 4, 3, 2, 1]