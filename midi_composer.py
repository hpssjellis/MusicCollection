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

class FibonacciNumber(object):
    def __init__(self, start_1=0, start_2=1):
        self.f1 = start_1
        self.f2 = start_2

    def next(self):
        f3 = self.f1 + self.f2
        self.f1, self.f2 = self.f2, f3
        return f3


if __name__ == "__main__":
    f = FibonacciNumber()
    for i in range(10):
        print f.next()