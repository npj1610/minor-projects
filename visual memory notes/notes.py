import graphics
import time

staff_x = 200
staff_y = 200

extra_y = 50 #space for higher/lower notes

border_size = 50

staff_start_x = border_size
staff_start_y = border_size + extra_y

def getAnchorPoint(start_x, start_y, size_x, size_y):
    return graphics.Point(start_x + size_x/2, start_y + size_y/2)

def main():
    win = graphics.GraphWin("visual memory notes",
                                staff_x + 2*border_size,
                                staff_y + 2*extra_y + 2*border_size
                            )
    anchorPoint = getAnchorPoint(staff_start_x, staff_start_y, staff_x, staff_y)
    staff = graphics.Image(anchorPoint, "pics/staff.png")
    treble_clef = graphics.Image(anchorPoint, "pics/sol.png")
    bass_clef = graphics.Image(anchorPoint, "pics/fa.png")
    
    staff.draw(win)
    bass_clef.draw(win)
    while True:
        time.sleep(0.5)
        print(win.checkKey())
    win.close()


if __name__ == "__main__":
    main()
