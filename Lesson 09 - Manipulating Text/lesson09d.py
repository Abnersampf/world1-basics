phrase = "Hi, my name is Abner!"
print(f"Phrase: {phrase}\n")

print(f"- phrase.split(): {phrase.split()}")
print(f"- phrase.split(\",\"): {phrase.split(",")}")

splited_phrase = phrase.split()
print(f"- \"@\".join(phrase): {"@".join(phrase.split())}")
print(f"- len(phrase): {len(phrase)}")
print(f"- phrase[:52]: {phrase[:52]}|\n")

long_text = """Hi, my name is Abner Rodrigues Sambugari!
I'm 21 years old and i'm currently learning Python. It's
a easy programming language and it's very used in a lot
of softwares"""

print(long_text)