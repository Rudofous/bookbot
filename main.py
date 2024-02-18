def main():
    book = "books/frankenstein.txt"
    with open(book) as f:
        file_contents = f.read()
    report(book, count_words(file_contents), count_letters(file_contents))

# A function to count words in the provided text
def count_words(file_contents):
    number_of_words = len(file_contents.split())
    return number_of_words

# A function for sorting
def sort_on(dict):
    return dict["count"]

# A function to count letters
def count_letters(file_contents):
    lower_case_text = file_contents.lower()
    number_of_letters = {}
    list_of_letters = []

    # Counting only alphabetical letters, filling a dictionary
    for i in lower_case_text:
        if i.isalpha() and i in number_of_letters:
            number_of_letters[i] = number_of_letters[i] + 1
        elif i.isalpha():
            number_of_letters[i] = 1

    # Making a list of dictionaries
    for i in number_of_letters:
        dict_item = {"letter": i, "count": number_of_letters[i]}
        list_of_letters.append(dict_item)

    # Sorting the list
    list_of_letters.sort(reverse = True, key = sort_on)
    return list_of_letters

# A function to print out the report
def report(book, number_of_words, number_of_letters):
    print(f"--- Start of the report of {book} ---")
    print()
    print(f"{number_of_words} words were found in the document.")
    print()

    for i in number_of_letters:
        print(f"Letter '{i["letter"]}' was found {i["count"]} times.")

    print()
    print("--- End of report --- ")


main()