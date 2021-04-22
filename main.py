import re
import json

def display_rtf(rtffile):
    class Color:
      def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    strtoreturn = ''
    colorlist = []
    doc =  open(rtffile, "r")
    firstline = doc.readline()
    firstline = re.sub('\\s', '', firstline)
    styles = re.split("colortbl", firstline)
    colors = styles[1].split(";")
    for color in colors:
        try:
            start_red = color.index("red") + 3
            end_red = color.index("\\", start_red)
            start_green = color.index("green") + 5
            end_green = color.index("\\", start_green)
            start_blue = color.index("blue") + 4
            c = Color(color[start_red:end_red], color[start_green:end_green], color[start_blue:])
            colorlist.append(c)
        except Exception:
            pass
    for line in doc:
        line = line.lstrip()
        line = line.replace("\\par", '')
        if line[3:4] != '':
            strtoreturn += '<span style="color:rgb('+colorlist[int(line[3:4])-1].red + ',' + colorlist[int(line[3:4])-1].green + ',' + colorlist[int(line[3:4])-1].blue + ')">' + line[6:] + '</span>'

    doc.close()
    return json.dumps(strtoreturn)
