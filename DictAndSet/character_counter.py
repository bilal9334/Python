word_count = {}

text = "Later in the course, you'll see how to use the collection Counter class."

for char in text.casefold():
    if char.isalnum():
        word_count[char] = word_count.setdefault(char, 0) + 1

for letter, count in sorted(word_count.items()):
    print(letter, count)
