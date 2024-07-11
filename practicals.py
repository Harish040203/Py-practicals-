numbers=[21,34,54,12]
print("list:",numbers)
#using remove method
numbers.remove(34)
print("after remove",numbers)
#using insert
numbers.insert(4,69)
print("after insert",numbers)
#append
numbers.append(663)
print("after append ",numbers)
#len
length=len(numbers)
print("length is ", length)
#pop
numbers.pop()
print("last value is removed ",length)
#clear
numbers.clear()
print("list is cleared ",length)
#_____________________________________________________________________________________________________________________
def prin():
    rows = 5
 
    for i in range(1, 6):
        print("*"* i)
    
    for i in range(rows-1,0,-1):
        print('*' * i)

prin()
#_____________________________________________________________________________________________________________________
a = int(input("enter an number"))
b = int(input("enter an number"))
add = a+b;
multiply=a*b;
divide=a/b;
sub=a-b;
print(add)
print(sub)
print(multiply)
print(divide)
#_________________________________________________________________________________________________________________________
import datetime
now=datetime.datetime.now()
print("current date and time")
print(now.strftime("%Y-%m-%d%H:%M:%S"))
print(now.strftime("%d-%m-%Y%I:%M:%S%p"))
print(now.strftime("%a-%b-%d%Y"))
print(now.strftime("%c"))























