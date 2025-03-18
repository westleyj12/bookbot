def word_count(book_contents):
    return(len(book_contents.split()))

def character_count(book_contents):
    # Generate dictionary to store characters
    character_count = {}
    # Make a list where each item is a character from the book. All letters are turned to lowercase
    book_contents_characters = list(book_contents.lower())
    # Iterate through all letters. If letter not in dictionary, add it, otherwise increase index for that letter
    for letter in book_contents_characters:
        if letter in character_count:
            character_count[letter] += 1
        else:
            character_count[letter] = 1
    return character_count

def sort_on(dict):
    return dict["count"]

def character_sort(character_count):
    character_sorted_list = []
    for character in character_count:
        if character.isalpha():
            character_sorted = {"character": character,
                                "count": character_count[character]}
            character_sorted_list.append(character_sorted)
        else:
            continue
    character_sorted_list.sort(reverse=True, key=sort_on)
    return character_sorted_list

