import csv

from santascript.model.gift_recipient import GiftRecipient
from santascript.model.santa import Santa


GIFT_RECIPIENT = 'Santee'
SANTA = 'Santa'
EXEMPT = 'Exempt'


class InvalidSantaTypeException(Exception):

    pass


def parse_family_tree(path_to_family_tree: str) -> (list, list):
    """
    Parses a CSV file into native Santa and GiftRecipient models and packs them into lists.
    :param path_to_family_tree: The path to the family tree CSV
    :return: Tuple of Secret Santa list and Gift Recipient list
    """
    secret_santas = []
    gift_recipients = []
    with open(path_to_family_tree, 'r') as family_tree_file:
        family_tree_parser = csv.reader(family_tree_file)
        for row in family_tree_parser:
            name, family_name, type = row
            if type == GIFT_RECIPIENT:
                gift_recipient = GiftRecipient(name, family_name)
                gift_recipients.append(gift_recipient)
            elif type == SANTA:
                santa = Santa(name, family_name)
                secret_santas.append(santa)
            elif type == EXEMPT:
                pass
            else:
                raise InvalidSantaTypeException('Unrecognized person type: {}'.format(type))
    return secret_santas, gift_recipients
