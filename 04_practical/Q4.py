def sum_tail_recursive(n, accumulator=0):
    if n == 0:
        return accumulator
    return sum_tail_recursive(n - 1, accumulator + n)

# Example usage
if __name__ == "__main__":
    result = sum_tail_recursive(5)
    print("Sum up to 5:", result)  # Output: 15