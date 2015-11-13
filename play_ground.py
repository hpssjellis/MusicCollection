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
# Add track name and tempo. The first argument to addTrackName and
# addTempo is the time to write the event.
track = 0
start_time = float(0)
MyMIDI.addTrackName(track, start_time, "Sample Track")
MyMIDI.addTempo(track, start_time, 120)
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

if __name__ == "__main__" and PLAYGROUND == "Check_Chords":
    for number_notes in range(1):
        chord = c_gen.gen_in_key_random_chords(60, 72)
        print chord["base_note"], REVERSE_KEY_LOOK_UP[chord["base_note"] % 12]+chord["pattern"]
        chorus = code_set.get_chord(chord["base_note"], chord["pattern"])
        chorus = list(chorus)
        random.shuffle(chorus)
        for note in chorus:
            # print note
            MyMIDI.addNote(track, channel, note, start_time, duration, volume)
            start_time += duration / 2

if __name__ == "__main__" and PLAYGROUND == "In_Key_Chorus":
    for number_notes in range(LENGTH):
        chord = c_gen.gen_in_key_random_chords(start=65, end=70)
        print chord["base_note"], REVERSE_KEY_LOOK_UP[chord["base_note"] % 12]+chord["pattern"]
        chorus = code_set.get_chord(chord["base_note"], chord["pattern"])
        chorus = list(chorus)
        random.shuffle(chorus)
        for note in chorus:
            # print note
            MyMIDI.addNote(track, channel, note, start_time, duration, volume)
            start_time += float(duration / 4)

if __name__ == "__main__" and PLAYGROUND == "Chords_Random":
    for number_notes in range(LENGTH):
        base_note = c_gen.gen_single_random_base_note(40, 70)
        chord = code_set.get_chord(base_note, random.randint(0, set_length - 1))
        for note in chord:
            # print note
            MyMIDI.addNote(track, channel, note, start_time, duration, volume)
        start_time += duration / 2

if __name__ == "__main__" and PLAYGROUND == "Chords_Inkey":
    for number_notes in range(LENGTH):
        base_note = c_gen.gen_in_key_random_note(KEY["C"], 30, 50)
        chord = code_set.get_chord(base_note, random.randint(0, set_length - 1))
        for note in chord:
            # print note
            MyMIDI.addNote(track, channel, note, start_time, duration, volume)
        start_time += 1

if __name__ == "__main__" and PLAYGROUND == "Melody":
    for number_notes in range(LENGTH):
        note = c_gen.gen_in_key_random_note(KEY["C"], 40, 70)
        MyMIDI.addNote(track, channel, note, start_time, duration, volume)
        start_time += 0.5

# And write it to disk.
binfile = open("output/output"+time_stamp+".mid", 'wb')
MyMIDI.writeFile(binfile)
binfile.close()