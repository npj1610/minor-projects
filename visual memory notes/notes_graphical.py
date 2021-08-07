import graphics

win = None
treble_clef = None
bass_clef = None

staff_x = 200
staff_y = 200

extra_y = 50 #space for higher/lower notes

text_y = 50 #space for text

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

text_anchor_point = graphics.Point(staff_anchor_point.x, staff_y + 2*extra_y + 2*border_size + text_y/2)

def getNoteAnchorPoint(pos):
    return graphics.Point(note_0_anchor_point.x, note_0_anchor_point.y-12*pos)


def drawText(text=None, color=None, memory = []):
    for obj in memory:
        obj.undraw()
    memory.clear()

    if color is not None:
        text = graphics.Text(text_anchor_point, text)
        text.setTextColor(color)
        text.setStyle("bold")
        text.draw(win)
        memory.append(text)

def deleteText():
    drawText()

def drawLine(line, clean = False, memory = []):
    if clean:
        for obj in memory:
            obj.undraw()
        memory.clear()
    else:
        line = graphics.Image(getNoteAnchorPoint(line), "pics/line.png")
        line.draw(win)
        memory.append(line)

def showNote(pos, memory = []):
    # draw no note
    if pos is None:
        return
    # cleans previous note
    for obj in memory:
        obj.undraw()
    memory.clear()
    drawLine(None, clean = True)
    # pos 0 = under first line
    # pos 1 = in first line
    if pos < -10 or 20 < pos:
        return
    
    note_anchor_point = getNoteAnchorPoint(pos)
    note = graphics.Image(note_anchor_point, "pics/note.png")
    note.draw(win)
    memory.append(note)
    
    if pos < 0:
        for line in range(-1, -11, -2):
            if line < pos:
                break
            else:
                drawLine(line)
    elif 10 < pos:
        for line in range(11, 21, 2):
            if pos < line:
                break
            else:
                drawLine(line)

def drawSolClef():
    bass_clef.undraw()
    treble_clef.undraw()
    treble_clef.draw(win)

def drawFaClef():
    treble_clef.undraw()
    bass_clef.undraw()
    bass_clef.draw(win)

def startWindow(title):
    global win
    global treble_clef
    global bass_clef
    
    win = graphics.GraphWin(title,
                                staff_x + 2*border_size,
                                staff_y + 2*extra_y + 2*border_size + text_y
                            )    
    staff = graphics.Image(staff_anchor_point, "pics/staff.png")
    treble_clef = graphics.Image(staff_anchor_point, "pics/sol.png")
    bass_clef = graphics.Image(staff_anchor_point, "pics/fa.png")
    
    staff.draw(win)
