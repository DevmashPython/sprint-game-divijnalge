import msvcrt
import time

finish=10
count=0
count1=0
count2=0
m=0
print"press enter"
raw_input()
s_time=time.time()
print"move to the right"

while(1):
    key=msvcrt.getch()
    if key!='d':
        m=1
        print"\nGAME OVER"
        break
    if key=='d':
        count=count+1
        print"-->",
        if count==finish:
            break
if m==0:
    print"move down"
while(1):
    if m==1:
        break
    key1=msvcrt.getch()
    if key1!='s':
        m=1
        print"\nGAME OVER"
        break
    if key1=='s':
        count1 = count1 + 1
        print"\t\t\t\t\t|\n"
        if count1==finish:
            break
if m==0:
    print "\t\t\t\t\tmove right"
while(1):
    if m==1:
        break
    key2=msvcrt.getch()
    if key2!='d':
        m=1
        print"\nGAME OVER"
        break
    if key2=='d':
        count2=count2+1
        if count2==1:
            print"\t\t\t\t\t-->",
        if count2==15:
            break
        if count2>1:
            print"-->",
        
time_elap=time.time()-s_time
if m==0:
    print"\nCongrats you have finished the game"
    print "\nTime taken is " +str(round(time_elap))
