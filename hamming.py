def hamming_distance(str1, str2):
    """
    Computes the Hamming Distance between two strings of equal length.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.

    Returns:
        int: The Hamming Distance, or -1 if the strings have different lengths.
    """
    # Hamming distance is only defined for strings of equal length.
    if len(str1) != len(str2):
        print("Error: The strings must have the same length.")
        return -1

    distance = 0
    # Iterate through the strings and count differing characters.
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            distance += 1
            
    return distance

# --- Example Usage ---

# Example 1: Comparing two words
word1 = "karolin"
word2 = "kathrin"
dist = hamming_distance(word1, word2)
if dist != -1:
    print(f"The Hamming Distance between '{word1}' and '{word2}' is: {dist}")

# Example 2: Comparing two binary strings
binary1 = "1011101"
binary2 = "1001001"
dist_binary = hamming_distance(binary1, binary2)
if dist_binary != -1:
    print(f"The Hamming Distance between '{binary1}' and '{binary2}' is: {dist_binary}")

# Example 3: Demonstrating the error check for different lengths
word3 = "hello"
word4 = "world!"
dist_mismatch = hamming_distance(word3, word4)
if dist_mismatch != -1:
    print(f"The Hamming Distance between '{word3}' and '{word4}' is: {dist_mismatch}")