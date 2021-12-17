with open("cyber-rotkaeppchen.md") as f:
    text = f.read()

binary = ""
for zeichen in ",.!\n\r\"":
    text = text.replace(zeichen, " ")
for word in text.split(" "):
    if "cyber" in word.lower():
        if "cyber-" in word.lower():
            binary += "1"
        else:
            binary += "0"

print("Binary:\n"+binary)

print("\nEntschlüsseltes PW:")
print(''.join(chr(int(binary[i * 8:i * 8 + 8], 2)) for i in range(len(binary) // 8)))
