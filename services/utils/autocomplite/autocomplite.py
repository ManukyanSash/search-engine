import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append("structures")
from ..structures.trie import Trie

def fill_trie(): # TODO: Change this function
    tree = Trie()
    with open(WORDS_DB_FILE, 'r') as file:
        for word in file:
            tree.insert(word.strip())
    
    return tree

