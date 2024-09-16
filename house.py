class House:
    """
    A house of a certain type

    Attributes
    ----------
    type: String
        The type of the house ('Landhaus', 'Stadthaus', ...)
    """

    def __init__(self, name='Landhaus'):
        """
        Creates the object with the specified type
        """
        self._type = name

    @property
    def type(self):
        """ Returns the type of the house """
        return self._type