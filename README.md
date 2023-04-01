# Search Engine

This is a simple search engine program written in Python. It allows you to search for web pages using the Google search engine and filters out results from certain sites.

## Features

- Search for web pages using the Google search engine
- Filter out results from certain sites
- Promote certain sites to the top of the search results

## Requirements

- Python 3.x
- `googlesearch` module (can be installed using pip)

## Installation

1. Clone this repository to your local machine:

		git clone https://github.com/AlmostAnEngineer/TerminalFiltredSearch

2. Install the `googlesearch` module using pip:

		python3 -m pip install googlesearch-python

3. (Optional) Add the project directory to your PATH environment variable to run the program from any directory.

## Usage

1. Enter a search query when prompted by the program.
2. Enter the maximum number of search results you want to see.
3. The program will display the search results in the terminal.

## Customization

If you want to add or remove sites from the list of filtered or promoted sites, you can modify the `forbiddenSitesInResults` and `promotedSites` lists in the `googleSearchFiltered` function in the `search_engine.py` file.

## Credits

This program was created by [AlmostAnEngineer](https://github.com/AlmostAnEngineer).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


