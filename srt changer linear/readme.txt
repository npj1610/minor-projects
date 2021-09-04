this program uses 2 pairs of subtitle and movie timestamps making them match in the .srt file.

it calculates a fitting linear transformation and aplies it to every timestamp in the file.

to use it you need to change the timestamps in the srt_changer_linear.py. hash comments mark the strings you need to modify. then drop the .srt file into the "exec.bat" (or write "python srt_changer_linear name_of_my_file.srt" in the terminal after changing directory to this folder)