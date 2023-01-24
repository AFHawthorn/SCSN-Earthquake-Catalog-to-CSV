import io, sys, unicodedata

year = int(sys.argv[1])
endYear = int(sys.argv[2])

while year <= endYear:
    file = str(year) + '.catalog'
    with io.open(file, 'r', encoding='latin-1') as f:
        text = f.read()
    fixed = unicodedata.normalize('NFKD', text).encode('ASCII')
    
    writefile = str(year) + '.csv'
    g = open(writefile, "a")
    
    # this is ugly, but it's a character count for the leading intro block of text at the top of the catalog files as of Jan 2023
    x = 787 
    
    while fixed[x] == '1' or fixed[x] == '2':
        g.write(fixed[x:x+4] + "," + fixed[x+5:x+7] + "," + fixed[x+8:x+10] + "," + fixed[x+11:x+22] + "," + fixed[x+23:x+25] + "," + fixed[x+27:x+28] + "," + fixed[x+29:x+33] + "," + fixed[x+34:x+35] + "," + fixed[x+39:x+45] + "," + fixed[x+46:x+54] + "," + fixed[x+56:x+60] + "," + fixed[x+61:x+62] + "," + fixed[x+63:x+71] + "," + fixed[x+74:x+76] + "," + fixed[x+78:x+81] + "\n")
        x += 82
    g.close()
    year += 1

print("Finished")