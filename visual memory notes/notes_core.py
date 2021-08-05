

class Note:
    #it is highly encouraged to use note names instead of numbers
    #octaves are internally stored with the middle C starting octave 0
    #externally they are numbered as piano keys would (middle C = octave 4)
    notes = ["do", "re", "mi", "fa", "sol", "la", "si"]
    
    def __init__(self, note = 0, octave = 4):
        if note in Note.notes:
            self.note = Note.notes.index(note)
        else:
            self.note = note
        self.octave = octave - 4

    def __add__(self, other):
        if isinstance(other, int):
            positions = other
            return Note(
                        note = (self.note + positions) % 7,
                        octave = 4 + self.octave + (self.note + positions) // 7
                       )
        else:
            return NotImplemented  
    __radd__ = __add__

    def __sub__(self, other):
        if isinstance(other, int):
            return self + (-other)
        elif isinstance(other, self.__class__):
            return (self.note + 7*self.octave) - (other.note + 7*other.octave)
        else:
            return NotImplemented
    
    def __repr__(self):
        return Note.notes[self.note]+str(self.octave+4)

clefs = {"sol" : (3, Note("sol", 4)), "fa" : (7, Note("fa", 3)) }

def noteToPos(note, clef):
    base_pos = clefs[clef][0]
    base_note = clefs[clef][1]
    return base_pos + (note - base_note)

def posToNote(pos, clef):
    base_pos = clefs[clef][0]
    base_note = clefs[clef][1]
    return base_note + (pos - base_pos)
    

print(noteToPos(Note("do"), "sol"))
print(noteToPos(Note("do"), "fa"))
