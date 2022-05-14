import itertools
import enchant

d1 = enchant.Dict("en_UK")

chrs = 'abcdefghijklmnopqrstuvwxyz'
n = 5

file = open('Words.txt','a')
for w in itertools.product(chrs,repeat=n):
    word = (''.join(w))
    if (d1.check(word) == True):
        file.write(word + '\n');
        print(word)
    

    
    
    

print('ALL WORDS DONE')
file.close();