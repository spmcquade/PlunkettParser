company_dir = []

data = open('F500DATA.txt', 'r')
out = open('F500PARSED.txt', 'w')

ticker = ""
for line in data.readlines():
    if 6 > len(line.replace(" ", "").strip()) > 0:
        line = line.replace(" ", "").strip()
        ticker = line
    elif line.endswith("Director\n"):
        line = " ".join(line.split())
        words = line.split()
        line = ticker + "," + words[0] + " " + words[1]
        out.write(line)
        out.write('\n')

