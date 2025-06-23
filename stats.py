def get_num_words(text):
    list_of_words = text.split()
    return len(list_of_words)

def get_char_counts(text):
    char_dict = {}
    list_of_chars = list(text.lower())
    
    for char in list_of_chars:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    
    return char_dict

def sort_on(items):
    return items["num"]

def sort_dict(unsorted_dict):
    sorted_char_list = []
    
    for char in unsorted_dict:
        if char.isalpha():
            sorted_char_list.append({"char": char, "num": unsorted_dict[char]})
    
    sorted_char_list.sort(reverse=True, key=sort_on)

    return sorted_char_list