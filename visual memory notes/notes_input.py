import notes_core
import notes_graphical

import mido

keyboard_dict = {}
octaves_lists = [
    ["1", "2", "3", "4", "5", "6", "7", "8"],
    ["q", "w", "e", "r", "t", "y", "u", "i"],
    ["a", "s", "d", "f", "g", "h", "j", "k"],
    ["z", "x", "c", "v", "b", "n", "m", "comma"]
]

first_note = notes_core.Note("do", 2)
next_note = first_note

for octave in range(len(octaves_lists)):
    for key in octaves_lists[octave]:
        keyboard_dict[key] = next_note
        next_note = next_note + 1
    next_note = next_note - 1

def inputToNote(input):
    try:
        return keyboard_dict[input]
    except KeyError:
        return None

def askQuestion(question, answers):
    options = "( "
    for i in range(len(answers)):
        if i != 0:
            options += ", "
        options += str(i) + "->" + str(answers[i])
    options += " )"
        
    while True:
        print(question+" "+options)
        try:
            i = int(input())
            if i < 0:
                raise IndexError
            return answers[i]
        except (IndexError, ValueError):
            print("Invalid answer, try again")

midi_in_port = mido.open_input()

def midiToNote():
    final = None
    for msg in midi_in_port.iter_pending():
        if msg.type == 'note_on':
            final = msg
    
    if final is None:
        return None
    else:
        return notes_core.midiToNote(final.note)

modes = ["computer keyboard", "midi keyboard"]

def non_block_input(mode):
    if mode == modes[0]:
        return inputToNote(notes_graphical.win.checkKey())
    elif mode == modes[1]:
        return midiToNote()
    else:
        return None
