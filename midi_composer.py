import random
from chords_database import *
"""
Guide line:
The Midi library is a interface to create Midi file, all composing and editing
should be performed in other form (representation).
Midi wrapper should be converter
Composer contains algorithms
"""
DEFAULT_BOUND = (30, 80)
class FibonacciNumber(object):
    def __init__(self, start_1=0, start_2=1):
        self.f1 = start_1
        self.f2 = start_2

    def next(self):
        f3 = self.f1 + self.f2
        self.f1, self.f2 = self.f2, f3
        return f3


class ChordsPatternGenerator(object):
    def __init__(self, seed=0, key=KEY["C"], start=DEFAULT_BOUND[0], end=DEFAULT_BOUND[1]):
        self.start, self.end, self.key = start, end, key
        self.in_key_octave = (0, 2, 4, 5, 7, 9, 11, 12)
        self.seed = seed
        random.seed = seed

    def gen_single_random_base_note(self, start=None, end=None):
        if start is not None and end is not None:
            return random.randint(start, end)
        return random.randint(self.start, self.end)

    def gen_in_key_random_note(self, key=None, start=None, end=None):
        if key is not None:
            self.key = key
        if start is not None and end is not None:
            self.start, self.end = start, end
        off_set = int(random.random() * 10000) % len(self.in_key_octave)
        # print off_set
        note_offset = self.in_key_octave[off_set]
        # print off_set
        pitch = random.randint(self.start, self.end)
        octave = pitch / 12
        pitch = octave * 12 + note_offset
        return pitch



if __name__ == "__main__":
    f = FibonacciNumber()
    for i in range(10):
        print f.next()