alphabet_dict = {
  "a": "@",
  "b": "8",
  "c": "(",
  "d": "|)",
  "e": "3",
  "f": "#",
  "g": "6",
  "h": "[-]",
  "i": "|",
  "j": "_|",
  "k": "|<",
  "l": "1",
  "m": "[]\/[]",
  "n": "[]\[]",
  "o": "0",
  "p": "|D",
  "q": "(,)",
  "r": "|Z",
  "s": "$",
  "t": "']['",
  "u": "|_|",
  "v": "\/",
  "w": "\/\/",
  "x": "}{",
  "y": "`/",
  "z": "2"
}

translated = ""
for i in input().lower():
    if i in alphabet_dict.keys():
        translated+=alphabet_dict[i]
    else:
        translated+=i
print(translated)
