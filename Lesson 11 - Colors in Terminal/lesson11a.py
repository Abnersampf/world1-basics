"""
\033[Style;Text Color;Background Colorm

Style:          Text Color:   Background color
0 (none)        30 (white)    40 (white)
1 (bold)        31 (red)      41 (red)
4 (underline)   32 (green)    42 (green)
7 (negative)    33 (yellow)   43 (yellow)
                34 (blue)     44 (blue)
                35 (pink)     45 (pink)
                36 (cyan)     46 (cyan)
                37 (grey)     47 (grey)
"""

reset = "\033[m"
color1 = "\033[0;30;41m"
color2 = "\033[4;33;44m"
color3 = "\033[1;35;43m"
color4 = "\033[40;42m"
color5 = "\033[7;30;47m"
color6 = "\033[7;37m"

text = "Test"

print(color1, text, reset)
print(color2, text, reset)
print(color3, text, reset)
print(color4, text, reset)
print(color5, text, reset)
print(color6, text, reset)
