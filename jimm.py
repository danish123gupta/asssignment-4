#q.no.1
lst=[10,20,30,'danish','ramesh','suresh']
lst.reverse()
print(lst)

#q.no.2
str="hello my name is danish"
for i in str:
    if i==i.upper():
        print(i,end=" ",sep=" ")
print(str)


#q.no.3
string=(input("enter some elements separated by commas")).split(",")
w=list(string)
print(w)

#q.no.4
x=input("enter number:")
if x[::-1]==x:
    print("num is palindrome")
else:
    print("num not palindrome")

#q.no.5
x=['python','java','pshell','hard']
id(x)
print(id(x))
p=x
id(p)
print(id(p))
s=x.copy()
id(s)
print(id(s))
del x[-1]
print(x)
print(p)
print(s)
#x and y is the shallow copy
#p is the deep copy


