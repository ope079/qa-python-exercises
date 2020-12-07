def seperated(words):
    list_words = words.split(" ")
    sorted_words = sorted(list_words)
    set_words = set(sorted_words)
    final_string = " ".join(sorted(list(set_words)))
    return final_string
