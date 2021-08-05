import notes_graphical
import notes_input
import notes_core

from notes_core import Note
from notes_core import noteToPos

import time

clef = "fa"
limits = {
    "min" : Note("do", 3),
    "max" : Note("do", 6),
}
def main():
    notes_graphical.startWindow("visual memory notes")
    
    if clef == "sol":
        notes_graphical.drawSolClef()
    if clef == "fa":
        notes_graphical.drawFaClef()
    
    while True:
        time.sleep(0.2)
        note = notes_input.inputToNote(notes_graphical.win.checkKey())
        pos = None
        if note is not None:
            pos = noteToPos(note, clef)
            if pos < noteToPos(limits["min"], clef) or noteToPos(limits["max"], clef) < pos:
                pos = None
        notes_graphical.showNote(pos)
    win.close()


if __name__ == "__main__":
    main()
