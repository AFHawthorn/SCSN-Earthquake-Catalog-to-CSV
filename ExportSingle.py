import io, sys, unicodedata

file = 'SearchResults.txt'
writefile = 'SearchResults.csv'

with io.open(file, 'r', encoding='latin-1') as f:
    text = f.read()
fixed = unicodedata.normalize('NFKD', text).encode('ASCII')
g = open(writefile, "a")

# this is ugly, but it's a character count for the leading intro lines of text at the top of the search result file as of Jan 2023
x = 152

while fixed[x] == '1' or fixed[x] == '2':
    g.write(fixed[x:x+4] + "," + fixed[x+5:x+7] + "," + fixed[x+8:x+10] + "," + fixed[x+11:x+22] + "," + fixed[x+23:x+25] + "," + fixed[x+27:x+28] + "," + fixed[x+29:x+33] + "," + fixed[x+34:x+35] + "," + fixed[x+38:x+46] + "," + fixed[x+47:x+57] + "," + fixed[x+59:x+63] + "," + fixed[x+64:x+65] + "," + fixed[x+66:x+74] + "," + fixed[x+76:x+79] + "," + fixed[x+80:x+84] + "\n")
    x += 85

print("finished")
g.close()