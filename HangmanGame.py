import random
import Hangmanstages
words=['apple','table','home','laptop','glass','mobile','bike','watch','bottle']
random_word=random.choice(words)
randlist=[]
list=[]
life=6
for i in range(len(random_word)):
    randlist+=random_word[i]
    list+='_'

print("-----------------Guse the word.-----------------\n")
print(list,"\n")
while life != 0:
    print(Hangmanstages.stage[life])
    print(f"you have {life} chance left :\n")
    ch=input("Enter a charecter to choose : ").lower()
    for i in range(len(random_word)):
        if random_word[i] == ch:
            list[i] = ch
    if ch not in random_word:
        print("You lost 1 life.")
        life-=1
    print("\n",list,"\n")
    if '_' not in list:
        print("\n-------Congratulation you gussed it right.-------")
        break
if life == 0:
    print("You have 0 chance left.")
    print(Hangmanstages.stage[0])
    print("You totally lose.")      