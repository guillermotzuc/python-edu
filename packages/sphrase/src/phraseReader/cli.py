import argparse
def create_parser():
    parser = argparse.ArgumentParser()
    # parser.add_argument('--path', help='the path to the export file')
    # parser.add_argument('--format', default='json', choices=['json', 'csv'], type=str.lower)
    return parser

# Inside here, we're going simply import some things.
# They'll only import though if someone runs the main
# function. If someone just runs the create_parser
# function on its own, then these will NOT be imported.
def main():

    import sys

    # Here, we want to import the export and users modules
    from phraseReader import PhraseReader as phraseReader

    # Here we're going to create a parser, and immediately
    # have it start parsing the args, so that we have access
    # to the args.
    args = create_parser().parse_args()

    # This reads in the user information (from the pwd module
    # that we used in users.py).
    stoicPhrase = phraseReader.fetch_phrase()
    print(stoicPhrase['phrase'])
    file = sys.stdout
    
