#importing graphics.py causes windows to unselect the terminal
#idk what to do about it
import notes_graphical
import notes_input

from notes_core import clefs
from notes_core import Note
from notes_core import noteToPos
from notes_core import posToNote

import time
import random
import traceback


def main():
    not_answered = 0
    correct = 0
    incorrect = 0
    # Sets parameters
    clef = notes_input.askQuestion("Select a clef", list(clefs.keys()))

    limit_min = notes_input.askQuestion("Select a lower note",
                                                [Note("do", 4), Note("do", 3), Note("do", 2)]
                                            )
    limit_max = notes_input.askQuestion("Select a higher note",
                                                [Note("do", 5), Note("do", 6), Note("do", 7)]
                                            )
        
    reaction_time = notes_input.askQuestion("Select a reaction time", [0.7, 1, 1.5])
    input_mode = notes_input.askQuestion("Select an input mode", notes_input.modes)


    # Importing graphical causes to unselect the terminal
    # this bodge avoids the need of clicking before answering the questions
    # i hate it but I can't do it better

    if noteToPos(limit_min, clef) < notes_graphical.lower_pos:
        limit_min = posToNote(notes_graphical.lower_pos, clef)

    if notes_graphical.higher_pos < noteToPos(limit_max, clef):
        limit_max = posToNote(notes_graphical.higher_pos, clef)

    limits = {
        "min" : limit_min,
        "max" : limit_max
    }

            
    # Creates the window
    notes_graphical.startWindow("visual memory notes")
        
    if clef == "sol":
        notes_graphical.drawSolClef()
    if clef == "fa":
        notes_graphical.drawFaClef()

        
    notes_graphical.drawText("CLICK HERE")
    notes_graphical.win.getMouse()
    notes_graphical.deleteText()

    # must be recalculated if clef is changed
    min_pos = noteToPos(limits["min"], clef)
    max_pos = noteToPos(limits["max"], clef) + 1

    #Starts the game
    try:
        while True:
            correct_pos = random.randrange(min_pos, max_pos)
            correct_note = posToNote(correct_pos, clef)
            notes_graphical.showNote(correct_pos)
            
            time.sleep(reaction_time)

            read_note = notes_input.non_block_input(input_mode)
            if read_note is None:
                notes_graphical.drawText("NOT ANSWERED, ANSWER: "+str(correct_note), "orange")
                not_answered += 1
            elif correct_note == read_note:
                notes_graphical.drawText("CORRECT", "green")
                correct += 1
            else:
                notes_graphical.drawText("INCORRECT, ANSWER: "+str(correct_note), "red")
                incorrect += 1

            time.sleep(2*reaction_time)
            # cleans output text
            notes_graphical.deleteText()
            # cleans input buffer
            if input_mode == notes_input.modes[0]:
                notes_graphical.win.checkKey()
            
    except:
        print("CORRECT      : "+str(correct))
        print("INCORRECT    : "+str(incorrect))
        print("NOT ANSWERED : "+str(not_answered))
        print("TOTAL        : "+str(correct+incorrect+not_answered))
        #to debug: traceback.print_exc()
        notes_input.midi_in_port.close()
        

if __name__ == "__main__":
    main()
