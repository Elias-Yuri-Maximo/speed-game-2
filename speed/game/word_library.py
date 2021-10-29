from game import constants
from game.actor import Actor
from game.point import Point
from speed.game import word

class WordLibrary:
    '''
    This class is responsible for holding instances of word that will be called and drawn

    steryotype: information holder
    '''
    def __init__(self):
        _word_objects_list = []
        #saves instances of the object word

    def insert_new_word(self, object_word): 
        '''
        gets a new object word and saves it into the list 
        '''
        pass

    def get_word_list(self):
        '''
        returns the whole word list 
        '''
        pass
    def check_is_word_in_word_list_(self, word_from_user):
        '''
        checks if the word from the user (string) is in one of the
        texts of the object words in the list. 
        SHOULD RETURN TRUE IF YES 
        SHOULD RETURN FALSE IF NO
        '''
        pass