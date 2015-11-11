from midi_composer import Composer, FibonacciNumber
'''
'__doc__', '__init__', '__module__', 'addControllerEvent', 'addNote', 'addProgramChange', 'addSysEx', 'addTempo',
'addTrackName', 'addUniversalSysEx', 'changeNoteTuning', 'close', 'closed', 'findOrigin', 'header', 'numTracks',
'shiftTracks', 'tracks', 'writeFile'
'''

#Import the library
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

PLAYGROUND = "Chords"
if __name__ == "__main__" and PLAYGROUND == "Chords":
    import random
    f = FibonacciNumber()
    # Create seed base note with same duration
    channel = 0
    base_note = 60
    duration = 2
    volume = 100
    # get a composer
    c = Composer()
    # create a major note
    # major_3 = c.Major3(base_note, float(random.randint(1, 16)) / 2,
    #                    float(random.randint(1, 16)) / 2,
    #                    float(random.randint(1, 16)) / 2)
    major_3 = c.Major3(base_note, duration, duration, duration)
    random.seed(time.time())
    # 12 bars test file
    for bar in range(96):
        base_note = f.next()
        if base_note > 128:
            base_note %= 127
        print base_note, track, channel
        # major_3 = c.Major3(base_note, float(random.randint(1, 16)) / 2,
        #                    float(random.randint(1, 16)) / 2,
        #                    float(random.randint(1, 16)) / 2)
        major_3 = c.Major3(base_note, duration, duration, duration)
        MyMIDI.addNote(track, channel, major_3[0][0], start_time, major_3[0][1], volume)
        MyMIDI.addNote(track, channel, major_3[1][0], start_time, major_3[1][1], volume)
        MyMIDI.addNote(track, channel, major_3[2][0], start_time, major_3[2][1], volume)
        start_time += 0.5


if __name__ == "__main__" and PLAYGROUND == "SingleNote":


    # Add a note. addNote expects the following information:
    channel = 0
    pitch = 60
    duration = 1
    volume = 100
    # Now add the note.
    for beat in range(48):
        if pitch > 84:
            pitch = 60
        MyMIDI.addNote(track, channel, pitch, start_time, duration, volume)
        pitch += 0
        start_time += 1

    # add chords
    base_note = 53
    mid_note = 57
    chords_duration = 4
    chords_time = 0
    for bar in range(12):
        if base_note > 84:
            base_note %= 60
        MyMIDI.addNote(track, channel, base_note, chords_time, duration, volume)
        MyMIDI.addNote(track, channel, mid_note, chords_time, duration, volume)
        base_note += 0
        mid_note += 0
        chords_time += 4



# And write it to disk.
binfile = open("output/output"+time_stamp+".mid", 'wb')
MyMIDI.writeFile(binfile)
binfile.close()