f=int(input('Enter the first number: '))
l=int(input('Enter the last number: '))

number={}

def numbers(a):
    devisers=[]
    j=2
    while a>=2:
        if a>=j and a%j==0:
            devisers.append(j)
            a/=j
        else:
            j+=1
    if len(devisers)>1:
        for v in devisers:
            number.setdefault(i,[]).append(v)

for i in range(f,l+1):
    numbers(i)

for i in number.keys():
        print(str(i)+' is multiple of '+str(number[i][0]),*number[i][1:len(number[i])],sep='*')

