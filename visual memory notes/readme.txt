this program is a small python game that teaches you how to read music

everything is highly improvable, but it is functional, so it's also highly improbable that i make any changes

the program's main file is 'notes.py'. it depends on John Zelle's graphics.py and mido (and python-rtmidi because of port usage).

on startup you can set up various parameters (don't be afraid to mess with the code to add new options, should be easy to do).

the 'midi keyboard' input mode should work with any midi instrument you have as long as it is the default midi input. the 'computer keyboard' input mode maps rows of my qwerty spanish keyboard to 4 octaves. you can change the mapping modifying the 'notes_input.py' file.