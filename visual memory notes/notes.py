import notes_graphical
import time

def main():
    notes_graphical.startWindow("visual memory notes")
    pos = -9
    notes_graphical.showNote(pos)
    while True:
        time.sleep(0.2)
        key = notes_graphical.win.checkKey()
        if key == "n":
            pos = pos + 1
            notes_graphical.showNote(pos)
        elif key == "b":
            pos = pos - 1
            notes_graphical.showNote(pos)
    win.close()


if __name__ == "__main__":
    main()
