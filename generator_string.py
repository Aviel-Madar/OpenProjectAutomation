import random
import string


class GeneratorString:

    length = 6

    def get_unique_string(self):
        new_string = ''.join(random.choice(string.ascii_lowercase) for i in range(self.length))
        return new_string
