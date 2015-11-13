from midi_composer import FibonacciNumber, ChordsPatternGenerator
from chords_database import ChordsSet, NOTE, KEY
'''
'__doc__', '__init__', '__module__', 'addControllerEvent', 'addNote', 'addProgramChange', 'addSysEx', 'addTempo',
'addTrackName', 'addUniversalSysEx', 'changeNoteTuning', 'close', 'closed', 'findOrigin', 'header', 'numTracks',
'shiftTracks', 'tracks', 'writeFile'
'''

# Import midi library
from midiutil.MidiFile import MIDIFile
import time
from datetime import datetime
time_stamp = datetime.now().__str__()
time_stamp = time_stamp.split(".", 1)[0]
time_stamp = time_stamp.replace(" ", "_").replace(":", "_")

# Create the MIDIFile Object
MyMIDI = MIDIFile(1)
# Add track name and tempo. The first argument to addTrackName and
# addTempo is the time to write the event.
track = 0
start_time = 0
MyMIDI.addTrackName(track, start_time, "Sample Track")
MyMIDI.addTempo(track, start_time, 120)
import random
f = FibonacciNumber()
# Create seed base note with same duration
channel = 0
base_note = 60
duration = 2
volume = 100
# get a composer
code_set = ChordsSet()
c_gen = ChordsPatternGenerator()
set_length = code_set.length
LENGTH = 40
PLAYGROUND = "Melody"
if __name__ == "__main__" and PLAYGROUND == "Chords_Random":
    for bar in range(LENGTH):
        base_note = c_gen.gen_single_random_base_note(40, 70)
        chord = code_set.get_chord(base_note, random.randint(0, set_length - 1))
        for note in chord:
            # print note
            MyMIDI.addNote(track, channel, note, start_time, duration, volume)
        start_time += duration

if __name__ == "__main__" and PLAYGROUND == "Chords_Inkey":
    for bar in range(LENGTH):
        base_note = c_gen.gen_in_key_random_note(KEY["C"], 40, 70)
        chord = code_set.get_chord(base_note, random.randint(0, set_length - 1))
        for note in chord:
            # print note
            MyMIDI.addNote(track, channel, note, start_time, duration, volume)
        start_time += duration

if __name__ == "__main__" and PLAYGROUND == "Melody":
    for bar in range(LENGTH):
        note = c_gen.gen_in_key_random_note(KEY["C"], 40, 70)
        MyMIDI.addNote(track, channel, note, start_time, duration, volume)
        start_time += 0.5

# And write it to disk.
binfile = open("output/output"+time_stamp+".mid", 'wb')
MyMIDI.writeFile(binfile)
binfile.close()