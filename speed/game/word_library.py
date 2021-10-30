from game import constants
from game.actor import Actor
from game.point import Point
#from speed.game import word

class WordLibrary:
    '''
    This class is responsible for holding instances of word that will be called and drawn

    steryotype: information holder
    '''
    def __init__(self):
        self._word_objects_list = []
        #saves instances of the object word

    def insert_new_word(self, object_word): 
        '''
        gets a new object word and saves it into the list 
        '''
        self._word_objects_list.append(object_word)



    def get_word_list(self):
        '''
        returns the whole word list 
        '''
        return self._word_objects_list



    def check_is_word_in_word_list_(self, word_from_user):
        '''
        checks if the word from the user (string) is in one of the
        texts of the object words in the list. 
        SHOULD RETURN TRUE IF YES 
        SHOULD RETURN FALSE IF NO
        '''
        for word in self._word_objects_list:
            if word_from_user == word.get_text():
                return False
            else:
                return True
            