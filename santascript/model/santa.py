from santascript.model.gift_recipient import GiftRecipient
from santascript.model.person import Person


class Santa(Person):

    def __init__(self, name, family_name):
        super(Santa, self).__init__(name, family_name)
        self._gift_recipients = []

    def _is_already_gifting(self, gift_recipient: GiftRecipient) -> bool:
        """
        Check to see if the specified recipient is already being gifted by this Santa.
        :param gift_recipient: Gift recipient to check
        :return: Whether or not this person has already been selected by this Santa
        """
        return gift_recipient.get_name() in self._gift_recipients

    def _is_related(self, person: GiftRecipient) -> bool:
        """
        Check to see if the specified recipient is related to this Santa
        :param person: Gift recipient to check
        :return: Whether or not the two are related (same family name)
        """
        return self._family_name == person.get_family_name()

    def add_recipient(self, gift_recipient: GiftRecipient) -> None:
        """
        Add a new recipient to this Santa's list
        :param gift_recipient: Gift recipient to add
        :return:
        """
        self._gift_recipients.append(gift_recipient.get_name())

    def should_give_gift_to_person(self, gift_recipient: GiftRecipient) -> bool:
        """
        Assess whether or not the gift recipient should be eligible for this Santa
        :param gift_recipient: Gift recipient to check
        :return: Whether or not the recipient is eligible for this Santa
        """
        already_gifting = self._is_already_gifting(gift_recipient)
        related = self._is_related(gift_recipient)
        return not related and not already_gifting

    def __str__(self):
        """
        This feels like an abuse of the __str__ functionality but sometimes you just have to #YOLO.
        :return: String representation of this Secret Santa's assignment
        """
        to_print = '{}: {}'.format(self._name, self._gift_recipients)
        return to_print