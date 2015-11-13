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
OCTAVE_INTERVAL = 7
POS_TO_PITCH = {
    1: 0, 2: 2, 3: 4, 4: 5, 5: 7, 6: 9, 7: 11
}
PITCH_TO_POS = {
    0: 1, 2: 2, 4: 3, 5: 4, 7: 5, 9: 6, 11: 7
}
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
        self.in_key_chords_pattern = {
            0: ["M3", "sus2", "M7", "6", "M9", "sus4", "5"],
            2: ["m3", "m7", "m6", "m9", "7"],
            4: ["m3", "m7", "m6"],
            5: ["M3", "sus2", "M7", "6", "M9", "sus4", "5"],
            7: ["M3", "sus2", "7", "7#5", "7sus4", "7sus2"],
            9: ["m3", "m7", "m6", "7"],
            11: ["dim", "dim7", "dim9"]
        }

        self.set_seed()

    def set_seed(self, seed=None):
        if seed is None:
            random.seed = self.seed
        else:
            random.seed = int(seed)

    def gen_single_random_base_note(self, start=None, end=None):
        if start is not None and end is not None:
            return random.randint(start, end)
        return random.randint(self.start, self.end)

    def gen_in_key_random_offset(self):
        off_set = int(random.random() * 10000) % len(self.in_key_octave)
        # print off_set
        note_offset = self.in_key_octave[off_set]
        return note_offset

    def gen_in_key_random_note(self, key=None, start=None, end=None):
        if key is not None:
            self.key = key
        if start is not None and end is not None:
            self.start, self.end = start, end
        note_offset = self.gen_in_key_random_offset()
        # print off_set
        pitch = random.randint(self.start, self.end)
        octave = pitch / 12
        pitch = octave * 12 + note_offset
        return pitch

    def gen_in_key_random_chords(self, key=None, start=None, end=None):
        base_note = self.gen_in_key_random_note(key=key, start=start, end=end)
        abs_pitch = base_note % 12
        pattern = self.in_key_chords_pattern[abs_pitch][random.randint(0, len(self.in_key_chords_pattern[abs_pitch])-1)]
        return {
                    "base_note": base_note,
                    "pattern": pattern
                }


if __name__ == "__main__":
    f = FibonacciNumber()
    for i in range(10):
        print f.next()