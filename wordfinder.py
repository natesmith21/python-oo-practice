"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    ...
    def __init__(self, path):
        file = open(path, 'r')
        self.words = self.make_words_list(file)

        print(f'{len(self.words)} words read')

    
    def make_words_list(self, file):
       
       return [w.strip() for w in file] 
        
    def random(self):
        return random.choice(self.words)
        

class RandomWordFinder(WordFinder):
    '''find a word inside a category'''



def make_wordsf_list(self, file):
    return [w.strip() for w in file
            if w.strip() and not w.startswith('#')]

