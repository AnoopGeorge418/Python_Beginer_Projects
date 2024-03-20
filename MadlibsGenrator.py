# MadlibGenerator Explaination :- https://chat.openai.com/share/2d892668-a72b-4628-b4e7-ca5dd9a106b0
## USE Story.txt

# Opening .txt file - Using with file closes automatically.
with open('Story.txt', 'r') as file:
    story = file.read() #gives me all the text inside .txt

# Storing words starts and ends with <' '> in a set cause no duplicates needed.
words = set()
staring_index_of_word = -1

target_start = '<'
target_end = '>'

# Here i is the index of elements and char is the elements.
for i, char in enumerate(story):
    if char == target_start:
        staring_index_of_word = i

    if char == target_end and staring_index_of_word != -1:
        word = story[staring_index_of_word: i + 1] # slicing
        words.add(word)
        staring_index_of_word = -1

# Getting answer from users for words and storing it in dictionary
answers = {}

for word in words:
    answer = input(f'Enter a word for {word}: ')
    answers[word] = answer.lower()

# replacing words in story
for word in words:
    story = story.replace(word, answers[word])

print(story)
