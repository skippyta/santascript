from collections import Counter
import random


def draw(secret_santas: list, gift_recipients: list, num_gifts=2) -> None:
    """
    Simulate the actual drawing of Secret Santa gift recipients and print
    :param secret_santas: A list of Santa objects
    :param gift_recipients:  A list of GiftRecipient objects
    :param num_gifts: Number of to be received by each recipient. Uniform for now.
    :return:
    """
    # This is my bogus way of simulating a hat draw. Just shuffle the list and run it through.
    random.shuffle(secret_santas)
    random.shuffle(gift_recipients)
    gift_counter = Counter()

    # Keep drawing while we still have people who need to hit allotted gift number
    while gift_recipients:
        # Pass through the Secret Santa candidates in turn (shuffled) so we get a mostly-balanced draw
        for santa in secret_santas:
            """
            Iterate over the list of recipients and break when we get a good match
            Doing it this way prevents infinite looping problem that could be encountered
            by doing random selection
            """
            for recipient in gift_recipients:
                if santa.should_give_gift_to_person(recipient):
                    santa.add_recipient(recipient)
                    recipient_name = recipient.get_name()
                    gift_counter[recipient_name] += 1
                    if gift_counter[recipient_name] == num_gifts:
                        gift_recipients.remove(recipient)
                    break
        # Shuffle between draws so we don't end up with static ordering.
        random.shuffle(secret_santas)
        random.shuffle(gift_recipients)

    for santa in secret_santas:
        print(santa)
