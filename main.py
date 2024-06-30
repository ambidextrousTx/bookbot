from collections import Counter


def sort_on(dict):
    return dict['count']


def report(words, character_frequencies):
    print('--- Begin report of books/frankenstein.txt ---')
    print(f'{len(words)} words were found in the document', end='\n\n')
    for occurrence in character_frequencies:
        char = occurrence['char']
        count = occurrence['count']
        if char.isalpha():
            print(f'The \'{char}\' character was found {count} times')

    print('--- End report ---')


def character_occurrences(file_contents):
    freqs = Counter(file_contents)
    occurrences = []
    for freq, count in freqs.items():
        occurrence = {}
        occurrence['char'] = freq
        occurrence['count'] = count
        occurrences.append(occurrence)

    occurrences.sort(reverse=True, key=sort_on)
    return occurrences


def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read().lower()
        words = file_contents.split()

        report(words, character_occurrences(file_contents))


main()
