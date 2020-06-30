f=int(input('Enter the first number: '))
l=int(input('Enter the last number: '))
 
arm=[]

def armstrong(a):
    n=a
    digit=0
    summation=0
    while n>0:
        digit+=1
        n//=10
    while a>0:
        n=a//10
        a%=10
        summation+=a**digit
        a=n
    if summation==number:
        arm.append(summation)

for number in range(f,l+1):
    armstrong(number)
    
for value in arm:
    print(value,'is Armstrong number')