import notes_core


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
