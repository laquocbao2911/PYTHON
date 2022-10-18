def cat(num):
    sum =0
    int(num)
    while(num!=0):
        temp = num%10
        sum += temp
        num = int(num/10)
    return sum

inp = input("Mời bạn nhập ngày tháng năm sinh (Cách nhau dấu /) : ")
date = inp.split("/")
# Câu a
caua = cat(int(date[0])) + cat(int(date[1])) + cat(int(date[2]))
if caua>11:
    caua = cat(caua)
print("Your life path number/ master number = %d"%(caua))
# Câu b
caub = cat(int(date[0])) + cat(int(date[1])) + cat(2022)
if caub>9:
    caub = cat(caub)
print("Personal year number = %d"%(caub))
