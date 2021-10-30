import sys
from asciimatics.event import KeyboardEvent
from game.point import Point

class InputService:
    """Detects player input. The responsibility of the class of objects is to detect player keypresses and translate them into a point representing a direction (or velocity).

    Stereotype: 
        Service Provider

    Attributes:
        _screen (Screen): An Asciimatics screen.
    """

    def __init__(self, screen):
        """The class constructor.
        
        Args:
            self (InputService): An instance of InputService.
        """
        self._screen = screen
        self._direction = Point(0, 1) # LEFT
    '''
      
    def get_letter(self):
        """Gets the letter that was typed. If the enter key was pressed returns an asterisk.

        Args:
            self (InputService): An instance of InputService.

        Returns:
            string: The letter that was typed.
        """
        result = ""
        event = self._screen.get_key()
        if not event is None:
            if event == 27: #ESC KEY
                sys.exit()
            elif event == 10: #Enter Key
                result = "*"
            elif event >= 97 and event <= 122: 
                result = chr(event)
        return result
        '''

    def get_letter(self):
        """Gets the letter that was typed. If the enter key was pressed returns an asterisk.

        Args:
            self (InputService): An instance of InputService.

        Returns:
            string: The letter that was typed.
        """
        result = ""
        event = self._screen.get_event()
        if isinstance(event, KeyboardEvent):
            if event.key_code == 27: #ESC KEY
                sys.exit()
            elif event.key_code == 10: #Enter Key
                result = "*"
            elif event.key_code >= 97 and event.key_code <= 122: 
                result = chr(event)
        return result




       # result = ""
       # event = self._screen.get_event()
       # if isinstance(event, KeyboardEvent):
       #     if event.key_code == 27: #ESC KEY
       #         sys.exit()
       #     elif event.key_code == 10: #Enter Key
       #         result = "*"
       #     elif event.key_code>= 97 and event.key_code <= 122: 
       #         result = chr(event.key_code)
       # return result

    def get_direction(self):

        return self._direction

    def get_attempt(self, prompt):

        attempt = input(prompt)

        return attempt

