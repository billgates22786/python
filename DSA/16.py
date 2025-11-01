def longest_repeating_sequence(s):
    n = len(s)
    # Create a 2D DP array
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    result = 0

    # Build the table
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            # If characters match and indexes are not same
            if s[i - 1] == s[j - 1] and dp[i - 1][j - 1] < (j - i):
                dp[i][j] = dp[i - 1][j - 1] + 1
                result = max(result, dp[i][j])
            else:
                dp[i][j] = 0

    return result

# Example usage
string = input("Enter a string: ")
print("Length of the longest repeating sequence is:", longest_repeating_sequence(string))
