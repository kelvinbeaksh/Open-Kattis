from collections import defaultdict
grammer_dict = {"number of":{"c"},"amount of":{"m"},"most":{"c","m"},"fewest":{"c"},"least":{"m"},"more":{"c","m"},"fewer":{"c"},"less":{"m"},"many":{"c"},"much":{"m"},"few":{"c"},"little":{"m"}}

noun_dict = defaultdict(lambda:None)
n,p = map(int,input().split())
for _ in range(n):
    noun,d = map(str,input().split(" "))
    noun_dict[noun] = d
for _ in range(p):
    line = list(map(str,input().split(" ")))
    grammer,noun = " ".join(line[0:len(line)-1]),line[-1]
    
    if noun_dict[noun] in grammer_dict[grammer]:
        print("Correct!")
    else:
        print("Not on my watch!")
