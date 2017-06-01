"""Retrieve  and print words from a URL.
FILENAME    :   words.py
AUTHOR      :   Robert James Patterson
DATE        :   05/01/2017
USAGE       :   python words.py <URL>
"""
import sys
from urllib.request import urlopen

def fetch_words(url):
    """Fetch a list of words from a URL.
    
        Args:
            url: The URL of a UTF-8 text
            
        Returns:
            A list of strings containg the words from the fetched document at the given URL.
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_item(items):
    """Print items one per line.
    
        Args:
            items: An iterable series of printable items.
    """
    for item in items:
        print(item)
    return None


def main(url):
    """Print each word from a text document found at the URL.
        
     Args: 
        url: The URL of an UTF-8 text document. 
    """
    words = fetch_words(url)
    print_item(words)
    return None


if __name__ == '__main__':
    main(sys.argv[1])
