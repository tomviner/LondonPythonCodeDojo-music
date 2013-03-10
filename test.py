#!/usr/bin/python

from midiutil.MidiFile import MIDIFile

# See http://www.tonalsoft.com/pub/news/pitch-bend.aspx
# To play on Linux: install timidity package and just execute:
# timidity file.mid


def addTrack(midi, track_number, track_name, tempo):
    midi.addTrackName(track_number, 0, track_name)

    # tempo in beats per minute
    midi.addTempo(track_number, 0, tempo)

def writeFile(midi, filename):
    binfile = open(filename, 'wb')
    midi.writeFile(binfile)
    binfile.close()

def addNotes(midi):
    """
        Arguments:
            track: The track to which the note is added.
            channel: the MIDI channel to assign to the note. [Integer, 0-15]
            pitch: the MIDI pitch number [Integer, 0-127].
            time: the time (in beats) at which the note sounds [Float].
            duration: the duration of the note (in beats) [Float].
            volume: the volume (velocity) of the note. [Integer, 0-127].
    """
    for x in xrange(1,100):
        midi.addNote(0, 0, 60+(x%10), x, 5, 100)

def main():
    myMidi = MIDIFile(2)

    addTrack(myMidi, 0, 'track-1', 120)
    addTrack(myMidi, 1, 'track-2', 120)

    addNotes(myMidi)

    writeFile(myMidi, 'output.mid')

if __name__ == '__main__':
    main()

