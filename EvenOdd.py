import time;
print 'Check whether numbers are even or odd'
time.sleep(1)
num=int(raw_input('How many numbers do you want to enter:'))
numlist=[]
EvenCount=0
OddCount=0
for i in range(num):
    no=int(raw_input('Enter your numbers:'))
    numlist.append(no)
    print (numlist)

print 'Counting Even and Odd'
time.sleep(1)
for i in range(num):
    if numlist[i]%2==0:
        EvenCount+=1
else:
        OddCount+=14

print 'Total Even Numbers:',EvenCount
print 'Total Odd Numbers:' ,OddCount