def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"--- Begin report of {book_path}")
    print(f"{num_words} words found in document")
    char_dict = count_characters(text)
    char_list = list_from_dir(char_dict)
    for item in char_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item["char"]}' character was found {item["num"]} tiems")
    print("--- End report ---")


def list_from_dir(char_dict):
    sorted_list = []
    for key in char_dict:
        sorted_list.append({"char": key, "num": char_dict[key]})
    sorted_list.sort(reverse=True, key=lambda x: x["num"])
    return sorted_list


def count_characters(book):
    characters = {}
    for char in book.lower():
        if char not in characters:
            characters[char] = 1
        else:
            characters[char] += 1
    return characters


def get_num_words(book):
    words = book.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
