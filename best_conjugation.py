
words = []
english_words = open('words.txt')
for word in english_words:
    clean_word = word.strip('\n')
    words.append(''.join(clean_word))


entry_word = input("Please enter your word here? ")
list_word = list(entry_word)
count = 0

for i in words:
    if i in entry_word:
        print(i)
        count += 1

print(count)