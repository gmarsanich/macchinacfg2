file = "terminal_logo_alt.txt"

with open(file, "r") as fp:
    artfile = fp.read()

# smaller factor -> smaller output
# max factor == 7
factor = 9

art = artfile.splitlines()
for line in art[:: len(art) // factor]:
    print(line[:: len(art) // factor])
