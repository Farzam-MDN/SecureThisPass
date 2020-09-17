import os
import time
import webbrowser
import random



global smallletters
global capletters
global symbols

smallletters = 'abcdefghijklmnopqrstuvwxyz'
capletters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols = '`~!@#$%^&*()_+}{[]\:;/.,<>?'


#functions
def GetInput():
    unsercurepass = input('Input the pass you want to make more secure:')
    ProcessInput(unsercurepass)


def ProcessInput(passwordinput):

     if(passwordinput != ''):
        nrchars = len(passwordinput)
        generatedsecurestrings = GenerateSecureString()
        passwordtbsecured = passwordinput

        #random caputaliztion
        randnr1 = random.randint(0, nrchars - 1)
        randnr2 = random.randint(0, nrchars - 1)
        passwordtbsecured = ''.join([passwordtbsecured[:randnr1], passwordtbsecured[randnr1].upper(), passwordtbsecured[randnr1 + 1:]])
        passwordtbsecured = ''.join([passwordtbsecured[:randnr2], passwordtbsecured[randnr2].upper(), passwordtbsecured[randnr2 + 1:]])

        #print(passwordtbsecured)
        #print(generatedsecurestrings[0][2])

        #adding 2 random digits
        randnr1 = random.randint(0, nrchars - 1)
        ##randnr2 = random.randint(0, nrchars - 1)
        randomdigit = random.randint(0, 1000)
        randomdigit = str(randomdigit)
        passwordtbsecured = ''.join([passwordtbsecured[:randnr1 + 1], randomdigit, passwordtbsecured[randnr1 + 1:]])
        ##passwordtbsecured = ''.join([passwordtbsecured[:randnr2 + 1], passwordtbsecured[randnr2].upper(), passwordtbsecured[randnr2 + 1:]])

        #adding 2 random symbols
        randnr1 = random.randint(0, nrchars - 1)
        randnr2 = random.randint(0, nrchars - 1)
        passwordtbsecured = ''.join([passwordtbsecured[:randnr1 + 1], generatedsecurestrings[2][0], passwordtbsecured[randnr1 + 1:]])
        passwordtbsecured = ''.join([passwordtbsecured[:randnr2 + 1], generatedsecurestrings[2][1], passwordtbsecured[randnr2 + 1:]])

        #print(passwordtbsecured)


        nrcharsupdated = len(passwordtbsecured)

        if (nrcharsupdated == 0):
            #if empty input try catch before here and generate a totally new pass
            pass
        elif(nrcharsupdated < 5):
            print('The pass is less than 5 characters long. Perfoming step 2..')
            f = open('10letterwords.txt','r',encoding='utf-8')
            content = f.readline()
            f.close()
            splitcontent = content.split(',')
            lencontent =  len(splitcontent)

            #print('Number of words in wordlist is: ' + str(lencontent-1))
            #get a random number
            randnr = random.randint(0, len(splitcontent) - 2)
            #print(splitcontent[randnr])
            passwordtbsecured = passwordtbsecured + splitcontent[randnr]
            print('Your pass is now secure')
            print('The pass is:')
            print(passwordtbsecured)



        elif(nrcharsupdated >= 5 and nrcharsupdated < 12):
            #print('The pass is less than 12 characters long. Perfoming step 2..')
            #open 6 letter words or sth and choose a random word

            f = open('6letterwords.txt','r',encoding='utf-8')
            content = f.readline()
            f.close()
            splitcontent = content.split(',')
            lencontent =  len(splitcontent)

            #print('Number of words in wordlist is: ' + str(lencontent-1))
            #get a random number
            randnr = random.randint(0, len(splitcontent) - 2)
            #print(splitcontent[randnr])
            passwordtbsecured = passwordtbsecured + splitcontent[randnr]
            print('Your pass is now secure')
            print('The pass is:')
            print(passwordtbsecured)

        else:
            print('Your pass is now secure')
            print('The pass is:')
            print(passwordtbsecured)

     elif(passwordinput == ''):
        print('We are generating a totally new password for you..')
        #word1
        f = open('10letterwords.txt','r',encoding='utf-8')
        content = f.readline()
        f.close()
        splitcontent = content.split(',')
        lencontent =  len(splitcontent)

        #print('Number of words in wordlist is: ' + str(lencontent-1))
        #get a random number
        randnr = random.randint(0, len(splitcontent) - 2)
        word1 = splitcontent[randnr]

        #word2
        f = open('5letterwords.txt','r',encoding='utf-8')
        content = f.readline()
        f.close()
        splitcontent = content.split(',')
        lencontent =  len(splitcontent)

        #print('Number of words in wordlist is: ' + str(lencontent-1))
        #get a random number
        randnr = random.randint(0, len(splitcontent) - 2)
        word2 = splitcontent[randnr]


        #word3
        f = open('4letterwords.txt','r',encoding='utf-8')
        content = f.readline()
        f.close()
        splitcontent = content.split(',')
        lencontent =  len(splitcontent)

        #print('Number of words in wordlist is: ' + str(lencontent-1))
        #get a random number
        randnr = random.randint(0, len(splitcontent) - 2)
        word3 = splitcontent[randnr]

        passwordtbsecured = word1 + word2 + word3
        nrchars = len(passwordtbsecured)
        generatedsecurestrings = GenerateSecureString()


        #randomization process

        randnr1 = random.randint(0, nrchars - 1)
        randnr2 = random.randint(0, nrchars - 1)
        passwordtbsecured = ''.join([passwordtbsecured[:randnr1], passwordtbsecured[randnr1].upper(), passwordtbsecured[randnr1 + 1:]])
        passwordtbsecured = ''.join([passwordtbsecured[:randnr2], passwordtbsecured[randnr2].upper(), passwordtbsecured[randnr2 + 1:]])

        #print(passwordtbsecured)
        #print(generatedsecurestrings[0][2])

        #adding 2 random digits
        randnr1 = random.randint(0, nrchars - 1)
        ##randnr2 = random.randint(0, nrchars - 1)
        randomdigit = random.randint(0, 1000)
        randomdigit = str(randomdigit)
        passwordtbsecured = ''.join([passwordtbsecured[:randnr1 + 1], randomdigit, passwordtbsecured[randnr1 + 1:]])
        ##passwordtbsecured = ''.join([passwordtbsecured[:randnr2 + 1], passwordtbsecured[randnr2].upper(), passwordtbsecured[randnr2 + 1:]])

        #adding 2 random symbols
        randnr1 = random.randint(0, nrchars - 1)
        randnr2 = random.randint(0, nrchars - 1)
        passwordtbsecured = ''.join([passwordtbsecured[:randnr1 + 1], generatedsecurestrings[2][0], passwordtbsecured[randnr1 + 1:]])
        passwordtbsecured = ''.join([passwordtbsecured[:randnr2 + 1], generatedsecurestrings[2][1], passwordtbsecured[randnr2 + 1:]])



        print('The generated secure pass is:')
        print(passwordtbsecured)






def GenerateSecureString():
    global smallletters
    global capletters
    global symbols
    smallletterslist = []
    capletterslist = []
    symbolslist = []

    for char in smallletters:
        smallletterslist.append(char)

    for char in capletters:
        capletterslist.append(char)

    for char in symbols:
        symbolslist.append(char)


    random.shuffle(smallletterslist)
    rndmsmlltrs = ''.join(smallletterslist)

    random.shuffle(capletterslist)
    rndmcaplltrs = ''.join(capletterslist)

    random.shuffle(symbolslist)
    rndmsymbols = ''.join(symbolslist)

    return [smallletterslist,capletterslist,symbolslist]




def StartApp():
    GetInput()

#program
StartApp()
