phrase = input("Enter a phrase: ").strip().upper()
print(f"The letter A appears {phrase.count("A")}.")
print(f"The first letter A appeared in position {phrase.find("A") + 1}")
print(f"The last letter A appeared in position {phrase.rfind("A") + 1}")
# or
reversed_phrase = phrase[::-1]
print(f"The last letter A appeared in postition {reversed_phrase.find("A") + 1}")