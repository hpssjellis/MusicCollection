from midi_composer import FibonacciNumber, ChordsPatternGenerator
from chords_database import *
'''
'__doc__', '__init__', '__module__', 'addControllerEvent', 'addNote', 'addProgramChange', 'addSysEx', 'addTempo',
'addTrackName', 'addUniversalSysEx', 'changeNoteTuning', 'close', 'closed', 'findOrigin', 'header', 'numTracks',
'shiftTracks', 'tracks', 'writeFile'
'''

# Import midi library
from midiutil.MidiFile import MIDIFile
import time
from datetime import datetime
import random
time_stamp = datetime.now().__str__()
time_stamp = time_stamp.split(".", 1)[0]
time_stamp = time_stamp.replace(" ", "_").replace(":", "_")

# Create the MIDIFile Object
MyMIDI = MIDIFile(1)
MyMIDI2 = MIDIFile(2)
# Add track name and tempo. The first argument to addTrackName and
# addTempo is the time to write the event.
track = 0
base_track = 1
start_time = float(0)
MyMIDI.addTrackName(track, start_time, "Melody Track")
MyMIDI2.addTrackName(base_track, start_time, "Base note Track")
MyMIDI.addTempo(track, start_time, 120)
MyMIDI2.addTempo(track, start_time, 120)
f = FibonacciNumber()
# Create seed base note with same duration
channel = 0
base_note = 60
duration = float(2)
volume = 100
# get a composer
code_set = ChordsSet()
c_gen = ChordsPatternGenerator(seed=time.ctime())
set_length = code_set.length
LENGTH = 40
PLAYGROUND = "In_Key_Chorus"


if __name__ == "__main__" and PLAYGROUND == "In_Key_Chorus":
    for number_notes in range(LENGTH):
        chord = c_gen.gen_in_key_random_chords(start=65, end=66)
        print chord["base_note"], REVERSE_KEY_LOOK_UP[chord["base_note"] % 12]+chord["pattern"]
        chorus = code_set.get_chord(chord["base_note"], chord["pattern"])
        chorus = list(chorus)
        random.shuffle(chorus)
        for note in chorus:
            # print note
            MyMIDI.addNote(track, channel, note, start_time, duration, volume)
            start_time += float(duration / 4)
        MyMIDI2.addNote(base_track, channel, chord["base_note"], start_time, duration, volume)





# And write it to disk.
track1 = open("output/base.mid", 'w')
track2 = open("output/melody.mid", 'w')
MyMIDI.writeFile(track1)
MyMIDI2.writeFile(track2)
track1.close()
track2.close()