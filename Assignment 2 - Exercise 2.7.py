# 2.8

Hour=[0,5,10,15]
Bacteria=[]
for h in Hour:
    B=200*2**h
    Bacteria.append(B)

print('Hour'+ '\t'+ 'Number of Bacteria')
for i in range(len(Hour)):
    print(Hour[i],'\t',Bacteria[i])

print('Hour'+ '\t'+ 'Number of Bacteria')
for i in range(len(Hour)):
    print('{:>4d}\t{:>18d}'.format(Hour[i],Bacteria[i]))

# 2.12
o=10
ps=[0.03,0.03,0.03,0.03,0.03,-0.03,-0.03]
ns=[1]
for i in range(1,len(ps)):
    if ps[i]*ps[i-1]<0:
        ns.append(1)
    else:
        ns.append(ns[-1]+1)

for i in range(len(ps)):
    p=ps[i]
    n=ns[i]
    w=o*(1+p)**n
    print(w)
    o=w

# 3.1
passes = 0 
failures = 0 
while 1:
    result = input('Enter result (1=pass, 2=fail): ')
    if result in ['1','2']:
        if result == '1':
            passes = passes + 1
        else:
            failures = failures + 1
        if passes+failures==10:
            break
    else:
        print('Please enter a correct value.')
print('Passed:', passes)
print('Failed:', failures)
if passes > 8:
    print('Bonus to instructor')


# 3.6

while 1:
    question=input( 'What is your problem?')
    ever=input('Have you had this problem before (yes or no)?' )
    if ever='yes':
        print('Well, you have it again.')
    else:
        print('Well, you have it now.')
## No, because the computer answers the question the same way every time

# 3.10

o=10
ps=[0.03 for i in range(10)]
ns=[1]
for i in range(1,len(ps)):
    if ps[i]*ps[i-1]<0:
        ns.append(1)
    else:
        ns.append(ns[-1]+1)

for i in range(len(ps)):
    p=ps[i]
    n=ns[i]
    w=o*(1+p)**n
    print(w)
    o=w



## 3.16
speeds=[]
for i in range(1,11):
    speed=eval(input("Please input No.{i} runner's speed(m/sec)"))
    speeds.append(speed)
speeds=sorted(speeds)
print(f"The fastest runner's speed is {speeds[-1]}m/sec")
print(f"The second fastest runner's speed is {speeds[-2]}m/sec")



## 4.9
import math
for degrees in range(1,181):
    rad=degrees*math.pi/180
    print(f'degrees={degrees}   rad={rad:.2f}')

# 4.12
import random

def racehare():
    num=random.randint(1,10)
    if 1<=num<=2:
        return 0
    elif 3<=num<=4:
        return 9
    elif 5<=num<6:
        return -12
    elif 6<=num<=8:
        return 1
    elif 9<=num<=10:
        return -2

def racetortoise():
    num=random.randint(1,10)
    if 1<=num<=5:
        return 3
    elif 6<=num<=7:
        return -6
    elif 8<=num<=10:
        return 1

print("""BANG !!!!!
AND THEY'RE OFF !!!!!""")
T=0
H=0
while 1:
    t=racetortoise()
    h=racehare()
    T+=t
    H+=h
    
    T=max(0,T)
    H=max(0,H)
    T=min(69,T)
    H=min(69,H)
    line=' '*70
    if T==H:
        
        ls=list(line)
        ls[T]='OUCH!!!'
        print(''.join(ls))
    else:
        ls=list(line)
        ls[T]='T'
        ls[H]='H'
        print(''.join(ls))
    if T==69 and H==69:
        print('TORTOISE WINS!!! YAY!!! ')
        break
    elif T==69:
        print('TORTOISE WINS!!! YAY!!! ')
        break
    elif H==69:
        print('Hare wins')
        break

