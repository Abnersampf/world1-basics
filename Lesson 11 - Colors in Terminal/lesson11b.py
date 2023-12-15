style_none = "\033[0m"
style_bold = "\033[1m"
style_underline = "\033[4m"
style_negative = "\033[7m"

text_white = "\033[30m"
text_red = "\033[31m"
text_green = "\033[32m"
text_yellow = "\033[33m"
text_blue = "\033[34m"
text_pink = "\033[35m"
text_cyan = "\033[36m"
text_grey = "\033[37m"

background_white = "\033[40m"
background_red = "\033[41m"
background_green = "\033[42m"
background_yellow = "\033[43m"
background_blue = "\033[44m"
background_pink = "\033[45m"
background_cyan = "\033[46m"
background_grey = "\033[47m"

reset = "\033[m"

name = input("What's your name? ")
print(f"Nice to meet you {style_underline + text_blue + name + reset}!")
