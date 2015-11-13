__author__ = 'y.zhou'


class Chords(object):
    def __init__(self):
        self.base_note = 60
        self.chords_set = {
            "Major3": (self.base_note,  self.base_note + 4, self.base_note + 7),
            "minor3": (self.base_note,  self.base_note + 3, self.base_note + 7),
            "dim": (self.base_note,  self.base_note + 3,  self.base_note + 6),
            "aug": (self.base_note,  self.base_note + 4,  self.base_note + 8),
            "sus2": (self.base_note,  self.base_note + 4, self.base_note + 7, self.base_note + 14),
            "7": (self.base_note,  self.base_note + 4,  self.base_note + 7, self.base_note + 10),
            "M7": (self.base_note,  self.base_note + 4,  self.base_note + 7, self.base_note + 11),
            "m7": (self.base_note,  self.base_note + 3,  self.base_note + 7, self.base_note + 10),
            "dim7": (self.base_note,  self.base_note + 3,  self.base_note + 6, self.base_note + 9),
            "mM7": (self.base_note,  self.base_note + 3,  self.base_note + 7, self.base_note + 11),
            "m#7": (self.base_note,  self.base_note + 3,  self.base_note + 7, self.base_note + 11),
            "7#5": (self.base_note,  self.base_note + 4,  self.base_note + 8, self.base_note + 10),
            "7+5": (self.base_note,  self.base_note + 4,  self.base_note + 8, self.base_note + 10),
            "7sus2": (self.base_note,  self.base_note + 3, self.base_note + 7, self.base_note + 10),
            "7sus4": (self.base_note,  self.base_note + 5, self.base_note + 7, self.base_note + 10),
            "6": (self.base_note,  self.base_note + 4, self.base_note + 7, self.base_note + 9),
            "m6": (self.base_note,  self.base_note + 3, self.base_note + 7, self.base_note + 9),
            "M9": (self.base_note,  self.base_note + 4, self.base_note + 11, self.base_note + 14),
            "9":  (self.base_note,  self.base_note + 4, self.base_note + 7,  self.base_note + 10, self.base_note + 14),
            "dim9": (self.base_note,  self.base_note + 4, self.base_note + 10, self.base_note + 13),
            "m9": (self.base_note,  self.base_note + 3, self.base_note + 7, self.base_note + 10, self.base_note + 14),
            "m-9": (self.base_note,  self.base_note + 3, self.base_note + 7, self.base_note + 10, self.base_note + 13),
            "sus4": (self.base_note,  self.base_note + 5, self.base_note + 7),
            "add9": (self.base_note,  self.base_note + 4, self.base_note + 7, self.base_note + 14),
            "5": (self.base_note,  self.base_note + 7, self.base_note + 12)
        }

    def Major3(self, base_note):
        self.base_note = base_note
        return self.chords_set["Major3"]

    def minor3(self, base_note):
        self.base_note = base_note
        return self.chords_set["minor3"]

    def dim(self, base_note):
        self.base_note = base_note
        return self.chords_set["dim"]

    def aug(self, base_note):
        self.base_note = base_note
        return self.chords_set["aug"]

    def sus2(self, base_note):
        self.base_note = base_note
        return self.chords_set["sus2"]

    def Dominant7(self, base_note):
        self.base_note = base_note
        return self.chords_set["7"]

    def Major7(self, base_note):
        self.base_note = base_note
        return self.chords_set["M7"]

    def minor7(self, base_note):
        self.base_note = base_note
        return self.chords_set["m7"]

    def dim7(self, base_note):
        self.base_note = base_note
        return self.chords_set["dim7"]

    def mM7(self, base_note):
        self.base_note = base_note
        return self.chords_set["m#7"]

    def Dominant7Aug5(self, base_note):
        self.base_note = base_note
        return self.chords_set["7#5"]

    def Dominant7Sus2(self, base_note):
        self.base_note = base_note
        return self.chords_set["7sus2"]

    def Dominant7Sus4(self, base_note):
        self.base_note = base_note
        return self.chords_set["7sus4"]

    def Major6(self, base_note):
        self.base_note = base_note
        return self.chords_set["6"]

    def minor6(self, base_note):
        self.base_note = base_note
        return self.chords_set["m6"]

    def Dominant9(self, base_note):
        self.base_note = base_note
        return self.chords_set["9"]

    def dim9(self, base_note):
        self.base_note = base_note
        return self.chords_set["dim9"]

    def minor9(self, base_note):
        self.base_note = base_note
        return self.chords_set["m9"]

    def minor3dim9(self, base_note):
        self.base_note = base_note
        return self.chords_set["m-9"]

    def Major9(self, base_note):
        self.base_note = base_note
        return self.chords_set["M9"]

    def sus4(self, base_note):
        self.base_note = base_note
        return self.chords_set["sus4"]

    def add9(self, base_note):
        self.base_note = base_note
        return self.chords_set["add9"]

    def power5(self, base_note):
        self.base_note = base_note
        return self.chords_set["power5"]