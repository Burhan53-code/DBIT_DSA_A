def count_char_frequencies(text):
    freq = {}
    for char in text:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

# Example usage
if __name__ == "__main__":
    input_string = "data structures and algorithms"
    frequencies = count_char_frequencies(input_string)
    for char, count in frequencies.items():
        print(f"'{char}': {count}")