__author__ = 'y.zhou'
import exceptions

class ChordsSet(object):
    def __init__(self):
        self.base_note = 60
        self.shift = 0
        self.chords_set = {
            "M3": (self.shift,  self.shift + 4, self.shift + 7),
            "m3": (self.shift,  self.shift + 3, self.shift + 7),
            "dim": (self.shift,  self.shift + 3,  self.shift + 6),
            "aug": (self.shift,  self.shift + 4,  self.shift + 8),
            "sus2": (self.shift,  self.shift + 4, self.shift + 7, self.shift + 14),
            "7": (self.shift,  self.shift + 4,  self.shift + 7, self.shift + 10),
            "M7": (self.shift,  self.shift + 4,  self.shift + 7, self.shift + 11),
            "m7": (self.shift,  self.shift + 3,  self.shift + 7, self.shift + 10),
            "dim7": (self.shift,  self.shift + 3,  self.shift + 6, self.shift + 9),
            "mM7": (self.shift,  self.shift + 3,  self.shift + 7, self.shift + 11),
            "m#7": (self.shift,  self.shift + 3,  self.shift + 7, self.shift + 11),
            "7#5": (self.shift,  self.shift + 4,  self.shift + 8, self.shift + 10),
            "7+5": (self.shift,  self.shift + 4,  self.shift + 8, self.shift + 10),
            "7sus2": (self.shift,  self.shift + 3, self.shift + 7, self.shift + 10),
            "7sus4": (self.shift,  self.shift + 5, self.shift + 7, self.shift + 10),
            "m7-5": (self.shift,  self.shift + 3, self.shift + 6, self.shift + 10),
            "6": (self.shift,  self.shift + 4, self.shift + 7, self.shift + 9),
            "m6": (self.shift,  self.shift + 3, self.shift + 7, self.shift + 9),
            "M9": (self.shift,  self.shift + 4, self.shift + 11, self.shift + 14),
            "9":  (self.shift,  self.shift + 4, self.shift + 7,  self.shift + 10, self.shift + 14),
            "dim9": (self.shift,  self.shift + 4, self.shift + 10, self.shift + 13),
            "m9": (self.shift,  self.shift + 3, self.shift + 7, self.shift + 10, self.shift + 14),
            "m-9": (self.shift,  self.shift + 3, self.shift + 7, self.shift + 10, self.shift + 13),
            "sus4": (self.shift,  self.shift + 5, self.shift + 7),
            "add9": (self.shift,  self.shift + 4, self.shift + 7, self.shift + 14),
            "5": (self.shift,  self.shift + 7, self.shift + 12),
            "11": (self.shift,  self.shift + 4, self.shift + 7, self.shift + 10, self.shift + 14, self.shift + 17),
            "m11": (self.shift,  self.shift + 3, self.shift + 7, self.shift + 10, self.shift + 14, self.shift + 17)
        }
        self.length = len(self.chords_set)

    def get_chord(self, base_note, chord=None):
        self.base_note = base_note
        if chord is None:
            raise exceptions.AttributeError("need pass chord name or reference number")
        elif type(chord) is str:
            # print len(self.chords_set), self.length, chord, len(self.chords_set.values())
            chord_template = self.chords_set[chord]
            ret_chord = [None] * len(chord_template)
            for i in range(len(chord_template)):
                ret_chord[i] = chord_template[i] + base_note
            return tuple(ret_chord)
        elif type(chord) is int:
            # print len(self.chords_set), self.length, chord, len(self.chords_set.values())
            chord_template = self.chords_set.values()[chord]
            ret_chord = [None] * len(chord_template)
            for i in range(len(chord_template)):
                ret_chord[i] = chord_template[i] + base_note
            return tuple(ret_chord)

    def Major3(self, base_note):
        self.base_note = base_note
        return self.chords_set["M3"]

    def minor3(self, base_note):
        self.base_note = base_note
        return self.chords_set["m3"]

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


