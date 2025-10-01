from stats import count_words
from stats import char_counter
from stats import create_list_of_dictionaries
import sys



def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    
    return file_contents







def format_char_counts(list):
    lines = []
    for item in list:
        if str(item["char"]).isalpha():
            lines.append( f"{item['char']}: {item['num']}")
    return "\n".join(lines)

       


def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) 
    else: 
        path = sys.argv[1]
        text = get_book_text(path)
        to_be_printed = create_list_of_dictionaries(char_counter(text))
    
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path}...")
        print("----------- Word Count ----------")
        print(f"Found {count_words(text)} total words")
        print("--------- Character Count -------")
        print(format_char_counts(to_be_printed))
        print("============= END ===============")
main()



#path= "books/frankenstein.txt"
#dict = char_counter(get_book_text(path))
#list_of_items = create_list_of_dictionaries(dict)
#convert(list_of_items)