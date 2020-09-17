

f = open('wordlist.txt', "r", encoding='utf-8')
lines = f.readlines()
f.close()


len4 = []
len5 = []
len6 = []
len7 = []
len8 = []
len9 = []
len10 = []
len11 = []
len12 = []


##f = open('wordlistgen.txt', "w", encoding='utf-8')
##f.close()

for line in lines:
    linelen = len(line)
    line = line[0:linelen - 1]
    #line.strip('\n')
    #line.replace('\n','')
    line.replace(' ', '')

    if len(line) == 4:
        len4.append(line)

    elif len(line) == 5:
        len5.append(line)

    elif len(line) == 6:
        len6.append(line)

    elif len(line) == 7:
        len7.append(line)

    elif len(line) == 8:
        len8.append(line)

    elif len(line) == 9:
        len9.append(line)

    elif len(line) == 10:
        len10.append(line)

    elif len(line) == 11:
        len11.append(line)

    elif len(line) == 12:
        len12.append(line)



#print(len4)

f = open('4letterwords.txt', "w", encoding='utf-8')

for word in len4:
    word.replace('\n','')
    word.replace(' ','')
    f.write(',')
    f.write(word)

#f.write('\n')
f.close()


f = open('5letterwords.txt', "w", encoding='utf-8')
for word in len5:
    word.replace('\n','')
    word.replace(' ','')
    f.write(word + ',')

#f.write('\n')
f.close()


f = open('6letterwords.txt', "w", encoding='utf-8')
for word in len6:
    word.replace('\n','')
    word.replace(' ','')
    f.write(word + ',')

#f.write('\n')
f.close()

f = open('7letterwords.txt', "w", encoding='utf-8')
for word in len7:
    word.replace('\n','')
    word.replace(' ','')
    f.write(word + ',')

#f.write('\n')
f.close()

f = open('8letterwords.txt', "w", encoding='utf-8')
for word in len8:
    word.replace('\n','')
    word.replace(' ','')
    f.write(word + ',')

#f.write('\n')
f.close()

f = open('9letterwords.txt', "w", encoding='utf-8')
for word in len9:
    word.replace('\n','')
    word.replace(' ','')
    f.write(word + ',')

#f.write('\n')
f.close()

f = open('10letterwords.txt', "w", encoding='utf-8')
for word in len10:
    word.replace('\n','')
    word.replace(' ','')
    f.write(word + ',')

#f.write('\n')
f.close()

f = open('11letterwords.txt', "w", encoding='utf-8')
for word in len11:
    word.replace('\n','')
    word.replace(' ','')
    f.write(word + ',')

#f.write('\n')
f.close()

f = open('12letterwords.txt', "w", encoding='utf-8')
for word in len12:
    word.replace('\n','')
    word.replace(' ','')
    f.write(word + ',')

#f.write('\n')
f.close()




