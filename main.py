from stats import count_words
from stats import char_counter

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    
    return file_contents



def main(): 
    text = get_book_text("books/frankenstein.txt")
    
    num_words = count_words(text)
    print(f"Found {num_words} total words")
    print(char_counter(text))

main()