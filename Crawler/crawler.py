import os
import sys
import requests
import parse
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append("reader")
from reader.reader import add_to_documents

def parse_page(url):
    print("A")
    content = ""
    try:
        response = requests.get(url)
        if response.status_code == 200:
            content = parse.parse_url(response)
        else:
            print("Request failed with status code:", response.status_code)

    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

    finally:
        with open("log.txt", "w") as file:
            file.write(content)
        add_to_documents(url)

        

