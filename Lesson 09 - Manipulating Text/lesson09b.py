phrase = "I'm learning Python!"
print(f"Phrase: {phrase}\n")

# | I | ' | m |   | l | e | a | r | n |  i |  n |  g |    |  P |  y |  t |  h |  o |  n |
# | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 |

print(f"- len(phrase): {len(phrase)}")
print(f"- phrase.count(\"o\"): {phrase.count("o")}")
print(f"- phrase[4:12]: {phrase[4:12]}")
print(f"- phrase.count(\"o\", 4, 12): {phrase.count("o", 4, 12)}")
print(f"- phrase.find(\"ing\"): {phrase.find("o")}")
print(f"- phrase.find(\"x\"): {phrase.find("x")}")
print(f"- \"Hi\" in phrase: {"Hi" in phrase}")

replaced_phrase = phrase.replace("Python", "a new programming language")
print(f"- phrase.replace(\"Python\", \"a new programming language\"): {replaced_phrase}")

replaced_phrase_2 = phrase.replace("x", "a new programming language")
print(f"- phrase.replace(\"x\", \"a new programming laguage\"): {replaced_phrase_2}")

print(f"- phrase.upper(): {phrase.upper()}")
print(f"- phrase.lower(): {phrase.lower()}")
print(f"- phrase.capitalize(): {phrase.capitalize()}")

phrase2 = " <- Space character"
print(f"\nPhrase 2: {phrase2}\n")

# |   | < | - |   | s | p | a | c | e |    |  c |  h |  a |  r |  a |  c |  t |  e |  r |
# | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 |

print(f"- phrase2.capitalized(): {phrase2.capitalize()}")
print(f"- phrase2.title(): {phrase2.title()}")