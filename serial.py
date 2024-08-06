"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        self.start = start
        self.current = 0

    def __repr__(self):
        return f'<SerialGenerator start={self.start} next={(self.current + 1)}>'

    def generate(self):
        '''creates next serial number in succession'''
        if self.current == None:
            self.current = self.start
            return self.current 
        else:
            self.current+=1 
            return self.current

    def reset(self):
        '''resets serial number back to start'''
        self.current = None




    
