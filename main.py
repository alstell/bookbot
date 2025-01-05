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
    char_count_list = []
    for key in charcount_dict:
        if key.isalpha():
            temp_dict = {}
            temp_dict["letter"] = key
            temp_dict["count"] = charcount_dict[key]
            char_count_list.append(temp_dict)
    
    char_count_list.sort(reverse=True, key=sort_on)
    return char_count_list


def sort_on(dict):
    return dict["count"]


def print_report(book, wordcount, sorted_char_list):
    print(f"***** Begin report of {book} *****")
    print("\n-----------------------------------")
    print(f"{wordcount} words found in the document")
    print("-----------------------------------")
    print("\n----------------------------------------------")
    print("Character list sorted from most to least used\n")
    for dict in sorted_char_list:
        print(f"The '{dict["letter"]}' character was found {dict["count"]} times")
    print("----------------------------------------\n")
    print(f"***** End report of {book} *****")

main()

