style = {"none": "\033[0m", "bold": "\033[1m",
         "underline": "\033[4m", "negative": "\033[7m"}

text_color = {"white": "\033[30m", "red": "\033[31m",
              "green": "\033[32m", "yellow": "\033[33m",
              "blue": "\033[34m", "pink": "\033[35m",
              "cyan": "\033[36m", "grey": "\033[37m"}

background_color = {"white": "\033[40m", "red": "\033[41m",
                    "green": "\033[42m", "yellow": "\033[43m",
                    "blue": "\033[44m", "pink": "\033[45m",
                    "cyan": "\033[46m", "grey": "\033[47m"}

reset = "\033[m"

name = input("What's your name? ")
print(f"Nice to meet you {style['bold'] +
      text_color['green'] + name + reset}!")
