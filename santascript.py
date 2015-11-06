import sys

from santascript.util import family_tree_parser, secret_santa_drawer


if __name__ == '__main__':
    family_tree_csv_path = sys.argv[1]
    num_gifts = int(sys.argv[2])

    secret_santas, gift_recipients = family_tree_parser.parse_family_tree(family_tree_csv_path)
    secret_santa_drawer.draw(secret_santas, gift_recipients, num_gifts)