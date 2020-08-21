from telnetlib import DO


thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple,'\n')

for a in thistuple:
    print(a)
    
print()

for a in thistuple:
    print(a,end='')
    
print('\n')

for a in thistuple:
    print(a,',',end='')
      
print('\n')

for a in thistuple:
    print(a,end='')
    if a!=thistuple[len(thistuple)-1]:
        print(',',end='')
      
print('\n')
  
i=0;
while i<len(thistuple):
    print(thistuple[i],end='')
    if i<len(thistuple)-1:
        print(',',end='')
    i+=1
      
print('\n')

'''Python don't have do while loop'''
'''one has to create a customized one like shown below'''
  
i=0;
while True:
    print(thistuple[i],end='')
    if i<len(thistuple)-1:
        print(',',end='')
    if i==len(thistuple)-1:
        break;
    i+=1