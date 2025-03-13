def word_count(text: str) -> dict:
    words = text.lower().split()
    frequency = {}

    for word in words:
        word = word.strip(",.!?")
        frequency[word] = frequency.get(word, 0) + 1

    return frequency

text = "Python is great and Python is easy"
result = word_count(text)
print(result)
