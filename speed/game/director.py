from _typeshed import Self
from time import sleep
from game import constants
from game.buffer import Buffer
from game.score import Score
from game.word import Word
from game.word_library import WordLibrary
from speed.game import output_service, word
#from game.point import Point


class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        food (Food): The snake's target.
        input_service (InputService): The input mechanism.
        keep_playing (boolean): Whether or not the game can continue.
        output_service (OutputService): The output mechanism.
        score (Score): The current score.
        snake (Snake): The player or snake.
    """

    def __init__(self, input_service, output_service):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._attempt = ''
        #This will be used to store the user attemptts
        self._buffer = Buffer()
        self._input_service = input_service
        self._keep_playing = True
        self._output_service = output_service
        self._word_library = WordLibrary()
        self._score = Score()
        
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            sleep(constants.FRAME_LENGTH)

    

   
        
        
    def populate_word_list(self):
        '''this function initializes 5 words(that should be randomly chosen from the word_class)
        and saves them into the word_library class 

        takes only self as an argument
        '''

        for _ in range(5):
            word = Word()
            self._word_library.insert_new_word(self, word)




    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the desired direction and moving the snake.

        Args:
            self (Director): An instance of Director.
        """
        
        object_word_list = self._word_library.get_word_list()
        self._output_service.draw_actors(object_word_list)
        ##gets the word list saved in word_library and passes it as 
        #an argument fot the output_service to print
        self._attempt = self.output_service.get_attempt('Write one of the words you see: ')
        

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means checking for a collision and updating the score.

        Args:
            self (Director): An instance of Director.
        """
        
        self._keep_playing = self._word_library.check_is_word_in_word_list_(self._attempt)
        #The word passed here will be a string.
        #This function will return a BOOLEAN VALUE that will be used by the score to add or to subtract.

        #I am not sure of what these do, but, I assumed they are important, so I put them here 
        self._output_service.clear_screen()     
        self._output_service.flush_buffer()

   
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring 
        the winner.

        Args:
            self (Director): An instance of Director.
        """
        self._output_service.clear_screen()
        self._output_service.draw_actor(self._buffer)        
        self._output_service.draw_actors(self._word_library.get_word_list())
        self._output_service.draw_actor(self._score)
        self._output_service.flush_buffer()

        if self._score > 5:
            self._keep_playing = False