def test():
    infile = open('test001.txt', 'r', encoding='utf­8')
    outfile = open('test002.txt', 'w', encoding='utf­8')
    for line in infile:
        lines = ":".join(line)
 #       s = line.split(".")
        outfile.write(lines)
#        outfile.write(s)
    infile.close()
    outfile.close()


test()
