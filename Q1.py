f = open('H:/words.txt')
fout = open('H:/Q1.txt','w')
string = f.read()
words = string.split(' ')
num = 0
while len(words):
    num += 1
    word = words[0]
    fre = words.count(word)
    words.remove(word)
    while words.count(word):
        words.remove(word)
    fout.write(word + ' ' + repr(num) + ' ' + repr(fre))
    if len(words):
        fout.write('\n')
f.close()
fout.close()
