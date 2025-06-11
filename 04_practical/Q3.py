def countdown(n):
    if n < 0:
        return
    # Head recursion: recursive call happens before any other logic
    countdown(n - 1)
    print(n)

# Example usage
if __name__ == "__main__":
    countdown(5)