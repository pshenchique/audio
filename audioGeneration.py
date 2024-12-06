import random
from mingus.midi import fluidsynth
from mingus.containers import Track, Bar, Note, Composition
from mingus.core import *
import numpy as np

def playSound(indexI, indexW, indexC):

    inst = int(np.interp(indexW, [0,100], [0,20]))
    inst2 = int(np.interp(indexC, [0,100], [0,20]))

    fluidsynth.init("SMW.sf2")
    fluidsynth.set_instrument(0, inst2)
    fluidsynth.set_instrument(1, inst)

    key = scales.Diatonic('C', (3,7)).ascending()[random.randint(0,7)]
    print("key: "+key)

    if int(round(indexW+indexC))>100:
        progression = [chords.major_triad(key)]
    else:
        progression = [chords.minor_triad(key)]
        key = intervals.major_sixth(key)



    for i in range(0, 3):
        current_scale = scales.Major(key).ascending()
        mutation = int(round(np.interp(indexI, [100,300], [4,0]))+random.randint(0,5))

        # if mutation > 4:
        #     mutation - 

        match mutation:
            case 0:
                current_chord = chords.seventh(current_scale[random.randint(0, 7)], key)
            case 1:
                current_chord = chords.augmented_major_seventh(current_scale[random.randint(0, 7)])
            case 2:
                current_chord = chords.major_ninth(current_scale[random.randint(0, 7)])
            case 3:
                current_chord = chords.major_triad(current_scale[random.randint(0, 7)])
            case 4:
                current_chord = chords.minor_triad(current_scale[random.randint(0, 7)])
            case _:
                current_chord = chords.triad(current_scale[random.randint(0, 7)], key)

        print("current_chord: "+ str(chords.determine(current_chord, True, True)))
        progression.append(current_chord)

        

    pianoTrack = Track()
    bassTrack = Track()


    for i in range (0, 4):
        bar = Bar()
        bar.place_notes(progression[i][0], 4)
        bar.place_notes(progression[i][1], 4)
        bar.place_notes(progression[i][-1], 4)
        bar.place_notes(progression[i][-2], 4)
        pianoTrack + bar

    for i in range (0, 4):
        bar = Bar()
        t = int(np.interp(indexW, [0,100], [6,2]))
        t2 = int(np.interp(indexW, [0,100], [1,6]))
        bar.place_notes(Note(progression[i][0], t), t2)
        bassTrack + bar

    col = Composition()
    col.add_track(pianoTrack)
    col.add_track(bassTrack)

    t = int(np.interp(indexI, [100,300], [60,140]))

    fluidsynth.play_Composition(col, [inst2, inst], t)

