import string
from tabnanny import check

from pip import List;

chrs = list(string.ascii_uppercase)
chrs_In = [];
chrs_Out = [];
wordle = list('@@@@@')
same = 0



def checkSame():
    tries = [];
    with open('Words.txt','r',encoding='utf-8') as words:
        for word in words.readlines():
            snap = 0;
            for i in range(5):
               if (word[i] == wordle[i]):
                snap+=1
            if (snap == same):
                tries.append(word)
            snap = 0;
    checkIn(tries);

def checkIn(words):
    tries = [];
    for w in words:
        for i in range(5):
            if w[i] in chrs_In:
                tries.append(w);
    tries = list(dict.fromkeys(tries))
    checkOut(tries)

def checkOut(words):
    tries = words;
    for w in words:
        for i in range(5):
            if w[i] in chrs_Out:
                try:
                    tries.remove(w)
                except:
                    None;
    print(tries);
        

    




while True:
    for i in range(5):
        letter = input('Input Letter %s : '%(i+1));
        letter = letter.upper();
        if ('+' in letter):
            wordle[i] = letter.replace('+','')
            same+=1;
        elif ('-' in letter):
            chrs_Out.append(letter.replace('-',''))
        elif ('/' in letter):
            chrs_In.append(letter.replace('/',''))
    checkSame()