def count_words(text):
    words = text.split()
    return len(words)

def char_counter(text):
    counts = {}
    for char in text.lower():
        counts[char] = counts.get(char, 0) + 1

    return counts

test_dictionary = {"t" : 29493, "h": 19176, "e": 44538}
#test_dictionary_list =[{"char": "t", "num", 29493}, {"char": "h", "num", 19176}, {"char": "t", "num", 445383}]

def get_num_key(item):
    return item["num"]

def create_list_of_dictionaries(dictionary):

    list_of_dictionaries = []
    new_dictionary ={}

    for key, value in dictionary.items():
        new_dictionary = {"char" : key, "num" : value}
        list_of_dictionaries.append(new_dictionary)
    
    list_of_dictionaries.sort(reverse = True, key = get_num_key)
    return list_of_dictionaries
    
