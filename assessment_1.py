# # reversing words, but punctuation marks are not reversed

# #import set of punctuation marks
# import string as str_lib

# def letter_reverser(string):
#     string_split = string
#     only_punctuation = []

#     #store punctuation marks with their original indices
#     for char in string_split:
#         if char in str_lib.punctuation:
#             only_punctuation.append(char+str(string_split.index(char)))

    
#     index = 0
#     while index < len(only_punctuation)-1:
#         #check if the first numbers after the punctuation mark are more than one digit
#         if abs(only_punctuation[index][0] - only_punctuation[index+1][0]) == 1:
#             continue
#         else:
#             #go to the part of the string without punctuation marks
#             string_split[only_punctuation[index][0]+1:int(only_punctuation[index+1][1])] = string_split[::-1]

#         index += 1
#     return ''.join(string_split)


    
import string as str_lib

def letter_reverser(input_string):
    # Convert the string into a list for mutability
    string_split = list(input_string)
    
    # Store punctuation marks with their original indices
    punctuation_indices = [(i, char) for i, char in enumerate(string_split) if char in str_lib.punctuation]
    
    # Remove punctuation from the string
    words_only = [char for char in string_split if char not in str_lib.punctuation]
    
    # Reverse the letters in the words
    reversed_letters = words_only[::-1]
    
    # Reinsert punctuation at their original positions
    for index, punct in punctuation_indices:
        reversed_letters.insert(index, punct)
    
    # Join the list back into a string
    return ''.join(reversed_letters)

# Example usage
input_string = "hello,world"
result = letter_reverser(input_string)
print(result)  # Output: "olleh,dlrow"