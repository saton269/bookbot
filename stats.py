def count_words(text):
    num_words = text.split()
    word_count = len(num_words)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    #return word_count

def count_chrs(text):
    characters = {}
    print("--------- Character Count -------")
    for t in text:
        convert_to_lower = t.lower()
        if(convert_to_lower in characters):
            count = characters[convert_to_lower]
            count += 1
            characters[convert_to_lower] = count
        else:
            characters[convert_to_lower] = 1
        #print(convert_to_lower)
        #return convert_to_lower
    return characters

def sort_on(items): # This function takes one item (a dictionary)
    return items["num"]

def report(dictionary):
    dictionaries = []
    for item in dictionary:
        num = dictionary[item]
        small_dictionary = {}
        small_dictionary["char"] = item
        small_dictionary["num"] = num
        dictionaries.append(small_dictionary)
    dictionaries.sort(reverse=True, key=sort_on)
    print()
    for diction in dictionaries:
        if diction["char"].isalpha():
            print(f"{diction['char']}: {diction['num']}")
    #print(dictionaries)
    print("============= END ===============")