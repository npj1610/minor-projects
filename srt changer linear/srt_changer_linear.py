import re
import sys

timeFormat = r'(\d+):(\d+):(\d+),(\d+)'
timestampFormat = timeFormat+' --> '+timeFormat

originalFile = sys.argv[1]
targetFile = '.'.join(sys.argv[1].split('.')[0:-1])+"_new.srt"

#Choose 2 timespans to fit together
#(one quote start from the begining and one
# quote start from the end works fine)
subtitleTime0 = "00:01:11,238"	#.STR TIME FOR QUOTE 1
movieTime0 = "0:1:4,759"	#MOVIE TIME FOR QUOTE 1

subtitleTime1 = "01:26:02,892"	#.STR TIME FOR QUOTE 2
movieTime1 = "1:18:13,352"	#MOVIE TIME FOR QUOTE 2

def toMiliseconds(h, m, s, ms):
    #hours to minutes
    m = 60*h + m
    #minutes to seconds
    s = 60*m + s
    #seconds to ms
    ms = 1000*s + ms
    return ms;

def toHours(ms):
    #ms to seconds
    s = ms // 1000
    ms = ms % 1000
    #seconds to minutes
    m = s // 60
    s = s % 60
    #minutes to hours
    h = m // 60
    m = m % 60
    return [h, m, s, ms]

def readTime(time):
    tokens = re.match(timeFormat, time).groups()
    times = [int(tok) for tok in tokens]
    return toMiliseconds(times[0], times[1], times[2], times[3])

def changeTime(tiempos, offset, stretch):
    
    milisegundo = toMiliseconds(tiempos[0], tiempos[1], tiempos[2], tiempos[3])

    #changes the time
    milisegundo = offset + stretch * milisegundo

    return toHours(milisegundo)


def modify(tokentuple, offset, stretch):
    tokens = [int(tok) for tok in tokentuple]

    time1 = changeTime(tokens[0:4], offset, stretch)
    tokens1 = [
        '{0:0>2.0f}'.format(tok) for tok in time1
    ]
    timestamp1 = tokens1[0]+':'+tokens1[1]+':'+tokens1[2]+','+tokens1[3]

    time2 = changeTime(tokens[4:8], offset, stretch)
    tokens2 = [
        '{0:0>2.0f}'.format(tok) for tok in time2
    ]
    timestamp2 = tokens2[0]+':'+tokens2[1]+':'+tokens2[2]+','+tokens2[3]
    
    return timestamp1+' --> '+timestamp2+'\n'

x0 = readTime(subtitleTime0)
x1 = readTime(subtitleTime1)
y0 = readTime(movieTime0)
y1 = readTime(movieTime1)

#adjustes for a lineal transformation
stretch = (y1 - y0)/(x1 - x0)
offset = (x1*y0 - x0*y1)/(x1 - x0)

with open(originalFile, 'r') as original:
    with open(targetFile, 'w') as target:
        for line in original:
            try:
                #if the line is a timestamp, modify it
                tokens = re.match(timestampFormat, line).groups()
                target.write(modify(tokens, offset, stretch))
            except AttributeError:
                #if the line doesn't fit the regular expresion, dont touch it
                target.write(line)

#Im Stoned as Heck while translating do Not expect the utmost clarity
