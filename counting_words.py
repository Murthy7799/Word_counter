# Importing regular expression module
import re

# Getting the input from the user
input_string = input("please enter your input string: ")
# Empty dictionary to store the output
words_dictionary = {}
# Stop words list to identify the special characters
stopwords = [':', ';', '.', ',', '(', ')', '|', '{', '}', '©', '#', '&', '%', '$', '[', ']', '/', '=:', '«', '(%.)']
# number count variable to count the numbers in the string
number_count = len(re.findall(r'[0-9]+', input_string))
# Replacing the numbers with space to avoid confusion
input_string.replace('r[0-9]+', '')
# Storing the number count to the dictionary only if the numeric count is greater than zero
if number_count > 0:
    words_dictionary['numerics'] = number_count
# Reassigning the input string by removing the spaces
input_string = re.sub('[^a-zA-Z \n\.]','', input_string)

# Converting the entire string to lower case
input_string = input_string.lower()
# Splitting the sting in to words and storing in words variable
words = input_string.split()

# function for detecting and removing the special characters
def clearing_stopwords(word):

    c_word = []
    n_word = ''
    for char in word:
        if char in stopwords:
            print("special character")
        else:
            c_word.append(char)
    # the return statement will return by joining all the characters as word
    return n_word.join(c_word)


# Looping the words to count the words
for word in words:
    # checking the word for special characters and removing it by passing the word to clearing stopwords function
    word = clearing_stopwords(word)
    # checking the dictionary whether the word is available in it or not
    if word not in words_dictionary.keys():
        # if the word is not available it will create the word in dictionary and gives the count as 1
        words_dictionary[word] = 1
    # if the word is available it will increment the count
    else:
        words_dictionary[word] += 1

# Finally printing the out put of the dictionaryS
print(words_dictionary)
