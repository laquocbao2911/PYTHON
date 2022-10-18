def tinhtoan(charac):
    pytha = {1:['A','J','S'],2:['B','K','T'],3:['C','L','U'],4:['D','M','V']
    ,5:['E','N','W'],6:['F','O','X'],7:['G','P','Y'],8:['H','Q','Z'],9:['I','Z']}
    for i in pytha.keys():
        for j in pytha[i]:
            if charac == j:
                return i

inp = (input("Enter name: ")).upper()
lst =[]
for i in inp:
    lst.append(i)
for j in lst:
    if j == " ":
        lst.remove(j)
# Câu 8d
name = inp.split(" ")[-1]
dic8d = ['A','Ă','Â','E','Ê','I','O','Ô','Ơ','U','Ư','Y']
check = 0
for k in dic8d:
    for n in name:
        if n == k:
            print("Soul number = %d"%(tinhtoan(n)))
            check+=1
        if check ==1:
            break
        
