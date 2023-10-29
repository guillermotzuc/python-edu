import argparse
def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', help='the path to the export file')
    parser.add_argument('--format', default='json', choices=['json', 'csv'], type=str.lower)
    return parser

# Inside here, we're going simply import some things.
# They'll only import though if someone runs the main
# function. If someone just runs the create_parser
# function on its own, then these will NOT be imported.
def main():

    import sys

    # Here, we want to import the export and users modules
    from hr import export, users

    # We're importing as u, because users is probably what
    # the list will be named.
    from hr import users as u

    # Here we're going to create a parser, and immediately
    # have it start parsing the args, so that we have access
    # to the args.
    args = create_parser().parse_args()

    # This reads in the user information (from the pwd module
    # that we used in users.py).
    users = u.fetch_users()

    # Now for some conditional logic, based on the path that's
    # passed in, to determine the file that we're using, and
    # and the format that's passed in, so that we know how to
    # export it

    # The first argument is going to be the path.
    if args.path:

        # If the path is present at all, we're going to open the file,
        # make sure it's writable, and set the newline to be an empty
        # string. We don't want any extra strings or characters in what
        # we're doing.
        file = open(args.path, 'w', newline='')

    # If we're NOT writing to a file, then the output is going to
    # be STDOUT
    else:
        file = sys.stdout

    # This is where the writing will actually happen. Our first part
    # if the if/else will be testing for whether we're dealing with
    # JSON or not. If it is (which is the default), then we'll call the
    # export module to_json_file and write users out to the file in
    # JSON format.
    if args.format == 'json':
        export.to_json_file(file, users)

    # And if it's not JSON, then we're planning on it being csv. We'll
    # call the export module to_csv_file and write out users to the
    # file in csv format.
    else:
        export.to_csv_file(file, users)
