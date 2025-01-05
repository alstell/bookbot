def main():
    book_path = "books/frankenstein.txt"
    
    with open(book_path) as f:
        book_text = f.read()
        wordcount = (wordcounter(book_text))
        sorted_char_count = convert_count(charcount(book_text))
        print_report(book_path, wordcount, sorted_char_count)

def wordcounter(text):
    return len(text.split())

def charcount(text):
    char_count = {}
    lower_text = text.lower()

    for char in lower_text:
        if(char not in char_count):
            char_count[char] = 1
        else:
            char_count[char] += 1
    
    return(char_count)

def convert_count(charcount_dict):
    pass

def sort_on(dict):
    pass

def print_report(book, wordcount, sorted_char_list):
    print(f"***** Begin report of {book} *****")

main()

