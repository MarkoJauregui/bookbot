def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_chars_dict = get_chars_list(chars_dict)
    print(f"--- Begin Report of {book_path} ---")
    print(f"{num_words} words found in the document")
    for char_dict in sorted_chars_dict :
        print(f"The {char_dict['char']} character was found {char_dict['num']} times")
    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def sort_on(dict):
    return dict["num"]

def get_chars_list(chars_dict):
    chars_list = []
    for char, num in chars_dict.items():
        if char.isalpha():
            char_dict = {"char": char, "num": num}
            chars_list.append(char_dict)

    chars_list.sort(reverse=True, key=sort_on)
    return chars_list

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
