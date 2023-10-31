from phraseReader import config

def fetch_phrase():
    """
    Get a random phrase from a file
    >>> phrase = fetch_phrase()
    >>> phrase is not None
    True
    """
    
    import json
    import random

    with open(config.PHRASE_PATH, 'r+') as json_file:
        json_content = json_file.read()
        phrase_json = json.loads(json_content)
        return random.choice(phrase_json)
        
    return "There aren't any phrase roght now, sorry."

#if __name__ == "__main__":
#    import doctest
#    doctest.testmod()
# python -m doctest -v /home/gtzuc/Documents/code/python-edu/packages/stoic-phrase/src/phraseReader/PhraseReader.py
#