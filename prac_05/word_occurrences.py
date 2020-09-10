word_occurrences = {}
word_length = 0
text = input("text: ")
spilt_text = text.split()
spilt_text.sort()
for text in spilt_text:
    text_count = spilt_text.count(text)
    word_occurrences[text] = text_count
    if len(text) > word_length:
        word_length = len(text)
print(word_occurrences)
for entry in word_occurrences:
    print("{0:{2}} : {1}".format(entry, word_occurrences[entry], word_length))
