"""
CP1404 - Prac 5
Task - Word Occurrences
Estimate - 25 mins
Actual   - 28 mins
"""

user_string = input("Enter a phrase/sentence: ").lower()

for character in ",.!?;:":
     user_string = user_string.replace(character, "") # Remove punctuation from words

words = user_string.split()
word_counter = {}

for word in words:
    if word in word_counter:
        word_counter[word] += 1
    else:
        word_counter[word] = 1

longest_word = max(len(word) for word in word_counter)
for word in sorted(word_counter):
    print(f"{word:{longest_word}} - {word_counter[word]}")
