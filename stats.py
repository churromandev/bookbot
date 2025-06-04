def get_word_count(booktext):
   return len(booktext.split())

def get_char_counts(booktext):
    char_count_dict = {}
    booktext = booktext.lower()
    word_list = booktext.split()
    for word in word_list:
        for char in word:
            char_count_dict.setdefault(char, 0)
            char_count_dict[char] += 1
    return char_count_dict

def create_sorted_list(dict):
    sorted_list = []
    for char_key in dict:
        if char_key.isalpha():
            new_dict = {"char": char_key, "num": dict[char_key]}
            sorted_list.append(new_dict)
    sorted_list.sort(key=lambda dict: dict["num"], reverse=True)
    return sorted_list
	
