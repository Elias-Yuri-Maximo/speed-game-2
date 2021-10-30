from game import constants
from game.actor import Actor
from game.point import Point
import random


class Word(Actor):
    """The responsibility of Word is keep track of this word segments. It contains starting the movement.

    Stereotype:
        Information Holder

    Attributes:
        _text (List): The word as a string
    """

    def __init__(self, library):
        """The class constructor.

        Args:
            self (Word): An instance of word.
        """
        super().__init__()

        self._word_list = library
        # should save the word list here
        # THIS IS JUST A PLACEHOLDER, NUMBER SHOULD BE GENERATED RANDOMLY
        self._position = Point(x=random.randint(
            1, (constants.MAX_X - 2)), y=random.randint(1, (constants.MAX_Y - 2)))

        self._velocity = Point(0, 1)
        self._text = self._prepare_word()

    def _prepare_word(self):
        """Gets the word from the word list and equals it to self.text

        Args:
            self (Snake): an instance of Snake.
        """
        # THIS IS JUST A PLACEHOLDER, THIS SHOULD GET A WORD FROM _WORD_LIST

        word = random.choice(self._word_list)
       
        return word
