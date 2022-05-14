import random


file = open('Words.txt','r',encoding='utf-8')
words = file.readlines();
loop = True
letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',]
Wordle = ['@','@','@','@','@']
check = 0
while True:
    possible = [];
    possible = [];
    for i in range(5):
        resp = input('LETTER %s : '%str(i+1))
        if '+' in resp:
            new = resp.replace('+','');
            Wordle[i] = new;
            check+=1
        if '-' in resp:
            new = resp.replace('-','')
            letters.remove(new)


    for word in words:
        match = 0
        word = word.replace('\n','')
        strip = list(word);
        for i in range(5):
            if strip[i] == Wordle[i]:
                match+=1
        if match == check:
            possible.append(word)
    for poss in possible:
        strip = list(poss)
        for i in range(5):
            if strip[i] not in letters:
                possible.remove(poss)
                break
    print('POSSIBLILTIES : %s'%len(possible))
    if (len(possible) <= 20):
        print(possible)
        
    else:
        pick = [];
        for i in range(5):
            ran = random.randrange(0,len(possible))
            pick.append(possible[ran])
        print(pick); 
    print(Wordle);
    print(letters);
