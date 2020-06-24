from music21 import converter, instrument, note, chord, graph
import os

music_dir = "../ff_midi/"

notes = []
note_durations = []
chords = []
for filename in os.listdir(music_dir):
    if filename.endswith(".mid"):
        print(filename)
        filepath = music_dir + filename
        midi = converter.parse(filepath)
        notes_to_parse = None

        # midi.plot('histogram', 'pitch')
        plt = graph.plot.HorizontalBar(midi)
        plt.figureSize = (20, 3)
        plt.run()

        parts = instrument.partitionByInstrument(midi)

        if parts:
            notes_to_parse = parts.parts[0].recurse()
        else:
            notes_to_parse = midi.flat.notes

        for element in notes_to_parse:
            if isinstance(element, note.Note):
                notes.append(element.pitch)
                # note_durations.append(element.duration)
            elif isinstance(element, chord.Chord):
                chords.append('.'.join(str(n) for n in element.normalOrder))

        notes.plot('histogram', 'pitch')
pass
