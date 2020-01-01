# read word into list
f = open('hasla', 'r')
lines = f.readlines()
words = []
for line in lines:
    words.append(line.strip('\n'))
print(words)
f.close()
# create and display gui
