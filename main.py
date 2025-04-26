import sys
from stats import count_words, histo,sort_histo

def get_book_txt(file_path):
    with open(file_path) as f:
        book_text = f.read()
        return book_text


def main():
    print(sys.argv)
    print(len(sys.argv))

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    bookpath = sys.argv[1]
    print(f"Analyzing book found at {bookpath}...")
    text = get_book_txt(bookpath)

    print("----------- Word Count ----------")
    num_words = count_words(text)
    print(f"Found {num_words} total words found")


    print("--------- Character Count -------")
    char_counts = histo(text)
    #print (char_counts)
    sorted = sort_histo(char_counts)

    for item in sorted:
        if item["char"].isalpha():
            c = item["char"]
            num = item["num"]
            print(f"{c}: {num}")
    print("============= END ===============")
    
main()
