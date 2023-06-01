import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append("structures")
from structures.trie import Trie 
from settings import WORDS_DB_FILE

def fill_trie():
    tree = Trie()
    with open(WORDS_DB_FILE, 'r') as file:
        for word in file:
            tree.insert(word.strip())
    
    return tree

