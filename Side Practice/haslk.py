def get_ordinal(word):
    ord_total = 0
    for char in word:
        ord_total += ord(char)
    return ord_total

def group_anagrams(path):
    try:
        list_words = []
        with open(path, 'r') as file:
            for line in file:
                word = line.strip()
                list_words.append(word)

        anagrams = []
        not_anagrams = []
        i = 0
        length = len(list_words)

        while i < length:
            iword = list_words[i]
            ana_list = [iword]
            j = i + 1  # Start j from i+1 to avoid re-checking words
            found_anagram = False  # Flag to track if an anagram is found for iword
            while j < length:
                jword = list_words[j]
                if get_ordinal(iword) == get_ordinal(jword):
                    ana_list.append(jword)
                    list_words.pop(j)
                    length -= 1  # Update length after removing an anagram
                    found_anagram = True  # Set flag to true if an anagram is found
                else:
                    j += 1  # Increment j only when not removing a word

            if not found_anagram:
                not_anagrams.append(iword)
                i += 1  # Increment i only when a non-anagram is found
            else:
                if len(ana_list) > 1:
                    anagrams.append(ana_list)

        # Append remaining non-anagrams
        if not_anagrams:
            anagrams.append([not_anagrams.pop()])  # Append the last non-anagram to anagrams

        return anagrams

    except FileNotFoundError:
        print("Unable to read the file. Please check the file path.")
        return None

anagrams = group_anagrams("hw_text1.txt")
print(anagrams)
