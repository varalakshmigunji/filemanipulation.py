def count_word_occurrences(file_path):
    word_count = {}
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                # Removing punctuation and converting to lowercase
                word = word.strip('.,!?"\'').lower()
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

    # Sorting the word count dictionary alphabetically by keys
    sorted_word_count = sorted(word_count.items())

    # Displaying the results
    for word, count in sorted_word_count:
        print(f"{word}: {count}")
file_path = "D:/file.txt"  
count_word_occurrences(file_path)