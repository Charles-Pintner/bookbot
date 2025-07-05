def get_num_words(text_to_count):
    words = text_to_count.split()
    num_words = len(words)
    return num_words
def count_characters(text):
    char_counts = {}
    for i in text:
        char_lower = i.lower()
        if char_lower in char_counts:
            char_counts[char_lower] += 1
        else:
            char_counts[char_lower] = 1
    return char_counts
def sort_on(char_counts):
    return char_counts["num"]
def convert_and_sort_chars(char_counts):
    char_list = []
    for char, count in char_counts.items():
        char_dict = {"char": char, "num": count}
        char_list.append(char_dict)
    char_list.sort(reverse=True, key=sort_on)
    return char_list