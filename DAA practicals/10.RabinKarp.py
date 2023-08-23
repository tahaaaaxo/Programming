def rabin_karp(text, pattern):
    # Define the base and modulo for the hash function
    base = 101
    modulo = 10**9+7

    # Compute the hash value of the pattern
    pattern_hash = 0
    for char in pattern:
        pattern_hash = (pattern_hash*base + ord(char)) % modulo

    # Initialize the hash value of the text window and the base power
    text_hash = 0
    base_power = 1
    for i in range(len(pattern)):
        text_hash = (text_hash*base + ord(text[i])) % modulo
        base_power = (base_power*base) % modulo

    # Loop through all possible text windows
    for i in range(len(text)-len(pattern)+1):
        # Check if the current text window matches the pattern
        if text_hash == pattern_hash and text[i:i+len(pattern)] == pattern:
            return i

        # Compute the hash value of the next text window
        if i+len(pattern) < len(text):
            text_hash = (
                text_hash*base - ord(text[i])*base_power + ord(text[i+len(pattern)])) % modulo

    # Return -1 if the pattern was not found
    return -1


# Example usage
text = "hello world"
pattern = "world"
index = rabin_karp(text, pattern)
print(index)