NOTE = {
    "C0": 0, "C1": 12, "C2": 24, "C3": 36, "C4": 48, "C5": 60, "C6": 72, "C7": 84, "C8": 96, "C9": 108, "C10": 120,
    "C#0": 1, "Db0": 1, "C#1": 13, "Db1": 13, "C#2": 25, "Db2": 25, "C#3": 37, "Db3": 37, "C#4": 49, "Db4": 49,
    "C#5": 61, "Db5": 61, "C#6": 73, "Db6": 73, "C#7": 85, "Db7": 85, "C#8": 97, "Db8": 97, "C#9": 109, "Db9": 109,
    "C#10": 121, "Db10": 121,
    "D0": 2, "D1": 14, "D2": 26, "D3": 38, "D4": 50, "D5": 62, "D6": 74, "D7": 86, "D8": 98, "D9": 110, "D10": 122,
    "D#0": 3, "Eb0": 3, "D#1": 15, "Eb1": 15, "D#2": 27, "Eb2": 27, "D#3": 39, "Eb3": 39, "D#4": 51, "Eb4": 51,
    "D#5": 63, "Eb5": 63, "D#6": 75, "Eb6": 75, "D#7": 87, "Eb7": 87, "D#8": 99, "Eb8": 99, "D#9": 111, "Eb9": 111,
    "D#10": 123, "Eb10": 123,
    "E0": 4, "E1": 16, "E2": 28, "E3": 40, "E4": 52, "E5": 64, "E6": 76, "E7": 88, "E8": 100, "E9": 112, "E10": 124,
    "F0": 5, "F1": 17, "F2": 29, "F3": 41, "F4": 53, "F5": 65, "F6": 77, "F7": 89, "F8": 101, "F9": 113, "F10": 125,
    "F#0": 6, "Gb0": 6, "F#1": 18, "Gb1": 18, "F#2": 30, "Gb2": 30, "F#3": 42, "Gb3": 42, "F#4": 54, "Gb4": 54,
    "F#5": 66, "Gb5": 66, "F#6": 78, "Gb6": 78, "F#7": 90, "Gb7": 90, "F#8": 102, "Gb8": 102, "F#9": 114, "Gb9": 114,
    "F#10": 126, "Gb10": 126,
    "G0": 7, "G1": 19, "G2": 31, "G3": 43, "G4": 55, "G5": 67, "G6": 79, "G7": 91, "G8": 103, "G9": 115, "G10": 127,
    "G#0": 8, "Ab0": 8, "G#1": 20, "Ab1": 20, "G#2": 32, "Ab2": 32, "G#3": 44, "Ab3": 44, "G#4": 56, "Ab4": 56,
    "G#5": 68, "Ab5": 68, "G#6": 80, "Ab6": 80, "G#7": 92, "Ab7": 92, "G#8": 104, "Ab8": 104, "G#9": 116, "Ab9": 116,
    "A0": 9, "A1": 21, "A2": 33, "A3": 45, "A4": 57, "A5": 69, "A6": 81, "A7": 93, "A8": 105, "A9": 117,
    "A#0": 10, "Bb0": 10, "A#1": 22, "Bb1": 22, "A#2": 34, "Bb2": 34, "A#3": 46, "Bb3": 46, "A#4": 58, "Bb4": 58,
    "A#5": 70, "Bb5": 70, "A#6": 82, "Bb6": 82, "A#7": 94, "Bb7": 94, "A#8": 106, "Bb8": 106, "A#9": 118, "Bb9": 118,
    "B0": 11, "B1": 23, "B2": 35, "B3": 47, "B4": 59, "B5": 71, "B6": 83, "B7": 95, "B8": 107, "B9": 119
}

KEY = {
    "C": 0, "C#": 1, "Db": 1, "D": 2, "D#": 3, "Eb": 3, "E": 4, "F": 5, "F#": 6, "Gb": 6, "G": 7, "G#": 8, "Ab": 8,
    "A": 9, "A#": 10, "Bb": 10, "B": 11
}

REVERSE_KEY_LOOK_UP = {}

for notation, pitch in KEY.iteritems():
    REVERSE_KEY_LOOK_UP[pitch] = notation

