import re
from collections import Counter


class Dictionary:

    def __init__(self, filename, length):
        self.filename = filename
        self.length = length
        self.word_list = []
        self.count = Counter()

        file1 = open(filename, 'r', encoding='utf-8')
        lines = file1.readlines()

        print(len(lines))

        for line in lines:
            line = re.sub('[^\w]+', '', line)
            line = line.lower()
            if len(line) == length:
                self.word_list.append(line)
                self.count.update([letter for letter in line])

    def score(self, word, round):
        score = 0;
        vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'å', 'ä', 'ö']
        for letter in word:
            score += (self.count[letter] * 2 if letter in vowels else 1) / word.count(letter) ** round
        return score

    def get_suggestions(self, n, round_nr=5):
        self.word_list = sorted(self.word_list, key=lambda x: -self.score(x, round_nr))
        return self.word_list[:n]

    def update_list(self, possible_letters_per_space, contained_letters):

        new_list = []
        self.count = Counter()

        for word in self.word_list:
            add_word = True
            for i, letter in enumerate(word):
                if letter not in (possible_letters_per_space[i]):
                    add_word = False
                    break
            if add_word:
                new_list.append(word)

        self.word_list = []

        for word in new_list:
            add_word = True
            for letter in contained_letters:
                if letter not in word:
                    add_word = False
            if add_word:
                self.word_list.append(word)

