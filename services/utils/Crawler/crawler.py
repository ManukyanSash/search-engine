import requests
import parse

def parse_page(url): # TODO: Change function structure
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

        

