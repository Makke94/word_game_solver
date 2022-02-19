# Press the green button in the gutter to run the script.
import copy

from Dictionary import Dictionary


def main():
    lang = int(input("Engelska (1)/svenska (2)"))

    length = int(input("Hur långt är ordet"))

    if lang == 1:
        dict1 = Dictionary("words_alpha.txt", length)
    else:
        dict1 = Dictionary("svenska-ord.txt", length)

    possible_letters_per_space = []
    contained_letters = []
    for i in range(length):
        possible_letters_per_space.append("qwertyuiopåäölkjhgfdsazxcvbnm")

    undecided_letters = list(range(length))

    for round in range(6, 0, -1):
        sugg = dict1.get_suggestions(10, round)
        print(sugg)

        copy_undecided_letters = copy.deepcopy(undecided_letters)

        choice = int(input("Vilket ord valde du 1-10?"))

        word = sugg[choice - 1]

        for i in undecided_letters:
            letter = word[i]
            choice = int(input(f'Bokstaven \'{letter}\' på plats {i + 1}, var den rätt plats (1), rätt bokstav (2), '
                               f'fel bokstav (3)'))
            if choice == 1:
                possible_letters_per_space[i] = letter
                contained_letters.append(letter)
                copy_undecided_letters.remove(i)
            if choice == 2:
                possible_letters_per_space[i] = possible_letters_per_space[i].replace(letter, '')
                contained_letters.append(letter)
            if choice == 3:
                for j in range(length):
                    possible_letters_per_space[j] = possible_letters_per_space[j].replace(letter, '')

        undecided_letters = copy_undecided_letters
        dict1.update_list(possible_letters_per_space, contained_letters)

        if len(undecided_letters) == 0:
            print("GRATTIS")
            return
    print("Tråkig")
    return


if __name__ == '__main__':
    main()
