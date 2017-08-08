li = [12,22,3,11,8,10]

for m in range(len(li)-1):
    for n in range(m+1,len(li)):
        if li[m] > li[n]:
            temp = li[n]
            li[n] = li[m]
            li[m] = temp
        print li



'''
for m in range(5):
    num1 = li[m]
    num2 = li[m+1]
    if num1 > num2:
        temp = li[m]
        li[m] = num2
        li[m+1] = temp
    print li

print '0_____'

for m in range(4):
    num1 = li[m]
    num2 = li[m+1]
    if num1 > num2:
        temp = li[m]
        li[m] = num2
        li[m+1] = temp
    print li

print '0_____'

for m in range(3):
    num1 = li[m]
    num2 = li[m+1]
    if num1 > num2:
        temp = li[m]
        li[m] = num2
        li[m+1] = temp
    print li
'''

for n in range(1,len(li)-1):
    for m in range(len(li)-n):
        num1 = li[m]
        num2 = li[m + 1]
        if num1 > num2:
            temp = li[m]
            li[m] = num2
            li[m + 1] = temp
print li