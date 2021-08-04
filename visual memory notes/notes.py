import graphics
import time

staff_x = 200
staff_y = 200

extra_y = 50 #space for higher/lower notes

border_size = 50

staff_start_x = border_size
staff_start_y = border_size + extra_y

note_0_start_x = staff_start_x + 130
note_0_start_y = staff_start_y + 150 - 2

note_x = 38
note_y = 26

def getAnchorPoint(start_x, start_y, size_x, size_y):
    return graphics.Point(start_x + size_x/2, start_y + size_y/2)

staff_anchor_point = getAnchorPoint(staff_start_x, staff_start_y, staff_x, staff_y)
note_0_anchor_point = getAnchorPoint(note_0_start_x, note_0_start_y, note_x, note_y)

def getNoteAnchorPoint(pos):
    return graphics.Point(note_0_anchor_point.x, note_0_anchor_point.y-12*pos)

def drawLine(win, line, clean = False, memory = []):
    if clean:
        for obj in memory:
            obj.undraw()
        memory.clear()
    else:
        line = graphics.Image(getNoteAnchorPoint(line), "pics/line.png")
        line.draw(win)
        memory.append(line)

def showNote(win, pos, memory = []):
    # pos 0 = under first line
    # pos 1 = in first line
    if pos < -9 or 19 < pos:
        return
    # cleans previous note
    for obj in memory:
        obj.undraw()
    memory.clear()
    drawLine(None, None, clean = True)
    
    note_anchor_point = getNoteAnchorPoint(pos)
    note = graphics.Image(note_anchor_point, "pics/note.png")
    note.draw(win)
    memory.append(note)
    
    if pos < 0:
        for line in range(-1, -9, -2):
            if line < pos:
                break
            else:
                drawLine(win, line)
    elif 10 < pos:
        for line in range(11, 19, 2):
            if pos < line:
                break
            else:
                drawLine(win, line)
    

def main():
    win = graphics.GraphWin("visual memory notes",
                                staff_x + 2*border_size,
                                staff_y + 2*extra_y + 2*border_size
                            )
    
    staff = graphics.Image(staff_anchor_point, "pics/staff.png")
    treble_clef = graphics.Image(staff_anchor_point, "pics/sol.png")
    bass_clef = graphics.Image(staff_anchor_point, "pics/fa.png")
    
    staff.draw(win)
    bass_clef.draw(win)
    pos = -9
    showNote(win, pos)
    while True:
        time.sleep(0.2)
        key = win.checkKey()
        if key == "n":
            pos = pos + 1
            showNote(win, pos)
        elif key == "b":
            pos = pos - 1
            showNote(win, pos)
    win.close()


if __name__ == "__main__":
    main()
