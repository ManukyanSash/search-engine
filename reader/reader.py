import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from settings import DOCUMENTS_FILE, INDEX_FILE

def read_documents():
    content = dict()
    with open(DOCUMENTS_FILE, 'r') as file:
        for line in file:
            line = line.strip()
            if line.find(' ') == -1 or line[0].isdigit() == 0:
                continue
            index = int(line.split(' ')[0].strip())
            link = line.split(' ')[1].strip()
            content[index] = link
    return content

def add_to_documents(link):
    content = read_documents()
    index = 1
    if len(content.keys()) > 0:
        index = max(list(content.keys())) + 1
    with open(DOCUMENTS_FILE, 'a') as file:
        file.write('\n' + str(index) + ' ' + link)

def update_documents(index, link):
    content = read_documents()
    content[index] = link 
    with open(DOCUMENTS_FILE, 'w') as file:
        for index in content:
            file.write(str(index) + ' ' + content[index] + '\n')
