import random, time

while True:
    score = 0 # postavi rezultat

    number_of_digits = 1 # postavi n
    
    while True:
        out = ''
        digits = []
        for j in range(number_of_digits): # generiraj nasumični niz
            n = random.randint(0, 9)
            out += str(n) + ' '
            digits.append(n)
        print(out)
        time.sleep(3)
        for i in range(80):
            print()
        a = list(map(int, input().split()))
        if a == digits: # ispitanik odgovara točno
            score+=1
            number_of_digits+=1
        else: # ispitanik odgovara krivo
            print("Score:", score) 
            break

        
        