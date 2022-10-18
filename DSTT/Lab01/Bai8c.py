def tinhtoan(charac, num,sum):
    pytha = {1:['A','J','S'],2:['B','K','T'],3:['C','L','U'],4:['D','M','V']
    ,5:['E','N','W'],6:['F','P','X'],7:['G','P','Y'],8:['H','Q','Z'],9:['I','Z']}
    for i in pytha.keys():
        for j in pytha[i]:
            if charac == j:
                sum = sum + (i*num)
    return sum

def cat(num):
    sum =0
    int(num)
    while(num!=0):
        temp = num%10
        sum += temp
        num = int(num/10)
    return sum

inp = input("Enter name: ").upper()
lst =[]
for i in inp:
    lst.append(i)
for j in lst:
    if j == " ":
        lst.remove(j)
count = {}
for k in lst:
    if k in count:
        count[k] +=1
    else:
        count[k] = 1
result = 0
for i in count.keys():
    result = tinhtoan(i,count[i],result)
if result >= 22:
    result = cat(result)
print("Destiny number = %d"%(result))
