f = open("s3.txt")
line = f.readline()
f.close()
f = open("s3.txt")
lines = f.readlines()
print(line)
print(lines)
print(lines[0])
f.close()
