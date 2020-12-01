entry_word = input("Please enter your word here? ")

def conjugation(entry_word):
    words = []
    english_words = open('words.txt')
    for word in english_words:
        clean_word = word.strip('\n')
        words.append(''.join(clean_word))

    count = 0
    for i in words:
        if i in entry_word:
            count += 1

    return count

print(conjugation(entry_word))