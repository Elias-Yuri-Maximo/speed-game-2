
import random
from game import constants
from game.actor import Actor
from game.point import Point
from game.constants import MAX_X, MAX_Y

class Buffer(Actor):

    '''
    this function will receive and store the state of the buffer, it 
    will alse be able to reset it when needed'''

    def __init__(self):
        
        super().__init__() 
        self._buffer_letter_list = []  
        self._text = ''
        self._character = ''
        self.reset()

    def reset(self):
        '''
        This function will reset the buffer text to [] 
        '''
        self._buffer_letter_list = []  

    def add_character(self, character):
        '''
        This function will add a character from what the player has typed.
        '''
        self._buffer_letter_list.append(character)

    def to_string(self):
        self._text = str(self._buffer_letter_list)
        '''
        passes the chacter list to a string and saves it to _TEXT attribute
        '''