import random


liste = [1,2,3,4,5]
randomsayi = random.randint(0,13)

if randomsayi in liste:
    print('VAR -->', randomsayi)
else:
    print('YOK -->', randomsayi)