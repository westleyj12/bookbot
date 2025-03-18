from stats import word_count, character_count, character_sort
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        book_contents = f.read()
    return book_contents

def main():
    # file_path = "books/frankenstein.txt"
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_contents = get_book_text(sys.argv[1])
        character_dict = character_count(book_contents)
        character_sorted_list = character_sort(character_dict)
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(f"Found {word_count(book_contents)} total words")
        print("--------- Character Count -------")
        for character in character_sorted_list:    
            print(f"{character["character"]}: {character["count"]}")
        print("============= END ===============")
    
main()