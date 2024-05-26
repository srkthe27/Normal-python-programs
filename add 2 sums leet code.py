l1 = [2,4,3]
l2 = [5,6,4]
l1.reverse()
l2.reverse()
num1 = 0
num2 = 0
for i in l1:
    num1 = num1*10+i 
for i in l2:
    num2 = num2*10+i
summ = num1+num2
l3 = []
while (summ>0):
    a = summ%10
    summ = summ//10
    l3.append(a)
print(l3)
