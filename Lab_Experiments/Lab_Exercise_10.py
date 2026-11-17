# Input a sentence
sentence = input("Enter a sentence: ")
# Convert sentence to lowercase and split into words
words = sentence.lower().split()
# Dictionary to store word frequencies
frequency = {}
# Count the frequency of each word
for word in words:
    word = word.strip(".,!?;:\"'()[]{}")
    if word:
        frequency[word] = frequency.get(word, 0) + 1
# Display the frequency of each word
print("\nWord Frequency:")
for word, count in frequency.items():
    print(word, ":", count)
