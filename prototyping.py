# Import midi library
from midiutil.MidiFile import MIDIFile
import os
import midi

cur_dir = os.path.dirname(__file__)
"""
'channel', 'copy', 'data', 'get_pitch', 'get_velocity', 'is_event', 'length', 'name', 'pitch',
'set_pitch', 'set_velocity', 'statusmsg', 'tick', 'velocity'
"""

class MIDIConverter(object):
    def __init__(self, file_path):
        self.pattern = midi.read_midifile(file_path)
        # store pitch and tick into tuple in vector
        self.data_vector = [(self.pattern[1][i].pitch, self.pattern[1][i].tick)
                             for i in range(len(self.pattern[1])-1)]
        self.backup_vector = self.data_vector
        self.is_notes_repr = False
        self.is_midi_repr = True

    def midi_info(self):
        print "number notes:", len(self.data_vector)
        print "highest", max([t[0] for t in self.data_vector])
        print "lowest", min([t[0] for t in self.data_vector])
        print "longest", max([t[1] for t in self.data_vector])
        print "shortest", min([t[1] for t in self.data_vector])

    def convert_to_notes_representation(self):
        if self.is_notes_repr:
            return
        elif self.is_midi_repr:
            self.backup_vector = self.data_vector
        self.data_vector = [(self.data_vector[t][0],self.data_vector[t+1][1]) for t in range(0, len(self.data_vector), 2)]



if __name__ == "__main__":
    test_file = os.path.join(cur_dir, "TrainingSet", "Bach", "cellosui", "04gigue.mid")
    test = MIDIConverter(test_file)
    test.midi_info()
    for i in range(len(test.data_vector)):
        print "{0}\t\t{1}\t\t".format(test.data_vector[i][0], test.data_vector[i][1]),
    print "\n",
    test.convert_to_notes_representation()
    for t in range(0, len(test.data_vector), 2):
        print "{0}\t{1}\t\t\t\t".format(test.data_vector[t][0], test.data_vector[t][1]),
    print
    print test.data_vector
    test.midi_info()

