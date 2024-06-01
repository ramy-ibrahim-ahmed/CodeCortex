def customSortString(order: str, s: str) -> str:
    # Create a dictionary to map characters to their corresponding indices in the order string
    char_map = {char: index for index, char in enumerate(order)}

    # Define a custom sorting function based on the character map
    def custom_sort(char):
        return char_map.get(char, float("infinity"))

    # Sort the string 's' using the custom sorting function
    s = sorted(s, key=custom_sort)
    
    # Join the sorted characters to form the final string
    return "".join(s)
############################################################################################################
def customSortString(order : str, s : str) -> str:
    ans = ""  # Initialize an empty string to store the result

    # Iterate through each character in the order string
    for ch in order:
        if ch in s:
            # Append the character to the result string the same number of times it occurs in 's'
            for _ in range(s.count(ch)):
                ans += ch
    
    # Iterate through each character in 's' that is not already in the result string
    for ch in s:
        if ch not in ans:
            ans += ch  # Append the character to the result string
    
    # Return the final result string
    return ans


order, s = "kqep", "pekeq"
print(customSortString(order, s))  # Output: "kqeep"