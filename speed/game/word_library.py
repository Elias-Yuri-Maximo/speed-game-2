from game import constants
from game.actor import Actor
from game.point import Point
from game.word import Word
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



    def check_is_word_in_word_list(self, word_from_user):
        '''
        checks if the word from the user (string) is in one of the
        texts of the object words in the list. 
        SHOULD RETURN TRUE IF YES 
        SHOULD RETURN FALSE IF NO
        '''
        #for word in self.get_word_list():
        #    if word_from_user == word.get_text():
        #       return True
        word_list = self.get_word_list()

        for i in range(len(word_list)):
            if word_from_user == word_list[i].get_text():
                
                self._word_objects_list.pop(i)
                return True
    
    def move_words(self):
        '''moves each word to the next spot'''
        word_list = self.get_word_list()
        
        for i in range(len(word_list)):
            word_list[i].move_next()
            
            