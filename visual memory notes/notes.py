import notes_graphical
import notes_input

from notes_core import Note
from notes_core import noteToPos
from notes_core import posToNote

import time
import random
import traceback

clef = "sol"
limits = {
    "min" : Note("do", 4),
    "max" : Note("do", 5),
}

reaction_time = 1

def main():
    notes_graphical.startWindow("visual memory notes")
    
    if clef == "sol":
        notes_graphical.drawSolClef()
    if clef == "fa":
        notes_graphical.drawFaClef()

    # must be recalculated if clef is changed
    min_pos = noteToPos(limits["min"], clef)
    max_pos = noteToPos(limits["max"], clef) + 1
    try:
        while True:
            correct_pos = random.randrange(min_pos, max_pos)
            correct_note = posToNote(correct_pos, clef)
            notes_graphical.showNote(correct_pos)
            
            time.sleep(reaction_time)

            read_note = notes_input.inputToNote(notes_graphical.win.checkKey())
            if read_note is None:
                notes_graphical.drawText("NOT ANSWERED", "yellow")
            elif correct_note == read_note:
                notes_graphical.drawText("CORRECT", "green")
            else:
                notes_graphical.drawText("INCORRECT, REAL NOTE: "+str(correct_note), "red")

            time.sleep(2*reaction_time)
            # cleans output text
            notes_graphical.deleteText()
            # cleans input buffer
            notes_graphical.win.checkKey()
            
    except:
        pass #to debug: traceback.print_exc()
    notes_graphical.win.close()

#Graphics error

if __name__ == "__main__":
    main()
