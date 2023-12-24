input_string = input("Enter a string:-")

frequency = {}
words = input_string.split()

for word in words:
    if word != '':
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

print("Word frequencies:")
for word, freq in frequency.items():
    print(f"{word}: {freq}")
