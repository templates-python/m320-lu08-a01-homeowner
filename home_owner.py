class HomeOwner:
    """
    The owner of a house.

    Attributes
    ----------
    name: String
        The full name of the homeowner.
    my_house: House
        The house this person owns
    """

    def __init__(self, name, house):
        """
        Creates an object with the name and a reference to the house

        :param name: Full name of the homeowner.
        :param house: Reference to a house.
        """
        self._name = name
        self._my_house = house

    @property
    def name(self):
        """ Returns the full name. """
        return self._name

    def __str__(self):
        """
        Returns a string with information about the owner and his house.
        """
        return f'{self._name} besitzt ein {self._my_house.type}'
