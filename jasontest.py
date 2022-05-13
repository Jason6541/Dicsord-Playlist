import re

with open('bops.txt','rt',errors='backslashreplace') as file:
        for line in file:
            urls = re.findall('(www.youtube.com/watch?\S+)', line)
            print(urls)

            with open("youtube.txt", "a") as fw:
                for item in urls:
                    fw.writelines("%s\n" % item)
                    print("%s\n" % item)

lines_seen = set() # holds lines already seen
outfile = open("youtube2.txt", "w")
for line in open("youtube.txt", "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()