from string import ascii_lowercase

alphabet = {}
a = 1

for i in range(len(ascii_lowercase)):
    alphabet[ascii_lowercase[i]] = a
    a += 1

for key, value in alphabet.items():
    print(key, value)
