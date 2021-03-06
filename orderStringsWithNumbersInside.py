# Your task is to sort a given string. Each word in the String will contain a single number. This number is the position the word should have in the result.

# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

# If the input String is empty, return an empty String. The words in the input String will only contain valid consecutive numbers.

# For an input: "is2 Thi1s T4est 3a" the function should return "Thi1s is2 3a T4est"

# your_order("is2 Thi1s T4est 3a")
# [1] "Thi1s is2 3a T4est"




def order(sentence):
    words = sentence.split(" ")
    dict_words = {}
    for item in words:
        dict_words[(sorted(item)[0])] = item
    dict_words= sorted(dict_words.items(), key=lambda k: k[0])
    new_setence = ''
    for item in dict_words:
        new_setence = new_setence + item[1] + " "
    return new_setence.strip()