__author__ = 'y.zhou'


class Chords(object):
    def __init__(self):
        self.base_note = 60
        self.base_d, self.mid_d, self.high_d = 1
        self.chords_set = {
            "Major3": ((self.base_note, self.base_d), (self.base_note + 4, self.mid_d),
                       (self.base_note + 7, self.high_d)),
            "minor3": ((self.base_note, self.base_d), (self.base_note + 3, self.mid_d),
                       (self.base_note + 7, self.high_d)),
            "dim": ((self.base_note, self.base_d), (self.base_note + 3, self.mid_d), (self.base_note + 6, self.high_d)),
            "aug": ((self.base_note, self.base_d), (self.base_note + 4, self.mid_d), (self.base_note + 8, self.high_d)),
            "sus2": ((self.base_note, self.base_d), (self.base_note + 3, self.mid_d),
                     (self.base_note + 7, self.high_d)),
            "7": ((self.base_note, self.base_d), (self.base_note + 4, self.mid_d), (self.base_note + 7, self.high_d),
                  (self.base_note + 10, self.base_d)),
            "M7": ((self.base_note, self.base_d), (self.base_note + 4, self.mid_d), (self.base_note + 7, self.high_d),
                   (self.base_note + 11, self.base_d)),
            "m7": ((self.base_note, self.base_d), (self.base_note + 3, self.mid_d), (self.base_note + 7, self.high_d),
                   (self.base_note + 10, self.base_d)),
            "dim7": ((self.base_note, self.base_d), (self.base_note + 3, self.mid_d), (self.base_note + 6, self.high_d),
                     (self.base_note + 9, self.base_d)),
            "mM7": ((self.base_note, self.base_d), (self.base_note + 3, self.mid_d), (self.base_note + 7, self.high_d),
                    (self.base_note + 11, self.base_d)),
            "m#7": ((self.base_note, self.base_d), (self.base_note + 3, self.mid_d), (self.base_note + 7, self.high_d),
                    (self.base_note + 11, self.base_d)),
            "7#5": ((self.base_note, self.base_d), (self.base_note + 4, self.mid_d), (self.base_note + 8, self.high_d),
                    (self.base_note + 10, self.base_d)),
            "7+5": ((self.base_note, self.base_d), (self.base_note + 4, self.mid_d), (self.base_note + 8, self.high_d),
                    (self.base_note + 10, self.base_d)),
            "7sus2": ((self.base_note, self.base_d), (self.base_note + 3, self.mid_d),
                      (self.base_note + 7, self.high_d), (self.base_note + 10, self.base_d)),
            "7sus4": ((self.base_note, self.base_d), (self.base_note + 5, self.mid_d),
                      (self.base_note + 7, self.high_d), (self.base_note + 10, self.base_d)),
            "6": ((self.base_note, self.base_d), (self.base_note + 4, self.mid_d),
                  (self.base_note + 7, self.high_d), (self.base_note + 9, self.base_d)),
        }

    def Major3(self, base_note, base_d, mid_d, high_d):
        self.base_note, self.base_d, self.mid_d, self.high_d = base_note, base_d, mid_d, high_d
        return self.chords_set["Major3"]

    def minor3(self, base_note, base_d, mid_d, high_d):
        self.base_note, self.base_d, self.mid_d, self.high_d = base_note, base_d, mid_d, high_d
        return self.chords_set["minor3"]

    def dim(self, base_note, base_d, mid_d, high_d):
        self.base_note, self.base_d, self.mid_d, self.high_d = base_note, base_d, mid_d, high_d
        return self.chords_set["dim"]

    def aug(self, base_note, base_d, mid_d, high_d):
        self.base_note, self.base_d, self.mid_d, self.high_d = base_note, base_d, mid_d, high_d
        return self.chords_set["aug"]

    def sus2(self, base_note, base_d, mid_d, high_d):
        self.base_note, self.base_d, self.mid_d, self.high_d = base_note, base_d, mid_d, high_d
        return self.chords_set["sus2"]

    def Dominant7(self, base_note, base_d, mid_d, high_d):
        self.base_note, self.base_d, self.mid_d, self.high_d = base_note, base_d, mid_d, high_d
        return self.chords_set["7"]

    def Major7(self, base_note, base_d, mid_d, high_d):
        self.base_note, self.base_d, self.mid_d, self.high_d = base_note, base_d, mid_d, high_d
        return self.chords_set["M7"]

    def minor7(self, base_note, base_d, mid_d, high_d):
        self.base_note, self.base_d, self.mid_d, self.high_d = base_note, base_d, mid_d, high_d
        return self.chords_set["m7"]

    def dim7(self, base_note, base_d, mid_d, high_d):
        self.base_note, self.base_d, self.mid_d, self.high_d = base_note, base_d, mid_d, high_d
        return self.chords_set["dim7"]

    def mM7(self, base_note, base_d, mid_d, high_d):
        self.base_note, self.base_d, self.mid_d, self.high_d = base_note, base_d, mid_d, high_d
        return self.chords_set["m#7"]

    def Dominant7Aug5(self, base_note, base_d, mid_d, high_d):
        self.base_note, self.base_d, self.mid_d, self.high_d = base_note, base_d, mid_d, high_d
        return self.chords_set["7#5"]

    def Dominant7Sus2(self, base_note, base_d, mid_d, high_d):
        self.base_note, self.base_d, self.mid_d, self.high_d = base_note, base_d, mid_d, high_d
        return self.chords_set["7sus2"]

    def Dominant7Sus4(self, base_note, base_d, mid_d, high_d):
        self.base_note, self.base_d, self.mid_d, self.high_d = base_note, base_d, mid_d, high_d
        return self.chords_set["7sus4"]

    def Major6(self, base_note, base_d, mid_d, high_d):
        self.base_note, self.base_d, self.mid_d, self.high_d = base_note, base_d, mid_d, high_d
        return self.chords_set["6"]