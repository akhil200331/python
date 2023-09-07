n=int(input('enter the no of word to enter: '))
list=[]
listnew=[]
for i in range(n):
    list.append(input())
list.sort()
for j in list:
    if j not in listnew:
        listnew.append(j)
print("the word without duplicate words in sort form:")
for x in listnew:
    print(x)
