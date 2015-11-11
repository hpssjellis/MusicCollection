class Composer(object):
    def __init__(self):
        pass

    def Major3(self, base_note, base_d, mid_d, high_d):
        m3 = ((base_note, base_d), (base_note + 4, mid_d), (base_note + 7, high_d))
        return m3

"""
Guide line:
The Midi library is a interface to create Midi file, all composing and editing
should be performed in other form (representation).
Midi wrapper should be converter
Composer contains algorithms
"""
