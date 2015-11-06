class Person:

    def __init__(self, name: str, family_name: str):
        self._name = name
        self._family_name = family_name

    def get_name(self) -> str:
        """
        Get this person's name
        :return: This person's name
        """
        return self._name

    def get_family_name(self) -> str:
        """
        Get this person's family name
        :return: This person's family name
        """
        return self._family_name