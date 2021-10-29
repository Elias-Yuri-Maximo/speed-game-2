from game import constants
from game.actor import Actor
from game.point import Point

class Word(Actor):
    """The responsibility of Word is keep track of this word segments. It contains starting the movement.

    Stereotype:
        Information Holder

    Attributes:
        _text (List): The word as a string
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Word): An instance of word.
        """
        super().__init__()
        
        self._word_list = ['','','','','','','','','','','','','']
        #should save the word list here 
        #THIS IS JUST A PLACEHOLDER, NUMBER SHOULD BE GENERATED RANDOMLY
        self._position = Point(1 , 20)
       
        #self._velocity = self. set_velocity(Point(0, 1))
        self._text = self.set_text(self._prepare_word())
        print(self._text)

    
        
    

    def _prepare_word(self):
        """Gets the word from the word list and equals it to self.text
        
        Args:
            self (Snake): an instance of Snake.
        """
        #THIS IS JUST A PLACEHOLDER, THIS SHOULD GET A WORD FROM _WORD_LIST
        word = 'running word'
        return word
        


