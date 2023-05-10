import functools

# get dictionary words from mac file
dictionary_words = None
with open('/usr/share/dict/words', 'r') as f:
    dictionary_words = f.read().splitlines()

def word_combinations(letters, original_length):
    # base case: if there is one character in the string return the character     
    if len(letters)==1: 
        return [letters]
    # instantiate array to store word combinations
    result=[]
    # use enumerate to iterate over each character in string and keep track of character's index
    for i, character in enumerate(letters):
        # recursively call word combinations with all letters except current character
        # for combinations in this recursive call 
        for combination in word_combinations(letters[:i]+letters[i+1:], original_length):
            # the word is the current character plus all combinations
            word = character+combination
            # if the word length is equal to the original length (meaning it is using all letters)
            if len(word) == original_length:
                # check if the word is in dictionary words and does not already appear in the result list
                if word not in result and word in dictionary_words:
                    # if is dict word and uses all letters, 
                    # append the current character plus the combination to results 
                    result.append(word)
            else:
                # else this is a subcombination and just append the word to results to continue recursive call
                result.append(word)
    # return list of results
    return result


# function to find all possible circle letter jumbles from all possible real words
#     # input:
#     #   all of the real words found from the word combinations for all positions 
#     #   indexes of the circles for each word
#     # example:
#     #   WORDS = {
#     #   'word1' = ['mane', 'mean', 'amen', 'enam', 'name', 'nema']
#     #   'word2' = ['kiosk']
#     #   'word3' = ['immune']
#     #   'word4' = ['cousin']
#     #   }
#     #   INDEXES = {
#     #   'word1' = [2, 3]
#     #   'word2' = [0, 1, 3]
#     #   'word3' = [4]
#     #   'word4' = [3, 4]
#     #   }
#     # output:
#     #   list of all possible jumbled words from the given words and indexes
#     possible_jumbles = []
#     for key, words_list in words_dict:
#         i = 0
#         this_jumble = []
#         for index in indexes_dict[key]:
#             # Append the character at the specified index of each word in the words_list to this_jumble
#             this_jumble.append([word[index] for word in words_list])

def circle_letter_combinations(words_dict, indexes_dict):
    circle_letters_dict = {
        'word1_letters': [],
        'word2_letters': [],
        'word3_letters': [],
        'word4_letters': [],
    }
    for key, words_list in words_dict.items():
        for word in words_list:
            circle_letters = [word[index] for index in indexes_dict[key]]
            new_key = f'{key}_letters'
            circle_letters_dict[new_key].append(circle_letters)
    return circle_letters_dict

def final_combinations(letters_dict):
    if len(letters_dict) == 0:
        return ['']
    else:
        key, letters = letters_dict.popitem()
        combinations = final_combinations(letters_dict)
        new_combinations = []
        for letter in letters:
            letter_str = functools.reduce(lambda x,y : x+y, letter)
            for combination in combinations:
                new_combo = letter_str + combination
                if new_combo not in new_combinations:
                    new_combinations.append(new_combo)
        return new_combinations

def final_word_combinations(letters, original_length):
    # base case: if there is one character in the string return the character     
    if len(letters)==1: 
        return [letters]
    # instantiate array to store word combinations
    result=[]
    # use enumerate to iterate over each character in string and keep track of character's index
    for i, character in enumerate(letters):
        # recursively call word combinations with all letters except current character
        # for combinations in this recursive call 
        for combination in final_word_combinations(letters[:i]+letters[i+1:], original_length):
            # the word is the current character plus all combinations
            word = character+combination
            # if the word length is equal to the original length (meaning it is using all letters)
            if len(word) == original_length:
                # check if the word is in dictionary words and does not already appear in the result list
                if check_for_words(word[2:]) and word[:2] in dictionary_words and word not in result:
                    # if is dict word and uses all letters, 
                    # append the current character plus the combination to results 
                    result.append(word[:2] + '-' + word[2:])
            else:
                # else this is a subcombination and just append the word to results to continue recursive call
                result.append(word)
    # return list of results
    return result

def find_substrings(s):
    # Create a set of all possible substrings of s with length > 3
    substrings = set()
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if j - i > 4:
                substrings.add(s[i:j])
    return substrings

def check_for_words(s):
    # Check if any substring of s is a word in the dictionary
    substrings = find_substrings(s)
    for substring in substrings:
        if substring in dictionary_words:
            return True
    return False


all_possible_word_combos = {
    'word1': word_combinations('tefon', len('tefon')),
    'word2': word_combinations('sokik', len('sokik')),
    'word3': word_combinations('niumem', len('niumem')),
    'word4': word_combinations('siconu', len('siconu'))
}

print(all_possible_word_combos)

all_word_circle_indexes = {
    'word1': [2, 4],
    'word2': [0, 1, 3],
    'word3': [4],
    'word4': [3, 4]
}

circle_letter_dict = circle_letter_combinations(all_possible_word_combos, all_word_circle_indexes)
print(circle_letter_dict)

jumble_combinations = final_combinations(circle_letter_dict)
print(jumble_combinations)

for combo in jumble_combinations:
    print(final_word_combinations(combo, len(combo)))


print("Farley rolled on the barn floor because of his 'in-stinks'")