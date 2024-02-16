def main():
    book = "books/frankenstein.txt"
    with open(book) as f:
        file_contents = f.read()
    number_of_words = count_words(file_contents)
    number_of_letters = count_letters(file_contents)
    report(book, number_of_words, number_of_letters)


def count_words(file_contents):
    number_of_words = len(file_contents.split())
    return number_of_words


def sort_on(dict):
    return dict["count"]


def count_letters(file_contents):
    lower_case_text = file_contents.lower()
    number_of_letters = {}
    list_of_letters = []

    for i in lower_case_text:
        if i.isalpha() and i in number_of_letters:
            number_of_letters[i] = number_of_letters[i] + 1
        elif i.isalpha():
            number_of_letters[i] = 1

    for i in number_of_letters:
        dict_item = {"letter": i, "count": number_of_letters[i]}
        list_of_letters.append(dict_item)
        print(list_of_letters)

    list_of_letters.sort(reverse = True, key = sort_on)
    return list_of_letters


def report(book, number_of_words, number_of_letters):
    print(f"--- Start of the report of {book} ---")
    print(f"{number_of_words} words were found in the document.")
    print()

    for i in number_of_letters:
        print(f"Letter '{i["letter"]}' was found {i["count"]} times.")
    
    print("--- End of report --- ")


main()