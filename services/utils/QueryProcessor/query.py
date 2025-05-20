import os
import sys
import ast
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append("Indexer")
sys.path.append("Crawler")
from Crawler.crawler import parse_page
from Indexer.indexer import normalizing, whole_process
from settings import DOCUMENTS_FILE, INDEX_FILE, WORDS_DB_FILE

def get_words_indexes(str):
    w_list = str.strip().split(' ')
    words = normalizing(w_list, WORDS_DB_FILE)
    indexes = list()
    with open(INDEX_FILE, 'r') as file:
        for word in words:
            for line in file:
                if word in line:
                    indexes += list(ast.literal_eval(line.strip().split(':')[1].strip()))
                    break
    return indexes

def get_words_links(indexes):
    links = list()
    with open(DOCUMENTS_FILE, 'r') as file:
        for index in indexes:
            for line in file:
                if int(line[0]) == int(index):
                    links.append(line.strip().split(' ')[1])
                break
    return links 

def add_page(link):
    parse_page(link)
    whole_process('log.txt')
