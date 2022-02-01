from typing import List, Dict


def read_words(filename: str = "words5.txt") -> List:
    words = []
    with open(filename, 'r') as f:
        for line in f:
            words.append(line.strip())

    return words


def check_score(guess: str, result: str) -> str:
    retval = ''
    for i in range(len(guess)):
        if guess[i] == result[i]:
            retval += '2'
        elif guess[i] in result:
            retval += '1'
        else:
            retval += '0'

    return retval


def check_previous_words(p_words: Dict, current_word: str) -> bool:
    for word, score in p_words.items():
        current_score = check_score(word, current_word)
        if current_score != score:
            return False
        else:
            continue

    return True


def get_score(word: str) -> str:
    retval = input(f"{word}: ")

    return retval


if __name__ == '__main__':
    words = read_words()
    p_words = {}

    for word in words:
        if check_previous_words(p_words, word):
            current_score = get_score(word)
            if current_score == '22222':
                print(f"Word found: {word}")
                exit()
            else:
                p_words[word] = current_score

    print("Cannot find the word!")
    exit()
