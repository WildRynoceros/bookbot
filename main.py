def open_book(fname):
    with open(fname) as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
    split_text = text.split()
    return len(split_text)

def count_characters(text):
    lower_text = text.lower()
    char_set = list(set(lower_text))
    return {char: lower_text.count(char) for char in char_set}

def print_report(fname='books/frankenstein.txt'):
    contents = open_book(fname)
    word_count = count_words(contents)
    char_count = count_characters(contents)

    sorted_char_count = dict(sorted(char_count.items(), key=lambda item: item[1], reverse=True))

    print(f'--- Begin report of {fname} ---')
    print(f'{word_count} words found in the document\n')

    for char, count in sorted_char_count.items():
        if char.isalpha():
            print(f"The character '{char}' was found {count} times")
    
    print('--- End report ---')


def main():
    print_report()

main()