import sys
from collections import defaultdict


# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["count"]


def print_report(char_count_list, count, file_path):
    
    print(f"--- Begin report of {file_path} ---")
    print(f"{count} words found in the document")
    print(f"\n")
    

    for entry in char_count_list:
        char = entry['char']
        count = entry['count']
        if char.isalpha():
            print(f"The {entry['char']} character was found {entry['count']} times")

    print(f"--- End Report ---")




def main():
    if (len(sys.argv) < 2):
        print("please supply a book")

    
    character_count = defaultdict(int)
    char_count_list = []
    word_count = 0

    # Open file
    with open(sys.argv[1]) as f:
        

        # Read contents
        file_contents =f.read()

        # Delimeter by any whitespace
        array_of_words = file_contents.split()
        word_count = len(array_of_words)

        # Count characters
        for string in array_of_words:
            for char in string.lower():
                character_count[char] += 1
    

    # Convert the letter counts to a list of dictionaries 
    char_count_list = [{'char': char, 'count': count} for char, count in character_count.items()]

    char_count_list.sort(reverse=True, key=sort_on)
    #print(char_count_list)
    print_report(char_count_list, word_count, sys.argv[1])
    

if __name__ == "__main__":
    main()