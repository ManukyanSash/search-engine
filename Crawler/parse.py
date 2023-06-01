import re
from bs4 import BeautifulSoup

def parse_url(response):
    soup = BeautifulSoup(response.text, 'html.parser')
    text_content = soup.get_text()
    text_content = text_content.replace('\n', ' ')
    text_content = re.sub(' +', ' ', text_content)
    return text_content

def parse_log(log_file):
    res = list()
    with open(log_file, 'r') as file:
        content = file.read()
        res = content.strip().split(' ')
    return res