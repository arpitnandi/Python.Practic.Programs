f=int(input('Enter the first number: '))
l=int(input('Enter the last number: '))

numbers={}
prime=[]

def numbers(a):
    j=2
    while a>=2 and j<=a:
        if not a%j==0:
            j+=1
        elif a==j and a%j==0:
            prime.append(a)

for i in range(f,l+1):
    numbers(i)
                 
for i in prime:
    print(i,'is prime number')

