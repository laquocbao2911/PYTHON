def tinhtoan(charac,result):
    pytha = {1:['A','J','S'],2:['B','K','T'],3:['C','L','U'],4:['D','M','V']
    ,5:['E','N','W'],6:['F','O','X'],7:['G','P','Y'],8:['H','Q','Z'],9:['I','Z']}
    for i in pytha.keys():
        for j in pytha[i]:
            if charac == j:
                result += i
    return result

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
# Câu 8d
name = inp.split(" ")[-1]
dic8e = ['A','Ă','Â','E','Ê','I','O','Ô','Ơ','U','Ư','Y']
check = 0
check1=0
sum = 0
# Các kí tự không thuộc table 3
for h in name:
    for m in dic8e:
        if h == m:
            check+=1
    if check == 0:
        sum = tinhtoan(h,sum)
        break
# Các kí tự thuộc table 3
for k in dic8e:
    for n in name:
        if n == k:
            check+=1
            if check > 1:
                sum = tinhtoan(n,sum)
                break

if sum > 11:
    print("Impression number = %d"%(cat(sum)))