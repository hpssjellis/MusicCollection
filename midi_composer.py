############################################################################
# A sample program to create a single-track MIDI file, add a note,
# and write to disk.
############################################################################

#Import the library
from midiutil.MidiFile import MIDIFile
from datetime import datetime
time_stamp = datetime.now().__str__()
time_stamp = time_stamp.split(".", 1)[0]
time_stamp = time_stamp.replace(" ", "_").replace(":", "_")
# Create the MIDIFile Object
MyMIDI = MIDIFile(1)

# Add track name and tempo. The first argument to addTrackName and
# addTempo is the time to write the event.
track = 0
time = 0
MyMIDI.addTrackName(track,time,"Sample Track")
MyMIDI.addTempo(track,time, 120)

# Add a note. addNote expects the following information:
channel = 0
pitch = 60
duration = 1
volume = 100

# Now add the note.
MyMIDI.addNote(track,channel,pitch,time,duration,volume)

# And write it to disk.
binfile = open("output/output"+time_stamp+".mid", 'wb')
MyMIDI.writeFile(binfile)
binfile.close()

