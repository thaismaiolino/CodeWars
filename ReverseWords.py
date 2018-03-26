# Write a reverseWords function that accepts a string a parameter, and reverses each word in the string. Any spaces in the string should be retained.

# Example:

# reverse_words("This is an example!") # returns  "sihT si na !elpmaxe"
# reverse_words("double  spaces") # returns  "elbuod  secaps"


def reverse_words(str):
    reverse_str = ''
    reverse_word_temp = ''
    for idx, element in enumerate(str):
        if element != ' ':
            reverse_word_temp = element + reverse_word_temp
        else:
            reverse_str = reverse_str + reverse_word_temp + " "  
            reverse_word_temp = ''
        if idx == len(str)-1:
            reverse_str = reverse_str + reverse_word_temp  
                 
    return reverse_str