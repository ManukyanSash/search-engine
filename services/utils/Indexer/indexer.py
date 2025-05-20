import os
import sys
import ast
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append("structures")
sys.path.append("reader")
from reader.reader import read_documents
from structures.Levinshtein import levinshtein_distance
from settings import INDEX_FILE, WORDS_DB_FILE

def tokenizing(input_file):
    res = list() 
    with open(input_file, 'r') as file:
        res = file.read().strip().split(' ') 
    print(res)
    return res

def normalizing(words_list, db_file):
    res_list = list()
    for word in words_list:
        min_diff = len(word)
        min_word = word
        with open(db_file, 'r') as file:
            for line in file:
                cmp_word = line.strip()
                diff = levinshtein_distance(word, cmp_word)
                if diff == 0:
                    min_word = cmp_word
                    break
                if min_diff > diff:
                    min_diff = diff
                    min_word = cmp_word
            res_list.append(min_word)
    return res_list

def indexing(words_list, link_index):
    words_dict = dict()
    with open(INDEX_FILE, 'r') as file:
        for line in file:
            if len(line) > 1:
                word = line.strip().split(":")[0].strip()
                word_indexes = ast.literal_eval(line.strip().split(":")[1].strip())
                word_indexes = list(word_indexes)
                words_dict[word] = word_indexes

    for word in words_list:
        if word in words_dict:
            words_dict[word].append(link_index)
        else:
            words_dict[word] = [link_index]
    
    with open(INDEX_FILE, 'w') as file:
        for word in words_dict:
            file.write(word + ' : ' + str(list(set(words_dict[word]))) + '\n')

def whole_process(input_file):
    tokens = tokenizing(input_file)
    normal_words = normalizing(tokens, WORDS_DB_FILE)
    index = max(read_documents().keys())
    indexing(normal_words, index)