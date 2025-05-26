from stats import get_num_words, count_chars, present_chars
import sys

def get_book_text(filepath: str):
    content = None
    with open(filepath) as f:
        content = f.read()

    return content

def main():

    try:
        fpath = sys.argv[1]
    except Exception as e:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    content = get_book_text(fpath)
    char_dict = count_chars(fpath)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {fpath}...")
    print(f"----------- Word Count ----------")
    print(f"Found {get_num_words(content)} total words")
    print("--------- Character Count -------")
    present_chars(char_dict)

main()