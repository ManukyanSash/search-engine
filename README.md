# Search Engine

Welcome to the Search Engine project! This search engine allows users to parse website pages, index their content, and search for specific words within the indexed pages. It utilizes a combination of server-side logic in Python, HTML/CSS, and JavaScript for the frontend. The project incorporates autocorrect and autocompletion features for an enhanced user experience.

## Features

- Parsing: The search engine can parse website pages to extract their content using a crawler.
- Indexing: The content of parsed pages is indexed using the Indexer, which assigns each word to the corresponding webpage in the index.txt file.
- Searching: Users can search for specific words within the indexed pages, similar to Google Search.
- Autocorrect: The search engine provides autocorrect functionality using the Levenshtein algorithm, which suggests corrections for mistyped or misspelled words.
- Autocompletion: Autocompletion is implemented using a prefix tree (trie) data structure, enabling users to get word suggestions as they type.

## Components

- Server Side: The server side of the Search Engine is implemented in Python. It includes the crawler for parsing web pages, the indexer for indexing the content, and the search functionality.
- Frontend: The frontend of the Search Engine is developed using HTML, CSS, and JavaScript. It provides the user interface for interacting with the search engine and displaying search results.
- Autocorrect: The autocorrect feature is implemented using the Levenshtein algorithm in Python to suggest corrections for mistyped words.
- Autocompletion: The autocompletion feature is implemented using a prefix tree (trie) data structure in Python, providing word suggestions as the user types.

## Getting Started

1. Clone the repository:

```shell
git clone https://github.com/ManukyanSash/search-engine  
```

2. Install the required dependencies. Make sure you have Python and the necessary libraries installed.

3. Start the server by running the server.py file:

```shell
python3 main.app
```